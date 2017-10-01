from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
import keysdata
import constants
from Property.models import PropertyTable
from Property.models import PropertyImage
# Create your views here.
@csrf_exempt
def show_property(request):
    if request.method == 'GET':
        json_response = {keysdata.GET_PROPERTY:[]}
        try:
            title = request.GET.get(keysdata.TITLE)
            print title
            try:
                property = PropertyTable.objects.get(title=title)
                print property
                print 12345
                temp_json = {"title": str(property.title), "location": str(property.location),
                            "bhk": int(property.bhk), "description": str(property.description),
                            "price": int(property.price), "contact": str(property.contact),
                            "usage": str(property.usage), "date_added": str(property.date_added),
                             "about": str(property.about_property)}
                property_image = PropertyImage.objects.filter(property = property)
                print "Image"
                print property_image
                temp_json1 = {}
                images=[]
                for img in property_image:
                    temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() +\
                                                     "/" + str(img.image)
                    images.append(temp_json1[keysdata.IMAGE_URL])
                print "Append"
                temp_json[keysdata.IMAGES] = images
            except Exception as e:
                print e
                print "Image could not be found"
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
                return JsonResponse(json_response)
            print 765
            json_response[keysdata.GET_PROPERTY].append(temp_json)
            json_response[constants.SUCCESS] = constants.TRUE
            json_response[constants.MSG] = constants.SUCCESSMSG
        except Exception as e:
            print e
            print "Invalid Title"
            json_response[constants.SUCCESS] = constants.FALSE
            json_response[constants.MSG] = constants.FAILMSG
        print str(json_response)
        return JsonResponse(json_response)
    print 12345678


def view_detail(request):
    return render(request, 'property_detail.html')

