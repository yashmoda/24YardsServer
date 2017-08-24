from django.views.decorators.csrf import csrf_exempt
from random import random, randint

from django.http.response import JsonResponse

from django.shortcuts import render
from OTP.models import OTP
# Create your views here.
import jwt
from SMS.views import send_sms
import constants
import sys
# Create your views here.


@csrf_exempt
def send_otp(request):
    if request.method == 'POST':
        json_response = {}
        try:
            contact = request.POST.get('contact')
            print contact
            otp = randint(100000, 999999)
            try:
                msg = "Your one time password is " + str(otp)
                #send_sms(msg, str(contact))
                print msg
            except Exception as e:
                print e
            try:
                otp_obj = OTP.objects.get(phone=str(contact))
                otp_obj.otp = otp
                otp_obj.save()
            except Exception as e:
                print e
                OTP.objects.create(phone = str(contact), otp = str(otp))
            json_response[constants.success] = constants.true
            json_response[constants.msg] = "OTP SENT"
            pass
        except Exception as e:
            print e
            json_response[constants.success] = constants.false
            json_response[constants.msg] = "OTP NOT SENT"
        print (str(json_response))
        return JsonResponse(json_response)
    print 123
    return render(request, 'sendotp.html')


@csrf_exempt
def verify_otp(request):
    json_response = {constants.success:[], constants.msg:[]}
    if request.method == 'POST':
        try:
            contact = request.POST.get('contact')
            otp = request.POST.get('otp')
            otpobj = OTP.objects.get(phone=str(contact))
            if otpobj.otp == otp:
                access_token = jwt.encode({'mobile': str(contact)}, '810810', algorithm='HS256')
                otpobj.save()
                json_response['access_token'] = str(access_token)
                print('Access Token Created')
                #json = jwt.decode(str(access_token), '810910', algorithms='HS256')
                user = OTP.objects.filter(phone=str(contact))
                if user.exists():
                    for u in user:
                        u.delete()
                json_response[constants.success] = constants.true
                json_response[constants.msg] = "Successful"
            else:
                json_response[constants.success] = constants.false
                json_response[constants.msg] = "Invalid OTP"
        except Exception as e:
            print e
            json_response[constants.success] = constants.false
            json_response[constants.msg] = "Invalid Mobile Number"
        print 23456
        return JsonResponse(json_response)
    print 23
    return render(request, 'verifyotp.html')