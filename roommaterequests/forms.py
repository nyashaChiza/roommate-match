from django import forms
from django.contrib.auth import get_user_model
from roommaterequests.models import RoommateRequest

class RoommateRequestForm(forms.ModelForm):
    class Meta:
        model = RoommateRequest
        fields = ['receiver', 'sender']
        widgets = {
            'receiver': forms.Select(attrs={'class': 'form-control'}),
            'sender': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'receiver': 'Receiver',
            'sender': 'Sender',
        }

class RoommateRequestReviewForm(forms.ModelForm):
    class Meta:
        model = RoommateRequest
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
