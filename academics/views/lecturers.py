from academics.models import Lecturer, TimeTable
from django.views.generic import ListView, UpdateView, TemplateView, CreateView, DeleteView, DetailView
from academics.forms import LecturerUpdateForm, LecturerForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class LecturerListView(LoginRequiredMixin, ListView):
    model = Lecturer
    template_name = 'lecturer/index.html'
    context_object_name = 'lecturer_index'
    paginate_by = 10

    def get_queryset(self):
        return Lecturer.objects.all_lecturers()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lecturer_details'] = 'List of Lecturers'
        return context


class LecturerUpdateView(LoginRequiredMixin, UpdateView):
    model = Lecturer
    template_name = 'lecturer/update.html'
    form_class = LecturerUpdateForm
    success_url = reverse_lazy('lecturer_create_success')


class LecturerCreateSuccessTemplateView(TemplateView):
    template_name = 'lecturer/create_success.html'


class LecturerCreateView(LoginRequiredMixin, CreateView):
    model = Lecturer
    template_name = 'lecturer/create.html'
    form_class = LecturerForm
    success_url = reverse_lazy('lecturer_create_success')


class LecturerDeleteSuccessTemplateView(TemplateView):
    template_name = 'lecturer/delete_success.html'


class LecturerDeleteView(LoginRequiredMixin, DeleteView):
    model = Lecturer
    template_name = 'lecturer/confirm_delete.html'
    success_url = reverse_lazy('lecturer_delete_success')


class LecturerDetailView(LoginRequiredMixin, DetailView):
    model = Lecturer
    template_name = 'lecturer/lecturer_timetable.html'
    context_object_name = 'lecturer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lecturer = self.object
        timetable_entries = TimeTable.objects.filter(lecturer=lecturer)
        context['timetable_entries'] = timetable_entries
        return context
