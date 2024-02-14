from academics.models import Lecturer
from django.views.generic import ListView, DetailView


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
