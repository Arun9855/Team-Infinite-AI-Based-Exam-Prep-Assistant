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
# from rasa_sdk import Action
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet
# import re

# class ActionSolveMath(Action):
#     def name(self):
#         return "action_solve_math"

#     def run(self, dispatcher, tracker, domain):
#         user_message = tracker.latest_message.get("text")

#         # Extract numbers and operators
#         math_expression = re.sub(r'[^0-9+\-*/().]', '', user_message)

#         try:
#             # Evaluate the math expression safely
#             result = eval(math_expression)
#             dispatcher.utter_message(text=f"The answer is: {result}")
#         except:
#             dispatcher.utter_message(text="Sorry, I couldn't understand the math problem.")

#         return []

from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import re

class ActionSolveMath(Action):
    def name(self):
        return "action_solve_math"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get("text")

        # Extract numbers and operators
        math_expression = re.sub(r'[^0-9+\-*/().]', '', user_message)

        try:
            # Evaluate the math expression safely
            result = eval(math_expression)
            dispatcher.utter_message(text=f"The answer is: {result}")
        except:
            dispatcher.utter_message(text="Sorry, I couldn't understand the math problem.")

        return []

