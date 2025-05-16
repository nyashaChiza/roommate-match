# accounts/admin.py
from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'user_type', 'verification_status', 'gender', 'date_of_birth',
        'sleep_schedule', 'cleanliness_level', 'social_habits', 'study_preference',
        'created', 'updated',
    )
    list_filter = (
        'user_type', 'verification_status', 'gender', 'sleep_schedule',
        'cleanliness_level', 'social_habits', 'study_preference',
    )
    search_fields = ('user__username', 'user__email', 'hobbies', 'interests')
    readonly_fields = ('created', 'updated', 'verified_at')

    fieldsets = (
        ('Account Info', {
            'fields': ('user', 'user_type', 'verification_status', 'verified_at')
        }),
        ('Personal Details', {
            'fields': ('gender', 'date_of_birth', 'address', 'profile_picture')
        }),
        ('Lifestyle & Preferences', {
            'fields': (
                'sleep_schedule', 'cleanliness_level',
                'social_habits', 'study_preference',
                'hobbies', 'interests'
            )
        }),
        ('Timestamps', {
            'fields': ('created', 'updated')
        }),
    )
