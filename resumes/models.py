from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    TEMPLATE_CHOICES = [
        ('classic', 'Classic'),
        ('modern', 'Modern'),
        ('professional', 'Professional'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)

    summary = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    projects = models.TextField(blank=True, null=True)

    template = models.CharField(
        max_length=50,
        choices=TEMPLATE_CHOICES,
        default='classic'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title