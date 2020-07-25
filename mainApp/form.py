from django import forms
from .models import HelpPost, helpComment

class PostingForm(forms.ModelForm):
    class Meta:
        model = HelpPost
        fields = ['deadLine', 'description']

class HelpCommentForm(forms.ModelForm):
    class Meta:
        model = helpComment
        fields = ['body']