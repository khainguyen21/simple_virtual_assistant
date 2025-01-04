# import text to speech library
import pyttsx3
# import speech recognition library
import speech_recognition

# Robot Mouth
# initialize robot mouth to speak
#robot_mouth = pyttsx3.init()

# say something
#robot_mouth.say("I will speak this text")
#robot_mouth.runAndWait()

# Robot Ear
# initialize robot ear to hear
robot_ear = speech_recognition.Recognizer()

# initialize microphone aka open the microphone
# using with to turn off the microphone after hearing successfully
with speech_recognition.Microphone() as mic:
    print("Robot: I'm Listening")
    # record the sound from the microphone
    audio = robot_ear.listen(mic)

# function recognize_google() built by google to recognize voice and convert to text
you = robot_ear.recognize_google(audio)
print("You: " + you)
