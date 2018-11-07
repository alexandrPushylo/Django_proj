from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from app1.models import Person

class PersonInline(admin.StackedInline):
    model = Person
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (PersonInline, )
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
