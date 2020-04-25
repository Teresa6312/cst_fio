from .models import Notic
from django.utils.translation import ugettext_lazy as _

def get_contexts(request):
	notic = Notic.objects.order_by('-created_date').first()
	contexts = {
		'notic': notic if notic and notic.open else None,
	}
	if request.user.is_authenticated:
		contexts['package_num'] = 99
		return contexts
	return contexts

def send_confirmation_email(request):
	if request.user.email:
		try:
			send_confirmation_email(request, request.user)
			messages.info(request, _('Confirmation link was sent successfully. Please check your email!'))
		except:
			messages.error(request, _('Confirmation link was fail to send!'))
	else:
		messages.error(request, _('Failure! Please check your email.'))