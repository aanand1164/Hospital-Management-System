from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as ms
import csv
import time

def center_window(window, width, height):
    screen_width=window.winfo_screenwidth()
    screen_height=window.winfo_screenheight()

    x_coordinate=(screen_width-width)//2
    y_coordinate=(screen_height-height)//2

    window.geometry("{}x{}+{}+{}".format(width,height,x_coordinate,y_coordinate))


def clear_fields_add():
    first_name_entry.delete(0, 'end')
    last_name_entry.delete(0, 'end')
    insurance_no_entry.delete(0, 'end')
    phone_no_entry.delete(0, 'end')
    address_entry.delete(0, 'end')


def save_to_csv():    
    last_entry_number = 0
    with open('user_data.csv', 'r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            last_entry_number=int(row['Entry Number'])
        file.close()

    new_entry_number=last_entry_number+1
    first_name=first_name_entry.get()
    last_name=last_name_entry.get()
    insurance_no=insurance_no_entry.get()
    phone_no=phone_no_entry.get()
    address=address_entry.get()

    with open('user_data.csv', 'a', newline='') as file:
        writer=csv.writer(file)
        writer.writerow([new_entry_number, first_name, last_name, insurance_no, phone_no, address])
    file.close()

    add_win.destroy()
    show_record()
    

def addrec_window():
    global first_name_entry, last_name_entry, insurance_no_entry, phone_no_entry, address_entry, add_win
    add_win=tk.Toplevel()
    add_win.title('Add Record')
    add_win.resizable(0,0)
    add_win.grab_set()
    center_window(add_win, 700, 450)

    add_win.grid_columnconfigure(0, weight=1)
    add_win.grid_columnconfigure(1, weight=1)

    add_win.grid_rowconfigure(0, weight=1)
    add_win.grid_rowconfigure(1, weight=1)
    add_win.grid_rowconfigure(2, weight=1)
    add_win.grid_rowconfigure(3, weight=1)
    add_win.grid_rowconfigure(4, weight=1)
    add_win.grid_rowconfigure(5, weight=1)

    tk.Label(add_win, text="First Name:", font=("Times New Roman",17)).grid(row=0, column=0, padx=5, pady=5)
    first_name_entry=tk.Entry(add_win)
    first_name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(add_win, text="Last Name:", font=("Times New Roman",17)).grid(row=1, column=0, padx=5, pady=5)
    last_name_entry=tk.Entry(add_win)
    last_name_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(add_win, text="Insurance No.:", font=("Times New Roman",17)).grid(row=2, column=0, padx=5, pady=5)
    insurance_no_entry=tk.Entry(add_win)
    insurance_no_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(add_win, text="Phone No.:", font=("Times New Roman",17)).grid(row=3, column=0, padx=5, pady=5)
    phone_no_entry=tk.Entry(add_win)
    phone_no_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(add_win, text="Address:", font=("Times New Roman",17)).grid(row=4, column=0, padx=5, pady=5)
    address_entry=tk.Entry(add_win)
    address_entry.grid(row=4, column=1, padx=5, pady=5)

    clear_button=ttk.Button(add_win, text="Clear", command=clear_fields_add)
    clear_button.grid(row=5, column=0, padx=5, pady=10, sticky='e')

    save_button=ttk.Button(add_win, text="Add Record", command=save_to_csv)
    save_button.grid(row=5, column=1, padx=5, pady=10, sticky='w')

    add_win.mainloop()

def srch_record(entry_number):
    for row in recordtable.get_children():
        recordtable.delete(row)

    with open('user_data.csv', 'r') as file:
        reader=csv.reader(file)
        next(reader, None)
        for row in reader:
            if row[0]==entry_number:
                recordtable.insert("", "end", values=row)
                

    search_win.destroy()

def searchrec_window():
    global search_win
    def search_record():
        entry_number = search_entry.get()
        if not entry_number:
            ms.showerror("Error", "Please enter an entry number.")
            return

        srch_record(entry_number)
        
    search_win=tk.Toplevel()
    search_win.title("Search Record")
    search_win.resizable(0,0)
    search_win.grab_set()
    center_window(search_win, 450, 150)

    search_win.grid_columnconfigure(0, weight=1)
    search_win.grid_columnconfigure(1, weight=1)

    search_win.grid_rowconfigure(0, weight=1)
    search_win.grid_rowconfigure(1, weight=1)

    search_label=Label(search_win, text='Enter Entry Number:', font=('calbiri', 12, 'bold'))
    search_label.grid(row=0, column=0, padx=10, pady=10)
    search_entry = Entry(search_win, bd=2, font=('calbiri', 12), width=20)
    search_entry.grid(row=0, column=1, padx=10, pady=10)

    search_button=ttk.Button(search_win, text='SEARCH', width=10, command=search_record)
    search_button.grid(row=1, column=0, columnspan=2)



def del_record(entry_number):
    with open('user_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    new_rows = [row for row in rows if row['Entry Number'] != entry_number]

    with open('user_data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(new_rows)

    delete_entry.delete(0, 'end')
    delete_win.destroy()
    show_record()



def deleterec_window():
    global delete_entry,delete_win
    def delete_record():
        entry_number = delete_entry.get()
        if not entry_number:
            ms.showerror("Error", "Please enter an entry number.",parent=delete_win)
            return

        del_record(entry_number)
        
    delete_win=tk.Toplevel()
    delete_win.title("Delete Record")
    delete_win.resizable(0,0)
    delete_win.grab_set()
    center_window(delete_win, 450, 150)

    delete_win.grid_columnconfigure(0, weight=1)
    delete_win.grid_columnconfigure(1, weight=1)

    delete_win.grid_rowconfigure(0, weight=1)
    delete_win.grid_rowconfigure(1, weight=1)

    delete_label=Label(delete_win, text='Enter Entry Number:', font=('calbiri', 12, 'bold'))
    delete_label.grid(row=0, column=0, padx=10, pady=10)
    delete_entry = Entry(delete_win, bd=2, font=('calbiri', 12), width=20)
    delete_entry.grid(row=0, column=1, padx=10, pady=10)

    delete_button=ttk.Button(delete_win, text='DELETE', width=10, command=delete_record)
    delete_button.grid(row=1, column=0, columnspan=2)


def update_record():
    entry_number=entry_number_entry.get()
    first_name=first_name_entry.get()
    last_name=last_name_entry.get()
    insurance_no=insurance_no_entry.get()
    phone_no=phone_no_entry.get()
    address=address_entry.get()

    new_data=[entry_number, first_name, last_name, insurance_no, phone_no, address]

    with open('user_data.csv', 'r', newline='') as file:
        reader=csv.reader(file)
        data=list(reader)

    for i, row in enumerate(data):
        if row[0]==entry_number:
            for j in range(1, len(row)):
                if j < len(new_data) and new_data[j]:
                    row[j]=new_data[j]
            break
        

    with open('user_data.csv', 'w', newline='') as file:
        writer=csv.writer(file)
        writer.writerows(data)

    update_win.destroy()
    show_record()


def updaterec_window():
    global entry_number_entry, first_name_entry, last_name_entry, insurance_no_entry, phone_no_entry, address_entry, update_win
    update_win=tk.Toplevel()
    update_win.title('Add Record')
    update_win.resizable(0,0)
    update_win.grab_set()
    center_window(update_win, 700, 450)

    update_win.grid_columnconfigure(0, weight=1)
    update_win.grid_columnconfigure(1, weight=1)

    update_win.grid_rowconfigure(0, weight=1)
    update_win.grid_rowconfigure(1, weight=1)
    update_win.grid_rowconfigure(2, weight=1)
    update_win.grid_rowconfigure(3, weight=1)
    update_win.grid_rowconfigure(4, weight=1)
    update_win.grid_rowconfigure(5, weight=1)

    tk.Label(update_win, text="Entry Number:", font=("Times New Roman",17)).grid(row=0, column=0, padx=5, pady=5)
    entry_number_entry=tk.Entry(update_win)
    entry_number_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(update_win, text="First Name:", font=("Times New Roman",17)).grid(row=1, column=0, padx=5, pady=5)
    first_name_entry=tk.Entry(update_win)
    first_name_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(update_win, text="Last Name:", font=("Times New Roman",17)).grid(row=2, column=0, padx=5, pady=5)
    last_name_entry=tk.Entry(update_win)
    last_name_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(update_win, text="Insurance No.:", font=("Times New Roman",17)).grid(row=3, column=0, padx=5, pady=5)
    insurance_no_entry=tk.Entry(update_win)
    insurance_no_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(update_win, text="Phone No.:", font=("Times New Roman",17)).grid(row=4, column=0, padx=5, pady=5)
    phone_no_entry=tk.Entry(update_win)
    phone_no_entry.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(update_win, text="Address:", font=("Times New Roman",17)).grid(row=5, column=0, padx=5, pady=5)
    address_entry=tk.Entry(update_win)
    address_entry.grid(row=5, column=1, padx=5, pady=5)

    clear_button = ttk.Button(update_win, text="Clear", command=lambda: [entry.delete(0, 'end') for entry in (entry_number_entry, first_name_entry, last_name_entry, insurance_no_entry, phone_no_entry, address_entry)])
    clear_button.grid(row=6, column=0, padx=5, pady=10, sticky='e')

    save_button=ttk.Button(update_win, text="Update Record", command=update_record)
    save_button.grid(row=6, column=1, padx=5, pady=10, sticky='w')

    update_win.mainloop()
    
def show_record():
    for row in recordtable.get_children():
        recordtable.delete(row)

    with open('user_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            recordtable.insert("", "end", values=row)

def hide_record():
    for row in recordtable.get_children():
        recordtable.delete(row)

def HMS():
    global recordtable
    
    win=tk.Toplevel()
    win.attributes('-fullscreen', True)
    win.title('Hospital Management System')

    screen_width=win.winfo_screenwidth()
    screen_height=win.winfo_screenheight()

    datelabel=Label(win,font=('sans serif',18,'bold'))
    datelabel.place(x=5,y=8)
    todaysdate=time.strftime('%d/%m/%Y')
    datelabel.config(text="Date: {}".format(todaysdate))

    heading=Label(win,text='HOSPITAL MANAGEMENT SYSTEM',font=('Times New Roman',25,'bold','underline'))
    heading.pack()

    exitbutton=tk.Button(win,text='X',bg="red",width=4,command=win.destroy)
    exitbutton.place(x=screen_width-40,y=3)

    header=Frame(win)
    header.place(x=0,y=60,width=1530,height=150)

    addrec=ttk.Button(header,text='Add Record',width=25,command=addrec_window)
    addrec.grid(row=0, column=0,pady=70,padx=((screen_width//2)-475,0))

    searchrec=ttk.Button(header,text='Search Record',width=25,command=searchrec_window)
    searchrec.grid(row=0,column=1)

    deleterec=ttk.Button(header,text='Delete Record',width=25,command=deleterec_window)
    deleterec.grid(row=0,column=2)

    updaterec=ttk.Button(header,text='Update Record',width=25, command=updaterec_window)
    updaterec.grid(row=0,column=3)

    showrec=ttk.Button(header,text='Show All Records',width=25,command=show_record)
    showrec.grid(row=0,column=4)

    hiderec=ttk.Button(header,text='Hide All Records',width=25,command=hide_record)
    hiderec.grid(row=0,column=5)

    records=Frame(win)
    records.place(x=0,y=210,width=screen_width,height=590)

    recordtable=ttk.Treeview(records,columns=('Entry Number','First Name','Last Name','Insurance No.','Phone No.','Address'))
    recordtable.pack(fill=BOTH,expand=1)

    recordtable.heading('Entry Number',text='ENTRY NUMBER')
    recordtable.heading('First Name',text='FIRST NAME')
    recordtable.heading('Last Name',text='LAST NAME')
    recordtable.heading('Insurance No.',text='INSURANCE NO.')
    recordtable.heading('Phone No.',text='PHONE NO.')
    recordtable.heading('Address',text='ADDRESS')
    
    with open('user_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            recordtable.insert("", "end", values=row)

    recordtable.config(show='headings')
    win.mainloop()

def check_credentials(username,password):
    with open('credentials.csv', 'r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row['Username']==username:
                if row['Password']==password:
                    return True
                else:
                    return False
        return False

def login():
    username=username_entry.get()
    password=password_entry.get()

    if username.strip() == "" or password.strip() == "":
        ms.showerror("Error", "Username and password cannot be empty.")
    else:
        check=check_credentials(username,password)
        if check==False:
            ms.showerror("Error","Check your credentials and try again!")
        else:
            ms.showinfo("Login Successful", "Welcome, {}!".format(username))
            HMS()
            
def root():
    global username_entry, password_entry
    
    root=tk.Tk()
    root.attributes('-fullscreen', True)

    canvas=tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack()
    background_image=tk.PhotoImage(file="bg.png")
    canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()

    entry_x=screen_width//2
    entry_y=screen_height//2

    root.geometry("{0}x{1}".format(screen_width, screen_height))
    root.title('Login')

    exitbutton=tk.Button(root,text='X',bg="red",width=4,command=root.destroy)
    exitbutton.place(x=screen_width-40,y=3)

    head_label=Label(root,text="Hospital Management System", font=("Arial",17))
    head_label.place(x=entry_x-140,y=entry_y-130)

    canvas.create_text(entry_x-150, entry_y-60, text="Enter Username:", fill="black", font=("Arial", 13), anchor="w")
    username_entry=Entry()
    username_entry.place(x=entry_x+50, y=entry_y-70)


    canvas.create_text(entry_x-150, entry_y, text="Enter Password:", fill="black", font=("Arial", 13), anchor="w")    
    password_entry=Entry(root, show="*")
    password_entry.place(x=entry_x+50, y=entry_y-10)
     
    btn=Button(root,text="Login",width=15,font=("italics",10),bg="white",command=login)
    btn.place(x=entry_x, y=entry_y+60, anchor='center')

    root.mainloop()

root()


