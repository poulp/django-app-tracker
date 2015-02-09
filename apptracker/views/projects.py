from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.core.urlresolvers import reverse_lazy

from apptracker.models import Project
from apptracker.mixins import ProjectMixin
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
    fields = ['name', 'description']

    def get_success_url(self):
        return reverse_lazy('project-list')


class ProjectLabelsView(ProjectMixin, FormView):
    template_name = 'apptracker/projects/labels.html'
    form_class = LabelForm

    def get_success_url(self):
        return reverse_lazy('project-labels', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(ProjectLabelsView, self).get_context_data(**kwargs)
        context['labels'] = self.get_project().labels.all
        return context

    def form_valid(self, form):
        label = form.save(commit=False)
        label.project = self.get_project()
        label.save()
        return super(ProjectLabelsView, self).form_valid(form)