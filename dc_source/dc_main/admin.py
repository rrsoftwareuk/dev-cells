from django.contrib import admin
from .models import Profile, Relationship, Action, Review, dev_cell_rating, performance_rating, grade, potential_grade, location, position

# Register your models here.

admin.site.register(Profile)
admin.site.register(Relationship)
admin.site.register(Action)
admin.site.register(Review)
admin.site.register(dev_cell_rating)
admin.site.register(performance_rating)
admin.site.register(grade)
admin.site.register(potential_grade)
admin.site.register(location)
admin.site.register(position)
