# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import random
import requests
import urllib.parse
from rasa_sdk.forms import FormAction


class ActionBusSearch(Action):

    def name(self) -> Text:
        return "action_bus_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_destination = tracker.get_slot("location")

        if user_destination != None:

            buses_available = random.randint(0, 3)

            if buses_available>0:
                bus_nos = []

                for xr in range(buses_available):
                    bus_nos.append(random.randint(1, 160))
                
                dispatcher.utter_message("Take these buses to get to {}:{}".format(user_destination, bus_nos))
            else:
                dispatcher.utter_message("Sorry no buses available right now for {}".format(user_destination))

            return [(SlotSet("loc_address", user_destination))]
        else:
            dispatcher.utter_message("I'm sorry I am unable to parse this location. Can you rephrase your query?")
            return []


class ActionDefaultFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("I'm sorry I don't understand your query?")
        return []


class ActionGetWeather(Action):

    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        query = tracker.get_slot("location2")

        if query != None:

            response = requests.get("https://www.metaweather.com/api/location/search/?query="+urllib.parse.quote(str(query)))

            if response.status_code == 200:

                weat_data = response.json()

                if weat_data == None or len(weat_data) == 0:
                    dispatcher.utter_message('Invalid Location')
                else:
                    woeid = weat_data[0]['woeid']
                    response2 = requests.get("https://www.metaweather.com/api/location/"+str(woeid))

                    if response2.status_code == 200:
                        wActual = response2.json()

                        if wActual['consolidated_weather']:
                            highest_prob_obj = []
                            highest_prob = 0
                            for consol in wActual['consolidated_weather']:
                                if highest_prob< consol['predictability']:
                                    highest_prob_obj = consol


                            dispatcher.utter_message('Predicted {} with temps of {}'.format(highest_prob_obj['weather_state_name'], highest_prob_obj['the_temp']))
                        else:
                            dispatcher.utter_message("Failed to retrieve weather data")


                    else:
                        dispatcher.utter_message("Failed to retrieve weather data")
            else:
                dispatcher.utter_message("Sorry error occured during fetch weather data")

            return []
        else:
            dispatcher.utter_message("I'm sorry I am unable to parse this location. Can you rephrase your query?")
            return []


class WeatherForm(FormAction):

    def name(self) -> Text:
        return "weather_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["location2"]

    def slot_mappings(self) -> Dict[Text, any]:
        return {"location2": self.from_entity(entity="location2",intent=["ask_weather"])}

    
    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:

        location2 = tracker.get_slot('location2')

        weather_result = "Sunny Weather Today at "+location2

        if location2 != None:
            dispatcher.utter_message(weather_result)

        else:
            dispatcher.utter_message("Invalid Location for weather data")