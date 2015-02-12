
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from apptracker.mixins import ProjectMixin
from apptracker.forms import NewIssueForm, IssueFilterForm
from apptracker.models import Issue


class IssuesListView(ProjectMixin, ListView):
    template_name = 'apptracker/issues/list.html'
    context_object_name = 'issues'
    paginate_by = 20

    def get_queryset(self, **kwargs):
        return self.get_project().issues.all()

    def get_context_data(self, **kwargs):
        context = super(IssuesListView, self).get_context_data(**kwargs)
        context['filter_form'] = IssueFilterForm()
        return context


class IssueDetailView(ProjectMixin, DetailView):
    model = Issue
    template_name = 'apptracker/issues/detail.html'
    context_object_name = 'issue'
    pk_url_kwarg = 'issue_pk'


class IssueDeleteView(ProjectMixin, DeleteView):
    model = Issue
    pk_url_kwarg = 'issue_pk'
    template_name = 'apptracker/issues/confirm_delete.html'
    context_object_name = 'issue'

    def get_success_url(self):
        return reverse('issue-list', kwargs={'pk': self.get_project().pk})


class IssueNewView(ProjectMixin, FormView):
    template_name = 'apptracker/issues/new.html'
    form_class = NewIssueForm

    def get_form(self, form_class):
        return form_class(project=self.get_project(), **self.get_form_kwargs())

    def get_success_url(self):
        return reverse_lazy('issue-list', kwargs={'pk': self.kwargs['pk']})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IssueNewView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        issue = form.save(commit=False)
        issue.owner = self.request.user
        issue.project = self.get_project()
        issue.save()
        form.save_m2m()
        return super(IssueNewView, self).form_valid(form)