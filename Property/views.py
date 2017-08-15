from django.views.decorators.csrf import csrf_exempt

from django.http.response import JsonResponse

from django.shortcuts import render

# Create your views here.
from Property.models import PropertyTable
from HomeScreen.models import PropertyType
from Property.models import PropertyImage
# Create your views here.
import constants
@csrf_exempt
def choose_property(request):
    if request.method == 'POST':
        json_response = {'get_property':[]}
        try:
            property_type = request.POST.get('property_type')
            print property_type
            try:
                property_table = PropertyType.objects.get(property_type=str(property_type))
                print str(property_table)
            except Exception as e:
                print e
            try:
                property = PropertyTable.objects.get(property_type=property_table)
                property_data = PropertyImage.objects.get(property=property)
                for obj in property:
                    print obj.title
                    temp_json = {"title":str(obj.title), "location":str(obj.location),
                                 "bhk":int(obj.bhk), "description":str(obj.description),
                                 "price":int(obj.price), "contact":str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    for img in property_data:
                        temp_json1['image'] = request.scheme + "://" + request.get_host() +\
                                              "/images/" + str(img.image)
                        images.append(temp_json1['image'])
                    print 567876545678
                    temp_json['images'] = images
                    print 2345678
                    json_response['get_property'].append(temp_json)
                json_response[constants.success] = constants.true
                json_response[constants.msg] = constants.successmsg
            except Exception as e:
                print e
                json_response[constants.success] = constants.false
                json_response[constants.msg] = constants.failmsg
        except Exception as e:
            print e
            print "Invalid Property Type"
        print str(json_response)
        return JsonResponse(json_response)
    print 234567