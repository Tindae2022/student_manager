from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import (Course, Module, Lecturer, Class, Semester, Student, Appraisal,
                     ClassRoom, TimeTable, TIME_CHOICES)
from datetime import datetime


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'status']

    labels = {
        'name': 'Course Name',
        'code': 'Course Code',
        'status': 'Status',
    }

    widgets = {
        'name': forms.TextInput(attrs={'placeholder': 'enter course name'}),
        'code': forms.TextInput(attrs={'placeholder': 'enter Course code'})
    }

    def save(self, commit=True):
        course = super(CourseForm, self).save(commit=False)
        if commit:
            course.save()
        return course


class CourseUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CourseUpdateForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'placeholder': 'enter course name'})
        self.fields['code'].widget.attrs.update({'placeholder': 'enter course code'})

    class Meta:
        model = Course
        fields = ['name', 'code', 'status']

    def save(self, commit=True):
        course = super(CourseUpdateForm, self).save(commit=False)
        if commit:
            course.save()

        return course


class ModuleForm(forms.ModelForm):
    name = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(ModuleForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Module Name'
        self.fields['code'].label = 'Course Code'
        self.fields['course'].label = 'Course'
        self.fields['status'].label = 'Status'
        self.fields['name'].widget.attrs.update({'placeholder': 'enter the module name'})

    class Meta:
        model = Module
        fields = ['name', 'code', 'course', 'status']

        error_messages = {
            'name': {'required': 'Module name is required', 'max_length': 'module name is too long'}

        }

    def save(self, commit=True):
        module = super(ModuleForm, self).save(commit=False)
        if module:
            module.save()
        return module


class ModuleUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModuleUpdateForm, self).__init__(*args, **kwargs)

        self.fields['name'].label = 'Module Name'
        self.fields['code'].label = 'Module Code'
        self.fields['course'].label = 'Course'
        self.fields['status'].label = 'Status'

        self.fields['name'].widget.attrs.update({'placeholder': 'enter module name'})

    class Meta:
        model = Module
        fields = ['name', 'code', 'course', 'status']

        error_messages = {
            'name': {'required': 'Module name is required', 'max_length': 'module name is too long'}

        }

    def save(self, commit=True):
        module = super(ModuleUpdateForm, self).save(commit=False)
        if commit:
            module.save()

        return module


class LecturerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LecturerForm, self).__init__(*args, **kwargs)

        self.fields['name'].label = 'Lecturer''s Name'
        self.fields['modules'].label = 'Modules'

        self.fields['name'].widget.attrs.update({'placeholder': 'enter lecturer full name'})

    class Meta:
        model = Lecturer
        fields = ['name', 'modules']

        error_messages = {
            'required': 'lecturer name is required', 'max_length': 'Name is too long'
        }

    def save(self, commit=True):
        lecturer = super(LecturerForm, self).save(commit=False)

        lecturer.role = 'lecturer'
        if commit:
            lecturer.save()

        return lecturer


class LecturerUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LecturerUpdateForm, self).__init__(*args, **kwargs)

        self.fields['name'].label = 'Lecturer''s Name'
        self.fields['modules'].label = 'Modules'

        self.fields['name'].widgets.attrs.update({'placeholder': 'enter lecturer full name'})

    class Meta:
        model = Lecturer
        fields = ['name', 'modules']

        error_messages = {
            'required': 'lecturer name is required', 'max_length': 'Name is too long'
        }

    def save(self, commit=True):
        lecturer = super(LecturerUpdateForm, self).save(commit=False)

        lecturer.role = 'lecturer'
        if commit:
            lecturer.save()

        return lecturer


class ClassForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)

        self.fields['name'].label = 'Class Name'
        self.fields['status'].label = 'Status'

        self.fields['name'].widget.attrs.update({'placeholder': 'enter class name'})

    class Meta:
        model = Class
        fields = ['name', 'status']

    def save(self, commit=True):
        class_form = super(ClassForm, self).save(commit=False)

        if commit:
            class_form.save()

        return class_form


class ClassUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClassUpdateForm, self).__init__(*args, **kwargs)

        self.fields['name'].label = 'Class Name'
        self.fields['status'].label = 'Status'

        self.fields['name'].widget.attrs.update({'placeholder': 'enter class name'})

    class Meta:
        model = Class
        fields = ['name', 'status']

    def save(self, commit=True):
        class_form = super(ClassUpdateForm, self).save(commit=False)

        if commit:
            class_form.save()

        return class_form


class SemesterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SemesterForm, self).__init__(*args, **kwargs)

        self.fields['name'].label = 'Semester Name'
        self.fields['classes'].label = 'Classes'
        self.fields['status'].label = 'Status'

        self.fields['name'].widget.attrs.update({'placeholder': 'enter semester name'})

    class Meta:
        model = Semester
        fields = ['name', 'classes', 'status']

    def save(self, commit=True):
        semester = super(SemesterForm, self).save(commit=False)

        if commit:
            semester.save()

        return semester


class SemesterUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SemesterUpdateForm, self).__init__(*args, **kwargs)
        self.fields['classes'].queryset = Class.objects.all()

    class Meta:
        model = Semester
        fields = ['name', 'classes', 'status']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_id', 'semester', 'course', 'shortCode', 'student_class', 'email',
                  'class_rep', 'image']

    def save(self, commit=True):
        student = super(StudentForm, self).save(commit=False)
        student.role = 'student'
        if commit:
            student.save()

        return student


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_id', 'semester', 'course', 'class_rep', 'shortCode',
                  'student_class', 'email', 'image']
        error_messages = {
            'first_name': {'required': 'first name is required', 'max_length': 'first name is too long'},
            'last_name': {'required': 'last name is required', 'max_length': 'last name is too long'},
            'student_id': {'required': 'student id is required'},
            'semester': {'required': 'semester is required'}
        }


class AppraisalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppraisalForm, self).__init__(*args, **kwargs)

        self.fields['student'].label = 'Student'
        self.fields['lecturer'].label = 'Lecturer'
        self.fields['score'].label = 'Score'
        self.fields['comments'].label = 'Comments'

        self.fields['comments'].widget.attrs.update({'placeholder': 'write a comment message on the lecturer '
                                                                    'performance'})

    class Meta:
        model = Appraisal
        fields = ['student', 'lecturer', 'score', 'comments']

    def save(self, commit=True):
        appraisal = super(AppraisalForm, self).save(commit=False)

        if commit:
            appraisal.save()

        return appraisal


class AppraisalUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppraisalUpdateForm, self).__init__(*args, **kwargs)

        self.fields['student'].label = 'Student'
        self.fields['lecturer'].label = 'Lecturer'
        self.fields['score'].label = 'Score'
        self.fields['comments'].label = 'Comments'

        self.fields['comments'].widget.attrs.update({'placeholder': 'write a comment message on the lecturer '
                                                                    'performance'})

    class Meta:
        model = Appraisal
        fields = ['student', 'lecturer', 'score', 'comments']

    def clean_score(self):
        score = self.cleaned_data['score']
        if score < 0 or score > 5:
            raise forms.ValidationError('The score must be between 1 - 5')
        return score

    def save(self, commit=True):
        appraisal = super(AppraisalUpdateForm, self).save(commit=False)

        if commit:
            appraisal.save()

        return appraisal


class StudentEmailForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    #  = forms.EmailField()


class ClassSearchForm(forms.Form):
    search_term = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Search'}))


class CSVImportForm(forms.Form):
    csv_file = forms.FileField()


class TimeTableForm(forms.ModelForm):
    start_time = forms.ChoiceField(choices=TIME_CHOICES)
    end_time = forms.ChoiceField(choices=TIME_CHOICES)

    class Meta:
        model = TimeTable
        fields = ['class_name', 'semester', 'day', 'module', 'room_name', 'lecturer', 'start_time', 'end_time']
