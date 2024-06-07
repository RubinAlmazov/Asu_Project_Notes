
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

class Ui_TrashWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1115, 891)
        MainWindow.setStyleSheet(u"background-color: rgb(101, 67, 33);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 196, 281))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Main_page_butt_TW = QPushButton(self.layoutWidget)
        self.Main_page_butt_TW.setObjectName(u"Main_page_butt_TW")
        self.Main_page_butt_TW.setMouseTracking(False)
        self.Main_page_butt_TW.setAcceptDrops(True)
        self.Main_page_butt_TW.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Main_page_butt_TW.setStyleSheet(
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
        self.Main_page_butt_TW.setIcon(icon)
        self.Main_page_butt_TW.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.Main_page_butt_TW)

        self.Archive_butt_TW = QPushButton(self.layoutWidget)
        self.Archive_butt_TW.setObjectName(u"Archive_butt_TW")
        self.Archive_butt_TW.setStyleSheet(
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
        self.Archive_butt_TW.setIcon(icon1)
        self.Archive_butt_TW.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.Archive_butt_TW)

        self.Remindes_butt_TW = QPushButton(self.layoutWidget)
        self.Remindes_butt_TW.setObjectName(u"Remindes_butt_TW")
        self.Remindes_butt_TW.setStyleSheet(
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
        self.Remindes_butt_TW.setIcon(icon2)
        self.Remindes_butt_TW.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.Remindes_butt_TW)

        self.Trash_butt_TW = QPushButton(self.layoutWidget)
        self.Trash_butt_TW.setObjectName(u"Trash_butt_TW")
        self.Trash_butt_TW.setStyleSheet(
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
        self.Trash_butt_TW.setIcon(icon3)
        self.Trash_butt_TW.setIconSize(QSize(24, 24))
        self.Trash_butt_TW.setAutoRepeat(False)

        self.verticalLayout_3.addWidget(self.Trash_butt_TW)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(360, 20, 581, 41))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_ur_trash = QLabel(self.verticalLayoutWidget)
        self.label_ur_trash.setObjectName(u"label_ur_trash")
        self.label_ur_trash.setStyleSheet(u"border-radius: 7px;\n"
"font: 20pt \"Arial\"; justify: left; color: rgb(237,145,33)")
        self.label_ur_trash.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_ur_trash)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Корзина", None))
        self.Main_page_butt_TW.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.Archive_butt_TW.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0445\u0438\u0432", None))
        self.Remindes_butt_TW.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u044f", None))
        self.Trash_butt_TW.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u0437\u0438\u043d\u0430", None))
        self.label_ur_trash.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448\u0430 \u041a\u043e\u0440\u0437\u0438\u043d\u0430", None))
    # retranslateUi

