from django.contrib import admin
from .models import (Class, Module, Lecturer, Course, Student,
                     Semester, Appraisal, Enrollment, ClassRoom, TimeTable)


# Register your models here.
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    pass


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    pass


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(Appraisal)
class AppraisalAdmin(admin.ModelAdmin):
    pass


@admin.register(ClassRoom)
class ClassRoomsAdmin(admin.ModelAdmin):
    pass


@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    pass
