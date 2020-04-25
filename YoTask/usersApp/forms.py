from allauth.account.forms import SignupForm
from django import forms
from django.core.validators import RegexValidator


class CustomSignupForm(SignupForm):
    telegram = forms.CharField(max_length=50,
                               required=False,
                               label='Telegram',
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'username',
                                   'class': 'form-control'
                               }),
                               validators=[
                                   RegexValidator('^[\.\_a-zA-Z0-9]+$', message="Неправильный Telegram ID.")])

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.telegram = self.cleaned_data['telegram']
        user.save()

        return user
