#importing libraries
import time
import random
import tkinter
from tkinter import messagebox
#importing pyfiglet library for fonts
from pyfiglet import Figlet
import mysql.connector
from openpyxl import load_workbook
import pandas as pd

#CSV file for Bus route sheet
DF=pd.read_csv("C:\\Users\\jyoti\\Desktop\\Project\\Bus route sheet.csv",dtype = {'Bus No.': int, 'Driver Name': str, 'Dr. Contact': int,'Conductor Name':str,'Cond. Contact':int,'Route':str})

#MySQL connection
cn=mysql.connector.connect(user="root",password="root",host="localhost",charset="utf8")
con=cn.cursor(buffered=True)
con.execute("use bus;")

'''    FUNCTIONS DEFINITIONS START  '''

#Main menu function
def main():
    while 1:    
        f = Figlet(font='slant')
        print (f.renderText('MENU'))
        f=Figlet(font='digital')
        print (f.renderText('1. Register as Student\n2. Login as a Student\n3. Exit'))
        f=Figlet(font='digital')
        print (f.renderText(""))
        f=Figlet(font='digital')
        print (f.renderText(""))
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register_student()
            continue
        elif choice == "2":
            login_student()
            continue
        elif choice == "3":
            Exit()
            continue
        else:
            print("Invalid choice. Please try again.")


# Function for student login
def login_student():
    """Handles student login"""
    f = Figlet()
    print (f.renderText('Log in'))
    while 1:
        #check if student id is present in database
        stu_ID1 = int(input("\nEnter your Student ID: "))
        query="Select student_id from student where student_id=%s;"
        con.execute(query, (stu_ID1,))
        result = con.fetchone()
        cn.commit()
        if result:
            while 1:
                Password = input("\nEnter Password: ")
                query2="Select student_id, password from student;"
                con.execute(query2)
                cn.commit()
                #check if student is registered or not
                for (student_id,password) in con:
                    if student_id==stu_ID1 and password==None:
                        print("\nNot registered")
                        main()
                    elif stu_ID1 ==student_id and Password==password :
                        login_menu(stu_ID1)
                print("\nInvalid password")
        else:
             print("Invalid student ID")
             continue


#function for register student
def register_student():
    """Registers a new student"""
    f = Figlet()
    print (f.renderText('Register'))
    while 1:
        stu_ID2 = int(input("\nEnter your Student ID: "))
        #check if student id exist in database
        query=("select student_id from student where student_id=%s;")
        con.execute(query, (stu_ID2,))
        result = con.fetchone()
        cn.commit()
        if result:
            #insert password into student table of respective student
            password = input("\nUpdate or Create a Password: ")
            insertrow=("update student set password=%s where student_id=%s;")
            data=(password,stu_ID2)
            con.execute(insertrow,data)
            cn.commit()
            print("Password updated!\n")
            break
        else:
            print("\nStudent not found!\n")
            
    while 1:
        login_menu(stu_ID2)
        
    
#function for exiting program    
def Exit():
    f = Figlet()
    print (f.renderText('Exit'))
    while(1):
        choice=input("\nDo you really want to exit? (Enter Y for Yes and N for No.): ")
        if(choice=="Y" or choice=="y"):
            exit()
        elif(choice=="N" or choice=="n"):
            return
        else:
            print("\nInvalid input\n")
            continue


#function for login menu
def login_menu(stu_ID):
    #menu after logging in
    while(1):
        f=Figlet(font='digital')
        print (f.renderText("\n1. Register for bus facility\n2. Bus Chart\n3. Go to main menu\n4. Exit "))
        inp=int(input("\nEnter choice:"))
        if (inp==1):
            fill_bus_form(stu_ID)
            continue
        elif inp==2:
            bus_chart()
            continue
        elif inp==3:
            main()
        else:
            Exit()
            continue

#function to generate bus card
def bus_card(name,studentid,fathername,course,contact_no,route,bus_no,seat_no):
    root2 = tkinter.Tk()
    lbl=tkinter.Label(root2,text="GRAPHIC ERA HILL UNIVERSITY\n BHIMTAL", font=("Arial", 30))
    lbl.pack(anchor=tkinter.W,padx=50)
    lbl=tkinter.Label(root2,text="BUS CARD", font=("Arial", 30))
    lbl.pack(anchor=tkinter.W,padx=250)
    root2.geometry("800x500")
    root2.configure(bg="#ADD8E6")
    root2.title("BUS CARD")
    name_label = tkinter.Label(root2,text=f"Name : {name}",font=("Arial", 25))
    name_label.pack(anchor=tkinter.W,padx=20)
    studentid_label = tkinter.Label(root2,text=f"Student ID : {studentid}",font=("Arial", 25))
    studentid_label.pack(anchor=tkinter.W,padx=20)
    fname_label = tkinter.Label(root2,text=f"Father's Name : {fathername}",font=("Arial", 25))
    fname_label.pack(anchor=tkinter.W,padx=20)
    course_label = tkinter.Label(root2,text=f"Course : {course}",font=("Arial", 25))
    course_label.pack(anchor=tkinter.W,padx=20)
    contact_label = tkinter.Label(root2,text=f"Contact No. : {contact_no}",font=("Arial", 25))
    contact_label.pack(anchor=tkinter.W,padx=20)
    route_label = tkinter.Label(root2,text=f"Route : {route}",font=("Arial", 25))
    route_label.pack(anchor=tkinter.W,padx=20)
    busno_label = tkinter.Label(root2,text=f"Bus No. : {bus_no}",font=("Arial", 25))
    busno_label.pack(anchor=tkinter.W,padx=20)
    seatno_label = tkinter.Label(root2,text=f"Seat No. : {seat_no}",font=("Arial", 25))
    seatno_label.pack(anchor=tkinter.W,padx=20)
    root2.mainloop()

