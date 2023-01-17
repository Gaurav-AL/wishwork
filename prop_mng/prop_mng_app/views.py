from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Property_details ,State_details
from .constants import mapping

import json
# Create your views here.
# welcome endpoint
def index(request):
    return JsonResponse({
        "message":"Welcome to Property Management",
        "End points":"/create_new_property, /fetch_property_details, /update_property_details"
    })
    
#create property endpoints 
@csrf_exempt
def create_new_property(request):
    if(request.method == 'POST'):
        p_name = request.POST['property_name']
        p_address = request.POST['address']
        p_city = request.POST['city']
        p_state = request.POST['state']
        
        # inserting property details
        try:
            details = Property_details(p_name=p_name,p_addr=p_address,p_city=p_city,p_state_name = p_state)
            details.save()
        except Exception as err:
            error = err.args
            return JsonResponse({"Messgae":error})
        
    return JsonResponse({"Property_id":details.p_id,
                         "Property_name":details.p_name,
                         "Property_address":details.p_addr,
                         "Property_state":details.p_state_name,
                         "Property_city":details.p_city
                         })    
    
@csrf_exempt
def fetch_property_details(request):
    if(request.method == 'POST'):
        
        city = request.POST['city_name']
        
        # searching property by city name
        try:
            property_fetched = Property_details.objects.filter(p_city = city).all()
        except Exception as err:
            error = err.args
            return JsonResponse({"Messgae":error})
        
        # Making Property details Json Serializable
        output = {}
        properties_list = list(property_fetched)
        for index,property in enumerate(properties_list):
            output[index+1]= str(property)
               
        return JsonResponse({"Properties":output})
    
    return JsonResponse({"message":"Need city name"})
        


@csrf_exempt
def update_property_details(request):
    if(request.method == 'POST'):
        p_id = request.POST['property_id']
        p_updated_name = request.POST['property name']
        p_updated_city = request.POST['city']
        p_updated_state = request.POST['state']

        # updating property according to property ID
        try:
            update_property = Property_details.objects.get(p_id = p_id)
            update_property.p_name = p_updated_name
            update_property.p_city = p_updated_city
            update_property.p_state_name = p_updated_state
            update_property.save()
            
        except Exception as err:
            error = err.args
            return JsonResponse({"Messgae":error})
        
        return JsonResponse({
            "Updated_Property_name":update_property.p_name,
            "Updated_Property_city":update_property.p_city,
            "Updated_property_state_name":update_property.p_city,
            "Updated_property_address":update_property.p_addr,
            "Property_id":update_property.p_id        
        })
    return JsonResponse({"message":"Need more details, see details about this api"})
        
    
@csrf_exempt
def find_cities_by_state(request):
    if(request.method == 'POST'):
        state = request.POST['state_name']
        state = state.lower()
        return JsonResponse({"Major Cities":mapping[state]})
    return JsonResponse({"message":"Need State Name"})   

@csrf_exempt
def find_similar_properties(request):
    if(request.method == 'POST'):
        property_id = request.POST['property_id']
        
        try:
            record = Property_details.objects.filter(p_id = property_id).first()
            city_name = record.p_city
            needed_details = Property_details.objects.filter(p_city = city_name).all()
        except Exception as err:
            error = err.args
            return JsonResponse({"Messgae":error})
        
        output = {}
        properties_list = list(needed_details)
        for index,property in enumerate(properties_list):
            output[index+1]= str(property)
               
        return JsonResponse({"Properties":output})
            
            
