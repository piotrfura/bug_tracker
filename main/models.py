from django.db import models


class Timestamped(models.Model):
    """
    Abstract base model that provides a creation timestamp.

    Fields:
        - created_at: Date and time when the object was created (automatically set on creation).

    Intended for inheritance by other models to add creation tracking.
    """
    created_at = models.DateTimeField(auto_now_add=True)


# BugReport model with: title, description, created_at
class BugReport(Timestamped):
    """
    Model representing a bug report submitted by users.

    Inherits timestamp information from the Timestamped base model.
    Stores the title and detailed description of the reported issue.

    Fields:
        - title: The title of the bug report.
        - description: A detailed description of the bug.
        - created_at: The date and time when the report was created (inherited).

    Meta:
        - verbose_name: Human-readable singular name for the model.
        - verbose_name_plural: Human-readable plural name for the model.

    Methods:
        - __str__: Returns the title of the bug report.
    """
    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = "Bug Report"
        verbose_name_plural = "Bug Reports"

    def __str__(self):
        return self.title
