from . import models
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, ButtonHolder, Div, HTML


class CustomerFeedbackForm(forms.ModelForm):
    class Meta:
        model = models.customerFeedback
        fields = ['name', 'email', 'feedback']
    
    def __init__(self, *args, **kwargs):
        super(CustomerFeedbackForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Customer Feedback',
                Div('name', css_class='form-group'),
                Div('email', css_class='form-group'),
                Div('feedback', css_class='form-group'),
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-primary')
            )
        )
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary'))