import pandas as pd
from rasa_sdk.forms import FormAction
from typing import Dict, Text, Any, List, Union
from random import randint

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher


class InterviewForm(FormAction):
    """Collects interview information and adds it to the spreadsheet"""
    def __init__(self):
        self.index = []
        self.sheet = []

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "interview_form"
    
    @staticmethod
    def required_slots(tracker):
        return ["interview_topic","section","answer"]
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "interview_topic": self.from_entity(entity="interview_topic", intent="inform"),
            "section": 
                self.from_text(intent = "select"),
            "answer":
                self.from_text()
            
        }
        
    def validate_interview_topic(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        tracker.slots["interview_topic"] = value
        return {'interview_topic':value}
    
    def validate_section(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        interview = tracker.get_slot("interview_topic")
        sheet = pd.read_csv('question.csv')
        question = sheet['question'].loc[(sheet['interview_topic']==interview) & (sheet['section']==value)]
        dispatcher.utter_message("Thanks for preparing your interview with us. Get ready for you first practice")
        n = randint(min(question.index),max(question.index))
        self.index = n
        dispatcher.utter_message(question[n])
        return {'section':value}
    
    def validate_answer(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        tracker.slots["answer"] = value
        return {'answer':value}
    

    def jaccard_similarity(self,list1, list2):
        s1 = set(list1)
        s2 = set(list2)
        return len(s1.intersection(s2)) / len(s2)
    
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        sheet = pd.read_csv('/Users/caoyuru/Desktop/MasterPaper/chatbot/question.csv')
        answer = str(tracker.get_slot("answer"))
        question = str(sheet['answer'][self.index])
        self.jaccard_similarity(answer,question)
        score = self.jaccard_similarity(answer,question)
        dispatcher.utter_message("Your score is " + str(int(score*100)))       
        dispatcher.utter_message("The correct answer is\n" + sheet['answer'][self.index])
        return []
    






