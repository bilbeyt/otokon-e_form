from django import forms
from .models import Form


class FormCreateForm(forms.ModelForm):
    class Meta:
        model = Form
        exclude=['reg_date', 'is_evaluated']
