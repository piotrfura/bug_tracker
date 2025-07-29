from django.urls import path

from main.views import create_bug_report
from main.views import index
from main.views import list_bug_reports


app_name = "main"

urlpatterns = [
    path('', index, name='index'),
    path("bugs/", list_bug_reports, name="list_bug_reports"),
    path("bugs/create/", create_bug_report, name="create_bug_report"),
]

admin.site.site_title = "Bug Tracker Admin Portal"
