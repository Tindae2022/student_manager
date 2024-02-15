from academics.models import Lecturer
from django.views.generic import ListView, UpdateView, TemplateView, CreateView, DeleteView
from academics.forms import LecturerUpdateForm, LecturerForm
from django.urls import reverse_lazy


class LecturerListView(ListView):
    model = Lecturer
    template_name = 'lecturer/index.html'
    context_object_name = 'lecturer_index'

    def get_queryset(self):
        return Lecturer.objects.all_lecturers()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lecturer_details'] = 'List of Lecturers'
        return context


class LecturerUpdateView(UpdateView):
    model = Lecturer
    template_name = 'lecturer/update.html'
    form_class = LecturerUpdateForm
    success_url = reverse_lazy('lecturer_create_success')


class LecturerCreateSuccessTemplateView(TemplateView):
    template_name = 'lecturer/create_success.html'


class LecturerCreateView(CreateView):
    model = Lecturer
    template_name = 'lecturer/create.html'
    form_class = LecturerForm
    success_url = reverse_lazy('lecturer_create_success')


class LecturerDeleteSuccessTemplateView(TemplateView):
    template_name = 'lecturer/delete_success.html'


class LecturerDeleteView(DeleteView):
    model = Lecturer
    template_name = 'lecturer/confirm_delete.html'
    success_url = reverse_lazy('lecturer_delete_success')



