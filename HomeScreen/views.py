from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
# Create your views here.
from django.shortcuts import render
import requests
from HomeScreen.models import PropertyType
from Property.models import PropertyTable
import constants
# Create your views here.
import keysdata

@csrf_exempt
def home(request):
    if request.method == 'GET':
        json_response={keysdata.DATA:[], keysdata.LOCATION:[]}
        try:
            json_response[constants.SUCCESS] = constants.TRUE
            json_response[constants.MSG] = "Data Found"
            print 12345678
            for obj in PropertyType.objects.all():
                print 876543
                temp_json={}
                temp_json[keysdata.PROPERTY_TYPE] = str(obj.property_type)
                #temp_json[keysdata.MESSAGE] = str(obj.message)
                print 98765432
                temp_json[keysdata.IMAGE_URL] = request.scheme + '://' + request.get_host() + \
                                                '/' + str(obj.image)
                print temp_json
                print 7654345678765
                json_response[keysdata.DATA].append(temp_json)
                print 1234
            prop = PropertyTable.objects.values('location').distinct()
            print prop
            for objloc in prop:
                temp_json1 = str(objloc['location'])
                print str(objloc['location'])
                json_response[keysdata.LOCATION].append(temp_json1)
        except Exception as e:
            print e
            json_response[constants.SUCCESS] = constants.FALSE
            json_response[constants.MSG] = "Data Not Found"
        print str(json_response)
        return JsonResponse(json_response)
    print 12345


def view_home(request):
    return render(request, 'home.html')