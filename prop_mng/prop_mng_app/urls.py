from django.urls import path,include
from .views import index,create_new_property,fetch_property_details,update_property_details,find_cities_by_state,find_similar_properties

urlpatterns = [
    path('',index,name="welcome"),
    path('create_new_property',create_new_property,name="create"),
    path('fetch_property_details',fetch_property_details,name="fetch"),
    path('update_property_details',update_property_details,name="update"),
    path('find_cities_by_state',find_cities_by_state,name="fetch_cities"),
    path('find_similar_properties',find_similar_properties,name="smiliar_cities"),   
]