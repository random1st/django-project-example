from django.contrib import admin

from db.core.models import BaseUser, UserBalance


@admin.register(BaseUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'first_name', 'last_name', 'username', 'is_staff', 'created_date', 'modified_date',
        'balance'
    )
    search_fields = ('email', 'username')
    list_filter = ('is_staff',)
