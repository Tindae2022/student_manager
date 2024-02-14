from django.db.models import Count
from django.http import JsonResponse
from academics.models import Student, Course, Lecturer, Semester
from issues.models import Issue
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    total_students = Student.objects.total_students()
    total_courses = Course.objects.total_courses()
    total_active_courses = Course.objects.total_active_courses()
    total_inactive_courses = Course.objects.total_inactive_courses()
    total_archived_courses = Course.objects.total_archived_courses()
    total_lecturers = Lecturer.objects.total_lecturers()
    total_active_semester = Semester.objects.total_active_semester()
    total_issues = Issue.objects.total_issues()
    pending_issues = Issue.objects.total_pending_issues()
    solved_issues = Issue.objects.total_solved_issues()
    unsolved_issues = Issue.objects.total_unsolved_issues()
    all_issues = Issue.objects.order_by('-date_reported')[:3]
    travel_category = Issue.objects.filter(category__icontains='travel').count()
    fees_category = Issue.objects.filter(category__icontains='fees').count()
    exam_category = Issue.objects.filter(category__icontains='exam').count()
    medical_category = Issue.objects.filter(category__icontains='medical').count()
    drugs_category = Issue.objects.filter(category__icontains='drugs').count()
    others_category = Issue.objects.filter(category__icontains='others').count()

    courses = Course.objects.all()

    course_labels = [course.name for course in courses]
    course_data = [Issue.objects.filter(student__course=course).count() for course in courses]

    labels = ['Pending', 'Solved', 'Unsolved', 'Total']
    data = [pending_issues, solved_issues, unsolved_issues, total_issues]

    cat_labels = ['Travel', 'Fees', 'Exam', 'Medical', 'Drugs', 'Others']
    cat_data = [travel_category, fees_category, exam_category, medical_category, drugs_category, others_category]

    context = {
        'total_students': total_students,
        'total_courses': total_courses,
        'total_active_courses': total_active_courses,
        'total_inactive_courses': total_inactive_courses,
        'total_archived_courses': total_archived_courses,
        'total_lecturers': total_lecturers,
        'total_active_semester': total_active_semester,
        'total_issues': total_issues,
        'all_issues': all_issues,
        'solved_issues': solved_issues,
        'pending_issues': pending_issues,
        'unsolved_issues': unsolved_issues,
        'bar_chart_data': {
            'labels': labels,
            'data': data,
            'course_labels': course_labels,
            'course_data': course_data,
        },
        'category_barchart': {
            'labels': cat_labels,
            'data': cat_data,
        },

    }

    return render(request, 'admin/dashboard.html', context)
