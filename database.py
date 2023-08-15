import mysql.connector
from tkinter import messagebox

############################### ADD MEDICINE FUNCTIONALITY DECLARATION #############################

def add_med(self):
    # Connection with mysql is made
    connection = mysql.connector.connect(host="localhost", username= "root", password="root123",database="mypharmacy")
    my_cursor = connection.cursor()
    my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(
                                        self.refmed_var.get(),
                                        self.addmed_var.get()
                            ))
    connection.commit()
    connection.close()
    messagebox.showinfo("Success","Medicine Added")


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

        my_cursor.execute("insert into pharmacy(Ref,MedName) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

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
        connection.close()
        messagebox.showinfo("Success", "Data has been inserted.")


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

