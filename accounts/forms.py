from allauth.account.forms import SignupForm
from django import forms
from .models import Profile


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Last Name'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
    




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'verified_at', 'created', 'updated', 'verification_status', 'user_type')

        widgets = {
            'gender': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-lg'}),
            'address': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': 3}),
            'sleep_schedule': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'cleanliness_level': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'social_habits': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'study_preference': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'hobbies': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': 2}),
            'interests': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields if not overridden above
        for field in self.fields.values():
            if not field.widget.attrs.get('class'):
                field.widget.attrs['class'] = 'form-control form-control-lg'
