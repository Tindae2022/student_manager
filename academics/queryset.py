from django.db import models
from django.db.models import Q


class SemesterQueryset(models.QuerySet):
    def get_all_semester(self):
        return self.all()

    def get_active_semester(self):
        return self.filter(status='active')

    def get_inactive_semester(self):
        return self.filter(status='inactive')

    def total_active_semester(self):
        return self.filter(status='active').count()

    def get_archived_semester(self):
        return self.filter(status='archived')

    def search_semester(self, query):
        return self.filter(name__icontains=query) | models.Q(status__icontains=query)


class StudentQueryset(models.QuerySet):

    def get_all_students(self):
        return self.all()

    def search_student(self, query):
        queryset = self.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(student_id__icontains=query) |
            Q(semester__name__icontains=query) |
            Q(course__name__icontains=query) |
            Q(student_class__name__icontains=query)
        )
        return queryset

    def total_students(self):
        return self.all().count()


class AppraisalQueryset(models.QuerySet):
    def get_all_appraisal(self):
        return self.all()

    def search_appraisal(self, query):
        return (self.filter(student__icontains=query) | models.Q(student_id__icontains=query) |
                models.Q(lecturer__icontains=query))


class CourseQueryset(models.QuerySet):

    def get_all_courses(self):
        return self.all()

    def search_course(self, query):
        return self.filter(name__icontains=query) | models.Q(code__icontains=query)

    def get_active_courses(self):
        return self.filter(status='active')

    def get_inactive_courses(self):
        return self.filter(status='inactive')

    def get_archived_courses(self):
        return self.filter(status='archived')

    def total_courses(self):
        return self.all().count()

    def total_active_courses(self):
        return self.filter(status='active').count()

    def total_inactive_courses(self):
        return self.filter(status='inactive').count()

    def total_archived_courses(self):
        return self.filter(status='archived').count()


class ModuleQueryset(models.QuerySet):

    def all_modules(self):
        return self.all()

    def search_module(self, query):
        return self.filter(
            models.Q(name__icontains=query) |
            models.Q(code__icontains=query)
        )

    def all_active_modules(self):
        return self.filter(status='active')

    def all_inactive_modules(self):
        return self.filter(status='inactive')

    def all_archived_modules(self):
        return self.filter(status='archived')


class LecturerQueryset(models.QuerySet):

    def all_lecturers(self):
        return self.all()

    def search_lecturer(self, query):
        return self.filter(name__icontains=query)

    def get_lecturers_for_a_specific_modules(self, query):
        return self.filter(modules__in=query)

    def total_lecturers(self):
        return self.all().count()


class ClassQueryset(models.QuerySet):

    def all_classes(self):
        return self.all()

    def search_classes(self, query):
        return self.filter(name__icontains=query)

    def all_active_classes(self):
        return self.filter(status='active')

    def all_inactive_classes(self):
        return self.filter(status='inactive')

    def all_archived_classes(self):
        return self.filter(status='archived')
