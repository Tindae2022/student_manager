from django.db import models
from datetime import datetime


class IssuesQueryset(models.QuerySet):

    def all_issues(self):
        return self.all()

    def search_issues(self, query):
        return self.filter(student__icontains=query) | models.Q(module__icontains=query)

    def pending_issues(self):
        return self.filter(status='pending')

    def solved_issues(self):
        return self.filter(status='solved')

    def unsolved_issues(self):
        return self.filter(status='unsolved')

    def total_issues(self):
        return self.all().count()

    def total_pending_issues(self):
        return self.filter(status='pending').count()

    def total_solved_issues(self):
        return self.filter(status='solved').count()

    def total_unsolved_issues(self):
        return self.filter(status='unsolved').count()

    def issues_in_date_range(self, start_date, end_date):
        return self.filter(date_reported__range=[start_date, end_date])
