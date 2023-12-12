import tkinter as tk
from tkinter import Button, StringVar, Widget, ttk
from tkinter import messagebox
from tkinter.constants import END

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("KATARSIS CLUB MEMEBERSHIP REGISTRATION SYSTEM")

#Background Colour
win.config(bg="black")

#Adding some style
style = ttk.Style()

#Pick a theme
style.theme_use("default")

style.configure("Treeview", 
    background="#FFC0CB", 
    foreground="black", 
    rowheight=25, 
    fieldbackground="white"
)

#Change selected colour
style.map(
    "Treeview",
    background=[("selected","#FF7F24")]
)

#Top Menu

title_label = tk.Label(
    win, 
    text="KATARSIS CLUB MEMEBERSHIP REGISTRATION SYSTEM", 
    font=("britannic bold", 20, "bold"), 
    padx=15, 
    pady=15, 
    border=0, 
    relief=tk.GROOVE, 
    bg="#4B0082", 
    foreground="white"
)
title_label.pack(side=tk.TOP, fill=tk.X)

#Left Menu

detail_frame = tk.LabelFrame(
    win, text="STUDENT RECORDS", 
    font=("Berlin Sans FB", 19), 
    bg="#68228B", 
    foreground="white", 
    relief=tk.GROOVE
)
detail_frame.place(x=40, y=90, width=420, height=570)

#Data Frame

data_frame = tk.Frame(
    win, 
    bg="teal", 
    relief=tk.GROOVE
)
data_frame.place(x=490, y=98, width=1000, height=565)

#Label with Entry

#ID
id_lab = tk.Label(
    detail_frame, 
    text=" ID:", 
    font=("Segoe UI Black",14), 
    bg="#FFB6C1", 
    foreground="black"
)
id_lab.place(x=20, y=15)

#entry 1
id_ent = tk.Entry(
    detail_frame, 
    bd=1,     
    font=("Segoe UI Black", 14), 
    bg="#FFB6C1", 
    foreground="black",
)
id_ent.place(x=110, y=17, width=290, height=30)

#Name
name_lab = tk.Label(
    detail_frame,
    text="Name:", 
    font=("Segoe UI Black",14), 
    bg="#FFB6C1", 
    foreground="black"
)
name_lab.place(x=20, y=65)

#entry 2
name_ent = tk.Entry( 
    detail_frame, 
    bd=1, 
    font=("Segoe UI Black", 14),
    bg="#FFB6C1",
    foreground="black",
)
name_ent.place(x=110, y=65, width=290, height=30)

#Gender
gen_lab = tk.Label(
    detail_frame, 
    text="Gender:", 
    font=("Segoe UI Black",14), 
    bg="#FFA07A", 
    foreground="black"
)
gen_lab.place(x=20, y=113)

#entry 3
gen_ent = ttk.Combobox(
    detail_frame, 
    font=("Segoe UI Black,",14),
)
gen_ent["values"] = ("Male", "Female", "others")
gen_ent.place(x=110, y=113, width=290, height=30)

#Age
age_lab = tk.Label(
    detail_frame, 
    text="Age:", 
    font=("Segoe UI Black",14), 
    bg="#FFB6C1", 
    foreground="black"
)
age_lab.place(x=20, y=161)

#entry 4
age_ent = tk.Entry(
    detail_frame, 
    bd=1, 
    font=("Segoe UI Black", 14), 
    bg="#FFB6C1", 
    foreground="black",
)
age_ent.place(x=110, y=161, width=290, height=30)

#Email
email_lab = tk.Label(
    detail_frame, 
    text="Email:", 
    font=("Segoe UI Black", 14), 
    bg="#FFB6C1", 
    foreground="black",
)
email_lab.place(x=20, y=209)

#entry 5
email_ent = tk.Entry(
    detail_frame, 
    bd=1, 
    font=("Segoe UI Black",14), 
    bg="#FFB6C1", 
    foreground="black",
)
email_ent.place(x=110, y=209, width=290, height=30)

#Faculty
faculty_lab = tk.Label(
    detail_frame, 
    text="Faculty:", 
    font=("Segoe UI Black", 14), 
    bg="#FFA07A", 
    foreground="black",
)
faculty_lab.place(x=20, y=257)

