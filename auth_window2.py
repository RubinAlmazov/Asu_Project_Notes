# ADD BUTTONS ANIMATION

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Auth_Window2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1095, 863)
        MainWindow.setStyleSheet(u"background-color: rgb(101, 67, 33);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.LogLine = QLineEdit(self.centralwidget)
        self.LogLine.setObjectName(u"LogLine")
        self.LogLine.setGeometry(QRect(299, 285, 491, 51))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(15)
        self.LogLine.setFont(font)
        self.LogLine.setStyleSheet(u";background-color: rgb(255, 239, 205)")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(280, 30, 538, 201))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TextLabel1 = QLabel(self.layoutWidget)
        self.TextLabel1.setObjectName(u"TextLabel1")
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

        self.verticalLayout.addWidget(self.TextLabel1)

        self.TextLabel2 = QLabel(self.layoutWidget)
        self.TextLabel2.setObjectName(u"TextLabel2")
        self.TextLabel2.setFont(font1)
        self.TextLabel2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.TextLabel2.setAutoFillBackground(False)
        self.TextLabel2.setStyleSheet(u"border-radius: 7px;\n"
"font: 20pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.TextLabel2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.TextLabel2)

        self.TextLabel3 = QLabel(self.layoutWidget)
        self.TextLabel3.setObjectName(u"TextLabel3")
        self.TextLabel3.setFont(font1)
        self.TextLabel3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.TextLabel3.setAutoFillBackground(False)
        self.TextLabel3.setStyleSheet(u"border-radius: 7px;\n"
"font: 20pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.TextLabel3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.TextLabel3)

        self.LoginButt = QPushButton(self.centralwidget)
        self.LoginButt.setObjectName(u"LoginButt")
        self.LoginButt.setGeometry(QRect(299, 415, 241, 51))
        self.LoginButt.setFont(font)
        self.LoginButt.setStyleSheet(u";background-color: rgb(255, 239, 205)")
        self.RegLine = QLineEdit(self.centralwidget)
        self.RegLine.setObjectName(u"RegLine")
        self.RegLine.setGeometry(QRect(300, 350, 491, 51))
        self.RegLine.setFont(font)
        self.RegLine.setStyleSheet(u";background-color: rgb(255, 239, 205)")
        self.RegButt = QPushButton(self.centralwidget)
        self.RegButt.setObjectName(u"RegButt")
        self.RegButt.setGeometry(QRect(550, 415, 241, 51))
        self.RegButt.setFont(font)
        self.RegButt.setStyleSheet(
            "QPushButton {"
            "   border: 1px solid rgb(0,0,0);"
            "   background-color: rgb(255, 239, 205);"
            "   border-radius: 7px;"
            "   font: 15pt \"Arial\";"
            "   height: 50px;"
            "}"
            "QPushButton:hover {"
            "   background-color: rgb(237,145,33);"
            "}"
        )
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 490, 311, 20))
        self.label.setStyleSheet(u";font: 12pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.hide()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LogLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d..", None))
        self.TextLabel1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u041f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 \u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.TextLabel2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0434\u0438\u0442\u0435 \u0418\u043b\u0438 \u0417\u0430\u0440\u0435\u0433\u0435\u0441\u0442\u0440\u0438\u0440\u0443\u0439\u0442\u0435\u0441\u044c", None))
        self.TextLabel3.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0442\u043e\u0431\u044b \u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c \u0420\u0430\u0431\u043e\u0442\u0443 \u041d\u0430\u0434 \u0417\u0430\u043c\u0435\u0442\u043a\u0430\u043c\u0438", None))
        self.LoginButt.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.RegLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c..", None))
        self.RegButt.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0435\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

