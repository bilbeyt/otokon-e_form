from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import Accordion, AccordionGroup
from .models import Form
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import widgets


class FormCreateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'
    helper.layout = Layout(
        Accordion(
            AccordionGroup(_('Personal Information'),
                'name',
                'department',
                'school_number',
                'birthday',
            ),
            AccordionGroup(_('Contact'),
                'phone_number',
                'mail',
            ),
            AccordionGroup(_('Technical'),
                'interests',
                'tech_info',
                'experience',
            ),
            AccordionGroup(_('What do you want to do ?'),
                'is_projects',
                'is_education',
                'is_informatics',
                'is_magazine',
                'is_robot',
            )
        )
    )
    class Meta:
        model = Form
        exclude=['reg_date', 'is_evaluated']

    def __init__(self, *args, **kwargs):
        super(FormCreateForm, self).__init__(*args, **kwargs)
        self.fields['birthday'] = forms.DateField(widget=widgets.AdminDateWidget())
