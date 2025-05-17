# accounts/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


User = get_user_model()

class RoommateRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
        ('Cancelled', 'Cancelled'),
    ]

    sender = models.ForeignKey(User, related_name='sent_roommate_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_roommate_requests', on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('sender', 'receiver')
        ordering = ['-created']

    def __str__(self):
        return f"{self.sender.username} → {self.receiver.username} ({self.status})"
