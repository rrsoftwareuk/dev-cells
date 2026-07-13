from django.contrib import admin
from django.contrib.admin import actions

from .models import Profile, Relationship, Action, Review

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'role', 'dev_cell_rating', 'performance_rating', 'grade')

class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user')

class ActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'action_owner', 'action_status')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'review_date')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Relationship, RelationshipAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(Review, ReviewAdmin)