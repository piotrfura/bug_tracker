from django import forms
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit

from main.models import BugReport


class BugReportForm(forms.ModelForm):
    """
    Django ModelForm for submitting bug reports.

    Allows users to provide a title and a detailed description of a bug.
    Uses crispy-forms with Bootstrap 5 styling for a user-friendly layout.

    Fields:
        - title: The title of the bug report.
        - description: A detailed description of the issue.

    Additional:
        - Sets custom labels and help text for fields.
        - Defines the form layout with a submit button.
    """
    class Meta:
        model = BugReport
        fields = [
            'title',
            'description',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Bug title'
        self.fields['description'].label = 'Bug description'
        self.fields['description'].help_text = 'Be as detailed as possible to help us understand the issue.'
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Bug Report Form',
                FloatingField('title', required=True),
                FloatingField('description', required=True),
            ),
            Submit('submit', 'Submit the bug', css_class='btn-time-primary w-100'),
        )
