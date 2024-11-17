from ttkbootstrap import Window, Frame, Label, Entry, Button, Combobox
from src import tools as tl
from forms import users_form as uf


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
        imageFrame.grid(row=1, rowspan=2, column=0, padx=(20, 0), pady=(20, 0))

        self.imageLogin = tl.image_resize("./img/monitor.png", 250, 250)

        imageLabel = Label(imageFrame, image=self.imageLogin)
        imageLabel.pack()

        # Entries Frame
        entriesFrame = Frame(self, relief="raised")
        entriesFrame.grid(row=1, column=1, padx=(40, 20), pady=(20, 0))

        nameLabel = Label(entriesFrame, text="User Name")
        nameLabel.grid(row=0, column=0, padx=(15, 15), pady=(15, 0))

        # nameEntry = Entry(entriesFrame, width=25)
        # nameEntry.grid(row=1, column=0, padx=(15, 15), pady=(5, 15))

        nameCombo = Combobox(entriesFrame, width=23, state="readonly")
        nameCombo.grid(row=1, column=0, padx=(15, 15), pady=(5, 15))

        passwordLabel = Label(entriesFrame, text="Password")
        passwordLabel.grid(row=2, column=0, padx=(15, 15), pady=(15, 0))

        passwordEntry = Entry(entriesFrame, width=25)
        passwordEntry.grid(row=3, column=0, padx=(15, 15), pady=(5, 20))

        # Buttons Frame
        buttonsFrame = Frame(self)
        buttonsFrame.grid(row=2, column=1, padx=(40, 20), pady=(20, 0))

        buttonAccess = Button(buttonsFrame, width=15, text="Access",
                              bootstyle="success")
        buttonAccess.grid(row=0, column=0, padx=(0, 25))

        buttonCancel = Button(buttonsFrame, width=15, text="Cancel",
                              command=self.quit, bootstyle="outline-danger")
        buttonCancel.grid(row=0, column=1)

        # Add User Frame
        addUserFrame = Frame(self)
        addUserFrame.grid(row=3, column=1, padx=(40, 20), pady=(20, 15),
                          sticky="e")

        self.imageAdd = tl.image_resize("./img/add_user.png", 35, 35)

        addUserButton = Button(addUserFrame, image=self.imageAdd, padding=0,
                               command=lambda: uf.MyUsers(self),
                               bootstyle="success-link")
        addUserButton.pack()
