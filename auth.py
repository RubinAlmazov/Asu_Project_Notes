# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LogReg(object):
    def setupUi(self, LogReg):
        if not LogReg.objectName():
            LogReg.setObjectName(u"LogReg")
        LogReg.resize(449, 194)
        LogReg.setStyleSheet(u"background-color: rgb(101, 67, 33);")
        LogReg.setStyleSheet("""
                    QWidget {
                        background: QLinearGradient(x1: 0, y1: 0,
                                                    x2: 0, y2: 1,
                                                    stop: 0   rgba(69, 43, 26, 255), /* более темный коричневый */
                                                    stop: 0.5 rgba(102, 68, 34, 255), /* средний коричневый */
                                                    stop: 1   rgba(122, 101, 82, 255)); /* светлый коричневый */
                    }
                """)
        self.verticalLayout_2 = QVBoxLayout(LogReg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LogLine = QLineEdit(LogReg)
        self.LogLine.setObjectName(u"LogLine")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(15)
        self.LogLine.setFont(font)
        self.LogLine.setStyleSheet(u";background-color: rgb(255, 239, 205)")

        self.verticalLayout.addWidget(self.LogLine)

        self.RegLine = QLineEdit(LogReg)
        self.RegLine.setObjectName(u"RegLine")
        self.RegLine.setFont(font)
        self.RegLine.setStyleSheet(u";background-color: rgb(255, 239, 205)")

        self.verticalLayout.addWidget(self.RegLine)

        self.LoginButt = QPushButton(LogReg)
        self.LoginButt.setObjectName(u"LoginButt")
        self.LoginButt.setFont(font)
        self.LoginButt.setStyleSheet(u";background-color: rgb(255, 239, 205)")

        self.verticalLayout.addWidget(self.LoginButt)

        self.RegButt = QPushButton(LogReg)
        self.RegButt.setObjectName(u"RegButt")
        self.RegButt.setFont(font)
        self.RegButt.setStyleSheet(u";background-color: rgb(255, 239, 205)")

        self.verticalLayout.addWidget(self.RegButt)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(LogReg)

        QMetaObject.connectSlotsByName(LogReg)
    # setupUi

    def retranslateUi(self, LogReg):
        LogReg.setWindowTitle(QCoreApplication.translate("LogReg", u"Form", None))
        self.LogLine.setPlaceholderText(QCoreApplication.translate("LogReg", u"\u041b\u043e\u0433\u0438\u043d..", None))
        self.RegLine.setPlaceholderText(QCoreApplication.translate("LogReg", u"\u041f\u0430\u0440\u043e\u043b\u044c..", None))
        self.LoginButt.setText(QCoreApplication.translate("LogReg", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.RegButt.setText(QCoreApplication.translate("LogReg", u"\u0417\u0430\u0440\u0435\u0433\u0435\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
    # retranslateUi

