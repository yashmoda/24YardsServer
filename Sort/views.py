from django.views.decorators.csrf import csrf_exempt

from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from Property.models import *
from HomeScreen.models import *
import constants, keysdata
# Create your views here.

@csrf_exempt
def sorting(request):
    if request.method == 'POST':
        json_response = {keysdata.GET_PROPERTY: []}
        property_type = request.POST.get(keysdata.PROPERTY_TYPE)
        sort_order = request.POST.get(keysdata.SORT_ORDER)
        print property_type
        print sort_order
        try:
            property_table = PropertyType.objects.get(property_type=property_type)
            print str(property_table)
            if sort_order == '1':
                try:
                    property = PropertyTable.objects.filter(property_type=property_table).\
                        order_by('-price')
                    print "Price high to low"
                    for obj in property:
                        print obj.title
                        temp_json = {"title": str(obj.title), "location": str(obj.location),
                                    "bhk": int(obj.bhk), "description": str(obj.description),
                                    "price": int(obj.price), "contact": str(obj.contact),
                                    "usage": str(obj.usage), "date_added": str(obj.date_added)}
                        images = []
                        temp_json1 = {}
                        property_data = PropertyImage.objects.filter(property=property)
                        print 12345674
                        for img in property_data:
                            temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + \
                                                             request.get_host() + \
                                                             "/images/" + str(img.image)
                            images.append(temp_json1[keysdata.IMAGE_URL])
                        temp_json['images'] = images
                        json_response[keysdata.GET_PROPERTY].append(temp_json)
                    json_response[constants.SUCCESS] = constants.TRUE
                    json_response[constants.MSG] = constants.SUCCESSMSG
                except Exception as e:
                    print e
                    json_response[constants.SUCCESS] = constants.FALSE
                    json_response[constants.MSG] = constants.FAILMSG
            if sort_order == '2':
                try:
                    property = PropertyTable.objects.filter(property_type=property_table).\
                        order_by('price')
                    print "Price low to high"
                    for obj in property:
                        print obj.title
                        temp_json = {"title": str(obj.title), "location": str(obj.location),
                                     "bhk": int(obj.bhk), "description": str(obj.description),
                                     "price": int(obj.price), "contact": str(obj.contact),
                                     "usage": str(obj.usage), "date_added": str(obj.date_added)}
                        images = []
                        temp_json1 = {}
                        property_data = PropertyImage.objects.filter(property=property)
                        print 12345674
                        for img in property_data:
                            temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + \
                                                             request.get_host() + \
                                                             "/images/" + str(img.image)
                            images.append(temp_json1[keysdata.IMAGE_URL])
                        temp_json['images'] = images
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
                                     "usage": str(obj.usage), "date_added": str(obj.date_added)}
                        images = []
                        temp_json1 = {}
                        property_data = PropertyImage.objects.filter(property=property)
                        print 12345674
                        for img in property_data:
                            temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + \
                                                             request.get_host() + \
                                                             "/images/" + str(img.image)
                            images.append(temp_json1[keysdata.IMAGE_URL])
                        temp_json['images'] = images
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
                                     "usage": str(obj.usage), "date_added": str(obj.date_added)}
                        images = []
                        temp_json1 = {}
                        property_data = PropertyImage.objects.filter(property=property)
                        print 12345674
                        for img in property_data:
                            temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + \
                                                             request.get_host() + \
                                                             "/images/" + str(img.image)
                            images.append(temp_json1[keysdata.IMAGE_URL])
                        temp_json['images'] = images
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
        print str(json_response)
        return JsonResponse(json_response)
    print 2345678987654


