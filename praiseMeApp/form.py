from django import forms
from .models import PraiseMePost

class PostingForm(forms.ModelForm):
    class Meta:
        model = PraiseMePost
        fields = ['body']

class ReceiverPraiseMeForm(forms.ModelForm):
    class Meta:
        model = ReceiverPraiseMeComment
        fields = ['text']

class DonatorPraiseMeForm(forms.ModelForm):
    class Meta:
        model = DonatorPraiseMeComment
        fields = ['text']