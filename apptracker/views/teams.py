from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse

from apptracker.models import TrackerTeam
from apptracker.mixins import LoginRequiredMixin, ProjectMixin
from apptracker.forms import TrackerTeamForm


class TeamListView(LoginRequiredMixin, ProjectMixin, ListView):
    template_name = 'apptracker/projects/teams/list.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return TrackerTeam.objects.all()


class TeamCreateView(LoginRequiredMixin, ProjectMixin, CreateView):
    template_name = 'apptracker/projects/teams/create.html'
    model = TrackerTeam
    form_class = TrackerTeamForm

    def get_success_url(self):
        return reverse('team-list', kwargs={'project_pk': self.kwargs['project_pk']})


class TeamDeleteView(LoginRequiredMixin, ProjectMixin, DeleteView):
    model = TrackerTeam
    template_name = 'apptracker/projects/teams/confirm_delete.html'
    context_object_name = 'team'
    pk_url_kwarg = 'team_pk'

    def get_success_url(self):
        return reverse('team-list', kwargs={'project_pk': self.kwargs['project_pk']})