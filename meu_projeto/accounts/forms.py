from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import CustomUser, Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    security_question = forms.CharField(max_length=255, initial="Qual o nome da sua cidade natal?")
    security_answer = forms.CharField(max_length=255, widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'security_question', 'security_answer')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = user.profile
            profile.security_question = self.cleaned_data['security_question']
            profile.security_answer = self.cleaned_data['security_answer']  # Save hash it
            profile.save()
        return user

class PasswordResetByQuestionForm(forms.Form):
    username = forms.CharField(max_length=150)
    answer = forms.CharField(max_length=255, widget=forms.PasswordInput)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('new_password1') != cleaned_data.get('new_password2'):
            raise forms.ValidationError("Senhas não coincidem")
        return cleaned_data