# Function to fill the bus form (student chooses a bus)
def fill_bus_form(stu_ID):
    #check whether student already registered or not
    query=("select student_id from bus_card_details where student_id=%s;")
    con.execute(query, (stu_ID,))
    result = con.fetchone()
    cn.commit()
    if result:
        print("Already registered for bus facility")
    else:
        root = tkinter.Tk() 
        lbl=tkinter.Label(root,text="Registration Form", font=("Arial", 50))
        lbl.pack(anchor=tkinter.W,padx=50)

        def onclick_submit():
            name = name_textbox.get()
            studentid = studentid_textbox.get()
            fathername= fathername_textbox.get()
            course = course_textbox.get()
            route = route_textbox.get()
            contact_no = contact_textbox.get()
            
            if name and studentid and fathername and course and route and contact_no:
                #assign bus no. based on route
                cnt = 1
                found = False
                for i in DF['Route']:
                    if route == i.strip().lower():
                        messagebox.showinfo("Bus Allocated!", f"Route Found!\nBus No.: {cnt}")
                        found = True
                        break
                    cnt += 1
    
                # If not found, show an error
                if not found:
                    messagebox.showerror("Error", "Route Not Found!")
                else:
                    #assign random seat no.
                    random_number = random.randint(1, 30)
                    query = "SELECT seat_no FROM bus_card_details WHERE bus_no = %s"
                    con.execute(query, (cnt,))
                    occupied_seats = [row[0] for row in con.fetchall()]
                    # Assign a random seat that is not already occupied
                    available_seats = set(range(1, 31)) - set(occupied_seats)
                    if available_seats:
                        random_number = random.choice(list(available_seats))
                        #insert data into database
                        insertrow=("insert into bus_card_details (name,student_id,father_name,course,phone_no,Route,bus_no,seat_no) values(%s,%s,%s,%s,%s,%s,%s,%s);")
                        data=(name,studentid,fathername,course,contact_no,route,cnt,random_number)
                        con.execute(insertrow,data)
                        cn.commit()
                    
                        #display bus card
                        print("\n Generating bus card.........")
                        time.sleep(1)
                        root.destroy()
                        bus_card(name,studentid,fathername,course,contact_no,route,cnt,random_number)
                    else:
                        print("No seats available!")
                    
            else:
                messagebox.showwarning("Warning","Please fill all the fields")

        root.geometry("1000x1000")
        root.configure(bg="#ADD8E6")
        root.title("REGISTRATION FORM")
        
        name_label = tkinter.Label(root,text = "Enter Name ",font=("Arial", 25))
        name_label.pack(anchor=tkinter.W,padx=20)
        name_textbox =tkinter.Entry(root,font=("Arial", 25))
        name_textbox.pack(anchor=tkinter.W,padx= 20)

        studentid_label = tkinter.Label(root,text = "Enter Student Id ",font=("Arial", 25))
        studentid_label.pack(anchor=tkinter.W,padx=20)
        studentid_textbox =tkinter.Entry(root,font=("Arial", 25))
        studentid_textbox.pack(anchor=tkinter.W,padx=20)

        fathername_label = tkinter.Label(root,text = "Enter Father's Name ",font=("Arial", 25))
        fathername_label.pack(anchor=tkinter.W,padx=20)
        fathername_textbox =tkinter.Entry(root,font=("Arial", 25))
        fathername_textbox.pack(anchor=tkinter.W,padx=20)

        course_label = tkinter.Label(root,text = "Enter Course Name ",font=("Arial", 25))
        course_label.pack(anchor=tkinter.W,padx=20)
        course_textbox =tkinter.Entry(root,font=("Arial", 25))
        course_textbox.pack(anchor=tkinter.W,padx=20)

        route_label = tkinter.Label(root,text = "Enter Route ",font=("Arial", 25))
        route_label.pack(anchor=tkinter.W,padx=20)
        route_textbox =tkinter.Entry(root,font=("Arial", 25))
        route_textbox.pack(anchor=tkinter.W,padx=20)

        contact_label = tkinter.Label(root,text = "Enter Contact No. ",font=("Arial", 25))
        contact_label.pack(anchor=tkinter.W,padx=20)
        contact_textbox =tkinter.Entry(root,font=("Arial", 25))
        contact_textbox.pack(anchor=tkinter.W,padx=20)
        
        submit_button= tkinter.Button(root, text='Submit',font=("Arial", 25),command=onclick_submit)
        submit_button.pack(anchor=tkinter.W,padx=20)
        root.mainloop()

#function for bus route chart 
def bus_chart():
    f = Figlet()
    print (f.renderText('Bus Route Chart'))
    from tabulate import tabulate

    # Display DataFrame as a formatted table
    table = tabulate(DF, headers='keys', tablefmt='pipe')
    print(table)

'''    FUNCTIONS DEFINITIONS END  '''

f = Figlet()
print (f.renderText('UNIVERSITY \nBUS PORTAL'))

#calling main function
main()
