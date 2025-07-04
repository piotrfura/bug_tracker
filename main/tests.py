from django.test import TestCase
from main.models import BugReport
from main.forms import BugReportForm


class BugReportModelTest(TestCase):
    """
    Test case for the BugReport model.

    Verifies correct creation of bug reports and their string representation.
    """
    def setUp(self):
        """
        Set up the test environment by creating a sample bug report.
        """
        BugReport.objects.create(title="Test Bug", description="This is a test bug report.")

    def test_bug_report_creation(self):
        """Test that a BugReport can be created."""
        bug_report = BugReport.objects.get(title="Test Bug")
        self.assertEqual(bug_report.description, "This is a test bug report.")

    def test_bug_report_str(self):
        """Test the string representation of the BugReport model."""
        bug_report = BugReport.objects.get(title="Test Bug")
        self.assertEqual(str(bug_report), "Test Bug")


class BugReportFormTest(TestCase):
    """
    Test case for the BugReportForm.

    Verifies form validation and field attributes.
    """
    def test_form_valid(self):
        """Test that the form is valid with correct data."""
        form_data = {
            'title': 'Valid Bug Title',
            'description': 'This is a valid bug description.'
        }
        form = BugReportForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        """Test that the form is invalid with missing required fields."""
        form_data = {
            'title': '',
            'description': ''
        }
        form = BugReportForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('description', form.errors)

