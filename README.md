# interview-chatbot
A Chatbot-based Interactive Interview Preparation System

## Getting Started
These instructions will get you a copy of this project up and running.

### Introduction
This is a individual project to a Master thesis paper as graduation from 2020 UNC Information Science program. The idea behind this app is to deploy an AI chatbot framework to a web application to help users practice on random interview quesitons as they requested. I used Python's flask web framework to build the website, deployed RASA chatbot technology into a toggle window, included Machine Learning similarity models to calculate the score from user's input.

### Workflow
Interview questions are collected selectively. There are four interview_topics: Machine Learning, Statistics, SQL and Programming. Each of them have their own sections for users to choose. They will get a random question after they input both the topic and section to the bot. The answer they provide will then be compared with the correct answer to the question from the database. A final similarity score will show up and tell user to improve their answers. 

### Technologies
* HTML5
* CSS3
* JavaScript
* Flask - A python's micro webframework.
* Python 2.7
* Bootstrap 3
* jQuery

### Installation

- You can clone the repository 
https://github.com/caoyr03/interview-chatbot.git
Or you can download the zip file and simply extract it to a folder.

* You need to install all the packages from the `requirements.txt` file and make sure the version of the Python is 2.7.

```
pip install -r requirements.txt
```

* After installation, try to run the application in the local browse by following command.

```
python app.py
```

* Open two terminal windows, set up these two local server separately. This will get your rasa server running.

```
rasa run actions
```

```
rasa run --enable-api
```

### Deployment
* You can deploy this project on your local server.





