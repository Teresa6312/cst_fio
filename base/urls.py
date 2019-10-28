from . import views
from django.urls import path, re_path

# , permission_required



urlpatterns = [
# open for everyone
    path('', views.HomeView.as_view(), name = 'home'),
]

