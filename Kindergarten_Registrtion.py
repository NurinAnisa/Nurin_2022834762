import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kindergarten_registration"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

def enter_data():
    parent_name =parent_name_entry.get()
    parent_email = email_entry.get()
    parent_phone_number = phone_number_entry.get()
    child_name = child_name_entry.get()
    child_age =child_age_entry.get()
    child_gender = child_gender_var.get()
 
  # Inserting data into a table
    sql = "INSERT INTO user_registration (parent_name, parent_email, parent_phone_number, child_name, child_age,child_gender) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (parent_name, parent_email, parent_phone_number, child_name, child_age, child_gender)
    mycursor.execute(sql, val)
    mydb.commit()


# Your Main window, You need to have the title, geometry (MUST)
root = tk.Tk()
root.title("Kindergarten Registration Form")
root.geometry('500x500')
root.configure(bg="#FDFD96"
)

# Page Title
label = tk.Label(root,text=" Kindergarten Registration", font=("New York",20, "bold"), bg="#79BAEC")
label.grid(ipadx=10, pady=10)


# Parent Information
info_frame = tk.Frame(root)
info_frame.grid()

# Parent Name
parent_name_label=tk.Label(info_frame, text="Parent Name:")
parent_name_label.grid(row=0, column=0)
parent_name_entry = tk.Entry(info_frame)
parent_name_entry.grid(row=0, column=1)

# Parent Email
email_label=tk.Label(info_frame, text="Email:")
email_label.grid(row=1, column=0)
email_entry = tk.Entry(info_frame)
email_entry.grid(row=1, column=1)

#Parent Number Phone
phone_number_label=tk.Label(info_frame, text="Phone Number:")
phone_number_label.grid(row=2, column=0)
phone_number_entry = tk.Entry(info_frame)
phone_number_entry.grid(row=2, column=1)

# Child name
child_name_label = tk.Label(info_frame, text="Child Name:")
child_name_label.grid(row=3, column=0, padx=5, pady=5)
child_name_entry = tk.Entry(info_frame, width=30)
child_name_entry.grid(row=3, column=1, padx=5, pady=5)

# Child age
child_age_label = tk.Label(info_frame, text="Age:")
child_age_label.grid(row=4, column=0, padx=5, pady=5)
child_age_entry = tk.Entry(info_frame, width=30)
child_age_entry.grid(row=4, column=1, padx=5, pady=5)


# Gender Dropdown
child_gender_var = tk.StringVar(root)
child_gender_var.set("Select Your Child gender") 
               # Default value before your selection
child_gender_dropdown = tk.OptionMenu(root, child_gender_var, "Male", "Female")
child_gender_dropdown.grid(pady=10)

# Information by using textbox
Information_text = tk.Text(root, height=3, width=60)
Information_text.grid(pady=20)

# The defined list by using textbox
Information_text.insert(tk.END, "Registration is open to children aged 4 to 6 years only !\n\n")
Information_text.insert(tk.END, "Registration only open from 5 January until 10 Febuary !\n\n")
Information_text.configure(state='disabled')

# Submit Button
submit_button = tk.Button(root, text="Submit Form", command=enter_data)
submit_button.grid(pady=10)

label = tk.Label(root, text="Thank You for Your Registration!", font=("New York",14, "bold"), bg= "#79BAEC")
label.grid(padx=10, pady=10)


root.mainloop()