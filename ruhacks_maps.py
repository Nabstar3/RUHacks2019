import urllib.request, json
#"""
##
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyCQAs4T3bVLI2RRJQN3bwsj4ZkSiQHMQUs'
##

origin = "Ryerson+University"#input('Where are you?: ').replace(' ','+')
dest = "CN+Tower"#input('Where do you want to go?: ').replace(' ','+')
mode = 'transit'#change later

nav_request = 'origin={}&destination={}&key={}&mode={}'.format(origin,dest,api_key,mode)
request = endpoint + nav_request

response = urllib.request.urlopen(request).read()

directions = json.loads(response)

#result = ''
result = directions['routes'][0]['legs'][0]['steps'][1]['transit_details']['departure_time']['text']

print("result bus will arrive at {}".format(result))
#"""

"""
routes, legs,stepsXignore,transit_details, arrival_time,text
"""

class direction_data:
    def __init__(self):
        self.json_data = {}
        self.origin, self.dest, self.mode = '','',"transit"
        self.endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
        self.api_key = 'AIzaSyCQAs4T3bVLI2RRJQN3bwsj4ZkSiQHMQUs'
        
    def load_origin(self):
        pass
    def load_dest(self):
        pass
    def load_json(self):
        nav_request = 'origin={}&destination={}&key={}&mode={}'.format(self.origin,self.dest,self.api_key,self.mode)
        request = self.endpoint + nav_request
        response = urllib.request.urlopen(request).read()
        self.json_data = json.loads(response)
        
    #check if ^this works

    def get_time(self):
        result = directions['routes'][0]['legs'][0]['steps'][1]['transit_details']['departure_time']['text']
        return result

    def get_possible_routes(self):
        self.origin = "Ryerson+University"#input('Where are you?: ').replace(' ','+')
    def get_specific_route(self):
        self.dest = "CN+Tower"#input('Where do you want to go?: ').replace(' ','+')

"""
#if __name__ == "__main__":
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyCQAs4T3bVLI2RRJQN3bwsj4ZkSiQHMQUs'

dir_data = direction_data()
dir_data.load_origin()
dir_data.load_dest()

dir_data.load_json()
result = dir_data.get_time()

print("result bus will arrive at {}".format(result))
"""
