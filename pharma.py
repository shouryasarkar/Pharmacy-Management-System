from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class PharmacyManagementSystem:
    def __init__(self,root):
        self.root = root

        # Setting the title of the GUI window
        self.root.title("Pharmacy Management System")

        # Setting the size of the window 
        self.root.geometry("1550x800+0+0")

        ######## ADD MED VARIABLE ########

        self.addmed_var = StringVar()
        self.refmed_var = StringVar()

        ################ MAIN TEXT VARIABLE ################

        self.ref_var = StringVar()
        self.cmpName_var = StringVar()
        self.typeMed_var = StringVar()
        self.medName_var = StringVar()
        self.lot_var = StringVar()
        self.issuedate_var = StringVar()
        self.expdate_var = StringVar()
        self.uses_var = StringVar()
        self.sideEffect_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.product_var = StringVar()


        # Creating a Label and setting border and border style
        label_title = Label(self.root, text="MEDICARE PLUS",bd=15,relief=RIDGE
                                ,bg="white",fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)

        # To show the label in the window we use the pack mathod
        label_title.pack(side=TOP, fill=X)


        # Importing the Logo image
        image1 = Image.open("doctor.png")
        image1 = image1.resize((80,80),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(image1)
        button1 = Button(self.root,image=self.photoimage1,borderwidth=0)
        button1.place(x=50,y=15)


        ################################## DATA FRAME ##################################### 
        data_frame = Frame(self.root,bd=15,relief=RIDGE,padx=20)
        data_frame.place(x=0,y=120,width=1530,height=400)

        # This is the dataframe for the left side 
        data_frame_left = LabelFrame(data_frame,bd=10,relief=RIDGE,padx=20,text="Medicine Details",
                                        fg="darkgreen",font=("arial",12,"bold"))
        data_frame_left.place(x=0,y=5,width=900,height=350)


        ############################################ BUTTONS FRAME ##############################################
        button_frame = Frame(self.root,bd=15,relief=RIDGE,padx=20)
        button_frame.place(x=0,y=520,width=1530,height=69)
        
        ####################################### MAIN BUTTONS ####################################################

        ####################### ADD BUTTON ######################
        add_data_button = Button(button_frame,command=self.add_data,text="ADD MEDICINE", font=("arial",12,"bold"),width=14, bg="darkgreen", fg="white")
        add_data_button.grid(row=0, column=0)

        ###################### UPDATE BUTTON ###################
        update_data_button = Button(button_frame,command=self.update, text="UPDATE", font=("arial",12,"bold"),width=14, bg="lightgreen", fg="white")
        update_data_button.grid(row=0, column=1)

        ##################### DELETE BUTTON ###################
        delete_data_button = Button(button_frame,command=self.delete, text="DELETE", font=("arial",12,"bold"), width=14, bg="red", fg="white")
        delete_data_button.grid(row=0, column=2)

        #################### RESET BUTTON ####################
        reset_data_button = Button(button_frame,command=self.reset, text="RESET", font=("arial",12,"bold"),width=14, bg="yellow", fg="white")
        reset_data_button.grid(row=0, column=3)

        #################### EXIT BUTTON ####################
        exit_data_button = Button(button_frame, text="EXIT", font=("arial",12,"bold"),width=14, bg="lightblue", fg="white")
        exit_data_button.grid(row=0, column=4)

        ############# SEARCH SPACE #############
        search_label = Label(button_frame, font=("arial",17,"bold"),text="Search By",padx=2,bg="red", fg="white")
        search_label.grid(row=0,column=5,sticky=W)

        self.search_variable = StringVar()

        search_combo = ttk.Combobox(button_frame,textvariable=self.search_variable,width=10, font=("arial",17,"bold"), state="readonly")
        search_combo["values"] = ("Ref No", "Med No", "Lot No")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        self.search_text = StringVar()
        
        text_search = Entry(button_frame,textvariable=self.search_text,bd=3,relief=RIDGE,width=13,font=("arial",17,"bold"))
        text_search.grid(row=0,column=7)


        #################### SEARCH BUTTON ####################
        search_data_button = Button(button_frame,command=self.search_data, text="SEARCH", font=("arial",12,"bold"),width=12, bg="white", fg="grey")
        search_data_button.grid(row=0, column=8)


        #################### SHOW BUTTON ####################
        show_data_button = Button(button_frame, command=self.fetch_data,text="SHOW ALL", font=("arial",12,"bold"),width=12, bg="blue", fg="white")
        show_data_button.grid(row=0, column=9)
        
        
        ########################################## ENTRY AND LABELS ######################################
        reference_label = Label(data_frame_left, font=("arial",12,"bold"),text="Reference No",padx=2)
        reference_label.grid(row=0,column=0,sticky=W)

        # Connection with mysql is made
        connection = mysql.connector.connect(host="localhost", username= "root", password="root123",database="mypharmacy")
        my_cursor = connection.cursor()
        my_cursor.execute("select Ref from pharma")
        row = my_cursor.fetchall()

        ref_combo = ttk.Combobox(data_frame_left,textvariable=self.ref_var,width=20, font=("arial",17,"bold"), state="readonly")
        ref_combo["values"] = row
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)

        ############################ COMPANY NAME #############################
        company_name = Label(data_frame_left, font=("arial",12,"bold"),text="Company Name",padx=2)
        company_name.grid(row=1,column=0,sticky= W)
        company_name = Entry(data_frame_left,textvariable=self.cmpName_var,bd=2,relief=RIDGE,width=20,font=("arial",17,"bold"))
        company_name.grid(row=1,column=1)


        ########################################## TYPE OF MEDICINE ######################################
        medicine_label = Label(data_frame_left, font=("arial",12,"bold"),text="Type of Medicine",padx=2)
        medicine_label.grid(row=2,column=0,sticky=W)

        med_combo = ttk.Combobox(data_frame_left,textvariable=self.typeMed_var,width=20, font=("arial",17,"bold"), state="readonly")
        med_combo["values"] = ("Tablet", "Liquid", "Capsules", "Drops", "Inhalers", "Injection")
        med_combo.grid(row=2,column=1)
        med_combo.current(0)


        #################################### ADD MEDICINE ##################################
        label_medicine_name = Label(data_frame_left,font=("arial",12,"bold"), text="Medicine Name",padx=2,pady=6)
        label_medicine_name.grid(row=3,column=0,sticky=W)

        # Connection with mysql is made
        connection = mysql.connector.connect(host="localhost", username= "root", password="root123",database="mypharmacy")
        my_cursor = connection.cursor()
        my_cursor.execute("select MedName from pharma")
        med = my_cursor.fetchall()

        company_medicine_name = ttk.Combobox(data_frame_left,textvariable=self.medName_var,width=29,font=("arial",12,"bold"),state="readonly")
        company_medicine_name["value"] = med
        company_medicine_name.grid(row=3,column=1)
        company_medicine_name.current(0)


        label_lot_number = Label(data_frame_left,font=("arial",12,"bold"),text="Lot No:",padx=2, pady=6)
        label_lot_number.grid(row=4,column=0,sticky=W)
        text_lot_number = Entry(data_frame_left,textvariable=self.lot_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        text_lot_number.grid(row=4,column=1)

        label_issue_date = Label(data_frame_left,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        label_issue_date.grid(row=5,column=0,sticky=W)
        text_issue_date = Entry(data_frame_left,textvariable=self.issuedate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        text_issue_date.grid(row=5,column=1)

        label_expiery_data = Label(data_frame_left,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        label_expiery_data.grid(row=6,column=0,sticky=W)
        text_expiry_date = Entry(data_frame_left,textvariable=self.expdate_var,font=("aria",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        text_expiry_date.grid(row=6,column=1)

        label_uses = Label(data_frame_left,font=("arial",12,"bold"),text="Uses:",padx=2,pady=6)
        label_uses.grid(row=7,column=0,sticky=W)
        text_uses = Entry(data_frame_left,textvariable=self.uses_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        text_uses.grid(row=7,column=1)

        label_side_effects = Label(data_frame_left,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        label_side_effects.grid(row=8,column=0,sticky=W)
        text_side_effects = Entry(data_frame_left,textvariable=self.sideEffect_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        text_side_effects.grid(row=8,column=1)

        label_prec_warning = Label(data_frame_left,font=("arial",12,"bold"),text="Prec&Warning:",padx=15)
        label_prec_warning.grid(row=0,column=2,sticky=W)
        text_prec_warning = Entry(data_frame_left,textvariable=self.warning_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        text_prec_warning.grid(row=0,column=3)

        label_dosage = Label(data_frame_left,font=("arial",12,"bold"),text="Dosage:",padx=15,pady=6)
        label_dosage.grid(row=1,column=2,sticky=W)
        text_dosage = Entry(data_frame_left,textvariable=self.dosage_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        text_dosage.grid(row=1,column=3)

        label_tab_price = Label(data_frame_left,font=("arial",12,"bold"),text="Tablets Price:",padx=15,pady=6)
        label_tab_price.grid(row=2,column=2,sticky=W)
        text_tab_price = Entry(data_frame_left,textvariable=self.price_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        text_tab_price.grid(row=2,column=3)

        label_pro_qt = Label(data_frame_left,font=("arial",12,"bold"),text="Product Quantity:",padx=15,pady=6)
        label_pro_qt.grid(row=3,column=2,sticky=W)
        text_pro_qt = Entry(data_frame_left,textvariable=self.product_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        text_pro_qt.grid(row=3,column=3,sticky=W)

        ################################### STAY HOME LABEL ###############################################
        label_home = Label(data_frame_left,font=("arial",12,"bold"),text="STAY HOME STAY SAFE",padx=1,pady=6,fg="red",width=40)
        label_home.place(x=420,y=140)

        # Importing the Logo image
        image2 = Image.open("tablet.jpeg")
        image2 = image2.resize((150,135),Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(image2)
        button1 = Button(self.root,image=self.photoimage2,borderwidth=0)
        button1.place(x=500,y=330)

        # Importing the Logo image
        image3 = Image.open("medicine.jpeg")
        image3 = image3.resize((150,135),Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(image3)
        button1 = Button(self.root,image=self.photoimage3,borderwidth=0)
        button1.place(x=700,y=330)

        ############################################# DATA FRAME RIGHT #########################################################

        # This is the data frame for the right side 
        data_frame_right = LabelFrame(data_frame,bd=10,relief=RIDGE,padx=20,text="Medicine Cart",
                                        fg="darkgreen",font=("arial",12,"bold"))
        data_frame_right.place(x=910,y=5,width=550,height=350)

        # Importing the medicine image
        image4 = Image.open("capsules.jpeg")
        image4 = image4.resize((200,75),Image.ANTIALIAS)
        self.photoimage4 = ImageTk.PhotoImage(image4)
        button1 = Button(self.root,image=self.photoimage4,borderwidth=0)
        button1.place(x=960,y=160)

        # Importing the medicine image
        image5 = Image.open("shop.jpeg")
        image5 = image5.resize((200,75),Image.ANTIALIAS)
        self.photoimage5 = ImageTk.PhotoImage(image5)
        button1 = Button(self.root,image=self.photoimage5,borderwidth=0)
        button1.place(x=1160,y=160)

        label_refno = Label(data_frame_right,font=("arial",12,"bold"),text="Reference No:",padx=15,pady=6)
        label_refno.place(x=0,y=80)
        text_refno = Entry(data_frame_right,textvariable=self.refmed_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=14)
        text_refno.place(x=140,y=80)

        label_medname = Label(data_frame_right,font=("arial",12,"bold"),text="Medicine Name:",padx=15,pady=6)
        label_medname.place(x=0,y=110)
        text_medname = Entry(data_frame_right,textvariable=self.addmed_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=14)
        text_medname.place(x=140,y=110)


        ################################################### SIDE FRAME #######################################################
        side_frame = Frame(data_frame_right,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=290,height=160)

        scroolbar_x = ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        scroolbar_x.pack(side=BOTTOM,fill=X)
        scroolbar_y = ttk.Scrollbar(side_frame,orient=VERTICAL)
        scroolbar_y.pack(side=RIGHT,fill=Y)


        self.medicine_table = ttk.Treeview(side_frame,column=("ref","medname"), xscrollcommand=scroolbar_x.set, yscrollcommand=scroolbar_y.set)

        scroolbar_x.config(command=self.medicine_table.xview)
        scroolbar_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill=BOTH,expand=1)
        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)

        self.medicine_table.bind("<ButtonRelease-1>",self.get_medicine)


        ################################################### MEDICINE ADD BUTTONS #####################################################
        down_frame = Frame(data_frame_right,bd=4,relief=RIDGE,bg="white")
        down_frame.place(x=330,y=150,width=135,height=160)

        add_medicine_button = Button(down_frame, text="ADD", font=("arial",12,"bold"),width=12, bg="green", fg="white",pady=4, command=self.add_med)
        add_medicine_button.grid(row=0, column=0)

        update_data_button = Button(down_frame, text="UPDATE", font=("arial",12,"bold"),width=12, bg="yellow", fg="white",pady=4,command=self.update_med)
        update_data_button.grid(row=1, column=0)

        delete_data_button = Button(down_frame, text="DELETE", font=("arial",12,"bold"),width=12, bg="red", fg="white",pady=4,command=self.delete_medicine)
        delete_data_button.grid(row=2, column=0)

        clear_data_button = Button(down_frame, text="CLEAR", font=("arial",12,"bold"),width=12, bg="darkblue", fg="white",pady=4,command=self.clear_medicine)
        clear_data_button.grid(row=3, column=0)

        ################################################### FRAME DETAILS ##########################################################
        frame_details = Frame(self.root,bd=15,relief=RIDGE,bg="white")
        frame_details.place(x=0,y=580,width=1530,height=210)

        #################### MAIN TABLE AND SCROLLBAR #####################

        # table_frame = Frame(self.root,bd=15,relief=RIDGE,padx=20)
        # table_frame.place(x=0,y=1,width=1460,height=180)

        scrool_x = ttk.Scrollbar(frame_details,orient=HORIZONTAL)
        scrool_x.pack(side=BOTTOM,fill=X)
        scrool_y = ttk.Scrollbar(frame_details,orient=VERTICAL)
        scrool_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table = ttk.Treeview(frame_details,column=("ref","companyname","type"
                                    ,"tablename","lotno","issuedate","expdate","uses","sideeffect","warning","dosage","price","prodectqt")
                                    ,xscrollcommand=scrool_x.set,yscrollcommand=scrool_y.set)
        
        scrool_x.pack(side=BOTTOM,fill=X)
        scrool_y.pack(side=RIGHT,fill=Y)

        scrool_x.config(command=self.pharmacy_table.xview)
        scrool_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"] = "headings"

        self.pharmacy_table.heading("ref",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type of Medicine")
        self.pharmacy_table.heading("tablename",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec & Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("prodectqt",text="Product Qts")

        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("ref",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tablename",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("prodectqt",width=100)
        self.fetch_med_data()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)


    ########################## ADD MEDICINE FUNCTIONALITY DECLARATION #############################

    def add_med(self):
        # Connection with mysql is made
        connection = mysql.connector.connect(host="localhost", username= "root", password="root123",database="mypharmacy")
        my_cursor = connection.cursor()
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(
                                            self.refmed_var.get(),
                                            self.addmed_var.get()
                                ))
        connection.commit()
        self.fetch_med_data()
        self.get_medicine()
        connection.close()
        messagebox.showinfo("Success","Medicine Added")

    def fetch_med_data(self):
        # Connection with mysql is made
        connection = mysql.connector.connect(host="localhost", username= "root", password="root123",database="mypharmacy")
        my_cursor = connection.cursor()
        my_cursor.execute("select * from pharma")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)

                connection.commit()
            connection.close()

    ############################################## GET MEDICINE CURSOR ##########################################################

    def get_medicine(self,event=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        value = content["values"]
        self.refmed_var.set(value[0])
        self.addmed_var.set(value[1])


    def update_med(self):
        if self.refmed_var.get() == "" or self.addmed_var.get() == "":
            messagebox.showerror("Error","All fields are Required")
        else:
            # Connection with mysql is made
            connection = mysql.connector.connect(host="localhost", username= "root", password="root123",database="mypharmacy")
            my_cursor = connection.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s",(
                                                                                self.addmed_var.get(),
                                                                                self.refmed_var.get()
                                                                            ))
            connection.commit()
            self.fetch_med_data()
            connection.close()

            messagebox.showinfo("Success", "Medicine has been Updated")


    def delete_medicine(self):
            # Connection with mysql is made
            connection = mysql.connector.connect(host="localhost", username= "root", password="root123",database="mypharmacy")
            my_cursor = connection.cursor()

            sql = "delete from pharma where Ref=%s"
            val = (self.refmed_var.get(),)
            my_cursor.execute(sql,val)

            connection.commit()
            self.fetch_med_data()
            connection.close()

    
    def clear_medicine(self):
        self.refmed_var.set("")
        self.addmed_var.set("")



    ######################################################### MAIN TABLE ################################################################

    def add_data(self):
        if self.ref_var.get() == "" or self.lot_var.get() == "":
            messagebox.showerror("Error", "All fields are required.")
        else:
            # Connection with mysql is made
            connection = mysql.connector.connect(host="localhost", username= "root", password="root123",database="mypharmacy")
            my_cursor = connection.cursor()

            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                    self.ref_var.get(),
                                                    self.cmpName_var.get(),
                                                    self.typeMed_var.get(),
                                                    self.medName_var.get(),
                                                    self.lot_var.get(),
                                                    self.issuedate_var.get(),
                                                    self.expdate_var.get(),
                                                    self.uses_var.get(),
                                                    self.sideEffect_var.get(),
                                                    self.warning_var.get(),
                                                    self.dosage_var.get(),
                                                    self.price_var.get(),
                                                    self.product_var.get()
                                        ))
                
            connection.commit()
            self.fetch_data()
            connection.close()
            messagebox.showinfo("Success", "Data has been inserted.")
    


    def fetch_data(self):
        # Connection with mysql is made
            connection = mysql.connector.connect(host="localhost", username= "root", password="root123",database="mypharmacy")
            my_cursor = connection.cursor()

            my_cursor.execute("select * from pharmacy")
            row = my_cursor.fetchall()
            if len(row) != 0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                for i in row:
                    self.pharmacy_table.insert("",END,values=i)
                connection.commit()
            connection.close()
    

    def get_cursor(self,event=""):
        cursor_row = self.pharmacy_table.focus()
        content = self.pharmacy_table.item(cursor_row)
        value = content["values"]

        self.ref_var.set(value[0])
        self.cmpName_var.set(value[1])
        self.typeMed_var.set(value[2])
        self.medName_var.set(value[3])
        self.lot_var.set(value[4])
        self.issuedate_var.set(value[5])
        self.expdate_var.set(value[6])
        self.uses_var.set(value[7])
        self.sideEffect_var.set(value[8])
        self.warning_var.set(value[9])
        self.dosage_var.set(value[10])
        self.price_var.set(value[11])
        self.product_var.set(value[12])


    def update(self):
        if self.ref_var.get() == "" or self.lot_var.get() == "":
            messagebox.showerror("Error","All fields are Required")
        else:
            # Connection with mysql is made
            connection = mysql.connector.connect(host="localhost", username= "root", password="root123",database="mypharmacy")
            my_cursor = connection.cursor()
            my_cursor.execute("update pharmacy set CmpName=%s,Type=%s, MedName=%s, LotNo=%s, Issuedate=%s, ExpDate=%s, Uses=%s, Sideeffect=%s, Warning=%s, Dosage=%s, Price=%s, Product=%s where RefNo=%s",(
                                                    
                                                    self.ref_var.get(),
                                                    self.cmpName_var.get(),
                                                    self.typeMed_var.get(),
                                                    self.medName_var.get(),
                                                    self.lot_var.get(),
                                                    self.issuedate_var.get(),
                                                    self.expdate_var.get(),
                                                    self.uses_var.get(),
                                                    self.sideEffect_var.get(),
                                                    self.warning_var.get(),
                                                    self.dosage_var.get(),
                                                    self.price_var.get(),
                                                    self.product_var.get()
                                             ))
            connection.commit()
            self.fetch_data()
            connection.close()

            messagebox.showinfo("Success", "Medicine has been Updated")

    
    def delete(self):
        # Connection with mysql is made
        connection = mysql.connector.connect(host="localhost", username= "root", password="root123",database="mypharmacy")
        my_cursor = connection.cursor()

        sql = "delete from pharmacy where RefNo=%s"
        val = (self.ref_var.get(),)
        my_cursor.execute(sql,val)

        connection.commit()
        self.fetch_data()
        connection.close()

        messagebox.showinfo("Delete", "Information deleted successfully")



    def reset(self):

        # self.ref_var.set(""),
        self.cmpName_var.set(""),
        # self.typeMed_var.set(""),
        # self.medName_var.set(""),
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.warning_var.set(""),
        self.dosage_var.set(r""),
        self.price_var.set(r""),
        self.product_var.set(r""),


    def search_data(self):
        # Connection with mysql is made
        connection = mysql.connector.connect(host="localhost", username= "root", password="root123",database="mypharmacy")
        my_cursor = connection.cursor()
        my_cursor.execute("select * from pharmacy where " +str(self.search_variable.get())+ " LIKE '%" +str(self.search_text.get())+ "%'")

        row = my_cursor.fetchall()
        if len(row) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,values=i)
                connection.commit()
        connection.close()


    
if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()