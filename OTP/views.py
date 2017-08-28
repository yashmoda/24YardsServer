from django.views.decorators.csrf import csrf_exempt
from random import randint

from django.http.response import JsonResponse

from django.shortcuts import render
from OTP.models import OTP
import jwt
from SMS.views import send_sms
import constants
import keysdata
# Create your views here.


@csrf_exempt
def send_otp(request):
    if request.method == 'POST':
        json_response = {}
        temp_json = {}
        try:
            contact = request.POST.get(keysdata.CONTACT)
            print contact
            temp_json['contact'] = str(contact)
            otp = randint(100000, 999999)
            try:
                msg = "Your one time password is " + str(otp)
                send_sms(msg, str(contact))
                print msg
            except Exception as e:
                print e
            try:
                otp_obj = OTP.objects.get(phone=str(contact))
                otp_obj.otp = otp
                otp_obj.save()
            except Exception as e:
                print e
                OTP.objects.create(phone=str(contact), otp=str(otp))
            json_response[constants.SUCCESS] = constants.TRUE
            json_response[constants.MSG] = "OTP SENT"
            print 34
            #json_response[constants.TOKEN] = jwt.encode(temp_json, '24Yards', algorithm='HS256')
            pass
        except Exception as e:
            print e
            json_response[constants.SUCCESS] = constants.FALSE
            json_response[constants.MSG] = "OTP NOT SENT"
        print (str(json_response))
        return JsonResponse(json_response)
    print 123


@csrf_exempt
def view_send_otp(request):
    return render(request, 'sendotp.html')


@csrf_exempt
def verify_otp(request):
    json_response = {constants.SUCCESS: [], constants.MSG: []}
    if request.method == 'POST':
        try:
            contact = request.POST.get(keysdata.CONTACT)
            #token = request.POST.get(keysdata.TOKEN)
            #temp_json = jwt.decode(token, '24Yards', algorithms=['HS256'])
            #contact = temp_json['contact']
            otp = request.POST.get(keysdata.OTP)
            otpobj = OTP.objects.get(phone=str(contact))
            if otpobj.otp == otp:
                access_token = jwt.encode({'mobile': str(contact)}, '810810', algorithm='HS256')
                otpobj.save()
                json_response['access_token'] = str(access_token)
                print('Access Token Created')
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = "Successful"
            else:
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = "Invalid OTP"
        except Exception as e:
            print e
            json_response[constants.SUCCESS] = constants.FALSE
            json_response[constants.MSG] = "Invalid Mobile Number"
        print 23456
        return JsonResponse(json_response)
    print 23