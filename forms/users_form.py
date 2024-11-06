from ttkbootstrap import Toplevel


class MyUsers(Toplevel):
    def __init__(self, parent):
        super().__init__(title="Users Information", resizable=(False, False))

        self.transient(parent)
        self.grab_set()
        self.focus()
