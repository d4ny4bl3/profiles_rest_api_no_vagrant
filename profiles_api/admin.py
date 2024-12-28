from django.contrib import admin

from profiles_api import models
# nebo:
# from .models import UserProfile


admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
