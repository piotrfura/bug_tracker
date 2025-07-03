from django.contrib import admin
from main.models import BugReport


# Registering the BugReport model with the Django admin interface
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    list_filter = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at',)
