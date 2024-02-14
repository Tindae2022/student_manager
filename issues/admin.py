from django.contrib import admin
from .models import Issue


# Register your models here.
@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    pass
