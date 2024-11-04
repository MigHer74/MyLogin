from ttkbootstrap import Window, Frame, Label, Entry, Button
from src import tools as tl


class MyLogin(Window):
    def __init__(self):
        super().__init__(title="MyLogin", resizable=(False, False),
                         themename="superhero")
        self.build_login()

    def build_login(self):
        # Title Frame
        titleFrame = Frame(self)
        titleFrame.grid(row=0, column=0, columnspan=2, pady=(15, 0))

        titleLabel = Label(titleFrame, text="Login",
                           font=("Centura", 30, "bold"))
        titleLabel.pack()

        # Image Frame
        imageFrame = Frame(self)
        imageFrame.grid(row=1, column=0)

        self.imageLogin = tl.image_resize("./img/monitor.png", 250, 250)

        imageLabel = Label(imageFrame, image=self.imageLogin)
        imageLabel.pack()

        # Entries Frame
        entriesFrame = Frame(self)
        entriesFrame.grid(row=1, column=1)

        nameLabel = Label(entriesFrame, text="User Name")
        nameLabel.grid(row=0, column=0)

        nameEntry = Entry(entriesFrame, width=25)
        nameEntry.grid(row=1, column=0)

        passwordLabel = Label(entriesFrame, text="Password")
        passwordLabel.grid(row=2, column=0)

        passwordEntry = Entry(entriesFrame, width=25)
        passwordEntry.grid(row=3, column=0)

        # Buttons Frame
        buttonsFrame = Frame(self)
        buttonsFrame.grid(row=2, column=1)

        buttonAccess = Button(buttonsFrame, width=15, text="Access")
        buttonAccess.grid(row=0, column=0)

        buttonCancel = Button(buttonsFrame, width=15, text="Cancel")
        buttonCancel.grid(row=1, column=0)

        # Add User Frame
        addUserFrame = Frame(self)
        addUserFrame.grid(row=3, column=1)

        self.imageAdd = tl.image_resize("./img/add_user.png", 25, 25)

        addUserButton = Button(addUserFrame, image=self.imageAdd)
        addUserButton.pack()
