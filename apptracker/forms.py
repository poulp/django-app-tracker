
from django import forms
from django.forms.fields import TextInput

from apptracker.models import Issue, Label


class NewIssueForm(forms.ModelForm):
    class Meta(object):
        model = Issue
        fields = ['title', 'description', 'labels']


class LabelForm(forms.ModelForm):
    class Meta(object):
        model = Label
        fields = ['title', 'color']
        widgets = {
            'color': TextInput(attrs={'class': 'color-input'})
        }


class IssueFilterForm(forms.Form):
    is_closed = forms.BooleanField(initial=False)
    is_open = forms.BooleanField(initial=True)