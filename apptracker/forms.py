
from django.forms import ModelForm

from apptracker.models import Issue


class NewIssueForm(ModelForm):
    class Meta(object):
        model = Issue
        fields = ['title', 'description', 'labels']