import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="psbe",database = "prefinal")
mycursor = mydb.cursor()
mycursor.execute('''CREATE TABLE pr(ano varchar(5) PRIMARY KEY NOT NULL, 
stname varchar(25), class varchar(4), percent varchar(10), gender varchar(8), dob 
date, fname varchar(25), mname varchar(25), fno varchar(10), mno varchar(10), 
fmail varchar(25), mmail varchar(25), fjob varchar(20), mjob varchar(20), al1 
VARCHAR(60), al2 VARCHAR(60), al3 VARCHAR(60), al4 VARCHAR(60), sib 
varchar(25), fees varchar(10))''')

mycursor.execute('''CREATE TABLE se(ano varchar(5) PRIMARY KEY NOT NULL, 
stname varchar(25), class varchar(4), percent varchar(10), gender varchar(8), dob 
date, fname varchar(25), mname varchar(25), fno varchar(10), mno varchar(10), 
fmail varchar(25), mmail varchar(25), fjob varchar(20), mjob varchar(20), al1 
VARCHAR(60), al2 VARCHAR(60), al3 VARCHAR(60), al4 VARCHAR(60), sib 
varchar(25), fees varchar(10))''')

mycursor.execute('''CREATE TABLE p_u(ano varchar(5) PRIMARY KEY NOT NULL, 
stname varchar(25), class varchar(4), percent varchar(10), gender varchar(8), dob 
date, fname varchar(25), mname varchar(25), fno varchar(10), mno varchar(10), 
fmail varchar(25), mmail varchar(25), fjob varchar(20), mjob varchar(20), al1 
VARCHAR(60), al2 VARCHAR(60), al3 VARCHAR(60), al4 VARCHAR(60), sib 
varchar(25), fees varchar(10))''')

mycursor.execute("CREATE TABLE FEES (class varchar(4) PRIMARY KEY, fees varchar(10))")
mycursor.execute("insert into FEES(class, fees) values('{}','{}')".format('1','85775'))
mycursor.execute("insert into FEES(class, fees) values('{}','{}')".format('2','85775'))
mycursor.execute("insert into FEES(class, fees) values('{}','{}')".format('3','86355'))
mycursor.execute("insert into FEES(class, fees) values('{}','{}')".format('4','87640'))
mycursor.execute("insert into FEES(class, fees) values('{}','{}')".format('5','89970'))
mycursor.execute("insert into FEES(class, fees) values('{}','{}')".format('6','94180'))
mycursor.execute("insert into FEES(class, fees) values('{}','{}')".format('7','94180'))
mycursor.execute("insert into FEES(class, fees) values('{}','{}')".format('8','96120'))
mycursor.execute("insert into FEES(class, fees) values('{}','{}')".format('9','97970'))
mycursor.execute("insert into FEES(class, fees) values('{}','{}')".format('10','98640'))
mycursor.execute("insert into FEES(class, fees) values('{}','{}')".format('11','185090'))
mycursor.execute("insert into FEES(class, fees) values('{}','{}')".format('12','137200'))
mydb.commit()
