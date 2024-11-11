from ttkbootstrap import Toplevel, Frame, Label, Entry, Button
from ttkbootstrap import Treeview, Scrollbar
from src import dba as db


class MyUsers(Toplevel):
    def __init__(self, parent):
        super().__init__(title="Users Information", resizable=(False, False))

        self.build_users()
        self.transient(parent)
        self.grab_set()
        self.focus()

        self.load_users()

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

        self.idEntry = Entry(self.entryFrame, width=8, justify="center",
                             state="disabled")
        self.idEntry.grid(row=1, column=0, padx=(0, 15))

        self.nameEntry = Entry(self.entryFrame, width=40, state="disabled")
        self.nameEntry.grid(row=1, column=1)

        self.passwordEntry = Entry(self.entryFrame, width=20, state="disabled")
        self.passwordEntry.grid(row=3, column=1, padx=(0, 15), pady=(15, 0),
                                sticky="w")

        # Buttons Frame
        self.btnFrame = Frame(self)
        self.btnFrame.grid(row=1, column=1, padx=(20, 20), pady=(20, 20))

        self.btnNew = Button(self.btnFrame, width=15, text="New",
                             command=self.new_users)
        self.btnNew.grid(row=0, column=0, padx=(0, 20), pady=(0, 20))

        self.btnPassword = Button(self.btnFrame, width=15, text="Password",
                                  state="disabled", bootstyle="info")
        self.btnPassword.grid(row=0, column=1, pady=(0, 20))

        self.btnSave = Button(self.btnFrame, width=15, text="Save",
                              command=self.save_users, state="disabled",
                              bootstyle="success")
        self.btnSave.grid(row=1, column=0, padx=(0, 20), pady=(0, 20))

        self.btnDelete = Button(self.btnFrame, width=15, text="Delete",
                                state="disabled", bootstyle="outline-danger")
        self.btnDelete.grid(row=1, column=1, pady=(0, 20))

        self.btnCancel = Button(self.btnFrame, width=15, text="Cancel",
                                command=self.cancel_users, state="disabled",
                                bootstyle="warning")
        self.btnCancel.grid(row=2, column=0, padx=(0, 20))

        self.btnClose = Button(self.btnFrame, width=15, text="Close",
                               command=self.destroy, bootstyle="light")
        self.btnClose.grid(row=2, column=1)

    def load_users(self):
        dataUsers = db.retrieve_info()

        if dataUsers:
            self.tblUser.delete(*self.tblUser.get_children())

            for item in dataUsers:
                self.tblUser.insert("", index="end", text=item[0],
                                    values=[item[0], item[1]])

    def new_users(self):
        self.enable_entries()
        self.btnNew.config(state="disabled")
        self.btnSave.config(state="normal")
        self.btnCancel.config(state="normal")
        self.idEntry.focus()

    def save_users(self):
        db.insert_info(self.idEntry.get(), self.nameEntry.get(),
                       self.passwordEntry.get())
        self.cancel_users()
        self.load_users()

    def cancel_users(self):
        self.clear_entries()
        self.disable_entries()

        self.btnPassword.config(state="disabled")
        self.btnNew.config(state="normal")
        self.btnSave.config(state="disabled")
        self.btnDelete.config(state="disabled")
        self.btnCancel.config(state="disabled")

    def enable_entries(self):
        self.idEntry.config(state="normal", bootstyle="success")
        self.nameEntry.config(state="normal", bootstyle="success")
        self.passwordEntry.config(state="normal", bootstyle="success")

    def disable_entries(self):
        self.idEntry.config(state="disabled", bootstyle="default")
        self.nameEntry.config(state="disabled", bootstyle="default")
        self.passwordEntry.config(state="disabled", bootstyle="default")

    def clear_entries(self):
        self.idEntry.delete(0, "end")
        self.nameEntry.delete(0, "end")
        self.passwordEntry.delete(0, "end")
