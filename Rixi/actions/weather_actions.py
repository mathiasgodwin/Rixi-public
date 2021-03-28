from rasa_sdk import Action
from rasa_sdk.events import SlotSet


"""Custom Action to fetch weather data from (api.weatherstack.com)."""
class ActionWeather(Action):
    def name(self):
        return 'action_weather'
    	
    def run(self, dispatcher, tracker, domain):
        import requests
        
        loc = tracker.get_slot('location')
        if loc != None:
            try:
                params = {
                  'access_key': '1b490d719183c8cbeda0577c9b7144e4',
                  'query': loc
                }
                
                api_result = requests.get('http://api.weatherstack.com/current', params, verify=False)
                current = api_result.json()
                
                country       = current['location']['country']
                city          = current['location']['name']
                condition     = current['current']['weather_descriptions']
                temperature_c = current['current']['temperature']
                humidity      = current['current']['humidity']
                wind_mph      = current['current']['wind_speed']
                
                response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
                
                dispatcher.utter_message(response)
            except:
                #country       = "Not available"
                #city          = "Not available"
                #condition     = "Not available"
                #temperature_c = "Not available"
                #humidity      = "Not available"
                #wind_mph      = "Not available"
                responses = [
                """I can't connect to the internet. \n\nCheck your internet connection and try again.""",
                """Can really find me way to the internet...\n\nWill you check your internet connection please!"""
                """You don't seems to have an internet connection.\n\nHow about checking and try again, I'll be waiting!"""
                ]
                dispatcher.utter_message(responses)
        return [SlotSet('location',loc)]

