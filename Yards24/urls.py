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
from Sort.views import sorting
from OTP.views import send_otp
from OTP.views import verify_otp
from OTP.views import view_send_otp
from django.conf import settings
from django.conf.urls.static import static
from HomeScreen.views import view_home
from Property.views import view_property_view
from Search.views import view_search
from Enquiry.views import enquiry
from Details.views import show_property
from Contact.views import contact_form
from Favorites.views import add_favorite
from Favorites.views import show_favorite
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home', home),
    url(r'^choose_property', choose_property),
    url(r'^search', search),
    url(r'^sort', sorting),
    url(r'^send_otp', send_otp),
    url(r'^verify_otp', verify_otp),
    url(r'^view_send_otp', view_send_otp),
    url(r'view_home', view_home),
    url(r'view_property', view_property_view),
    url(r'^view_search', view_search),
    url(r'^enquire', enquiry),
    url(r'^show_property', show_property),
    url(r'^contact_form', contact_form),
    url(r'^add_favorite', add_favorite),
    url(r'^show_favorite', show_favorite),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
