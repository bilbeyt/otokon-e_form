from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab
from .models import Form
from django.utils.translation import ugettext_lazy as _


class FormCreateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-10'
    helper.form_tag = False
    helper.layout = Layout(
        TabHolder(
            Tab(
                _('Personal Information'),
                'name',
                'department',
                'school_number',
                'term',
                'birthday',
                'interests',
                'tech_info',
            ),
            Tab(
                _('Contact'),
                'phone_number',
                'mail',
                'dorm_adress',
                'home_adress',
            ),
            Tab(
                _('Join Teams'),
                'is_organization',
                'is_technical',
                'is_informatics',
                'is_education',
                'is_publish',
                'is_social',
            )
        )
    )

    class Meta:
        model = Form
        exclude=['reg_date', 'is_evaluated']

    def __init__(self, *args, **kwargs):
        super(FormCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
            if help_text != '':
                self.fields[field].widget.attrs.update({'class':'has-popover', 'data-content':help_text, 'data-placement':'right', 'data-container':'body'})
