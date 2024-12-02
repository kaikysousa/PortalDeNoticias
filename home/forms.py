from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    is_reader = forms.BooleanField(required=False, initial=False, label="Leitor")
    is_journalist = forms.BooleanField(required=False, initial=False, label="Jornalista")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_reader', 'is_journalist', 'is_admin']

    def clean(self):
        cleaned_data = super().clean()
        is_reader = cleaned_data.get('is_reader')
        is_journalist = cleaned_data.get('is_journalist')

        # Certifique-se de que pelo menos um seja selecionado
        if not is_reader and not is_journalist:
            raise forms.ValidationError("Você deve selecionar pelo menos uma função (Leitor ou Jornalista).")
        return cleaned_data
