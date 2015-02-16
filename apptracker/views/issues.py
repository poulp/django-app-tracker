
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import redirect, get_object_or_404

from apptracker.mixins import ProjectMixin, IssueMixin, LoginRequiredMixin
from apptracker.forms import NewIssueForm, IssueFilterForm, CommentForm
from apptracker.models import Issue

class IssuesListView(ProjectMixin, ListView):
    template_name = 'apptracker/issues/list.html'
    context_object_name = 'issues'
    paginate_by = 20

    def get_queryset(self, **kwargs):
        is_open = True if self.request.GET.get('is_open', False) else False
        is_close = True if self.request.GET.get('is_close', False) else False
        labels = self.request.GET.getlist('labels', [])

        filter_params = {}

        if not is_close == is_open:
            filter_params['is_closed'] = is_close

        if labels != []:
            filter_params['labels__slug__in'] = labels

        return self.get_project().issues.all().filter(**filter_params).distinct()

    def get_context_data(self, *args, **kwargs):
        context = super(IssuesListView, self).get_context_data(**kwargs)
        context['filter_form'] = IssueFilterForm(project=context['project'], data=self.request.GET)
        return context


class IssueDetailView(ProjectMixin, DetailView):
    model = Issue
    template_name = 'apptracker/issues/detail.html'
    context_object_name = 'issue'
    pk_url_kwarg = 'issue_pk'

    def get_context_data(self, *args, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class IssueCommentView(LoginRequiredMixin, ProjectMixin, IssueMixin, FormView):
    template_name = 'apptracker/issues/comment.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('issue-detail', kwargs={'pk': self.kwargs['pk'], 'issue_pk': self.kwargs['issue_pk']})

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.issue = self.get_issue()
        if comment.issue.owner == self.request.user:
            comment.is_issue_owner = True
        else:
            comment.is_issue_owner = False

        comment.save()
        return super(IssueCommentView, self).form_valid(form)


class IssueDeleteView(LoginRequiredMixin, ProjectMixin, DeleteView):
    model = Issue
    pk_url_kwarg = 'issue_pk'
    template_name = 'apptracker/issues/confirm_delete.html'
    context_object_name = 'issue'

    def get_success_url(self):
        return reverse('issue-list', kwargs={'pk': self.get_project().pk})


class IssueNewView(LoginRequiredMixin, ProjectMixin, FormView):
    template_name = 'apptracker/issues/new.html'
    form_class = NewIssueForm

    def get_form(self, form_class):
        return form_class(project=self.get_project(), **self.get_form_kwargs())

    def get_success_url(self):
        return reverse_lazy('issue-list', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        issue = form.save(commit=False)
        issue.owner = self.request.user
        issue.project = self.get_project()
        issue.save()
        form.save_m2m()
        return super(IssueNewView, self).form_valid(form)


class IssueEditView(LoginRequiredMixin, ProjectMixin, UpdateView):
    model = Issue
    template_name = 'apptracker/issues/edit.html'
    form_class = NewIssueForm
    context_object_name = 'issue'
    pk_url_kwarg = 'issue_pk'

    def get_success_url(self):
        return reverse('issue-detail', kwargs={'pk': self.get_project().pk, 'issue_pk': self.kwargs['issue_pk']})

    def get_form(self, form_class):
        return form_class(project=self.get_project(), **self.get_form_kwargs())

    def form_valid(self, form):
        issue = form.save(commit=False)
        if 'editclose' in self.request.POST:
            issue.is_closed = not issue.is_closed

        issue.save()
        return super(IssueEditView, self).form_valid(form)


class IssueCloseView(LoginRequiredMixin, ProjectMixin, View):

    def get(self, request, pk, issue_pk):
        issue = get_object_or_404(Issue, pk=issue_pk)
        issue.is_closed = not issue.is_closed
        issue.save()
        return redirect(reverse('issue-detail', kwargs={'pk': pk, 'issue_pk': issue_pk}))