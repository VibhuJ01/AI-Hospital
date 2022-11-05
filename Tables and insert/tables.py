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
    

def doctor_names():
    sql = '''create table doctor_names (
             S_no int PRIMARY KEY AUTO_INCREMENT,
             speciality varchar(20),
             doc_1 varchar(50),
             doc_2 varchar(50)
            );'''
    
    cur1.execute(sql)
    mycon.commit()


print('Done')
mycon.close()
