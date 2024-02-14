from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from academics.models import Module
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from academics.forms import ModuleForm, ModuleUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ModuleListView(LoginRequiredMixin, ListView):
    model = Module
    template_name = 'module/module_index.html'
    context_object_name = 'module_index'

    def get_queryset(self):
        return Module.objects.all_modules()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_modules'] = 'All Modules'
        return context


class ModuleCreateView(LoginRequiredMixin, CreateView):
    model = Module
    template_name = 'module/module_create.html'
    form_class = ModuleForm

    def get_success_url(self):
        return reverse_lazy('module_index')


class ModuleUpdateView(LoginRequiredMixin, UpdateView):
    model = Module
    template_name = 'module/module_update.html'
    form_class = ModuleUpdateForm
    success_url = reverse_lazy('module_index')


class ModuleDeleteView(LoginRequiredMixin, DeleteView):
    model = Module
    template_name = 'module/module_confirm_delete.html'
    success_url = reverse_lazy('module_index')
    context_object_name = 'module'


class ModuleSearchView(LoginRequiredMixin, View):
    template_name = 'module/module_index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        search_term = request.POST.get('search_term', '')
        modules = Module.objects.filter(name__icontains=search_term)
        context = {'modules': modules, 'search_term': search_term}
        return render(request, self.template_name, context)
