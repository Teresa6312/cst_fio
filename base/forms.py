from django import forms
from .models import (
	User, Address, phone_regex, zip_regex, LANGUAGE_CATEGORY
	)

from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _

import datetime

year = datetime.datetime.now().year
birthday_years = [i for i in range(year-100,year)]

class NewUserCreationForm(UserCreationForm):
	birthday = forms.DateField(required = False, widget=forms.SelectDateWidget(
						empty_label=("YYYY", "MM", "DD"),
					years = birthday_years))
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username', 'email', 'first_name', 'last_name',
					'phone', 'country', 'language', 'birthday', 'password1', 'password2', 'privacy_policy_agree')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# self.fields['birthday'].label = _('Birthday')
		self.fields['country'].initial = 'USA'
		self.fields['phone'].validators = [phone_regex]
		self.fields['language'].choices = LANGUAGE_CATEGORY
		self.fields['phone'].widget.attrs['placeholder'] = _('+1-234-567-8900')
		self.fields['privacy_policy_agree'].required = True

	def save(self, commit=True, *args, **kwargs):
		user = super(NewUserCreationForm, self).save(commit=False, *args, **kwargs)
		user.first_name = user.first_name.title()
		user.last_name = user.last_name.title()
		user.email = user.email.lower()
		if commit:
			user.save()
		return user

class NewUserChangeForm(UserChangeForm):
	birthday = forms.DateField(required = False, widget=forms.SelectDateWidget(
				empty_label=("YYYY", "MM", "DD"),
				years = birthday_years))

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name',
					'phone', 'country', 'language', 'birthday',
					'default_address', 'password',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['birthday'].label = _('Birthday')
		self.fields['country'].initial = 'USA'
		self.fields['phone'].validators = [phone_regex]
		self.fields['language'].choices = LANGUAGE_CATEGORY
		self.fields['phone'].widget.attrs['placeholder'] = _('+1-234-567-8900')
		if self.instance:
			try:
				user = User.objects.get(id = self.instance.id)
				if user.email_confirmed:
					self.fields['email'].widget.attrs['readonly'] = True
				if user.birthday:
					self.fields['birthday'].widget.attrs['readonly'] = True
			except:
				pass

	def save(self, commit=True, *args, **kwargs):
		user = super(NewUserChangeForm, self).save(commit=False, *args, **kwargs)
		user.first_name = user.first_name.title()
		user.last_name = user.last_name.title()
		user.email = user.email.lower()
		if commit:
			user.save()
		return user


class AddressForm(forms.ModelForm):

	class Meta:
		model = Address
		exclude = ('meno',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['apt'].widget.attrs['placeholder'] = _('Apartment/Suit/Unit')
		self.fields['phone'].widget.attrs['placeholder'] = _('+1-234-567-8900')
		self.fields['phone'].validators = [phone_regex]
		self.fields['address'].widget.attrs['placeholder'] = _('Street Address')


	def save(self, commit=True, *args, **kwargs):
		add = super(AddressForm, self).save(commit=False, *args, **kwargs)
		add.first_name = add.first_name.title()
		add.last_name = add.last_name.title()
		add.address = add.address.title()
		add.apt = add.apt.title()
		add.city = add.city.title()
		add.state = add.state.title()
		if commit:
			add.save()
		return add
