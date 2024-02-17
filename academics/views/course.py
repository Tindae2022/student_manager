from django.shortcuts import render
from django.views.generic import (ListView, DeleteView,
                                  CreateView, UpdateView, TemplateView)

from academics.models import Course
from academics.forms import CourseForm, CourseUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'course/course_index.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.get_all_courses()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_courses'] = 'All Courses'

        return context


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'course/course_create.html'
    form_class = CourseForm

    def get_success_url(self):
        return reverse_lazy('course_create_success')


class CourseSuccessTemplateView(TemplateView):
    template_name = 'course/success.html'


class CourseDeleteSuccessTemplateView(TemplateView):
    template_name = 'course/delete_success.html'


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseUpdateForm
    template_name = 'course/course_update.html'
    success_url = reverse_lazy('course_create_success')


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'course/course_confirm_delete.html'
    context_object_name = 'course_delete'
    success_url = reverse_lazy('course_delete_success')
