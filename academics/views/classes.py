from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from academics.models import Class, TimeTable
from academics.forms import ClassForm, ClassUpdateForm, ClassSearchForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ClassListView(LoginRequiredMixin, ListView):
    model = Class
    template_name = 'class/class_index.html'
    context_object_name = 'class_index'

    def get_queryset(self):
        queryset = Class.objects.all_classes()

        # Apply search filter if search term is provided
        search_term = self.request.GET.get('search_term')
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class_info'] = 'All Classes'
        context['search_form'] = ClassSearchForm(self.request.GET)

        return context


class ClassCreateView(LoginRequiredMixin, CreateView):
    model = Class
    template_name = 'class/class_create.html'
    form_class = ClassForm

    def get_success_url(self):
        return reverse_lazy('class_success')


def class_success(request):
    return render(request, 'class/successful_registration.html')


class ClassUpdateView(LoginRequiredMixin, UpdateView):
    model = Class
    template_name = 'class/class_update.html'
    form_class = ClassUpdateForm
    success_url = reverse_lazy('class_success')


class ClassDeleteView(LoginRequiredMixin, DeleteView):
    model = Class
    template_name = 'class/class_confirm_delete.html'
    success_url = reverse_lazy('class_delete_success')


def class_delete(request):
    return render(request, 'class/delete_success.html')


class ClassDetailView(DetailView):
    model = Class
    template_name = 'timetable/timetable.html'
    context_object_name = 'class_instance'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        class_instance = self.get_object()
        context['timetables'] = TimeTable.objects.filter(class_name=class_instance).order_by('start_time')

        return context


