from django.shortcuts import render

# Create your views here.
import requests
def send_sms(message, phone, sender='CodeNy'):
    authkey = '125195AnE7snTWFepK5925ea7c'
    url = 'https://control.msg91.com/api/sendhttp.php?authkey=' + authkey + '&mobiles='
    url += str(phone)
    url += '&message=' + message
    url += '&sender=' + sender + '&route=4&country=91'
    print url
    print requests.request('GET', url)