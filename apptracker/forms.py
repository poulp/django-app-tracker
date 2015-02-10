
from django.forms import ModelForm
from django.forms.fields import TextInput

from apptracker.models import Issue, Label


class NewIssueForm(ModelForm):
    class Meta(object):
        model = Issue
        fields = ['title', 'description', 'labels']


class LabelForm(ModelForm):
    class Meta(object):
        model = Label
        fields = ['title', 'color']
        widgets = {
            'color': TextInput(attrs={'class': 'color-input'})
        }