faculty_ent = ttk.Combobox(
    detail_frame, 
    font=("Segoe UI Black,",14),
)
faculty_ent["values"] = ("AC110", "AC220", "AM11O", "AM228", "IM110", "IM144", "AD111", "AD114", "AD244", "CS110", "BA111", "BA118", "BA119", "BA240", "BA242", "BA243", "BA244", "BA246", "BA249", "BA250")
faculty_ent.place(x=110, y=257, width=290, height=30)

#Semester
sem_lab = tk.Label(
    detail_frame, 
    text="Semester:", 
    font=("Segoe UI Black", 12), 
    bg="#FFA07A", 
    foreground="black",
)
sem_lab.place(x=20, y=305)

#entry 7
sem_ent = ttk.Combobox(
    detail_frame, 
    font=("Segoe UI Black,",14),
)
sem_ent["values"] = ("First Semester", "Second Semester", "Third Semester", "Fourth Semester", "Fifth Semester")
sem_ent.place(x=110, y=305, width=290, height=30)

#Phone Number
phone_lab = tk.Label(
    detail_frame, 
    text="Phone No:", 
    font=("Segoe UI Black", 12), 
    bg="#FFB6C1", 
    foreground="black"
)
phone_lab.place(x=20, y=353)

#entry 8
phone_ent = tk.Entry(
    detail_frame, 
    bd=1, 
    font=("Segoe UI Black",14), 
    bg="#FFB6C1", 
    foreground="black",
)
phone_ent.place(x=110, y=353, width=290, height=30)


#Database Frame

main_frame = tk.Frame(
    data_frame, 
    bg="teal", 
    bd=2, 
    relief=tk.GROOVE
)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

#Treeview database

student_table = ttk.Treeview(main_frame, column=(
    "ID", "Name", "Gender", "Age", "Email", "Faculty", "Semester", "Phone No"
), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set) 

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_table.heading("ID", text="ID")
student_table.heading("Name", text="Name")
student_table.heading("Gender", text="Gender")
student_table.heading("Age", text="Age")
student_table.heading("Email", text="Email")
student_table.heading("Faculty", text="Faculty")
student_table.heading("Semester", text="Semester")
student_table.heading("Phone No", text="Phone No")

student_table["show"] = "headings"

student_table.column("ID", width=100)
student_table.column("Name", width=100)
student_table.column("Gender", width=100)
student_table.column("Age", width=100)
student_table.column("Email", width=100)
student_table.column("Faculty", width=100)
student_table.column("Semester", width=100)
student_table.column("Phone No", width=100)

student_table.pack(fill=tk.BOTH, expand=True)

#Default data

data=[
    ["2022131999", "Lando", "Male", "24", "norris@gmail.com", "IM144", "Third Semester", "012-4543223"],
    ["2022021975", "Pedro", "Male", "28", "pascal@gmail.com", "CS110", "Fifth Semester", "014-5435433"],
    ["2022876758", "Ayu", "Female", "20", "bestie@gmail.com", "AC110", "Second Semester", "019-4533922"],
    ["2022411538", "Iman", "Male", "22", "udang@gmail.com", "BA242", "Third Semester", "016-4543222"],
    ["2022627328", "Zee", "Male", "24", "boy@gmail.com", "AD114", "Third Semester", "014-9975004"],
    ["2022827148", "Kamillah", "Female", "25", "gurl@gmail.com", "AC220", "Fourth Semester", "012-9584944"],
    ["2022895228", "Anis", "Female", "26", "bebeh@gmail.com", "IM110", "Fifth Semester", "018-8485894"],
    ["2022617084", "Nini", "Female", "25", "babe@gmail.com", "AM228", "Fourth Semester", "012-1145643"],
]

# Create stripped row tags
student_table.tag_configure("oddrow", background="#FFEFDB")
student_table.tag_configure("evenrow", background="#00AEAE")

global count
count = 0
for record in data:
    if count % 2 == 0:
        student_table.insert(parent="", index="end", iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]))
    else:
        student_table.insert(parent="", index="end", iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]))
    count += 1


#Functions

