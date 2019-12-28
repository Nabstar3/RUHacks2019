import random
import time
import speech_recognition as sr
import urllib.request, json
import re
import datetime
import urllib.request
import json
PROMPT_LIMIT = 3


def speech_from_txt(s):
    # [START tts_quickstart]
    """Synthesizes speech from the input string of text or ssml.
    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """
    from gtts import gTTS
    tts = gTTS(s)
    tts.save("va.mp3")

    try:
        
        from playsound import playsound
        playsound('vca.mp3')

    except:
        pass
    """from pygame import mixer
    #__init__()
    music.load("va.mp3")
    music.play() """  
    

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def prompt_user(recognizer,microphone):
    # set the list of words, maxnumber of guesses, and prompt limit
    #WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon"]
    #NUM_GUESSES = 3
    PROMPT_LIMIT = 3

    

    # get a random word from the list
    #word = random.choice(WORDS)

    # format the instructions string


    #speech_from_txt("Speak when asked to")
    
    # show instructions and wait 3 seconds before starting the game
    for j in range(PROMPT_LIMIT):
        time.sleep(1)
        print('Speak!\n')
        text = recognize_speech_from_mic(recognizer, microphone)
        if not text["success"]:
            print("error with API call")
            break
        if text["transcription"]:
            print("You said: {}.".format(text["transcription"]))
            time.sleep(0.2)

    # if there was an error, stop the game
    if text["error"]:
        print("ERROR: {}".format(text["error"]))
        
        
def google_api1(destination):
    print("CHECKING IF DESTINATION IS VALID")
    time.sleep(5)
    endpoint='https://maps.googleapis.com/maps/api/directions/json?'
    api_key='AIzaSyCQAs4T3bVLI2RRJQN3bwsj4ZkSiQHMQUs'
    origin='Yonge+and+Finch+Toronto+Ontario'
    destination=destination.replace(" ",'+')
    mode='transit'
    transit_mode='bus'
    #transit_routing_preference=['less_walking','fewer_transfers']
    #preference_input=input('To select a route that invloves less walking press or say 1, for a route that involves fewer bus transfers, press or say 2: ')
    #if (preference_input=='1'):
    navigation_req='origin={}&destination={}&mode={}&transit_mode={}&key={}'.format(origin, destination,mode,transit_mode,api_key)
    #else:
        #navigation_req='origin={}&destination={}&mode={}&transit_mode={}&transit_routing_preference={}&key={}'.format(origin, destination,mode,transit_mode,transit_routing_preference[1],api_key)
    google_request=endpoint + navigation_req
    response=urllib.request.urlopen(google_request).read()
    directions=json.loads(response)   
    routes=directions['routes']
    #print(routes)
    if (routes==[]):
        #return False
        routes_available= False
        print("NO AVAILABLE ROUTES FOUND. DESTINATION DOES NOT EXIST")
        time.sleep(2)
        #print("We couldn't find routes to the destination specified or the destination entered was invalid")
    else:
         #return True
        print("DESTINATION FOUND")
        time.sleep(2)
        routes_available= True
    return routes_available

def google_api2(destination,preference_input):
    print("CALCULATING DIRECTIONS TO THE CHOSEN DESTINATION\n")
    time.sleep(5)
    endpoint='https://maps.googleapis.com/maps/api/directions/json?'
    api_key='AIzaSyCQAs4T3bVLI2RRJQN3bwsj4ZkSiQHMQUs'
    origin='Yonge+and+Finch+Toronto+Ontario'
    destination=destination.replace(" ",'+')
    mode='transit'
    transit_mode='bus'
    #transit_routing_preference=['less_walking','fewer_transfers']
    
    #preference_input=input('To select a route that invloves less walking press or say 1, for a route that involves fewer bus transfers, press or say 2: ')
    navigation_req='origin={}&destination={}&mode={}&transit_mode={}&transit_routing_preference={}&key={}'.format(origin, destination,mode,transit_mode,preference_input,api_key)
    
    
    google_request=endpoint + navigation_req    
    response=urllib.request.urlopen(google_request).read()
    directions=json.loads(response)
    
    routes=directions['routes']
    route_available= google_api1(destination)
    if route_available==True:
         trip_details={}
         possible_routes=routes[0]['legs']
         distance1=possible_routes[0]['steps'][1]['distance']['text']
         bus_num=possible_routes[0]['steps'][1]['transit_details']['line']['short_name']
         departure_stop1=possible_routes[0]['steps'][1]['transit_details']['departure_stop']['name']
         departure_time1=possible_routes[0]['steps'][1]['transit_details']['departure_time']['text']
         arrival_stop1=possible_routes[0]['steps'][1]['transit_details']['arrival_stop']['name']
         arrival_time1=possible_routes[0]['steps'][1]['transit_details']['arrival_time']['text']
         trip_details={'bus_num':bus_num,'Distance':distance1,
                              'Departure_stop':departure_stop1,
                              'Departure_time':departure_time1,
                              'arrival_stop':arrival_stop1,'arrival_time':arrival_time1}
    print("ITENERARY AQUIRED")
    time.sleep(3)
    return trip_details

