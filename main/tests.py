from django.test import TestCase
from main.models import BugReport

class BugReportModelTest(TestCase):
    def setUp(self):
        BugReport.objects.create(title="Test Bug", description="This is a test bug report.")

    def test_bug_report_creation(self):
        """Test that a BugReport can be created."""
        bug_report = BugReport.objects.get(title="Test Bug")
        self.assertEqual(bug_report.description, "This is a test bug report.")

    def test_bug_report_str(self):
        """Test the string representation of the BugReport model."""
        bug_report = BugReport.objects.get(title="Test Bug")
        self.assertEqual(str(bug_report), "Test Bug")
