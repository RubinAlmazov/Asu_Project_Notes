import sqlite3
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QTimer
from auth_window3 import Auth_Window2

db = sqlite3.connect('database_notes2')
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (ID INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, password TEXT)')
db.commit()


class AuthWindow(QtWidgets.QMainWindow, Auth_Window2):
    authenticated = QtCore.Signal(str)  # Signal to emit user_login


    def __init__(self):
        super(AuthWindow, self).__init__()
        self.setupUi(self)
        self.LoginButt.pressed.connect(self.login)
        self.RegButt.pressed.connect(self.register)

    def login_user(self, user_login):
        self.authenticated.emit(user_login)

    def register(self):
        user_login = self.LogLine.text()
        user_password = self.RegLine.text()

        if len(user_login) == 0 or len(user_password) == 0:
            self.label.setText('Логин и пароль не могут быть пустыми!')
            self.label.show()
            return

        cursor.execute('SELECT login FROM users WHERE login = ?', (user_login,))
        if cursor.fetchone() is None:
            cursor.execute('INSERT INTO users (login, password) VALUES (?, ?)', (user_login, user_password))
            self.label.setText(f'Аккаунт {user_login} успешно зарегистрирован')
            self.label.show()
            QTimer.singleShot(500, self.emit_and_close)
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

        cursor.execute('SELECT password FROM users WHERE login = ?', (user_login,))
        check_pass = cursor.fetchone()

        if check_pass and check_pass[0] == user_password:
            self.label.setText('Успешная авторизация')
            self.label.show()
            QTimer.singleShot(500, self.emit_and_close)
        else:
            self.label.setText('Ошибка авторизации')
            self.label.show()

    def emit_and_close(self):
        user_login = self.LogLine.text()
        self.authenticated.emit(user_login)
        self.hide()
