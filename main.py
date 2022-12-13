import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import PhotoImage
import project as pro
import sqlite3
import re
import random
import string
# from tkinter import*
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst


color={"neru":"#252726","orange":"#FF8700","darkorange":"#FE6101"}

root=tk.Tk()
root.geometry("1366x728")
root.title("Bill CRM")
root.resizable(0, 0)

btnState=False
navIcon=PhotoImage(file="images/navbar1.png")
closeIcon=PhotoImage(file="images/cross1.png")

def switch():
    global btnState
    if btnState is True:
        for x in range(3001):
            navRoot.place(x=-x,y=0)
            topFrame.update()

        homeLable.config(bg="orange")
        topFrame.config(bg="orange")

        btnState=False
    else:
        homeLable.config(bg="green")

        for x in range(-300,0):
            navRoot.place(x=x,y=0)
            topFrame.update()
            btnState=True


label1 = Label(root)
label1.place(x=0,y=0)
img = PhotoImage(file="real-mart-master/images/main.png")
label1.configure(image=img)
            
topFrame=tk.Frame(root,bg="orange")
topFrame.pack(side="top",fill=tk.X)
homeLable=tk.Label(topFrame,text="Neetpal Singh Projects",font=("Times",14),bg="orange",fg="gray17",height=2,padx=20)
homeLable.pack(side="right")

navbarBtn=tk.Button(topFrame,image=navIcon,bg="orange",activebackground="orange",bd=0,padx=20,command=switch)
navbarBtn.place(x=10,y=10)

navRoot=tk.Frame(root,bg="gray10",height=1000,width=250)
navRoot.place(x=-300,y=0)
tk.Label(navRoot,font="Times 14",bg="orange",fg="black",height=2,width=300,padx=20).place(x=0,y=0)

pic=tk.PhotoImage(file="images/neet.png")
tk.Label(navRoot,image=pic,bg="gray10").place(x=30,y=480)
tk.Label(navRoot,text="Developer: Neetpal Singh",bg="gray10",fg="orange",font=("Times",10)).place(x=20,y=640)
tk.Label(navRoot,text="E mail   : neetpalsingh750@gmail.com",bg="gray10",fg="orange",font=("Times",10)).place(x=20,y=655)
tk.Label(navRoot,text="contact  : +917505687812",bg="gray10",fg="orange",font=("Times",10)).place(x=20,y=670)

y=80
options=["Profile","About","Notepad","Calculator","Currecy Exchanger","Country Info"]
cmd=[None,None,None,None,None,None]
for i in range(6):
    tk.Button(navRoot,text=options[i],command=cmd[i],font="Times 14",bg="gray10",fg="orange",activebackground="gray17",activeforeground="green",bd=0).place(x=25,y=y)
    y+=40

closeBtn=tk.Button(navRoot,image=closeIcon,bg="orange",activebackground="orange",bd=0,command=switch)
closeBtn.place(x=220,y=10)



def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
    if sure == True:
        root.destroy()
        
root.protocol("WM_DELETE_WINDOW", Exit)



