# accounts/admin.py

from django.contrib import admin
from .models import RoommateRequest


@admin.register(RoommateRequest)
class RoommateRequestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'status', 'created', 'updated')
    list_filter = ('status', 'created')
    search_fields = ('sender__username', 'receiver__username', 'message')
    readonly_fields = ('created', 'updated')
