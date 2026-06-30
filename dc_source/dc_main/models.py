from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    ROLE_CHOICES = [
        ("individual", "Individual"),
        ("manager", "Manager"),
        ("quorum", "Quorum"),
        ("admin", "Admin")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    name = models.CharField(max_length=32)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    grade = models.CharField(max_length=16)
    position = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    history = models.TextField(blank=True)
    capabilities_and_attributes = models.TextField(blank=True)
    career_aspirations = models.TextField(blank=True)
    development_needs = models.TextField(blank=True)
    mobility = models.CharField(max_length=128)
    succession_plan = models.TextField(blank=True)
    successor = models.ForeignKey(User, null = True, on_delete=models.SET_NULL, related_name="successor_profile")
    potential_grade = models.CharField(max_length=16)
    dev_cell_rating = models.CharField(max_length=16)
    performance_rating = models.CharField(max_length=16)
    wants = models.TextField(blank=True)
    needs = models.TextField(blank=True)


class Relationship(models.Model):
    RELATIONSHIP_TYPES = [
        ("manager", "Manager"),
        ("mentor", "Mentor"),
    ]

    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="relationships_from")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="relationships_to")

    relationship_type = models.CharField(max_length=20, choices=RELATIONSHIP_TYPES)


class Action(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="actions")
    action = models.CharField(max_length=32)
    action_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    next_move = models.TextField(blank=True)
    action_status = models.CharField(max_length=32)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_date = models.DateField()
    review_information = models.TextField(blank=True)
