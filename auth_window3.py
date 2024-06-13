from PySide6.QtCore import (QCoreApplication,
                            QMetaObject, QRect, Qt, QSize)
from PySide6.QtGui import QFont,QIcon
from PySide6.QtWidgets import (QLabel, QLineEdit,
                               QPushButton, QWidget)


class Auth_Window2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        window_icon = QIcon(u"icons/spec.svg")
        MainWindow.setWindowIcon(window_icon)
        MainWindow.setFixedSize(1095, 863)
        MainWindow.setStyleSheet(u"background-color: rgb(101, 67, 33);")
        MainWindow.setStyleSheet("""
                                    QWidget {
                                        background: QLinearGradient(x1: 0, y1: 0,
                                                                    x2: 0, y2: 1,
                                                                    stop: 0   rgba(69, 43, 26, 255), /* более темный коричневый */
                                                                    stop: 0.5 rgba(102, 68, 34, 255), /* средний коричневый */
                                                                    stop: 1   rgba(122, 101, 82, 255)); /* светлый коричневый */
                                    }
                                """)
        button_style = """
                               QPushButton {
                                   background-color: qlineargradient(x1: 0, y1: 0, 
                                                                     x2: 0, y2: 1, 
                                                                     stop: 0 rgba(255, 248, 220, 204),  /* светло-бежевый */
                                                                     stop: 1 rgba(245, 222, 179, 204)); /* более тёмный бежевый */
                                   border: 1px solid rgb(200, 200, 200);
                                   border-radius: 7px;
                                   font: 15pt "Arial";
                                   height: 50px;
                               }
                               QPushButton:hover {
                                   background-color: qlineargradient(x1: 0, y1: 0, 
                                                                     x2: 0, y2: 1, 
                                                                     stop: 0 rgba(255, 240, 210, 204),  /* светло-бежевый */
                                                                     stop: 1 rgba(235, 215, 165, 204)); /* более тёмный бежевый */
                                   border: 1px solid rgb(170, 170, 170);
                               }
                               QPushButton:pressed {
                                   background-color: qlineargradient(x1: 0, y1: 0, 
                                                                     x2: 0, y2: 1, 
                                                                     stop: 0 rgba(240, 230, 200, 204),  /* светло-бежевый */
                                                                     stop: 1 rgba(220, 200, 150, 204)); /* более тёмный бежевый */
                                   border: 1px solid rgb(140, 140, 140);
                               }
                               """
        line_edit_style = """
                                  QLineEdit {
                                      background-color: qlineargradient(x1: 0, y1: 0, 
                                                                        x2: 0, y2: 1, 
                                                                        stop: 0 rgba(255, 248, 220, 204),  /* светло-бежевый */
                                                                        stop: 1 rgba(245, 222, 179, 204)); /* более тёмный бежевый */
                                      font: 20pt "Times New Roman";
                                      border: 1px solid rgb(200, 200, 200);
                                      border-radius: 7px;
                                  }
                                  QLineEdit:hover {
                                      background-color: qlineargradient(x1: 0, y1: 0, 
                                                                        x2: 0, y2: 1, 
                                                                        stop: 0 rgba(255, 240, 210, 204),  /* светло-бежевый */
                                                                        stop: 1 rgba(235, 215, 165, 204)); /* более тёмный бежевый */
                                      border: 1px solid rgb(170, 170, 170);
                                  }
                                  QLineEdit:focus {
                                      background-color: qlineargradient(x1: 0, y1: 0, 
                                                                        x2: 0, y2: 1, 
                                                                        stop: 0 rgba(240, 230, 200, 204),  /* светло-бежевый */
                                                                        stop: 1 rgba(220, 200, 150, 204)); /* более тёмный бежевый */
                                      border: 1px solid rgb(140, 140, 140);
                                  }
                                  """
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.LogLine = QLineEdit(self.centralwidget)
        self.LogLine.setObjectName(u"LogLine")
        self.LogLine.setGeometry(QRect(299, 285, 491, 51))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(15)
        self.LogLine.setFont(font)
        self.LogLine.setStyleSheet(line_edit_style)
        self.LoginButt = QPushButton(self.centralwidget)
        self.LoginButt.setObjectName(u"LoginButt")
        self.LoginButt.setGeometry(QRect(299, 415, 241, 51))
        self.LoginButt.setFont(font)
        self.LoginButt.setStyleSheet(button_style)
        self.RegLine = QLineEdit(self.centralwidget)
        self.RegLine.setObjectName(u"RegLine")
        self.RegLine.setGeometry(QRect(300, 350, 491, 51))
        self.RegLine.setFont(font)
        self.RegLine.setStyleSheet(line_edit_style)
        self.RegButt = QPushButton(self.centralwidget)
        self.RegButt.setObjectName(u"RegButt")
        self.RegButt.setGeometry(QRect(550, 415, 241, 51))
        self.RegButt.setFont(font)
        self.RegButt.setStyleSheet(button_style)
        icon1 = QIcon()
        icon1.addFile(u"icons/how_to_reg_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RegButt.setIcon(icon1)
        self.RegButt.setIconSize(QSize(24, 24))
        icon = QIcon()
        icon.addFile(u"icons/login_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.LoginButt.setIcon(icon)
        self.LoginButt.setIconSize(QSize(24, 24))

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 490, 311, 20))
        self.label.setStyleSheet(u"border-radius: 7px;\n"
                                      "font: 10pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.hide()
        self.TextLabel1 = QLabel(self.centralwidget)
        self.TextLabel1.setObjectName(u"TextLabel1")
        self.TextLabel1.setGeometry(QRect(281, 31, 536, 53))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        self.TextLabel1.setFont(font1)
        self.TextLabel1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.TextLabel1.setAutoFillBackground(False)
        self.TextLabel1.setStyleSheet(u"border-radius: 7px;\n"
                                      "font: 20pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.TextLabel1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TextLabel2 = QLabel(self.centralwidget)
        self.TextLabel2.setObjectName(u"TextLabel2")
        self.TextLabel2.setGeometry(QRect(281, 104, 536, 53))
        self.TextLabel2.setFont(font1)
        self.TextLabel2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.TextLabel2.setAutoFillBackground(False)
        self.TextLabel2.setStyleSheet(u"border-radius: 7px;\n"
                                      "font: 20pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.TextLabel2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TextLabel3 = QLabel(self.centralwidget)
        self.TextLabel3.setObjectName(u"TextLabel3")
        self.TextLabel3.setGeometry(QRect(281, 177, 536, 53))
        self.TextLabel3.setFont(font1)
        self.TextLabel3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.TextLabel3.setAutoFillBackground(False)
        self.TextLabel3.setStyleSheet(u"border-radius: 7px;\n"
                                      "font: 20pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.TextLabel3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Добро Пожаловать", None))
        self.LogLine.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d..", None))
        self.LoginButt.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.RegLine.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c..", None))
        self.RegButt.setText(QCoreApplication.translate("MainWindow",
                                                        "Зарегистрироваться",
                                                        None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.TextLabel1.setText(QCoreApplication.translate("MainWindow",
                                                           u"\u0414\u043e\u0431\u0440\u043e \u041f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 \u0417\u0430\u043c\u0435\u0442\u043a\u0438",
                                                           None))
        self.TextLabel2.setText(QCoreApplication.translate("MainWindow", "Войдите Или Зарегистрируйтесь",
                                                           None))
        self.TextLabel3.setText(QCoreApplication.translate("MainWindow",
                                                           u"\u0427\u0442\u043e\u0431\u044b \u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c \u0420\u0430\u0431\u043e\u0442\u0443 \u041d\u0430\u0434 \u0417\u0430\u043c\u0435\u0442\u043a\u0430\u043c\u0438",
                                                           None))
    # retranslateUi