####################
#####################
############ Employee method ================================================================================================================
def emp():
    # root = tk.Tk()
    second=tk.Toplevel(root)
    second.geometry("1266x668")
    second.title("Retail Manager")


    user = tk.StringVar()
    passwd = tk.StringVar()
    fname = tk.StringVar()
    lname = tk.StringVar()
    new_user = tk.StringVar()
    new_passwd = tk.StringVar()


    cust_name = tk.StringVar()
    cust_num = tk.StringVar()
    cust_new_bill = tk.StringVar()
    cust_search_bill = tk.StringVar()
    bill_date = tk.StringVar()


    with sqlite3.connect("real-mart-master/Database/store.db") as db:
        cur = db.cursor()

        
    def random_bill_number(stringLength):
        lettersAndDigits = string.ascii_letters.upper() + string.digits
        strr=''.join(random.choice(lettersAndDigits) for i in range(stringLength-2))
        return ('BB'+strr)


    def valid_phone(phn):
        if re.match(r"[789]\d{9}$", phn):
            return True
        return False

    def login(Event=None):
        global username
        username = user.get()
        password = passwd.get()

        with sqlite3.connect("real-mart-master/Database/store.db") as db:
            cur = db.cursor()
        find_user = "SELECT * FROM employee WHERE emp_id = ? and password = ?"
        cur.execute(find_user, [username, password])
        results = cur.fetchall()
        if results:
            messagebox.showinfo("Login Page", "The login is successful")
            page1.entry1.delete(0, tk.END)
            page1.entry2.delete(0, tk.END)
            second.withdraw()
            global biller
            global page2
            biller = tk.Toplevel()
            page2 = bill_window(biller)
            page2.time()
            biller.protocol("WM_DELETE_WINDOW", exitt)
            biller.mainloop()

        else:
            messagebox.showerror("Error", "Incorrect username or password.")
            page1.entry2.delete(0, tk.END)



    def logout():
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=biller)
        if sure == True:
            biller.destroy()
            second.deiconify()
            page1.entry1.delete(0, tk.END)
            page1.entry2.delete(0, tk.END)

    class login_page:
        def __init__(self, top=None):
            top.geometry("1366x768")
            top.resizable(0, 0)
            top.title("Retail Manager")

            self.label1 = tk.Label(second)
            self.label1.place(relx=0, rely=0, width=1366, height=768)
            self.img = tk.PhotoImage(file="real-mart-master/images/employee_login.png")
            self.label1.configure(image=self.img)

            self.btn = Button(second)
            self.btn.place(x=50, y=70, width=100, height=25)
            self.btn.configure(relief="flat")
            self.btn.configure(overrelief="flat")
            self.btn.configure(activebackground="#D2463E")
            self.btn.configure(cursor="hand2")
            self.btn.configure(foreground="#ffffff")
            self.btn.configure(background="#D2463E")
            self.btn.configure(font="-family {Poppins SemiBold} -size 10")
            self.btn.configure(borderwidth="0")
            self.btn.configure(text="""Back""")
            self.btn.configure(command=login)

            self.entry1 = tk.Entry(second)
            self.entry1.place(relx=0.373, rely=0.273, width=374, height=24)
            self.entry1.configure(font="-family {Poppins} -size 10")
            self.entry1.configure(relief="flat")
            self.entry1.configure(textvariable=user)

            self.entry2 = tk.Entry(second)
            self.entry2.place(relx=0.373, rely=0.384, width=374, height=24)
            self.entry2.configure(font="-family {Poppins} -size 10")
            self.entry2.configure(relief="flat")
            self.entry2.configure(show="*")
            self.entry2.configure(textvariable=passwd)

            self.button1 = tk.Button(second)
            self.button1.place(relx=0.366, rely=0.685, width=356, height=43)
            self.button1.configure(relief="flat")
            self.button1.configure(overrelief="flat")
            self.button1.configure(activebackground="#D2463E")
            self.button1.configure(cursor="hand2")
            self.button1.configure(foreground="#ffffff")
            self.button1.configure(background="#D2463E")
            self.button1.configure(font="-family {Poppins SemiBold} -size 20")
            self.button1.configure(borderwidth="0")
            self.button1.configure(text="""LOGIN""")
            self.button1.configure(command=login)


    class Item:
        def __init__(self, name, price, qty):
            self.product_name = name
            self.price = price
            self.qty = qty

    class Cart:
        def __init__(self):
            self.items = []
            self.dictionary = {}

        def add_item(self, item):
            self.items.append(item)

        def remove_item(self):
            self.items.pop()

        def remove_items(self):
            self.items.clear()

        def total(self):
            total = 0.0
            for i in self.items:
                total += i.price * i.qty
            return total

        def isEmpty(self):
            if len(self.items)==0:
                return True
            
        def allCart(self):
            for i in self.items:
                if (i.product_name in self.dictionary):
                    self.dictionary[i.product_name] += i.qty
                else:
                    self.dictionary.update({i.product_name:i.qty})
        

    def exitt():
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=biller)
        if sure == True:
            biller.destroy()
            second.destroy()


    class bill_window:
        def __init__(self, top=None):
            top.geometry("1366x768")
            top.resizable(0, 0)
            top.title("Billing System")

            self.label = tk.Label(biller)
            self.label.place(relx=0, rely=0, width=1366, height=768)
            self.img = tk.PhotoImage(file="real-mart-master/images/bill_window.png")
            self.label.configure(image=self.img)

            self.message = tk.Label(biller)
            self.message.place(relx=0.038, rely=0.055, width=136, height=30)
            self.message.configure(font="-family {Poppins} -size 10")
            self.message.configure(foreground="#000000")
            self.message.configure(background="#ffffff")
            self.message.configure(text=username)
            self.message.configure(anchor="w")

            self.clock = tk.Label(biller)
            self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
            self.clock.configure(font="-family {Poppins Light} -size 12")
            self.clock.configure(foreground="#000000")
            self.clock.configure(background="#ffffff")

            self.entry1 = tk.Entry(biller)
            self.entry1.place(relx=0.509, rely=0.23, width=240, height=24)
            self.entry1.configure(font="-family {Poppins} -size 12")
            self.entry1.configure(relief="flat")
            self.entry1.configure(textvariable=cust_name)

            self.entry2 = tk.Entry(biller)
            self.entry2.place(relx=0.791, rely=0.23, width=240, height=24)
            self.entry2.configure(font="-family {Poppins} -size 12")
            self.entry2.configure(relief="flat")
            self.entry2.configure(textvariable=cust_num)

            self.entry3 = tk.Entry(biller)
            self.entry3.place(relx=0.102, rely=0.23, width=240, height=24)
            self.entry3.configure(font="-family {Poppins} -size 12")
            self.entry3.configure(relief="flat")
            self.entry3.configure(textvariable=cust_search_bill)

            self.button1 = tk.Button(biller)
            self.button1.place(relx=0.031, rely=0.104, width=76, height=23)
            self.button1.configure(relief="flat")
            self.button1.configure(overrelief="flat")
            self.button1.configure(activebackground="#CF1E14")
            self.button1.configure(cursor="hand2")
            self.button1.configure(foreground="#ffffff")
            self.button1.configure(background="#CF1E14")
            self.button1.configure(font="-family {Poppins SemiBold} -size 12")
            self.button1.configure(borderwidth="0")
            self.button1.configure(text="""Logout""")
            self.button1.configure(command=logout)

            self.button2 = tk.Button(biller)
            self.button2.place(relx=0.315, rely=0.234, width=76, height=23)
            self.button2.configure(relief="flat")
            self.button2.configure(overrelief="flat")
            self.button2.configure(activebackground="#CF1E14")
            self.button2.configure(cursor="hand2")
            self.button2.configure(foreground="#ffffff")
            self.button2.configure(background="#CF1E14")
            self.button2.configure(font="-family {Poppins SemiBold} -size 12")
            self.button2.configure(borderwidth="0")
            self.button2.configure(text="""Search""")
            self.button2.configure(command=self.search_bill)

            self.button3 = tk.Button(biller)
            self.button3.place(relx=0.048, rely=0.885, width=86, height=25)
            self.button3.configure(relief="flat")
            self.button3.configure(overrelief="flat")
            self.button3.configure(activebackground="#CF1E14")
            self.button3.configure(cursor="hand2")
            self.button3.configure(foreground="#ffffff")
            self.button3.configure(background="#CF1E14")
            self.button3.configure(font="-family {Poppins SemiBold} -size 10")
            self.button3.configure(borderwidth="0")
            self.button3.configure(text="""Total""")
            self.button3.configure(command=self.total_bill)

            self.button4 = tk.Button(biller)
            self.button4.place(relx=0.141, rely=0.885, width=84, height=25)
            self.button4.configure(relief="flat")
            self.button4.configure(overrelief="flat")
            self.button4.configure(activebackground="#CF1E14")
            self.button4.configure(cursor="hand2")
            self.button4.configure(foreground="#ffffff")
            self.button4.configure(background="#CF1E14")
            self.button4.configure(font="-family {Poppins SemiBold} -size 10")
            self.button4.configure(borderwidth="0")
            self.button4.configure(text="""Generate""")
            self.button4.configure(command=self.gen_bill)

            self.button5 = tk.Button(biller)
            self.button5.place(relx=0.230, rely=0.885, width=86, height=25)
            self.button5.configure(relief="flat")
            self.button5.configure(overrelief="flat")
            self.button5.configure(activebackground="#CF1E14")
            self.button5.configure(cursor="hand2")
            self.button5.configure(foreground="#ffffff")
            self.button5.configure(background="#CF1E14")
            self.button5.configure(font="-family {Poppins SemiBold} -size 10")
            self.button5.configure(borderwidth="0")
            self.button5.configure(text="""Clear""")
            self.button5.configure(command=self.clear_bill)

            self.button6 = tk.Button(biller)
            self.button6.place(relx=0.322, rely=0.885, width=86, height=25)
            self.button6.configure(relief="flat")
            self.button6.configure(overrelief="flat")
            self.button6.configure(activebackground="#CF1E14")
            self.button6.configure(cursor="hand2")
            self.button6.configure(foreground="#ffffff")
            self.button6.configure(background="#CF1E14")
            self.button6.configure(font="-family {Poppins SemiBold} -size 10")
            self.button6.configure(borderwidth="0")
            self.button6.configure(text="""Exit""")
            self.button6.configure(command=exitt)

            self.button7 = tk.Button(biller)
            self.button7.place(relx=0.098, rely=0.734, width=86, height=26)
            self.button7.configure(relief="flat")
            self.button7.configure(overrelief="flat")
            self.button7.configure(activebackground="#CF1E14")
            self.button7.configure(cursor="hand2")
            self.button7.configure(foreground="#ffffff")
            self.button7.configure(background="#CF1E14")
            self.button7.configure(font="-family {Poppins SemiBold} -size 10")
            self.button7.configure(borderwidth="0")
            self.button7.configure(text="""Add To Cart""")
            self.button7.configure(command=self.add_to_cart)

            self.button8 = tk.Button(biller)
            self.button8.place(relx=0.274, rely=0.734, width=84, height=26)
            self.button8.configure(relief="flat")
            self.button8.configure(overrelief="flat")
            self.button8.configure(activebackground="#CF1E14")
            self.button8.configure(cursor="hand2")
            self.button8.configure(foreground="#ffffff")
            self.button8.configure(background="#CF1E14")
            self.button8.configure(font="-family {Poppins SemiBold} -size 10")
            self.button8.configure(borderwidth="0")
            self.button8.configure(text="""Clear""")
            self.button8.configure(command=self.clear_selection)

            self.button9 = tk.Button(biller)
            self.button9.place(relx=0.194, rely=0.734, width=68, height=26)
            self.button9.configure(relief="flat")
            self.button9.configure(overrelief="flat")
            self.button9.configure(activebackground="#CF1E14")
            self.button9.configure(cursor="hand2")
            self.button9.configure(foreground="#ffffff")
            self.button9.configure(background="#CF1E14")
            self.button9.configure(font="-family {Poppins SemiBold} -size 10")
            self.button9.configure(borderwidth="0")
            self.button9.configure(text="""Remove""")
            self.button9.configure(command=self.remove_product)

            text_font = ("Poppins", "8")
            self.combo1 = ttk.Combobox(biller)
            self.combo1.place(relx=0.035, rely=0.408, width=477, height=26)

            find_category = "SELECT product_cat FROM raw_inventory"
            cur.execute(find_category)
            result1 = cur.fetchall()
            cat = []
            for i in range(len(result1)):
                if(result1[i][0] not in cat):
                    cat.append(result1[i][0])


            self.combo1.configure(values=cat)
            self.combo1.configure(state="readonly")
            self.combo1.configure(font="-family {Poppins} -size 8")
            self.combo1.option_add("*TCombobox*Listbox.font", text_font)
            self.combo1.option_add("*TCombobox*Listbox.selectBackground", "#D2463E")


            self.combo2 = ttk.Combobox(biller)
            self.combo2.place(relx=0.035, rely=0.479, width=477, height=26)
            self.combo2.configure(font="-family {Poppins} -size 8")
            self.combo2.option_add("*TCombobox*Listbox.font", text_font) 
            self.combo2.configure(state="disabled")


            self.combo3 = ttk.Combobox(biller)
            self.combo3.place(relx=0.035, rely=0.551, width=477, height=26)
            self.combo3.configure(state="disabled")
            self.combo3.configure(font="-family {Poppins} -size 8")
            self.combo3.option_add("*TCombobox*Listbox.font", text_font)

            self.entry4 = ttk.Entry(biller)
            self.entry4.place(relx=0.035, rely=0.629, width=477, height=26)
            self.entry4.configure(font="-family {Poppins} -size 8")
            self.entry4.configure(foreground="#000000")
            self.entry4.configure(state="disabled")

            self.Scrolledtext1 = tkst.ScrolledText(top)
            self.Scrolledtext1.place(relx=0.439, rely=0.586, width=695, height=275)
            self.Scrolledtext1.configure(borderwidth=0)
            self.Scrolledtext1.configure(font="-family {Podkova} -size 8")
            self.Scrolledtext1.configure(state="disabled")

            self.combo1.bind("<<ComboboxSelected>>", self.get_category)
            
        def get_category(self, Event):
            self.combo2.configure(state="readonly")
            self.combo2.set('')
            self.combo3.set('')
            find_subcat = "SELECT product_subcat FROM raw_inventory WHERE product_cat = ?"
            cur.execute(find_subcat, [self.combo1.get()])
            result2 = cur.fetchall()
            subcat = []
            for j in range(len(result2)):
                if(result2[j][0] not in subcat):
                    subcat.append(result2[j][0])
            
            self.combo2.configure(values=subcat)
            self.combo2.bind("<<ComboboxSelected>>", self.get_subcat)
            self.combo3.configure(state="disabled")

        def get_subcat(self, Event):
            self.combo3.configure(state="readonly")
            self.combo3.set('')
            find_product = "SELECT product_name FROM raw_inventory WHERE product_cat = ? and product_subcat = ?"
            cur.execute(find_product, [self.combo1.get(), self.combo2.get()])
            result3 = cur.fetchall()
            pro = []
            for k in range(len(result3)):
                pro.append(result3[k][0])

            self.combo3.configure(values=pro)
            self.combo3.bind("<<ComboboxSelected>>", self.show_qty)
            self.entry4.configure(state="disabled")

        def show_qty(self, Event):
            self.entry4.configure(state="normal")
            self.qty_label = tk.Label(biller)
            self.qty_label.place(relx=0.033, rely=0.664, width=82, height=26)
            self.qty_label.configure(font="-family {Poppins} -size 8")
            self.qty_label.configure(anchor="w")

            product_name = self.combo3.get()
            find_qty = "SELECT stock FROM raw_inventory WHERE product_name = ?"
            cur.execute(find_qty, [product_name])
            results = cur.fetchone()
            self.qty_label.configure(text="In Stock: {}".format(results[0]))
            self.qty_label.configure(background="#ffffff")
            self.qty_label.configure(foreground="#333333")
        
        cart = Cart()
        def add_to_cart(self):
            self.Scrolledtext1.configure(state="normal")
            strr = self.Scrolledtext1.get('1.0', tk.END)
            if strr.find('Total')==-1:
                product_name = self.combo3.get()
                if(product_name!=""):
                    product_qty = self.entry4.get()
                    find_mrp = "SELECT mrp, stock FROM raw_inventory WHERE product_name = ?"
                    cur.execute(find_mrp, [product_name])
                    results = cur.fetchall()
                    stock = results[0][1]
                    mrp = results[0][0]
                    if product_qty.isdigit()==True:
                        if (stock-int(product_qty))>=0:
                            sp = mrp*int(product_qty)
                            item = Item(product_name, mrp, int(product_qty))
                            self.cart.add_item(item)
                            self.Scrolledtext1.configure(state="normal")
                            bill_text = "{}\t\t\t\t\t\t{}\t\t\t\t\t   {}\n".format(product_name, product_qty, sp)
                            self.Scrolledtext1.insert('insert', bill_text)
                            self.Scrolledtext1.configure(state="disabled")
                        else:
                            messagebox.showerror("Oops!", "Out of stock. Check quantity.", parent=biller)
                    else:
                        messagebox.showerror("Oops!", "Invalid quantity.", parent=biller)
                else:
                    messagebox.showerror("Oops!", "Choose a product.", parent=biller)
            else:
                self.Scrolledtext1.delete('1.0', tk.END)
                new_li = []
                li = strr.split("\n")
                for i in range(len(li)):
                    if len(li[i])!=0:
                        if li[i].find('Total')==-1:
                            new_li.append(li[i])
                        else:
                            break
                for j in range(len(new_li)-1):
                    self.Scrolledtext1.insert('insert', new_li[j])
                    self.Scrolledtext1.insert('insert','\n')
                product_name = self.combo3.get()
                if(product_name!=""):
                    product_qty = self.entry4.get()
                    find_mrp = "SELECT mrp, stock, product_id FROM raw_inventory WHERE product_name = ?"
                    cur.execute(find_mrp, [product_name])
                    results = cur.fetchall()
                    stock = results[0][1]
                    mrp = results[0][0]
                    if product_qty.isdigit()==True:
                        if (stock-int(product_qty))>=0:
                            sp = results[0][0]*int(product_qty)
                            item = Item(product_name, mrp, int(product_qty))
                            self.cart.add_item(item)
                            self.Scrolledtext1.configure(state="normal")
                            bill_text = "{}\t\t\t\t\t\t{}\t\t\t\t\t   {}\n".format(product_name, product_qty, sp)
                            self.Scrolledtext1.insert('insert', bill_text)
                            self.Scrolledtext1.configure(state="disabled")
                        else:
                            messagebox.showerror("Oops!", "Out of stock. Check quantity.", parent=biller)
                    else:
                        messagebox.showerror("Oops!", "Invalid quantity.", parent=biller)
                else:
                    messagebox.showerror("Oops!", "Choose a product.", parent=biller)

        def remove_product(self):
            if(self.cart.isEmpty()!=True):
                self.Scrolledtext1.configure(state="normal")
                strr = self.Scrolledtext1.get('1.0', tk.END)
                if strr.find('Total')==-1:
                    try:
                        self.cart.remove_item()
                    except IndexError:
                        messagebox.showerror("Oops!", "Cart is empty", parent=biller)
                    else:
                        self.Scrolledtext1.configure(state="normal")
                        get_all_bill = (self.Scrolledtext1.get('1.0', tk.END).split("\n"))
                        new_string = get_all_bill[:len(get_all_bill)-3]
                        self.Scrolledtext1.delete('1.0', tk.END)
                        for i in range(len(new_string)):
                            self.Scrolledtext1.insert('insert', new_string[i])
                            self.Scrolledtext1.insert('insert','\n')
                        
                        self.Scrolledtext1.configure(state="disabled")
                else:
                    try:
                        self.cart.remove_item()
                    except IndexError:
                        messagebox.showerror("Oops!", "Cart is empty", parent=biller)
                    else:
                        self.Scrolledtext1.delete('1.0', tk.END)
                        new_li = []
                        li = strr.split("\n")
                        for i in range(len(li)):
                            if len(li[i])!=0:
                                if li[i].find('Total')==-1:
                                    new_li.append(li[i])
                                else:
                                    break
                        new_li.pop()
                        for j in range(len(new_li)-1):
                            self.Scrolledtext1.insert('insert', new_li[j])
                            self.Scrolledtext1.insert('insert','\n')
                        self.Scrolledtext1.configure(state="disabled")

            else:
                messagebox.showerror("Oops!", "Add a product.", parent=biller)

        def wel_bill(self):
            self.name_message = tk.Text(biller)
            self.name_message.place(relx=0.514, rely=0.452, width=176, height=30)
            self.name_message.configure(font="-family {Podkova} -size 10")
            self.name_message.configure(borderwidth=0)
            self.name_message.configure(background="#ffffff")

            self.num_message = tk.Text(biller)
            self.num_message.place(relx=0.894, rely=0.452, width=90, height=30)
            self.num_message.configure(font="-family {Podkova} -size 10")
            self.num_message.configure(borderwidth=0)
            self.num_message.configure(background="#ffffff")

            self.bill_message = tk.Text(biller)
            self.bill_message.place(relx=0.499, rely=0.477, width=176, height=26)
            self.bill_message.configure(font="-family {Podkova} -size 10")
            self.bill_message.configure(borderwidth=0)
            self.bill_message.configure(background="#ffffff")

            self.bill_date_message = tk.Text(biller)
            self.bill_date_message.place(relx=0.852, rely=0.477, width=90, height=26)
            self.bill_date_message.configure(font="-family {Podkova} -size 10")
            self.bill_date_message.configure(borderwidth=0)
            self.bill_date_message.configure(background="#ffffff")
        
        def total_bill(self):
            if self.cart.isEmpty():
                messagebox.showerror("Oops!", "Add a product.", parent=biller)
            else:
                self.Scrolledtext1.configure(state="normal")
                strr = self.Scrolledtext1.get('1.0', tk.END)
                if strr.find('Total')==-1:
                    self.Scrolledtext1.configure(state="normal")
                    divider = "\n\n\n"+("─"*61)
                    self.Scrolledtext1.insert('insert', divider)
                    total = "\nTotal\t\t\t\t\t\t\t\t\t\t\tRs. {}".format(self.cart.total())
                    self.Scrolledtext1.insert('insert', total)
                    divider2 = "\n"+("─"*61)
                    self.Scrolledtext1.insert('insert', divider2)
                    self.Scrolledtext1.configure(state="disabled")
                else:
                    return

        state = 1
        def gen_bill(self):

            if self.state == 1:
                strr = self.Scrolledtext1.get('1.0', tk.END)
                self.wel_bill()
                if(cust_name.get()==""):
                    messagebox.showerror("Oops!", "Please enter a name.", parent=biller)
                elif(cust_num.get()==""):
                    messagebox.showerror("Oops!", "Please enter a number.", parent=biller)
                elif valid_phone(cust_num.get())==False:
                    messagebox.showerror("Oops!", "Please enter a valid number.", parent=biller)
                elif(self.cart.isEmpty()):
                    messagebox.showerror("Oops!", "Cart is empty.", parent=biller)
                else: 
                    if strr.find('Total')==-1:
                        self.total_bill()
                        self.gen_bill()
                    else:
                        self.name_message.insert(tk.END, cust_name.get())
                        self.name_message.configure(state="disabled")
                
                        self.num_message.insert(tk.END, cust_num.get())
                        self.num_message.configure(state="disabled")
                
                        cust_new_bill.set(random_bill_number(8))

                        self.bill_message.insert(tk.END, cust_new_bill.get())
                        self.bill_message.configure(state="disabled")
                    
                        bill_date.set(str(date.today()))

                        self.bill_date_message.insert(tk.END, bill_date.get())
                        self.bill_date_message.configure(state="disabled")

                        

                        with sqlite3.connect("real-mart-master/Database/store.db") as db:
                            cur = db.cursor()
                        insert = (
                            "INSERT INTO bill(bill_no, date, customer_name, customer_no, bill_details) VALUES(?,?,?,?,?)"
                        )
                        cur.execute(insert, [cust_new_bill.get(), bill_date.get(), cust_name.get(), cust_num.get(), self.Scrolledtext1.get('1.0', tk.END)])
                        db.commit()
                        #print(self.cart.items)
                        print(self.cart.allCart())
                        for name, qty in self.cart.dictionary.items():
                            update_qty = "UPDATE raw_inventory SET stock = stock - ? WHERE product_name = ?"
                            cur.execute(update_qty, [qty, name])
                            db.commit()
                        messagebox.showinfo("Success!!", "Bill Generated", parent=biller)
                        self.entry1.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
                        self.entry2.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
                        self.state = 0
            else:
                return
                        
        def clear_bill(self):
            self.wel_bill()
            self.entry1.configure(state="normal")
            self.entry2.configure(state="normal")
            self.entry1.delete(0, tk.END)
            self.entry2.delete(0, tk.END)
            self.entry3.delete(0, tk.END)
            self.name_message.configure(state="normal")
            self.num_message.configure(state="normal")
            self.bill_message.configure(state="normal")
            self.bill_date_message.configure(state="normal")
            self.Scrolledtext1.configure(state="normal")
            self.name_message.delete(1.0, tk.END)
            self.num_message.delete(1.0, tk.END)
            self.bill_message.delete(1.0, tk.END)
            self.bill_date_message.delete(1.0, tk.END)
            self.Scrolledtext1.delete(1.0, tk.END)
            self.name_message.configure(state="disabled")
            self.num_message.configure(state="disabled")
            self.bill_message.configure(state="disabled")
            self.bill_date_message.configure(state="disabled")
            self.Scrolledtext1.configure(state="disabled")
            self.cart.remove_items()
            self.state = 1

        def clear_selection(self):
            self.entry4.delete(0, tk.END)
            self.combo1.configure(state="normal")
            self.combo2.configure(state="normal")
            self.combo3.configure(state="normal")
            self.combo1.delete(0, tk.END)
            self.combo2.delete(0, tk.END)
            self.combo3.delete(0, tk.END)
            self.combo2.configure(state="disabled")
            self.combo3.configure(state="disabled")
            self.entry4.configure(state="disabled")
            try:
                self.qty_label.configure(foreground="#ffffff")
            except AttributeError:
                pass
                
        def search_bill(self):
            find_bill = "SELECT * FROM bill WHERE bill_no = ?"
            cur.execute(find_bill, [cust_search_bill.get().rstrip()])
            results = cur.fetchall()
            if results:
                self.clear_bill()
                self.wel_bill()
                self.name_message.insert(tk.END, results[0][2])
                self.name_message.configure(state="disabled")
        
                self.num_message.insert(tk.END, results[0][3])
                self.num_message.configure(state="disabled")
        
                self.bill_message.insert(tk.END, results[0][0])
                self.bill_message.configure(state="disabled")

                self.bill_date_message.insert(tk.END, results[0][1])
                self.bill_date_message.configure(state="disabled")

                self.Scrolledtext1.configure(state="normal")
                self.Scrolledtext1.insert(tk.END, results[0][4])
                self.Scrolledtext1.configure(state="disabled")

                self.entry1.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
                self.entry2.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")

                self.state = 0

            else:
                messagebox.showerror("Error!!", "Bill not found.", parent=biller)
                self.entry3.delete(0, tk.END)
                
        def time(self):
            string = strftime("%H:%M:%S %p")
            self.clock.config(text=string)
            self.clock.after(1000, self.time)


    page1 = login_page(second)
    second.bind("<Return>", login)
    second.mainloop()

