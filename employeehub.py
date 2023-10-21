from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x685+0+0")  #window size
        self.root.title('EmployeeHub')  #window title name

        

        #variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_desig=StringVar()
        self.var_email=StringVar()
        self.var_marital_status=StringVar()
        self.var_address=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_combo_id=StringVar()
        self.var_id_proof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()




        # project title  
        lbl_title=Label(self.root,text='EMPLOYEE-HUB ',font=('Times New Roman',37,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1350,height=50)

        
        #logo image
        img_logo=Image.open('Images\logo.png')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=170,y=0,width=50,height=50)


        
        #img frame
        img_frame=Frame(self.root,border=2,relief=RIDGE,background='white')
        img_frame.place(x=0,y=50,width=1350,height=160)

        # 1 img
        img_1=Image.open('Images\img1.jpg')
        img_1=img_1.resize((540,160),Image.ANTIALIAS)
        self.photo_1=ImageTk.PhotoImage(img_1)

        self.img1=Label(img_frame,image=self.photo_1)
        self.img1.place(x=0,y=0,width=540,height=160)


        # 2 img
        img_2=Image.open('Images\img2.jpg')
        img_2=img_2.resize((540,160),Image.ANTIALIAS)
        self.photo_2=ImageTk.PhotoImage(img_2)

        self.img2=Label(img_frame,image=self.photo_2)
        self.img2.place(x=500,y=0,width=540,height=160)


        #3 img
        img_3=Image.open('Images\img3.jpg')
        img_3=img_3.resize((540,160),Image.ANTIALIAS)
        self.photo_3=ImageTk.PhotoImage(img_3)

        self.img3=Label(img_frame,image=self.photo_3)
        self.img3.place(x=1000,y=0,width=540,height=160)


        
        #main frame
        main_frame=Frame(self.root,border=2,relief=RIDGE,background='white')
        main_frame.place(x=10,y=220,width=1330,height=455)

        #upper frame
        upper_frame=LabelFrame(main_frame,border=2,relief=RIDGE,background='white', text='Employee Details', font=('Times New Roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=3,width=1305,height=220)

        #Labels and entry field
        #For department
        lbl_dep=Label(upper_frame,text='Department:',font=('arial',11,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',11),width=15,state='readonly')
        combo_dep['value']=('Select Department','HR','Mnager','Software Engineer','Data Analytics','Data Scientist')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #for name
        lbl_name=Label(upper_frame,text='Name:',font=('arial',11,'bold'),bg='white')
        lbl_name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=20,font=('arial',10,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        #for Designation
        lbl_desig=Label(upper_frame,text='Designation:',font=('arial',11,'bold'),bg='white')
        lbl_desig.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_desig=ttk.Entry(upper_frame,textvariable=self.var_desig,width=20,font=('arial',10,'bold'))
        txt_desig.grid(row=1,column=1,padx=2,pady=7)

        #for email
        lbl_email=Label(upper_frame,text='Email:',font=('arial',11,'bold'),bg='white')
        lbl_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=20,font=('arial',10,'bold'))
        txt_email.grid(row=1,column=3,padx=2,pady=7)

        #for marital status
        lbl_marital=Label(upper_frame,text='Marital Status:',font=('arial',11,'bold'),bg='white')
        lbl_marital.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        combo_marital=ttk.Combobox(upper_frame,textvariable=self.var_marital_status,font=('arial',11),width=15,state='readonly')
        combo_marital['value']=('Select Marital Status','Married','Unmarried','Divorced')
        combo_marital.current(0)
        combo_marital.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #for Address
        lbl_add=Label(upper_frame,text='Address:',font=('arial',11,'bold'),bg='white')
        lbl_add.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        txt_add=ttk.Entry(upper_frame,textvariable=self.var_address,width=20,font=('arial',10,'bold'))
        txt_add.grid(row=2,column=3,padx=2,pady=7)

        #for date of birth
        lbl_dob=Label(upper_frame,text='Birth Date:',font=('arial',11,'bold'),bg='white')
        lbl_dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=20,font=('arial',10,'bold'))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        #for date of joining
        lbl_doj=Label(upper_frame,text='Joining Date:',font=('arial',11,'bold'),bg='white')
        lbl_doj.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=20,font=('arial',10,'bold'))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)

        #for id proof
        combo_id=ttk.Combobox(upper_frame,textvariable=self.var_combo_id,font=('arial',11),width=15,state='readonly')
        combo_id['value']=('Select ID Proof','PAN Card','Aadhar Card','Driving Licence')
        combo_id.current(0)
        combo_id.grid(row=4,column=0,padx=2,pady=10,sticky=W)

        txt_id=ttk.Entry(upper_frame,textvariable=self.var_id_proof,width=20,font=('arial',10,'bold'))
        txt_id.grid(row=4,column=1,padx=2,pady=7)

        #for gender
        lbl_gender=Label(upper_frame,text='Gender:',font=('arial',11,'bold'),bg='white')
        lbl_gender.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        combo_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',11),width=15,state='readonly')
        combo_gender['value']=('Select Gender','Male','Female','Other')
        combo_gender.current(0)
        combo_gender.grid(row=4,column=3,padx=2,pady=10,sticky=W)

        #for phone
        lbl_phone=Label(upper_frame,text='Contact Number:',font=('arial',11,'bold'),bg='white')
        lbl_phone.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=20,font=('arial',10,'bold'))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        #for country
        lbl_country=Label(upper_frame,text='Country:',font=('arial',11,'bold'),bg='white')
        lbl_country.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=20,font=('arial',10,'bold'))
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        #for salary
        lbl_ctc=Label(upper_frame,text='Salary(CTC):',font=('arial',11,'bold'),bg='white')
        lbl_ctc.grid(row=2,column=4,padx=2,pady=7,sticky=W)

        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=20,font=('arial',10,'bold'))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7)

        #employee img
        img_emp=Image.open('Images\emp.jpg')
        img_emp=img_emp.resize((220,220),Image.ANTIALIAS)
        self.photo_emp=ImageTk.PhotoImage(img_emp)

        self.img_emp=Label(upper_frame,image=self.photo_emp)
        self.img_emp.place(x=900,y=0,width=220,height=190)

        #button frame
        button_frame=Frame(upper_frame,border=2,relief=RIDGE,background='white')
        button_frame.place(x=1130,y=5,width=150,height=185)

        btn_add=Button(button_frame,text='Save',command=self.add_data,font=('arial',15,'bold'),width='13',bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=3)

        btn_update=Button(button_frame,text='Update',command=self.update_data,font=('arial',15,'bold'),width='13',bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=3)

        btn_delete=Button(button_frame,text='Delete',command=self.delete_data,font=('arial',15,'bold'),width='13',bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=3)

        btn_clear=Button(button_frame,text='Clear',command=self.reset_data,font=('arial',15,'bold'),width='13',bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=3)


        #lower frame
        lower_frame=LabelFrame(main_frame,border=2,relief=RIDGE,background='white', text='Employee Details Table', font=('Times New Roman',11,'bold'),fg='red')
        lower_frame.place(x=10,y=227,width=1305,height=220)

        #search frame
        search_frame=LabelFrame(lower_frame,border=2,relief=RIDGE,background='white', text='Search Employee Details', font=('Times New Roman',11,'bold'),fg='red')
        search_frame.place(x=2,y=0,width=1295,height=60)

        search_by=Label(search_frame,font=('arial',10,'bold'),text='Search By:',fg='white',bg='Red')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #search
        self.var_com_search=StringVar()
        combo_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',11),width=15,state='readonly')
        combo_search['value']=('Select Option','ID Proof','Contact')
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=5,sticky=W)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=20,font=('arial',10,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text='Search',command=self.search_data,font=('arial',15,'bold'),width='13',bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5)

        btn_showall=Button(search_frame,text='Show All',command=self.fetch_data,font=('arial',15,'bold'),width='13',bg='blue',fg='white')
        btn_showall.grid(row=0,column=4,padx=5)
        
        img_ext=Image.open('Images\ext.jpg')
        img_ext=img_ext.resize((500,60),Image.ANTIALIAS)
        self.photo_ext=ImageTk.PhotoImage(img_ext)

        self.img_ext=Label(search_frame,image=self.photo_ext)
        self.img_ext.place(x=770,y=0,width=500,height=40)

        #=========Employee Table===========
        #table frame
        table_frame=Frame(lower_frame,border=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1300,height=140)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=('dep','name','desig','email','marital_status','address','dob','doj','id_proof_type','id_proof','gender','phone','country','salary',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        
        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('desig',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('marital_status',text='Marital_Status')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('dob',text='Birth_Date')
        self.employee_table.heading('doj',text='Joining_Date')
        self.employee_table.heading('id_proof_type',text='ID_Proof_Type')
        self.employee_table.heading('id_proof',text='ID_Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Contact_Number')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary(CTC)')

        self.employee_table['show']='headings'

        self.employee_table.column('dep',width=150)
        self.employee_table.column('name',width=150)
        self.employee_table.column('desig',width=150)
        self.employee_table.column('email',width=150)
        self.employee_table.column('marital_status',width=150)
        self.employee_table.column('address',width=150)
        self.employee_table.column('dob',width=150)
        self.employee_table.column('doj',width=150)
        self.employee_table.column('id_proof_type',width=150)
        self.employee_table.column('id_proof',width=150)
        self.employee_table.column('gender',width=150)
        self.employee_table.column('phone',width=150)
        self.employee_table.column('country',width=150)
        self.employee_table.column('salary',width=150)

        self.employee_table.pack(fill='both',expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    #*******************Function Declaration*******************
    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are Required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Vivek@mysql',database='employee_management_system')
                my_cursor=conn.cursor()
                my_cursor.execute('INSERT INTO emp VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                 (self.var_dep.get(), self.var_name.get(), self.var_desig.get(), self.var_email.get(),
                  self.var_marital_status.get(), self.var_address.get(), self.var_dob.get(), self.var_doj.get(),
                  self.var_combo_id.get(), self.var_id_proof.get(), self.var_gender.get(), self.var_phone.get(),
                  self.var_country.get(), self.var_salary.get()))

                                                                                                               
         
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee has been successfully added',parent=self.root)
            except Exception as ex:
                messagebox.showerror('Error',f'Due To:{str(ex)}',parent=self.root)


    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Vivek@mysql',database='employee_management_system')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from emp')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END, values=i)
            conn.commit()
        conn.close()


    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_desig.set(data[2])
        self.var_email.set(data[3])
        self.var_marital_status.set(data[4])
        self.var_address.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_combo_id.set(data[8])
        self.var_id_proof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])       


    # update data

    def update_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All Fields are Required')
        else:
            try:
                update = messagebox.askyesno('Update', 'Are you sure to update Employee data')
                if update:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Vivek@mysql', database='employee_management_system')
                    my_cursor = conn.cursor()
                    query = 'UPDATE emp SET Department=%s, Name=%s, Designation=%s, Email=%s, `Marital Status`=%s, Address=%s, `Birth Date`=%s, `Joining Date`=%s, `ID Proof Type`=%s, Gender=%s, Contact=%s, Country=%s, Salary=%s WHERE `ID Proof`=%s'
                    values = (
                    self.var_dep.get(), self.var_name.get(), self.var_desig.get(), self.var_email.get(),
                    self.var_marital_status.get(), self.var_address.get(), self.var_dob.get(), self.var_doj.get(),
                    self.var_combo_id.get(), self.var_gender.get(), self.var_phone.get(),
                    self.var_country.get(), self.var_salary.get(), self.var_id_proof.get()
                    )
                    my_cursor.execute(query, values)
                    conn.commit()
                    conn.close()
                    self.fetch_data()
                    messagebox.showinfo('Success', 'Employee Successfully Updated!', parent=self.root)
                else:
                    return
            except Exception as ex:
                messagebox.showerror('Error', f'Due To: {str(ex)}', parent=self.root)

        
    # Delete Data
    def delete_data(self):
        if self.var_id_proof.get()=="":
            messagebox.showerror('Error','All Fields are Required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure, You want to Delete Employee Data',parent=self.root)
                if Delete>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Vivek@mysql', database='employee_management_system')
                    my_cursor = conn.cursor()
                    sql='delete from emp where `ID Proof`=%s'
                    value=(self.var_id_proof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee Data has been successfully Deleted',parent=self.root)
            except Exception as ex:
                messagebox.showerror('Error',f'Due To:{str(ex)}',parent=self.root)


    # Reset Data
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_desig.set("")
        self.var_email.set("")
        self.var_marital_status.set("Select Marital Status")
        self.var_address.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_combo_id.set("Select ID Proof")
        self.var_id_proof.set("")
        self.var_gender.set("Select Gender")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")

    
    # Search data
    
    def search_data(self):
        if self.var_com_search.get() == '' or self.var_search.get() == '':
            messagebox.showerror('Error', 'Please Select Option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Vivek@mysql', database='employee_management_system')
                my_cursor = conn.cursor()
                search_column = self.var_com_search.get()
                search_value = self.var_search.get()
                query = f"SELECT * FROM emp WHERE `{search_column}` LIKE '%{search_value}%'"
                my_cursor.execute(query)
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("", END, values=i)
                conn.commit()
                conn.close()
            except Exception as ex:
                messagebox.showerror('Error', f'Due To: {str(ex)}', parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()        