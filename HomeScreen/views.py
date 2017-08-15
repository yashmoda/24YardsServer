from django.http.response import JsonResponse

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
from HomeScreen.models import PropertyType
import constants
# Create your views here.


def home(request):
    if request.method == 'GET':
        json_response={'data':[]}
        try:
            json_response[constants.success] = constants.true
            json_response[constants.msg] = "Data Found"
            print 12345678
            for obj in PropertyType.objects.all():
                print 876543
                temp_json={}
                temp_json["property_type"] = str(obj.property_type)
                temp_json["message"] = str(obj.message)
                print 98765432
                temp_json["image_url"] = request.scheme + '://' + request.get_host() + \
                                         '/home/' + str(obj.image)
                print temp_json
                print 7654345678765
                json_response["data"].append(temp_json)
                print 1234
        except Exception as e:
            print e
            json_response[constants.success] = constants.false
            json_response[constants.msg] = "Data Not Found"
        print str(json_response)
        #return HttpResponse(str(json_response))
        return JsonResponse(json_response)
    print 12345