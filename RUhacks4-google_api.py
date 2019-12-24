# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:43:50 2019

@author: risha
"""
import urllib.request
import json
def google_api1(destination,preference_input):
    endpoint='https://maps.googleapis.com/maps/api/directions/json?'
    api_key='AIzaSyCQAs4T3bVLI2RRJQN3bwsj4ZkSiQHMQUs'
    origin='Yonge+and+Finch+Toronto+Ontario'
    #destination=input('Where do you want to go:').replace(" ",'+')

    mode='transit'
    transit_mode='bus'
    transit_routing_preference=['less_walking','fewer_transfers']
    
    #preference_input=input('To select a route that invloves less walking press or say 1, for a route that involves fewer bus transfers, press or say 2: ')
    if (preference_input=='1'):
        navigation_req='origin={}&destination={}&mode={}&transit_mode={}&transit_routing_preference={}&key={}'.format(origin, destination,mode,transit_mode,transit_routing_preference[0],api_key)
    else:
        navigation_req='origin={}&destination={}&mode={}&transit_mode={}&transit_routing_preference={}&key={}'.format(origin, destination,mode,transit_mode,transit_routing_preference[1],api_key)
        
    
    
    google_request=endpoint + navigation_req
    response=urllib.request.urlopen(google_request).read()
    directions=json.loads(response)   
    
    
    routes=directions['routes']
    #print(routes)
  
    if (routes==[]):
        #return False
        routes_available= False
        #print("We couldn't find routes to the destination specified or the destination entered was invalid")
    else:
         #return True
         routes_available= True
         
    return routes_available


def google_api2(destination,preference_input):
    
    
    endpoint='https://maps.googleapis.com/maps/api/directions/json?'
    api_key='AIzaSyCQAs4T3bVLI2RRJQN3bwsj4ZkSiQHMQUs'
    origin='Yonge+and+Finch+Toronto+Ontario'
       
    mode='transit'
    transit_mode='bus'
    transit_routing_preference=['less_walking','fewer_transfers']
    
    
    #preference_input=input('To select a route that invloves less walking press or say 1, for a route that involves fewer bus transfers, press or say 2: ')
    if (preference_input=='1'):
        navigation_req='origin={}&destination={}&mode={}&transit_mode={}&transit_routing_preference={}&key={}'.format(origin, destination,mode,transit_mode,transit_routing_preference[0],api_key)
    else:
        navigation_req='origin={}&destination={}&mode={}&transit_mode={}&transit_routing_preference={}&key={}'.format(origin, destination,mode,transit_mode,transit_routing_preference[1],api_key)
    
    google_request=endpoint + navigation_req    
    response=urllib.request.urlopen(google_request).read()
    directions=json.loads(response)
    
    
    routes=directions['routes']
    route_available= google_api1(destination,preference_input)
    if route_available==True:
         trip_details={}
         possible_routes=routes[0]['legs']
         distance1=possible_routes[0]['steps'][1]['distance']['text'] 
         departure_stop1=possible_routes[0]['steps'][1]['transit_details']['departure_stop']['name']
         departure_time1=possible_routes[0]['steps'][1]['transit_details']['departure_time']['text']
         arrival_stop1=possible_routes[0]['steps'][1]['transit_details']['arrival_stop']['name']
         arrival_time1=possible_routes[0]['steps'][1]['transit_details']['arrival_time']['text']
#        
         trip_details={'Distance':distance1,
                              'Departure_stop':departure_stop1,
                              'Departure_time':departure_time1,
                              'arrival_stop':arrival_stop1,'arrival_time':arrival_time1}
    return trip_details



destination="cn+tower"
preference_input=1
#print(google_api1(destination))
print(google_api2(destination,preference_input))
