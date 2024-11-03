from src import tools as tl
from forms import login_form as lf


if __name__ == "__main__":
    tl.verify_storage()

    app = lf.MyLogin()
    app.mainloop()
