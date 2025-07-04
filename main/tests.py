from django.test import TestCase

from main.forms import BugReportForm
from main.models import BugReport
from main.views import create_bug_report
from main.views import index
from main.views import list_bug_reports


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


class IndexViewTest(TestCase):
    """
    Test case for the index view.

    Verifies that the index view returns a 200 status code and renders the correct template.
    """
    def test_index_view(self):
        """Test that the index view loads successfully."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')


class ListBugReportsViewTest(TestCase):
    """
    Test case for the list_bug_reports view.

    Verifies that the view returns a 200 status code and renders the correct template.
    """
    def setUp(self):
        """Set up by creating a sample bug report."""
        BugReport.objects.create(title="Sample Bug", description="This is a sample bug report.")

    def test_list_bug_reports_view(self):
        """Test that the list_bug_reports view loads successfully."""
        response = self.client.get('/bugs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/bug_reports.html')
        self.assertContains(response, "Sample Bug")


class CreateBugReportViewTest(TestCase):
    """
    Test case for the create_bug_report view.

    Verifies that the view allows creating a new bug report and redirects correctly.
    """
    def test_create_bug_report_view(self):
        """Test that the create_bug_report view allows creating a new bug report."""
        response = self.client.post('/bugs/create/', {
            'title': 'New Bug',
            'description': 'This is a new bug report.'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful creation
        self.assertTrue(BugReport.objects.filter(title='New Bug').exists())
