from django.db import models


class Timestamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


# BugReport model with: title, description, created_at
class BugReport(Timestamped):
    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = "Bug Report"
        verbose_name_plural = "Bug Reports"

    def __str__(self):
        return self.title
