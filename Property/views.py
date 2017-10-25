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


def show_prop(request):
    if request.method == 'GET':
        json_response = {keysdata.GET_PROPERTY: []}
        try:
            property_type = request.GET.get(keysdata.PROPERTY_TYPE,'')
            sort_order = request.GET.get(keysdata.SORT_ORDER,'')
            location = request.GET.get(keysdata.LOCATION,'')
            bhk = list(request.GET.get(keysdata.BHK,''))
            usage = request.GET.get(keysdata.USAGE,'')
            min_price = request.GET.get(keysdata.MIN_PRICE,'')
            max_price = request.GET.get(keysdata.MAX_PRICE,'')
            print property_type
            print sort_order
            print location
            print bhk
            print usage
            print min_price
            print max_price
            #Chosen Property Type1
            if property_type != '' and sort_order == '' and location == '' and len(bhk) == 0 and usage == '' and min_price == '' and max_price == '':
                try:
                    print property_type
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Table"
                except Exception as e:
                    print e
                    print "Invalid Property Type"
                try:
                    property = PropertyTable.objects.filter(property_type=property_table)
                    print property
                    for obj in property:
                        print obj.title
                        temp_json = {"title": str(obj.title), "location": str(obj.location),
                                    "bhk": int(obj.bhk), "description": str(obj.description),
                                    "price": int(obj.price), "contact": str(obj.contact),
                                    "usage": str(obj.usage), "date_added": str(obj.date_added),
                                    "image": request.scheme + "://" + request.get_host() +
                                            "/" + str(obj.image)}
                        print 2345678
                        json_response[keysdata.GET_PROPERTY].append(temp_json)
                    json_response[constants.SUCCESS] = constants.TRUE
                    json_response[constants.MSG] = constants.SUCCESSMSG
                except Exception as e:
                    print e
                    json_response[constants.SUCCESS] = constants.FALSE
                    json_response[constants.MSG] = constants.FAILMSG
                print str(json_response)
                return JsonResponse(json_response)
            #Sorting
            if property_type != '' and sort_order != '' and location == '' and len(bhk) == 0 and usage == '' and min_price == '' and max_price == '':
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
                print str(json_response)
                return JsonResponse(json_response)
            #Searching only for location2
            if property_type == '' and sort_order == '' and location != '' and len(bhk) == 0 and usage == '' and min_price == '' and max_price == '':
                try:
                    property = PropertyTable.objects.filter(location=location)
                    print "Location"
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
            #Searching only for bhk3
            if property_type == '' and sort_order == '' and location == '' and len(bhk) != 0 and usage == '' and min_price == '' and max_price == '':
                try:
                    property = PropertyTable.objects.filter(bhk__in=bhk)
                    print "BHK"
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
            #Search usage4
            if property_type == '' and sort_order == '' and location == '' and len(bhk) == 0 and usage != '' and min_price == '' and max_price == '':
                try:
                    property = PropertyTable.objects.filter(usage=usage)
                    print "Usage"
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
            #Search Budget5
            if property_type == '' and sort_order == '' and location == '' and len(bhk) == 0 and usage == '' and min_price != '' and max_price != '':
                try:
                    property = PropertyTable.objects.filter(price__gte = int(min_price), price__lte = int(max_price))
                    print "Budget"
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
            #Search Property Type and Location6
            if property_type != '' and sort_order == '' and location != '' and len(bhk) == 0 and usage == '' and min_price == '' and max_price == '':
                try:
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Property Type"
                    property = PropertyTable.objects.filter(property_type=property_table,
                                                            location=location)
                    print "Property Type Location"
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
            #Prop Type and BHK7
            if property_type != '' and sort_order == '' and location == '' and len(bhk) != 0 and usage == '' and min_price == '' and max_price == '':
                try:
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Property Type"
                    property = PropertyTable.objects.filter(property_type=property_table,
                                                            bhk__in=bhk)
                    print "Property Type BHK"
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
            #Prop Type and usage8
            if property_type != '' and sort_order == '' and location == '' and len(bhk) == 0 and usage != '' and min_price == '' and max_price == '':
                try:
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Property Type"
                    property = PropertyTable.objects.filter(property_type=property_table,
                                                            usage=usage)
                    print "Property Type usage"
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
            #Prop type budget9
            if property_type != '' and sort_order == '' and location == '' and len(bhk) == 0 and usage == '' and min_price != '' and max_price != '':
                try:
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Property Type"
                    property = PropertyTable.objects.filter(property_type=property_table,
                                                            price__gte=int(min_price), price__lte=int(max_price))
                    print "Property Type budget"
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
            #Location BHK10
            if property_type == '' and sort_order == '' and location != '' and len(bhk) != 0 and usage == '' and min_price == '' and max_price == '':
                try:
                    property = PropertyTable.objects.filter(location=location, bhk__in=bhk)
                    print "Location BHK"
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
            #Location Usage11
            if property_type == '' and sort_order == '' and location != '' and len(bhk) == 0 and usage != '' and min_price == '' and max_price == '':
                try:
                    property = PropertyTable.objects.filter(location=location, usage=usage)
                    print "Location usage"
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
            #Location Budget12
            if property_type == '' and sort_order == '' and location != '' and len(bhk) == 0 and usage == '' and min_price != '' and max_price != '':
                try:
                    property = PropertyTable.objects.filter(location=location, price__gte=int(min_price),
                                                            price__lte=int(max_price))
                    print "Location Budget"
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
            #Bhk usage13
            if property_type == '' and sort_order == '' and location == '' and len(bhk) != 0 and usage != '' and min_price == '' and max_price == '':
                try:
                    property = PropertyTable.objects.filter(bhk__in=bhk, usage=usage)
                    print "BHK Usage"
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
            #BHK budget14
            if property_type == '' and sort_order == '' and location == '' and len(bhk) != 0 and usage == '' and min_price != '' and max_price != '':
                try:
                    property = PropertyTable.objects.filter(bhk__in=bhk, price__gte=int(min_price),
                                                            price__lte=int(max_price))
                    print "BHK Budget"
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
            #Usage budget15
            if property_type == '' and sort_order == '' and location == '' and len(bhk) == 0 and usage != '' and min_price != '' and max_price != '':
                try:
                    property = PropertyTable.objects.filter(usage=usage, price__gte=int(min_price),
                                                            price__lte=int(max_price))
                    print "Usage Budget"
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
            #Prop type location bhk16
            if property_type != '' and sort_order == '' and location != '' and len(bhk) != 0 and usage == '' and min_price == '' and max_price == '':
                try:
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Property Type"
                    property = PropertyTable.objects.filter(property_type=property_table,
                                                            bhk__in=bhk, location=location)
                    print "Property Type BHK location"
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
            #Prop type location usage17
            if property_type != '' and sort_order == '' and location != '' and len(bhk) == 0 and usage != '' and min_price == '' and max_price == '':
                try:
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Property Type"
                    property = PropertyTable.objects.filter(property_type=property_table,
                                                            usage=usage, location=location)
                    print "Property Type usage location"
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
            #Prop type location budget18
            if property_type != '' and sort_order == '' and location != '' and len(bhk) == 0 and usage == '' and min_price != '' and max_price != '':
                try:
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Property Type"
                    property = PropertyTable.objects.filter(property_type=property_table, location=location,
                                                            price__gte=int(min_price), price__lte=int(max_price))
                    print "Property Type budget location"
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
            #Prop type bhk usage19
            if property_type != '' and sort_order == '' and location == '' and len(bhk) != 0 and usage != '' and min_price == '' and max_price == '':
                try:
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Property Type"
                    property = PropertyTable.objects.filter(property_type=property_table,
                                                            usage=usage, bhk__in=bhk)
                    print "Property Type usage bhk"
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
            #Prop type budget
            #Prop type bhk budget20
            if property_type != '' and sort_order == '' and location == '' and len(bhk) != 0 and usage == '' and min_price != '' and max_price != '':
                try:
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Property Type"
                    property = PropertyTable.objects.filter(property_type=property_table, bhk__in=bhk,
                                                            price__gte=int(min_price), price__lte=int(max_price))
                    print "Property Type budget bhk"
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
            #Location bhk usage21
            if property_type == '' and sort_order == '' and location != '' and len(bhk) != 0 and usage != '' and min_price == '' and max_price == '':
                try:
                    property = PropertyTable.objects.filter(bhk__in=bhk, usage=usage, location=location)
                    print "BHK Usage Location"
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
            #Location bhk budget22
            if property_type == '' and sort_order == '' and location != '' and len(bhk) != 0 and usage == '' and min_price != '' and max_price != '':
                try:
                    property = PropertyTable.objects.filter(bhk__in=bhk, price__gte=int(min_price),
                                                            price__lte=int(max_price), location=location)
                    print "BHK Budget location"
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
            #Location usage budget23
            if property_type == '' and sort_order == '' and location != '' and len(bhk) == 0 and usage != '' and min_price != '' and max_price != '':
                try:
                    property = PropertyTable.objects.filter(usage=usage, price__gte=int(min_price),
                                                            price__lte=int(max_price), location=location)
                    print "Usage Budget Location"
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
            #bhk usage budget24
            if property_type == '' and sort_order == '' and location == '' and len(bhk) != 0 and usage != '' and min_price != '' and max_price != '':
                try:
                    property = PropertyTable.objects.filter(bhk__in=bhk, price__gte=int(min_price),
                                                            price__lte=int(max_price), usage=usage)
                    print "BHK Budget usage"
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
            #Prop type location bhk usage25
            if property_type != '' and sort_order == '' and location != '' and len(bhk) != 0 and usage != '' and min_price == '' and max_price == '':
                try:
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Property Type"
                    property = PropertyTable.objects.filter(property_type=property_table, usage=usage,
                                                            bhk__in=bhk, location=location)
                    print "Property Type BHK location usage"
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
            #Prop type location bhk budget26
            if property_type != '' and sort_order == '' and location != '' and len(bhk) != 0 and usage == '' and min_price != '' and max_price != '':
                try:
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Property Type"
                    property = PropertyTable.objects.filter(property_type=property_table, location=location,
                                                            price__gte=int(min_price), price__lte=int(max_price),
                                                            bhk__in=bhk)
                    print "Property Type budget bhk location"
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
            #Prop type location usage budget27
            if property_type != '' and sort_order == '' and location != '' and len(bhk) == 0 and usage != '' and min_price != '' and max_price != '':
                try:
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Property Type"
                    property = PropertyTable.objects.filter(property_type=property_table, location=location,
                                                            price__gte=int(min_price), price__lte=int(max_price),
                                                            usage=usage)
                    print "Property Type budget location usage"
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
            #Property type budget bhk usage28
            if property_type != '' and sort_order == '' and location == '' and len(bhk) != 0 and usage != '' and min_price != '' and max_price != '':
                try:
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Property Type"
                    property = PropertyTable.objects.filter(property_type=property_table, bhk__in=bhk, usage=usage,
                                                            price__gte=int(min_price), price__lte=int(max_price))
                    print "Property Type budget bhk usage"
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
            #Location budget bhk usage29
            if property_type == '' and sort_order == '' and location != '' and len(bhk) != 0 and usage != '' and min_price != '' and max_price != '':
                try:
                    property = PropertyTable.objects.filter(bhk__in=bhk, price__gte=int(min_price),
                                                            price__lte=int(max_price), location=location,
                                                            usage=usage)
                    print "BHK Budget location usage"
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
            #Prop type budget usage30
            if property_type != '' and sort_order == '' and location == '' and len(bhk) == 0 and usage != '' and min_price != '' and max_price != '':
                try:
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Property Type"
                    property = PropertyTable.objects.filter(property_type=property_table, usage=usage,
                                                            price__gte=int(min_price), price__lte=int(max_price))
                    print "Property Type budget usage"
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
            #All31
            if property_type != '' and sort_order == '' and location != '' and len(bhk) != 0 and usage != '' and min_price != '' and max_price != '':
                try:
                    property_table = PropertyType.objects.get(property_type=property_type)
                    print "Property Type"
                    property = PropertyTable.objects.filter(property_type=property_table, location=location,
                                                            price__gte=int(min_price), price__lte=int(max_price),
                                                            bhk__in=bhk, usage=usage)
                    print "Property Type budget bhk location usage"
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
        except Exception as e:
            print e
            print "Invalid Entry"
            json_response[constants.SUCCESS] = constants.FALSE
            json_response[constants.MSG] = constants.FAILMSG
        print str(json_response)
        return JsonResponse(json_response)
    print "Out of If"



@csrf_exempt
def choose_property(request):
    if request.method == 'GET':
        json_response = {keysdata.GET_PROPERTY: [], keysdata.LOCATION:[]}
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
                prop = PropertyTable.objects.values('location').distinct()
                print prop
                for objloc in prop:
                    temp_json1 = str(objloc['location'])
                    print str(objloc['location'])
                    json_response[keysdata.LOCATION].append(temp_json1)
                json_response[constants.SUCCESS] = constants.TRUE
                json_response[constants.MSG] = constants.SUCCESSMSG
            except Exception as e:
                print e
                json_response[constants.SUCCESS] = constants.FALSE
                json_response[constants.MSG] = constants.FAILMSG
        except Exception as e:
            print e
            print "Invalid Property Type"
        print str(json_response[keysdata.LOCATION])
        print str(json_response)
        return JsonResponse(json_response)
    print 234567


def view_property_view(request):
    return render(request, 'property_view.html')