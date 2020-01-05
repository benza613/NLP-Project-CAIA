## search local transport
* greet
  - utter_greet
* search_bus{"veh_bus": "bus", "location": "Roosevelt"}
  - action_bus_search
* goodbye
  - utter_goodbye

## search local transport 2
* greet
  - utter_greet
* search_bus{"veh_bus":"bus"}
  - utter_ask_location
* info_IL{"location":"Roosevelt"}
  - action_bus_search
* goodbye
  - utter_did_that_help

## search local transport 3 
* search_bus{"location": "Roosevelt"}
  - action_bus_search
* goodbye
  - utter_happy
  - utter_goodbye

## query transport is valid 
* query_valid_transport
  - utter_assure_valid_transport

## weather 1
* greet 
  - utter_greet
* ask_weather{"location2":"San Francisco"}
  - action_get_weather
* goodbye
  - utter_did_that_help
* affirm 
  - utter_happy

## weather 2
* ask_weather{"location2":"San Francisco"}
  - action_get_weather
* goodbye
  - utter_did_that_help
* deny 
  - utter_sad

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
