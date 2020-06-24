"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from users import views as us
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from bike import views as b
from django.conf.urls import url,re_path
from bike.models import COBBikesData


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mainpage,name='mainpage'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('signup',us.register,name='signup'),
    path('login',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),

    path('password-reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),

    path('profile',us.profile,name='profile'),

    path('bike',views.bike,name='bike'),
    path('scooter',views.scooter,name='scooter'),
    path('bookbk',b.bikebook,name='bookbk'),
    path('booksc',b.scbook,name='booksc'),
    path('booked',b.booked,name='booked'),
    path('bdetail/<int:id>',b.bdetail,name='bdetail'),
    path('sdetail/<int:id>',b.sdetail,name='sdetail'),
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)