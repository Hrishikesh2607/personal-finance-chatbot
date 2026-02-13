# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

API_URL = "http://127.0.0.1:5000"

class ActionCheckSpending(Action):
    def name(self):
        return "action_check_spending"

    def run(self, dispatcher, tracker, domain):
     category = tracker.get_slot("category")

     try:
        response = requests.post(
            f"{API_URL}/spending",
            json={"category": category},
            timeout=5
        )

        data = response.json()
        total = data.get("total_spent", 0)

        dispatcher.utter_message(
            text=f"You have spent ₹{total} on {category} this month."
        )

     except Exception as e:
        dispatcher.utter_message(
            text="Sorry, I couldn't fetch your spending right now."
        )
        print("ERROR:", e)

     return []





