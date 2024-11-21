from ttkbootstrap import Toplevel, Frame, Label, Button
from src import tools as tl


class MyAbout(Toplevel):
    def __init__(self, parent):
        super().__init__(title="About", resizable=(False, False))
        self.build_about()
        self.place_window_center()
        self.transient(parent)
        self.grab_set()
        self.focus()

    def build_about(self):
        self.image01 = tl.image_resize("./img/monitor.png", 50, 50)
        self.image02 = tl.image_resize("./img/add_user.png", 50, 50)
        self.image03 = tl.image_resize("./img/alert_icon.png", 50, 50)

        # Title Frame
        self.lblFrame = Frame(self)
        self.lblFrame.grid(row=0, column=0, padx=(20, 20), pady=(20, 0))

        self.lblTitle = Label(self.lblFrame, text="MyLogin",
                              font=("Arial", 30, "bold"),
                              bootstyle="danger")
        self.lblTitle.pack()

        # Frame "Developed By"
        self.devFrame = Frame(self)
        self.devFrame.grid(row=1, column=0, padx=(20, 20), pady=(40, 0),
                           sticky="ew")

        self.devLabel = Label(self.devFrame,
                              text="Developed by Miguel Hernandez",
                              font=("Arial", 16, "normal"),
                              bootstyle="success")
        self.devLabel.pack()

        # Frame "Images"
        self.imgFrame01 = Frame(self)
        self.imgFrame01.grid(row=2, column=0, padx=(20, 20), pady=(40, 0),
                             sticky="w")

        self.imgLabel01 = Label(self.imgFrame01, image=self.image01)
        self.imgLabel01.pack(side="left")

        self.rowLabel01 = Label(self.imgFrame01,
                                text="'Monitor' icon of LAFS in Freepik.",
                                font=("Arial", 14, "normal"),
                                bootstyle="warning")
        self.rowLabel01.pack(padx=(15, 0), expand="y")

        self.imgFrame02 = Frame(self)
        self.imgFrame02.grid(row=3, column=0, padx=(20, 20), pady=(20, 0),
                             sticky="w")

        self.imgLabel02 = Label(self.imgFrame02, image=self.image02)
        self.imgLabel02.pack(side="left")

        self.rowLabel02 = Label(self.imgFrame02,
                                text="""'Add User' icon of Md Tanvirul Haque
                                in Freepik.""",
                                font=("Arial", 14, "normal"),
                                bootstyle="warning")
        self.rowLabel02.pack(padx=(15, 0), expand="y")

        self.imgFrame03 = Frame(self)
        self.imgFrame03.grid(row=4, column=0, padx=(20, 20), pady=(20, 0),
                             sticky="w")

        self.imgLabel03 = Label(self.imgFrame03, image=self.image03)
        self.imgLabel03.pack(side="left")

        self.rowLabel03 = Label(self.imgFrame03,
                                text="'Alert Icon' of icon_small in Freepik.",
                                font=("Arial", 14, "normal"),
                                bootstyle="warning")
        self.rowLabel03.pack(padx=(15, 0), expand="y")

        # Button Frame
        self.btnFrame = Frame(self)
        self.btnFrame.grid(row=5, column=0, padx=(20, 20), pady=(30, 20),
                           sticky="e")

        self.btnClose = Button(self.btnFrame, width=15, text="Close",
                               command=self.destroy,
                               bootstyle="info")
        self.btnClose.pack()
