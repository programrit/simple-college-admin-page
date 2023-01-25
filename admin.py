import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="ENTER USER",
    password="ENTER PASSWORD",
    database="Admin"
)
mycursor=mydb.cursor()
# mycursor.execute("create database Admin")
# mycursor.execute("create table admin_login(username varchar(30),password varchar(100))")
print("**************ABC college admin page**********************")
def login(): # admin login
    while True:
        username=input("Enter your username: ")
        password=input("Enter your password: ")
        # check the username and password in the db.
        sql2=("select * from admin_login where username=%s and password=%s")
        mycursor.execute(sql2,[(username),(password)])
        result=mycursor.fetchall()
        if result:
            print("\n\tWelcome",username)
            break
        else:
            print("\tIncorrect username and password") 
            continue 
login() 
def student_view(): # view student data 
# mycursor.execute("create table student(student_id int primary key auto_increment,student_name varchar(30),phone_no varchar(10),address varchar(100))")
    mycursor.execute("select * from student")
    result1=mycursor.fetchall()
    for row in result1:
        print(row)  
def student_add(): # add student data 
    sql="insert into student(student_name,phone_no,address)values(%s,%s,%s)"
    while True:
        student_name=input("Enter student_name: ")
        if len(student_name) < 3:
            print("\tYour name is less than 3.")
            print("\tPlease enter your correct name")
            continue
        else:    
            if not student_name.isalpha():
                print("\tNot allowed,number and special charcters")
                print("\tPlease enter your correct name")
                continue
            else:
                break
    while True:
        try:
            phone_no=int(input("Enter your phoneno: "))
        except:
            print("\tplease enter number only!")
            continue
        if len(str(phone_no))==10:
            break
        else:
            print("\tPlease enter correct phoneno")
            continue
    while True:
        address=input("Enter address: ")
        if address==0:
            print("Please enter your correct address")
            continue
        else:  
            val=(student_name,phone_no,address)
            mycursor.execute(sql,val)
            mydb.commit() 
            break
def student_update(): # update student data 
    try:
        sql=("select * from student where student_id=%s")
        student_id=list(input("Enter id: "))
        mycursor.execute(sql,student_id)                   
        myresult=mycursor.fetchall()
        for row in myresult:
            print(row)
            def check():
                print("If you update name enter no1: ")
                print("If you update phone enter no1: ")
                print("If you update address enter no1: ")
                user=input("Enter your choose(enter only 1,2,3): ")
                if user=="1":   
                    sql="update student set student_name=%s where student_name=%s"
                    while True:
                        student_name=input("Enter student_name: ")
                        if len(student_name) < 3:
                            print("\tYour name is less than 3.")
                            print("\tPlease enter your correct name")
                            continue
                        else:    
                            if not student_name.isalpha():
                                print("\tNot allowed,number and special charcters")
                                print("\tPlease enter your correct name")
                                continue
                            else: 
                                val=(student_name,row[1])
                                mycursor.execute(sql,val)
                                mydb.commit()
                                print(mycursor.rowcount,"record affected")
                                break
                elif user=="2":
                    sql="update student set phone_no=%s where phone_no=%s"
                    while True:
                        try:
                            phone_no=int(input("Enter your phoneno: "))
                        except:
                            print("\tplease enter number only!")
                            continue
                        if len(str(phone_no))==10:
                            val=(phone_no,row[2])
                            mycursor.execute(sql,val)
                            mydb.commit()
                            print(mycursor.rowcount,"record affected")
                            break
                        else:
                            print("\tPlease enter correct phoneno")
                            continue 
                elif user=="3":
                    sql="update student set address=%s where address=%s"
                    while True:
                        address=input("Enter address: ")
                        if address==0:
                            print("Please enter your correct address")
                            continue
                        else:  
                            val=(address,row[3])
                            mycursor.execute(sql,val)
                            mydb.commit()
                            print(mycursor.rowcount,"record affected")
                            break
                else:
                    print("Invalid input!")
                    check()
            check()        
    except:
        print("Enter only number")
        student_update()
def student_delete(): # delete student data 
    sql=("select * from student where student_id=%s")
    student_id=list(input("Enter id: "))
    mycursor.execute(sql,student_id)
    myresult=mycursor.fetchall()
    for row in myresult:
        print(row)
        while True:
            user=input("Do you want delete the data(yes/no): ").lower()
            if user=="yes":
                sql1=("delete from student where student_id=%s")
                mycursor.execute(sql1,student_id)
                mydb.commit()
                print(mycursor.rowcount,"record deleted")
                break
            elif user=="no":
                break
            else:
                print("Invalid input")
                continue
def teacher(): # view teacher data 
# mycursor.execute("create table teacher(teacher_id int primary key auto_increment,teacher_name varchar(30),phone_no varchar(10),address varchar(100))")          
    mycursor.execute("select * from teacher")
    result1=mycursor.fetchall()
    for row in result1:
        print(row)
def choose():
    print("1) Student data") 
    print("2) Teacher data") 
    user=input("Enter your choose: ")
    if user=="1":
        print("1) View data")
        print("2) Add data")
        print("3) update data")
        print("4) delete data")
        print("5) exit")
        while True:
            choose1=input("Enter your choose: ")
            if choose1=="1":
                student_view()
                break
            elif choose1 =="2":
                student_add()
                break
            elif choose1=="3":
                student_update()
                break
            elif choose1=="4":
                student_delete()
                break
            elif choose1=="5":
                break
            else:
                print("Invalid input")
                continue
    elif user=="2":
        print("\tOnly you can view the teacher data")
        teacher()
    else:
        print("Invalid input")
        choose() 
choose()  

   





