import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime

#init
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

# Listen
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I am listening")
        audio = robot_ear.listen(mic)

    print("Robot: ...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you == ""

    print("You :"+ you)

    #Understand
    if you == "":
        robot_brain = "I can not hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello Ron"
    elif you == "how are you":
        robot_brain = "I'm fine, thanks Ron so much"
    elif "hi" in you:
        robot_brain = "Hi Ron"
    elif "date" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()    
        robot_brain = now.strftime("%H:%M:%S")
    elif "my parents" in you: 
        robot_brain = "Van Anh and Huong Giang"
    elif "my girlfriend" in you:
        robot_brain = "Tuyet Nhung"
    elif "handsome" in you:
        robot_brain = "you are the best"
    elif "bye" in you:
        robot_brain = "Bye Bye Ron"
        print("Robot :"+ robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break

    print("Robot :"+ robot_brain)
    #speak
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