# Add Function
def add_record():
    student_table.tag_configure("oddrow", background="white")
    student_table.tag_configure("evenrow", background="#00AEAE")

    global count
    try:
        # Validate and convert certain fields to float
        age = float(age_ent.get())
        phone = float(phone_ent.get())
        
        # Additional validations if needed

        if count % 2 == 0:
            student_table.insert(parent="", index="end", iid=count, text="", values=(
                id_ent.get(),
                name_ent.get(),
                gen_ent.get(),
                age_ent.get(),
                email_ent.get(),
                faculty_ent.get(),
                sem_ent.get(),
                phone_ent.get()
            ),
                tags=("evenrow")
            )
        else:
            student_table.insert(parent="", index="end", iid=count, text="", values=(
                id_ent.get(),
                name_ent.get(),
                gen_ent.get(),
                age_ent.get(),
                email_ent.get(),
                faculty_ent.get(),
                sem_ent.get(),
                phone_ent.get()
            ),
                tags=("oddrow")
            )
        count += 1

    except ValueError:
        messagebox.showerror("Error", "Invalid input for numeric fields. Please enter valid numbers.")

#Delete All Function
def delete_all():
    for record in student_table.get_children():
        student_table.delete(record)

#Delete One Function
def delete_one():
    x = student_table.selection()[0]
    student_table.delete(x)

#Select Record
def select_record():

    id_ent.delete(0, END)
    name_ent.delete(0, END)
    gen_ent.delete(0,END)
    age_ent.delete(0, END), 
    email_ent.delete(0, END), 
    faculty_ent.delete(0, END),
    sem_ent.delete(0, END),
    phone_ent.delete(0, END),
 
    selected = student_table.focus()
    values = student_table.item(selected, "values")

    id_ent.insert(0, values[0])
    name_ent.insert(0, values[1])
    gen_ent.insert(0, values[2])
    age_ent.insert(0, values[3])
    email_ent.insert(0, values[4])
    faculty_ent.insert(0, values[5])
    sem_ent.insert(0, values[6])
    phone_ent.insert(0, values[7])

#Update Button
def update_record():
    selected = student_table.focus()
    student_table.item(selected, text="", values=(id_ent.get(), name_ent.get(), gen_ent.get(), age_ent.get(), email_ent.get(), faculty_ent.get(), sem_ent.get(), phone_ent.get()))

    id_ent.delete(0, END),
    name_ent.delete(0, END),
    gen_ent.delete(0, END),
    age_ent.delete(0, END),
    email_ent.delete(0, END),
    faculty_ent.delete(0, END),
    sem_ent.delete(0, END),
    phone_ent.delete(0, END)


#Clear boxes
    id_ent.delete(0, END),
    name_ent.delete(0, END), 
    gen_ent.delete(0, END),
    age_ent.delete(0, END),
    email_ent.delete(0, END),
    faculty_ent.delete(0, END),
    sem_ent.delete(0, END),
    phone_ent.delete(0, END)


#Buttons

btn_frame = tk.Frame(
    detail_frame, 
    bg="#698B22", 
    bd=0,  
    relief= tk.GROOVE
)
btn_frame.place(x=40, y=400, width=300, height=130)

#Add Button
add_btn = tk.Button(
    btn_frame, 
    bg="#B3EE3A", 
    foreground="black", 
    text="ADD", 
    bd=2, 
    font=("Franklin Gothic Heavy", 12), width=15, 
    command=add_record
)
add_btn.grid(row=0, column=0, padx=2, pady=2)


#Update Button
update_btn = tk.Button(
    btn_frame, 
    bg="#B3EE3A", 
    foreground="black", 
    text="UPDATE", 
    bd=2, 
    font=("Franklin Gothic Heavy", 12), width=15, 
    command=select_record
)
update_btn.grid(row=0, column=1, padx=2, pady=2)
    
#Save Button
cal_btn = tk.Button(
    btn_frame, 
    bg="#96CDCD", 
    foreground="BLACK", 
    text="SAVE", 
    bd=2, 
    font=("Franklin Gothic Heavy", 12), width=15, 
    command=update_record
)
cal_btn.grid(row=1, column=0, padx=2, pady=2)

#Save Button
save_btn = tk.Button(
    btn_frame, 
    bg="#EE2C2C", 
    foreground="black", 
    text="CLEAR ALL", 
    bd=2, 
    font=("Franklin Gothic Heavy", 12), width=15, 
    command=delete_all
)
save_btn.grid(row=2, column=0, padx=2, pady=2)

#Delete Button
delete_btn = tk.Button(
    btn_frame, 
    bg="#EE2C2C", 
    foreground="black", 
    text="DELETE", 
    bd=2, 
    font=("Franklin Gothic Heavy", 12), width=15, 
    command=delete_one
)
delete_btn.grid(row=2, column=1, padx=2, pady=2)




win.mainloop()