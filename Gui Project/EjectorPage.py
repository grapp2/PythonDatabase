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

TITLE_FONT = ("Verdana", 12, 'bold')
BODY_FONT = ("Verdana", 10)



class SeaofBTCapp(Tkinter.Tk):
    def __init__(self, *args, **kwargs):
        a = Tkinter.Frame.__init__(self, *args, **kwargs)
        container = Tkinter.Frame(a, bg="lavender")
        container.grid_rowconfigure(0, weight=0)
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for f in (Ejector, ):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=1, column=0)
        self.show_frame(Ejector)
        container.update()
        container.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Ejector(Tkinter.Frame):
    '''
    classdocs
    '''
    def __init__(self, parent, controller):
        '''
        Constructor
        '''
        Tkinter.Frame.__init__(self, parent)
        parent.grid_rowconfigure(1, weight=1)
        self.winfo_toplevel().title("New Ejector Shipment")
        self.winfo_toplevel().grid_rowconfigure(0, weight=1)
        self.winfo_toplevel().grid_columnconfigure(0, weight=1)
        parent.winfo_toplevel().geometry('%dx%d+0+0' % (parent.winfo_toplevel().winfo_screenwidth(), parent.winfo_toplevel().winfo_screenheight()))
        header = Tkinter.Frame(parent, bg="white", height=100)
        header.grid_columnconfigure(0, weight=1)
        pneumalogo = PIL.Image.open("C:/Users/GreggRapp/PycharmProjects/pythonProject/pneumalogo.png")
        resized = pneumalogo.resize((150, 75), PIL.Image.ANTIALIAS)
        global logo
        logo = ImageTk.PhotoImage(resized)
        home_button = Tkinter.Button(header, text="",
                                     image=logo, compound=LEFT, activebackground="silver", bg="white",
                                     borderwidth=0
                                     )
        page_label = Tkinter.Label(header, text="New Shipment of Ejectors", font=TITLE_FONT, bg="white")
        home_button.image = logo
        header.grid(row=0, column=0, sticky="new")
        page_label.grid(row=0, column=0, sticky="ns")
        home_button.grid(row=0, column=0, sticky="w", pady=10)

        entity_frame = Tkinter.Frame(parent, bg='Lavender')
        entity_frame.grid_rowconfigure(1, weight=1)
        entity_frame.grid_rowconfigure(2, weight=1)
        entity_frame.grid_columnconfigure(0, weight=1)
        entity_frame.grid_columnconfigure(1, weight=1)
        entity_frame.grid_columnconfigure(2, weight=1)
        entity_frame.grid(row=1, column=0, sticky='nsew', padx=15, pady=15)

        # Setup frames for revision, mesh, ceramic, and ejectors
        insert_frame = Tkinter.Frame(entity_frame, bg="Lavender")
        lot_frame = Tkinter.Frame(entity_frame, bg="Lavender")
        shipment_frame = Tkinter.Frame(entity_frame, bg="Lavender")
        revision_frame = Tkinter.Frame(entity_frame, bg="Lavender")
        mesh_frame = Tkinter.Frame(entity_frame, bg="Lavender")
        ceramic_frame = Tkinter.Frame(entity_frame, bg="Lavender")
        insert_frame.grid(row=0, column=0, columnspan=3, sticky="n", pady=(0,15))
        lot_frame.grid(row=1, column=0, sticky="ew", columnspan=2, padx=(0, 8))
        shipment_frame.grid(row=1, column=1, columnspan=2, sticky="ew", padx=(8, 0))
        revision_frame.grid(row=2, column=0, sticky="nsew", pady=(8, 0), padx=(0, 8))
        mesh_frame.grid(row=2, column=1, sticky="nsew", pady=(8, 0), padx=8)
        ceramic_frame.grid(row=2, column=2, sticky="w", pady=(8, 0), padx=(8, 0))

        lot_fields = Tkinter.Frame(lot_frame, bg="Lavender")
        lot_fields.grid_columnconfigure(4, weight=1)
        shipment_fields = Tkinter.Frame(shipment_frame, bg="Lavender")
        shipment_fields.grid_columnconfigure(4, weight=1)
        revision_fields = Tkinter.Frame(revision_frame, bg="Lavender")
        revision_fields.grid_columnconfigure(4, weight=1)
        mesh_fields = Tkinter.Frame(mesh_frame, bg="Lavender")
        mesh_fields.grid_columnconfigure(4, weight=1)
        ceramic_fields = Tkinter.Frame(ceramic_frame, bg="Lavender")
        ceramic_fields.grid_columnconfigure(4, weight=1)
        lot_fields.grid(row=0, column=0, columnspan=2, sticky="new")
        shipment_fields.grid(row=0, column=0, columnspan=2, sticky="new")
        revision_fields.grid(row=0, column=0, columnspan=2, sticky="new")
        mesh_fields.grid(row=0, column=0, columnspan=2, sticky="new")
        ceramic_fields.grid(row=0, column=0, columnspan=2, sticky="new")

        # refresh picture
        refreshpic = PIL.Image.open("C:/Users/GreggRapp/PycharmProjects/pythonProject/icon_refresh.png")
        resized_refresh = refreshpic.resize((20, 20), PIL.Image.ANTIALIAS)
        global refresh_image
        refresh_image = ImageTk.PhotoImage(resized_refresh)

        # fill insert frame with attributes
        insert_title = Tkinter.Label(insert_frame, text="Insert Ejectors by Lot", bg="lavender", font=TITLE_FONT)
        insert_body = Tkinter.Label(insert_frame, text="Select lot and its corresponding shipment, then select "
                                                       "its revision, mesh, and ceramic", bg="lavender", font=BODY_FONT)
        insert_lotlabel = Tkinter.Label(insert_frame, text="Lot ID:", bg="lavender", font=BODY_FONT, fg='gray')
        insert_shipmentlabel = Tkinter.Label(insert_frame, text="Shipment ID:", bg="lavender", font=BODY_FONT, fg='gray')
        insert_revisionlabel = Tkinter.Label(insert_frame, text="Revision ID:", bg="lavender", font=BODY_FONT, fg='gray')
        insert_meshlabel = Tkinter.Label(insert_frame, text="Mesh ID:", bg="lavender", font=BODY_FONT, fg='gray')
        insert_ceramiclabel = Tkinter.Label(insert_frame, text="Ceramic ID:", bg="lavender", font=BODY_FONT, fg='gray')
        insert_lotentry = Tkinter.Entry(insert_frame, state='disabled', justify='center')
        insert_shipmententry = Tkinter.Entry(insert_frame, state='disabled', justify='center')
        insert_revisionentry = Tkinter.Entry(insert_frame, state='disabled', justify='center')
        insert_meshentry = Tkinter.Entry(insert_frame, state='disabled', justify='center')
        insert_ceramicentry = Tkinter.Entry(insert_frame, state='disabled', justify='center')
        insert_button = Tkinter.Button(insert_frame, text="Submit", command=self.submit)
        insert_title.grid(row=0, column=0, columnspan=5, sticky='nsew')
        insert_body.grid(row=1, column=0, columnspan=5, sticky='nsew', pady=(0, 5))
        insert_lotlabel.grid(row=2, column=0, sticky='nsew')
        insert_shipmentlabel.grid(row=2, column=1, sticky='nsew')
        insert_revisionlabel.grid(row=2, column=2, sticky='nsew')
        insert_meshlabel.grid(row=2, column=3, sticky='nsew')
        insert_ceramiclabel.grid(row=2, column=4, sticky='nsew')
        insert_lotentry.grid(row=3, column=0, sticky='nsew')
        insert_shipmententry.grid(row=3, column=1, sticky='nsew')
        insert_revisionentry.grid(row=3, column=2, sticky='nsew')
        insert_meshentry.grid(row=3, column=3, sticky='nsew')
        insert_ceramicentry.grid(row=3, column=4, sticky='nsew')
        insert_button.grid(row=4, column=0, columnspan=5, sticky='s', pady=(10, 0))

        # declare style for treeview
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#d3d3d3", foreground="blue", rowheight=25,
                        fieldbackground="#d3d3d3")
        style.map('Treeview', background=[('selected', 'dark blue')])

        # Set tree for lot
        lot_treescroll = Tkinter.Scrollbar(lot_frame)
        lot_tree = ttk.Treeview(lot_frame,
                                     columns=('Lot ID', 'Name', 'Lot Type', 'Quantity'),
                                     yscrollcommand=lot_treescroll.set)
        lot_treescroll.config(command=lot_tree.yview)
        lot_treescroll.grid(row=1, column=1, sticky="ns")

        # Set tree for shipment
        shipment_treescroll = Tkinter.Scrollbar(shipment_frame)
        shipment_tree = ttk.Treeview(shipment_frame,
                                     columns=('Shipment ID', 'Sender', 'Receiver', 'Service', 'Date', 'Tracking Number'),
                                     yscrollcommand=shipment_treescroll.set)
        shipment_treescroll.config(command=shipment_tree.yview)
        shipment_treescroll.grid(row=1, column=1, sticky="ns")

        # Set tree for revision
        revision_treescroll = Tkinter.Scrollbar(revision_frame)
        revision_tree = ttk.Treeview(revision_frame,
                                     columns=('Revision ID', 'Name', 'Description'),
                                     yscrollcommand=revision_treescroll.set)
        revision_treescroll.config(command=revision_tree.yview)
        revision_treescroll.grid(row=1, column=1, sticky="ns")

        # Set tree for mesh
        mesh_treescroll = Tkinter.Scrollbar(mesh_frame)
        mesh_tree = ttk.Treeview(mesh_frame,
                                 columns=('Mesh ID', 'Name', 'Specced Hole Size', 'Specced Pitch', 'Specced Thickness'),
                                 yscrollcommand=mesh_treescroll.set)
        mesh_treescroll.config(command=mesh_tree.yview)
        mesh_treescroll.grid(row=1, column=1, sticky="ns")

        # Set tree for ceramic
        ceramic_treescroll = Tkinter.Scrollbar(ceramic_frame)
        ceramic_tree = ttk.Treeview(ceramic_frame,
                                    columns=('Ceramic ID', 'Name', 'Outer Diameter', 'Inner Diameter'),
                                    yscrollcommand=ceramic_treescroll.set)
        ceramic_treescroll.config(command=ceramic_tree.yview)
        ceramic_treescroll.grid(row=1, column=1, sticky="ns")

        # place trees
        lot_frame.grid_rowconfigure(1, weight=1)
        shipment_frame.grid_rowconfigure(1, weight=1)
        revision_frame.grid_rowconfigure(1, weight=1)
        mesh_frame.grid_rowconfigure(1, weight=1)
        ceramic_frame.grid_rowconfigure(1, weight=1)
        lot_tree.grid(row=1, column=0, sticky='nsew')
        shipment_tree.grid(row=1, column=0, sticky='nsew')
        revision_tree.grid(row=1, column=0, sticky='nsew')
        mesh_tree.grid(row=1, column=0, sticky='nsew')
        ceramic_tree.grid(row=1, column=0, sticky='nsew')

        # build lot tree view
        lot_tree.heading('Lot ID', text='ID', anchor=Tkinter.CENTER)
        lot_tree.heading('Name', text='Name', anchor=Tkinter.CENTER)
        lot_tree.heading('Lot Type', text='Lot Type', anchor=Tkinter.CENTER)
        lot_tree.heading('Quantity', text='Quantity', anchor=Tkinter.CENTER)
        lot_tree.column('#0', width=0, stretch=Tkinter.NO)
        lot_tree.column('Lot ID', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        lot_tree.column('Name', stretch=Tkinter.YES, anchor=Tkinter.CENTER, width=120)
        lot_tree.column('Lot Type', stretch=Tkinter.YES, anchor=Tkinter.CENTER, width=100)
        lot_tree.column('Quantity', stretch=Tkinter.YES, anchor=Tkinter.CENTER, width=80)
        lot_tree.tag_configure('oddrow', background="white")
        lot_tree.tag_configure('evenrow', background="lightblue")

        # build shipment tree view
        shipment_tree.heading('Shipment ID', text='ID', anchor=Tkinter.CENTER)
        shipment_tree.heading('Sender', text='Sender', anchor=Tkinter.CENTER)
        shipment_tree.heading('Receiver', text='Receiver', anchor=Tkinter.CENTER)
        shipment_tree.heading('Service', text='Service', anchor=Tkinter.CENTER)
        shipment_tree.heading('Date', text='Date', anchor=Tkinter.CENTER)
        shipment_tree.heading('Tracking Number', text='Tracking #', anchor=Tkinter.CENTER)
        shipment_tree.column('#0', width=0, stretch=Tkinter.NO)
        shipment_tree.column('Shipment ID', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        shipment_tree.column('Sender', stretch=Tkinter.YES, anchor=Tkinter.CENTER, width=120)
        shipment_tree.column('Receiver', stretch=Tkinter.YES, anchor=Tkinter.CENTER, width=120)
        shipment_tree.column('Service', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=120)
        shipment_tree.column('Date', stretch=Tkinter.YES, anchor=Tkinter.CENTER, width=100)
        shipment_tree.column('Tracking Number', stretch=Tkinter.YES, anchor=Tkinter.CENTER, width=100)
        shipment_tree.tag_configure('oddrow', background="white")
        shipment_tree.tag_configure('evenrow', background="lightblue")

        # build revision tree view
        revision_tree.heading('Revision ID', text='ID', anchor=Tkinter.CENTER)
        revision_tree.heading('Name', text='Name', anchor=Tkinter.CENTER)
        revision_tree.heading('Description', text='Description', anchor=Tkinter.CENTER)
        revision_tree.column('#0', width=0, stretch=Tkinter.NO)
        revision_tree.column('Revision ID', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        revision_tree.column('Name', stretch=Tkinter.YES, anchor=Tkinter.CENTER, width=100)
        revision_tree.column('Description', stretch=Tkinter.YES, anchor=Tkinter.CENTER, width=200)
        revision_tree.tag_configure('oddrow', background="white")
        revision_tree.tag_configure('evenrow', background="lightblue")

        # build mesh tree view
        mesh_tree.heading('Mesh ID', text='Mesh ID', anchor=Tkinter.CENTER)
        mesh_tree.heading('Name', text='Name', anchor=Tkinter.CENTER)
        mesh_tree.heading('Specced Hole Size', text='Specced Hole Size', anchor=Tkinter.CENTER)
        mesh_tree.heading('Specced Pitch', text='Specced Pitch', anchor=Tkinter.CENTER)
        mesh_tree.heading('Specced Thickness', text='Specced Thickness', anchor=Tkinter.CENTER)
        mesh_tree.column('#0', width=0, stretch=Tkinter.NO)
        mesh_tree.column('Mesh ID', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        mesh_tree.column('Name', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=150)
        mesh_tree.column('Specced Hole Size', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=100)
        mesh_tree.column('Specced Pitch', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=100)
        mesh_tree.column('Specced Thickness', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=100)
        mesh_tree.tag_configure('oddrow', background="white")
        mesh_tree.tag_configure('evenrow', background="lightblue")

        # build ceramic tree view
        ceramic_tree.heading('Ceramic ID', text='Ceramic ID', anchor=Tkinter.CENTER)
        ceramic_tree.heading('Name', text='Name', anchor=Tkinter.CENTER)
        ceramic_tree.heading('Outer Diameter', text='Outer Diameter', anchor=Tkinter.CENTER)
        ceramic_tree.heading('Inner Diameter', text='Inner Diameter', anchor=Tkinter.CENTER)
        ceramic_tree.column('#0', width=0, stretch=Tkinter.NO)
        ceramic_tree.column('Ceramic ID', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        ceramic_tree.column('Name', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=150)
        ceramic_tree.column('Outer Diameter', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=100)
        ceramic_tree.column('Inner Diameter', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=100)
        ceramic_tree.tag_configure('oddrow', background="white")
        ceramic_tree.tag_configure('evenrow', background="lightblue")

        username = "root"
        password = "VRSCm1998!"
        self.my_connect = mysql.connector.connect(
            host="localhost",
            user=username,
            passwd=password,
            database="pneumabase"
        )

        def update_lot():
            self.update_lot(lot_tree)

        def insert_lot():
            self.insert_lot(lot_tree)

        def modify_lot():
            self.modify_lot(lot_tree)

        def delete_lot():
            self.delete_lot(lot_tree)

        def update_ceramic():
            self.update_ceramic(ceramic_tree)

        def insert_ceramic():
            self.insert_ceramic(ceramic_tree)

        def modify_ceramic():
            self.modify_ceramic(ceramic_tree)

        def delete_ceramic():
            self.delete_ceramic(ceramic_tree)

        def update_shipment():
            self.update_shipment(shipment_tree)

        def insert_shipment():
            self.insert_shipment(shipment_tree)

        def modify_shipment():
            self.modify_shipment(shipment_tree)

        def delete_shipment():
            self.delete_shipment(shipment_tree)

        def update_revision():
            self.update_revision(revision_tree)

        def insert_revision():
            self.insert_revision(revision_tree)

        def modify_revision():
            self.modify_revision(revision_tree)

        def delete_revision():
            self.delete_revision(revision_tree)

        def update_mesh():
            self.update_mesh(mesh_tree)

        def insert_mesh():
            self.insert_mesh(mesh_tree)

        def modify_mesh():
            self.modify_mesh(mesh_tree)

        def delete_mesh():
            self.delete_mesh(mesh_tree)

        # fill lot field frame with attributes
        lot_label = Tkinter.Label(lot_fields, text="Select Lot", bg="lavender", font=TITLE_FONT)
        lot_insert = Tkinter.Button(lot_fields, text="Insert", command=insert_lot)
        lot_delete = Tkinter.Button(lot_fields, text="Delete Selected", command=delete_lot)
        lot_update = Tkinter.Button(lot_fields, text="", command=update_lot, image=refresh_image,
                                    compound=LEFT)
        lot_update.image = refresh_image
        lot_modify = Tkinter.Button(lot_fields, text="Modify Record", command=modify_lot)
        lot_label.grid(row=0, column=0, sticky="new", columnspan=5)
        lot_insert.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
        lot_delete.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        lot_modify.grid(row=1, column=3, sticky="w", padx=10, pady=10)
        lot_update.grid(row=1, column=4, sticky="e", padx=(10, 0), pady=10)

        # fill shipment field frame with attributes
        shipment_label = Tkinter.Label(shipment_fields, text="Select Shipment", bg="lavender", font=TITLE_FONT)
        shipment_insert = Tkinter.Button(shipment_fields, text="Insert", command=insert_shipment)
        shipment_delete = Tkinter.Button(shipment_fields, text="Delete Selected", command=delete_shipment)
        shipment_update = Tkinter.Button(shipment_fields, text="", command=update_shipment, image=refresh_image,
                                         compound=LEFT)
        shipment_update.image = refresh_image
        shipment_modify = Tkinter.Button(shipment_fields, text="Modify Record", command=modify_shipment)
        shipment_label.grid(row=0, column=0, sticky="new", columnspan=5)
        shipment_insert.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
        shipment_delete.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        shipment_modify.grid(row=1, column=3, sticky="w", padx=10, pady=10)
        shipment_update.grid(row=1, column=4, sticky="e", padx=(10, 0), pady=10)

        # fill revision field frame with attributes
        revision_label = Tkinter.Label(revision_fields, text="Select Revision", bg="lavender", font=TITLE_FONT)
        revision_insert = Tkinter.Button(revision_fields, text="Insert", command=insert_revision)
        revision_delete = Tkinter.Button(revision_fields, text="Delete Selected", command=delete_revision)
        revision_update = Tkinter.Button(revision_fields, text="", command=update_revision, image=refresh_image,
                                         compound=LEFT)
        revision_update.image = refresh_image
        revision_modify = Tkinter.Button(revision_fields, text="Modify Record", command=modify_revision)
        revision_label.grid(row=0, column=0, sticky="new", columnspan=5)
        revision_insert.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
        revision_delete.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        revision_modify.grid(row=1, column=3, sticky="w", padx=10, pady=10)
        revision_update.grid(row=1, column=4, sticky="e", padx=(10, 0), pady=10)

        # fill mesh field frame with attributes
        mesh_label = Tkinter.Label(mesh_fields, text="Select Mesh", bg="lavender", font=TITLE_FONT)
        mesh_insert = Tkinter.Button(mesh_fields, text="Insert", command=insert_mesh)
        mesh_delete = Tkinter.Button(mesh_fields, text="Delete Selected", command=delete_mesh)
        mesh_update = Tkinter.Button(mesh_fields, text="", command=update_mesh, image=refresh_image, compound=LEFT)
        mesh_update.image = refresh_image
        mesh_modify = Tkinter.Button(mesh_fields, text="Modify Record", command=modify_mesh)
        mesh_label.grid(row=0, column=0, sticky="new", columnspan=5)
        mesh_insert.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
        mesh_delete.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        mesh_modify.grid(row=1, column=3, sticky="w", padx=10, pady=10)
        mesh_update.grid(row=1, column=4, sticky="e", padx=(10, 0), pady=10)

        # fill ceramic field frame with attributes
        ceramic_label = Tkinter.Label(ceramic_fields, text="Select Ceramic", bg="lavender", font=TITLE_FONT)
        ceramic_insert = Tkinter.Button(ceramic_fields, text="Insert", command=insert_ceramic)
        ceramic_delete = Tkinter.Button(ceramic_fields, text="Delete Selected", command=delete_ceramic)
        ceramic_update = Tkinter.Button(ceramic_fields, text="", command=update_ceramic, image=refresh_image,
                                        compound=LEFT)
        ceramic_update.image = refresh_image
        ceramic_modify = Tkinter.Button(ceramic_fields, text="Modify Record", command=modify_ceramic)
        ceramic_label.grid(row=0, column=0, sticky="new", columnspan=5)
        ceramic_insert.grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
        ceramic_delete.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        ceramic_modify.grid(row=1, column=3, sticky="w", padx=10, pady=10)
        ceramic_update.grid(row=1, column=4, sticky="e", padx=(10, 0), pady=10)

        self.parent = parent
        self.update_lot(lot_tree)
        self.update_shipment(shipment_tree)
        self.update_revision(revision_tree)
        self.update_mesh(mesh_tree)
        self.update_ceramic(ceramic_tree)

    # input date with '/', output sql formatted date
    def format_date(self, date):
            list = date.split('/')
            month = list[0]
            day = list[1]
            year = list[2]
            return year + '-' + month + '-' + day

    def submit(self):
        pass

    # Creates popup after sql error appears
    def error_popup(self, e):
        popup = Tkinter.Tk()
        popup.title("Error")
        message = Tkinter.Label(popup, text="", fg='red')
        close = Tkinter.Button(popup, text="Close", command=popup.destroy)
        message['text'] = "Error " + str(e)
        message.pack(pady=(15, 7), padx=15)
        close.pack(pady=(7, 15))

    # Creates custom error popup with the string input being the label
    def custom_error_popup(self, string):
        popup = Tkinter.Tk()
        popup.title("Error")
        message = Tkinter.Label(popup, text="", fg='red')
        close = Tkinter.Button(popup, text="Close", command=popup.destroy)
        message['text'] = "Error: " + string
        message.pack(pady=(15, 7), padx=15)
        close.pack(pady=(7, 15))

    # returns record[row][column] containing indexed values within table in database
    def find_in_table(self, tablename, index):
        if tablename == "Company":
            try:
                my_curs = self.create_connection()
                sql = "select * from company where Company_ID = %s;"
                val = (index,)
                my_curs.execute(sql, val)
                return my_curs.fetchall()
            except mysql.connector.Error as e:
                self.error_popup(e)
        elif tablename == "Shipment":
            try:
                my_curs = self.create_connection()
                sql = "select * from shipment where Shipment_ID = %s;"
                val = (index,)
                my_curs.execute(sql, val)
                return my_curs.fetchall()
            except mysql.connector.Error as e:
                self.error_popup(e)
        elif tablename == "Lot":
            try:
                my_curs = self.create_connection()
                sql = "select * from lot where Lot_ID = %s;"
                val = (index,)
                my_curs.execute(sql, val)
                return my_curs.fetchall()
            except mysql.connector.Error as e:
                self.error_popup(e)
        elif tablename == "Revision":
            try:
                my_curs = self.create_connection()
                sql = "select * from revision where Revision_ID = %s;"
                val = (index,)
                my_curs.execute(sql, val)
                return my_curs.fetchall()
            except mysql.connector.Error as e:
                self.error_popup(e)
        elif tablename == "Mesh":
            try:
                my_curs = self.create_connection()
                sql = "select * from mesh where Mesh_ID = %s;"
                val = (index,)
                my_curs.execute(sql, val)
                return my_curs.fetchall()
            except mysql.connector.Error as e:
                self.error_popup(e)
        elif tablename == "Ceramic":
            try:
                my_curs = self.create_connection()
                sql = "select * from ceramic where Ceramic_ID = %s;"
                val = (index,)
                my_curs.execute(sql, val)
                return my_curs.fetchall()
            except mysql.connector.Error as e:
                self.error_popup(e)
        else:
            self.custom_error_popup("Invalid parameter in find_in_table")

    # Creates popup to insert into revision
    def insert_revision(self, treeview):
        popup = Tkinter.Toplevel()
        popup.title("Insert Data")
        popup.grid_rowconfigure(1, weight=1)
        popup.grid_columnconfigure(0, weight=1)
        field_frame = Tkinter.Frame(popup)
        field_frame.columnconfigure(0, weight=1)
        field_frame.columnconfigure(1, weight=1)
        tree_frame = Tkinter.Frame(popup)
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.columnconfigure(2, weight=1)
        tree_frame.rowconfigure(2, weight=1)
        button_frame = Tkinter.Frame(popup)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        field_frame.grid(row=0, column=0, pady=10, sticky='n')
        tree_frame.grid(row=1, column=0, padx=10, sticky='nsew')
        button_frame.grid(row=2, column=0, pady=10, padx=10, sticky='ew')
        tree_buttons = Tkinter.Frame(tree_frame)
        tree_buttons.grid(row=1, column=0, columnspan=2, sticky='sew')
        tree_buttons.columnconfigure(3, weight=1)
        # Initialize other entries and labels
        title_label = Tkinter.Label(field_frame, text="Insert New Revision", font=TITLE_FONT)
        explanation_label = Tkinter.Label(field_frame, text="Fill out entries and select the revision's associated components\n* entries mandatory", font=BODY_FONT)
        name_label = Tkinter.Label(field_frame, text="*Revision Name:", font=BODY_FONT)
        name_entry = Tkinter.Entry(field_frame)
        description_label = Tkinter.Label(field_frame, text="*Description:", font=BODY_FONT)
        description_entry = Tkinter.Entry(field_frame)
        title_label.grid(row=0, column=0, sticky=Tkinter.NSEW, columnspan=3, padx=15, pady=15)
        explanation_label.grid(row=1, column=0, sticky=Tkinter.NSEW, columnspan=3, padx=15, pady=(0, 15))
        name_label.grid(row=2, column=0, sticky='e', padx=(15, 8))
        name_entry.grid(row=2, column=1, sticky='w', padx=(8, 15))
        description_label.grid(row=3, column=0, sticky='e', padx=(15, 8))
        description_entry.grid(row=3, column=1, sticky='w', padx=(8, 15))

        component_title = Tkinter.Label(tree_frame, text="*Select Components", font=TITLE_FONT)
        component_treescroll = Tkinter.Scrollbar(tree_frame)
        component_tree = ttk.Treeview(tree_frame,
                                      columns=('Component ID', 'Name', 'Manufacturer', 'Type', 'Description'),
                                      yscrollcommand=component_treescroll.set, selectmode='none')
        component_treescroll.config(command=component_tree.yview)
        component_treescroll.grid(row=2, column=1, sticky="ns")

        # Set tree for revision
        revision_title = Tkinter.Label(tree_frame, text="Revision", font=TITLE_FONT)
        revision_instruction = Tkinter.Label(tree_frame, text="Select all components from existing revision", font=BODY_FONT)
        revision_treescroll = Tkinter.Scrollbar(tree_frame)
        revision_tree = ttk.Treeview(tree_frame,
                                     columns=('Revision ID', 'Name', 'Description'),
                                     yscrollcommand=revision_treescroll.set)
        revision_treescroll.config(command=revision_tree.yview)
        revision_treescroll.grid(row=2, column=3, sticky="ns")

        component_tree.heading('Component ID', text='Component ID', anchor=Tkinter.CENTER)
        component_tree.heading('Name', text='Name', anchor=Tkinter.CENTER)
        component_tree.heading('Manufacturer', text='Manufacturer', anchor=Tkinter.CENTER)
        component_tree.heading('Type', text='Type', anchor=Tkinter.CENTER)
        component_tree.heading('Description', text='Description', anchor=Tkinter.CENTER)
        component_tree.column('#0', width=0, stretch=Tkinter.NO)
        component_tree.column('Component ID', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        component_tree.column('Name', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=100)
        component_tree.column('Manufacturer', width=120, stretch=Tkinter.NO, anchor=Tkinter.CENTER)
        component_tree.column('Type', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=100)
        component_tree.column('Description', width=200, stretch=Tkinter.YES, anchor=Tkinter.CENTER)
        component_tree.tag_configure('oddrow', background="white")
        component_tree.tag_configure('evenrow', background="lightblue")

        # build revision tree view
        revision_tree.heading('Revision ID', text='ID', anchor=Tkinter.CENTER)
        revision_tree.heading('Name', text='Name', anchor=Tkinter.CENTER)
        revision_tree.heading('Description', text='Description', anchor=Tkinter.CENTER)
        revision_tree.column('#0', width=0, stretch=Tkinter.NO)
        revision_tree.column('Revision ID', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        revision_tree.column('Name', stretch=Tkinter.YES, anchor=Tkinter.CENTER, width=100)
        revision_tree.column('Description', stretch=Tkinter.YES, anchor=Tkinter.CENTER, width=200)
        revision_tree.tag_configure('oddrow', background="white")
        revision_tree.tag_configure('evenrow', background="lightblue")

        def update_component_tree():
            self.update_component(component_tree, 'no device')

        def insert_component_tree():
            self.insert_component(component_tree)
            update_component_tree()

        def delete_component():
            self.delete_component(component_tree)
            update_component_tree()

        def modify_component():
            self.modify_component(component_tree)
            update_component_tree()

        # selects all components of selected revision
        def select_components(event):
            record = revision_tree.selection_get()
            if len(record) == 1:
                components = self.revision_components(record[0])
                component_tree.selection_set(components)
            else:
                pass

        def select(event=None):
            component_tree.selection_toggle(component_tree.focus())

        def collect_text():
            string = ['' for i in range(2)]
            string[0] = name_entry.get()
            string[1] = description_entry.get()
            return string

        def delete_boxtext():
            name_entry.delete(0, 'end')
            description_entry.delete(0, 'end')
            component_tree.selection_clear()

        def link_components(id):
            try:
                my_curs = self.create_connection()
                records = component_tree.selection()
                for record in records:
                    val = (id, int(component_tree.item(record, 'values')[0]))
                    sql = "INSERT INTO revision_component (Revision_ID, Component_ID) VALUES (%s,%s)"
                    my_curs.execute(sql, val)
                    self.my_connect.commit()
                delete_boxtext()
                self.confirmation_popup('Revision')
            except mysql.connector.Error as e:
                self.error_popup(e)

        def submit():
            strings = collect_text()
            sql = "INSERT INTO revision (Name, Description)" \
                  "VALUES (%s,%s);"
            for i in range(len(strings)):  # check for empty strings label as NONE
                if (strings[i] == "" or strings[i] == "<Select>"):
                    strings[i] = None
            val = (strings[0], strings[1])
            try:
                my_curs = self.create_connection()
                my_curs.execute(sql, val)
                self.my_connect.commit()
                print(my_curs.lastrowid)
                link_components(my_curs.lastrowid)
            except mysql.connector.Error as e:
                self.error_popup(e)

        submit_button = Tkinter.Button(button_frame, text="Submit", command=submit)
        cancel_button = Tkinter.Button(button_frame, text="Cancel", command=popup.destroy)
        submit_button.grid(row=0, column=1, sticky='e')
        cancel_button.grid(row=0, column=0, sticky='w')

        component_tree.bind('<ButtonRelease-1>', select)
        revision_tree.bind("<Double-1>", select_components)
        component_insert = Tkinter.Button(tree_buttons, text="Insert", command=insert_component_tree)
        component_delete = Tkinter.Button(tree_buttons, text="Delete Selected", command=delete_component)
        component_update = Tkinter.Button(tree_buttons, text="", command=update_component_tree, image=refresh_image,
                                          compound=LEFT)
        component_update.image = refresh_image
        component_modify = Tkinter.Button(tree_buttons, text="Modify Record", command=modify_component)

        component_insert.grid(row=0, column=0, sticky='w', padx=(0, 10))
        component_delete.grid(row=0, column=1, sticky='w', padx=10)
        component_modify.grid(row=0, column=2, sticky='w', padx=10)
        component_update.grid(row=0, column=3, sticky='e', padx=(0,10))

        component_title.grid(row=0, column=0, columnspan=2, sticky='nsew', pady=10)
        component_tree.grid(row=2, column=0, sticky='nsew', pady=10)
        revision_title.grid(row=0, column=2, columnspan=2, sticky='nsew')
        revision_instruction.grid(row=1, column=2, columnspan=2, sticky='n')
        revision_tree.grid(row=2, column=2, sticky='nsew', pady=10)

        self.update_component(component_tree, 'no device')
        self.update_revision(revision_tree)

    def update_revision(self, treeview):
        try:
            my_curs = self.create_connection()
            my_curs.execute("select * from revision order by Name ASC")
        except mysql.connector.Error as e:
            self.error_popup(e)
        string = ["" for i in range(3)]
        size = 0
        for i in treeview.get_children():
            treeview.delete(i)
        for revision in my_curs:
            size += 1
            string[0] = str(revision[0])
            string[1] = str(revision[1])
            string[2] = str(revision[2])
            if size % 2 == 0:
                treeview.insert('', 'end', iid=revision[0],
                                     values=(string[0], string[1], string[2]),
                                     tags=('evenrow',)
                                     )
            else:
                treeview.insert('', 'end', iid=revision[0],
                                     values=(string[0], string[1], string[2]),
                                     tags=('oddrow',)
                                     )

    def delete_revision(self, treeview):
        pass

    def modify_revision(self, treeview):
        pass

    def delete_company(self, treeview):
        record = treeview.selection()
        if record:
            popup = Tkinter.Tk()
            popup.title("Confirm Changes")
            # delete string from table
            def delete_company():
                try:
                    my_curs = self.create_connection()
                    for rec in record:
                        dat = (str(treeview.item(rec, "values")[0]),)
                        sql = "DELETE FROM company WHERE Company_ID = %s"
                        val = dat
                        my_curs.execute(sql, val)
                        self.my_connect.commit()
                    self.update_company(treeview, 'no shipper')
                    popup.destroy()
                except mysql.connector.Error as e:
                    self.error_popup(e)

            frame = Tkinter.Frame(popup)
            label = Tkinter.Label(frame, text="Confirm Changes")
            confirm_button = Tkinter.Button(frame, text="Confirm", command=delete_company)
            cancel_button = Tkinter.Button(frame, text="Cancel", command=popup.destroy)
            label.pack(side='top', fill='y', pady=(15, 7.5))
            confirm_button.pack(side='left', fill='y', padx=15, pady=(7.5, 15))
            cancel_button.pack(side='right', fill='y', padx=15, pady=(7.5, 15))
            frame.pack()
        else:
            pass

    def modify_company(self, treeview):
        record = treeview.selection()
        if len(record) == 1:
            popup = Tkinter.Tk()
            popup.title("Modify Company")
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
                string = self.find_in_table("Company", treeview.item(record, "values")[0])
                string = string[0]
                add_boxtext(string)

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
                return string

            def add_boxtext(string):
                for i in string:
                    if i == None:
                        i = ''
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
                index = int(treeview.item(record, "values")[0])
                modify(index)

            def modify(index):
                if index >= 0:
                    data = collect_text()
                    sql = "update company set Address1 = %s, " \
                          "Address2 = %s, State = %s, Zip = %s, Country = %s," \
                          "Name = %s, City = %s, CompanyType = %s" \
                          "where Company_ID = %s;"
                    for i in range(len(data)):
                        if data[i] == "" or data[i] == "None" or data[i] == "<Select>":
                            data[i] = None
                    val = (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], index)
                    try:
                        my_curs = self.create_connection()
                        my_curs.execute(sql, val)
                        self.my_connect.commit()
                    except mysql.connector.Error as e:
                        self.error_popup(e)
                    self.update_company(treeview, 'no shipper')
                    popup.destroy()
                else:
                    self.custom_error_popup("modify_record was used with negative index")

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

    def insert_company(self, treeview):
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
                my_curs = self.create_connection()
                collect_text()
                strings = self.field_data
                sql = "INSERT INTO company (Address1, Address2, State, Zip, Country, Name, City,CompanyType)VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
                for i in range(len(strings)):  # check for empty strings label as NONE
                    if (strings[i] == "" or strings[i] == "<Select>"):
                        strings[i] = None
                val = (strings[0], strings[1], strings[2], strings[3], strings[4], strings[5], strings[6], strings[7])
                my_curs.execute(sql, val)
                self.my_connect.commit()
                self.update_company(treeview, 'no shipper')
                delete_boxtext()
            except mysql.connector.Error as e:
                self.error_popup(e)

        insert_button = Tkinter.Button(field_frame, text="Insert", command=insert_data)
        cancel_button = Tkinter.Button(field_frame, text="Cancel", command=popup.destroy)
        insert_button.grid(row=9, column=1, sticky=Tkinter.E, padx=15, pady=10)
        cancel_button.grid(row=9, column=0, sticky=Tkinter.W, padx=15, pady=10)

    # 'no shipper', 'only shipper', 'only manufacturer'
    def update_company(self, treeview, type):
        my_curs = self.create_connection()
        if type == "no shipper":
            try:
                my_curs.execute("select * from company where CompanyType != 'Shipper' order by CompanyType, Name ASC")
            except mysql.connector.Error as e:
                self.error_popup(e)
        elif type == "only shipper":
            try:
                my_curs.execute("select * from company where CompanyType = 'Shipper' order by CompanyType, Name ASC")
            except mysql.connector.Error as e:
                self.error_popup(e)
        elif type == 'only manufacturer':
            try:
                my_curs.execute("select * from company where CompanyType = 'Manufacturer' order by CompanyType, Name ASC")
            except mysql.connector.Error as e:
                self.error_popup(e)
        string = ["" for i in range(9)]
        size = 0
        # Checks to see if there are more not null entries in arr
        def checkMoreEntries(arr, index):
            if index == len(arr):
                return False
            else:
                for i in range(index + 1, len(arr)):
                    if arr[i] != "None":
                        return True
                return False

        for i in treeview.get_children():
            treeview.delete(i)
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
                a = checkMoreEntries(string, i)
                if string[i] != "None":
                    if a:
                        val += string[i] + ", "
                    elif not a:
                        val += string[i]
            size += 1
            if size % 2 == 0:
                treeview.insert('', 'end', iid=company[0],
                                     values=(string[0], string[1], string[2], string[3], val),
                                     tags=('evenrow',)
                                     )
            else:
                treeview.insert('', 'end', iid=company[0],
                                     values=(string[0], string[1], string[2], string[3], val),
                                     tags=('oddrow',)
                                     )

    def insert_component(self, treeview):
        popup = Tkinter.Toplevel()
        popup.title("Insert Component")
        popup.grid_rowconfigure(1, weight=1)
        popup.grid_columnconfigure(0, weight=1)
        field_frame = Tkinter.Frame(popup)
        tree_frame = Tkinter.Frame(popup)
        button_frame = Tkinter.Frame(popup)
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        tree_frame.grid_rowconfigure(1, weight=1)
        field_frame.grid(row=0, column=0, pady=(10, 0))
        tree_frame.grid(row=1, column=0, padx=10, pady=10)
        button_frame.grid(row=2, column=0, padx=10, pady=(0, 10))
        # Create type combo box entry and label
        type_options = ["<Select>",
                        "Ejector",
                        "Device"]
        type_entry = ttk.Combobox(field_frame, value=type_options)

        # Set field frame
        header = Tkinter.Label(field_frame, text="Insert New Component", font=TITLE_FONT)
        instruction_label = Tkinter.Label(field_frame,
                                          text="Fill out entries and select the manufacturer\n* entries mandatory",
                                          font=BODY_FONT)
        name_label = Tkinter.Label(field_frame, text="*Name of component:", font=BODY_FONT)
        type_label = Tkinter.Label(field_frame, text="*Component type:", font=BODY_FONT)
        description_label = Tkinter.Label(field_frame, text="*Description:", font=BODY_FONT)
        name_field = Tkinter.Entry(field_frame, justify='center')
        description_field = Tkinter.Entry(field_frame, justify='center')
        header.grid(row=0, column=0, columnspan=2, sticky='nsew', pady=10)
        instruction_label.grid(row=1, column=0, columnspan=2, sticky='nsew')
        name_label.grid(row=2, column=0, sticky='e')
        name_field.grid(row=2, column=1, sticky='nsew')
        type_label.grid(row=3, column=0, sticky='e')
        type_entry.grid(row=3, column=1, sticky='nsew')
        description_label.grid(row=4, column=0, sticky='e')
        description_field.grid(row=4, column=1, sticky='nsew')
        # Set tree for manufacturer
        manufacturer_frame = Tkinter.Frame(tree_frame)
        manufacturer_fields = Tkinter.Frame(tree_frame)
        manufacturer_fields.columnconfigure(3, weight=1)
        manufacturer_frame.grid_rowconfigure(0, weight=1)
        manufacturer_frame.grid_columnconfigure(0, weight=1)
        manufacturer_fields.grid(row=0, column=0, sticky='nsew')
        manufacturer_frame.grid(row=1, column=0, sticky='nsew')

        manufacturer_treescroll = Tkinter.Scrollbar(manufacturer_frame)
        manufacturer_tree = ttk.Treeview(manufacturer_frame,
                                   columns=('Company ID', 'Company', 'Type', 'Country', 'Address'),
                                   yscrollcommand=manufacturer_treescroll.set)
        manufacturer_treescroll.config(command=manufacturer_tree.yview)
        manufacturer_treescroll.grid(row=0, column=1, sticky='nse')
        manufacturer_tree.heading('Company ID', text='Company ID', anchor=Tkinter.CENTER)
        manufacturer_tree.heading('Company', text='Company', anchor=Tkinter.CENTER)
        manufacturer_tree.heading('Type', text='Type', anchor=Tkinter.CENTER)
        manufacturer_tree.heading('Country', text='Country', anchor=Tkinter.CENTER)
        manufacturer_tree.heading('Address', text='Address', anchor=Tkinter.CENTER)
        manufacturer_tree.column('#0', width=0, stretch=Tkinter.NO)
        manufacturer_tree.column('Company ID', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        manufacturer_tree.column('Company', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=150)
        manufacturer_tree.column('Type', width=100, stretch=Tkinter.NO, anchor=Tkinter.CENTER)
        manufacturer_tree.column('Country', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        manufacturer_tree.column('Address', width=300, stretch=Tkinter.YES, anchor=Tkinter.CENTER)
        manufacturer_tree.tag_configure('oddrow', background="white")
        manufacturer_tree.tag_configure('evenrow', background="lightblue")
        manufacturer_tree.grid(row=0, column=0, sticky='nsew')

        def update_manufacturer():
            self.update_company(manufacturer_tree, 'no shipper')

        def insert_manufacturer():
            self.insert_company(manufacturer_tree)

        def delete_manufacturer():
            self.delete_company(manufacturer_tree)
            self.update_company(manufacturer_tree, 'no shipper')

        def modify_manufacturer():
            self.modify_company(manufacturer_tree)
            self.update_company(manufacturer_tree, 'no shipper')

        def collect_text():
            record = manufacturer_tree.selection()
            if len(record) == 1:
                string = ["" for i in range(5)]
                string[0] = name_field.get()
                string[1] = int(manufacturer_tree.item(record, 'values')[0])
                string[2] = None
                string[3] = type_entry.get()
                string[4] = description_field.get()
                return string
            else:
                self.custom_error_popup("Must select one manufacturer")
                return None

        def delete_boxtext():
            name_field.delete(0, 'end')
            type_entry.current(0)
            description_field.delete(0, 'end')
            manufacturer_tree.selection_clear()

        def submit():
            strings = collect_text()
            sql = "INSERT INTO component (Name, Manufacturer_ID, Datasheet, ComponentType, Description)" \
                  "VALUES (%s,%s,%s,%s,%s);"
            for i in range(len(strings)):  # check for empty strings label as NONE
                if (strings[i] == "" or strings[i] == "<Select>"):
                    strings[i] = None
            val = (strings[0], int(strings[1]), strings[2], strings[3], strings[4])
            try:
                my_curs = self.create_connection()
                my_curs.execute(sql, val)
                self.my_connect.commit()
                delete_boxtext()
            except mysql.connector.Error as e:
                self.error_popup(e)

        submit_button = Tkinter.Button(button_frame, text="Submit", command=submit)
        cancel_button = Tkinter.Button(button_frame, text="Cancel", command=popup.destroy)
        submit_button.grid(row=0, column=1, sticky='e', pady=10)
        cancel_button.grid(row=0, column=0, sticky='w', pady=10)
        manufacturer_title = Tkinter.Label(manufacturer_fields, text='*Manufacturer', font=TITLE_FONT)
        manufacturer_insert = Tkinter.Button(manufacturer_fields, text="Insert", command=insert_manufacturer)
        manufacturer_delete = Tkinter.Button(manufacturer_fields, text="Delete Selected", command=delete_manufacturer)
        manufacturer_update = Tkinter.Button(manufacturer_fields, text="", command=update_manufacturer,
                                             image=refresh_image, compound=LEFT)
        manufacturer_update.image = refresh_image
        manufacturer_modify = Tkinter.Button(manufacturer_fields, text="Modify Record",
                                             command=modify_manufacturer)
        # Place buttons in manufacturer frame
        manufacturer_title.grid(row=0, column=0, columnspan=4, pady=10)
        manufacturer_insert.grid(row=1, column=0, sticky=Tkinter.W, padx=20, pady=(0, 10))
        manufacturer_delete.grid(row=1, column=1, sticky=Tkinter.W, padx=20, pady=(0, 10))
        manufacturer_modify.grid(row=1, column=2, sticky=Tkinter.W, padx=20, pady=(0, 10))
        manufacturer_update.grid(row=1, column=3, sticky="e", padx=20, pady=(0, 10))
        self.update_company(manufacturer_tree, 'no shipper')

    # fills treeview input with components of specific type
    def update_component(self, treeview, type):
        my_curs = self.create_connection()
        if type == "no ejector":
            try:
                my_curs.execute("select * from component where ComponentType != 'Device' order by Name ASC")
            except mysql.connector.Error as e:
                self.error_popup(e)
        elif type == "no device":
            try:
                my_curs.execute("select * from component where ComponentType = 'Ejector' order by Name ASC")
            except mysql.connector.Error as e:
                self.error_popup(e)
        elif type == "all":
            try:
                my_curs.execute("select * from component order by Name ASC")
            except mysql.connector.Error as e:
                self.error_popup(e)
        string = ["" for i in range(5)]
        size = 0
        for i in treeview.get_children():
            treeview.delete(i)
        for component in my_curs:
            string[0] = str(component[0])
            string[1] = str(component[1])
            string[2] = self.find_companyname(component[2])
            string[3] = str(component[4])
            string[4] = str(component[5])
            size += 1
            if size % 2 == 0:
                treeview.insert('', 'end', iid=component[0],
                                values=(string[0], string[1], string[2], string[3], string[4]),
                                tags=('evenrow',)
                                )
            else:
                treeview.insert('', 'end', iid=component[0],
                                values=(string[0], string[1], string[2], string[3], string[4]),
                                tags=('oddrow',)
                                )

    def delete_component(self, treeview):
        if treeview.selection():
            popup = Tkinter.Tk()
            popup.title("Confirm Changes")

            # delete string from table
            def deleteCompany():
                try:
                    my_curs = self.create_connection()
                    for record in treeview.selection():
                        val = (str(treeview.item(record, "values")[0]),)
                        sql = "DELETE FROM component WHERE Component_ID = %s"
                        my_curs.execute(sql, val)
                        self.my_connect.commit()
                    popup.destroy()
                except mysql.connector.Error as e:
                    self.error_popup(e)

            frame = Tkinter.Frame(popup)
            label = Tkinter.Label(frame, text="Confirm Changes")
            confirm_button = Tkinter.Button(frame, text="Confirm", command=deleteCompany)
            cancel_button = Tkinter.Button(frame, text="Cancel", command=popup.destroy)
            label.pack(side='top', fill='y', pady=(15, 7.5))
            confirm_button.pack(side='left', fill='y', padx=15, pady=(7.5, 15))
            cancel_button.pack(side='right', fill='y', padx=15, pady=(7.5, 15))
            frame.pack()
        else:
            self.custom_error_popup("No component(s) selected for deletion")

    def modify_component(self, treeview):
        pass

    def insert_mesh(self, treeview):
        pass

    def modify_mesh(self, treeview):
        pass

    def delete_mesh(self, treeview):
        pass

    def update_mesh(self, treeview):
        try:
            my_curs = self.create_connection()
            my_curs.execute("select * from mesh order by Name ASC")
        except mysql.connector.Error as e:
            self.error_popup(e)
        string = ["" for i in range(5)]
        size = 0
        for i in treeview.get_children():
            treeview.delete(i)
        for mesh in my_curs:
            size += 1
            string[0] = str(mesh[0])
            string[1] = str(mesh[8])
            string[2] = str(mesh[2])
            string[3] = str(mesh[3])
            string[4] = str(mesh[5])

            if size % 2 == 0:
                treeview.insert('', 'end', iid=mesh[0],
                                              values=(string[0], string[1], string[2], string[3], string[4]),
                                              tags=('evenrow',)
                                              )
            else:
                treeview.insert('', 'end', iid=mesh[0],
                                              values=(string[0], string[1], string[2], string[3], string[4]),
                                              tags=('oddrow',)
                                              )

    def insert_ceramic(self, treeview):
        pass

    def delete_ceramic(self, treeview):
        pass

    def modify_ceramic(self, treeview):
        pass

    def update_ceramic(self, treeview):
        try:
            my_curs = self.create_connection()
            my_curs.execute("select * from mesh order by Name ASC")
        except mysql.connector.Error as e:
            self.error_popup(e)
        string = ["" for i in range(5)]
        size = 0
        for i in treeview.get_children():
            treeview.delete(i)
        for mesh in my_curs:
            size += 1
            string[0] = str(mesh[0])
            string[1] = str(mesh[8])
            string[2] = str(mesh[2])
            string[3] = str(mesh[3])
            string[4] = str(mesh[5])

            if size % 2 == 0:
                treeview.insert('', 'end', iid=mesh[0],
                                              values=(string[0], string[1], string[2], string[3], string[4]),
                                              tags=('evenrow',)
                                              )
            else:
                treeview.insert('', 'end', iid=mesh[0],
                                              values=(string[0], string[1], string[2], string[3], string[4]),
                                              tags=('oddrow',)
                                              )

    def insert_lot(self, treeview):
        popup = Tkinter.Tk()
        popup.title("Insert Lot")
        field_frame = Tkinter.Frame(popup)
        field_frame.pack()
        # Create type combo box entry and label
        type_options = ["<Select>",
                        "Ejector",
                        "Device",
                        "Component"]
        type_label = Tkinter.Label(field_frame, text="*Lot Type:", font=BODY_FONT)
        type_entry = ttk.Combobox(field_frame, value=type_options)
        type_entry.current(0)

        # Initialize other entries and labels
        title_label = Tkinter.Label(field_frame, text="Insert New Lot", font=TITLE_FONT)
        explanation_label = Tkinter.Label(field_frame,
                                          text="Fill out entries and click insert\n* entries mandatory",
                                          font=BODY_FONT)
        name_label = Tkinter.Label(field_frame, text="*Lot Name:", font=BODY_FONT)
        name_entry = Tkinter.Entry(field_frame)
        quantity_label = Tkinter.Label(field_frame, text="Quantity:", font=BODY_FONT)
        quantity_entry = Tkinter.Entry(field_frame)
        title_label.grid(row=0, column=0, sticky=Tkinter.NSEW, columnspan=2, padx=15, pady=15)
        explanation_label.grid(row=1, column=0, sticky=Tkinter.NSEW, columnspan=2, padx=15, pady=15)
        name_label.grid(row=2, column=0, sticky=Tkinter.E, padx=(15, 8))
        name_entry.grid(row=2, column=1, sticky=Tkinter.EW, padx=(8, 15))
        type_label.grid(row=3, column=0, sticky=Tkinter.E, padx=(15, 8))
        type_entry.grid(row=3, column=1, sticky=Tkinter.EW, padx=(8, 15))
        quantity_label.grid(row=4, column=0, sticky=Tkinter.E, padx=(15, 8))
        quantity_entry.grid(row=4, column=1, sticky=Tkinter.EW, padx=(8, 15))

        def collect_text():
            string = ["" for i in range(4)]
            string[0] = name_entry.get()
            string[2] = type_entry.get()
            string[3] = quantity_entry.get()
            return string

        def delete_boxtext():
            name_entry.delete(0, 'end')
            type_entry.current(0)
            quantity_entry.delete(0, 'end')

        # inserts data from textbox to server then updates table
        def insert_data():
            strings = collect_text()
            sql = "INSERT INTO lot (LotName, ParentLot_ID, LotType, Quantity)VALUES (%s,%s,%s,%s);"
            for i in range(len(strings)):  # check for empty strings label as NONE
                if (strings[i] == "" or strings[i] == "<Select>"):
                    strings[i] = None
            val = (strings[0], strings[1], strings[2], int(strings[3]))
            try:
                my_curs = self.create_connection()
                my_curs.execute(sql, val)
                self.my_connect.commit()
                delete_boxtext()
                self.update_lot(treeview)
            except mysql.connector.Error as e:
                self.error_popup(e)

        # Create cancel and insert buttons
        insert_button = Tkinter.Button(field_frame, text="Insert", command=insert_data)
        cancel_button = Tkinter.Button(field_frame, text="Cancel", command=popup.destroy)
        insert_button.grid(row=5, column=1, sticky="e", padx=10, pady=10)
        cancel_button.grid(row=5, column=0, sticky="w", padx=15, pady=15)

    def delete_lot(self, treeview):
        records = treeview.selection()
        if records:
            popup = Tkinter.Tk()
            popup.title("Confirm Changes")

            # delete string from table
            def deleteCompany():
                try:
                    for record in records:
                        my_curs = self.create_connection()
                        dat = (str(treeview.item(record, "values")[0]),)
                        sql = "DELETE FROM lot WHERE Lot_ID = %s"
                        val = (dat)
                        my_curs.execute(sql, val)
                        self.my_connect.commit()
                        self.update_lot(treeview)
                    popup.destroy()
                except mysql.connector.Error as e:
                    self.error_popup(e)

            frame = Tkinter.Frame(popup)
            label = Tkinter.Label(frame, text="Confirm Changes")
            confirm_button = Tkinter.Button(frame, text="Confirm", command=deleteCompany)
            cancel_button = Tkinter.Button(frame, text="Cancel", command=popup.destroy)
            label.pack(side='top', fill='y', pady=(15, 7.5))
            confirm_button.pack(side='left', fill='y', padx=15, pady=(7.5, 15))
            cancel_button.pack(side='right', fill='y', padx=15, pady=(7.5, 15))
            frame.pack()
        else:
            pass

    def modify_lot(self, treeview):
        record = treeview.selection()
        if len(record) == 1:
            popup = Tkinter.Tk()
            popup.title("Modify Lot")
            field_frame = Tkinter.Frame(popup)
            field_frame.pack()
            index = int(treeview.item(record, "values")[0])
            # Create type combo box entry and label
            type_options = ["<Select>",
                            "Ejector",
                            "Device",
                            "Component"]
            type_label = Tkinter.Label(field_frame, text="*Lot Type:", font=BODY_FONT)
            type_entry = ttk.Combobox(field_frame, value=type_options)
            type_entry.current(0)

            # Initialize other entries and labels
            title_label = Tkinter.Label(field_frame, text="Modify Lot", font=TITLE_FONT)
            explanation_label = Tkinter.Label(field_frame,
                                              text="Fill out entries and click insert\n* entries mandatory",
                                              font=BODY_FONT)
            name_label = Tkinter.Label(field_frame, text="*Lot Name:", font=BODY_FONT)
            name_entry = Tkinter.Entry(field_frame)
            quantity_label = Tkinter.Label(field_frame, text="Quantity:", font=BODY_FONT)
            quantity_entry = Tkinter.Entry(field_frame)
            title_label.grid(row=0, column=0, sticky=Tkinter.NSEW, columnspan=2, padx=15, pady=15)
            explanation_label.grid(row=1, column=0, sticky=Tkinter.NSEW, columnspan=2, padx=15, pady=15)
            name_label.grid(row=2, column=0, sticky=Tkinter.E, padx=(15, 8))
            name_entry.grid(row=2, column=1, sticky=Tkinter.EW, padx=(8, 15))
            type_label.grid(row=3, column=0, sticky=Tkinter.E, padx=(15, 8))
            type_entry.grid(row=3, column=1, sticky=Tkinter.EW, padx=(8, 15))
            quantity_label.grid(row=4, column=0, sticky=Tkinter.E, padx=(15, 8))
            quantity_entry.grid(row=4, column=1, sticky=Tkinter.EW, padx=(8, 15))

            def collect_text():
                string = ["" for i in range(4)]
                string[0] = name_entry.get()
                string[2] = type_entry.get()
                string[3] = quantity_entry.get()
                return string

            # modifies data from textbox to server then updates table
            def save_modification():
                if index >= 0:
                    data = collect_text()
                    sql = "UPDATE lot SET LotName = %s, " \
                          "ParentLot_ID = %s, LotType = %s, Quantity = %s " \
                          "WHERE Lot_ID = %s;"
                    for i in range(len(data)):
                        if data[i] == "" or data[i] == "None" or data[i] == "<Select>":
                            data[i] = None
                    val = (data[0], data[1], data[2], int(data[3]), index)
                    try:
                        my_curs = self.create_connection()
                        my_curs.execute(sql, val)
                        self.my_connect.commit()
                        self.update_lot(treeview)
                        popup.destroy()
                        self.confirmation_popup("Lots")
                    except mysql.connector.Error as e:
                        self.error_popup(e)
                else:
                    self.custom_error_popup("modify_record was used with negative index")

            def add_boxtext(data):
                name_entry.insert(0, str(data[1]))
                cur_type = data[3]
                switcher = {
                    "<Select>": 0,
                    "Ejector": 1,
                    "Device": 2,
                    "Component": 3
                }
                type_entry.current(switcher.get(cur_type, data[3]))
                quantity_entry.insert(0, str(data[4]))

            def modify_record():
                data = self.find_in_table("Lot", treeview.item(record, "values")[0])
                data = data[0]
                add_boxtext(data)

            # Create cancel and insert buttons
            insert_button = Tkinter.Button(field_frame, text="Save Modification", command=save_modification)
            cancel_button = Tkinter.Button(field_frame, text="Cancel", command=popup.destroy)
            insert_button.grid(row=5, column=1, sticky="e", padx=10, pady=10)
            cancel_button.grid(row=5, column=0, sticky="w", padx=15, pady=15)
            modify_record()
        else:
            self.custom_error_popup("Select one lot to modify")

    def update_lot(self, treeview):
        try:
            my_curs = self.create_connection()
            my_curs.execute("select * from lot order by Lot_ID ASC")
        except mysql.connector.Error as e:
            self.error_popup(e)
        string = ["" for i in range(5)]
        size = 0
        for i in treeview.get_children():
            treeview.delete(i)
        for lot in my_curs:
            size += 1
            string[0] = str(lot[0])
            string[1] = str(lot[1])
            string[2] = str(lot[3])
            string[3] = str(lot[4])
            if size % 2 == 0:
                treeview.insert('', 'end', iid=lot[0],
                                              values=(string[0], string[1], string[2], string[3], string[4]),
                                              tags=('evenrow',)
                                              )
            else:
                treeview.insert('', 'end', iid=lot[0],
                                              values=(string[0], string[1], string[2], string[3], string[4]),
                                              tags=('oddrow',)
                                              )

    def delete_shipment(self, treeview):
        records = treeview.selection()
        if records:
            popup = Tkinter.Tk()
            popup.title("Confirm Changes")

            # delete string from table
            def deleteCompany():
                try:
                    for record in records:
                        my_curs = self.create_connection()
                        dat = (str(treeview.item(record, "values")[0]),)
                        sql = "DELETE FROM shipment WHERE Shipment_ID = %s"
                        val = (dat)
                        my_curs.execute(sql, val)
                        self.my_connect.commit()
                        self.update_shipment(treeview)
                    popup.destroy()
                except mysql.connector.Error as e:
                    self.error_popup(e)

            frame = Tkinter.Frame(popup)
            label = Tkinter.Label(frame, text="Confirm Changes")
            confirm_button = Tkinter.Button(frame, text="Confirm", command=deleteCompany)
            cancel_button = Tkinter.Button(frame, text="Cancel", command=popup.destroy)
            label.pack(side='top', fill='y', pady=(15, 7.5))
            confirm_button.pack(side='left', fill='y', padx=15, pady=(7.5, 15))
            cancel_button.pack(side='right', fill='y', padx=15, pady=(7.5, 15))
            frame.pack()
        else:
            pass

    def modify_shipment(self, treeview):
        record = treeview.selection()
        if len(record) == 1:
            popup = Tkinter.Toplevel()
            popup.title("Modify Shipment")
            field_frame = Tkinter.Frame(popup)
            tree_frame = Tkinter.Frame(popup)
            popup.grid_rowconfigure(1, weight=1)
            popup.grid_columnconfigure(0, weight=1)
            field_frame.grid_columnconfigure(0, weight=1)
            field_frame.grid_columnconfigure(4, weight=1)
            field_frame.grid(row=0, column=0, sticky='nsew')
            tree_frame.grid(row=1, column=0, sticky='nsew')
            index = int(treeview.item(record, "values")[0])

            sender_frame = Tkinter.Frame(tree_frame)
            receiving_frame = Tkinter.Frame(tree_frame)
            service_frame = Tkinter.Frame(tree_frame)
            service_frame.grid_rowconfigure(1, weight=1)
            tree_frame.grid_rowconfigure(1, weight=1)
            sender_frame.grid(row=0, column=0, padx=10)
            receiving_frame.grid(row=0, column=1, padx=10)
            service_frame.grid(row=1, column=0, columnspan=2)

            # Set field frame
            header = Tkinter.Label(field_frame, text="Modify Existing Shipment", font=TITLE_FONT)
            instruction_label = Tkinter.Label(field_frame,
                                              text="Enter new date and tracking number then double click to select sender, receiving, and service from tables.",
                                              font=BODY_FONT)
            sender_label = Tkinter.Label(field_frame, text="Sender ID", font=BODY_FONT, fg="gray")
            receiving_label = Tkinter.Label(field_frame, text="Receiver ID", font=BODY_FONT, fg="gray")
            service_label = Tkinter.Label(field_frame, text="Service ID", font=BODY_FONT, fg="gray")
            date_label = Tkinter.Label(field_frame, text="Date", font=BODY_FONT)
            tracking_label = Tkinter.Label(field_frame, text="Tracking Number", font=BODY_FONT)
            sender_field = Tkinter.Entry(field_frame, state="disabled", justify='center')
            service_field = Tkinter.Entry(field_frame, state="disabled", justify='center')
            receiving_field = Tkinter.Entry(field_frame, state="disabled", justify='center')
            date_field = Tkinter.Entry(field_frame)
            tracking_field = Tkinter.Entry(field_frame)

            header.grid(row=0, column=1, sticky="ew", columnspan=3, pady=10)
            instruction_label.grid(row=1, column=1, sticky='ew', columnspan=3, pady=(0, 10))
            date_label.grid(row=2, column=1, sticky="ew")
            tracking_label.grid(row=2, column=2, sticky="ew")
            date_field.grid(row=3, column=1, sticky="ew")
            tracking_field.grid(row=3, column=2, sticky="ew")
            sender_label.grid(row=4, column=1, sticky="ew")
            receiving_label.grid(row=4, column=2, sticky="ew")
            service_label.grid(row=4, column=3, sticky="ew")
            sender_field.grid(row=5, column=1, sticky="ew")
            receiving_field.grid(row=5, column=2, sticky="ew")
            service_field.grid(row=5, column=3, sticky="ew")

            # declare style for treeview
            style = ttk.Style()
            style.theme_use("default")
            style.configure("Treeview", background="#d3d3d3", foreground="red", rowheight=25,
                            fieldbackground="#d3d3d3")
            style.map('Treeview', background=[('selected', 'black')])

            # Set tree for sender
            sender_title = Tkinter.Label(sender_frame, text="Sender", font=TITLE_FONT)
            sender_treescroll = Tkinter.Scrollbar(sender_frame)
            sender_tree = ttk.Treeview(sender_frame,
                                       columns=('Company ID', 'Company', 'Type', 'Country', 'Address'),
                                       yscrollcommand=sender_treescroll.set)
            sender_treescroll.config(command=sender_tree.yview)

            # Set tree for receiving
            receiving_title = Tkinter.Label(receiving_frame, text="Receiver", font=TITLE_FONT)
            receiving_treescroll = Tkinter.Scrollbar(receiving_frame)
            receiving_tree = ttk.Treeview(receiving_frame,
                                          columns=('Company ID', 'Company', 'Type', 'Country', 'Address'),
                                          yscrollcommand=receiving_treescroll.set)
            receiving_treescroll.config(command=receiving_tree.yview)

            # Set tree for service
            service_title = Tkinter.Label(service_frame, text="Service", font=TITLE_FONT)
            service_treescroll = Tkinter.Scrollbar(service_frame)
            service_tree = ttk.Treeview(service_frame,
                                        columns=('Company ID', 'Company', 'Type', 'Country', 'Address'),
                                        yscrollcommand=service_treescroll.set)
            service_treescroll.config(command=service_tree.yview)
            sender_title.grid(row=0, column=0, sticky="nsew", pady=10)
            receiving_title.grid(row=0, column=0, sticky="nsew", pady=10)
            service_title.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=10)
            sender_treescroll.grid(row=1, column=1, sticky="nse")
            receiving_treescroll.grid(row=1, column=1, sticky="nse")
            service_treescroll.grid(row=1, column=1, sticky="nse")

            sender_tree.heading('Company ID', text='Company ID', anchor=Tkinter.CENTER)
            sender_tree.heading('Company', text='Company', anchor=Tkinter.CENTER)
            sender_tree.heading('Type', text='Type', anchor=Tkinter.CENTER)
            sender_tree.heading('Country', text='Country', anchor=Tkinter.CENTER)
            sender_tree.heading('Address', text='Address', anchor=Tkinter.CENTER)
            sender_tree.column('#0', width=0, stretch=Tkinter.NO)
            sender_tree.column('Company ID', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
            sender_tree.column('Company', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=150)
            sender_tree.column('Type', width=100, stretch=Tkinter.NO, anchor=Tkinter.CENTER)
            sender_tree.column('Country', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
            sender_tree.column('Address', width=300, stretch=Tkinter.YES, anchor=Tkinter.CENTER)

            receiving_tree.heading('Company ID', text='Company ID', anchor=Tkinter.CENTER)
            receiving_tree.heading('Company', text='Company', anchor=Tkinter.CENTER)
            receiving_tree.heading('Type', text='Type', anchor=Tkinter.CENTER)
            receiving_tree.heading('Country', text='Country', anchor=Tkinter.CENTER)
            receiving_tree.heading('Address', text='Address', anchor=Tkinter.CENTER)
            receiving_tree.column('#0', width=0, stretch=Tkinter.NO)
            receiving_tree.column('Company ID', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
            receiving_tree.column('Company', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=150)
            receiving_tree.column('Type', width=100, stretch=Tkinter.NO, anchor=Tkinter.CENTER)
            receiving_tree.column('Country', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
            receiving_tree.column('Address', width=300, stretch=Tkinter.YES, anchor=Tkinter.CENTER)

            service_tree.heading('Company ID', text='Company ID', anchor=Tkinter.CENTER)
            service_tree.heading('Company', text='Company', anchor=Tkinter.CENTER)
            service_tree.heading('Type', text='Type', anchor=Tkinter.CENTER)
            service_tree.heading('Country', text='Country', anchor=Tkinter.CENTER)
            service_tree.heading('Address', text='Address', anchor=Tkinter.CENTER)
            service_tree.column('#0', width=0, stretch=Tkinter.NO)
            service_tree.column('Company ID', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
            service_tree.column('Company', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=150)
            service_tree.column('Type', width=100, stretch=Tkinter.NO, anchor=Tkinter.CENTER)
            service_tree.column('Country', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
            service_tree.column('Address', width=300, stretch=Tkinter.YES, anchor=Tkinter.CENTER)

            sender_tree.tag_configure('oddrow', background="white")
            sender_tree.tag_configure('evenrow', background="lightblue")
            receiving_tree.tag_configure('oddrow', background="white")
            receiving_tree.tag_configure('evenrow', background="lightblue")
            service_tree.tag_configure('oddrow', background="white")
            service_tree.tag_configure('evenrow', background="lightblue")

            sender_tree.grid(row=1, column=0, sticky="nsew")
            receiving_tree.grid(row=1, column=0, sticky="nsew")
            service_tree.grid(row=1, column=0, sticky="nsew")

            def sel_sender(event):
                sender_record = sender_tree.selection()
                if len(sender_record) == 1:
                    string = self.find_in_table("Company", sender_tree.item(sender_record, "values")[0])
                    sender_field['state'] = 'normal'
                    sender_field.delete(0, 'end')
                    sender_field.insert(0, string[0][0])
                    sender_field['state'] = 'disabled'
                    sender_label['fg'] = 'black'
                else:
                    pass

            def sel_receiver(event):
                receiver_record = receiving_tree.selection()
                if len(receiver_record) == 1:
                    string = self.find_in_table("Company", receiving_tree.item(receiver_record, "values")[0])
                    receiving_field['state'] = 'normal'
                    receiving_field.delete(0, 'end')
                    receiving_field.insert(0, string[0][0])
                    receiving_field['state'] = 'disabled'
                    receiving_label['fg'] = 'black'
                else:
                    pass

            def sel_service(event):
                service_record = service_tree.selection()
                if len(service_record) == 1:
                    string = self.find_in_table("Company", service_tree.item(service_record, "values")[0])
                    service_field['state'] = 'normal'
                    service_field.delete(0, 'end')
                    service_field.insert(0, string[0][0])
                    service_field['state'] = 'disabled'
                    service_label['fg'] = 'black'
                else:
                    pass

            def add_boxtext(string):
                sender_field['state'] = 'normal'
                receiving_field['state'] = 'normal'
                service_field['state'] = 'normal'
                date_field.insert(0, str(string[0][3]))
                tracking_field.insert(0, str(string[0][5]))
                sender_field.insert(0, str(string[0][2]))
                receiving_field.insert(0, str(string[0][1]))
                service_field.insert(0, str(string[0][4]))
                sender_field['state'] = 'disabled'
                receiving_field['state'] = 'disabled'
                service_field['state'] = 'disabled'
                sender_field['disabledbackground'] = 'white'
                receiving_field['disabledbackground'] = 'white'
                service_field['disabledbackground'] = 'white'
                sender_label['fg'] = 'black'
                receiving_label['fg'] = 'black'
                service_label['fg'] = 'black'

            def collect_text():
                string = ["" for i in range(5)]
                string[2] = date_field.get()
                string[4] = tracking_field.get()
                string[1] = sender_field.get()
                string[0] = receiving_field.get()
                string[3] = service_field.get()
                return string

            def save_modification():
                if sender_field.get() != receiving_field.get():
                    if index >= 0:
                        data = collect_text()
                        sql = "UPDATE shipment SET ReceivingCompany_ID = %s, " \
                              "Sender_ID = %s, Date = %s, ShippingCompany_ID = %s, TrackingNumber = %s " \
                              "WHERE Shipment_ID = %s;"
                        for i in range(len(data)):
                            if data[i] == "" or data[i] == "None" or data[i] == "<Select>":
                                data[i] = None
                        val = (int(data[0]), int(data[1]), data[2], int(data[3]), int(data[4]), index)
                        try:
                            my_curs = self.create_connection()
                            my_curs.execute(sql, val)
                            self.my_connect.commit()
                            self.update_shipment(treeview)
                            popup.destroy()
                            self.confirmation_popup("Shipments")
                        except mysql.connector.Error as e:
                            self.error_popup(e)
                    else:
                        self.custom_error_popup("modify_record was used with negative index")
                else:
                    self.custom_error_popup("Sender cannot be the same as receiver")

            def modify_record():
                string = self.find_in_table("Shipment", treeview.item(record, "values")[0])
                add_boxtext(string)
            # buttons and bindings
            submit_button = Tkinter.Button(field_frame, text="Submit", command=save_modification)
            submit_button.grid(row=6, column=0, columnspan=3, sticky="n", pady=(10, 0))
            sender_tree.bind("<Double-1>", sel_sender)
            receiving_tree.bind("<Double-1>", sel_receiver)
            service_tree.bind("<Double-1>", sel_service)

            self.update_company(sender_tree, "no shipper")
            self.update_company(receiving_tree, "no shipper")
            self.update_company(service_tree, "only shipper")
            modify_record()
        else:
            self.custom_error_popup("Select one shipment to modify")

    def update_shipment(self, treeview):
        try:
            my_curs = self.create_connection()
            my_curs.execute("select * from shipment order by Date DESC")
        except mysql.connector.Error as e:
            self.error_popup(e)
        string = ["" for i in range(6)]
        size = 0
        for i in treeview.get_children():
            treeview.delete(i)
        for shipment in my_curs:
            size += 1
            string[0] = str(shipment[0])
            string[1] = self.find_companyname(shipment[2])
            string[2] = self.find_companyname(shipment[1])
            string[3] = self.find_companyname(shipment[4])
            print(str(shipment[2]))
            string[4] = str(shipment[3])
            string[5] = str(shipment[5])

            if size % 2 == 0:
                treeview.insert('', 'end', iid=shipment[0],
                                              values=(string[0], string[1], string[2], string[3], string[4], string[5]),
                                              tags=('evenrow',)
                                              )
            else:
                treeview.insert('', 'end', iid=shipment[0],
                                              values=(string[0], string[1], string[2], string[3], string[4], string[5]),
                                              tags=('oddrow',)
                                              )

    def insert_shipment(self, treeview):
        popup = Tkinter.Toplevel()
        popup.geometry('%dx%d+0+0' % (popup.winfo_screenwidth(), popup.winfo_screenheight()))
        popup.title("Insert Shipment")
        field_frame = Tkinter.Frame(popup)
        tree_frame = Tkinter.Frame(popup)
        popup.grid_rowconfigure(1, weight=1)
        popup.grid_columnconfigure(0, weight=1)
        field_frame.grid_columnconfigure(0, weight=1)
        field_frame.grid_columnconfigure(4, weight=1)
        field_frame.grid(row=0, column=0, sticky='nsew')
        tree_frame.grid(row=1, column=0, sticky='nsew')

        sender_frame = Tkinter.Frame(tree_frame)
        receiving_frame = Tkinter.Frame(tree_frame)
        service_frame = Tkinter.Frame(tree_frame)
        service_frame.grid_rowconfigure(1, weight=1)
        tree_frame.grid_rowconfigure(1, weight=1)
        sender_frame.grid(row=0, column=0, padx=10)
        receiving_frame.grid(row=0, column=1, padx=10)
        service_frame.grid(row=1, column=0, columnspan=2)


        # Set field frame
        header = Tkinter.Label(field_frame, text="Insert New Shipment", font=TITLE_FONT)
        instruction_label = Tkinter.Label(field_frame,
            text="Enter date and tracking number then double click to select sender, receiving, and service from tables.",
            font=BODY_FONT)
        sender_label = Tkinter.Label(field_frame, text="Sender ID", font=BODY_FONT, fg="gray")
        receiving_label = Tkinter.Label(field_frame, text="Receiver ID", font=BODY_FONT, fg="gray")
        service_label = Tkinter.Label(field_frame, text="Service ID", font=BODY_FONT, fg="gray")
        date_label = Tkinter.Label(field_frame, text="Date", font=BODY_FONT)
        tracking_label = Tkinter.Label(field_frame, text="Tracking Number", font=BODY_FONT)
        sender_field = Tkinter.Entry(field_frame, state="disabled", justify='center')
        service_field = Tkinter.Entry(field_frame, state="disabled", justify='center')
        receiving_field = Tkinter.Entry(field_frame, state="disabled", justify='center')
        date_field = Tkinter.Entry(field_frame)
        tracking_field = Tkinter.Entry(field_frame)

        header.grid(row=0, column=1, sticky= "ew", columnspan=3, pady=10)
        instruction_label.grid(row=1, column=1, sticky='ew', columnspan=3, pady=(0,10))
        date_label.grid(row=2, column=1, sticky="ew")
        tracking_label.grid(row=2, column=2, sticky="ew")
        date_field.grid(row=3, column=1, sticky="ew")
        tracking_field.grid(row=3, column=2, sticky="ew")
        sender_label.grid(row=4, column=1, sticky="ew")
        receiving_label.grid(row=4, column=2, sticky="ew")
        service_label.grid(row=4, column=3, sticky="ew")
        sender_field.grid(row=5, column=1, sticky="ew")
        receiving_field.grid(row=5, column=2, sticky="ew")
        service_field.grid(row=5, column=3, sticky="ew")

        # declare style for treeview
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#d3d3d3", foreground="red", rowheight=25,
                        fieldbackground="#d3d3d3")
        style.map('Treeview', background=[('selected', 'black')])

        # Set tree for sender
        sender_title = Tkinter.Label(sender_frame, text="Sender", font=TITLE_FONT)
        sender_treescroll = Tkinter.Scrollbar(sender_frame)
        sender_tree = ttk.Treeview(sender_frame,
                                 columns=('Company ID', 'Company', 'Type', 'Country', 'Address'),
                                 yscrollcommand=sender_treescroll.set)
        sender_treescroll.config(command=sender_tree.yview)

        # Set tree for receiving
        receiving_title = Tkinter.Label(receiving_frame, text="Receiver", font=TITLE_FONT)
        receiving_treescroll = Tkinter.Scrollbar(receiving_frame)
        receiving_tree = ttk.Treeview(receiving_frame,
                                 columns=('Company ID', 'Company', 'Type', 'Country', 'Address'),
                                 yscrollcommand=receiving_treescroll.set)
        receiving_treescroll.config(command=receiving_tree.yview)

        # Set tree for service
        service_title = Tkinter.Label(service_frame, text="Service", font=TITLE_FONT)
        service_treescroll = Tkinter.Scrollbar(service_frame)
        service_tree = ttk.Treeview(service_frame,
                                 columns=('Company ID', 'Company', 'Type', 'Country', 'Address'),
                                 yscrollcommand=service_treescroll.set)
        service_treescroll.config(command=service_tree.yview)
        sender_title.grid(row=0, column=0, sticky="nsew", pady=10)
        receiving_title.grid(row=0, column=0, sticky="nsew", pady=10)
        service_title.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=10)
        sender_treescroll.grid(row=1, column=1, sticky="nse")
        receiving_treescroll.grid(row=1, column=1, sticky="nse")
        service_treescroll.grid(row=1, column=1, sticky="nse")

        sender_tree.heading('Company ID', text='Company ID', anchor=Tkinter.CENTER)
        sender_tree.heading('Company', text='Company', anchor=Tkinter.CENTER)
        sender_tree.heading('Type', text='Type', anchor=Tkinter.CENTER)
        sender_tree.heading('Country', text='Country', anchor=Tkinter.CENTER)
        sender_tree.heading('Address', text='Address', anchor=Tkinter.CENTER)
        sender_tree.column('#0', width=0, stretch=Tkinter.NO)
        sender_tree.column('Company ID', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        sender_tree.column('Company', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=150)
        sender_tree.column('Type', width=100, stretch=Tkinter.NO, anchor=Tkinter.CENTER)
        sender_tree.column('Country', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        sender_tree.column('Address', width=300, stretch=Tkinter.YES, anchor=Tkinter.CENTER)

        receiving_tree.heading('Company ID', text='Company ID', anchor=Tkinter.CENTER)
        receiving_tree.heading('Company', text='Company', anchor=Tkinter.CENTER)
        receiving_tree.heading('Type', text='Type', anchor=Tkinter.CENTER)
        receiving_tree.heading('Country', text='Country', anchor=Tkinter.CENTER)
        receiving_tree.heading('Address', text='Address', anchor=Tkinter.CENTER)
        receiving_tree.column('#0', width=0, stretch=Tkinter.NO)
        receiving_tree.column('Company ID', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        receiving_tree.column('Company', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=150)
        receiving_tree.column('Type', width=100, stretch=Tkinter.NO, anchor=Tkinter.CENTER)
        receiving_tree.column('Country', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        receiving_tree.column('Address', width=300, stretch=Tkinter.YES, anchor=Tkinter.CENTER)

        service_tree.heading('Company ID', text='Company ID', anchor=Tkinter.CENTER)
        service_tree.heading('Company', text='Company', anchor=Tkinter.CENTER)
        service_tree.heading('Type', text='Type', anchor=Tkinter.CENTER)
        service_tree.heading('Country', text='Country', anchor=Tkinter.CENTER)
        service_tree.heading('Address', text='Address', anchor=Tkinter.CENTER)
        service_tree.column('#0', width=0, stretch=Tkinter.NO)
        service_tree.column('Company ID', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        service_tree.column('Company', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=150)
        service_tree.column('Type', width=100, stretch=Tkinter.NO, anchor=Tkinter.CENTER)
        service_tree.column('Country', stretch=Tkinter.NO, anchor=Tkinter.CENTER, width=80)
        service_tree.column('Address', width=300, stretch=Tkinter.YES, anchor=Tkinter.CENTER)

        sender_tree.tag_configure('oddrow', background="white")
        sender_tree.tag_configure('evenrow', background="lightblue")
        receiving_tree.tag_configure('oddrow', background="white")
        receiving_tree.tag_configure('evenrow', background="lightblue")
        service_tree.tag_configure('oddrow', background="white")
        service_tree.tag_configure('evenrow', background="lightblue")

        sender_tree.grid(row=1, column=0, sticky="nsew")
        receiving_tree.grid(row=1, column=0, sticky="nsew")
        service_tree.grid(row=1, column=0, sticky="nsew")

        def refresh_button():
            pass

        def sel_sender(event):
            record = sender_tree.selection()
            if len(record) == 1:
                string = self.find_in_table("Company", sender_tree.item(record, "values")[0])
                sender_field['state'] = 'normal'
                sender_field.delete(0, 'end')
                sender_field.insert(0, string[0][0])
                sender_field['state'] = 'disabled'
                sender_field['disabledbackground'] = 'white'
                sender_label['fg'] = 'black'
            else:
                pass
        def sel_receiver(event):
            record = receiving_tree.selection()
            if len(record) == 1:
                string = self.find_in_table("Company", receiving_tree.item(record, "values")[0])
                receiving_field['state'] = 'normal'
                receiving_field.delete(0, 'end')
                receiving_field.insert(0, string[0][0])
                receiving_field['state'] = 'disabled'
                receiving_field['disabledbackground'] = 'white'
                receiving_label['fg'] = 'black'
                refresh_button()
            else:
                pass

        def sel_service(event):
            record = service_tree.selection()
            if len(record) == 1:
                string = self.find_in_table("Company", service_tree.item(record, "values")[0])
                service_field['state'] = 'normal'
                service_field.delete(0, 'end')
                service_field.insert(0, string[0][0])
                service_field['state'] = 'disabled'
                service_field['disabledbackground'] = 'white'
                service_label['fg'] = 'black'
            else:
                pass

        def delete_boxtext():
            date_field.delete(0, 'end')
            tracking_field.delete(0, 'end')
            sender_field.delete(0, 'end')
            receiving_field.delete(0, 'end')
            service_field.delete(0, 'end')

        def insert_shipment():
            if sender_field.get() != receiving_field.get():
                string = ["" for i in range(5)]
                string[0] = receiving_field.get()
                string[1] = sender_field.get()
                string[2] = self.format_date(date_field.get())
                string[3] = service_field.get()
                string[4] = tracking_field.get()
                sql = "INSERT INTO shipment (ReceivingCompany_ID, Sender_ID, Date, ShippingCompany_ID, TrackingNumber)VALUES (%s,%s,%s,%s,%s);"
                val = (int(string[0]), int(string[1]), string[2], int(string[3]), int(string[4]))
                try:
                    my_curs = self.create_connection()
                    my_curs.execute(sql, val)
                    self.my_connect.commit()
                    self.update_shipment(treeview)
                    delete_boxtext()
                    self.confirmation_popup("Shipments")
                except mysql.connector.Error as e:
                    self.error_popup(e)
                self.update_company(sender_tree, "no shipper")
                self.update_company(receiving_tree, "no shipper")
                self.update_company(service_tree, "only shipper")
            else:
                self.custom_error_popup("Sender and Receiver may not have the same ID")
        # buttons and bindings
        submit_button = Tkinter.Button(field_frame, text="Submit", command=insert_shipment)
        submit_button.grid(row=6, column=0, columnspan=3, sticky="n", pady=(10, 0))
        sender_tree.bind("<Double-1>", sel_sender)
        receiving_tree.bind("<Double-1>", sel_receiver)
        service_tree.bind("<Double-1>", sel_service)

        self.update_company(sender_tree, "no shipper")
        self.update_company(receiving_tree, "no shipper")
        self.update_company(service_tree, "only shipper")

    def confirmation_popup(self, tablename):
        popup = Tkinter.Tk()
        popup.title("Confirmation")
        message = Tkinter.Label(popup, text="", fg='black')
        close = Tkinter.Button(popup, text="Close", command=popup.destroy)
        message['text'] = "Your record has been saved in " + tablename
        message.pack(pady=(15, 7), padx=15)
        close.pack(pady=(7, 15))

    # Input revision id, return list of associated component id's
    def revision_components(self, revision_id):
        components = []
        my_curs = self.create_connection()
        i = 0
        try:

            my_curs.execute('SELECT * FROM revision_component WHERE Revision_ID = %s', (revision_id,))
        except mysql.connector.Error as e:
            self.error_popup(e)
        for component in my_curs:
            components[i] = component[1]
            ++i
        print(components)
        return components

    def find_companyname(self, id):
        try:
            my_curs = self.create_connection()
            sql = "select Name from company where Company_ID = %s;"
            val = (id, )
            my_curs.execute(sql, val)
            return str(my_curs.fetchone()[0])
        except mysql.connector.Error as e:
            self.error_popup(e)

    def create_connection(self):
        return self.my_connect.cursor(buffered=True)

app = SeaofBTCapp()
app.mainloop()