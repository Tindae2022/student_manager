from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User
from .mixins import TimestampedMixinModel
from .managers import (ClassManagers, SemesterManagers, StudentManagers, AppraisalManagers,
                       ModuleManagers, LecturerManagers, CourseManagers
                       )

# Create your models here.
CLASS_STATUS_CHOICES = [
    ('active', 'active'),
    ('inactive', 'inactive'),
    ('archived', 'archived')
]
COURSE_SHORT_CODE = [
    ('BSEM', 'BSEM'),
    ('BBIT', 'BBIT'),
    ('BIT', 'BIT'),
    ('BICT', 'BICT')
]

DAY_CHOICES = [
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday'),

]
TIME_CHOICES = [
    ('8:30am', '8:30am'),
    ('11:30am', '11:30am'),
    ('2:30pm', '2:30pm'),
    ('5:30pm', '5:30pm'),
    ('7:30pm', '7:30pm')

]


class Class(TimestampedMixinModel, models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=CLASS_STATUS_CHOICES, default='active')

    objects = ClassManagers()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.status}'

    @classmethod
    def create_class(cls, name, status, timetable):
        class_create = cls(name=name, status=status, timetable=timetable)
        class_create.save()
        return class_create

    def update_class(self, name=None, status=None, timetable=None):

        if name is not None:
            self.name = name

        if status is not None:
            self.status = status

        if timetable is not None:
            self.timetable = timetable

        self.save()

    def delete_class(self):
        self.delete()

    def pre_save(self):
        if not self.status:
            self.status = 'active'

    def post_save(self):
        print(f'Class {self.name} saved successfully')

    def save(self, *args, **kwargs):
        self.pre_save()
        super().save(*args, **kwargs)
        self.post_save()


class Semester(models.Model):
    name = models.CharField(max_length=225)
    status = models.CharField(max_length=20, choices=CLASS_STATUS_CHOICES, default='active')
    classes = models.ManyToManyField(Class)

    objects = SemesterManagers()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @classmethod
    def create_semester(cls, name, status, classes):
        semester = cls(name=name, status=status, classes=classes)
        semester.save()
        return semester

    def update_semester(self, name=None, status=None, classes=None):
        if name is not None:
            self.name = name

        if status is not None:
            self.status = status

        if classes is not None:
            self.classes = classes

        self.save()

    def delete_semester(self):
        self.delete()

    def pre_save(self):
        if not self.status:
            self.status = 'active'

    def post_save(self):
        print(f'Semester {self.name} saved successfully')

    def save(self, *args, **kwargs):
        self.pre_save()
        super().save(*args, **kwargs)
        self.post_save()


class Course(models.Model):
    name = models.CharField(max_length=225, verbose_name='Course Name')
    code = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=20, choices=CLASS_STATUS_CHOICES, default='active')

    objects = CourseManagers()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def create_course(cls, name, code, status):
        course = cls(name=name, code=code, status=status)

        course.save()
        return course

    def update_course(self, name=None, code=None, status=None):

        if name is not None:
            self.name = name

        if code is not None:
            self.code = code

        if status is not None:
            self.status = status

        self.save()

    def delete_course(self):
        self.delete()

    def pre_save(self):
        if not self.status:
            self.status = "active"

    def post_save(self):
        print(f"Course {self.name} saved successfully")

    def save(self, *args, **kwargs):
        self.pre_save()
        super().save(*args, **kwargs)
        self.post_save()


class Student(models.Model):
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    student_id = models.CharField(max_length=10, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    shortCode = models.CharField(max_length=10, choices=COURSE_SHORT_CODE, default='BICT')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    class_rep = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, default='')
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    objects = StudentManagers()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('student_details', kwargs={'pk': self.pk})

    @classmethod
    def create_student(cls, student_id, semester, student_class):
        student = cls(student_id=student_id, semester=semester, student_class=student_class)
        student.save()
        return student

    def update_student(self, student_id=None, semester=None, student_class=None):
        if student_id is not None:
            self.student_id = student_id

        if semester is not None:
            self.semester = semester

        if student_class is not None:
            self.student_class = student_class

        self.save()

    def delete_student(self):
        self.delete()

    def post_save(self):
        print(f'Student {self.first_name} {self.last_name} saved successfully')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.post_save()


