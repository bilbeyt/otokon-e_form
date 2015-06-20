from django import forms
from .models import Form
from captcha.fields import CaptchaField


class FormCreateForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Form
        exclude = ['slug', 'is_evaluated', 'reg_date']
