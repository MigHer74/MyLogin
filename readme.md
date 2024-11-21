# Project "My Login"

## Description
"My Login" is a project that I wanted to use for hashing password using python bcrypt library, in order to do that I created a graphical user interface using ttkbootstrap library.

The project is form by a main window contains the classical entry fields for user name and password (the user names is a combobox), a button to verify the password and a button to close the window plus there is a button that opens a secondary window where stores the user data such as id, name and password.

The app verify that exists the folder and file for the database, in case there are not the both elements the app create them before shows the main window.

On the secondary window can manage the users and here is where the app uses bcrypt to encrypt the password.

Finally, if the user name and password are correct the app shows a succesful access message if not, it shows an error message.

The users data stores in a sqlite3 database file.

This little project is going to be a part for a larger project.
<br>

## Project Files
| Files            | Description                                                      |
| ---------------- | ---------------------------------------------------------------- |
| main.py          | Script that starts the app.                                      |
| dba.py           | Functions for manage the database.                               |
| tools.py         | Contains functions for the app.                                  |
| login_form.py    | The file contains the code of the main window.                   |
| users_form.py    | The file contains the code of managing users info.               |
| about_form.py    | The file contains the code of "About" window.                    |
| requirements.txt | File containing the names of the project's additional libraries. |
| readme.md        | Description and information of the project.                      |
| .gitignore       | Includes non-important files of the project.                     |
<br>

## Project Foldes
| Folder | Description                                       |
| ------ | ------------------------------------------------- |
| db     | The directory where the database is located.      |
| forms  | The directory includes the scripts of every form. |
| src    | The directory contains the general scripts.       |
<br>

> ### ***If you think education is expensive, try ignorance. - Derek Bok***
