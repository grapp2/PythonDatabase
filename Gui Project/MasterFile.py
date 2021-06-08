'''
Created on 1/15/2021
Master File
@author: Greg Rapp
'''
import PIL
try:
    import mysql.connector
    import Tkinter
    import ttk
except ImportError:
    import tkinter as Tkinter
    from PIL import ImageTk, Image
    from tkinter import *
    import tkinter.ttk as ttk
username = "root"
password = "VRSCm1998!"
my_connect = mysql.connector.connect(
    host="localhost",
    user=username,
    passwd=password,
    database="pneumabase"
)
my_curs = my_connect.cursor()

class SeaofBTCapp(Tkinter.Tk):
    def __init__(self, *args, **kwargs):
        a = Tkinter.Frame.__init__(self, *args, **kwargs)
        container = Tkinter.Frame(a, bg="lavender")
        container.grid_rowconfigure(0, weight=0)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for f in (Company, ):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=1, column=0)
        self.show_frame(Company)
        container.update()

        container.grid(row=0, column=0, sticky="nsew")


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Company(Tkinter.Frame):
    '''
    classdocs
    '''
    def __init__(self, parent, controller):
        '''
        Constructor
        '''
        Tkinter.Frame.__init__(self, parent)
        header = Tkinter.Frame(parent, height=100, bg="white")
        home_frame = Tkinter.Frame(parent)
        pneumalogo = PIL.Image.open("C:/Users/GreggRapp/PycharmProjects/pythonProject/pneumalogo.png")
        resized = pneumalogo.resize((150, 75), PIL.Image.ANTIALIAS)
        resized_pic = ImageTk.PhotoImage(resized)
        home_button = Tkinter.Button(home_frame, text="",
                                     image=resized_pic, compound=LEFT, activebackground="silver", bg="white",
                                     borderwidth=0
                                     )
        home_button.image = resized_pic
        home_button.grid(row=0, column=0, sticky=Tkinter.W)
        header.grid(row=0, column=0, sticky="new")
        home_frame.grid(row=0, column=0, sticky="nw", padx=15, pady=(15,0))
        self.winfo_toplevel().title("Companies")
        self.winfo_toplevel().grid_rowconfigure(0, weight=1)
        self.winfo_toplevel().grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(2, weight=1)
        # initialize frames
        button_frame = Tkinter.Frame(parent, bg="Lavender")
        tree_frame = Tkinter.Frame(parent, bg="Lavender")
        button_frame.grid_columnconfigure(4, weight=1)
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid(row=1, column=0, sticky="new")
        tree_frame.grid(row=2, column=0, sticky="nsew")

        # fill button_frames with attributes
        submit_button = Tkinter.Button(button_frame, text="Insert", command=self.insert_popup)
        delete_button = Tkinter.Button(button_frame, text="Delete Selected", command=self.confirm_popup)
        refreshpic = PIL.Image.open("C:/Users/GreggRapp/PycharmProjects/pythonProject/icon_refresh.png")
        resized = refreshpic.resize((20, 20), PIL.Image.ANTIALIAS)
        resized_pic = ImageTk.PhotoImage(resized)
        refresh_button = Tkinter.Button(button_frame, text="", command=self.update_table, image=resized_pic,
                                        compound=LEFT)
        refresh_button.image = resized_pic

        modify_button = Tkinter.Button(button_frame, text="Update Record",
                                             command=self.modify_popup)
        # Place buttons in button frame
        submit_button.grid(row=1, column=0, sticky=Tkinter.W, padx=20, pady=15)
        delete_button.grid(row=1, column=1, sticky=Tkinter.W, padx=20, pady=15)
        modify_button.grid(row=1, column=3, sticky=Tkinter.W, padx=20, pady=15)
        refresh_button.grid(row=1, column=4, sticky="e", padx=20, pady=15)

        # declare style for treeview
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#d3d3d3", foreground="red", rowheight=25,
                        fieldbackground="#d3d3d3")
        style.map('Treeview', background=[('selected', 'black')])

        # Scrollbar
        tree_scroll = Tkinter.Scrollbar(tree_frame)
        # Set treeview
        tree = ttk.Treeview(tree_frame, columns=('Company ID', 'Company', 'Type', 'Country', 'Address'),
                            yscrollcommand=tree_scroll.set)
        tree_scroll.config(command=tree.yview)
        # build tree view
        tree.heading('Company ID', text='Company ID', anchor=Tkinter.CENTER)
        tree.heading('Company', text='Company', anchor=Tkinter.CENTER)
        tree.heading('Type', text='Type', anchor=Tkinter.CENTER)
        tree.heading('Country', text='Country', anchor=Tkinter.CENTER)
        tree.heading('Address', text='Address', anchor=Tkinter.CENTER)

        tree.column('#0', width=0, stretch=Tkinter.NO)
        tree.column('Company ID', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        tree.column('Company', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=150)
        tree.column('Type', width=100, stretch=Tkinter.NO, anchor=Tkinter.CENTER)
        tree.column('Country', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        tree.column('Address', width=400, stretch=Tkinter.YES, anchor=Tkinter.CENTER)
        tree.tag_configure('oddrow', background="white")
        tree.tag_configure('evenrow', background="lightblue")
        tree_scroll.grid(row=0, column=1, sticky="ns", padx=(0,15), pady=(0, 15))
        tree.grid(row=0, column=0, sticky="nsew", padx=(15,0), pady=(0,15))
        self.parent = parent
        self.treeview = tree
        self.button_frame_ref = button_frame
        self.tree_frame_ref = tree_frame
        self.confirmation = False
        self.field_data = ["" for i in range(8)]
        self.update_table()

    # Creates popup after clicking update button
    def modify_popup(self):
        if len(self.treeview.selection()) == 1:
            popup = Tkinter.Tk()
            popup.title("Modify Data")
            field_frame = Tkinter.Frame(popup)
            field_frame.pack()
            company_label = Tkinter.Label(field_frame, text="Name of Company:")
            company_entry = Tkinter.Entry(field_frame)
            type_options = ["<Select>",
                            "Shipper",
                            "Manufacturer",
                            "Processor",
                            "Home"]
            explanation_label = Tkinter.Label(field_frame, text="Update company information\n* entries mandatory")
            type_label = Tkinter.Label(field_frame, text="*Company Type:")
            type_entry = ttk.Combobox(field_frame, value=type_options)
            type_entry.current(0)
            country_label = Tkinter.Label(field_frame, text="Country:")
            country_entry = Tkinter.Entry(field_frame)
            address1_label = Tkinter.Label(field_frame, text="Address 1:")
            address1_entry = Tkinter.Entry(field_frame)
            address2_label = Tkinter.Label(field_frame, text="Address 2:")
            address2_entry = Tkinter.Entry(field_frame)
            city_label = Tkinter.Label(field_frame, text="City")
            city_entry = Tkinter.Entry(field_frame)
            state_label = Tkinter.Label(field_frame, text="State")
            state_entry = Tkinter.Entry(field_frame)
            zip_label = Tkinter.Label(field_frame, text="Zip:")
            zip_entry = Tkinter.Entry(field_frame)

            # inserts data from textbox to server then updates table
            def modify_record():
                record = self.treeview.selection()
                if len(record) == 1:
                    string = self.find_in_company(self.treeview.item(record, "values")[0])
                    add_boxtext(string[0])
                    self.modify_index = int(string[0][0])
                else:
                    pass

            def collect_text():
                string = ["" for i in range(8)]
                string[5] = company_entry.get()
                string[7] = type_entry.get()
                string[4] = country_entry.get()
                string[0] = address1_entry.get()
                string[1] = address2_entry.get()
                string[6] = city_entry.get()
                string[2] = state_entry.get()
                string[3] = zip_entry.get()
                self.field_data = string

            def add_boxtext(string):
                company_entry.insert(0, str(string[6]))
                cur_type = str(string[8])
                switcher = {
                    "<Select>": 0,
                    "Shipper": 1,
                    "Manufacturer": 2,
                    "Processor": 3,
                    "Home": 4
                }
                type_entry.current(switcher.get(cur_type, string[8]))
                country_entry.insert(0, str(string[5]))
                address1_entry.insert(0, str(string[1]))
                address2_entry.insert(0, str(string[2]))
                city_entry.insert(0, str(string[7]))
                state_entry.insert(0, str(string[3]))
                zip_entry.insert(0, str(string[4]))

            def save_modification():
                try:
                    index = self.modify_index
                    if index != None:
                        collect_text()
                        data = self.field_data
                        sql = "update company set Address1 = %s, " \
                              "Address2 = %s, State = %s, Zip = %s, Country = %s," \
                              "Name = %s, City = %s, CompanyType = %s" \
                              "where Company_ID = %s;"
                        for i in range(len(data)):
                            if data[i] == "" or data[i] == "None" or data[i] == "<Select>":
                                data[i] = None
                        val = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], index)
                        my_curs.execute(sql, val)
                        my_connect.commit()
                        self.update_table()
                        self.modify_index = None
                        popup.destroy()
                    else:
                        pass
                except mysql.connector.Error as e:
                    self.error_popup(e)

            save_button = Tkinter.Button(field_frame, text="Submit", command=save_modification)
            cancel_button = Tkinter.Button(field_frame, text="Cancel", command=popup.destroy)
            explanation_label.grid(row=0, column=0, sticky=Tkinter.NSEW, padx=15, pady=15, columnspan=2)
            company_label.grid(row=1, column=0, sticky=Tkinter.W, padx=15)
            company_entry.grid(row=1, column=1, sticky=Tkinter.EW, padx=15)
            type_label.grid(row=2, column=0, sticky=Tkinter.W, padx=15)
            type_entry.grid(row=2, column=1, sticky=Tkinter.EW, padx=15)
            country_label.grid(row=3, column=0, sticky=Tkinter.W, padx=15)
            country_entry.grid(row=3, column=1, sticky=Tkinter.EW, padx=15)
            address1_label.grid(row=4, column=0, sticky=Tkinter.W, padx=15)
            address1_entry.grid(row=4, column=1, sticky=Tkinter.EW, padx=15)
            address2_label.grid(row=5, column=0, sticky=Tkinter.W, padx=15)
            address2_entry.grid(row=5, column=1, sticky=Tkinter.EW, padx=15)
            city_label.grid(row=6, column=0, sticky=Tkinter.W, padx=15)
            city_entry.grid(row=6, column=1, sticky=Tkinter.EW, padx=15)
            state_label.grid(row=7, column=0, sticky=Tkinter.W, padx=15)
            state_entry.grid(row=7, column=1, sticky=Tkinter.EW, padx=15)
            zip_label.grid(row=8, column=0, sticky=Tkinter.W, padx=15)
            zip_entry.grid(row=8, column=1, sticky=Tkinter.EW, padx=15)
            save_button.grid(row=9, column=1, sticky=Tkinter.E, padx=15, pady=10)
            cancel_button.grid(row=9, column=0, sticky=Tkinter.W, padx=15, pady=10)
            modify_record()
        else:
            pass

    # Creates popup after error appears
    def error_popup(self, e):
        popup = Tkinter.Tk()
        popup.title("Error")
        message = Tkinter.Label(popup, text="", fg='red')
        close = Tkinter.Button(popup, text="Close", command=popup.destroy)
        message['text'] = "Error " + str(e)
        message.pack(pady=(15, 7), padx=15)
        close.pack(pady=(7, 15))

    # returns record[row][column] containing indexed values within company
    def find_in_company(self, index):
        try:
            sql = "select * from company where Company_ID = %s;"
            val = (index, )
            my_curs.execute(sql, val)
            return my_curs.fetchall()
        except mysql.connector.Error as e:
            self.error_popup(e)

    # inserts data from table to treeview
    def update_table(self):
        try:
            my_curs.execute("select * from company order by CompanyType, Name ASC")
        except mysql.connector.Error as e:
            self.error_popup(e)
        string = ["" for i in range(9)]
        size = 0
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        for company in my_curs:
            val = ""
            string[0] = str(company[0])
            string[1] = str(company[6])
            string[2] = str(company[8])
            string[3] = str(company[5])
            string[4] = str(company[1])
            string[5] = str(company[2])
            string[6] = str(company[7])
            string[7] = str(company[3])
            string[8] = str(company[4])

            for i in range(4, len(string)):
                a = self.checkMoreEntries(string, i)
                if string[i] != "None":
                    if a:
                        val += string[i] + ", "
                    elif not a:
                        val += string[i]
            size += 1
            if size % 2 == 0:
                self.treeview.insert('', 'end', iid=company[0],
                                     values=(string[0], string[1], string[2], string[3], val),
                                     tags=('evenrow',)
                                     )
            else:
                self.treeview.insert('', 'end', iid=company[0],
                                     values=(string[0], string[1], string[2], string[3], val),
                                     tags=('oddrow',)
                                     )

    # Checks to see if there are more not null entries in arr
    def checkMoreEntries(self, arr, index):
        if index == len(arr):
            return False
        else:
            for i in range(index+1, len(arr)):
                if arr[i] != "None":
                    return True
            return False

    # Creates a popup to insert data into database
    def insert_popup(self):
        popup = Tkinter.Tk()
        popup.title("Insert Data")
        field_frame = Tkinter.Frame(popup)
        field_frame.pack()

        # Create type combo box entry and label
        type_options = ["<Select>",
                        "Shipper",
                        "Manufacturer",
                        "Processor",
                        "Home"]
        type_label = Tkinter.Label(field_frame, text="*Company Type:")
        type_entry = ttk.Combobox(field_frame, value=type_options)
        type_entry.current(0)

        # Initialize other entries and labels
        explanation_label = Tkinter.Label(field_frame, text="Enter in company information\n* entries mandatory")
        company_label = Tkinter.Label(field_frame, text="*Name of Company:")
        company_entry = Tkinter.Entry(field_frame)
        country_label = Tkinter.Label(field_frame, text=" Country:")
        country_entry = Tkinter.Entry(field_frame)
        address1_label = Tkinter.Label(field_frame, text=" Address 1:")
        address1_entry = Tkinter.Entry(field_frame)
        address2_label = Tkinter.Label(field_frame, text=" Address 2:")
        address2_entry = Tkinter.Entry(field_frame)
        city_label = Tkinter.Label(field_frame, text=" City")
        city_entry = Tkinter.Entry(field_frame)
        state_label = Tkinter.Label(field_frame, text=" State")
        state_entry = Tkinter.Entry(field_frame)
        zip_label = Tkinter.Label(field_frame, text=" Zip:")
        zip_entry = Tkinter.Entry(field_frame)
        explanation_label.grid(row=0, column=0, sticky=Tkinter.NSEW, columnspan=2, padx=15, pady=15)
        company_label.grid(row=1, column=0, sticky=Tkinter.E, padx=(15, 8))
        company_entry.grid(row=1, column=1, sticky=Tkinter.EW, padx=(8, 15))
        type_label.grid(row=2, column=0, sticky=Tkinter.E, padx=(15, 8))
        type_entry.grid(row=2, column=1, sticky=Tkinter.EW, padx=(8, 15))
        country_label.grid(row=3, column=0, sticky=Tkinter.E, padx=(15, 8))
        country_entry.grid(row=3, column=1, sticky=Tkinter.EW, padx=(8, 15))
        address1_label.grid(row=4, column=0, sticky=Tkinter.E, padx=(15, 8))
        address1_entry.grid(row=4, column=1, sticky=Tkinter.EW, padx=(8, 15))
        address2_label.grid(row=5, column=0, sticky=Tkinter.E, padx=(15, 8))
        address2_entry.grid(row=5, column=1, sticky=Tkinter.EW, padx=(8, 15))
        city_label.grid(row=6, column=0, sticky=Tkinter.E, padx=(15, 8))
        city_entry.grid(row=6, column=1, sticky=Tkinter.EW, padx=(8, 15))
        state_label.grid(row=7, column=0, sticky=Tkinter.E, padx=(15, 8))
        state_entry.grid(row=7, column=1, sticky=Tkinter.EW, padx=(8, 15))
        zip_label.grid(row=8, column=0, sticky=Tkinter.E, padx=(15, 8))
        zip_entry.grid(row=8, column=1, sticky=Tkinter.EW, padx=(8, 15))

        def delete_boxtext():
            company_entry.delete(0, 'end')
            type_entry.current(0)
            country_entry.delete(0, 'end')
            address1_entry.delete(0, 'end')
            address2_entry.delete(0, 'end')
            city_entry.delete(0, 'end')
            state_entry.delete(0, 'end')
            zip_entry.delete(0, 'end')

        def collect_text():
            string = ["" for i in range(8)]
            string[5] = company_entry.get()
            string[7] = type_entry.get()
            string[4] = country_entry.get()
            string[0] = address1_entry.get()
            string[1] = address2_entry.get()
            string[6] = city_entry.get()
            string[2] = state_entry.get()
            string[3] = zip_entry.get()
            self.field_data = string

        # inserts data from textbox to server then updates table
        def insert_data():
            try:
                collect_text()
                strings = self.field_data
                sql = "INSERT INTO company (Address1, Address2, State, Zip, Country, Name, City,CompanyType)VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
                for i in range(len(strings)):  # check for empty strings label as NONE
                    if (strings[i] == "" or strings[i] == "<Select>"):
                        strings[i] = None
                val = (strings[0], strings[1], strings[2], strings[3], strings[4], strings[5], strings[6], strings[7])
                my_curs.execute(sql, val)
                my_connect.commit()
                delete_boxtext()
                self.update_table()
            except mysql.connector.Error as e:
                self.error_popup(e)

        insert_button = Tkinter.Button(field_frame, text="Insert", command=insert_data)
        cancel_button = Tkinter.Button(field_frame, text="Cancel", command=popup.destroy)
        insert_button.grid(row=9, column=1, sticky=Tkinter.E, padx=15, pady=10)
        cancel_button.grid(row=9, column=0, sticky=Tkinter.W, padx=15, pady=10)

    # replace dat1 with dat2, assumes dat1 is in same column as dat2
    def edit_string(self, table, column, dat1, dat2):
        try:
            sql = "UPDATE %s SET %s = '%s' WHERE %s = '%s'"
            val = (table, column, dat2, column, dat1)
            my_curs.execute(sql, val)
            my_connect.commit()
            self.update_table()
        except mysql.connector.Error as e:
            self.error_popup(e)

    # Confirm popupbox activates when delete button is pushed
    def confirm_popup(self):
        if self.treeview.selection():
            popup = Tkinter.Tk()
            popup.title("Confirm Changes")
            # delete string from table
            def deleteCompany():
                try:
                    for record in self.treeview.selection():
                        dat = (str(self.treeview.item(record, "values")[0]),)
                        sql = "DELETE FROM company WHERE Company_ID = %s"
                        val = (dat)
                        my_curs.execute(sql, val)
                        my_connect.commit()
                        self.update_table()
                    popup.destroy()
                except mysql.connector.Error as e:
                    self.error_popup(e)

            frame = Tkinter.Frame(popup)
            label = Tkinter.Label(frame, text="Confirm Changes")
            confirm_button = Tkinter.Button(frame, text="Confirm", command=deleteCompany)
            cancel_button = Tkinter.Button(frame, text="Cancel", command=popup.destroy)
            label.pack(side='top', fill='y', pady=(15,7.5))
            confirm_button.pack(side='left', fill='y',padx=15, pady=(7.5, 15))
            cancel_button.pack(side='right', fill='y',padx=15, pady=(7.5, 15))
            frame.pack()
        else:
            pass

app = SeaofBTCapp()
app.mainloop()