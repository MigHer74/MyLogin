from ttkbootstrap import Toplevel, Frame, Label, Button


class MyAbout(Toplevel):
    def __init__(self, parent):
        super().__init__(title="About", resizable=(False, False))
        self.place_window_center()
        self.transient(parent)
        self.grab_set()
        self.focus()
