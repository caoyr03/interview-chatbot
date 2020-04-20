## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
  - utter_cheer_up
* affirm
    - interview_form                   <!--Run the sales_form action-->
    - form{"name": "interview_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->
* thank
  - utter_noworries
* goodbye
  - utter_goodbye

## request path
* greet
  - utter_greet
* request_interview
    - interview_form                   <!--Run the sales_form action-->
    - form{"name": "interview_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->
* thank
  - utter_noworries
* goodbye
  - utter_goodbye

## unhappy path
* greet
    - utter_greet
* chitchat
    - utter_cheer_up
    - utter_did_that_help
* affirm
    - interview_form
    - form{"name": "interview_form"}
    - form{"name": null}
* thank
    - utter_noworries


## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
    - interview_form                   <!--Run the sales_form action-->
    - form{"name": "interview_form"}   <!--Activate the form-->
    - form{"name": null}           <!--Deactivate the form-->
* goodbye
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

