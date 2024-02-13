"""gestschoolproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))0
"""

from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView
from gestschools import views
from .views import menu
from gestschools.views import login_view, register_view, logout_view,eleve,menueleve,classe,enseignant,menu
# from . import views
from  django.contrib.auth import views as auth_views




urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    # path('gestschools/menu/', menu, name='menu'),
    path('gestschools/register/', register_view),
    # path('gestschools/logout/', logout_view),
    # path(r'logout', views.logout_view, name='logout'),

    path('gestschools/', include('gestschools.urls')),
    
    
    path('menu/', views.menu, name='menu'),
    # path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),


    path(r'password_reset/', auth_views.PasswordResetView.as_view(template_name='gestschools/registration/password_reset_form.html', success_url="done"), name='password_reset'),
    path(r'password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='gestschools/registration/password_reset_done.html'), name='password_reset_done'),
    path(r'password_change/form/', auth_views.PasswordChangeView.as_view(template_name='gestschools/registration/password_change_form.html'), name='password_change_form'),
    path(r'password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='gestschools/registration/password_change_done.html'), name='password_change_done'),
    path(r'reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='gestschools/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path(r'reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='gestschools/registration/password_reset_complete.html'), name='password_reset_complete'),

]  



