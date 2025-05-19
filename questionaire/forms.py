from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'is_active']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question', 'answer_text']
        widgets = {
            'answer_text': forms.Textarea(attrs={'class': 'form-control'}),
        }
