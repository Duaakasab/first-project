from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


class Student():
    #_______ WINDOW______
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x690+1+1")
        self.root.title("School management program")
        self.root.configure(background="silver")
        self.root.resizable(False,False)
        title = Label(self.root,
        text="Student registration system",
        bg="#1AAECB",
        font=("monospace",14,"bold"),
        fg="white")
        title.pack(fill=X)
        #___________variable _____
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()
        self.certi_var = StringVar()
        self.gender_var = StringVar()
        self.address_var = StringVar()
        self.se_var = StringVar()
        self.se_by = StringVar()
        self.dell_var = StringVar()

        #________CONTROL ROOTS_____
        Manage_Frame = Frame(self.root,bg="white")
        Manage_Frame.place(x=1137,y=30,width=210,height=400)
        lb1_Id = Label(Manage_Frame,text="Serial number",bg="white")
        lb1_Id.pack()
        ID_Entry = Entry(Manage_Frame,textvariable=self.id_var, bd="2",justify="center")
        ID_Entry.pack()
        lbl_name = Label(Manage_Frame,bg="white",text="Student's name")
        lbl_name.pack()
        name_Entry = Entry(Manage_Frame,textvariable=self.name_var, bd="2",justify="center")
        name_Entry.pack()
        lbl_email = Label(Manage_Frame, bg="white", text="Student's E-mail")
        lbl_email.pack()

        email_Entry = Entry(Manage_Frame,textvariable=self.email_var, bd="2", justify="center")
        email_Entry.pack()

        lbl_phone = Label(Manage_Frame, bg="white", text="Student's phone number")
        lbl_phone.pack()

        phone_Entry = Entry(Manage_Frame,textvariable=self.phone_var, bd="2", justify="center")
        phone_Entry.pack()

        lbl_certi = Label(Manage_Frame, bg="white", text="the certi of student")
        lbl_certi.pack()

        certi_Entry = Entry(Manage_Frame,textvariable=self.certi_var, bd="2", justify="center")
        certi_Entry.pack()

        lbl_gender = Label(Manage_Frame , text="Choose the number of the student" ,bg="white")
        lbl_gender.pack()
        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.gender_var)
        combo_gender['value'] = ("boy","girl")
        combo_gender.pack()
        lbl_address = Label(Manage_Frame, text= "Student's address", bg="white")
        lbl_address.pack()
        adress_Entry = Entry(Manage_Frame ,textvariable=self.address_var, bd="2", justify="center")
        adress_Entry.pack()
        lbl_delete = Label(Manage_Frame ,fg="red" , bg="white", text="Delete student")
        lbl_delete.pack()
        delete_Entry = Entry(Manage_Frame,textvariable=self.dell_var, bd="2" , justify="center")
        delete_Entry.pack()
        #________ buttons ________
        btn_Frame = Frame(self.root, bg="white")
        btn_Frame.place(x=1137, y=435 ,width=210 , height= 253)
        title1=Label(btn_Frame, text="Control panel", font=("deco",14),fg="white",bg="#2980B9")
        title1.pack(fill=X)
        add_btn = Button(btn_Frame, text="Add student" ,bg= "#85929E",fg="white",command=self.add_student)
        add_btn.place(x=33,y=40,width=150,height=30)

        del_btn = Button(btn_Frame, text="Delete student" , bg= "#85929E",fg="white",command=self.delete)
        del_btn.place(x=33, y=75, width=150, height=30)
        update_btn = Button(btn_Frame, text="Edit student data" , bg= "#85929E",fg="white",command=self.edit)
        update_btn.place(x=33, y=110, width=150, height=30)
        clear_btn = Button(btn_Frame, text="Empty fields"  , bg= "#85929E",fg="white",command=self.clear )
        clear_btn.place(x=33, y=145, width=150, height=30)
        about_btn = Button(btn_Frame, text="About the developer" , bg= "#85929E",fg="white",command=self.about)
        about_btn.place(x=33, y=180, width=150, height=30)
        exit_btn = Button(btn_Frame, text="Close the program" ,bg= "#85929E",fg="white",command=root.quit)
        exit_btn.place(x=33, y=215, width=150, height=30)
        #__________ search mange__________
        search_Frame = Frame(self.root,bg="white")
        search_Frame.place(x=2,y=30,width=1134,height=50)
        lbl_search = Label( search_Frame , text="Search of student",bg="white")
        lbl_search.place(x=1034,y=12)

        combo_search = ttk.Combobox(search_Frame,justify="left")
        combo_search["value"]=("ID","Name","E-mail","phone")
        combo_search.place(x=890,y=12)
        search_Entry = Entry(search_Frame,textvariable=self.se_var,justify="left",bd="2")
        search_Entry.place(x=750,y=12)
        se_btn = Button(search_Frame,text="Search",bg="#3498DB",fg="white",command=self.search)
        se_btn.place(x=630,y=9,width=100,height=25)
        #--------- dietals -------
        Dietals_Frame = Frame(self.root,bg="#F2F4F4")
        Dietals_Frame.place(x=2,y=82,width=1133,height=605)
        #------- SCROLL---------
        scroll_x=Scrollbar(Dietals_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Dietals_Frame,orient=VERTICAL)
        #---------treeveiw-------
        self.student_table=ttk.Treeview(Dietals_Frame,
        columns=('address','gender','phone','certi','E-mail','name','Id'),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set)
        self.student_table.place(x=18,y=1,width=1130,height=590)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table['show']='headings'
        self.student_table.heading('address',text="the ID of student")
        self.student_table.heading('gender', text="the name of student")
        self.student_table.heading('certi', text="the E-mail address of student")
        self.student_table.heading('phone', text="the phone number of student")
        self.student_table.heading('E-mail', text="the certi of student")
        self.student_table.heading('name', text="the gender of student")
        self.student_table.heading('Id', text="the address of student")

        self.student_table.column("Id",width=130)
        self.student_table.column("name",width=30)
        self.student_table.column("E-mail",width=65)
        self.student_table.column("phone",width=65)
        self.student_table.column("certi",width=70)
        self.student_table.column("gender",width=100)
        self.student_table.column("address",width=20)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        #__________ con + ad __________
        self.fetch_all()
    def add_student(self):
            con = pymysql.connect(host="localhost", user="root", password="", database="stud")
            cur = con.cursor()
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                self.id_var.get(),
                                                                self.name_var.get(),
                                                                self.phone_var.get(),
                                                                self.email_var.get(),
                                                                self.certi_var.get(),
                                                                self.gender_var.get(),
                                                                self.address_var.get()
            ))
            con.commit()
            self.fetch_all()
            self.clear()
            con.close()

    def fetch_all(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stud")
        cur = con.cursor()
        cur.execute("select *  from student ")
        rows = cur.fetchall()
        if len (rows) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values =row)
            con.commit()
        con.close()

    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stud")
        cur = con.cursor()
        cur.execute("delete from student where name=%s",self.dell_var.get())
        con.commit()
        self.fetch_all()
        con.close()

    def clear(self):
        self.id_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.certi_var.set("")
        self.gender_var.set("")
        self.address_var.set("")

    def get_cursor(self,ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row=contents["values"]
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.phone_var.set(row[3])
        self.certi_var.set(row[4])
        self.gender_var.set(row[5])
        self.address_var.set(row[6])

    def edit(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stud")
        cur = con.cursor()
        cur.execute("update student set address=%s , gender=%s, certi=%s , email=%s , phone=%s , name=%s where id=%s", (
            self.address_var.get(),
            self.gender_var.get(),
            self.certi_var.get(),
            self.email_var.get(),
            self.phone_var.get(),
            self.name_var.get(),
            self.id_var.get()
        ))

        con.commit()
        self.fetch_all()
        self.clear()
        con.close()

    def search(self):
            con = pymysql.connect(host="localhost", user="root", password="", database="stud")
            cur = con.cursor()
            cur.execute("select * from student where " +
            str(self.se_by.get())+" LIKE '%"+str(self.se_var.get())+"%'")
            rows = cur.fetchall()
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END,values=row)
                con.commit()
            con.close()

    def about(self):
        messagebox.showinfo("Devloper duaa alkassab","Welcome to our first project")






root = Tk()
ob = Student(root)
root.mainloop()
root.mainloop()
