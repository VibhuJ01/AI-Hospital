import datetime as dt
x = dt.datetime.now()

import mysql.connector as ms
mycon = ms.connect(host='localhost', user='root', db='medic', passwd='vibhu')
cur1 = mycon.cursor()

import pyttsx3
speech = pyttsx3.init()
speech.setProperty("rate", 150)


def appointment(doctor,a):

    if(a == 1):
        print(' 1. Cardiologist')    
        print(' 2. Radiologist')    
        print(' 3. OPHTHALMOLOGIST')   
        print(' 4. DENTIST')     
        print(' 5. ENT_SPECIALIST')  
        print(' 6. GYNECOLOGIST')
        print(' 7. ORTHOPEDIC')   
        print(' 8. PEDIATRICIAN')  
        print(' 9. PSYCHIATRIST')   
        print('10. PULMONOLOGIST')  
        print('11. ENDOCRINOLOGIST') 
        print('12. DERMATOLOGIST')  
        print('13. ONCOLOGIST')      
        print('14. NEUROLOGIST')
        print('15. GENERAL PHYSICIAN')
        print('16. Back')
        ch2 = input('Pick your specialist: ')
        print("\n--------------------------------------------\n")


        if(ch2 == '1'):
            doctor = 'cardiologist'

        elif(ch2 == '2'):
            doctor = 'radiologist'

        elif(ch2 == '3'):
            doctor = 'opthalmologist'

        elif(ch2 == '4'):
            doctor = 'dentist'

        elif(ch2 == '5'):
            doctor = 'ent_specialist'

        elif(ch2 == '6'):
            doctor = 'gynecologist'

        elif(ch2 == '7'):
            doctor = 'orthopedic'

        elif(ch2 == '8'):
            doctor = 'pediatrician'

        elif(ch2 == '9'):
            doctor = 'psychiatrist'

        elif(ch2 == '10'):
            doctor = 'pulmonologist'

        elif(ch2 == '11'):
            doctor = 'endocrinologist'

        elif(ch2 == '12'):
            doctor = 'dermatologist'

        elif(ch2 == '13'):
            doctor = 'oncologist'

        elif(ch2 == '14'):
            doctor = 'neurologist'
        

        elif(ch2 == '15'):
            doctor = 'general physician'

        elif(ch2 == '16'):
            return
            
        else:
            print("Wrong Input")
            print("\n--------------------------------------------\n")
            appointment(doctor,1)
            
    sql = 'select * from doctor_names where speciality = %s'
    data = [doctor]
    cur1.execute(sql,data)
    result = cur1.fetchall()

    # Print number of appointments and
    #the current patient number that is going on
    while(True):
        print('Following doctors have specialisation in',doctor)
        print('1. ',result[0][2])
        print('2. ',result[0][3])
        ch = input('Which doctor do you want? ')
        if(ch == '1'):
            special = result[0][2]
            break

        elif(ch == '2'):
            special = result[0][3]
            break

        else:
            print('Wrong Input')
            print("\n--------------------------------------------\n")
            
    print("\n--------------------------------------------\n")
    daily(doctor,special)


def daily(doctor,special):

    while(True):
        f_name = input("Enter patient's First name: ")
        l_name = input("Enter patient's Last name: ")
        print("\n--------------------------------------------\n")
        print("Patient's Full Name: "+f_name+" "+l_name)
        print("\n--------------------------------------------\n")
        ch = input('Is your Name correct?(y/n) ')
        print("\n--------------------------------------------\n")
        if(ch.lower() == 'y'):
            break

    while(True):
        try:
            age = int(input("Enter patient's age: "))
            print("\n--------------------------------------------\n")
            if(age > 130):
                print('Invalid Age')
                print("\n--------------------------------------------\n")
                continue

        except:
            print("\n--------------------------------------------\n")
            print('Wrong Input, Try Again')
            print("\n--------------------------------------------\n")

        else:
            print("Patient's age is: ",age)
            print("\n--------------------------------------------\n")
            ch = input('Is your Age correct?(y/n) ')
            print("\n--------------------------------------------\n")
            if(ch.lower() == 'y'):
                break
            
    date = str(x.day) + '-' + str(x.month) + '-' + str(x.year)
    time = str(x.hour) + ':' + str(x.minute) + ':' + str(x.second)


    while(True):
        try:
            c_code = int(input("Enter your country code +"))
            phone_no = input("Enter your phone_no: ")
            print("\n--------------------------------------------\n")

        except:
            print("\n--------------------------------------------\n")
            print('Wrong Input, Try Again')
            print("\n--------------------------------------------\n")

        else:
            phone_no = '+' + str(c_code) + str(phone_no)
            print("Patient's Phone Number is:",phone_no)
            print("\n--------------------------------------------\n")
            ch = input('Is your Phone Number correct?(y/n) ')
            print("\n--------------------------------------------\n")
            if(ch.lower() == 'y'):
                break
            













            
