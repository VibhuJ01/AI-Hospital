import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",db="medic",passwd="vibhu")
cur1 = mycon.cursor()

def keyword_insert():
    
    sql = '''INSERT INTO keywords VALUES(1, 'heart','cardiologist'),
            (2, 'cardiovascular','cardiologist'),(3, 'cardiac','cardiologist'),
            (4, 'heartache', 'cardiologist'),
            (5, 'chest pain','cardiologist'),(6, 'scan', 'radiologist'),
            (7, 'ultrasound', 'radiologist'),(8, 'x-ray', 'radiologist'),
            (9, 'MRI', 'radiologist'),(10, 'eye', 'ophthalmologist'),
            (11, 'vision', 'ophthalmologist'),(12, 'stye', 'ophthalmologist'),
            (13, 'cataract', 'ophthalmologist'),(14, 'blurry', 'ophthalmologist');
            INSERT INTO keywords VALUES(15, 'conjunctivitis', 'ophthalmologist');
            INSERT INTO keywords VALUES(16, 'see', 'ophthalmologist');
            INSERT INTO keywords VALUES(17, 'watch', 'ophthalmologist');
            INSERT INTO keywords VALUES(18, 'tooth', 'dentist');
            INSERT INTO keywords VALUES(19, 'teeth', 'dentist');
            INSERT INTO keywords VALUES(20, 'eat', 'dentist');
            INSERT INTO keywords VALUES(21, 'gums', 'dentist');
            INSERT INTO keywords VALUES(22, 'cavities', 'dentist');
            INSERT INTO keywords VALUES(23, 'taste', 'ent_Specialist');
            INSERT INTO keywords VALUES(24, 'hear', 'ent_Specialist');
            INSERT INTO keywords VALUES(25, 'ear', 'ent_Specialist');
            INSERT INTO keywords VALUES(26, 'smell', 'ent_Specialist');
            INSERT INTO keywords VALUES(27, 'nose', 'ent_Specialist');
            INSERT INTO keywords VALUES(28, 'throat', 'ent_Specialist');
            INSERT INTO keywords VALUES(29, 'swallow', 'ent_Specialist');
            INSERT INTO keywords VALUES(30, 'tonsils', 'ent_Specialist');
            INSERT INTO keywords VALUES(31, 'uterus', 'gynaecologist');
            INSERT INTO keywords VALUES(32, 'periods', 'gynaecologist');
            INSERT INTO keywords VALUES(33, 'baby', 'gynaecologist');
            INSERT INTO keywords VALUES(34, 'pregnant', 'gynaecologist');
            INSERT INTO keywords VALUES(35, 'child', 'gynaecologist');
            INSERT INTO keywords VALUES(36, 'birth', 'gynaecologist');
            INSERT INTO keywords VALUES(37, 'bone', 'orthopedic');
            INSERT INTO keywords VALUES(38, 'fracture', 'orthopedic');
            INSERT INTO keywords VALUES(39, 'joint', 'orthopedic');
            INSERT INTO keywords VALUES(40, 'knee', 'orthopedic');
            INSERT INTO keywords VALUES(41, 'hairline', 'orthopedic');
            INSERT INTO keywords VALUES(42, 'elbow', 'orthopedic');
            INSERT INTO keywords VALUES(43, 'arthritis', 'orthopedic');
            INSERT INTO keywords VALUES(44, 'son', 'pediatrician');
            INSERT INTO keywords VALUES(45, 'daughter', 'pediatrician');
            INSERT INTO keywords VALUES(46, 'child', 'pediatrician');
            INSERT INTO keywords VALUES(47, 'baby', 'pediatrician');
            INSERT INTO keywords VALUES(48, 'mental', 'psychiatrist');
            INSERT INTO keywords VALUES(49, 'sad', 'psychiatrist');
            INSERT INTO keywords VALUES(50, 'depression', 'psychiatrist');
            INSERT INTO keywords VALUES(51, 'pressure', 'psychiatrist');
            INSERT INTO keywords VALUES(52, 'skin', 'dermatologist');
            INSERT INTO keywords VALUES(53, 'rash', 'dermatologist');
            INSERT INTO keywords VALUES(54, 'acne', 'dermatologist');
            INSERT INTO keywords VALUES(55, 'pimples', 'dermatologist');
            INSERT INTO keywords VALUES(56, 'allergy', 'dermatologist');
            INSERT INTO keywords VALUES(57, 'lung', 'pulmonologist');
            INSERT INTO keywords VALUES(58, 'asthama', 'pulmonologist');
            INSERT INTO keywords VALUES(59, 'breathe', 'pulmonologist');
            INSERT INTO keywords VALUES(60, 'bronchitis', 'pulmonologist');
            INSERT INTO keywords VALUES(61, 'typhoid', 'endocrinologist');
            INSERT INTO keywords VALUES(62, 'jaundice', 'endocrinologist');
            INSERT INTO keywords VALUES(63, 'liver', 'endocrinologist');
            INSERT INTO keywords VALUES(64, 'maligant', 'oncologist');
            INSERT INTO keywords VALUES(65, 'benign', 'oncologist');
            INSERT INTO keywords VALUES(66, 'tumor', 'oncologist');
            INSERT INTO keywords VALUES(67, 'cancer', 'oncologist');
            INSERT INTO keywords VALUES(68, 'head', 'neurologist');
            INSERT INTO keywords VALUES(69, 'spine', 'neurologist');
            INSERT INTO keywords VALUES(70, 'headache', 'neurologist');
            INSERT INTO keywords VALUES(71, 'nerve', 'neurologist');
            INSERT INTO keywords VALUES(72, 'vomiting', 'general physician');
            INSERT INTO keywords VALUES(73, 'fever', 'general physician');
            INSERT INTO keywords VALUES(74, 'cold', 'general physician');
            INSERT INTO keywords VALUES(75, 'cough', 'general physician');
            INSERT INTO keywords VALUES(76, 'braces', 'Dentist');'''
            
            
            

    cur1.execute(sql)
    mycon.commit()
    
