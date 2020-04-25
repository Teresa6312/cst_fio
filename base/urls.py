from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views


app_name = 'base'
urlpatterns = [
# open for everyone
    path('', views.home_view, name = 'home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='base/login.html'), name = 'login'),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #         views.activate_view, name='activate_account'),
    path('accounts/register/', views.register_view, name = 'register'),

    # # login_required
    path('account/logout/', views.logout_view, name = 'logout'),
    path('account/', views.account_view, name='account'),
    # path('myaccount/profile/update', views.update_profile_view, name='update_profile'),
    # path('myaccount/change-password/', views.change_password_view, name='change_password'),
]

