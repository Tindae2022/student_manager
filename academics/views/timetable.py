from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from academics.models import TimeTable
from academics.forms import TimeTableForm
from django.contrib.auth.mixins import LoginRequiredMixin


class TimetableCreateView(LoginRequiredMixin, CreateView):
    model = TimeTable
    template_name = 'timetable/create.html'
    form_class = TimeTableForm

    def get_success_url(self):
        return reverse_lazy('dashboard')


class TimetableUpdateView(LoginRequiredMixin, UpdateView):
    model = TimeTable
    form_class = TimeTableForm
    template_name = 'timetable/update.html'
    context_object_name = 'timetable_update'

    success_url = reverse_lazy('timetable_register_success')


def register_success(request):
    return render(request, 'timetable/register_success.html')


class TimetableDeleteView(LoginRequiredMixin, DeleteView):
    model = TimeTable
    template_name = 'timetable/confirm_delete.html'

    success_url = reverse_lazy('timetable_delete_success')


def delete_success(request):
    return render(request, 'timetable/delete_success.html')
