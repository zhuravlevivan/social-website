from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/registration/logged_out.html'), name='logout'),
    path('', views.dashboard, name='dashboard'),
    # url-адреса смены пароля
    path('password-change/',
         auth_views.PasswordChangeView.as_view(template_name='account/registration/password_change_form.html'),
         name='password_change'),
    path('password-change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='account/registration/password_change_done.html'),
         name='password_change_done'),
    # url-адреса сброса пароля
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='account/registration/password_reset_form.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='account/registration/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='account/registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
