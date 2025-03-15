# Import text to speech library
import speech_recognition
# Import the speaking library
import pyttsx3
# datetime already in python, so doesn't need to pip install <name of library>
# Import today's date
from datetime import date
# Import time right now
from datetime import datetime
import wikipedia
import re

# Initialize robot mouth to speak
robot_mouth = pyttsx3.init()
# Initialize robot ear to hear
robot_ear = speech_recognition.Recognizer()
# Initialize robot brain
robot_brain = ""

# Greeting
robot_mouth.say("Hi Sir, how can I assist you today? ")
print("Hi Sir, how can I assist you today? ")
robot_mouth.runAndWait()

## Run the program forever
while True:
    # Listening
    # Use with in order to turn off the microphone after successfully hearing from microphone
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        # record the message from microphone
        audio = robot_ear.listen(mic)

    print("Robot: ...")

    # Function recognize_google built by google to recognize voice line and convert to text
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)

    # Understanding
    if you == "":
        robot_brain = "Sir, I cannot hear you, please try again!"
    elif "how are" in you:
        robot_brain = "I am very good sir!"
    elif "hello" in you:
        robot_brain = "Hello Sir"
    elif "today" in you:
        today = date.today().strftime("%B %d, %Y")
        robot_brain = "It is " + today + " Sir"
    elif "time" in you:
        # Get the current date and time
        now = datetime.now()
        # Extract time from datetime object
        current_time = now.time().strftime("%H:%M:%S")
        # Format time as string
        robot_brain = "It is " + current_time + " right now Sir"
    elif "wikipedia" in you or "search" in you:
        temp = re.sub("wikipedia", "", you, flags= re.IGNORECASE)
        query = re.sub("search", "", you, flags = re.IGNORECASE)

        try :
            robot_brain = wikipedia.summary(query, sentences = 2)
        except:
            robot_brain = "Please be more specific"


    elif "bye" in you:
        robot_brain = "Bye Khai"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        print("Robot: Bye Khai!")
        break
    print("Robot: " + robot_brain)

    # Speaking
    # Robot say robot_brain
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()