class Module(models.Model):
    name = models.CharField(max_length=225, verbose_name='Module Name')
    code = models.CharField(max_length=15, default='')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=CLASS_STATUS_CHOICES, default='active')

    objects = ModuleManagers()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @classmethod
    def create_module(cls, name, course, status):
        module = cls(name=name, course=course, status=status)
        module.save()
        return module

    def update_module(self, name=None, course=None, status=None):
        if name is not None:
            self.name = name

        if course is not None:
            self.course = course

        if status is not None:
            self.status = status

    def delete_module(self):
        self.delete()

    def pre_save(self):
        if not self.status:
            self.status = "active"

    def post_save(self):
        print(f"Module {self.name} saved successfully")

    def save(self, *args, **kwargs):
        self.pre_save()
        super().save(*args, **kwargs)
        self.post_save()


class Enrollment(TimestampedMixinModel):
    title = models.CharField(max_length=255, default='')
    student = models.ManyToManyField(Student)
    modules = models.ManyToManyField(Module)

    def __str__(self):
        return self.title


class Lecturer(models.Model):
    name = models.CharField(max_length=50)
    modules = models.ManyToManyField(Module)

    objects = LecturerManagers()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @classmethod
    def create_lecturer(cls, name, modules):
        lecturer = cls(name=name, modules=modules)
        lecturer.save()
        return lecturer

    def update_lecturer(self, name=None, modules=None):
        if name is not None:
            self.name = name

        if modules is not None:
            self.modules = modules

        self.save()

    def delete_lecturer(self):
        self.delete()

    def post_save(self):
        print(f"Lecturer {self.name} saved successfully")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.post_save()


class Appraisal(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 11)])
    comments = models.TextField()
    date_appraised = models.DateTimeField(auto_now_add=True)

    objects = AppraisalManagers()

    def __str__(self):
        return f'{self.student}'

    @classmethod
    def create_appraisal(cls, student, lecturer, score, comments, data_appraised):
        appraisal = cls(student=student, lecturer=lecturer, score=score, comments=comments,
                        date_appraised=data_appraised)
        appraisal.save()
        return appraisal

    def update_appraisal(self, student=None, lecturer=None, score=None, comments=None, date_appraised=None):
        if student is not None:
            self.student = student

        if lecturer is not None:
            self.lecturer = lecturer

        if score is not None:
            self.score = score

        if comments is not None:
            self.comments = comments

        if date_appraised is not None:
            self.date_appraised = date_appraised

        self.save()

    def delete_appraisal(self):
        self.delete()

    def pre_save(self):
        if not self.score:
            self.score = 5

    def post_save(self):
        print(f'Appraisal {self.lecturer} saved successfully')

    def save(self, *args, **kwargs):
        self.pre_save()
        super().save(*args, **kwargs)
        self.post_save()


class ClassRoom(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class TimeTable(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    day = models.CharField(max_length=25, choices=DAY_CHOICES, default='Select Day')
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    room_name = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=10, default='')  # Change TimeField to CharField
    end_time = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.class_name.name

    class Meta:
        unique_together = ['class_name', 'day', 'start_time', 'end_time']

    def clean(self):
        # Check for existing timetable entry for the same day, time, and classroom
        existing_timetable = TimeTable.objects.filter(
            start_time=self.start_time,
            end_time=self.end_time,
            room_name=self.room_name
        ).exclude(pk=self.pk)  # Exclude current instance if it's being updated

        if existing_timetable.exists():
            raise ValidationError('This classroom is already occupied at the specified time.')

    def check_class_status(self):
        status = TimeTable.objects.filter(
            day=self.day,
            start_time=self.start_time,
            end_time=self.end_time,
            room_name=self.room_name
        ).exclude(pk=self.pk)  # Exclude current instance if it's being updated

        if status.exists():
            raise ValidationError('This class is already occupied at the specified time.')

    def get_absolute_url(self):
        class_id = self.class_name.pk
        day = self.day
        return reverse('class_timetable', kwargs={'class_id': class_id, 'day': day})
