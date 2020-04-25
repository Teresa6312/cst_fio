from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from .models import User, Address, Notic
from .forms import NewUserChangeForm, NewUserCreationForm, AddressForm
from .code import get_contexts, send_confirmation_email

def home_view(request):
	template_name = 'base/home.html'
	return render(request, template_name)

@login_required
def account_view(request):
	template_name = 'base/account.html'
	contexts = get_contexts(request)
	return render(request, template_name, contexts)

@login_required
def logout_view(request):
	logout(request)
	return redirect(reverse('base:home'))

def register_view(request):
	if request.user.is_authenticated:
		return redirect(reverse('base:account'))

	template_name = 'base/register.html'
	txt = get_contexts(request)

	if request.method == 'POST':
		form = NewUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			try:
				send_confirmation_email(request, user)
				messages.info(request, _('Confirmation link was sent successfully. Please check your email!'))
			except:
				messages.error(request, _('Confirmation link was fail to send! Please double check your emaill address!'))


			username = request.POST['username']
			password = request.POST['password1']
			login_user = authenticate(
				username = username,
				password = password
			)
			login(request, login_user)
			return redirect(reverse('base:account'))
		else:
			txt['form'] = form
			return render(request, template_name, txt)
	else:
		form = NewUserCreationForm()
		txt['form'] = form
		return render(request, template_name, txt)


# def activate_view(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
# 	try:
# 		uid = force_text(urlsafe_base64_decode(uidb64))
# 		user = User.objects.get(pk=uid)
# 	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
# 		user = None
# 	if user is not None and account_activation_token.check_token(user, token):
# 		user.is_active = True
# 		user.email_confirmed = True
# 		user.save()
# 		return redirect('account')
# 	else:
# 		return HttpResponse('Activation link is invalid!')

# def update_profile_view(request):
# 	template_name = 'main/updateprofile.html'
# 	txt = get_contexts(request)
# 	if request.method == 'POST':
# 		form = NewUserChangeForm(request.POST, instance=request.user)
# 		form.fields['password'].required = False
# 		if form.is_valid():
# 			user = form.save()
# 			return redirect(reverse('base:account'), txt, user = user)
# 		else:
# 			txt +={'form': form}
# 			return render(request, template_name, txt)
# 	else:
# 		form = NewUserChangeForm(instance=request.user)
# 		form.fields['password'].required = False
# 		txt +={'form': form}
# 		return render(request, template_name, txt)

# def change_password_view(request):
# 	template_name = 'main/changepassword.html'
# 	txt = get_contexts(request)
# 	if request.method == 'POST':
# 		form = PasswordChangeForm(request.POST, instance=request.user)
# 		if form.is_valid():
# 			form.save()
# 			update_session_auth_hash(request, form.user)
# 			return redirect(reverse('base:account'))
# 		else:
# 			txt +={'form': form}
# 			return render(request, template_name, txt)
# 	else:
# 		form = PasswordChangeForm(instance=request.user)
# 		form.fields['password'].required = False
# 		txt +={'form': form}
# 		return render(request, template_name, txt)


# def send_email_view(request):
# 	if request.method == 'POST':
# 		email = EmailForm(request.POST)
# 		if email.is_valid():
# 			user_email = email.cleaned_data['email'].lower()
# 			subject = _('Contact us - ') + email.cleaned_data['subject']
# 			content = _('User Email: ') + user_email + '\n' + email.cleaned_data['content']
# 			to_email = settings.support_email
# 			if email.cleaned_data['cc']:
# 				to_email.append(user_email)

# 			send_mail(
# 					subject,
# 					content,
# 					settings.DEFAULT_FROM_EMAIL,
# 					to_email,
# 					fail_silently=False,
# 				)
# 		if next and next!='':
# 			return redirect(next)
# 		else:
# 			return redirect(reverse('base:home'))
