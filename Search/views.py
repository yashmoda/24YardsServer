from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from Property.models import *
from HomeScreen.models import *
import constants, keysdata


def view_search(request):
    return render(request, 'search_view.html')


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
        if property_type == '' and location == '' and len(bhk) == 0 and usage == '':
            try:
                property = PropertyTable.objects.filter(price__gte = int(min_price),
                                                        price__lte = int(max_price))
                print 2345
                for obj in property:
                    print obj.title
                    temp_json = {"title": str(obj.title), "location": str(obj.location),
                                 "bhk": str(obj.bhk), "description": str(obj.description),
                                 "price": str(obj.price), "contact": str(obj.contact),
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
        if property_type != '' and location == '' and len(bhk) == 0 and usage == '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 654567
                property = PropertyTable.objects.filter(property_type=property_table,
                                                        price__gte = int(min_price),
                                                        price__lte = int(max_price))
                print 45
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
        if property_type == '' and location != '' and len(bhk) == 0 and usage == '':
            try:
                property = PropertyTable.objects.filter(location=location, price__gte = int(min_price),
                                                        price__lte = int(max_price))
                print 5
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
        if property_type == '' and location == '' and len(bhk) != 0 and usage == '':
            try:
                property = PropertyTable.objects.filter(bhk__in=bhk, price__lte = int(max_price),
                                                        price__gte = int(min_price))
                print 'dsfsc'
                print 45
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
        if property_type == '' and location == '' and len(bhk) == 0 and usage != '':
            try:
                property = PropertyTable.objects.filter(usage=usage, price__lte = int(max_price),
                                                        price__gte = int(min_price))
                print 45
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
        if property_type != '' and location != '' and len(bhk) == 0 and usage == '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 6567
                property = PropertyTable.objects.filter(property_type=property_table,
                                                        location=location, price__gte = int(min_price),
                                                        price__lte = int(max_price))
                print 45
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
        if property_type != '' and location == '' and len(bhk) != 0 and usage == '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 3456
                property = PropertyTable.objects.filter(bhk__in = bhk, property_type=property_table,
                                                        price__lte = int(max_price),
                                                        price__gte = int(min_price))
                print 45
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
        if property_type != '' and location == '' and len(bhk) == 0 and usage != '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 345
                property = PropertyTable.objects.filter(usage = usage, property_type=property_table,
                                                        price__lte = int(max_price),
                                                        price__gte = int(min_price))
                print 45
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
        if property_type == '' and location != '' and len(bhk) == 0 and usage != '':
            try:
                property = PropertyTable.objects.filter(usage = usage, location=location,
                                                        price__lte = int(max_price),
                                                        price__gte = int(min_price))
                print 45
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
        if property_type == '' and location != '' and len(bhk) != 0 and usage == '':
            try:
                property = PropertyTable.objects.filter(bhk__in=bhk, location=location,
                                                        price__lte = int(max_price),
                                                        price__gte = int(min_price))
                print 45
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
        if property_type == '' and location == '' and len(bhk) != 0 and usage != '':
            try:
                property = PropertyTable.objects.filter(usage = usage, bhk__in = bhk,
                                                        price__lte = int(max_price),
                                                        price__gte = int(min_price))
                print 45
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
        if property_type != '' and location != '' and len(bhk) != 0 and usage == '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 67
                property = PropertyTable.objects.filter(property_type=property_table,
                                                        location=location, bhk__in=bhk,
                                                        price__lte = int(max_price),
                                                        price__gte = int(min_price))
                print 45
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
        if property_type != '' and location != '' and len(bhk) == 0 and usage != '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 456
                property = PropertyTable.objects.filter(usage = usage, location = location,
                                                        property_type=property_table,
                                                        price__lte = int(max_price),
                                                        price__gte = int(min_price))
                print 45
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
        if property_type != '' and location == '' and len(bhk) != 0 and usage != '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 3567
                property = PropertyTable.objects.filter(usage = usage, property_type=property_table,
                                                        bhk__in=bhk, price__lte = int(max_price),
                                                        price__gte = int(min_price))
                print 45
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
        if property_type == '' and location != '' and len(bhk) != 0 and usage != '':
            try:
                property = PropertyTable.objects.filter(usage = usage, location=location, bhk__in=bhk,
                                                        price__lte = int(max_price),
                                                        price__gte = int(min_price))
                print 45
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
        if property_type != '' and location != '' and len(bhk) != 0 and usage != '':
            try:
                property_table = PropertyType.objects.get(property_type=property_type)
                print 34567098
                property = PropertyTable.objects.filter(usage = usage, property_type=property_table,
                                                        location=location, bhk__in=bhk,
                                                        price__lte = int(max_price),
                                                        price__gte = int(min_price))
                print 45
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
        print str(json_response)
        return JsonResponse(json_response)
    print 23456