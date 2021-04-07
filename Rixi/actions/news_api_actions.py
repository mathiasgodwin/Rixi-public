from typing import Dict, Text, Any, List, Union, Optional


from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action
from rasa_sdk.forms import FormAction

import requests

apikey = '6eb3969ae4cd40c49621be8721439cb9' # Not for commercial usage pls.
                                            # Go here (https://newsapi.org/register) if you have to.

def newsapi(country):
    """api call for getting top news headline based on country """
    urlnews = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={apikey}'
    response = requests.get(urlnews)
    data = response.json()
    return data

def sourcenews(source):
    """api call for getting hedlines from specific source"""
    urlnews = f'https://newsapi.org/v2/sources?category={source}&apiKey={apikey}'
    response = requests.get(urlnews)
    data = response.json()
    return data

def topicnews(topic):
    """api call for getting news based on specific topic"""
    urlnews = f'https://newsapi.org/v2/everything?q={topic}&sortBy=popularity&apiKey={apikey}'
    response = requests.get(urlnews)
    data = response.json()
    return data




class NewsBBc(Action):
    """example of custom action"""   
    def name(self):
        """name of the custom action"""
        return "action_news_bbc"

    def run(self, dispatcher, tracker, domain):
        """disply news headlines from bbc news"""  
        data = sourcenews("bbc-news")
        leng = len(data)
        for i in range(leng):	
            gt   =   {
                 "attachment": {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                                        {
                                    "title": data['articles'][i]['title'],
                                    "image_url":data['articles'][i]['urlToImage'],
                                    "subtitle": data['articles'][i]['description'],
                                    "buttons": [
                                        {
                                            "type": "web_url",
                                            "url": data['articles'][i]['url'],
                                            "title": "Read More"
                                        },
                                    ]
                                },
                            ]
                        }
                    }
                }
            dispatcher.utter_custom_json(gt)    
        return []  

class NewsABC(Action):
    """example of custom action"""   
    def name(self):
        """name of the custom action"""
        return "action_news_abc"

    def run(self, dispatcher, tracker, domain):
        """display news headlines from abc news"""  
        data = sourcenews("abc-news")
        leng = len(data)
        for i in range(leng):	
            gt  =  {
                    "attachment": {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                                        {
                                    "title": data['articles'][i]['title'],
                                    "image_url":data['articles'][i]['urlToImage'],
                                    "subtitle": data['articles'][i]['description'],
                                    "buttons": [
                                        {
                                            "type": "web_url",
                                            "url": data['articles'][i]['url'],
                                            "title": "Read More"
                                        },
                                    ]
                                },
                            ]
                        }
                    }
                }
                
            dispatcher.utter_custom_json(gt)    
        return []

class NewsCNN(Action):
    """example of custom action"""   
    def name(self):
        """name of the custom action"""
        return "action_news_cnn"

    def run(self, dispatcher, tracker, domain):
        """display news headlines from cnn news"""  
        data = sourcenews("cnn")
        leng = len(data)
        for i in range(leng):	
            gt  =  {
                  "attachment": {
                     "type": "template",
                     "payload": {
                         "template_type": "generic",
                         "elements": [
                                                     {
                                 "title": data['articles'][i]['title'],
                                 "image_url":data['articles'][i]['urlToImage'],
                                 "subtitle": data['articles'][i]['description'],
                                 "buttons": [
                                     {
                                         "type": "web_url",
                                         "url": data['articles'][i]['url'],
                                         "title": "Read More"
                                     },
                                 ]
                             },
                         ]
                     }
                 }
             }
            dispatcher.utter_custom_json(gt)    
        return []  
