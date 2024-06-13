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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
import res_rc

class RemindWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1114, 883)
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.TrashButtMW = QPushButton(self.centralwidget)
        self.TrashButtMW.setObjectName(u"TrashButtMW")
        self.TrashButtMW.setGeometry(QRect(0, 190, 194, 52))
        self.TrashButtMW.setStyleSheet(button_style)
        icon = QIcon()
        icon.addFile(u"icons/delete_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.TrashButtMW.setIcon(icon)
        self.TrashButtMW.setIconSize(QSize(24, 24))
        self.TrashButtMW.setAutoRepeat(False)
        self.RemindButtMW_2 = QPushButton(self.centralwidget)
        self.RemindButtMW_2.setObjectName(u"RemindButtMW_2")
        self.RemindButtMW_2.setGeometry(QRect(0, 130, 194, 52))
        self.RemindButtMW_2.setStyleSheet(button_style)
        icon1 = QIcon()
        icon1.addFile(u"icons/notifications_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.RemindButtMW_2.setIcon(icon1)
        self.RemindButtMW_2.setIconSize(QSize(24, 24))
        self.MainWindowButtMW = QPushButton(self.centralwidget)
        self.MainWindowButtMW.setObjectName(u"MainWindowButtMW")
        self.MainWindowButtMW.setGeometry(QRect(0, 10, 194, 52))
        self.MainWindowButtMW.setMouseTracking(False)
        self.MainWindowButtMW.setAcceptDrops(True)
        self.MainWindowButtMW.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.MainWindowButtMW.setStyleSheet(button_style)
        icon2 = QIcon()
        icon2.addFile(u"../../Downloads/notes_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.MainWindowButtMW.setIcon(icon2)
        self.MainWindowButtMW.setIconSize(QSize(24, 24))
        self.ArchiveButtMW_2 = QPushButton(self.centralwidget)
        self.ArchiveButtMW_2.setObjectName(u"ArchiveButtMW_2")
        self.ArchiveButtMW_2.setGeometry(QRect(0, 70, 194, 52))
        self.ArchiveButtMW_2.setStyleSheet(button_style)
        icon3 = QIcon()
        icon3.addFile(u"icons/archive_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ArchiveButtMW_2.setIcon(icon3)
        self.ArchiveButtMW_2.setIconSize(QSize(24, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Напоминания", None))
        self.TrashButtMW.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0437\u0438\u043d\u0430", None))
        self.RemindButtMW_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u044f", None))
        self.MainWindowButtMW.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.ArchiveButtMW_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0445\u0438\u0432", None))

