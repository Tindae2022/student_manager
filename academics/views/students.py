from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import (ListView, DetailView,
                                  DeleteView, CreateView, UpdateView, TemplateView)
from weasyprint import HTML

from academics.models import Student, Class, Course, Semester
from academics.forms import StudentForm, StudentUpdateForm, StudentEmailForm, CSVImportForm
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from issues.models import Issue
from django.http import HttpResponse
from django.template.loader import get_template
from itertools import groupby
from operator import attrgetter
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
import csv
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student/index.html'
    context_object_name = 'students'
    ordering = ['-first_name']
    paginate_by = 10

    def get_queryset(self):
        return Student.objects.get_all_students()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_students'] = 'All Students'
        return context


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'student/student_details.html'
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.object
        issues = Issue.objects.filter(student=student)
        context['students'] = 'Student Details'
        context['issues'] = issues

        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_create.html'

    def get_success_url(self):
        return reverse_lazy('student_create_success')


class StudentSuccessTemplateView(TemplateView):
    template_name = 'student/success.html'


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentUpdateForm
    template_name = 'student/student_update.html'
    success_url = reverse_lazy('student_create_success')


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'student/student_confirm_delete.html'
    success_url = reverse_lazy('student_delete_success')
    context_object_name = 'student'


class StudentDeleteSuccessTemplateView(TemplateView):
    template_name = 'student/delete_success.html'


class StudentSearchView(LoginRequiredMixin, ListView):
    template_name = 'student/index.html'
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = 'Search Result(s)'
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        search_term = request.POST.get('search_term', '')
        search_students = Student.objects.search_student(search_term)
        context = {'students': search_students, 'search_term': search_term}

        return render(request, self.template_name, context)


'''
class SendEmailView(FormView):
    template_name = 'student/send_email.html'
    form_class = StudentEmailForm
    success_url = reverse_lazy('student_index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        student_email = self.kwargs.get('student_email')
        student = get_object_or_404(Student, email=student_email)
        kwargs['initial']['recipient'] = student.email
        return kwargs

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        recipient = form.cleaned_data['recipient']

        send_mail(subject, message, 'alusinelavalie80@gmail.com', [recipient])
        messages.success(self.request, 'Email Sent Successfully')

        # Pass student_email to the template
        student_email = self.kwargs.get('student_email')
        context = {
            'form': form,
            'student_email': student_email
        }

        return render(self.request, self.template_name, context)
'''


def send_email_view(request, pk):
    template_name = 'student/send_email.html'
    success_url = reverse('student_index')

    if request.method == 'POST':
        form = StudentEmailForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                student = Student.objects.get(pk=pk)
                recipient = student.email
            except Student.DoesNotExist:
                messages.error(request, 'Student not found')
                return redirect(success_url)

            send_mail(subject, message, 'alusinelavalie80@gmail.com', [recipient])
            messages.success(request, 'Email sent successfully')
            return redirect(success_url)
    else:
        form = StudentEmailForm()

    context = {
        'form': form,
    }

    return render(request, template_name, context)


