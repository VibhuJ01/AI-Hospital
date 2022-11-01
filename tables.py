import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",db="medic",passwd="vibhu")
cur1 = mycon.cursor()

def keyword():

    sql = '''create table keywords (
             S_no int PRIMARY KEY AUTO_INCREMENT,
             keywords varchar(20),
             types_of_doctors varchar(20)
             );'''

    cur1.execute(sql)
    mycon.commit()
    
def keyword_insert():
    
    sql = """INSERT INTO keywords VALUES(1, 'heart','cardiologist');
            INSERT INTO keywords VALUES(2, 'cardiovascular','cardiologist');
            INSERT INTO keywords VALUES(3, 'cardiac','cardiologist');
            INSERT INTO keywords VALUES(4, 'chest pain','cardiologist');
            INSERT INTO keywords VALUES(5, 'scan', 'radiologist');
            INSERT INTO keywords VALUES(6, 'ultrasound', 'radiologist');
            INSERT INTO keywords VALUES(7, 'x-ray', 'radiologist');
            INSERT INTO keywords VALUES(8, 'MRI', 'radiologist');
            INSERT INTO keywords VALUES(9, 'eye', 'ophthalmologist');
            INSERT INTO keywords VALUES(10, 'vision', 'ophthalmologist');
            INSERT INTO keywords VALUES(11, 'stye', 'ophthalmologist');
            INSERT INTO keywords VALUES(12, 'cataract', 'ophthalmologist');
            INSERT INTO keywords VALUES(13, 'blurry', 'ophthalmologist');
            INSERT INTO keywords VALUES(14, 'conjunctivitis', 'ophthalmologist');
            INSERT INTO keywords VALUES(15, 'see', 'ophthalmologist');
            INSERT INTO keywords VALUES(16, 'watch', 'ophthalmologist');
            INSERT INTO keywords VALUES(17, 'tooth', 'dentist');
            INSERT INTO keywords VALUES(18, 'teeth', 'dentist');
            INSERT INTO keywords VALUES(19, 'eat', 'dentist');
            INSERT INTO keywords VALUES(20, 'gums', 'dentist');
            INSERT INTO keywords VALUES(21, 'cavities', 'dentist');
            INSERT INTO keywords VALUES(22, 'taste', 'ent_Specialist');
            INSERT INTO keywords VALUES(23, 'hear', 'ent_Specialist');
            INSERT INTO keywords VALUES(24, 'ear', 'ent_Specialist');
            INSERT INTO keywords VALUES(25, 'smell', 'ent_Specialist');
            INSERT INTO keywords VALUES(26, 'nose', 'ent_Specialist');
            INSERT INTO keywords VALUES(27, 'throat', 'ent_Specialist');
            INSERT INTO keywords VALUES(28, 'swallow', 'ent_Specialist');
            INSERT INTO keywords VALUES(29, 'tonsils', 'ent_Specialist');
            INSERT INTO keywords VALUES(30, 'uterus', 'gynecologist');
            INSERT INTO keywords VALUES(31, 'periods', 'gynecologist');
            INSERT INTO keywords VALUES(32, 'baby', 'gynecologist');
            INSERT INTO keywords VALUES(33, 'child', 'gynecologist');
            INSERT INTO keywords VALUES(34, 'birth', 'gynecologist');
            INSERT INTO keywords VALUES(35, 'bone', 'orthopedic');
            INSERT INTO keywords VALUES(36, 'fracture', 'orthopedic');
            INSERT INTO keywords VALUES(37, 'joint', 'orthopedic');
            INSERT INTO keywords VALUES(38, 'knee', 'orthopedic');
            INSERT INTO keywords VALUES(39, 'elbow', 'orthopedic');
            INSERT INTO keywords VALUES(40, 'arthritis', 'orthopedic');
            INSERT INTO keywords VALUES(41, 'son', 'pediatrician');
            INSERT INTO keywords VALUES(42, 'daughter', 'pediatrician');
            INSERT INTO keywords VALUES(43, 'child', 'pediatrician');
            INSERT INTO keywords VALUES(44, 'baby', 'pediatrician');
            INSERT INTO keywords VALUES(45, 'mental', 'psychiatrist');
            INSERT INTO keywords VALUES(46, 'sad', 'psychiatrist');
            INSERT INTO keywords VALUES(47, 'depression', 'psychiatrist');
            INSERT INTO keywords VALUES(48, 'pressure', 'psychiatrist');
            INSERT INTO keywords VALUES(49, 'skin', 'dermatologist');
            INSERT INTO keywords VALUES(50, 'rash', 'dermatologist');
            INSERT INTO keywords VALUES(51, 'acne', 'dermatologist');
            INSERT INTO keywords VALUES(52, 'pimples', 'dermatologist');
            INSERT INTO keywords VALUES(53, 'allergy', 'dermatologist');
            INSERT INTO keywords VALUES(54, 'lung', 'pulmonologist');
            INSERT INTO keywords VALUES(55, 'asthama', 'pulmonologist');
            INSERT INTO keywords VALUES(56, 'breathe', 'pulmonologist');
            INSERT INTO keywords VALUES(57, 'bronchitis', 'pulmonologist');
            INSERT INTO keywords VALUES(58, 'typhoid', 'endocrinologist');
            INSERT INTO keywords VALUES(59, 'jaundice', 'endocrinologist');
            INSERT INTO keywords VALUES(60, 'liver', 'endocrinologist');
            INSERT INTO keywords VALUES(61, 'maligant', 'oncologist');
            INSERT INTO keywords VALUES(62, 'benign', 'oncologist');
            INSERT INTO keywords VALUES(63, 'tumor', 'oncologist');
            INSERT INTO keywords VALUES(64, 'cancer', 'oncologist');
            INSERT INTO keywords VALUES(65, 'head', 'neurologist');
            INSERT INTO keywords VALUES(66, 'spine', 'neurologist');
            INSERT INTO keywords VALUES(67, 'headache', 'neurologist');
            INSERT INTO keywords VALUES(68, 'nerve', 'neurologist');
            INSERT INTO keywords VALUES(69, 'vomiting', 'general physician');
            INSERT INTO keywords VALUES(70, 'fever', 'general physician');
            INSERT INTO keywords VALUES(71, 'cold', 'general physician');
            INSERT INTO keywords VALUES(72, 'cough', 'general physician');
            INSERT INTO keywords VALUES(73, 'braces', 'Dentist');
            INSERT INTO keywords VALUES(74, 'pregnant', 'gynecologist');
            INSERT INTO keywords VALUES(75, 'hairline', 'orthopedic');
            INSERT INTO keywords VALUES(76, 'heartache', 'cardiologist');"""

    cur1.execute(sql)
    mycon.commit()

keyword_insert()
print('Done')
mycon.close()
