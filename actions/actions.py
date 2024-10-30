from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted 

class ActionClearSlots(Action):
    def name(self) -> str:
        return "action_clear_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain) -> list:

        # List of slots to clear
        slots_to_clear = [
            "manufacturer",
            "model",
            "kms_driven",
            "mileage",
            "fuel_type",
            "transmission_type",
            "engine",
            "max_power",
            "seats",
            "year_of_manufacture"
        ]
        
        # Clear the slots by setting them to None
        cleared_slots = [SlotSet(slot, None) for slot in slots_to_clear]

        # Print statement after clearing slots
        dispatcher.utter_message(text="Slots are cleared. Type hi to restart")

        # Return cleared slots
        return cleared_slots

class ActionCustomFallback(Action):
    def name(self) -> str:
        return "action_custom_fallback"

    async def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        # Customize your fallback response here
        dispatcher.utter_message(text="I'm sorry, I didn't quite understand that. Could you rephrase?")

        # You can also revert the user's last input if necessary
        return [UserUtteranceReverted()]

