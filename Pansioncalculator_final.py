from tkinter import *
import mysql.connector
from mysql.connector import Error
# Try block for connection...........................................................
try:
    #   connect to mySQL..............................................................
    flag = 0
    con = mysql.connector.connect(host='localhost', user='root', password='Jay@6350')
    cur = con.cursor(buffered=True)
    cur.execute("SHOW DATABASES")
    for x in cur.fetchall():
        for y in x:
            if y == 'pension_database':
                con = mysql.connector.connect(host='localhost', user='root', password='Jay@6350',database='pension_database')
                cur = con.cursor(buffered=True)
                flag = 1
                break
    if flag != 1:
        cur.execute("CREATE DATABASE pension_database")
        con = mysql.connector.connect(host='localhost', user='root', password='Jay@6350', database='pension_database')
        cur = con.cursor(buffered=True)
        cur.execute("CREATE TABLE pension_record(id INT PRIMARY KEY, name CHAR(50), Basic_pansion FLOAT, Commutation_amount FLOAT)")

    # creating main window...........................................................
    window = Tk()
    window.title("PENSION AND COMMUTATION CALCULATOR")
    #Variable define...............................................................
    e_val1 = StringVar()
    e_val2 = StringVar()
    e_val3 = StringVar()
    e_val4 = StringVar()
    e_val5 = StringVar()
    e_val6 = StringVar()
    e_val7 = StringVar()
    e_val8 = StringVar()
    e_val9 = StringVar()
    e_valname = StringVar()
    e_valid = StringVar()
    el1 = StringVar()
    el2 = StringVar()
    el3 = StringVar()
    el4 = StringVar()
    el5 = StringVar()
    t1 = Label(window, textvariable=el1)
    t2 = Label(window, textvariable=el2)
    t3 = Label(window, textvariable=el3)
    t4 = Label(window, textvariable=el4)
    t5 = Label(window, textvariable=el5)
    intro = Label(window, text="-----------------WELCOME TO PENSION AND COMMUTATION CALCULATOR-----------------------",
                  bg="black", fg='white')
    result = Label(window, text='----------------------CALCULATED PENSION AND COMMUTATION IS-------------------------',
                   bg="black", fg='white')



    #Function for show data(Function)...............................................
    def onClickShowAllF2():
        showAll = Tk(className="Records")
        showAll.configure(bg='black')
        showAll.geometry('600x800')

        p1 = Label(showAll, text='ID', font='time 16 bold', fg='white', bg='black')
        p1.grid(row=1, column=0, padx=10, pady=10)
        p2 = Label(showAll, text='Name', font='time 16 bold', fg='white', bg='black')
        p2.grid(row=1, column=1, padx=10, pady=10)
        p3 = Label(showAll, text='Basic Pansion', font='time 16 bold', fg='white', bg='black')
        p3.grid(row=1, column=2, padx=10, pady=10)
        p4 = Label(showAll, text='Commutation Amount', font='time 16 bold', fg='white', bg='black')
        p4.grid(row=1, column=3, padx=10, pady=10)
        # Selecting query form database
        query = 'SELECT * FROM pension_record'
        cur.execute(query)

        result = cur.fetchall()
        num = 2
        for x in result:  # print all the records................................
            ID = Label(showAll, text=x[0], font="time 12 bold", fg="orange", bg='black')
            ID.grid(row=num, column=0, pady=10, padx=10)

            Name = Label(showAll, text=x[1], font="time 12 bold", fg="orange", bg='black')
            Name.grid(row=num, column=1, padx=10, pady=10)

            Basic_pansion = Label(showAll, text=x[2], font="time 12 bold", fg="orange", bg='black')
            Basic_pansion.grid(row=num, column=2, padx=10, pady=10)

            Commutation_amount = Label(showAll, text=x[3], font="time 12 bold", fg="orange", bg='black')
            Commutation_amount.grid(row=num, column=3, padx=10, pady=10)

            num += 1


    # Logic and calculation for calculator start(function)................................................
    def logic():
        BasicPay = int(e1.get())
        BasicPay1 = 0
        SpecialPay = int(e2.get())
        SpecialPay1 = 0
        StagnationPay1 = 0
        StagnationPay = int(e3.get())
        QualificationPay1 = 0
        QualificationPay = int(e4.get())
        FixedPersonalPay1 = 0
        FixedPersonalPay = int(e5.get())
        OtherPay1 = 0
        OtherPay = int(e6.get())
        YearsOfService1 = 0
        YearsOfService = int(e7.get())
        AgeAtNextbirthday1 = 0
        AgeAtNextbirthday = int(e8.get())
        CommutationPercent1 = 0
        CommutationPercent = int(e9.get())
        CommutationFactor = 0
        # Checking format (Valid or Invalid Input)..................................................
        Id1 = 0
        Name1 = 0
        cond = True
        Id = int(e10.get())
        Name = e11.get()
        if (Id > 0):
            Id1 = Id
        Name1 = Name
        if (BasicPay > 0):
            BasicPay1 = BasicPay
        else:
            BasicPay1 = 0

        if (SpecialPay > 0):
            SpecialPay1 = SpecialPay
        else:
            SpecialPay1 = 0

        if (StagnationPay > 0):
            StagnationPay1 = StagnationPay
        else:
            StagnationPay1 = 0

        if (QualificationPay > 0):
            QualifationPay1 = QualificationPay
        else:
            QualificationPay1 = 0

        if (FixedPersonalPay > 0):
            FixedPersonalPay1 = FixedPersonalPay
        else:
            FixedPersonalPay1 = 0

        if (OtherPay > 0):
            OtherPay1 = OtherPay
        else:
            OtherPay1 = 0

        if (YearsOfService >= 33):
            YearsOfService1 = 33
        elif (YearsOfService >= 10):
            YearsOfService1 = YearsOfService
        else:
            YearsOfService1 = 0

        if (CommutationPercent >= 33.33):
            CommutationPercent1 = 33.3333
        elif (CommutationPercent > 0):
            CommutationPercent1 = CommutationPercent
        else:
            CommutationPercent1 = 0

        if (AgeAtNextbirthday > 0):
            AgeAtNextbirthday1 = AgeAtNextbirthday
        else:
            AgeAtNextbirthday1 = 0

        if (AgeAtNextbirthday == 28):
            CommutationFactor = 18.07

        elif (AgeAtNextbirthday == 29):
            CommutationFactor = 17.93

        elif (AgeAtNextbirthday == 30):
            CommutationFactor = 17.78


        elif (AgeAtNextbirthday == 31):
            CommutationFactor = 17.62


        elif (AgeAtNextbirthday == 32):
            CommutationFactor = 17.46
        elif (AgeAtNextbirthday == 33):
            CommutationFactor = 17.29

        elif (AgeAtNextbirthday == 34):
            CommutationFactor = 17.11


        elif (AgeAtNextbirthday == 35):
            CommutationFactor = 16.92


        elif (AgeAtNextbirthday == 36):
            CommutationFactor = 16.72


        elif (AgeAtNextbirthday == 37):
            CommutationFactor = 16.52


        elif (AgeAtNextbirthday == 38):
            CommutationFactor = 16.31


        elif (AgeAtNextbirthday == 39):
            CommutationFactor = 16.09


        elif (AgeAtNextbirthday == 40):
            CommutationFactor = 15.87


        elif (AgeAtNextbirthday == 41):
            CommutationFactor = 15.64


        elif (AgeAtNextbirthday == 42):
            CommutationFactor = 15.40


        elif (AgeAtNextbirthday == 43):
            CommutationFactor = 15.15


        elif (AgeAtNextbirthday == 44):
            CommutationFactor = 14.90


        elif (AgeAtNextbirthday == 45):
            CommutationFactor = 14.64


        elif (AgeAtNextbirthday == 46):
            CommutationFactor = 14.37


        elif (AgeAtNextbirthday == 47):
            CommutationFactor = 14.10

        elif (AgeAtNextbirthday == 48):
            CommutationFactor = 13.82

        elif (AgeAtNextbirthday == 49):
            CommutationFactor = 13.54

        elif (AgeAtNextbirthday == 50):
            CommutationFactor = 13.25

        elif (AgeAtNextbirthday == 51):
            CommutationFactor = 12.95

        elif (AgeAtNextbirthday == 52):
            CommutationFactor = 12.66

        elif (AgeAtNextbirthday == 53):
            CommutationFactor = 12.35

        elif (AgeAtNextbirthday == 54):
            CommutationFactor = 12.05

        elif (AgeAtNextbirthday == 55):
            CommutationFactor = 11.73

        elif (AgeAtNextbirthday == 56):
            CommutationFactor = 11.42

        elif (AgeAtNextbirthday == 57):
            CommutationFactor = 11.10

        elif (AgeAtNextbirthday == 58):
            CommutationFactor = 10.78

        elif (AgeAtNextbirthday == 59):
            CommutationFactor = 10.46

        elif (AgeAtNextbirthday == 60):
            CommutationFactor = 10.13

        elif (AgeAtNextbirthday == 61):
            CommutationFactor = 9.81

        elif (AgeAtNextbirthday == 62):
            CommutationFactor = 9.48

        elif (AgeAtNextbirthday == 63):
            CommutationFactor = 9.15

        elif (AgeAtNextbirthday == 64):
            CommutationFactor = 8.82

        elif (AgeAtNextbirthday == 65):
            CommutationFactor = 8.50
        # Calculation for Basic pension and Commutation Amount..........................................
        basicPension = .5 * (float(BasicPay1) + float(SpecialPay1) + float(StagnationPay1) + float(QualifationPay1) + float(FixedPersonalPay1) + float(OtherPay1)) * float(YearsOfService1) / 33
        basicpension1 = round(basicPension)
        CommutationAmount = basicPension * CommutationPercent1 / 100
        CommutationAmount1 = round(CommutationAmount)
        CommutationValue = CommutationAmount * CommutationFactor * 12
        CommutationValue1 = round(CommutationValue)
        ReducedBasicPension = (basicpension1 - CommutationAmount1)
        # If input is invalid...............................................................
        if cond is False:
            el1.set("Invalid Input")
            t1.grid(row=13, column=0)
            t2.grid_forget()
            t3.grid_forget()
            t4.grid_forget()
            t5.grid_forget()
            result.grid_forget()
        else:
            # If input is valid..........................................................
            el1.set("BASIC PENSION : " + str(basicpension1))
            el2.set('COMMUTATION AMOUNT : ' + str(CommutationAmount1))
            el3.set('REDUCED BASIC PENSION : ' + str(ReducedBasicPension))
            el4.set('COMMUTATION FACTOR : ' + str(CommutationFactor))
            el5.set('COMMUTATION VALUE : ' + str(CommutationValue1))
            result.grid(row=12, column=0, columnspan=5)
            t1.grid(row=13, column=0)
            t2.grid(row=14, column=0)
            t3.grid(row=15, column=0)
            t4.grid(row=16, column=0)
            t5.grid(row=17, column=0)
            query = 'INSERT INTO pension_record(Id,name,Basic_pansion,Commutation_amount) values(%s, %s, %s, %s);'
            values = (Id1, Name1, basicpension1, CommutationAmount1)
            cur.execute(query, values)
            con.commit()
            print('sucessfully inserted')

    # Designing frame ......................................................................
    l10 = Label(window, text="Enter the id :").grid(row=1, column=0, columnspan=2)
    l11 = Label(window, text="Enter the name :").grid(row=2, column=0, columnspan=2)
    l1 = Label(window, text="Enter Basic Pay : ", anchor="w")
    l2 = Label(window, text="Enter special Pay :")
    l3 = Label(window, text="Enter Stagnation Pay : ")
    l4 = Label(window, text="Enter Qualification Pay : ")
    l5 = Label(window, text="Enter Fixed Personal Pay (Portion Eligibe for PF Deduction ) : ")
    l6 = Label(window, text="Enter Other Pay (portion Eligible For PF Deduction) : ")
    l7 = Label(window, text="Enter Years of Service (Maximum 33 Years) : ")
    l8 = Label(window, text="Enter Age At Next Birthday : ")
    l9 = Label(window, text="Enter Commutation Percentage (MAX= 33.3333%) : ")
    e10 = Entry(window)
    e11 = Entry(window)
    e1 = Entry(window, textvariable=e_val1)
    e2 = Entry(window, textvariable=e_val2)
    e3 = Entry(window, textvariable=e_val3)
    e4 = Entry(window, textvariable=e_val4)
    e5 = Entry(window, textvariable=e_val5)
    e6 = Entry(window, textvariable=e_val6)
    e7 = Entry(window, textvariable=e_val7)
    e8 = Entry(window, textvariable=e_val8)
    e9 = Entry(window, textvariable=e_val9)
    b1 = Button(window, text="Calculate", command=logic)
    b2 = Button(window, text="Show data", command=onClickShowAllF2)

    intro.grid(row=0, column=0, columnspan=5)
    e10.grid(row=1, column=2, columnspan=3)
    e11.grid(row=2, column=2, columnspan=3)
    l1.grid(row=3, column=0, columnspan=2)
    e1.grid(row=3, column=2, columnspan=3)
    l2.grid(row=4, column=0, columnspan=2)
    e2.grid(row=4, column=2, columnspan=3)
    l3.grid(row=5, column=0, columnspan=2)
    e3.grid(row=5, column=2, columnspan=3)
    l4.grid(row=6, column=0, columnspan=2)
    e4.grid(row=6, column=2, columnspan=3)
    l5.grid(row=7, column=0, columnspan=2)
    e5.grid(row=7, column=2, columnspan=3)
    l6.grid(row=8, column=0, columnspan=2)
    e6.grid(row=8, column=2, columnspan=3)
    l7.grid(row=9, column=0, columnspan=2)
    e7.grid(row=9, column=2, columnspan=3)
    l8.grid(row=10, column=0, columnspan=2)
    e8.grid(row=10, column=2, columnspan=3)
    l9.grid(row=11, column=0, columnspan=2)
    e9.grid(row=11, column=2, columnspan=3)
    b1.grid(row=13, column=3, columnspan=1)
    b2.grid(row=13, column=4, columnspan=1)
    window.mainloop()
# Exception block for connection print error.......................................................
except Error as err:
    print(err)
# Finally block for connection giving message for connection close..................................
finally:
    if con.is_connected():
        cur.close()
        con.close()
        print('connection is closed')