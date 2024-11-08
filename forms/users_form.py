from ttkbootstrap import Toplevel, Frame, Label, Entry, Button
from ttkbootstrap import Treeview, Scrollbar


class MyUsers(Toplevel):
    def __init__(self, parent):
        super().__init__(title="Users Information", resizable=(False, False))

        self.build_users()
        self.transient(parent)
        self.grab_set()
        self.focus()

    def build_users(self):
        # Users List Frame
        self.tblFrame = Frame(self)
        self.tblFrame.grid(row=0, rowspan=2, column=0,
                           padx=(20, 0), pady=(20, 20))

        self.tblUser = Treeview(self.tblFrame, columns=(1, 2),
                                show="headings", height=15,
                                selectmode="browse")

        self.tblUser.heading(1, text="Id")
        self.tblUser.heading(2, text="Name")

        self.tblUser.column(1, width=100)
        self.tblUser.column(2, width=200)

        self.tblUser.pack(side="left")

        # ScrollBar
        self.sbrUser = Scrollbar(self.tblFrame, orient="vertical",
                                 bootstyle="round")
        self.sbrUser.pack(side="right", fill="y")

        self.tblUser.config(yscrollcommand=self.sbrUser.set)
        self.sbrUser.config(command=self.tblUser.yview)

        # User Data Frame
        self.entryFrame = Frame(self)
        self.entryFrame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0),
                             sticky="n")

        self.idLabel = Label(self.entryFrame, text="User Id")
        self.idLabel.grid(row=0, column=0, padx=(0, 15))

        self.nameLabel = Label(self.entryFrame, text="User Name")
        self.nameLabel.grid(row=0, column=1)

        self.passwordLabel = Label(self.entryFrame, text="Password")
        self.passwordLabel.grid(row=3, column=0, padx=(0, 15), pady=(15, 0),
                                sticky="w")

        self.idEntry = Entry(self.entryFrame, width=8, justify="center")
        self.idEntry.grid(row=1, column=0, padx=(0, 15))

        self.nameEntry = Entry(self.entryFrame, width=40)
        self.nameEntry.grid(row=1, column=1)

        self.passwordEntry = Entry(self.entryFrame, width=20)
        self.passwordEntry.grid(row=3, column=1, padx=(0, 15), pady=(15, 0),
                                sticky="w")

        # Buttons Frame
        self.btnFrame = Frame(self)
        self.btnFrame.grid(row=1, column=1)

        self.btnNew = Button(self.btnFrame, width=15, text="New")
        self.btnNew.grid(row=0, column=0)

        self.btnPassword = Button(self.btnFrame, width=15, text="Password")
        self.btnPassword.grid(row=0, column=1)

        self.btnSave = Button(self.btnFrame, width=15, text="Save")
        self.btnSave.grid(row=1, column=0)

        self.btnDelete = Button(self.btnFrame, width=15, text="Delete")
        self.btnDelete.grid(row=1, column=1)

        self.btnCancel = Button(self.btnFrame, width=15, text="Cancel")
        self.btnCancel.grid(row=2, column=0)

        self.btnClose = Button(self.btnFrame, width=15, text="Close")
        self.btnClose.grid(row=2, column=1)
