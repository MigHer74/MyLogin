from ttkbootstrap import Toplevel, Frame, Label, Entry, Button
from ttkbootstrap import Treeview, Scrollbar
from ttkbootstrap.dialogs.dialogs import Messagebox
from src import dba as db
from src import tools as tl


class MyUsers(Toplevel):
    def __init__(self, parent):
        super().__init__(title="Users Information", resizable=(False, False))

        self.build_users()
        self.place_window_center()
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

        self.tblUser.bind("<Double-Button-1>", self.select_modify)
        self.tblUser.bind("<<TreeviewSelect>>", self.select_delete)

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
                                  command=self.change_password,
                                  state="disabled", bootstyle="info")
        self.btnPassword.grid(row=0, column=1, pady=(0, 20))

        self.btnSave = Button(self.btnFrame, width=15, text="Save",
                              command=self.save_users, state="disabled",
                              bootstyle="success")
        self.btnSave.grid(row=1, column=0, padx=(0, 20), pady=(0, 20))

        self.btnDelete = Button(self.btnFrame, width=15, text="Delete",
                                command=self.delete_users, state="disabled",
                                bootstyle="outline-danger")
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

    def select_delete(self, event):
        self.keyUser = self.tblUser.item(self.tblUser.focus(), "text")

        if self.keyUser != "":
            self.btnDelete.config(state="normal")
            self.btnPassword.config(state="normal")

    def select_modify(self, event):
        self.keyUser = self.tblUser.item(self.tblUser.focus(), "text")

        if self.keyUser != "":
            self.saveType = "Modify"

            self.tblUser.config(selectmode="none")
            self.tblUser.unbind("<Double-Button-1>")
            self.tblUser.unbind("<<TreeviewSelect>>")

            self.btnNew.config(state="disabled")
            self.btnPassword.config(state="disabled")
            self.btnSave.config(state="normal")
            self.btnCancel.config(state="normal")
            self.btnDelete.config(state="disabled")

            modifyUser = db.retrieve_info(self.keyUser)

            self.enable_entries()
            self.clear_entries()

            self.idEntry.insert(0, modifyUser[0])
            self.nameEntry.insert(0, modifyUser[1])

            self.idEntry.config(state="disabled", bootstyle="default")
            self.passwordEntry.config(state="disabled", bootstyle="default")

    def new_users(self):
        self.saveType = "New"
        self.enable_entries()
        self.btnNew.config(state="disabled")
        self.btnPassword.config(state="disabled")
        self.btnSave.config(state="normal")
        self.btnCancel.config(state="normal")
        self.btnDelete.config(state="disabled")
        self.idEntry.focus()

    def change_password(self):
        self.saveType = "Change"
        self.keyUser = self.tblUser.item(self.tblUser.focus(), "text")

        self.tblUser.config(selectmode="none")
        self.tblUser.unbind("<Double-Button-1>")
        self.tblUser.unbind("<<TreeviewSelect>>")

        self.btnNew.config(state="disabled")
        self.btnPassword.config(state="disabled")
        self.btnSave.config(state="normal")
        self.btnCancel.config(state="normal")
        self.btnDelete.config(state="disabled")

        changeUser = db.retrieve_info(self.keyUser)

        self.enable_entries()
        self.clear_entries()

        self.idEntry.insert(0, changeUser[0])
        self.nameEntry.insert(0, changeUser[1])

        self.idEntry.config(state="disabled", bootstyle="default")
        self.nameEntry.config(state="disabled", bootstyle="default")

        self.passwordEntry.focus()

    def save_users(self):
        if self.saveType == "New":
            userPassword = tl.hashing_password(self.passwordEntry.get())
            db.insert_info(self.idEntry.get(), self.nameEntry.get(),
                           userPassword)
            self.update_master()
        elif self.saveType == "Modify":
            db.update_info(self.idEntry.get(), self.nameEntry.get())
        elif self.saveType == "Change":
            userPassword = tl.hashing_password(self.passwordEntry.get())
            db.update_password(self.keyUser, userPassword)

        self.saveType = None

        self.cancel_users()
        self.load_users()

        self.focus()

    def delete_users(self):
        deleteUser = db.retrieve_info(self.keyUser)

        msgUser = f"Do you want to delete {deleteUser[1]} user info ?."

        answer_user = Messagebox.show_question(message=msgUser,
                                               title="Delete User", alert=True,
                                               buttons=['Yes:success',
                                                        'No:outline-danger'],
                                               parent=self)

        if answer_user != "No":
            db.delete_info(self.keyUser)
            self.load_users()

        self.btnPassword.config(state="disabled")
        self.btnNew.config(state="normal")
        self.btnSave.config(state="disabled")
        self.btnDelete.config(state="disabled")
        self.btnCancel.config(state="disabled")

        self.focus()

    def cancel_users(self):
        self.enable_entries()
        self.clear_entries()
        self.disable_entries()

        self.tblUser.config(selectmode="browse")
        self.tblUser.bind("<Double-Button-1>", self.select_modify)
        self.tblUser.bind("<<TreeviewSelect>>", self.select_delete)

        self.btnPassword.config(state="disabled")
        self.btnNew.config(state="normal")
        self.btnSave.config(state="disabled")
        self.btnDelete.config(state="disabled")
        self.btnCancel.config(state="disabled")

        self.focus()

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

    def update_master(self):
        dataUsers = []
        loadUsers = db.retrieve_info()

        if loadUsers:
            for user in loadUsers:
                dataUsers.append(user[1])

        self.master.nameCombo.config(values=dataUsers, state="readonly")
        self.master.passwordEntry.config(state="normal")
