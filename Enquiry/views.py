# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt

from django.http.response import JsonResponse
from django.shortcuts import render
import constants
from Enquiry.models import EnquiryForm
import keysdata
# Create your views here.4

@csrf_exempt
def enquiry(request):
    if request.method == "POST":
        json_response={}
        try:
            name = request.POST.get(keysdata.NAME)
            contact = request.POST.get(keysdata.CONTACT)
            print name
            print contact
            try:
                enquiry_obj = EnquiryForm.objects.get(name = str(name))
                print "Data Already Exists"
            except Exception as e:
                print e
                EnquiryForm.objects.create(name = str(name), phone = str(contact))
            json_response[constants.SUCCESS] = constants.TRUE
            json_response[constants.MSG] = constants.SUCCESSMSG
        except Exception as e:
            print e
            json_response[constants.SUCCESS] = constants.FALSE
            json_response[constants.MSG] = constants.FAILMSG
        print str(json_response)
        return JsonResponse(json_response)
    print "qwertyuiop"