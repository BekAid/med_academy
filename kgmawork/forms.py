from django import forms
from . import models

class KgmaWorkForm(forms.ModelForm):
    class Meta:
        model = models.KgmaWork
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Commet_TV
        fields = '__all__'