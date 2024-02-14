from django.db import models
from .queryset import (ClassQueryset, CourseQueryset, LecturerQueryset,
                       ModuleQueryset,
                       StudentQueryset, SemesterQueryset, AppraisalQueryset

                       )


class ClassManagers(models.Manager):

    def get_queryset(self):
        return ClassQueryset(self.model, using=self._db).all()

    def all_classes(self):
        return self.get_queryset().all_classes()

    def search_classes(self, query):
        return self.get_queryset().search_classes(query)

    def all_active_classes(self):
        return self.get_queryset().all_active_classes()

    def all_inactive_classes(self):
        return self.get_queryset().all_inactive_classes()

    def all_archived_classes(self):
        return self.get_queryset().all_archived_classes()


class SemesterManagers(models.Manager):

    def get_queryset(self):
        return SemesterQueryset(self.model, using=self._db).all()

    def get_all_semester(self):
        return self.get_queryset().get_all_semester()

    def get_active_semester(self):
        return self.get_queryset().get_all_active_semester()

    def total_active_semester(self):
        return self.get_queryset().total_active_semester()

    def get_inactive_semester(self):
        return self.get_queryset().get_inactive_semester()

    def get_archived_semester(self):
        return self.get_queryset().get_archived_semester()

    def search_semester(self, query):
        return self.get_queryset().search_semester(query)


class StudentManagers(models.Manager):

    def get_queryset(self):
        return StudentQueryset(self.model, using=self._db).all()

    def get_all_students(self):
        return self.get_queryset().get_all_students()

    def search_student(self, query):
        return self.get_queryset().search_student(query)

    def total_students(self):
        return self.get_queryset().total_students()


class AppraisalManagers(models.Manager):

    def get_queryset(self):
        return AppraisalQueryset(self.model, using=self._db).all()

    def get_all_appraisal(self):
        return self.get_queryset().get_all_appraisal()

    def search_appraisal(self, query):
        return self.get_queryset().search_appraisal(query)


class ModuleManagers(models.Manager):

    def get_queryset(self):
        return ModuleQueryset(self.model, using=self._db).all()

    def all_modules(self):
        return self.get_queryset().all_modules()

    def search_module(self, query):
        return self.get_queryset().search_module(query)

    def all_active_modules(self):
        return self.get_queryset().all_active_modules()

    def all_inactive_modules(self):
        return self.get_queryset().all_inactive_modules()

    def all_archived_modules(self):
        return self.get_queryset().all_archived_modules()


class LecturerManagers(models.Manager):

    def get_queryset(self):
        return LecturerQueryset(self.model, using=self._db).all()

    def all_lecturers(self):
        return self.get_queryset().all_lecturers()

    def search_lecturer(self, query):
        return self.get_queryset().search_lecturer(query)

    def get_lecturers_for_a_specific_modules(self, query):
        return self.get_queryset().get_lecturers_for_a_specific_modules(query)

    def total_lecturers(self):
        return self.get_queryset().total_lecturers()


class CourseManagers(models.Manager):

    def get_queryset(self):
        return CourseQueryset(self.model, using=self._db).all()

    def get_all_courses(self):
        return self.get_queryset().get_all_courses()

    def search_course(self, query):
        return self.get_queryset().search_course(query)

    def get_active_courses(self):
        return self.get_queryset().get_active_courses()

    def get_inactive_courses(self):
        return self.get_queryset().get_inactive_courses()

    def get_archived_courses(self):
        return self.get_queryset().get_archived_courses()

    def total_courses(self):
        return self.get_queryset().total_courses()

    def total_active_courses(self):
        return self.get_queryset().total_active_courses()

    def total_inactive_courses(self):
        return self.get_queryset().total_inactive_courses()

    def total_archived_courses(self):
        return self.get_queryset().total_archived_courses()
