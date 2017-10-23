from django.views.decorators.csrf import csrf_exempt

from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from Property.models import *
from HomeScreen.models import *
import constants, keysdata


@csrf_exempt
def sorting(request):
    if request.method == 'GET':
        print "GET"
        json_response = {keysdata.GET_PROPERTY: [], keysdata.LOCATION:[]}
        property_type = request.GET.get(keysdata.PROPERTY_TYPE)
        sort_order = request.GET.get(keysdata.SORT_ORDER)
        print property_type
        print sort_order
        try:
            property_table = PropertyType.objects.get(property_type=property_type)
            print str(property_table)
            print 4565
            if sort_order == '1':
                try:
                    property = PropertyTable.objects.all().filter(property_type=property_table).order_by('-price')
                    print "Price high to low"
                    for obj in property:
                        print obj.title
                        temp_json = {"title": str(obj.title), "location": str(obj.location),
                                    "bhk": int(obj.bhk), "description": str(obj.description),
                                    "price": int(obj.price), "contact": str(obj.contact),
                                    "usage": str(obj.usage), "date_added": str(obj.date_added),
                                     "image": request.scheme + "://" + request.get_host() +
                                              "/" + str(obj.image)
                                     }
                        json_response[keysdata.GET_PROPERTY].append(temp_json)
                    json_response[constants.SUCCESS] = constants.TRUE
                    json_response[constants.MSG] = constants.SUCCESSMSG
                except Exception as e:
                    print e
                    json_response[constants.SUCCESS] = constants.FALSE
                    json_response[constants.MSG] = constants.FAILMSG
            if sort_order == '2':
                try:
                    print 1234
                    property = PropertyTable.objects.filter(property_type=property_table).order_by('price')
                    print "Price low to high"
                    for obj in property:
                        print obj.title
                        temp_json = {"title": str(obj.title), "location": str(obj.location),
                                     "bhk": int(obj.bhk), "description": str(obj.description),
                                     "price": int(obj.price), "contact": str(obj.contact),
                                     "usage": str(obj.usage), "date_added": str(obj.date_added),
                                     "image": request.scheme + "://" + request.get_host() +
                                              "/" + str(obj.image)
                                     }
                        json_response[keysdata.GET_PROPERTY].append(temp_json)
                    json_response[constants.SUCCESS] = constants.TRUE
                    json_response[constants.MSG] = constants.SUCCESSMSG
                except Exception as e:
                    print e
                    json_response[constants.SUCCESS] = constants.FALSE
                    json_response[constants.MSG] = constants.FAILMSG
            if sort_order == '3':
                try:
                    property = PropertyTable.objects.filter(property_type=property_table).\
                        order_by('-date_added')
                    print "Newest first"
                    for obj in property:
                        print obj.title
                        temp_json = {"title": str(obj.title), "location": str(obj.location),
                                     "bhk": int(obj.bhk), "description": str(obj.description),
                                     "price": int(obj.price), "contact": str(obj.contact),
                                     "usage": str(obj.usage), "date_added": str(obj.date_added),
                                     "image": request.scheme + "://" + request.get_host() +
                                              "/" + str(obj.image)
                                     }
                        json_response[keysdata.GET_PROPERTY].append(temp_json)
                    json_response[constants.SUCCESS] = constants.TRUE
                    json_response[constants.MSG] = constants.SUCCESSMSG

                except Exception as e:
                    print e
                    json_response[constants.SUCCESS] = constants.FALSE
                    json_response[constants.MSG] = constants.FAILMSG
            if sort_order == '4':
                try:
                    property = PropertyTable.objects.filter(property_type=property_table).\
                        order_by('date_added')
                    print "Oldest First"
                    for obj in property:
                        print obj.title
                        temp_json = {"title": str(obj.title), "location": str(obj.location),
                                     "bhk": int(obj.bhk), "description": str(obj.description),
                                     "price": int(obj.price), "contact": str(obj.contact),
                                     "usage": str(obj.usage), "date_added": str(obj.date_added),
                                     "image": request.scheme + "://" + request.get_host() +
                                              "/" + str(obj.image)
                                     }
                        json_response[keysdata.GET_PROPERTY].append(temp_json)
                    json_response[constants.SUCCESS] = constants.TRUE
                    json_response[constants.MSG] = constants.SUCCESSMSG

                except Exception as e:
                    print e
                    json_response[constants.SUCCESS] = constants.FALSE
                    json_response[constants.MSG] = constants.FAILMSG
            print 76578765
        except Exception as e:
            print e
            print "Invalid Property Type"
            json_response[constants.SUCCESS] = constants.FALSE
            json_response[constants.MSG] = constants.INVALID
        prop = PropertyTable.objects.values('location').distinct()
        print prop
        for objloc in prop:
            temp_json1 = str(objloc['location'])
            print str(objloc['location'])
            json_response[keysdata.LOCATION].append(temp_json1)
        print str(json_response)
        return JsonResponse(json_response)
    print 2345678987654


