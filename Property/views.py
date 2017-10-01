from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from django.http.response import JsonResponse
# Create your views here.
from Property.models import PropertyTable
from HomeScreen.models import PropertyType
from Property.models import PropertyImage
# Create your views here.
import constants
import keysdata


@csrf_exempt
def choose_property(request):
    if request.method == 'GET':
        json_response = {keysdata.GET_PROPERTY: []}
        try:
            property_type = request.GET.get(keysdata.PROPERTY_TYPE)
            print property_type
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print str(property_table)
            except Exception as e:
                print e
            try:
                property = PropertyTable.objects.filter(property_type=property_table)
                print 1234567
                print property
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added),
                                 "image" : request.scheme + "://" + request.get_host() +
                                 "/" + str(obj.image)}
                    print 2345678
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        except Exception as e:
            print e
            print "Invalid Property Type"
        print str(json_response)
        return JsonResponse(json_response)
    print 234567

def view_property_view(request):
    return render(request, 'property_view.html')