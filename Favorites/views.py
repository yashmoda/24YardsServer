# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt

from django.http.response import JsonResponse
from django.shortcuts import render
import keysdata
import constants
from Favorites.models import Favorite
from Property.models import PropertyTable
# Create your views here.


@csrf_exempt
def add_favorite(request):
    if(request.method=='POST'):
        json_response = {}
        try:
            property = request.POST.get(keysdata.TITLE)
            phone = request.POST.get(keysdata.CONTACT)
            print property
            print phone
            try:
                Favorite.objects.get(property=property, phone=phone)
                print "Object Already Exists"
            except Exception as e:
                print e
                Favorite.objects.create(property=property, phone=phone)
                print "Object Created"
            json_response[constants.SUCCESS] = constants.TRUE
            json_response[constants.MSG] = constants.SUCCESSMSG
        except Exception as e:
            print e
            json_response[constants.SUCCESS] = constants.FALSE
            json_response[constants.MSG] = constants.FAILMSG
        print str(json_response)
        return JsonResponse(json_response)


def show_favorite(request):
    if request.method=='GET':
        json_response = {keysdata.GET_PROPERTY: []}
        try:
            phone = request.GET.get(keysdata.CONTACT)
            print phone
            try:
                prop = Favorite.objects.filter(phone=phone)
                print prop
                for obj in prop:
                    propobj = PropertyTable.objects.get(title=obj.property)
                    print propobj
                    print propobj.title
                    temp_json = {"title": str(propobj.title), "location": str(propobj.location),
                                 "bhk": int(propobj.bhk), "description": str(propobj.description),
                                 "price": int(propobj.price), "contact": str(propobj.contact),
                                 "usage": str(propobj.usage), "date_added": str(propobj.date_added),
                                 "image": request.scheme + "://" + request.get_host() +
                                          "/" + str(propobj.image)}
                    print temp_json
                    print 2345678
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                    print "Append"
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        except Exception as e:
            print e
            json_response[constants.SUCCESS] = constants.FALSE
            json_response[constants.MSG] = constants.FAILMSG
        print str(json_response)
        return JsonResponse(json_response)
