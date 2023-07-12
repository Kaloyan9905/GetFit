from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.

UserModel = get_user_model()


@admin.register(UserModel)
class AuthUserAdmin(UserAdmin):
    pass

# D6+kaosc12
