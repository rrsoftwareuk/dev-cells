from django.contrib import admin
from .models import Profile, Relationship, Action, Review, dev_cell_rating, performance_rating, grade, potential_grade, location, position

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
admin.site.register(dev_cell_rating)
admin.site.register(performance_rating)
admin.site.register(grade)
admin.site.register(potential_grade)
admin.site.register(location)
admin.site.register(position)