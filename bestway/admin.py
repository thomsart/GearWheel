from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bestway.models import User
from .form import AccountForm, LoginForm

# Register your models here.

class UserAdmin(UserAdmin):
    add_form = AccountForm
    form = LoginForm
    model = User
    list_display = ['username', 'password']

#admin.site.register(ClientUser, ClientUserAdmin)