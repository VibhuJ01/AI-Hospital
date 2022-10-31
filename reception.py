import cv2 as cv
import pyttsx3


def reception():
    print('1. Map of the Hospital')
    print('2. How may i help you Today? ')
    ch = input('What do you want to do?')
    print("\n--------------------------------------------\n")
    
    if(ch == '1'):
        img = cv.imread('map_hospital.jpg',1)
        cv.imshow('image',img)

    elif(ch == '2'):  
        speech.say("How may i help you today?")
        speech.runAndWait()
        ch2 = input('How may I help you Today?')

    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")

    reception()
