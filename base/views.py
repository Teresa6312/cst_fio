from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = 'base/home.html'

	def get(self, request):
		return render(request, self.template_name)
