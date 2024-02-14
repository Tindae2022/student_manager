from django.db import models
from django.urls import reverse

from academics.models import Student, Module
from .managers import IssueManagers

# Create your models here.

ISSUE_STATUS_CHOICES = [
    ('unsolved', 'Unsolved'),
    ('pending', 'Pending'),
    ('solved', 'Solved'),
]

ISSUES_CATEGORIES = [
    ('travel', 'Travel'),
    ('fees', 'Fees'),
    ('exam', 'Exam'),
    ('medical', 'Medical'),
    ('drugs', 'Drugs'),
    ('others', 'Others'),
]


class Issue(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    category = models.CharField(max_length=20, choices=ISSUES_CATEGORIES, default='fees')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=ISSUE_STATUS_CHOICES, default='pending')
    date_reported = models.DateTimeField(auto_now_add=True)
    evidence_picture = models.ImageField(upload_to='issue_evidence/', null=True, blank=True)

    objects = IssueManagers()

    def __str__(self):
        return f"{self.student}"

    def get_absolute_url(self):
        return reverse('issue_detail', args=[str(self.id)])

    @classmethod
    def create_issue(cls, student, module, description, status, title):
        issue = cls(student=student, module=module, description=description, status=status, title=title)
        issue.save()
        return issue

    def update_issue(self, student=None, module=None, description=None, status=None,

                     ):

        if student is not None:
            self.student = student

        if module is not None:
            self.module = module

        if description is not None:
            self.description = description

        if status is not None:
            self.status = status

        self.save()

    def delete_issue(self):
        self.delete()

    def pre_save(self):
        if not self.status:
            self.status = 'pending'

    def post_save(self):
        print(f'Issue of {self.student} saved successfully')

    def save(self, *args, **kwargs):
        self.pre_save()
        super().save(*args, **kwargs)
        self.post_save()