def get_time(raw_time):
    print("CALCULATING REMAINING TIME LEFT TILL BUS ARRIVAL")
    time.sleep(3)
    current = datetime.datetime.now()
    hour_now = current.hour
    minute_now = current.minute

    bus_hour = int(raw_time[:-4])
    if raw_time[-1] == 'p':
        bus_hour += 12 
        

    bus_min = int(raw_time[-3:-1])

    bus_min_t = bus_min + 60*bus_hour
    min_t = minute_now + 60*hour_now

    print("{} {}".format(bus_hour,bus_min))
    print("{} {}".format(hour_now, minute_now))
    

    minutes = bus_min_t - min_t

    h = (60%minutes)
    m = (minutes - 60*h)

    print(h)
    print(m)

    
    m=str(m)
    h=str(h)
    print("TIME CALCULATED")
   
    time.sleep(2)
    return [h,m]

def get_raw_schedule():
    endpoint = 'https://myttc.ca/finch_station.json'
    response = urllib.request.urlopen(endpoint).read()
    raw_schedule = json.loads(response)
    print("GETTING RAW SCHEDULE")
    time.sleep(2)
    return raw_schedule

def create_schedule(raw_schedule):
    bus_timing = {}
    ls = raw_schedule['stops'][1]['routes']
    print("BUILDING SCHEDULE")
    time.sleep(2)
    for row in ls:
        for col in row["stop_times"]:
            bus_name = col["shape"]
            if bus_name in bus_timing.keys():
                continue
            else:
                bus_timing[bus_name] = col["departure_time"]
                #print("bus: {} is departing at {}".format(bus_name,bus_timing[bus_name]))
    print("BUS SCHEDULE GENERATED")
    time.sleep(2)
    return bus_timing

def get_certain_bus_time(bus_num,schedule):
    print("CHECKING TIMING FOR BUS")
    time.sleep(2)
    for key in schedule.keys():
        #print("key {} bus_num {}".format(key,bus_num))
        if bus_num in key:
            print("BUS FOUND")
            time.sleep(2)
            raw_time = schedule[key]
            return raw_time
        print("SEARCHING")
        time.sleep(1)
    print("BUS NOT FOUND")
    time.sleep(3)
    return "DNE"

if __name__ == "__main__":
    EXIT="exit"
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()    
    while(1):
        print("BEGINNING OF THE WHILE LOOP")
        time.sleep(1)
        print("Hello. Say option one to find the next arrival of a bus, option 2 to find transit directions to a place, or exit to start over")
        time.sleep(1)
        for a in range(PROMPT_LIMIT):
            command=prompt_user(recognizer,microphone)
            if command=="option 1":
                #Check for 2 options:Bus exists but is not at the current stop, bus exists and is at the current stop, bus does not exist
                print("Great. Which bus would you like to find?\n")
                for b in range(PROMPT_LIMIT):
                    command=prompt_user(recognizer,microphone)
                    if command==EXIT:
                        print("Exiting")
                        time.sleep(1)
                        break
                    else:
                        bus_num=command
                        print("Great! You're looking for bus"+bus_num)
                        time.sleep(1)
                        print("CHECKING IF BUS EXISTS")
                        time.sleep(1)
                        raw_schedule=get_raw_schedule()
                        schedule=create_schedule(raw_schedule)
                        bus_num = bus_num.upper()
                        bus_time=get_certain_bus_time(bus_num,schedule)
                        if bus_time!="DNE":
                            print("GETTING ETA")
                            time.sleep(3)
                            l = get_time(bus_time)
                            hours=l[0]
                            minutes=l[1]
                            if hours!=0:
                                message=bus_num+" will arrive in "+hours+" hours and "+minutes+" minutes"
                            else:
                                message=bus_num+" will arrive in "+minutes+" minutes"
                            print(message)
                            time.sleep(7)
                            break
                        #check if bus is unreachable from this current stop
                        #elif(bus is unreachable):
                        #find walking directions to the nearest bus stop if walking distance is <20 mins?
                        
                        else:
                            print("I'm sorry, I couldnt find when that bus will arrive. Please state a valid bus number or say exit to start over")
                            time.sleep(1)
            if command=="option 2":
                print("Great. Please state your destination address or say exit to start over")
                for c in range(PROMPT_LIMIT):
                    command=prompt_user(recognizer,microphone)
                    if command!=EXIT:
                        for k in range(PROMPT_LIMIT):
                            print("Did you want to find directions to"+command+"?")
                            command=prompt_user(recognizer,microphone)
                            if ("yes" in command):
                                destination=command
                                destination_exists=google_api1(destination)
                                if destination_exists==True:
                                    #check if destination is reachable
                                    option="fewer_transfers"
                                    itinerary=google_api2(destination,option)
                                    arrival_stop=itinerary["arrival_stop"]
                                    departure_time=itinerary['Departure_time']
                                    arrival_time=itinerary["arrival_time"]
                                    bus_num=itinerary["bus_num"]
                                    print("Take "+bus_num+" to"+arrival_stop+" at "+departure_time+". Your estimated time of arrival is "+arrival_time)
                                    command=EXIT
                                    break
                                else:
                                    print("Sorry, we couldnt find your destination.")
                                    time.sleep(2)
                                    command="no"
                            if ("no" in command):
                                print ("Please restate the destination you wish to travel to")
                                break
                            if("exit" in command):
                                print("Exiting")
                                time.sleep(1)
                                command=EXIT
                                break
                            else:
                                print("Sorry I didn't catch that")
                                continue
                    elif (command==EXIT):
                        print("exiting")
                        time.sleep(2)
                        break
                    else:
                        print("Sorry I didn't catch that, could you repeat your answer?")
                        continue
            if command==EXIT:
                print("Exiting")
                time.sleep(2)
                break
            else:
                print("Sorry thats not a valid option. Please choose again")
                time.sleep(1)
                continue
        
          