class newsHeadlineus(Action):
    """example of custom action"""     
    def name(self):
        """name of the custom action"""
        return "action_news_headline_us"

    def run(self, dispatcher, tracker, domain):
        """displaying news headlines of us"""  
        data = newsapi("us")
        leng = len(data)
        for i in range(leng):
            gt  =  {
                  "attachment": {
                      "type": "template",
                      "payload": {
                          "template_type": "generic",
                          "elements": [
                                                      {
                                  "title": data['articles'][i]['title'],
                                  "image_url":data['articles'][i]['urlToImage'],
                                  "subtitle": data['articles'][i]['description'],
                                  "buttons": [
                                      {
                                          "type": "web_url",
                                          "url": data['articles'][i]['url'],
                                          "title": "Read More"
                                      },
                                  ]
                              },
                          ]
                      }
                  }
              }  
            dispatcher.utter_custom_json(gt)
        return []
class NewsheadlineNigeria(Action):
    """example of custom action"""   
    def name(self):
        """name of the custom action"""
        return "action_news_headline_ng"
  
    def run(self, dispatcher, tracker, domain):
        """displaying news headlines of Nigeria"""  
        data = newsapi("ng")
        leng = len(data)
        for i in range(leng):	
            gt  =  {
                   "attachment": {
                       "type": "template",
                       "payload": {
                           "template_type": "generic",
                           "elements": [
                                                       {
                                   "title": data['articles'][i]['title'],
                                   "image_url":data['articles'][i]['urlToImage'],
                                   "subtitle": data['articles'][i]['description'],
                                   "buttons": [
                                       {
                                           "type": "web_url",
                                           "url": data['articles'][i]['url'],
                                           "title": "Read More"
                                       },
                                   ]
                               },
                           ]
                       }
                   }
               } 
            dispatcher.utter_custom_json(gt)
        return []

class NewsHeadlineAustralia(Action):
    """example of custom action"""  
    def name(self):
        """name of the custom action australia"""
        return "action_news_headline_au"

    def run(self,dispatcher,tracker,domain):
        """displaying news headlines of Australia"""  
        data = newsapi("au")
        leng = len(data)
        for i in range(leng):	
            gt  =  {
                    "attachment": {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                                        {
                                    "title": data['articles'][i]['title'],
                                    "image_url":data['articles'][i]['urlToImage'],
                                    "subtitle": data['articles'][i]['description'],
                                    "buttons": [
                                        {
                                            "type": "web_url",
                                            "url": data['articles'][i]['url'],
                                            "title": "Read More"
                                        },
                                    ]
                                },
                            ]
                        }
                    }
                } 
            dispatcher.utter_custom_json(gt)
        return []
class SearchForm(FormAction):
    """Example of a custom form action"""   
    def name(self):
        """Unique identifier of the form"""  
        return "search_form"
  
    def required_slots(self, tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""  
        return ["topic"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
              - an extracted entity
              - intent: value pairs
              - a whole message
              or a list of them, where a first match will be picked"""
        return {
                "topic": [
                    self.from_text(),
                ],
            }
    def submit(
           self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any],
       ) -> List[Dict]:
        """Define what the form has to do after all required slots are filled"""
        dispatcher.utter_message("here is related news") 
        return []

class NewsTopic(Action):
    def name(self):
        """name of the custom action"""
        return "action_news_search"

    def run(self, dispatcher, tracker, domain):
        """displaying news headlines based on specfic topic"""  
        topics = tracker.get_slot("topic")  
        data = topicnews(topics)
        leng = len(data)
        for i in range(leng): 
            gt = {
                  "attachment": {
                      "type": "template",
                      "payload": {
                          "template_type": "generic",
                          "elements": [
                                                      {
                                  "title": data['articles'][i]['title'],
                                  "image_url": data['articles'][i]['urlToImage'],
                                  "subtitle": data['articles'][i]['description'],
                                  "buttons": [
                                      {
                                          "type": "web_url",
                                          "url": data['articles'][i]['url'],
                                          "title": "Read More"
                                      },
                                  ]
                              },
                          ]
                      }
                  }
              }
            dispatcher.utter_custom_json(gt)    
        return []
