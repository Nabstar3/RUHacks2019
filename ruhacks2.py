import urllib.request, json
import re
import datetime

#"""
##
endpoint = 'https://myttc.ca/finch_station.json'


response = urllib.request.urlopen(endpoint).read()
directions = json.loads(response)

bus_timing = {}
ls = directions['stops'][1]['routes']

for row in ls:
    for col in row["stop_times"]:
        bus_name = col["shape"]
        if bus_name in bus_timing.keys():
            break
        else:
            bus_timing[bus_name] = col["departure_time"]
            print("bus: {} is departing at {}".format(bus_name,bus_timing[bus_name]))
####



def get_all_busses():
    pass

def tell_closes_busses():
    pass

def get_certain_bus_time(bus_num):
    bus = re.search("^d+",bus_num)
    time = ""
    for key in bus_timing.keys():
        if bus in key:
             time = bus_timing[key]

    if not time:
        print("sorry that bus does not come to this stop")
        return

    current = datetime.datetime.now()
    hour_now = current.hour
    minute_now = current.minute

    bus_hour = 0
    if time[-1] == 'p':
        bus_hour = 12+int(time[:-4])

    bus_min = time[-3:-1]

   # hour = 
def update_bus_timing():
    pass
