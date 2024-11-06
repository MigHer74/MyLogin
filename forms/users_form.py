from ttkbootstrap import Toplevel, Frame, Label, Entry, Treeview, Scrollbar


class MyUsers(Toplevel):
    def __init__(self, parent):
        super().__init__(title="Users Information", resizable=(False, False))

        self.build_users()
        self.transient(parent)
        self.grab_set()
        self.focus()

    def build_users(self):
        # User Data Frame
        self.entryFrame = Frame(self)
        self.entryFrame.grid(row=0, column=0)

        self.idLabel = Label(self.entryFrame, text="User Id")
        self.idLabel.grid(row=0, column=0)

        self.nameLabel = Label(self.entryFrame, text="User Name")
        self.nameLabel.grid(row=0, column=1)

        self.idEntry = Entry(self.entryFrame, width=8, justify="center")
        self.idEntry.grid(row=1, column=0)

        self.nameEntry = Entry(self.entryFrame, width=40)
        self.nameEntry.grid(row=1, column=1)

        # Users List Frame
        self.tblFrame = Frame(self)
        self.tblFrame.grid(row=1, column=0)

        self.tblUser = Treeview(self.tblFrame, columns=(1, 2),
                                show="headings", height=15,
                                selectmode="browse")

        self.tblUser.heading(1, text="Id")
        self.tblUser.heading(2, text="Name")

        self.tblUser.column(1, width=100)
        self.tblUser.column(2, width=200)

        self.tblUser.pack(side="left")

        # ScrollBar
        self.sbrUser = Scrollbar(self.tblFrame, orient="vertical")
        self.sbrUser.pack(side="right", fill="y")

        self.tblUser.config(yscrollcommand=self.sbrUser.set)
        self.sbrUser.config(command=self.tblUser.yview)
