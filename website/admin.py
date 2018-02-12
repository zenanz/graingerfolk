from django.contrib.admin import AdminSite
from mptt.admin import MPTTModelAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from website.models import *
# Register your models here.



class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )


class CommentAdminModel(MPTTModelAdmin):
    list_display = ('slug','user','parent', 'time_created')
    filter_horizontal = ('like',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Favourites)
admin.site.register(Comment,CommentAdminModel)