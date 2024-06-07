# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1095, 863)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet(u"background-color: rgb(101, 67, 33);\n"
"")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 196, 281))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainWindowButtMW = QPushButton(self.layoutWidget)
        self.MainWindowButtMW.setObjectName(u"MainWindowButtMW")
        self.MainWindowButtMW.setMouseTracking(False)
        self.MainWindowButtMW.setAcceptDrops(True)
        self.MainWindowButtMW.setLayoutDirection(Qt.LeftToRight)
        self.MainWindowButtMW.setStyleSheet(
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
        self.MainWindowButtMW.setIcon(icon)
        self.MainWindowButtMW.setIconSize(QSize(24, 24))
        self.MainWindowButtMW.setText('Заметки')

        self.verticalLayout.addWidget(self.MainWindowButtMW)

        self.ArchiveButtMW_2 = QPushButton(self.layoutWidget)
        self.ArchiveButtMW_2.setObjectName(u"ArchiveButtMW_2")
        self.ArchiveButtMW_2.setStyleSheet(
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
        self.ArchiveButtMW_2.setIcon(icon1)
        self.ArchiveButtMW_2.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.ArchiveButtMW_2)

        self.RemindButtMW_2 = QPushButton(self.layoutWidget)
        self.RemindButtMW_2.setObjectName(u"RemindButtMW_2")
        self.RemindButtMW_2.setStyleSheet(
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
        self.RemindButtMW_2.setIcon(icon2)
        self.RemindButtMW_2.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.RemindButtMW_2)

        self.TrashButtMW = QPushButton(self.layoutWidget)
        self.TrashButtMW.setObjectName(u"TrashButtMW")
        self.TrashButtMW.setStyleSheet(
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
        self.TrashButtMW.setIcon(icon3)
        self.TrashButtMW.setIconSize(QSize(24, 24))
        self.TrashButtMW.setAutoRepeat(False)

        self.verticalLayout.addWidget(self.TrashButtMW)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(340, 20, 581, 91))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.NotesLineMW = QLineEdit(self.verticalLayoutWidget)
        self.NotesLineMW.setObjectName(u"NotesLineMW")
        self.NotesLineMW.setCursor(QCursor(Qt.IBeamCursor))
        self.NotesLineMW.setStyleSheet(u"background-color: rgb(255, 239, 205);\n"
"font: 20pt \"Times New Roman\";border-radius: 7px")

        self.verticalLayout_2.addWidget(self.NotesLineMW)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u044f", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0437\u0438\u043d\u0430", None))

        self.ArchiveButtMW_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0445\u0438\u0432", None))
        self.RemindButtMW_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u044f", None))
        self.TrashButtMW.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0437\u0438\u043d\u0430", None))
        self.NotesLineMW.setText("")
        self.NotesLineMW.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u043c\u0435\u0442\u043a\u0443...", None))
    # retranslateUi

