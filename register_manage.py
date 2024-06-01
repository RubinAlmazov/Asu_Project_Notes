#TODO: CHANGE THE STYLE AND ANIMATION OF THE BUTTONS / ADD THE TEXT IF AUTH IS SUCCSESSFUL "WELCOME {user_name}" /
# PROBABLY CHANGE THE BD AND ADD THE COLUMN WITH THE TEXT OF NOTE

import sqlite3
from PySide6 import QtWidgets, QtCore

from auth_window2 import Auth_Window2

db = sqlite3.connect('database_notes2')
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (ID INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, password TEXT)')
db.commit()


class AuthWindow(QtWidgets.QMainWindow, Auth_Window2):
    # Создание пользовательского сигнала
    authenticated = QtCore.Signal()

    def __init__(self):
        super(AuthWindow, self).__init__()
        self.setupUi(self)
        self.LoginButt.pressed.connect(self.login)
        self.RegButt.pressed.connect(self.register)

    def register(self):
        user_login = self.LogLine.text()
        user_password = self.RegLine.text()

        if len(user_login) == 0 or len(user_password) == 0:
            self.label.setText('Логин и пароль не могут быть пустыми!')
            self.label.show()
            return

        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO users (login, password) VALUES ("{user_login}", "{user_password}")')
            self.label.setText(f'Аккаунт {user_login} успешно зарегистрирован')
            self.label.show()
            self.authenticated.emit()
            self.close()
            db.commit()
        else:
            self.label.setText('Такая запись уже имеется')
            self.label.show()

    def login(self):
        user_login = self.LogLine.text()
        user_password = self.RegLine.text()

        if len(user_login) == 0 or len(user_password) == 0:
            self.label.setText('Логин и пароль не могут быть пустыми!')
            self.label.show()
            return

        cursor.execute(f'SELECT password FROM users WHERE login="{user_login}"')
        check_pass = cursor.fetchall()

        cursor.execute(f'SELECT login FROM users WHERE login="{user_login}"')
        check_login = cursor.fetchall()

        if check_pass and check_pass[0][0] == user_password and check_login and check_login[0][0] == user_login:
            self.label.setText('Успешная авторизация')
            self.label.show()
            self.authenticated.emit()
            self.close()
        else:
            self.label.setText('Ошибка авторизации')
            self.label.show()
