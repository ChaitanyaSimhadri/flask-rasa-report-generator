from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGenerateReport(Action):
    def name(self) -> str:
        return "action_generate_report"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Placeholder for report generation logic
        dispatcher.utter_message(text="Generating report...")

        # Add report generation logic here

        dispatcher.utter_message(text="Report generated and sent to your email.")

        return []

class ActionEmailReport(Action):
    def name(self) -> str:
        return "action_email_report"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Placeholder for email sending logic
        dispatcher.utter_message(text="Sending report via email...")

        # Add email sending logic here

        dispatcher.utter_message(text="Report sent via email.")

        return []

class ActionQuerySummary(Action):
    def name(self) -> str:
        return "action_query_summary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Placeholder for query summary logic
        dispatcher.utter_message(text="Querying summary...")

        # Add query summary logic here

        dispatcher.utter_message(text="Here is the summary you requested.")

        return []
