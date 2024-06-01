# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1119, 928)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"background-color: rgb(101, 67, 33);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(140, 210, 841, 421))
        self.gridLayout_5 = QGridLayout(self.layoutWidget)
        self.gridLayout_5.setSpacing(50)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(50)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(4)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(50)
        self.gridLayout.setVerticalSpacing(10)
        self.NewNoteButtSW = QPushButton(self.layoutWidget)
        self.NewNoteButtSW.setObjectName(u"NewNoteButtSW")
        self.NewNoteButtSW.setStyleSheet(
                "QPushButton {"
                "   border: 1px solid rgb(0,0,0);"
                "   background-color: rgb(255, 239, 205);"
                "   border-radius: 7px;"
                "   font: 15pt \"Arial\";"
                "   height: 200px;"
                "}"
                "QPushButton:hover {"
                "   background-color: rgb(237,145,33);"
                "}"
        )
        icon = QIcon()
        icon.addFile(u"icons/add_notes_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.NewNoteButtSW.setIcon(icon)
        self.NewNoteButtSW.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.NewNoteButtSW, 0, 0, 1, 1)

        self.OpenButtSW = QPushButton(self.layoutWidget)
        self.OpenButtSW.setObjectName(u"OpenButtSW")
        self.OpenButtSW.setStyleSheet(
                "QPushButton {"
                "   border: 1px solid rgb(0,0,0);"
                "   background-color: rgb(255, 239, 205);"
                "   border-radius: 7px;"
                "   font: 15pt \"Arial\";"
                "   height: 200px;"
                "}"
                "QPushButton:hover {"
                "   background-color: rgb(237,145,33);"
                "}"
        )
        icon1 = QIcon()
        icon1.addFile(u"icons/folder_open_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.OpenButtSW.setIcon(icon1)
        self.OpenButtSW.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.OpenButtSW, 0, 1, 1, 1)

        self.TrashButtSW = QPushButton(self.layoutWidget)
        self.TrashButtSW.setObjectName(u"TrashButtSW")
        self.TrashButtSW.setStyleSheet(
                "QPushButton {"
                "   border: 1px solid rgb(0,0,0);"
                "   background-color: rgb(255, 239, 205);"
                "   border-radius: 7px;"
                "   font: 15pt \"Arial\";"
                "   height: 200px;"
                "}"
                "QPushButton:hover {"
                "   background-color: rgb(237,145,33);"
                "}"
        )
        icon2 = QIcon()
        icon2.addFile(u"icons/delete_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TrashButtSW.setIcon(icon2)
        self.TrashButtSW.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.TrashButtSW, 0, 2, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(50)
        self.gridLayout_2.setVerticalSpacing(10)
        self.NewNoteLabelSW = QLabel(self.layoutWidget)
        self.NewNoteLabelSW.setObjectName(u"NewNoteLabelSW")
        self.NewNoteLabelSW.setStyleSheet(u"border-radius: 7px;\n"
"font: 20pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.NewNoteLabelSW.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.NewNoteLabelSW, 0, 0, 1, 1)

        self.OpenLabelSW = QLabel(self.layoutWidget)
        self.OpenLabelSW.setObjectName(u"OpenLabelSW")
        self.OpenLabelSW.setStyleSheet(u"border-radius: 7px;\n"
"font: 20pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.OpenLabelSW.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.OpenLabelSW, 0, 1, 1, 1)

        self.TrashLabelSW = QLabel(self.layoutWidget)
        self.TrashLabelSW.setObjectName(u"TrashLabelSW")
        self.TrashLabelSW.setStyleSheet(u"border-radius: 7px;\n"
"font: 20pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.TrashLabelSW.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.TrashLabelSW, 0, 2, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.CreateNoteLabelSW = QLabel(self.layoutWidget)
        self.CreateNoteLabelSW.setObjectName(u"CreateNoteLabelSW")
        self.CreateNoteLabelSW.setStyleSheet(u"border-radius: 7px;\n"
"font: 15pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.CreateNoteLabelSW.setFrameShadow(QFrame.Sunken)
        self.CreateNoteLabelSW.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.CreateNoteLabelSW, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.WelcomeLabelSW = QLabel(self.layoutWidget)
        self.WelcomeLabelSW.setObjectName(u"WelcomeLabelSW")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.WelcomeLabelSW.setFont(font)
        self.WelcomeLabelSW.setLayoutDirection(Qt.LeftToRight)
        self.WelcomeLabelSW.setAutoFillBackground(False)
        self.WelcomeLabelSW.setStyleSheet(u"border-radius: 7px;\n"
"font: 20pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.WelcomeLabelSW.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.WelcomeLabelSW, 0, 0, 1, 1)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(1000, 0, 121, 111))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.RegLogButtSW = QPushButton(self.layoutWidget1)
        self.RegLogButtSW.setObjectName(u"RegLogButtSW")
        font1 = QFont()
        font1.setPointSize(10)
        self.RegLogButtSW.setFont(font1)
        self.RegLogButtSW.setStyleSheet(u"border: 1px solid rgb(0,0,0);background-color: rgb(255, 239, 205);border-radius: 7px;height:200")
        icon3 = QIcon()
        icon3.addFile(u"icons/how_to_reg_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RegLogButtSW.setIcon(icon3)
        self.RegLogButtSW.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.RegLogButtSW)

        self.RegLogLabelSW = QLabel(self.layoutWidget1)
        self.RegLogLabelSW.setObjectName(u"RegLogLabelSW")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.RegLogLabelSW.setFont(font2)
        self.RegLogLabelSW.setStyleSheet(u"border-radius: 7px;\n"
"font: 10pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.RegLogLabelSW.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.RegLogLabelSW)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.NewNoteButtSW.setText("")
        self.OpenButtSW.setText("")
        self.TrashButtSW.setText("")
        self.NewNoteLabelSW.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f \u0417\u0430\u043c\u0435\u0442\u043a\u0430", None))
        self.OpenLabelSW.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.TrashLabelSW.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0437\u0438\u043d\u0430", None))
        self.CreateNoteLabelSW.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0439\u0442\u0435 \u0421\u0432\u043e\u044e \u041f\u0435\u0440\u0432\u0443\u044e \u0417\u0430\u043c\u0435\u0442\u043a\u0443 \u0418\u043b\u0438 \u041f\u0440\u043e\u0434\u043b\u043e\u0436\u0438\u0442\u0435 \u041d\u0430\u0447\u0430\u0442\u0443\u044e.", None))
        self.WelcomeLabelSW.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u041f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 \u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.RegLogButtSW.setText("")
        self.RegLogLabelSW.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433/\u0412\u0445\u043e\u0434", None))
    # retranslateUi

