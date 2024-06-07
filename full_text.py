
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QScrollArea, QVBoxLayout, QWidget)

class Text4Note(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1000, 800)

        # Создаем QScrollArea и устанавливаем его как центральный виджет
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setGeometry(QRect(0, 0, 431, 329))
        self.scrollArea.setWidgetResizable(True)

        # Создаем виджет-контейнер для QLabel
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 429, 327))

        # Создаем вертикальный макет для контейнера
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)

        # Создаем QLabel и добавляем его в макет
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1181, 731))
        self.label.setStyleSheet(u"background-color: rgb(101, 67, 33);")
        self.label.setWordWrap(True)
        self.verticalLayout.addWidget(self.label)

        # Устанавливаем контейнер как виджет для прокрутки
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

