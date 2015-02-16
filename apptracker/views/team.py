from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse

from apptracker.models import TrackerTeam
from apptracker.mixins import LoginRequiredMixin, ProjectMixin


class TeamListView(LoginRequiredMixin, ProjectMixin, ListView):
    template_name = 'apptracker/projects/teams/list.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return TrackerTeam.objects.all()


class TeamCreateViews(LoginRequiredMixin, ProjectMixin, CreateView):
    template_name = 'apptracker/projects/teams/create.html'
    model = TrackerTeam

    def get_success_url(self):
        return reverse('team-list', kwargs={'project_pk': self.kwargs['project_pk']})