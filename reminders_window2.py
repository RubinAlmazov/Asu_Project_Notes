# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reminders_window.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import res_rc

class RemindWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1114, 883)
        MainWindow.setStyleSheet(u"background-color: rgb(101, 67, 33);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 196, 281))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Main_Page_butt = QPushButton(self.layoutWidget)
        self.Main_Page_butt.setObjectName(u"Main_Page_butt")
        self.Main_Page_butt.setMouseTracking(False)
        self.Main_Page_butt.setAcceptDrops(True)
        self.Main_Page_butt.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Main_Page_butt.setStyleSheet(
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
        icon = QIcon()
        icon.addFile(u"../../Downloads/notes_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Main_Page_butt.setIcon(icon)
        self.Main_Page_butt.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.Main_Page_butt)

        self.Archive_butt = QPushButton(self.layoutWidget)
        self.Archive_butt.setObjectName(u"Archive_butt")
        self.Archive_butt.setStyleSheet(
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
        icon1 = QIcon()
        icon1.addFile(u"icons/archive_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Archive_butt.setIcon(icon1)
        self.Archive_butt.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.Archive_butt)

        self.Remind_butt = QPushButton(self.layoutWidget)
        self.Remind_butt.setObjectName(u"Remind_butt")
        self.Remind_butt.setStyleSheet(
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
        icon2 = QIcon()
        icon2.addFile(u"icons/notifications_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Remind_butt.setIcon(icon2)
        self.Remind_butt.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.Remind_butt)

        self.Trash_butt = QPushButton(self.layoutWidget)
        self.Trash_butt.setObjectName(u"Trash_butt")
        self.Trash_butt.setStyleSheet(
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
        icon3 = QIcon()
        icon3.addFile(u"icons/delete_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Trash_butt.setIcon(icon3)
        self.Trash_butt.setIconSize(QSize(24, 24))
        self.Trash_butt.setAutoRepeat(False)

        self.verticalLayout.addWidget(self.Trash_butt)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(360, 20, 591, 41))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_text_ur_rems = QLabel(self.verticalLayoutWidget)
        self.label_text_ur_rems.setObjectName(u"label_text_ur_rems")
        self.label_text_ur_rems.setStyleSheet(u"border-radius: 7px;\n"
"font: 20pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.label_text_ur_rems.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_text_ur_rems)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Напоминания", None))
        self.Main_Page_butt.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.Archive_butt.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0445\u0438\u0432", None))
        self.Remind_butt.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u044f", None))
        self.Trash_butt.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0437\u0438\u043d\u0430", None))
        self.label_text_ur_rems.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448\u0438 \u041d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u044f", None))
    # retranslateUi

