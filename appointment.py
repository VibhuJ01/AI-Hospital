



def appointment(doctor,a):

    if(a == 1)
        print(' 1. CARDIOLOGIST')    
        print(' 2. RADIOLOGIST')    
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
        ch2 = input('Pick your specialist: ')

        if(ch2 == '1'):
            doctor = 'cardiologist'

        elif(ch2 == '2'):
