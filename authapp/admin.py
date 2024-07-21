from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register the default User model with the admin site
admin.site.unregister(User)  # Unregister the default User model
admin.site.register(User, UserAdmin)
