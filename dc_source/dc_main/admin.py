from django.contrib import admin
from .models import Profile, Relationship, Action, Review, ActionStatus, Mobility, Succession

# Register your models here.

admin.site.register(Profile)
admin.site.register(Relationship)
admin.site.register(Action)
admin.site.register(Review)
admin.site.register(ActionStatus)
admin.site.register(Mobility)
admin.site.register(Succession)