from django.shortcuts import render

# Create your views here.
import requests, keysdata
def send_sms(message, phone, sender='CodeNy'):
    url = 'https://control.msg91.com/api/sendhttp.php?authkey=' + keysdata.MSG91 + '&mobiles='
    url += str(phone)
    url += '&message=' + message
    url += '&sender=' + sender + '&route=4&country=91'
    print url
    print requests.request('GET', url)