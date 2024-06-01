# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'archive_window.ui'
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

class Ui_ArchiveWindow(object):
    def setupUi(self, ArchiveWindow):
        if not ArchiveWindow.objectName():
            ArchiveWindow.setObjectName(u"ArchiveWindow")
        ArchiveWindow.resize(1111, 884)
        ArchiveWindow.setStyleSheet(u"background-color: rgb(101, 67, 33);")
        self.centralwidget = QWidget(ArchiveWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 196, 281))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainWindowButtAW = QPushButton(self.layoutWidget)
        self.MainWindowButtAW.setObjectName(u"MainWindowButtAW")
        self.MainWindowButtAW.setMouseTracking(False)
        self.MainWindowButtAW.setAcceptDrops(True)
        self.MainWindowButtAW.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MainWindowButtAW.setStyleSheet(
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
        self.MainWindowButtAW.setIcon(icon)
        self.MainWindowButtAW.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.MainWindowButtAW)

        self.ArchiveButtAW = QPushButton(self.layoutWidget)
        self.ArchiveButtAW.setObjectName(u"ArchiveButtAW")
        self.ArchiveButtAW.setStyleSheet(
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
        self.ArchiveButtAW.setIcon(icon1)
        self.ArchiveButtAW.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.ArchiveButtAW)

        self.RemindButtAW = QPushButton(self.layoutWidget)
        self.RemindButtAW.setObjectName(u"RemindButtAW")
        self.RemindButtAW.setStyleSheet(
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
        self.RemindButtAW.setIcon(icon2)
        self.RemindButtAW.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.RemindButtAW)

        self.TrashButtAW = QPushButton(self.layoutWidget)
        self.TrashButtAW.setObjectName(u"TrashButtAW")
        self.TrashButtAW.setStyleSheet(
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
        self.TrashButtAW.setIcon(icon3)
        self.TrashButtAW.setIconSize(QSize(24, 24))
        self.TrashButtAW.setAutoRepeat(False)

        self.verticalLayout.addWidget(self.TrashButtAW)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(360, 20, 581, 41))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border-radius: 7px;\n"
"font: 20pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        ArchiveWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ArchiveWindow)

        QMetaObject.connectSlotsByName(ArchiveWindow)
    # setupUi

    def retranslateUi(self, ArchiveWindow):
        ArchiveWindow.setWindowTitle(QCoreApplication.translate("ArchiveWindow", u"MainWindow", None))
        self.MainWindowButtAW.setText(QCoreApplication.translate("ArchiveWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.ArchiveButtAW.setText(QCoreApplication.translate("ArchiveWindow", u"\u0410\u0440\u0445\u0438\u0432", None))
        self.RemindButtAW.setText(QCoreApplication.translate("ArchiveWindow", u"\u041d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u044f", None))
        self.TrashButtAW.setText(QCoreApplication.translate("ArchiveWindow", u"\u041a\u043e\u0440\u0437\u0438\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("ArchiveWindow", u"\u0412\u0430\u0448\u0438 \u0410\u0440\u0445\u0438\u0432\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
    # retranslateUi

