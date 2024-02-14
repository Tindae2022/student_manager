from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, UpdateView, CreateView,
                                  DeleteView)
from academics.models import Semester
from academics.forms import SemesterForm, SemesterUpdateForm
from itertools import groupby
from operator import attrgetter
from django.contrib.auth.mixins import LoginRequiredMixin


class SemesterListView(LoginRequiredMixin, ListView):
    model = Semester
    template_name = 'semester/semester_index.html'
    context_object_name = 'semester_index'

    def get_queryset(self):
        return Semester.objects.get_all_semester()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_semester'] = 'Semesters'
        return context


class SemesterTableListView(LoginRequiredMixin, ListView):
    model = Semester
    template_name = 'semester/table_view.html'
    context_object_name = 'semesters'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        semesters = Semester.objects.all().order_by('name')
        semester_with_classes = []

        for semester_instance in semesters:
            classes_for_semester = semester_instance.classes.all()
            semester_with_classes.append((semester_instance, classes_for_semester))

        context['semester_with_classes'] = semester_with_classes
        return context


class SemesterUpdateView(LoginRequiredMixin, UpdateView):
    model = Semester
    template_name = 'semester/semester_update.html'
    form_class = SemesterUpdateForm
    success_url = reverse_lazy('semester_success')


def semester_success(request):
    return render(request, 'semester/success.html')


class SemesterCreateView(LoginRequiredMixin, CreateView):
    model = Semester
    template_name = 'semester/semester_create.html'
    form_class = SemesterForm
    success_url = reverse_lazy('semester_success')


class SemesterDeleteView(LoginRequiredMixin, DeleteView):
    model = Semester
    template_name = 'semester/confirm_delete.html'
    success_url = reverse_lazy('semester_delete_success')


def semester_delete_success(request):
    return render(request, 'semester/delete_success.html')
