
from django import forms

from apptracker.models import Issue, Label, Comment


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