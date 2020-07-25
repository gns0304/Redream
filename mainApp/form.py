from django import forms
from .models import HelpPost, DonatorComment, ReceiverComment

class PostingForm(forms.ModelForm):
    class Meta:
        model = HelpPost
        fields = ['deadLine', 'description']

class DonatorCommentForm(forms.ModelForm):
    class Meta:
        model = DonatorComment
        fields = ['body']

class ReceiverCommentForm(forms.ModelForm):
    class Meta:
        model = ReceiverComment
        fields = ['body']