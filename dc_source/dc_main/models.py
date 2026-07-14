from django.db import models
from django.conf import settings
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

    @classmethod
    def create_profile(cls, user, first_name, last_name):
        profile = cls(user=user, name=f'{first_name} {last_name}', role='Individual')
        profile.save()
        return profile

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


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

    @classmethod
    def create_action(cls, user,  action, action_owner, next_move):
        new_action = cls(user=user, action=action, action_owner=action_owner, next_move=next_move)
        new_action.save()
        return new_action

    def __str__(self):
        return f'Action on {self.user.first_name} {self.user.last_name}'


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_date = models.DateField()
    review_information = models.TextField(blank=True)

class dev_cell_rating(models.Model):
    grade = models.CharField(max_length=32)

class performance_rating(models.Model):
    grade = models.CharField(max_length=32)

class grade(models.Model):
    grade = models.CharField(max_length=32)

class potential_grade(models.Model):
    grade = models.CharField(max_length=32)

class location(models.Model):
    location = models.CharField(max_length=32)

class position(models.Model):
    position = models.CharField(max_length=32)

    @classmethod
    def create_review(cls, user, review_date, review_information):
        new_review = cls(user=user, date=review_date, information=review_information)
        new_review.save()
        return new_review

    def __str__(self):
        return f'Review on {self.user.first_name} {self.user.last_name}'
