from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import ugettext_lazy as _

from django.urls import reverse

from django.db.models.signals import post_save

from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator

from datetime import date

phone_regex = RegexValidator(regex=r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$', \
	message=_("Invalid phone number format. Enter as 1-123-456-7890."))

zip_regex = RegexValidator(regex=r'^[0-9]{2,6}(?:-[0-9]{4})?$|^$', message=_("Plese Enter a valid zip code."))


LANGUAGE_CATEGORY = (
	('EN', _('English')),
	('CN', _('Chinese')),
)

class User(AbstractUser):
	email = models.EmailField(blank=False, default='', unique=True, verbose_name = _("Email"))
	email_confirmed = models.BooleanField(default =False, verbose_name= _('Email Confirmed'))
	email_confirmed.boolean = True

	phone = models.CharField(validators=[phone_regex], max_length=16, blank=True, default='',verbose_name= _('Phone Number'))
	default_address = models.ForeignKey('Address', on_delete=models.SET_NULL, blank=True, null=True,  related_name='default_address', verbose_name= _('Default Shipping Address'))

	reward = models.PositiveIntegerField(default = 0, verbose_name= _('Reward Points'))
	birthday = models.DateField(blank=True, null=True,verbose_name= _('Birthday'))
	updated_date = models.DateTimeField(auto_now = True, blank=True, null=True, verbose_name=_('Profile Updated Date'))
	country = models.CharField(max_length=100, blank=True, default='',verbose_name= _('Country'))
	language = models.CharField(max_length=100, choices=LANGUAGE_CATEGORY,  blank=True, default='',verbose_name= _('Preferred Language'))
	privacy_policy_agree = models.BooleanField(default =False, verbose_name= _('Privacy Policy Agreement'))
	memo = models.TextField(blank = True, default='', verbose_name= _('Memo'))

	def __str__(self):
		if self.first_name and self.last_name:
			return '%s %s: %s'%(self.first_name, self.last_name, self.email)
		else:
			return '%s : %s'%(self.username, self.email)


	class Meta(AbstractUser.Meta):
		verbose_name_plural = _("Users")
		ordering = ['-id']

class Address_Common_Info(models.Model):
	created_date = models.DateTimeField(auto_now_add = True, blank=True, null=True, verbose_name= _('Creation Date'))
	address = models.CharField(max_length=500, default='',verbose_name=_('address'))
	apt = models.CharField(blank=True, max_length=200, default='',verbose_name=_('Address2/Apartment'))
	city = models.CharField(max_length=100, default='',verbose_name= _('City'))
	state = models.CharField(max_length=100, default='',verbose_name= _('State/Province'))
	country = models.CharField(max_length=100, default='',verbose_name=_( 'Country'))
	zipcode = models.CharField(max_length=12, validators=[zip_regex], default='', verbose_name= _('Zip Code'))
	memo = models.TextField(blank = True, default='', verbose_name= _('Memo'))

	class Meta:
		abstract = True

class Address(Address_Common_Info):
	updated_date = models.DateTimeField(auto_now = True, blank=True, null=True, verbose_name= _('Address Updated Date'))
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name= _('User'))
	first_name = models.CharField(max_length=100, default='',verbose_name= _('First Name'))
	last_name = models.CharField(max_length=100, default='',verbose_name= _('Last Name'))
	phone = models.CharField(validators=[phone_regex], max_length=16, default='',verbose_name= _('Phone Number'))

	class Meta:
		verbose_name_plural = _("Addresses")
		unique_together=('user',
		'first_name',
		'last_name',
		'phone',
		'address',
		'apt',
		'city',
		'state',
		'zipcode'
		)

