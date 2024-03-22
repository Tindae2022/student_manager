from django.urls import reverse_lazy
from django.views.generic import CreateView
from academics.models import ClassRoom
from academics.forms import ClassRoomForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ClassRoomCreateView(LoginRequiredMixin, CreateView):
    model = ClassRoom
    template_name = 'class_room/create.html'
    form_class = ClassRoomForm
    success_url = reverse_lazy('dashboard')

