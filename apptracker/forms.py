
from django import forms

from apptracker.models import Issue, Label


class NewIssueForm(forms.ModelForm):
    class Meta(object):
        model = Issue
        fields = ['title', 'description', 'labels']

    def __init__(self, project, *args, **kwargs):
        super(NewIssueForm, self).__init__(*args, **kwargs)
        self.fields['labels'].queryset = Label.objects.filter(project=project)


class LabelForm(forms.ModelForm):
    class Meta(object):
        model = Label
        fields = ['title', 'color']


class IssueFilterForm(forms.Form):
    is_close = forms.BooleanField(initial=False)
    is_open = forms.BooleanField(initial=True)