def doctor_names_insert():

    sql = '''INSERT INTO doctor_names(speciality, doc_1, doc_2) VALUES('cardiologist' , 'Dr. Vivek Jawali', 'Dr. Ramakant Panda');
            INSERT INTO doctor_names(speciality, doc_1, doc_2) VALUES('radiologist' , 'Dr. R Suresh Kumar', 'Dr. Chenna Krishna Reddy');
            INSERT INTO doctor_names(speciality, doc_1, doc_2) VALUES('ophthalmologist' , 'Dr. Sanjay Chaudhary', 'Dr. Atul Kumar');
            INSERT INTO doctor_names(speciality, doc_1, doc_2) VALUES('dentist' , 'Dr. Satyavrat Arya', 'Dr. Arun Setia');
            INSERT INTO doctor_names(speciality, doc_1, doc_2) VALUES('ent_Specialist' , 'Dr. Anil Kumar', 'Dr. Aman Bhatia');
            INSERT INTO doctor_names(speciality, doc_1, doc_2) VALUES('gynaecologist' , 'Dr. Rajiv Khanna', 'Dr. E.V. Raman');
            INSERT INTO doctor_names(speciality, doc_1, doc_2) VALUES('orthopedic' , 'Dr. Anil Arora', 'Dr. Deepak Sharan');
            INSERT INTO doctor_names(speciality, doc_1, doc_2) VALUES('pediatrician' , 'Dr. Vivek Rege', 'Dr. Hitesh Pant');
            INSERT INTO doctor_names(speciality, doc_1, doc_2) VALUES('psychiatrist' , 'Dr. Parmanand Kulhara', 'Dr. Brahm Kapur');
            INSERT INTO doctor_names(speciality, doc_1, doc_2) VALUES('Dermatologist' , 'Dr. Ramji Gupta', 'Dr. Gopi Maddali');
            INSERT INTO doctor_names(speciality, doc_1, doc_2) VALUES('pulmonologist' , 'Dr. Ashok Rajput', 'Dr. Bala Chandran');
            INSERT INTO doctor_names(speciality, doc_1, doc_2) VALUES('endocrinologist' , 'Dr. Sharma Manuj', 'Dr. Shrivastava Abhishek');
            INSERT INTO doctor_names(speciality, doc_1, doc_2) VALUES('oncologist' , 'Dr. Rahul Bhargava', 'Dr. Vinod Raina');
            INSERT INTO doctor_names(speciality, doc_1, doc_2) VALUES('neurologist' , 'Dr. Atma Ram Bansal', 'Dr. Sandeep Vaishya');
            INSERT INTO doctor_names(speciality, doc_1, doc_2) VALUES('general physician' , 'Dr. Ashutosh Shukla', 'Dr. P.k.d. Shah');'''

    cur1.execute(sql)
    mycon.commit()

def daily_insert():
    sql='''insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Vivek Jawali','cardiologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Ramakant Panda','cardiologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. R Suresh Kumar','radiologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Chenna Krishna Reddy','radiologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Sanjay Chaudhary','ophthalmologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Atul Kumar','ophthalmologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Satyavrat Arya','dentist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Arun Setia','dentist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Anil Kumar','ent_specialist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Aman Bhatia','ent_specialist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Rajiv Khanna','gynaecologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. E.V. Raman','gynaecologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Anil Arora','orthopedic',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Deepak Sharan','orthopedic',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Vivek Rege','pediatrician',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Hitesh Pant','pediatrician',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Parmanand Kulhara','psychiatrist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Brahm Kapur','psychiatrist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Ramji Gupta','dermatologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Gopi Maddali','dermatologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Ashok Rajput','pulmonologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Bala Chandran','pulmonologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Sharma Manuj','endocrinologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Shrivastava Abhishek','endocrinologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Rahul Bhargava','oncologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Vinod Raina','oncologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Atma Ram Bansal','neurologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Sandeep Vaishya','neurologist',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. Ashutosh Shukla','general physician',0,0);
            insert into daily(name,speciality,tot_appoint,cur_patient) values('Dr. P.k.d. Shah','general physician',0,0);
            '''
    cur1.execute(sql)
    mycon.commit()
    
daily_insert()    
print('Done')
mycon.close()
