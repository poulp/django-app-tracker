
from django.forms import ModelForm

from apptracker.models import Issue, Label


class NewIssueForm(ModelForm):
    class Meta(object):
        model = Issue
        fields = ['title', 'description', 'labels']


class LabelForm(ModelForm):
    class Meta(object):
        model = Label
        fields = ['title', 'color']