from ttkbootstrap import Window, Frame, Label, Entry, Button, Combobox
from ttkbootstrap.dialogs.dialogs import Messagebox
from src import tools as tl
from src import dba as db
from forms import users_form as uf


class MyLogin(Window):
    def __init__(self):
        super().__init__(title="MyLogin", resizable=(False, False),
                         themename="superhero")
        self.load_login()
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

        self.nameCombo = Combobox(entriesFrame, width=23,
                                  values=self.dataUsers, state="readonly")
        self.nameCombo.grid(row=1, column=0, padx=(15, 15), pady=(5, 15))

        passwordLabel = Label(entriesFrame, text="Password")
        passwordLabel.grid(row=2, column=0, padx=(15, 15), pady=(15, 0))

        self.passwordEntry = Entry(entriesFrame, width=25, show="*")
        self.passwordEntry.grid(row=3, column=0, padx=(15, 15), pady=(5, 20))

        # Buttons Frame
        buttonsFrame = Frame(self)
        buttonsFrame.grid(row=2, column=1, padx=(40, 20), pady=(20, 0))

        buttonAccess = Button(buttonsFrame, width=15, text="Access",
                              command=self.allow_login, bootstyle="success")
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

    def load_login(self):
        self.dataUsers = []
        loadUsers = db.retrieve_info()

        for user in loadUsers:
            self.dataUsers.append(user[1])

    def allow_login(self):
        getPassword = db.seek_password(self.nameCombo.get())
        allowAccess = tl.hashing_compare(getPassword, self.passwordEntry.get())

        if allowAccess:
            Messagebox.ok(title="Access Granted", message="ACCESS GRANTED!!!",
                          parent=self)
        else:
            Messagebox.show_error(title="Access Denied",
                                  message="ACCESS DENIED!!!",
                                  parent=self)
