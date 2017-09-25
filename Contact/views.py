# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.shortcuts import render
import keysdata
import constants
from Contact.models import ContactForm
# Create your views here.


@csrf_exempt
def contact_form(request):
    if request.method == "POST":
        json_response = {}
        try:
            property_title = request.POST.get(keysdata.TITLE)
            name = request.POST.get(keysdata.NAME)
            phone = request.POST.get(keysdata.CONTACT)
            print property_title
            print name
            print phone
            try:
                contact_obj = ContactForm.objects.get(property_title = property_title, name = name,
                                                      phone = phone)
                print "Data Already Exists"
            except Exception as e:
                print e
                ContactForm.objects.create(property_title=property_title, name=name, phone=phone)
            json_response[constants.SUCCESS] = constants.TRUE
            json_response[constants.MSG] = constants.SUCCESSMSG
        except Exception as e:
            print e
            json_response[constants.SUCCESS] = constants.FALSE
            json_response[constants.MSG] = constants.FAILMSG
        print str(json_response)
        return JsonResponse(json_response)