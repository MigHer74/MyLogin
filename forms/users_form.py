from ttkbootstrap import Toplevel, Frame, Label, Entry


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
