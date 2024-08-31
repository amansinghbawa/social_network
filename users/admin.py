from django.contrib import admin
from .models import FriendRequest, User


# Register your models here.
class FriendRequestAdmin(admin.ModelAdmin):
    pass


admin.site.register(FriendRequest, FriendRequestAdmin)
admin.site.register(User)
