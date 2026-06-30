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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    name = models.CharField(max_length=16)
    # Photo = models.ImageField(upload_to='photos/')
    grade = models.CharField(max_length=16)
    position = models.CharField(max_length=16)
    location = models.CharField(max_length=16)
    history = models.TextField(max_length=256)
    capabilities_and_attributes = models.TextField(max_length=256)
    career_aspirations = models.TextField(max_length=256)
    development_needs = models.TextField(max_length=256)
    mobility = models.TextField(max_length=128)
    succession_plan = models.TextField(max_length=256)
    successor = models.CharField(max_length=32)
    potential_grade = models.CharField(max_length=16)
    dev_cell_rating = models.CharField(max_length=16)
    performance_rating = models.CharField(max_length=16)
    wants = models.TextField(max_length=256)
    needs = models.TextField(max_length=256)


class Relationship(models.Model):
    RELATIONSHIP_TYPES = [
        ("manager", "Manager"),
        ("mentor", "Mentor"),
    ]

    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="relationships_from")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="relationships_to")

    relationship_type = models.CharField(max_length=20, choices=RELATIONSHIP_TYPES)


class Action(models.Model):
    action = models.CharField(max_length=16)
    action_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    next_move = models.TextField(max_length=128)
    action_status = models.CharField(max_length=32)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_date = models.DateField()
    review_information = models.TextField(max_length=32)
