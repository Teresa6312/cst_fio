from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import NewUserCreationForm, NewUserChangeForm
from .models import (
	User, Address
)
from django.utils.html import mark_safe

# admin.site.unregister(User)

class AddressInline(admin.StackedInline):
	model = Address
	can_delete = False
	extra = 1
	can_delete = False
	fields = ('first_name', 'last_name', 'phone', 'address', 'city', 
                'state','country', 'zipcode','memo')
	verbose_name_plural = 'address list'


# Define a new User admin
class NewUserAdmin(UserAdmin):
	model = User
	add_form = NewUserCreationForm
	form = NewUserChangeForm

	inlines = (AddressInline, )
	list_filter = ('country',)
	list_display = ('username', 'first_name', 'last_name','email',
                    'email_confirmed',  'phone', 'country', 'reward')
	search_fields = ('username','first_name', 'last_name', 'email', 'phone')

	fieldsets = (
		(None, 		            {'fields': ('username', 'password')}),
		('Personal info',       {'fields': ('first_name', 'last_name', 'email', 'email_confirmed',
                                        'phone', 'country', 'language', 'default_address',
                                        'reward', 'birthday','privacy_policy_agree', 'memo')}),
		('Permissions',         {'fields': ('is_active', 'is_staff', 'is_superuser', 
                                    'groups', 'user_permissions')}),
		('Important dates',     {'fields': ('last_login', 'date_joined')}),
	)


admin.site.register(User, NewUserAdmin)

class AddressAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'first_name', 'last_name', 'phone',
                    'address','apt',  'city', 'state','country', 'zipcode')
	list_editable = ('phone', 'address','apt',  'city', 'state','country', 'zipcode')
	list_filter = ('country', 'state','city')
	search_fields = ('first_name', 'last_name')

	fieldsets = (
		('User', 				{'fields': ('user',)}),
		('Address',             {'fields': ('first_name', 'last_name', 'phone', 
                                            'address', 'city', 'state','country', 'zipcode')}),
		('Memo', 				{'fields': ('memo',)}),
	)

admin.site.register(Address, AddressAdmin,)