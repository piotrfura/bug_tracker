from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

from main.forms import BugReportForm
from main.models import BugReport


def index(request):
    """
    View function for the homepage.

    Displays a welcome message and renders the index page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML for the index page.
    """
    messages.success(request, "Welcome to the BugTracker!")
    return render(request, 'main/index.html')


def list_bug_reports(request):
    """
    View function to list all bug reports.

    Fetches all bug reports from the database, orders them by creation date,
    and renders the bug reports page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML for the bug reports page with context.
    """
    context = {}
    context['bug_reports'] = BugReport.objects.all().order_by('created_at')  # Fetch all bug reports
    return render(request, 'main/bug_reports.html', context)


def create_bug_report(request):
    """
    View function to create a new bug report.

    Handles GET and POST requests for the bug report creation form.
    Validates form data, saves the bug report to the database, and redirects
    to the bug reports list page upon success. Displays error messages if
    creation fails.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML for the bug report creation page or
        redirects to the bug reports list page upon success.
    """
    context = {}
    form = BugReportForm()
    context['form'] = form

    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            try:
                bug_report = BugReport.objects.create(**form.cleaned_data)
                bug_report.save()
                messages.success(request, "Bug report created successfully!")
                return redirect(reverse("main:list_bug_reports"))
            except Exception as e:
                messages.error(request, f"Error creating bug report: {e}")
                return render(request, 'main/create_bug_report.html', context)
        else:
            messages.error(request, "Bug report creation failed. Please try again.")
            return render(request, 'main/create_bug_report.html', context)
    return render(request, 'main/create_bug_report.html', context)
