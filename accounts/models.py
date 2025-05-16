# accounts/models.py
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    USER_TYPES = [
        ('User', 'User'),
        ('Admin', 'Admin'),
    ]
    STATUS_TYPES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('prefer_not_to_say', 'Prefer not to say'),
    ]

    SLEEP_SCHEDULE = [
        ('early_bird', 'Early Bird'),
        ('night_owl', 'Night Owl'),
        ('flexible', 'Flexible'),
    ]

    CLEANLINESS_LEVEL = [
        ('neat', 'Neat'),
        ('average', 'Average'),
        ('messy', 'Messy'),
    ]

    SOCIAL_HABITS = [
        ('introvert', 'Introvert'),
        ('extrovert', 'Extrovert'),
        ('ambivert', 'Ambivert'),
    ]

    STUDY_PREFERENCE = [
        ('quiet', 'Quiet and private'),
        ('group', 'Group study'),
        ('mixed', 'Mixed'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='User')
    verification_status = models.CharField(max_length=20, choices=STATUS_TYPES, default='pending')
    verified_at = models.DateTimeField(null=True, blank=True)

    # Personal Info
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Matching Preferences
    sleep_schedule = models.CharField(max_length=20, choices=SLEEP_SCHEDULE, blank=True, null=True)
    cleanliness_level = models.CharField(max_length=20, choices=CLEANLINESS_LEVEL, blank=True, null=True)
    social_habits = models.CharField(max_length=20, choices=SOCIAL_HABITS, blank=True, null=True)
    study_preference = models.CharField(max_length=20, choices=STUDY_PREFERENCE, blank=True, null=True)

    # Additional Preferences
    hobbies = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)

    # Profile Picture
    profile_picture = models.ImageField(upload_to='media/profile_pictures/', blank=True, null=True, )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"
    
    def get_age(self):
        if self.date_of_birth:
            from datetime import date
            return date.today().year - self.date_of_birth.year
        return None
