from django import forms
from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['student', 'module', 'description', 'category', 'status', 'title', 'evidence_picture']

        labels = {
            'student': 'Student',
            'module': 'Module',
            'description': 'Description',
            'category': 'Category',
            'status': 'Status',
            'evidence_picture': 'Evidence Picture',
            'title': 'Title',
        }

    def save(self, commit=True):
        issue = super(IssueForm, self).save(commit=False)

        if commit:
            issue.save()

        return issue


class IssueUpdateForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['student', 'module', 'category', 'description', 'status', 'title', 'evidence_picture']

        labels = {
            'student': 'Student',
            'module': 'Module',
            'title': 'Title',
            'description': 'Description',
            'category': 'Category',
            'status': 'Status',
            'evidence_picture': 'Evidence Picture'
        }

    def save(self, commit=True):
        issue = super(IssueUpdateForm, self).save(commit=False)

        if commit:
            issue.save()

        return issue
