from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Attendance, Feedback

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role','email')}),
    )
    list_display = ('username','email','role','is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Attendance)
admin.site.register(Feedback)
