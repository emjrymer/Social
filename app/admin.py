from django.contrib import admin

# Register your models here.
from app.models import UserProfile, Alcohol, Suggestion, Follower

admin.site.register(UserProfile)
admin.site.register(Alcohol)
admin.site.register(Suggestion)
admin.site.register(Follower)
