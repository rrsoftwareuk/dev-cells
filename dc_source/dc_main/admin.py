from django.contrib import admin
from .models import Profile, Relationship, Action, Review

# Register your models here.

admin.site.register(Profile)
admin.site.register(Relationship)
admin.site.register(Action)
admin.site.register(Review)