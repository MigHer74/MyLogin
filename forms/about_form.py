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

        # Title Frame
        self.lblFrame = Frame(self)
        self.lblFrame.pack()

        self.lblTitle = Label(self.lblFrame, text="MyLogin",
                              font=("Arial", 20, "bold"))
        self.lblTitle.pack()
