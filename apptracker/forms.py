
from django import forms
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

from apptracker.models import Issue, Label, Comment, TrackerTeam, Project


class NewIssueForm(forms.ModelForm):
    class Meta(object):
        model = Issue
        fields = ['title', 'description', 'labels', 'pull_request']

    def __init__(self, project, *args, **kwargs):
        super(NewIssueForm, self).__init__(*args, **kwargs)
        self.fields['labels'].queryset = Label.objects.filter(project=project)


class LabelForm(forms.ModelForm):
    class Meta(object):
        model = Label
        fields = ['title', 'color']


class IssueFilterForm(forms.Form):
    is_close = forms.BooleanField()
    is_open = forms.BooleanField()
    labels = forms.ModelMultipleChoiceField(queryset=None, to_field_name="slug")

    def __init__(self, project, *args, **kwargs):
        super(IssueFilterForm, self).__init__(*args, **kwargs)
        self.fields['labels'].queryset = Label.objects.filter(project=project)


class CommentForm(forms.ModelForm):
    class Meta(object):
        model = Comment
        fields = ['text']


class TrackerTeamForm(forms.ModelForm):
    class Meta(object):
        model = TrackerTeam
        fields = ['name', 'color', 'permissions']
        widgets = {
            'permissions': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(TrackerTeamForm, self).__init__(*args, **kwargs)
        apptracker_content_types = ContentType.objects.get_for_models(
            Issue, Label, Comment, TrackerTeam, Project).values()
        self.fields['permissions'].queryset = Permission.objects.filter(content_type__in=apptracker_content_types)