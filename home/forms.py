from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):


    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_reader', 'is_journalist']

    def clean_role(self):
        role = self.cleaned_data.get('role')