'''

class StudentPDFView(DetailView):
    model = Student
    template_name = 'student/pdf.html'

    def render_to_response(self, context, **response_kwargs):
        # Setup PDF response
        pdf_response = HttpResponse(content_type='application/pdf')
        pdf_response['Content-Disposition'] = f"filename='{context['student'].first_name}_details.pdf'"

        # Create PDF canvas
        buffer = BytesIO()
        canvas_pdf = canvas.Canvas(buffer, pagesize=letter)

        # Draw Logo
        logo_path = 'academics/static/images/lim_logo.png'
        logo = ImageReader(logo_path)
        canvas_pdf.drawImage(logo, 400, 750, width=100, height=50, mask='auto')

        # Draw Heading
        self.draw_heading(canvas_pdf, 'Student Details')

        # Draw Student Details
        self.draw_student_details(canvas_pdf, context)

        # Draw Issue Details
        self.draw_issue_details(canvas_pdf, context)

        # Save PDF
        canvas_pdf.showPage()
        canvas_pdf.save()

        # Get the value of the BytesIO buffer and return the response
        pdf_response.write(buffer.getvalue())
        buffer.close()

        return pdf_response

    def draw_heading(self, canvas_pdf, heading_text):
        canvas_pdf.setFont("Helvetica-Bold", 16)
        canvas_pdf.drawString(100, 750, heading_text)

    def draw_student_details(self, canvas_pdf, context):
        canvas_pdf.drawString(10, 800, 'Student Details:')
        y_position = 750
        details = [
            f"Name: {context['student'].first_name} {context['student'].last_name}",
            f"Student ID: {context['student'].student_id}",
            f"Course: {context['student'].course}",
            f"Semester: {context['student'].semester}",
            f"Class: {context['student'].student_class}",
            f"Email: {context['student'].email}",
        ]

        for detail in details:
            canvas_pdf.drawString(10, y_position, detail)
            # y_position -= self.get_line_height(detail)
            y_position -= 20
            y_position -= 15



    def draw_issue_details(self, canvas_pdf, context):
        canvas_pdf.drawString(10, 700, "Issue Details:")
        issues = context['student'].issue_set.all()
        y_position = 680

        for i, issue in enumerate(issues):
            canvas_pdf.drawString(10, y_position, f"Issue {i + 1}: {issue.title}")
            canvas_pdf.drawString(10, y_position - 20, f"Category: {issue.category}")
            canvas_pdf.drawString(10, y_position - 40, f"Status: {issue.status}")
            canvas_pdf.drawString(10, y_position - 60, f"Date Reported: {issue.date_reported.strftime('%b. %d, %Y, %I:%M %p')}")
            canvas_pdf.drawString(10, y_position - 80, f"Description: {issue.description}")
            y_position -= 80
            y_position -= 20

    def get_line_height(self, text):
        base_height = 12  # Base height without considering text length
        additional_height_per_char = 2  # Additional height for each character in text
        return base_height + additional_height_per_char * len(text)



class StudentPDFView(DetailView):
    model = Student
    template_name = 'student/pdf.html'

    def render_to_response(self, context, **response_kwargs):
        # Render HTML template
        template = get_template(self.template_name)
        html = template.render(context)

        # Create PDF
        pdf_response = HttpResponse(content_type='application/pdf')
        pdf_response['Content-Disposition'] = f"filename='{context['student'].first_name}_details.pdf'"

        # Use WeasyPrint to generate PDF
        HTML(string=html).write_pdf(pdf_response)

        return pdf_response
'''


class PdfView(LoginRequiredMixin, View):
    template_name = 'student/pdf.html'

    def get(self, request, student_id):
        # Assuming you want to generate a PDF for a specific student
        student = get_object_or_404(Student, pk=student_id)

        # Render HTML template
        template = get_template(self.template_name)
        html = template.render({'student': student})

        # Create PDF using WeasyPrint
        pdf_response = HttpResponse(content_type='application/pdf')
        pdf_response['Content-Disposition'] = f"filename={student.first_name}_issues_details.pdf"
        base_url = request.build_absolute_uri()
        HTML(string=html, base_url=base_url).write_pdf(pdf_response)
        return pdf_response


class StudentTableView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'student/table_view.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        students = Student.objects.all().order_by('student_class__name')

        students_by_class = groupby(students, key=attrgetter('student_class'))
        classes_with_students = [(class_instance, list(students)) for class_instance, students, in students_by_class]
        context['classes_with_students'] = classes_with_students
        return context


'''
@login_required
def import_csv(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                course_name = row['course']
                course_instance = get_object_or_404(Course, name=course_name)
                semester_name = row['semester']
                semester_instance = get_object_or_404(Semester, name=semester_name)
                class_name = row['student_class']
                class_instance = get_object_or_404(Class, name=class_name)

                Student.objects.create(
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    student_id=row['student_id'],
                    course=course_instance,
                    semester=semester_instance,
                    student_class=class_instance,
                    class_rep=row['class_rep'],
                    email=row['email']
                )
            return redirect('student_index')

    else:
        form = CSVImportForm()

    return render(request, 'student/import.html', {'form': form})
'''


@method_decorator([login_required], name='dispatch')
class ImportCSVView(View):
    template_name = 'student/import.html'

    def get(self, request):
        # Handle GET request
        form = CSVImportForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # Handle POST request
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
                csv_reader = csv.DictReader(csv_file)

                for row in csv_reader:
                    course_name = row['course']
                    course_instance = get_object_or_404(Course, name=course_name)
                    semester_name = row['semester']
                    semester_instance = get_object_or_404(Semester, name=semester_name)
                    class_name = row['student_class']
                    class_instance = get_object_or_404(Class, name=class_name)

                    Student.objects.create(
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        student_id=row['student_id'],
                        course=course_instance,
                        semester=semester_instance,
                        student_class=class_instance,
                        class_rep=row['class_rep'],
                        email=row['email']
                    )

                return redirect('student_index')

            except IntegrityError:
                # Handle IntegrityError, add a duplicate record error to the form
                form.add_error('csv_file', 'Duplicate records found. Please check your CSV file.')

        # If form is not valid or IntegrityError occurred, render the template with the form
        return render(request, self.template_name, {'form': form})
