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


    











            
