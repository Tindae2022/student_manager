from django.db import models
from .queryset import IssuesQueryset


class IssueManagers(models.Manager):

    def get_queryset(self):
        return IssuesQueryset(self.model, using=self._db).all()

    def all_issues(self):
        return self.get_queryset().all_issues()

    def search_issues(self, query):
        return self.get_queryset().search_issues(query)

    def pending_issues(self):
        return self.get_queryset().pending_issues()

    def solved_issues(self):
        return self.get_queryset().solved_issues()

    def unsolved_issues(self):
        return self.get_queryset().unsolved_issues()

    def issues_in_date_range(self, start_date, end_date):
        return self.get_queryset().issues_in_date_range(start_date, end_date)

    def total_issues(self):
        return self.get_queryset().total_issues()

    def total_pending_issues(self):
        return self.get_queryset().total_pending_issues()

    def total_solved_issues(self):
        return self.get_queryset().total_solved_issues()

    def total_unsolved_issues(self):
        return self.get_queryset().total_unsolved_issues()


