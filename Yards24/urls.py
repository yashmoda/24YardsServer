"""Yards24 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from HomeScreen.views import home
from Property.views import choose_property
from Search.views import search
from Sort.views import price_high_to_low
from Sort.views import price_low_to_high
from Sort.views import newest_first
from Sort.views import oldest_first
from OTP.views import send_otp
from OTP.views import verify_otp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', home, name='home'),
    url(r'^choose_property/$', choose_property, name='choose_property'),
    url(r'^search/$', search, name='search'),
    url(r'^descend/$', price_high_to_low, name='descend'),
    url(r'^ascend/$', price_low_to_high, name='ascend'),
    url(r'^latest/$', newest_first, name='latest'),
    url(r'^oldest/$', oldest_first, name='oldest'),
    url(r'^send_otp/$', send_otp, name='send_otp'),
    url(r'^verify_otp/$', verify_otp, name='verify_otp'),
]
