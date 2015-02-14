from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView
from django.core.urlresolvers import reverse

from apptracker.models import Project, Label
from apptracker.mixins import ProjectMixin, AjaxableResponseMixin
from apptracker.forms import LabelForm


class ProjectListView(ListView):
    model = Project
    template_name = 'apptracker/projects/list.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'apptracker/projects/detail.html'
    context_object_name = 'project'


class ProjectCreateView(CreateView):
    template_name = 'apptracker/projects/create.html'
    model = Project
    fields = [
        'name',
        'description',
        'repository',
        'documentation'
    ]

    def get_success_url(self):
        return reverse('project-list')

class ProjectUpdateView(ProjectMixin, UpdateView):
    template_name = 'apptracker/projects/edit.html'
    model = Project
    fields = [
        'name',
        'description',
        'repository',
        'documentation'
    ]

    def get_success_url(self):
        return reverse('project-list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'apptracker/projects/confirm_delete.html'
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project-list')


class ProjectLabelsView(ProjectMixin, FormView):
    template_name = 'apptracker/projects/labels.html'
    form_class = LabelForm

    def get_success_url(self):
        return reverse('project-labels', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(ProjectLabelsView, self).get_context_data(**kwargs)
        context['labels'] = self.get_project().labels.all
        return context

    def form_valid(self, form):
        label = form.save(commit=False)
        label.project = self.get_project()
        label.save()
        return super(ProjectLabelsView, self).form_valid(form)


class LabelDeleteView(AjaxableResponseMixin, DeleteView):
    model = Label
    pk_url_kwarg = 'label_pk'
    template_name = 'apptracker/projects/delete_label_confirm.html'

    def get_success_url(self):
        return reverse('project-list')
