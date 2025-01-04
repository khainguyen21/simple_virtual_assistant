# Import text to speech library
import speech_recognition
# Import the speaking library
import pyttsx3

from datetime import date
today = date.today()

d2 = today.strftime("%B %d, %Y")
print(d2)

# # Initialize robot mouth to speak
# robot_mouth = pyttsx3.init()
# # Initialize robot ear to hear
# robot_ear = speech_recognition.Recognizer()
# # Initialize robot brain
# robot_brain = ""
#
# # Listening
# # Use with in order to turn off the microphone after successfully hearing from microphone
# with speech_recognition.Microphone() as mic:
#     print("Robot: I'm listening")
#     # record the message from microphone
#     audio = robot_ear.listen(mic)
#
# print("Robot:m...")
# # Function recognize_google built by google to recognize voice and convert to text
# try:
#     you = robot_ear.recognize_google(audio)
# except:
#     you = ""
#
# print("You: " + you)
#
# # Understanding
# if you == "":
#     robot_brain = "I cannot hear you, please try again!"
# elif you == "hello":
#     robot_brain = "Hello Khai"
#
# print("Robot: " + robot_brain)
#
# # Speaking
#
# # Robot say robot_brain
# robot_mouth.say(robot_brain)
# robot_mouth.runAndWait()