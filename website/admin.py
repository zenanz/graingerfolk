from django.contrib.admin import AdminSite
from django.contrib import admin
from django.contrib.auth.models import User, Group
# Register your models here.

class UserAdmin(AdminSite):
    site_header = 'Grainger Folk Song Platform'
    site_title = 'User Administration'
    index_title = 'User Administration'

user_admin = UserAdmin(name='useradmin')

user_admin.register(User)
user_admin.register(Group)