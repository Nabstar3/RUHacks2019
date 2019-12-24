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

####

def get_all_busses():
    pass

def tell_closes_busses():
    pass

def get_certain_bus_time(bus_num,schedule):
    #bus = re.search("([0-9]+)([A-Z]*)",bus_num).group()
    #//bus = bus.matches()
    time = ""
    for key in schedule.keys():
        if bus_num in key:
             time = schedule[key]

    if not time:
        print("sorry that bus does not come to this stop")
        return

    l = get_time(time)
    h=l[0]
    m=l[1]
    
    if not h:
        print("bus is coming in {} minutes".format(m))
    else:
        print("bus is coming in {} hour(s) and {} minute(s)".format(h,m))
        
def get_time(time):
    current = datetime.datetime.now()
    hour_now = current.hour
    minute_now = current.minute

    bus_hour = 0
    if time[-1] == 'p':
        bus_hour = 12+int(time[:-4])

    bus_min = int(time[-3:-1])

    bus_min_t = bus_min + 60*bus_hour
    min_t = minute_now + 60*hour_now

    print(bus_min_t)
    print(min_t)
    minutes = bus_min_t - min_t

    h = 60%minutes
    m = minutes - 60*h

    return [h,m]

    

        
def update_bus_timing():
    pass

get_certain_bus_time("39D")
