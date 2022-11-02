import cv2 as cv

import pyttsx3
speech = pyttsx3.init()
speech.setProperty("rate", 150)
        
import mysql.connector as ms
mycon = ms.connect(host='localhost', user='root', db='medic', passwd='vibhu')
cur1 = mycon.cursor()

def reception():
    print('1. Map of the Hospital')
    print('2. How may i help you Today? ')
    print('3. Logout')
    ch = input('What do you want to do? ')
    print("\n--------------------------------------------\n")
    
    if(ch == '1'):
        img = cv.imread('map_hospital.jpg',1)
        cv.imshow('image',img)

    elif(ch == '2'):
        print('How may I help you Today?')
        speech.say("How may i help you today?")
        speech.runAndWait()
        doctor = preprocessing()
        appointment(doctor)
        
    elif(ch == '3'):
        outpass = 'D'
        ch2 = input('Enter Logout Password: ')
        
        if(ch2 == 'D'):
            print("\n--------------------------------------------\n")
            print('Logout Successful')
            print("\n--------------------------------------------\n")
            return

        else:
            print("\n--------------------------------------------\n")
            print('Logout Failed')
            print("\n--------------------------------------------\n")
                    
    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")

    reception()

def preprocessing():
    
    listen = input("I am listening: ")
    print("\n--------------------------------------------\n")
    listen = listen.lower()
    listen = listen.replace(".","")
    listen = listen.replace("?","")
    listen = listen.replace(",","")
    listen = listen.replace("!","")
    l = listen.split()
    i = 0
    while(i<len(l)):
        if(len(l[i])<3):
            l.pop(i)
        else:
            i+=1
            
    sql = 'select * from keywords'
    cur1.execute(sql)
    result = cur1.fetchall()
    
    for i in result:
        for j in l:
            if(i[1] == j):
                doctor = i[2]
                break
        else:
            continue
        break

    else:
        doctor = 'general physician'

    return doctor


def appointment(doctor):

    print('I think you should go to ' + doctor)
    speech.say('I think you should go to ' + doctor)
    speech.runAndWait()
    print("\n--------------------------------------------\n")
    
    print('1. To book appointment for '+ doctor)
    print('2. Show all the available Specialist')
    print('1. CARDIOLOGIST')    
    print('2.  RADIOLOGIST')    
    print('3. OPHTHALMOLOGIST')   
    print('4. DENTIST')     
    print('5. ENT_SPECIALIST')  
    print('6.GYNECOLOGIST')
    print('7. ORTHOPEDIC')   
    print('8. PEDIATRICIAN')  
    print('9. PSYCHIATRIST')   
    print('10. PULMONOLOGIST')  
    print('11. ENDOCRINOLOGIST') 
    print('12. DERMATOLOGIST')  
    print('13. ONCOLOGIST')      
    print('14. NEUROLOGIST')
    print('15. GENERAL PHYSICIAN') 
   
