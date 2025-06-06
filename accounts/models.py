# accounts/models.py
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    USER_TYPES = [
        ('User', 'User'),
        ('Admin', 'Admin'),
    ]
    STATUS_TYPES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Prefer not to say', 'Prefer not to say'),
    ]

    SLEEP_SCHEDULE = [
        ('Early Bird', 'Early Bird'),
        ('Night Owl', 'Night Owl'),
        ('Flexible', 'Flexible'),
    ]

    CLEANLINESS_LEVEL = [
        ('Neat', 'Neat'),
        ('Average', 'Average'),
        ('Messy', 'Messy'),
    ]

    SOCIAL_HABITS = [
        ('Introvert', 'Introvert'),
        ('Extrovert', 'Extrovert'),
        ('Ambivert', 'Ambivert'),
    ]

    STUDY_PREFERENCE = [
        ('Quiet', 'Quiet and private'),
        ('Group', 'Group study'),
        ('Mixed', 'Mixed'),
    ]

    NOISE_TOLERANCE = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    COOKING_FREQUENCY = [
        ('Rarely', 'Rarely'),
        ('Sometimes', 'Sometimes'),
        ('Frequently', 'Frequently'),
    ]

    GUEST_POLICY = [
        ('Never', 'Never'),
        ('Sometimes', 'Sometimes'),
        ('Often', 'Often'),
    ]

    PET_PREFERENCE = [
        ('No pets', 'No pets'),
        ('Okay with pets', 'Okay with pets'),
        ('Have pets', 'Have pets'),
    ]

    SMOKING_PREFERENCE = [
        ('Non-smoker', 'Non-smoker'),
        ('Okay with smoking', 'Okay with smoking'),
        ('Smoker', 'Smoker'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='User')
    verification_status = models.CharField(max_length=20, choices=STATUS_TYPES, default='pending')
    verified_at = models.DateTimeField(null=True, blank=True)

    # Personal Info
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    Phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Matching Preferences
    sleep_schedule = models.CharField(max_length=20, choices=SLEEP_SCHEDULE, blank=True, null=True)
    cleanliness_level = models.CharField(max_length=20, choices=CLEANLINESS_LEVEL, blank=True, null=True)
    social_habits = models.CharField(max_length=20, choices=SOCIAL_HABITS, blank=True, null=True)
    study_preference = models.CharField(max_length=20, choices=STUDY_PREFERENCE, blank=True, null=True)
    noise_tolerance = models.CharField(max_length=20, choices=NOISE_TOLERANCE, blank=True, null=True)
    cooking_frequency = models.CharField(max_length=20, choices=COOKING_FREQUENCY, blank=True, null=True)
    guest_policy = models.CharField(max_length=20, choices=GUEST_POLICY, blank=True, null=True)
    pet_preference = models.CharField(max_length=20, choices=PET_PREFERENCE, blank=True, null=True)
    smoking_preference = models.CharField(max_length=20, choices=SMOKING_PREFERENCE, blank=True, null=True)

    # Additional Preferences
    hobbies = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s profile"


    # Profile Picture
    profile_picture = models.ImageField(upload_to='media/profile_pictures/', blank=True, null=True, )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    def get_age(self):
        if self.date_of_birth:
            from datetime import date
            return date.today().year - self.date_of_birth.year
        return None
