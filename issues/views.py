import csv

from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View

from .models import Issue
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .forms import IssueForm, IssueUpdateForm
from django.urls import reverse_lazy
from academics.forms import CSVImportForm
from academics.models import Student, Module
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class IssueListView(LoginRequiredMixin, ListView):
    model = Issue
    template_name = 'issue/issue_index.html'
    context_object_name = 'issues'
    paginate_by = 10

    def get_queryset(self):
        return Issue.objects.all_issues()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titles'] = 'All Issues'
        return context


class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    template_name = 'issue/issue_create.html'
    form_class = IssueForm
    context_object_name = 'issue_create'

    def get_success_url(self):
        return reverse_lazy('issue_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create New Issue'
        return context


class IssueDetailView(LoginRequiredMixin, DetailView):
    model = Issue
    template_name = 'issue/issue_detail.html'
    context_object_name = 'issues'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue_context'] = 'Issue Details'

        return context


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    template_name = 'issue/issue_update.html'
    form_class = IssueUpdateForm
    context_object_name = 'update_issues'


class IssueDeleteView(LoginRequiredMixin, DeleteView):
    model = Issue
    template_name = 'issue/issue_confirm_delete.html'
    context_object_name = 'delete_issue'
    success_url = reverse_lazy('issue_index')


@method_decorator([login_required], name='dispatch')
class ImportIssueCSVView(View):
    template_name = 'issue/import.html'

    def get(self, request):
        form = CSVImportForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
                csv_reader = csv.DictReader(csv_file)

                for row in csv_reader:
                    student_id = row['student_id']
                    student_instance = get_object_or_404(Student, student_id=student_id)
                    module_name = row['module']
                    module_instance = get_object_or_404(Module, name=module_name)

                    Issue.objects.create(
                        student=student_instance,
                        module=module_instance,
                        title=row['title'],
                        category=row['category'],
                        description=row['description'],
                        status=row['status']
                    )

                return redirect('issue_index')

            except IntegrityError:
                form.add_error('csv_file',
                               'Error Occurred! Please check your csv file for duplicate errors '
                               'or incorrect field names.')

        return render(request, self.template_name, {'form': form})
