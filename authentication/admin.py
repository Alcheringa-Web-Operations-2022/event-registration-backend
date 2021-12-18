from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from authentication.models import NewUser


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email','username', 'fullname',)
    list_filter = ('email',  'username','fullname',
                   'is_active', 'is_staff', 'id')
    ordering = ('-date_joined',)
    list_display = ('email', 'username', 'fullname',
                    'is_active', 'is_staff', 'id',)
    fieldsets = (
        (None, {'fields': ('email', 'collegename', 'username',
         'fullname', 'id','city')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about', 'phone', 'provider')}),
    )
    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'collegename', 'fullname', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
