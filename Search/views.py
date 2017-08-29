from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.http.response import JsonResponse

# Create your views here.
from Property.models import *
from HomeScreen.models import *
import constants, keysdata
# Create your views here.

def view_search(request):
    return render(request, 'view_search.html')
@csrf_exempt
def search(request):
    if request.method == 'POST':
        json_response = {keysdata.GET_PROPERTY: []}
        property_type = request.POST.get(keysdata.PROPERTY_TYPE,'')
        location = request.POST.get(keysdata.LOCATION,'')
        min_price = request.POST.get(keysdata.MIN_PRICE,'')
        max_price = request.POST.get(keysdata.MAX_PRICE,'')
        bhk = list(request.POST.get(keysdata.BHK,''))
        usage = request.POST.get(keysdata.USAGE,'')
        if location == 'undefined':
            location=''
        if property_type == 'undefined':
            property_type=''
        if usage == 'undefined':
            usage=''
        print property_type
        print location
        print min_price
        print max_price
        print bhk
        print usage
        if property_type != '' and location == '' and min_price == '' and max_price == '' and len(bhk)==0 and usage == '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 654567
                property = PropertyTable.objects.filter(property_type=property_table)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type == '' and location != '' and min_price == '' and max_price == '' and len(bhk) == 0 and usage == '':
            try:
                property = PropertyTable.objects.filter(location=location)
                print 5
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type == '' and location == '' and min_price != '' and max_price != ''\
                and len(bhk) == 0 and usage == '':
            try:
                property = PropertyTable.objects.filter(price__lte = int(max_price),
                                                        price__gte = int(min_price))
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + \
                                                         request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type == '' and location == '' and min_price == '' and max_price == '' \
                and bhk != '' and usage == '':
            try:
                property = PropertyTable.objects.filter(bhk__in=bhk)
                print 'dsfsc'
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + \
                                                         request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type == '' and location == '' and min_price != '' and max_price != '' \
                and len(bhk) == 0 and usage != '':
            try:
                property = PropertyTable.objects.filter(usage=usage)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" +\
                                                         request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type != '' and location != '' and min_price == '' and max_price == '' \
                and len(bhk) == 0 and usage == '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 6567
                property = PropertyTable.objects.filter(property_type=property_table,
                                                        location=location)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + \
                                                         request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type != '' and location == '' and min_price!= '' and max_price != '' \
                and len(bhk) == 0 and usage == '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 4567
                property = PropertyTable.objects.filter(price__lte = int(max_price),
                                                        price__gte = int(min_price),
                                                        property_type = property_table)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type != '' and location == '' and min_price == '' and max_price == '' and bhk != '' and usage == '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 3456
                property = PropertyTable.objects.filter(bhk__in = bhk, property_type=property_table)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type != '' and location == '' and min_price == '' and max_price == '' and len(bhk) == 0 and usage != '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 345
                property = PropertyTable.objects.filter(usage = usage, property_type=property_table)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type == '' and location != '' and min_price == '' and max_price == '' and len(bhk) == 0 and usage != '':
            try:
                property = PropertyTable.objects.filter(usage = usage, location=location)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type == '' and location != '' and min_price == '' and max_price == '' and bhk != '' and usage == '':
            try:
                property = PropertyTable.objects.filter(bhk__in=bhk, location=location)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type == '' and location != '' and min_price != '' and max_price != '' and len(bhk) == 0 and usage == '':
            try:
                property = PropertyTable.objects.filter(price__lte = int(max_price), price__gte = int(min_price), location=location)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type == '' and location == '' and min_price != '' and max_price != '' and bhk != '' and usage == '':
            try:
                property = PropertyTable.objects.filter(price__lte = int(max_price), price__gte = int(min_price), bhk__in = bhk)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type == '' and location == '' and min_price != '' and max_price != '' and len(bhk) == 0 and usage != '':
            try:
                property = PropertyTable.objects.filter(usage = usage, price__lte = int(max_price), price__gte = int(min_price))
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type == '' and location == '' and min_price == '' and max_price == '' and bhk != '' and usage != '':
            try:
                property = PropertyTable.objects.filter(usage = usage, bhk__in = bhk)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type != '' and location != '' and min_price != '' and max_price != '' and len(bhk) == 0 and usage == '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 3467
                property = PropertyTable.objects.filter(location=location, property_type=property_table,
                                                        price__lte = int(max_price), price__gte = int(min_price))
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type != '' and location != '' and min_price == '' and max_price == '' and bhk != '' and usage == '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 67
                property = PropertyTable.objects.filter(property_type=property_table, location=location, bhk__in=bhk)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type != '' and location != '' and min_price == '' and max_price == '' and len(bhk) == 0 and usage != '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 456
                property = PropertyTable.objects.filter(usage = usage, location = location, property_type=property_table)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type != '' and location == '' and min_price != '' and \
                        max_price != '' and bhk != '' and usage == '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 3467
                property = PropertyTable.objects.filter(bhk__in = bhk, price__lte=int(max_price),
                                                        price__gte=int(min_price), property_type=property_table)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type != '' and location == '' and min_price != '' and max_price != '' and len(bhk) == 0 and usage != '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 3457
                property = PropertyTable.objects.filter(usage = usage, property_type=property_table,
                                                        price__lte=int(max_price), price__gte=int(min_price))
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type != '' and location == '' and min_price == '' and max_price == '' and bhk != '' and usage != '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 3567
                property = PropertyTable.objects.filter(usage = usage, property_type=property_table, bhk__in=bhk)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type == '' and location != '' and min_price != '' and max_price != '' \
                and bhk != '' and usage == '':
            try:
                property = PropertyTable.objects.filter(location=location, price__lte=int(max_price),
                                                        price__gte=int(min_price), bhk__in=bhk)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type == '' and location != '' and min_price != '' and max_price != '' and len(bhk) == 0 and usage != '':
            try:
                property = PropertyTable.objects.filter(usage = usage, location=location,
                                                        price__lte=int(max_price), price__gte=int(min_price))
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type == '' and location != '' and min_price == '' and max_price == '' and bhk != '' and usage != '':
            try:
                property = PropertyTable.objects.filter(usage = usage, location=location, bhk__in=bhk)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type == '' and location == '' and min_price != '' and max_price != '' and bhk != '' and usage != '':
            try:
                property = PropertyTable.objects.filter(usage = usage, bhk__in=bhk,
                                                        price__lte=int(max_price), price__gte=int(min_price))
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type != '' and location != '' and min_price != '' and max_price != '' and bhk != '' and usage == '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 348
                property = PropertyTable.objects.filter(bhk__in=bhk, property_type=property_table, location=location,
                                                        price__lte=int(max_price), price__gte=int(min_price))
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type != '' and location == '' and min_price != '' and max_price != ''\
                and bhk != '' and usage != '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 3456767
                property = PropertyTable.objects.filter(usage = usage, property_type=property_table, bhk__in=bhk,
                                                        price__lte=int(max_price), price__gte=int(min_price))
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type != '' and location != '' and min_price == '' and max_price == '' \
                and bhk != '' and usage != '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 34567098
                property = PropertyTable.objects.filter(usage = usage, property_type=property_table,
                                                        location=location, bhk__in=bhk)
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type != '' and location != '' and min_price != '' and max_price != '' and len(bhk) == 0 and usage != '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 34567565
                property = PropertyTable.objects.filter(usage = usage, property_type=property_table,
                                                        location=location, price__lte=int(max_price), price__gte=int(min_price))
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type == '' and location != '' and min_price != '' and max_price != '' and bhk != '' and usage != '':
            try:
                property = PropertyTable.objects.filter(usage = usage, property_type=property_table, bhk__in=bhk,
                                                        price__lte=int(max_price), price__gte=int(min_price))
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        if property_type != '' and location != '' and min_price != '' and max_price != '' and bhk != '' and usage != '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 3456723
                property = PropertyTable.objects.filter(usage = usage, property_type=property_table, location=location,
                                                        bhk__in=bhk, price__lte=int(max_price), price__gte=int(min_price))
                print 45
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": int(obj.bhk), "description": str(obj.description),
                                 "price": int(obj.price), "contact": str(obj.contact),
                                 "usage": str(obj.usage), "date_added": str(obj.date_added)}
                    images = []
                    temp_json1 = {}
                    property_data = PropertyImage.objects.filter(property=obj)
                    print 123456
                    for img in property_data:
                        temp_json1[keysdata.IMAGE_URL] = request.scheme + "://" + request.get_host() + \
                                                         "/" + str(img.image)
                        images.append(temp_json1[keysdata.IMAGE_URL])
                    temp_json['images'] = images
                    json_response[keysdata.GET_PROPERTY].append(temp_json)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        print str(json_response)
        return JsonResponse(json_response)
    print 23456