############################
##################
###### start admin method ################################################################################################################

def adm():
    # root=Tk()
    second=Toplevel(root)
    second.geometry("1366x768")
    second.title("Retail Manager(ADMIN)")


    user = StringVar()
    passwd = StringVar()
    fname = StringVar()
    lname = StringVar()


    with sqlite3.connect("real-mart-master/Database/store.db") as db:
        cur = db.cursor()

    def random_emp_id(stringLength):
        Digits = string.digits
        strr=''.join(random.choice(Digits) for i in range(stringLength-3))
        return ('EMP'+strr)

    def valid_phone(phn):
        if re.match(r"[789]\d{9}$", phn):
            return True
        return False

    def valid_aadhar(aad):
        if aad.isdigit() and len(aad)==12:
            return True
        return False


    class login_page:
        def __init__(self, top=None):
            top.geometry("1366x768")
            top.resizable(0, 0)
            top.title("Retail Manager(ADMIN)")

            self.label1 = Label(second)
            self.label1.place(relx=0, rely=0, width=1366, height=768)
            self.img = PhotoImage(file="real-mart-master/images/admin_login.png")
            self.label1.configure(image=self.img)
            # self.btn=Button(text="Back",fg="black",bg="orange",font=("Times",12))
            # self.btn.place(x=40,y=100)
            
            self.btn = Button(second)
            self.btn.place(x=50, y=70, width=100, height=25)
            self.btn.configure(relief="flat")
            self.btn.configure(overrelief="flat")
            self.btn.configure(activebackground="#D2463E")
            self.btn.configure(cursor="hand2")
            self.btn.configure(foreground="#ffffff")
            self.btn.configure(background="#D2463E")
            self.btn.configure(font="-family {Poppins SemiBold} -size 10")
            self.btn.configure(borderwidth="0")
            self.btn.configure(text="""Back""")
            self.btn.configure(command=self.login)
            

            self.entry1 = Entry(second)
            self.entry1.place(relx=0.373, rely=0.273, width=374, height=24)
            self.entry1.configure(font="-family {Poppins} -size 10")
            self.entry1.configure(relief="flat")
            self.entry1.configure(textvariable=user)

            self.entry2 = Entry(second)
            self.entry2.place(relx=0.373, rely=0.384, width=374, height=24)
            self.entry2.configure(font="-family {Poppins} -size 10")
            self.entry2.configure(relief="flat")
            self.entry2.configure(show="*")
            self.entry2.configure(textvariable=passwd)

            self.button1 = Button(second)
            self.button1.place(relx=0.366, rely=0.685, width=356, height=43)
            self.button1.configure(relief="flat")
            self.button1.configure(overrelief="flat")
            self.button1.configure(activebackground="#D2463E")
            self.button1.configure(cursor="hand2")
            self.button1.configure(foreground="#ffffff")
            self.button1.configure(background="#D2463E")
            self.button1.configure(font="-family {Poppins SemiBold} -size 20")
            self.button1.configure(borderwidth="0")
            self.button1.configure(text="""LOGIN""")
            self.button1.configure(command=self.login)

        def login(self, Event=None):
            username = user.get()
            password = passwd.get()

            with sqlite3.connect("real-mart-master/Database/store.db") as db:
                cur = db.cursor()
            find_user = "SELECT * FROM employee WHERE emp_id = ? and password = ?"
            cur.execute(find_user, [username, password])
            results = cur.fetchall()
            if results:
                if results[0][6]=="Admin":
                    messagebox.showinfo("Login Page", "The login is successful.")
                    page1.entry1.delete(0, END)
                    page1.entry2.delete(0, END)

                    second.withdraw()
                    global adm
                    global page2
                    adm = Toplevel()
                    page2 = Admin_Page(adm)
                    #page2.time()
                    adm.protocol("WM_DELETE_WINDOW", exitt)
                    adm.mainloop()
                else:
                    messagebox.showerror("Oops!!", "You are not an admin.")

            else:
                messagebox.showerror("Error", "Incorrect username or password.")
                page1.entry2.delete(0, END)

        
    def exitt():
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=second)
        if sure == True:
            adm.destroy()
            second.destroy()

    def inventory():
        adm.withdraw()
        global inv
        global page3
        inv = Toplevel()
        page3 = Inventory(inv)
        page3.time()
        inv.protocol("WM_DELETE_WINDOW", exitt)
        inv.mainloop()


    def employee():
        adm.withdraw()
        global emp
        global page5
        emp = Toplevel()
        page5 = Employee(emp)
        page5.time()
        emp.protocol("WM_DELETE_WINDOW", exitt)
        emp.mainloop()


    def invoices():
        adm.withdraw()
        global invoice
        invoice = Toplevel()
        page7 = Invoice(invoice)
        page7.time()
        invoice.protocol("WM_DELETE_WINDOW", exitt)
        invoice.mainloop()

    def about():
        pass



    class Admin_Page:
        def __init__(self, top=None):
            top.geometry("1366x768")
            top.resizable(0, 0)
            top.title("ADMIN Mode")

            self.label1 = Label(adm)
            self.label1.place(relx=0, rely=0, width=1366, height=768)
            self.img = PhotoImage(file="real-mart-master/images/admin.png")
            self.label1.configure(image=self.img)

            self.message = Label(adm)
            self.message.place(relx=0.046, rely=0.056, width=62, height=30)
            self.message.configure(font="-family {Poppins} -size 12")
            self.message.configure(foreground="#ffffff")
            self.message.configure(background="#FE6B61")
            self.message.configure(text="""ADMIN""")
            self.message.configure(anchor="w")

            self.button1 = Button(adm)
            self.button1.place(relx=0.035, rely=0.106, width=76, height=23)
            self.button1.configure(relief="flat")
            self.button1.configure(overrelief="flat")
            self.button1.configure(activebackground="orange")
            self.button1.configure(cursor="hand2")
            self.button1.configure(foreground="#ffffff")
            self.button1.configure(background="orange")
            self.button1.configure(font="-family {Poppins SemiBold} -size 12")
            self.button1.configure(borderwidth="0")
            self.button1.configure(text="""Logout""")
            self.button1.configure(command=self.Logout)

            self.button2 = Button(adm)
            self.button2.place(relx=0.14, rely=0.508, width=146, height=63)
            self.button2.configure(relief="flat")
            self.button2.configure(overrelief="flat")
            self.button2.configure(activebackground="#ffffff")
            self.button2.configure(cursor="hand2")
            self.button2.configure(foreground="#333333")
            self.button2.configure(background="#ffffff")
            self.button2.configure(font="-family {Poppins SemiBold} -size 12")
            self.button2.configure(borderwidth="0")
            self.button2.configure(text="""Inventory""")
            self.button2.configure(command=inventory)

            self.button3 = Button(adm)
            self.button3.place(relx=0.338, rely=0.508, width=146, height=63)
            self.button3.configure(relief="flat")
            self.button3.configure(overrelief="flat")
            self.button3.configure(activebackground="#ffffff")
            self.button3.configure(cursor="hand2")
            self.button3.configure(foreground="#333333")
            self.button3.configure(background="#ffffff")
            self.button3.configure(font="-family {Poppins SemiBold} -size 12")
            self.button3.configure(borderwidth="0")
            self.button3.configure(text="""Employees""")
            self.button3.configure(command=employee)


            self.button4 = Button(adm)
            self.button4.place(relx=0.536, rely=0.508, width=146, height=63)
            self.button4.configure(relief="flat")
            self.button4.configure(overrelief="flat")
            self.button4.configure(activebackground="#ffffff")
            self.button4.configure(cursor="hand2")
            self.button4.configure(foreground="#333333")
            self.button4.configure(background="#ffffff")
            self.button4.configure(font="-family {Poppins SemiBold} -size 12")
            self.button4.configure(borderwidth="0")
            self.button4.configure(text="""Invoices""")
            self.button4.configure(command=invoices)


            self.button5 = Button(adm)
            self.button5.place(relx=0.732, rely=0.508, width=146, height=63)
            self.button5.configure(relief="flat")
            self.button5.configure(overrelief="flat")
            self.button5.configure(activebackground="#ffffff")
            self.button5.configure(cursor="hand2")
            self.button5.configure(foreground="#333333")
            self.button5.configure(background="#ffffff")
            self.button5.configure(font="-family {Poppins SemiBold} -size 12")
            self.button5.configure(borderwidth="0")
            self.button5.configure(text="""About Us""")
            self.button5.configure(command=about)

        def Logout(self):
            sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=adm)
            if sure == True:
                adm.destroy()
                second.deiconify()
                page1.entry1.delete(0, END)
                page1.entry2.delete(0, END)


    class Inventory:
        def __init__(self, top=None):
            top.geometry("1366x768")
            top.resizable(0, 0)
            top.title("Inventory")

            self.label1 = Label(inv)
            self.label1.place(relx=0, rely=0, width=1366, height=768)
            self.img = PhotoImage(file="real-mart-master/images/inventory.png")
            self.label1.configure(image=self.img)

            self.message = Label(inv)
            self.message.place(relx=0.046, rely=0.055, width=136, height=30)
            self.message.configure(font="-family {Poppins} -size 10")
            self.message.configure(foreground="#000000")
            self.message.configure(background="#ffffff")
            self.message.configure(text="""ADMIN""")
            self.message.configure(anchor="w")

            self.clock = Label(inv)
            self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
            self.clock.configure(font="-family {Poppins Light} -size 12")
            self.clock.configure(foreground="#000000")
            self.clock.configure(background="#ffffff")

            self.entry1 = Entry(inv)
            self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
            self.entry1.configure(font="-family {Poppins} -size 12")
            self.entry1.configure(relief="flat")

            self.button1 = Button(inv)
            self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
            self.button1.configure(relief="flat")
            self.button1.configure(overrelief="flat")
            self.button1.configure(activebackground="orange")
            self.button1.configure(cursor="hand2")
            self.button1.configure(foreground="#ffffff")
            self.button1.configure(background="orange")
            self.button1.configure(font="-family {Poppins SemiBold} -size 10")
            self.button1.configure(borderwidth="0")
            self.button1.configure(text="""Search""")
            self.button1.configure(command=self.search_product)

            self.button2 = Button(inv)
            self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
            self.button2.configure(relief="flat")
            self.button2.configure(overrelief="flat")
            self.button2.configure(activebackground="orange")
            self.button2.configure(cursor="hand2")
            self.button2.configure(foreground="#ffffff")
            self.button2.configure(background="orange")
            self.button2.configure(font="-family {Poppins SemiBold} -size 12")
            self.button2.configure(borderwidth="0")
            self.button2.configure(text="""Logout""")
            self.button2.configure(command=self.Logout)

            self.button3 = Button(inv)
            self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
            self.button3.configure(relief="flat")
            self.button3.configure(overrelief="flat")
            self.button3.configure(activebackground="orange")
            self.button3.configure(cursor="hand2")
            self.button3.configure(foreground="#ffffff")
            self.button3.configure(background="orange")
            self.button3.configure(font="-family {Poppins SemiBold} -size 12")
            self.button3.configure(borderwidth="0")
            self.button3.configure(text="""ADD PRODUCT""")
            self.button3.configure(command=self.add_product)

            self.button4 = Button(inv)
            self.button4.place(relx=0.052, rely=0.5, width=306, height=28)
            self.button4.configure(relief="flat")
            self.button4.configure(overrelief="flat")
            self.button4.configure(activebackground="orange")
            self.button4.configure(cursor="hand2")
            self.button4.configure(foreground="#ffffff")
            self.button4.configure(background="orange")
            self.button4.configure(font="-family {Poppins SemiBold} -size 12")
            self.button4.configure(borderwidth="0")
            self.button4.configure(text="""UPDATE PRODUCT""")
            self.button4.configure(command=self.update_product)

            self.button5 = Button(inv)
            self.button5.place(relx=0.052, rely=0.57, width=306, height=28)
            self.button5.configure(relief="flat")
            self.button5.configure(overrelief="flat")
            self.button5.configure(activebackground="orange")
            self.button5.configure(cursor="hand2")
            self.button5.configure(foreground="#ffffff")
            self.button5.configure(background="orange")
            self.button5.configure(font="-family {Poppins SemiBold} -size 12")
            self.button5.configure(borderwidth="0")
            self.button5.configure(text="""DELETE PRODUCT""")
            self.button5.configure(command=self.delete_product)

            self.button6 = Button(inv)
            self.button6.place(relx=0.135, rely=0.885, width=76, height=23)
            self.button6.configure(relief="flat")
            self.button6.configure(overrelief="flat")
            self.button6.configure(activebackground="orange")
            self.button6.configure(cursor="hand2")
            self.button6.configure(foreground="#ffffff")
            self.button6.configure(background="orange")
            self.button6.configure(font="-family {Poppins SemiBold} -size 12")
            self.button6.configure(borderwidth="0")
            self.button6.configure(text="""EXIT""")
            self.button6.configure(command=self.Exit)

            self.scrollbarx = Scrollbar(inv, orient=HORIZONTAL)
            self.scrollbary = Scrollbar(inv, orient=VERTICAL)
            self.tree = ttk.Treeview(inv)
            self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
            self.tree.configure(
                yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
            )
            self.tree.configure(selectmode="extended")

            self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

            self.scrollbary.configure(command=self.tree.yview)
            self.scrollbarx.configure(command=self.tree.xview)

            self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
            self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

            self.tree.configure(
                columns=(
                    "Product ID",
                    "Name",
                    "Category",
                    "Sub-Category",
                    "In Stock",
                    "MRP",
                    "Cost Price",
                    "Vendor No.",
                )
            )

            self.tree.heading("Product ID", text="Product ID", anchor=W)
            self.tree.heading("Name", text="Name", anchor=W)
            self.tree.heading("Category", text="Category", anchor=W)
            self.tree.heading("Sub-Category", text="Sub-Category", anchor=W)
            self.tree.heading("In Stock", text="In Stock", anchor=W)
            self.tree.heading("MRP", text="MRP", anchor=W)
            self.tree.heading("Cost Price", text="Cost Price", anchor=W)
            self.tree.heading("Vendor No.", text="Vendor No.", anchor=W)

            self.tree.column("#0", stretch=NO, minwidth=0, width=0)
            self.tree.column("#1", stretch=NO, minwidth=0, width=80)
            self.tree.column("#2", stretch=NO, minwidth=0, width=260)
            self.tree.column("#3", stretch=NO, minwidth=0, width=100)
            self.tree.column("#4", stretch=NO, minwidth=0, width=120)
            self.tree.column("#5", stretch=NO, minwidth=0, width=80)
            self.tree.column("#6", stretch=NO, minwidth=0, width=80)
            self.tree.column("#7", stretch=NO, minwidth=0, width=80)
            self.tree.column("#8", stretch=NO, minwidth=0, width=100)

            self.DisplayData()

        def DisplayData(self):
            cur.execute("SELECT * FROM raw_inventory")
            fetch = cur.fetchall()
            for data in fetch:
                self.tree.insert("", "end", values=(data))

        def search_product(self):
            val = []
            for i in self.tree.get_children():
                val.append(i)
                for j in self.tree.item(i)["values"]:
                    val.append(j)

            try:
                to_search = int(self.entry1.get())
            except ValueError:
                messagebox.showerror("Oops!!", "Invalid Product Id.", parent=inv)
            else:
                for search in val:
                    if search==to_search:
                        self.tree.selection_set(val[val.index(search)-1])
                        self.tree.focus(val[val.index(search)-1])
                        messagebox.showinfo("Success!!", "Product ID: {} found.".format(self.entry1.get()), parent=inv)
                        break
                else: 
                    messagebox.showerror("Oops!!", "Product ID: {} not found.".format(self.entry1.get()), parent=inv)
        
        sel = []
        def on_tree_select(self, Event):
            self.sel.clear()
            for i in self.tree.selection():
                if i not in self.sel:
                    self.sel.append(i)

        def delete_product(self):
            val = []
            to_delete = []

            if len(self.sel)!=0:
                sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected products?", parent=inv)
                if sure == True:
                    for i in self.sel:
                        for j in self.tree.item(i)["values"]:
                            val.append(j)
                    
                    for j in range(len(val)):
                        if j%8==0:
                            to_delete.append(val[j])
                    
                    for k in to_delete:
                        delete = "DELETE FROM raw_inventory WHERE product_id = ?"
                        cur.execute(delete, [k])
                        db.commit()

                    messagebox.showinfo("Success!!", "Products deleted from database.", parent=inv)
                    self.sel.clear()
                    self.tree.delete(*self.tree.get_children())

                    self.DisplayData()
            else:
                messagebox.showerror("Error!!","Please select a product.", parent=inv)

        def update_product(self):
            if len(self.sel)==1:
                global p_update
                p_update = Toplevel()
                page9 = Update_Product(p_update)
                page9.time()
                p_update.protocol("WM_DELETE_WINDOW", self.ex2)
                global valll
                valll = []
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        valll.append(j)

                page9.entry1.insert(0, valll[1])
                page9.entry2.insert(0, valll[2])
                page9.entry3.insert(0, valll[4])
                page9.entry4.insert(0, valll[5])
                page9.entry6.insert(0, valll[3])
                page9.entry7.insert(0, valll[6])
                page9.entry8.insert(0, valll[7])


            elif len(self.sel)==0:
                messagebox.showerror("Error","Please choose a product to update.", parent=inv)
            else:
                messagebox.showerror("Error","Can only update one product at a time.", parent=inv)

            p_update.mainloop()

        

        def add_product(self):
            global p_add
            global page4
            p_add = Toplevel()
            page4 = add_product(p_add)
            page4.time()
            p_add.mainloop()

        def time(self):
            string = strftime("%H:%M:%S %p")
            self.clock.config(text=string)
            self.clock.after(1000, self.time)

        def Exit(self):
            sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=inv)
            if sure == True:
                inv.destroy()
                adm.deiconify()

        def ex2(self):
            sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=p_update)
            if sure == True:
                p_update.destroy()
                inv.deiconify()



        def Logout(self):
            sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
            if sure == True:
                second.deiconify()
                page1.entry1.delete(0, END)
                page1.entry2.delete(0, END)


    class add_product:
        def __init__(self, top=None):
            top.geometry("1366x768")
            top.resizable(0, 0)
            top.title("Add Product")

            self.label1 = Label(p_add)
            self.label1.place(relx=0, rely=0, width=1366, height=768)
            self.img = PhotoImage(file="real-mart-master/images/add_product.png")
            self.label1.configure(image=self.img)

            self.clock = Label(p_add)
            self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
            self.clock.configure(font="-family {Poppins Light} -size 12")
            self.clock.configure(foreground="#000000")
            self.clock.configure(background="#ffffff")

            self.entry1 = Entry(p_add)
            self.entry1.place(relx=0.132, rely=0.296, width=996, height=30)
            self.entry1.configure(font="-family {Poppins} -size 12")
            self.entry1.configure(relief="flat")

            self.entry2 = Entry(p_add)
            self.entry2.place(relx=0.132, rely=0.413, width=374, height=30)
            self.entry2.configure(font="-family {Poppins} -size 12")
            self.entry2.configure(relief="flat")

            self.r2 = p_add.register(self.testint)

            self.entry3 = Entry(p_add)
            self.entry3.place(relx=0.132, rely=0.529, width=374, height=30)
            self.entry3.configure(font="-family {Poppins} -size 12")
            self.entry3.configure(relief="flat")
            self.entry3.configure(validate="key", validatecommand=(self.r2, "%P"))

            self.entry4 = Entry(p_add)
            self.entry4.place(relx=0.132, rely=0.646, width=374, height=30)
            self.entry4.configure(font="-family {Poppins} -size 12")
            self.entry4.configure(relief="flat")
        

            self.entry6 = Entry(p_add)
            self.entry6.place(relx=0.527, rely=0.413, width=374, height=30)
            self.entry6.configure(font="-family {Poppins} -size 12")
            self.entry6.configure(relief="flat")
        

            self.entry7 = Entry(p_add)
            self.entry7.place(relx=0.527, rely=0.529, width=374, height=30)
            self.entry7.configure(font="-family {Poppins} -size 12")
            self.entry7.configure(relief="flat")
        

            self.entry8 = Entry(p_add)
            self.entry8.place(relx=0.527, rely=0.646, width=374, height=30)
            self.entry8.configure(font="-family {Poppins} -size 12")
            self.entry8.configure(relief="flat")
            self.entry8.configure(validate="key", validatecommand=(self.r2, "%P"))
        

            self.button1 = Button(p_add)
            self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
            self.button1.configure(relief="flat")
            self.button1.configure(overrelief="flat")
            self.button1.configure(activebackground="orange")
            self.button1.configure(cursor="hand2")
            self.button1.configure(foreground="#ffffff")
            self.button1.configure(background="orange")
            self.button1.configure(font="-family {Poppins SemiBold} -size 14")
            self.button1.configure(borderwidth="0")
            self.button1.configure(text="""ADD""")
            self.button1.configure(command=self.add)

            self.button2 = Button(p_add)
            self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
            self.button2.configure(relief="flat")
            self.button2.configure(overrelief="flat")
            self.button2.configure(activebackground="orange")
            self.button2.configure(cursor="hand2")
            self.button2.configure(foreground="#ffffff")
            self.button2.configure(background="orange")
            self.button2.configure(font="-family {Poppins SemiBold} -size 14")
            self.button2.configure(borderwidth="0")
            self.button2.configure(text="""CLEAR""")
            self.button2.configure(command=self.clearr)

        def add(self):
            pqty = self.entry3.get()
            pcat = self.entry2.get()  
            pmrp = self.entry4.get()  
            pname = self.entry1.get()  
            psubcat = self.entry6.get()  
            pcp = self.entry7.get()  
            pvendor = self.entry8.get()  
        

            if pname.strip():
                if pcat.strip():
                    if psubcat.strip():
                        if pqty:
                            if pcp:
                                try:
                                    float(pcp)
                                except ValueError:
                                    messagebox.showerror("Oops!", "Invalid cost price.", parent=p_add)
                                else:
                                    if pmrp:
                                        try:
                                            float(pmrp)
                                        except ValueError:
                                            messagebox.showerror("Oops!", "Invalid MRP.", parent=p_add)
                                        else:
                                            if valid_phone(pvendor):
                                                with sqlite3.connect("real-mart-master/Database/store.db") as db:
                                                    cur = db.cursor()
                                                insert = (
                                                            "INSERT INTO raw_inventory(product_name, product_cat, product_subcat, stock, mrp, cost_price, vendor_phn) VALUES(?,?,?,?,?,?,?)"
                                                        )
                                                cur.execute(insert, [pname, pcat, psubcat, int(pqty), float(pmrp), float(pcp), pvendor])
                                                db.commit()
                                                messagebox.showinfo("Success!!", "Product successfully added in inventory.", parent=p_add)
                                                p_add.destroy()
                                                page3.tree.delete(*page3.tree.get_children())
                                                page3.DisplayData()
                                                p_add.destroy()
                                            else:
                                                messagebox.showerror("Oops!", "Invalid phone number.", parent=p_add)
                                    else:
                                        messagebox.showerror("Oops!", "Please enter MRP.", parent=p_add)
                            else:
                                messagebox.showerror("Oops!", "Please enter product cost price.", parent=p_add)
                        else:
                            messagebox.showerror("Oops!", "Please enter product quantity.", parent=p_add)
                    else:
                        messagebox.showerror("Oops!", "Please enter product sub-category.", parent=p_add)
                else:
                    messagebox.showerror("Oops!", "Please enter product category.", parent=p_add)
            else:
                messagebox.showerror("Oops!", "Please enter product name", parent=p_add)

        def clearr(self):
            self.entry1.delete(0, END)
            self.entry2.delete(0, END)
            self.entry3.delete(0, END)
            self.entry4.delete(0, END)
            self.entry6.delete(0, END)
            self.entry7.delete(0, END)
            self.entry8.delete(0, END)

        def testint(self, val):
            if val.isdigit():
                return True
            elif val == "":
                return True
            return False

        def time(self):
            string = strftime("%H:%M:%S %p")
            self.clock.config(text=string)
            self.clock.after(1000, self.time)


    class Update_Product:
        def __init__(self, top=None):
            top.geometry("1366x768")
            top.resizable(0, 0)
            top.title("Add Product")

            self.label1 = Label(p_update)
            self.label1.place(relx=0, rely=0, width=1366, height=768)
            self.img = PhotoImage(file="real-mart-master/images/update_product.png")
            self.label1.configure(image=self.img)

            self.clock = Label(p_update)
            self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
            self.clock.configure(font="-family {Poppins Light} -size 12")
            self.clock.configure(foreground="#000000")
            self.clock.configure(background="#ffffff")

            self.entry1 = Entry(p_update)
            self.entry1.place(relx=0.132, rely=0.296, width=996, height=30)
            self.entry1.configure(font="-family {Poppins} -size 12")
            self.entry1.configure(relief="flat")

            self.entry2 = Entry(p_update)
            self.entry2.place(relx=0.132, rely=0.413, width=374, height=30)
            self.entry2.configure(font="-family {Poppins} -size 12")
            self.entry2.configure(relief="flat")

            self.r2 = p_update.register(self.testint)

            self.entry3 = Entry(p_update)
            self.entry3.place(relx=0.132, rely=0.529, width=374, height=30)
            self.entry3.configure(font="-family {Poppins} -size 12")
            self.entry3.configure(relief="flat")
            self.entry3.configure(validate="key", validatecommand=(self.r2, "%P"))

            self.entry4 = Entry(p_update)
            self.entry4.place(relx=0.132, rely=0.646, width=374, height=30)
            self.entry4.configure(font="-family {Poppins} -size 12")
            self.entry4.configure(relief="flat")
        

            self.entry6 = Entry(p_update)
            self.entry6.place(relx=0.527, rely=0.413, width=374, height=30)
            self.entry6.configure(font="-family {Poppins} -size 12")
            self.entry6.configure(relief="flat")
        

            self.entry7 = Entry(p_update)
            self.entry7.place(relx=0.527, rely=0.529, width=374, height=30)
            self.entry7.configure(font="-family {Poppins} -size 12")
            self.entry7.configure(relief="flat")
        

            self.entry8 = Entry(p_update)
            self.entry8.place(relx=0.527, rely=0.646, width=374, height=30)
            self.entry8.configure(font="-family {Poppins} -size 12")
            self.entry8.configure(relief="flat")
        

            self.button1 = Button(p_update)
            self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
            self.button1.configure(relief="flat")
            self.button1.configure(overrelief="flat")
            self.button1.configure(activebackground="orange")
            self.button1.configure(cursor="hand2")
            self.button1.configure(foreground="#ffffff")
            self.button1.configure(background="orange")
            self.button1.configure(font="-family {Poppins SemiBold} -size 14")
            self.button1.configure(borderwidth="0")
            self.button1.configure(text="""UPDATE""")
            self.button1.configure(command=self.update)

            self.button2 = Button(p_update)
            self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
            self.button2.configure(relief="flat")
            self.button2.configure(overrelief="flat")
            self.button2.configure(activebackground="orange")
            self.button2.configure(cursor="hand2")
            self.button2.configure(foreground="#ffffff")
            self.button2.configure(background="orange")
            self.button2.configure(font="-family {Poppins SemiBold} -size 14")
            self.button2.configure(borderwidth="0")
            self.button2.configure(text="""CLEAR""")
            self.button2.configure(command=self.clearr)

        def update(self):
            pqty = self.entry3.get()
            pcat = self.entry2.get()  
            pmrp = self.entry4.get()  
            pname = self.entry1.get()  
            psubcat = self.entry6.get()  
            pcp = self.entry7.get()  
            pvendor = self.entry8.get()  
        

            if pname.strip():
                if pcat.strip():
                    if psubcat.strip():
                        if pqty:
                            if pcp:
                                try:
                                    float(pcp)
                                except ValueError:
                                    messagebox.showerror("Oops!", "Invalid cost price.", parent=p_update)
                                else:
                                    if pmrp:
                                        try:
                                            float(pmrp)
                                        except ValueError:
                                            messagebox.showerror("Oops!", "Invalid MRP.", parent=p_update)
                                        else:
                                            if valid_phone(pvendor):
                                                product_id = valll[0]
                                                with sqlite3.connect("real-mart-master/Database/store.db") as db:
                                                    cur = db.cursor()
                                                update = (
                                                "UPDATE raw_inventory SET product_name = ?, product_cat = ?, product_subcat = ?, stock = ?, mrp = ?, cost_price = ?, vendor_phn = ? WHERE product_id = ?"
                                                )
                                                cur.execute(update, [pname, pcat, psubcat, int(pqty), float(pmrp), float(pcp), pvendor, product_id])
                                                db.commit()
                                                messagebox.showinfo("Success!!", "Product successfully updated in inventory.", parent=p_update)
                                                valll.clear()
                                                Inventory.sel.clear()
                                                page3.tree.delete(*page3.tree.get_children())
                                                page3.DisplayData()
                                                p_update.destroy()
                                            else:
                                                messagebox.showerror("Oops!", "Invalid phone number.", parent=p_update)
                                    else:
                                        messagebox.showerror("Oops!", "Please enter MRP.", parent=p_update)
                            else:
                                messagebox.showerror("Oops!", "Please enter product cost price.", parent=p_update)
                        else:
                            messagebox.showerror("Oops!", "Please enter product quantity.", parent=p_update)
                    else:
                        messagebox.showerror("Oops!", "Please enter product sub-category.", parent=p_update)
                else:
                    messagebox.showerror("Oops!", "Please enter product category.", parent=p_update)
            else:
                messagebox.showerror("Oops!", "Please enter product name", parent=p_update)

        def clearr(self):
            self.entry1.delete(0, END)
            self.entry2.delete(0, END)
            self.entry3.delete(0, END)
            self.entry4.delete(0, END)
            self.entry6.delete(0, END)
            self.entry7.delete(0, END)
            self.entry8.delete(0, END)

        def testint(self, val):
            if val.isdigit():
                return True
            elif val == "":
                return True
            return False

        def time(self):
            string = strftime("%H:%M:%S %p")
            self.clock.config(text=string)
            self.clock.after(1000, self.time)
        


    class Employee:
        def __init__(self, top=None):
            top.geometry("1366x768")
            top.resizable(0, 0)
            top.title("Employee Management")

            self.label1 = Label(emp)
            self.label1.place(relx=0, rely=0, width=1366, height=768)
            self.img = PhotoImage(file="real-mart-master/images/employee.png")
            self.label1.configure(image=self.img)

            self.message = Label(emp)
            self.message.place(relx=0.046, rely=0.055, width=136, height=30)
            self.message.configure(font="-family {Poppins} -size 10")
            self.message.configure(foreground="#000000")
            self.message.configure(background="#ffffff")
            self.message.configure(text="""ADMIN""")
            self.message.configure(anchor="w")

            self.clock = Label(emp)
            self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
            self.clock.configure(font="-family {Poppins Light} -size 12")
            self.clock.configure(foreground="#000000")
            self.clock.configure(background="#ffffff")

            self.entry1 = Entry(emp)
            self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
            self.entry1.configure(font="-family {Poppins} -size 12")
            self.entry1.configure(relief="flat")

            self.button1 = Button(emp)
            self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
            self.button1.configure(relief="flat")
            self.button1.configure(overrelief="flat")
            self.button1.configure(activebackground="orange")
            self.button1.configure(cursor="hand2")
            self.button1.configure(foreground="#ffffff")
            self.button1.configure(background="orange")
            self.button1.configure(font="-family {Poppins SemiBold} -size 10")
            self.button1.configure(borderwidth="0")
            self.button1.configure(text="""Search""")
            self.button1.configure(command=self.search_emp)

            self.button2 = Button(emp)
            self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
            self.button2.configure(relief="flat")
            self.button2.configure(overrelief="flat")
            self.button2.configure(activebackground="orange")
            self.button2.configure(cursor="hand2")
            self.button2.configure(foreground="#ffffff")
            self.button2.configure(background="orange")
            self.button2.configure(font="-family {Poppins SemiBold} -size 12")
            self.button2.configure(borderwidth="0")
            self.button2.configure(text="""Logout""")
            self.button2.configure(command=self.Logout)

            self.button3 = Button(emp)
            self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
            self.button3.configure(relief="flat")
            self.button3.configure(overrelief="flat")
            self.button3.configure(activebackground="orange")
            self.button3.configure(cursor="hand2")
            self.button3.configure(foreground="#ffffff")
            self.button3.configure(background="orange")
            self.button3.configure(font="-family {Poppins SemiBold} -size 12")
            self.button3.configure(borderwidth="0")
            self.button3.configure(text="""ADD EMPLOYEE""")
            self.button3.configure(command=self.add_emp)

            self.button4 = Button(emp)
            self.button4.place(relx=0.052, rely=0.5, width=306, height=28)
            self.button4.configure(relief="flat")
            self.button4.configure(overrelief="flat")
            self.button4.configure(activebackground="orange")
            self.button4.configure(cursor="hand2")
            self.button4.configure(foreground="#ffffff")
            self.button4.configure(background="orange")
            self.button4.configure(font="-family {Poppins SemiBold} -size 12")
            self.button4.configure(borderwidth="0")
            self.button4.configure(text="""UPDATE EMPLOYEE""")
            self.button4.configure(command=self.update_emp)

            self.button5 = Button(emp)
            self.button5.place(relx=0.052, rely=0.57, width=306, height=28)
            self.button5.configure(relief="flat")
            self.button5.configure(overrelief="flat")
            self.button5.configure(activebackground="orange")
            self.button5.configure(cursor="hand2")
            self.button5.configure(foreground="#ffffff")
            self.button5.configure(background="orange")
            self.button5.configure(font="-family {Poppins SemiBold} -size 12")
            self.button5.configure(borderwidth="0")
            self.button5.configure(text="""DELETE EMPLOYEE""")
            self.button5.configure(command=self.delete_emp)

            self.button6 = Button(emp)
            self.button6.place(relx=0.135, rely=0.885, width=76, height=23)
            self.button6.configure(relief="flat")
            self.button6.configure(overrelief="flat")
            self.button6.configure(activebackground="orange")
            self.button6.configure(cursor="hand2")
            self.button6.configure(foreground="#ffffff")
            self.button6.configure(background="orange")
            self.button6.configure(font="-family {Poppins SemiBold} -size 12")
            self.button6.configure(borderwidth="0")
            self.button6.configure(text="""EXIT""")
            self.button6.configure(command=self.Exit)

            self.scrollbarx = Scrollbar(emp, orient=HORIZONTAL)
            self.scrollbary = Scrollbar(emp, orient=VERTICAL)
            self.tree = ttk.Treeview(emp)
            self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
            self.tree.configure(
                yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
            )
            self.tree.configure(selectmode="extended")

            self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

            self.scrollbary.configure(command=self.tree.yview)
            self.scrollbarx.configure(command=self.tree.xview)

            self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
            self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

            self.tree.configure(
                columns=(
                    "Employee ID",
                    "Employee Name",
                    "Contact No.",
                    "Address",
                    "Aadhar No.",
                    "Password",
                    "Designation"
                )
            )

            self.tree.heading("Employee ID", text="Employee ID", anchor=W)
            self.tree.heading("Employee Name", text="Employee Name", anchor=W)
            self.tree.heading("Contact No.", text="Contact No.", anchor=W)
            self.tree.heading("Address", text="Address", anchor=W)
            self.tree.heading("Aadhar No.", text="Aadhar No.", anchor=W)
            self.tree.heading("Password", text="Password", anchor=W)
            self.tree.heading("Designation", text="Designation", anchor=W)

            self.tree.column("#0", stretch=NO, minwidth=0, width=0)
            self.tree.column("#1", stretch=NO, minwidth=0, width=80)
            self.tree.column("#2", stretch=NO, minwidth=0, width=260)
            self.tree.column("#3", stretch=NO, minwidth=0, width=100)
            self.tree.column("#4", stretch=NO, minwidth=0, width=198)
            self.tree.column("#5", stretch=NO, minwidth=0, width=80)
            self.tree.column("#6", stretch=NO, minwidth=0, width=80)
            self.tree.column("#7", stretch=NO, minwidth=0, width=80)

            self.DisplayData()

        def DisplayData(self):
            cur.execute("SELECT * FROM employee")
            fetch = cur.fetchall()
            for data in fetch:
                self.tree.insert("", "end", values=(data))

        def search_emp(self):
            val = []
            for i in self.tree.get_children():
                val.append(i)
                for j in self.tree.item(i)["values"]:
                    val.append(j)

            to_search = self.entry1.get()
            for search in val:
                if search==to_search:
                    self.tree.selection_set(val[val.index(search)-1])
                    self.tree.focus(val[val.index(search)-1])
                    messagebox.showinfo("Success!!", "Employee ID: {} found.".format(self.entry1.get()), parent=emp)
                    break
            else: 
                messagebox.showerror("Oops!!", "Employee ID: {} not found.".format(self.entry1.get()), parent=emp)
        
        sel = []
        def on_tree_select(self, Event):
            self.sel.clear()
            for i in self.tree.selection():
                if i not in self.sel:
                    self.sel.append(i)

        def delete_emp(self):
            val = []
            to_delete = []

            if len(self.sel)!=0:
                sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected employee(s)?", parent=emp)
                if sure == True:
                    for i in self.sel:
                        for j in self.tree.item(i)["values"]:
                            val.append(j)
                    
                    for j in range(len(val)):
                        if j%7==0:
                            to_delete.append(val[j])
                    
                    flag = 1

                    for k in to_delete:
                        if k=="EMP0000":
                            flag = 0
                            break
                        else:
                            delete = "DELETE FROM employee WHERE emp_id = ?"
                            cur.execute(delete, [k])
                            db.commit()

                    if flag==1:
                        messagebox.showinfo("Success!!", "Employee(s) deleted from database.", parent=emp)
                        self.sel.clear()
                        self.tree.delete(*self.tree.get_children())
                        self.DisplayData()
                    else:
                        messagebox.showerror("Error!!","Cannot delete master admin.")
            else:
                messagebox.showerror("Error!!","Please select an employee.", parent=emp)

        def update_emp(self):
            
            if len(self.sel)==1:
                global e_update
                e_update = Toplevel()
                page8 = Update_Employee(e_update)
                page8.time()
                e_update.protocol("WM_DELETE_WINDOW", self.ex2)
                global vall
                vall = []
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        vall.append(j)
                
                page8.entry1.insert(0, vall[1])
                page8.entry2.insert(0, vall[2])
                page8.entry3.insert(0, vall[4])
                page8.entry4.insert(0, vall[6])
                page8.entry5.insert(0, vall[3])
                page8.entry6.insert(0, vall[5])
                e_update.mainloop()
            elif len(self.sel)==0:
                messagebox.showerror("Error","Please select an employee to update.")
            else:
                messagebox.showerror("Error","Can only update one employee at a time.")

            


        def add_emp(self):
            global e_add
            e_add = Toplevel()
            page6 = add_employee(e_add)
            page6.time()
            e_add.protocol("WM_DELETE_WINDOW", self.ex)
            e_add.mainloop()


        def ex(self):
            e_add.destroy()
            self.tree.delete(*self.tree.get_children())
            self.DisplayData()   

        def ex2(self):
            e_update.destroy()
            self.tree.delete(*self.tree.get_children())
            self.DisplayData()  



        def time(self):
            string = strftime("%H:%M:%S %p")
            self.clock.config(text=string)
            self.clock.after(1000, self.time)

        def Exit(self):
            sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=emp)
            if sure == True:
                emp.destroy()
                adm.deiconify()


        def Logout(self):
            sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
            if sure == True:
                emp.destroy()
                second.deiconify()
                
                page1.entry1.delete(0, END)
                page1.entry2.delete(0, END)


    class add_employee:
        def __init__(self, top=None):
            top.geometry("1366x768")
            top.resizable(0, 0)
            top.title("Add Employee")

            self.label1 = Label(e_add)
            self.label1.place(relx=0, rely=0, width=1366, height=768)
            self.img = PhotoImage(file="real-mart-master/images/add_employee.png")
            self.label1.configure(image=self.img)

            self.clock = Label(e_add)
            self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
            self.clock.configure(font="-family {Poppins Light} -size 12")
            self.clock.configure(foreground="#000000")
            self.clock.configure(background="#ffffff")

            self.r1 = e_add.register(self.testint)
            self.r2 = e_add.register(self.testchar)

            self.entry1 = Entry(e_add)
            self.entry1.place(relx=0.132, rely=0.296, width=374, height=30)
            self.entry1.configure(font="-family {Poppins} -size 12")
            self.entry1.configure(relief="flat")
            

            self.entry2 = Entry(e_add)
            self.entry2.place(relx=0.132, rely=0.413, width=374, height=30)
            self.entry2.configure(font="-family {Poppins} -size 12")
            self.entry2.configure(relief="flat")
            self.entry2.configure(validate="key", validatecommand=(self.r1, "%P"))

            self.entry3 = Entry(e_add)
            self.entry3.place(relx=0.132, rely=0.529, width=374, height=30)
            self.entry3.configure(font="-family {Poppins} -size 12")
            self.entry3.configure(relief="flat")
            self.entry3.configure(validate="key", validatecommand=(self.r1, "%P"))

            self.entry4 = Entry(e_add)
            self.entry4.place(relx=0.527, rely=0.296, width=374, height=30)
            self.entry4.configure(font="-family {Poppins} -size 12")
            self.entry4.configure(relief="flat")
            self.entry4.configure(validate="key", validatecommand=(self.r2, "%P"))

            self.entry5 = Entry(e_add)
            self.entry5.place(relx=0.527, rely=0.413, width=374, height=30)
            self.entry5.configure(font="-family {Poppins} -size 12")
            self.entry5.configure(relief="flat")

            self.entry6 = Entry(e_add)
            self.entry6.place(relx=0.527, rely=0.529, width=374, height=30)
            self.entry6.configure(font="-family {Poppins} -size 12")
            self.entry6.configure(relief="flat")
            self.entry6.configure(show="*")

            self.button1 = Button(e_add)
            self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
            self.button1.configure(relief="flat")
            self.button1.configure(overrelief="flat")
            self.button1.configure(activebackground="orange")
            self.button1.configure(cursor="hand2")
            self.button1.configure(foreground="#ffffff")
            self.button1.configure(background="orange")
            self.button1.configure(font="-family {Poppins SemiBold} -size 14")
            self.button1.configure(borderwidth="0")
            self.button1.configure(text="""ADD""")
            self.button1.configure(command=self.add)

            self.button2 = Button(e_add)
            self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
            self.button2.configure(relief="flat")
            self.button2.configure(overrelief="flat")
            self.button2.configure(activebackground="orange")
            self.button2.configure(cursor="hand2")
            self.button2.configure(foreground="#ffffff")
            self.button2.configure(background="orange")
            self.button2.configure(font="-family {Poppins SemiBold} -size 14")
            self.button2.configure(borderwidth="0")
            self.button2.configure(text="""CLEAR""")
            self.button2.configure(command=self.clearr)



        def testint(self, val):
            if val.isdigit():
                return True
            elif val == "":
                return True
            return False

        def testchar(self, val):
            if val.isalpha():
                return True
            elif val == "":
                return True
            return False

        def time(self):
            string = strftime("%H:%M:%S %p")
            self.clock.config(text=string)
            self.clock.after(1000, self.time)

        
        def add(self):
            ename = self.entry1.get()
            econtact = self.entry2.get()
            eaddhar = self.entry3.get()
            edes = self.entry4.get()
            eadd = self.entry5.get()
            epass = self.entry6.get()

            if ename.strip():
                if valid_phone(econtact):
                    if valid_aadhar(eaddhar):
                        if edes:
                            if eadd:
                                if epass:
                                    emp_id = random_emp_id(7)
                                    insert = (
                                                "INSERT INTO employee(emp_id, name, contact_num, address, aadhar_num, password, designation) VALUES(?,?,?,?,?,?,?)"
                                            )
                                    cur.execute(insert, [emp_id, ename, econtact, eadd, eaddhar, epass, edes])
                                    db.commit()
                                    messagebox.showinfo("Success!!", "Employee ID: {} successfully added in database.".format(emp_id), parent=e_add)
                                    self.clearr()
                                else:
                                    messagebox.showerror("Oops!", "Please enter a password.", parent=e_add)
                            else:
                                messagebox.showerror("Oops!", "Please enter address.", parent=e_add)
                        else:
                            messagebox.showerror("Oops!", "Please enter designation.", parent=e_add)
                    else:
                        messagebox.showerror("Oops!", "Invalid Aadhar number.", parent=e_add)
                else:
                    messagebox.showerror("Oops!", "Invalid phone number.", parent=e_add)
            else:
                messagebox.showerror("Oops!", "Please enter employee name.", parent=e_add)

        def clearr(self):
            self.entry1.delete(0, END)
            self.entry2.delete(0, END)
            self.entry3.delete(0, END)
            self.entry4.delete(0, END)
            self.entry5.delete(0, END)
            self.entry6.delete(0, END)


    class Update_Employee:
        def __init__(self, top=None):
            top.geometry("1366x768")
            top.resizable(0, 0)
            top.title("Update Employee")

            self.label1 = Label(e_update)
            self.label1.place(relx=0, rely=0, width=1366, height=768)
            self.img = PhotoImage(file="real-mart-master/images/update_employee.png")
            self.label1.configure(image=self.img)

            self.clock = Label(e_update)
            self.clock.place(relx=0.84, rely=0.065, width=102, height=36)
            self.clock.configure(font="-family {Poppins Light} -size 12")
            self.clock.configure(foreground="#000000")
            self.clock.configure(background="#ffffff")

            self.r1 = e_update.register(self.testint)
            self.r2 = e_update.register(self.testchar)

            self.entry1 = Entry(e_update)
            self.entry1.place(relx=0.132, rely=0.296, width=374, height=30)
            self.entry1.configure(font="-family {Poppins} -size 12")
            self.entry1.configure(relief="flat")
            

            self.entry2 = Entry(e_update)
            self.entry2.place(relx=0.132, rely=0.413, width=374, height=30)
            self.entry2.configure(font="-family {Poppins} -size 12")
            self.entry2.configure(relief="flat")
            self.entry2.configure(validate="key", validatecommand=(self.r1, "%P"))

            self.entry3 = Entry(e_update)
            self.entry3.place(relx=0.132, rely=0.529, width=374, height=30)
            self.entry3.configure(font="-family {Poppins} -size 12")
            self.entry3.configure(relief="flat")
            self.entry3.configure(validate="key", validatecommand=(self.r1, "%P"))

            self.entry4 = Entry(e_update)
            self.entry4.place(relx=0.527, rely=0.296, width=374, height=30)
            self.entry4.configure(font="-family {Poppins} -size 12")
            self.entry4.configure(relief="flat")
            self.entry4.configure(validate="key", validatecommand=(self.r2, "%P"))

            self.entry5 = Entry(e_update)
            self.entry5.place(relx=0.527, rely=0.413, width=374, height=30)
            self.entry5.configure(font="-family {Poppins} -size 12")
            self.entry5.configure(relief="flat")

            self.entry6 = Entry(e_update)
            self.entry6.place(relx=0.527, rely=0.529, width=374, height=30)
            self.entry6.configure(font="-family {Poppins} -size 12")
            self.entry6.configure(relief="flat")
            self.entry6.configure(show="*")

            self.button1 = Button(e_update)
            self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
            self.button1.configure(relief="flat")
            self.button1.configure(overrelief="flat")
            self.button1.configure(activebackground="orange")
            self.button1.configure(cursor="hand2")
            self.button1.configure(foreground="#ffffff")
            self.button1.configure(background="orange")
            self.button1.configure(font="-family {Poppins SemiBold} -size 14")
            self.button1.configure(borderwidth="0")
            self.button1.configure(text="""UPDATE""")
            self.button1.configure(command=self.update)

            self.button2 = Button(e_update)
            self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
            self.button2.configure(relief="flat")
            self.button2.configure(overrelief="flat")
            self.button2.configure(activebackground="orange")
            self.button2.configure(cursor="hand2")
            self.button2.configure(foreground="#ffffff")
            self.button2.configure(background="orange")
            self.button2.configure(font="-family {Poppins SemiBold} -size 14")
            self.button2.configure(borderwidth="0")
            self.button2.configure(text="""CLEAR""")
            self.button2.configure(command=self.clearr)

        def update(self):
            ename = self.entry1.get()
            econtact = self.entry2.get()
            eaddhar = self.entry3.get()
            edes = self.entry4.get()
            eadd = self.entry5.get()
            epass = self.entry6.get()

            if ename.strip():
                if valid_phone(econtact):
                    if valid_aadhar(eaddhar):
                        if edes:
                            if eadd:
                                if epass:
                                    emp_id = vall[0]
                                    update = (
                                                "UPDATE employee SET name = ?, contact_num = ?, address = ?, aadhar_num = ?, password = ?, designation = ? WHERE emp_id = ?"
                                            )
                                    cur.execute(update, [ename, econtact, eadd, eaddhar, epass, edes, emp_id])
                                    db.commit()
                                    messagebox.showinfo("Success!!", "Employee ID: {} successfully updated in database.".format(emp_id), parent=e_update)
                                    vall.clear()
                                    page5.tree.delete(*page5.tree.get_children())
                                    page5.DisplayData()
                                    Employee.sel.clear()
                                    e_update.destroy()
                                else:
                                    messagebox.showerror("Oops!", "Please enter a password.", parent=e_add)
                            else:
                                messagebox.showerror("Oops!", "Please enter address.", parent=e_add)
                        else:
                            messagebox.showerror("Oops!", "Please enter designation.", parent=e_add)
                    else:
                        messagebox.showerror("Oops!", "Invalid Aadhar number.", parent=e_add)
                else:
                    messagebox.showerror("Oops!", "Invalid phone number.", parent=e_add)
            else:
                messagebox.showerror("Oops!", "Please enter employee name.", parent=e_add)


        def clearr(self):
            self.entry1.delete(0, END)
            self.entry2.delete(0, END)
            self.entry3.delete(0, END)
            self.entry4.delete(0, END)
            self.entry5.delete(0, END)
            self.entry6.delete(0, END)



        def testint(self, val):
            if val.isdigit():
                return True
            elif val == "":
                return True
            return False

        def testchar(self, val):
            if val.isalpha():
                return True
            elif val == "":
                return True
            return False

        def time(self):
            string = strftime("%H:%M:%S %p")
            self.clock.config(text=string)
            self.clock.after(1000, self.time)


            

    class Invoice:
        def __init__(self, top=None):
            top.geometry("1366x768")
            top.resizable(0, 0)
            top.title("Invoices")

            self.label1 = Label(invoice)
            self.label1.place(relx=0, rely=0, width=1366, height=768)
            self.img = PhotoImage(file="real-mart-master/images/invoices.png")
            self.label1.configure(image=self.img)

            self.message = Label(invoice)
            self.message.place(relx=0.046, rely=0.055, width=136, height=30)
            self.message.configure(font="-family {Poppins} -size 10")
            self.message.configure(foreground="#000000")
            self.message.configure(background="#ffffff")
            self.message.configure(text="""ADMIN""")
            self.message.configure(anchor="w")

            self.clock = Label(invoice)
            self.clock.place(relx=0.9, rely=0.065, width=102, height=36)
            self.clock.configure(font="-family {Poppins Light} -size 12")
            self.clock.configure(foreground="#000000")
            self.clock.configure(background="#ffffff")

            self.entry1 = Entry(invoice)
            self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
            self.entry1.configure(font="-family {Poppins} -size 12")
            self.entry1.configure(relief="flat")

            self.button1 = Button(invoice)
            self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
            self.button1.configure(relief="flat")
            self.button1.configure(overrelief="flat")
            self.button1.configure(activebackground="orange")
            self.button1.configure(cursor="hand2")
            self.button1.configure(foreground="#ffffff")
            self.button1.configure(background="orange")
            self.button1.configure(font="-family {Poppins SemiBold} -size 10")
            self.button1.configure(borderwidth="0")
            self.button1.configure(text="""Search""")
            self.button1.configure(command=self.search_inv)

            self.button2 = Button(invoice)
            self.button2.place(relx=0.035, rely=0.106, width=76, height=23)
            self.button2.configure(relief="flat")
            self.button2.configure(overrelief="flat")
            self.button2.configure(activebackground="orange")
            self.button2.configure(cursor="hand2")
            self.button2.configure(foreground="#ffffff")
            self.button2.configure(background="orange")
            self.button2.configure(font="-family {Poppins SemiBold} -size 12")
            self.button2.configure(borderwidth="0")
            self.button2.configure(text="""Logout""")
            self.button2.configure(command=self.Logout)

            self.button3 = Button(invoice)
            self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
            self.button3.configure(relief="flat")
            self.button3.configure(overrelief="flat")
            self.button3.configure(activebackground="orange")
            self.button3.configure(cursor="hand2")
            self.button3.configure(foreground="#ffffff")
            self.button3.configure(background="orange")
            self.button3.configure(font="-family {Poppins SemiBold} -size 12")
            self.button3.configure(borderwidth="0")
            self.button3.configure(text="""DELETE INVOICE""")
            self.button3.configure(command=self.delete_invoice)

            self.button4 = Button(invoice)
            self.button4.place(relx=0.135, rely=0.885, width=76, height=23)
            self.button4.configure(relief="flat")
            self.button4.configure(overrelief="flat")
            self.button4.configure(activebackground="orange")
            self.button4.configure(cursor="hand2")
            self.button4.configure(foreground="#ffffff")
            self.button4.configure(background="orange")
            self.button4.configure(font="-family {Poppins SemiBold} -size 12")
            self.button4.configure(borderwidth="0")
            self.button4.configure(text="""EXIT""")
            self.button4.configure(command=self.Exit)

            self.scrollbarx = Scrollbar(invoice, orient=HORIZONTAL)
            self.scrollbary = Scrollbar(invoice, orient=VERTICAL)
            self.tree = ttk.Treeview(invoice)
            self.tree.place(relx=0.307, rely=0.203, width=880, height=550)
            self.tree.configure(
                yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
            )
            self.tree.configure(selectmode="extended")

            self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
            self.tree.bind("<Double-1>", self.double_tap)

            self.scrollbary.configure(command=self.tree.yview)
            self.scrollbarx.configure(command=self.tree.xview)

            self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
            self.scrollbarx.place(relx=0.307, rely=0.924, width=884, height=22)

            self.tree.configure(
                columns=(
                    "Bill Number",
                    "Date",
                    "Customer Name",
                    "Customer Phone No.",
                )
            )

            self.tree.heading("Bill Number", text="Bill Number", anchor=W)
            self.tree.heading("Date", text="Date", anchor=W)
            self.tree.heading("Customer Name", text="Customer Name", anchor=W)
            self.tree.heading("Customer Phone No.", text="Customer Phone No.", anchor=W)
            

            self.tree.column("#0", stretch=NO, minwidth=0, width=0)
            self.tree.column("#1", stretch=NO, minwidth=0, width=219)
            self.tree.column("#2", stretch=NO, minwidth=0, width=219)
            self.tree.column("#3", stretch=NO, minwidth=0, width=219)
            self.tree.column("#4", stretch=NO, minwidth=0, width=219)
            

            self.DisplayData()


        def DisplayData(self):
            cur.execute("SELECT * FROM bill")
            fetch = cur.fetchall()
            for data in fetch:
                self.tree.insert("", "end", values=(data))

        sel = []
        def on_tree_select(self, Event):
            self.sel.clear()
            for i in self.tree.selection():
                if i not in self.sel:
                    self.sel.append(i)

        def double_tap(self, Event):
            item = self.tree.identify('item', Event.x, Event.y)
            global bill_num
            bill_num = self.tree.item(item)['values'][0]
            

            global bill
            bill = Toplevel()
            pg = open_bill(bill)
            #bill.protocol("WM_DELETE_WINDOW", exitt)
            bill.mainloop()

            


        def delete_invoice(self):
            val = []
            to_delete = []

            if len(self.sel)!=0:
                sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected invoice(s)?", parent=invoice)
                if sure == True:
                    for i in self.sel:
                        for j in self.tree.item(i)["values"]:
                            val.append(j)
                    
                    for j in range(len(val)):
                        if j%5==0:
                            to_delete.append(val[j])
                    
                    for k in to_delete:
                        delete = "DELETE FROM bill WHERE bill_no = ?"
                        cur.execute(delete, [k])
                        db.commit()

                    messagebox.showinfo("Success!!", "Invoice(s) deleted from database.", parent=invoice)
                    self.sel.clear()
                    self.tree.delete(*self.tree.get_children())

                    self.DisplayData()
            else:
                messagebox.showerror("Error!!","Please select an invoice", parent=invoice)

        def search_inv(self):
            val = []
            for i in self.tree.get_children():
                val.append(i)
                for j in self.tree.item(i)["values"]:
                    val.append(j)

            to_search = self.entry1.get()
            for search in val:
                if search==to_search:
                    self.tree.selection_set(val[val.index(search)-1])
                    self.tree.focus(val[val.index(search)-1])
                    messagebox.showinfo("Success!!", "Bill Number: {} found.".format(self.entry1.get()), parent=invoice)
                    break
            else: 
                messagebox.showerror("Oops!!", "Bill NUmber: {} not found.".format(self.entry1.get()), parent=invoice)


        def Logout(self):
            sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
            if sure == True:
                invoice.destroy()
                second.deiconify()
                page1.entry1.delete(0, END)
                page1.entry2.delete(0, END)

        def time(self):
            string = strftime("%H:%M:%S %p")
            self.clock.config(text=string)
            self.clock.after(1000, self.time)

        def Exit(self):
            sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=invoice)
            if sure == True:
                invoice.destroy()
                adm.deiconify()


    class open_bill:
        def __init__(self, top=None):
            
            top.geometry("765x488")
            top.resizable(0, 0)
            top.title("Bill")

            self.label1 = Label(bill)
            self.label1.place(relx=0, rely=0, width=765, height=488)
            self.img = PhotoImage(file="real-mart-master/images/bill.png")
            self.label1.configure(image=self.img)
            
            self.name_message = Text(bill)
            self.name_message.place(relx=0.178, rely=0.205, width=176, height=30)
            self.name_message.configure(font="-family {Podkova} -size 10")
            self.name_message.configure(borderwidth=0)
            self.name_message.configure(background="#ffffff")

            self.num_message = Text(bill)
            self.num_message.place(relx=0.854, rely=0.205, width=90, height=30)
            self.num_message.configure(font="-family {Podkova} -size 10")
            self.num_message.configure(borderwidth=0)
            self.num_message.configure(background="#ffffff")

            self.bill_message = Text(bill)
            self.bill_message.place(relx=0.150, rely=0.243, width=176, height=26)
            self.bill_message.configure(font="-family {Podkova} -size 10")
            self.bill_message.configure(borderwidth=0)
            self.bill_message.configure(background="#ffffff")

            self.bill_date_message = Text(bill)
            self.bill_date_message.place(relx=0.780, rely=0.243, width=90, height=26)
            self.bill_date_message.configure(font="-family {Podkova} -size 10")
            self.bill_date_message.configure(borderwidth=0)
            self.bill_date_message.configure(background="#ffffff")


            self.Scrolledtext1 = tkst.ScrolledText(top)
            self.Scrolledtext1.place(relx=0.044, rely=0.41, width=695, height=284)
            self.Scrolledtext1.configure(borderwidth=0)
            self.Scrolledtext1.configure(font="-family {Podkova} -size 8")
            self.Scrolledtext1.configure(state="disabled")

            find_bill = "SELECT * FROM bill WHERE bill_no = ?"
            cur.execute(find_bill, [bill_num])
            results = cur.fetchall()
            if results:
                self.name_message.insert(END, results[0][2])
                self.name_message.configure(state="disabled")
        
                self.num_message.insert(END, results[0][3])
                self.num_message.configure(state="disabled")
        
                self.bill_message.insert(END, results[0][0])
                self.bill_message.configure(state="disabled")

                self.bill_date_message.insert(END, results[0][1])
                self.bill_date_message.configure(state="disabled")

                self.Scrolledtext1.configure(state="normal")
                self.Scrolledtext1.insert(END, results[0][4])
                self.Scrolledtext1.configure(state="disabled")

    page1 = login_page(second)
    second.bind("<Return>", login_page.login)
    second.mainloop()


    
    
    
    
    
    
# def emp():
#     root.withdraw()
#     os.system("employee.py")
#     root.deiconify()




button1 = Button(root)
button1.place(relx=0.316,rely=0.446, width=146, height=90)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = PhotoImage(file="real-mart-master/images/1.png")
button1.configure(image=img2)
button1.configure(command=emp)

button2 = Button(root)
button2.place(relx=0.566,rely=0.448, width=146, height=90)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = PhotoImage(file="real-mart-master/images/2.png")
button2.configure(image=img3)
button2.configure(command=adm)

# root.mainloop()
root.mainloop()
