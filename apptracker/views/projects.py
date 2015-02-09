from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

from apptracker.models import Project
from apptracker.mixins import ProjectMixin


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


class ProjectLabelsView(ProjectMixin, ListView):
    template_name = 'apptracker/projects/labels.html'
    context_object_name = 'labels'

    def get_queryset(self):
        return self.get_project().labels.all()


