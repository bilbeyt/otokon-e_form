from django import forms
from .models import Form


class FormCreateForm(forms.ModelForm):
    class Meta:
        model = Form
        exclude = ['slug', 'is_evaluated', 'reg_date']
