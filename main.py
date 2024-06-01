# TODO: DO A FUNCTION LIKE GOOGLEKEEPS: The appearance of buttons with functionality when hovering over a note / CHANGE THE LOGIC OF WRAPING TEXT
#TODO: CHANGE THE LOGIC OF THE BUTTONS / SET ICONS / ADD A FOURTH BUTTON / ADD SPACE FOR BUTTONS / SET THE SCREEN RESOLUTION / ADD A SCROLL WHEEL
import sys
from PySide6 import QtCore, QtWidgets
from main_window import Ui_MainWindow
from start_window import Ui_MainWindow2
from archive_window2 import Ui_ArchiveWindow
from reminders_window2 import RemindWindow
from trash_window2 import Ui_TrashWindow
from register_manage import AuthWindow
from full_text import Text4Note


class NotesTracker(QtWidgets.QMainWindow):
    def __init__(self):
        super(NotesTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.MainWindowButtMW.setCheckable(True)
        self.ui.MainWindowButtMW.clicked.connect(self.open_start_window)
        self.ui.ArchiveButtMW_2.clicked.connect(self.open_archive_window)
        self.ui.RemindButtMW_2.clicked.connect(self.open_remind_window)
        self.ui.TrashButtMW.clicked.connect(self.open_trash_window)

        self.current_x = 250
        self.current_y = 120
        self.available_positions = []
        self.ui.NotesLineMW.returnPressed.connect(self.add_note)

    def open_start_window(self):
        global window2
        window2 = QtWidgets.QMainWindow()
        ui2 = Ui_MainWindow2()
        ui2.setupUi(window2)
        self.close()
        window2.show()

        def return_to_main_window():
            window2.close()
            self.show()

        ui2.NewNoteButtSW.clicked.connect(return_to_main_window)
        ui2.OpenButtSW.clicked.connect(self.open_archive_window)
        if window3:
            window3.close()
        if window4:
            window4.close()
        if window5:
            window5.close()

    def open_archive_window(self):
        global window3
        window3 = QtWidgets.QMainWindow()
        ui3 = Ui_ArchiveWindow()
        ui3.setupUi(window3)
        self.close()
        window3.show()

        ui3.MainWindowButtAW.clicked.connect(self.return_to_main_window)
        ui3.RemindButtAW.clicked.connect(self.open_remind_window)
        ui3.TrashButtAW.clicked.connect(self.open_trash_window)
        if window2:
            window2.close()
        if window4:
            window4.close()
        if window5:
            window5.close()

    def return_to_main_window(self):
        window3.close()
        self.show()

    def open_remind_window(self):
        global window4
        window4 = QtWidgets.QMainWindow()
        ui4 = RemindWindow()
        ui4.setupUi(window4)
        self.close()
        window4.show()

        ui4.Main_Page_butt.clicked.connect(self.return_to_main_window2)
        ui4.Archive_butt.clicked.connect(self.open_archive_window)
        ui4.Trash_butt.clicked.connect(self.open_trash_window)
        if window2:
            window2.close()
        if window3:
            window3.close()
        if window5:
            window5.close()

    def return_to_main_window2(self):
        window4.close()
        self.show()

    def open_trash_window(self):
        global window5
        window5 = QtWidgets.QMainWindow()
        ui5 = Ui_TrashWindow()
        ui5.setupUi(window5)
        self.close()
        window5.show()

        ui5.Main_page_butt_TW.clicked.connect(self.return_to_main_window3)
        ui5.Archive_butt_TW.clicked.connect(self.open_archive_window)
        ui5.Remindes_butt_TW.clicked.connect(self.open_remind_window)
        if window2:
            window2.close()
        if window3:
            window3.close()
        if window4:
            window4.close()

    def return_to_main_window3(self):
        window5.close()
        self.show()

    # For creating Notes / NOTES LOGIC
    def add_note(self):
        note_text = self.ui.NotesLineMW.text()
        if not note_text.strip():
            return

        x, y = self.current_x, self.current_y
        max_length = 315
        if len(note_text) > max_length:
            note_text = note_text[:max_length - 1] + '...'  # TODO: SET A LIMIT AND AFTER SHOW A MESSANGEBOX ERROR /
                                                                    # AFTER CLICKING ON THE NOTE SHOW THE ENTIRE TEXT

        note = QtWidgets.QFrame(self)
        note.setStyleSheet(
            "border: 1px solid rgb(0,0,0);"
            "background-color: rgb(255, 239, 205);"
        )
        note.setGeometry(x, y, 250, 170)

        # TO MOVE NOTES
        note.move(x, y)
        note.show()

        label = QtWidgets.QLabel(note)
        label.setText(note_text)
        #label.setStyleSheet(
            #"QFrame:hover {"
            #"   background-color: rgb(237,145,33);"
            #"}"
        #)
        label.show()


        # THE LOGIC OF THE WRAPING TEXT
        label.setWordWrap(True)
        label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        label.setGeometry(0,0, 250, 170) #TODO: A TEST IS NEEDED PERHAPS TEXT MAY BE OUT OF RANGE SET(5,5,240,140)

        # Creating buttons
        delete_button = QtWidgets.QPushButton("Удалить", note)
        archive_button = QtWidgets.QPushButton("Архивировать", note)
        remind_button = QtWidgets.QPushButton("Напомнить", note)
        show_text_button = QtWidgets.QPushButton("...", note)



        # Styling and positioning buttons
        button_style = """
               QPushButton {
                   background-color: rgba(255, 255, 255, 0.8);
                   border: 1px solid rgb(150, 150, 150);
                   border-radius: 5px;
               }
               """
        delete_button.setStyleSheet(button_style)
        archive_button.setStyleSheet(button_style)
        remind_button.setStyleSheet(button_style)
        show_text_button.setStyleSheet(button_style)

        delete_button.setGeometry(7, 135, 55, 30)
        archive_button.setGeometry(67, 135, 55, 30)
        remind_button.setGeometry(127, 135, 55, 30)
        show_text_button.setGeometry(187, 135, 55, 30)

        # Initially hide buttons
        delete_button.hide()
        archive_button.hide()
        remind_button.hide()
        show_text_button.hide()

        # Connect hover events using methods
        note.enterEvent = self.create_enter_event_handler(delete_button, archive_button, remind_button,show_text_button)
        note.leaveEvent = self.create_leave_event_handler(delete_button, archive_button, remind_button,show_text_button)

        # Connect delete button to the delete_note method
        delete_button.clicked.connect(self.create_delete_event_handler(note,x,y))
        show_text_button.clicked.connect(self.open_full_text)

        self.ui.NotesLineMW.clear()
        self.current_x += 285
        if self.current_x >= 1105:
            self.current_x = 250
            self.current_y += 185

            if self.current_y >= 860:  # TODO: CHANGE THE COUNTER LIKE: k=0 after ever creating note / click ENTER /
                # SMT ELSE k += 1 IF k == number: self.show_error()
                self.show_error()

    def create_delete_event_handler(self, note,x,y):
        def delete_event_handler():
            self.available_positions.append((x, y))
            note.deleteLater() # safe delete

        return delete_event_handler

    # doesnt work correct
    def open_full_text(self):
        note_text = self.ui.NotesLineMW.text()
        global window7
        window7 = QtWidgets.QMainWindow()
        ui7 = Text4Note()
        ui7.setupUi(window7)
        window7.show()
        frame = QtWidgets.QFrame(window7)
        frame.setStyleSheet(

            "background-color: rgb(255, 239, 205);"
        )
        frame.setGeometry(0, 0, 410, 1000)
        frame.show()

        label = QtWidgets.QLabel(frame)
        label.setText(note_text)
        # label.setStyleSheet(
        # "QFrame:hover {"
        # "   background-color: rgb(237,145,33);"
        # "}"
        # )
        label.show()

        # THE LOGIC OF THE WRAPING TEXT
        label.setWordWrap(True)
        label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        label.setGeometry(0, 0, 410, 1000)




    # doesnt work
    def move_notes(self):
        if self.available_positions:
            x, y = self.available_positions.pop(0)  # Берем первую свободную позицию из массива
            for note in self.findChildren(QtWidgets.QFrame):  # Находим все заметки
                if note.geometry().x() == self.current_x and note.geometry().y() == self.current_y:  # Находим текущую заметку
                    note.move(x, y)  # Перемещаем заметку на свободную позицию
                    self.current_x, self.current_y = x, y  # Обновляем текущие координаты заметки
                    break  # Заканчиваем поиск


    # THE LOGIC OF THE BUTTONS IS SIMILAR TO GOOGLE KEEP
    def create_enter_event_handler(self, *buttons):
        def enter_event_handler(event):
            self.show_buttons(*buttons)
        return enter_event_handler

    def create_leave_event_handler(self, *buttons):
        def leave_event_handler(event):
            self.hide_buttons(*buttons)
        return leave_event_handler

    def show_buttons(self, *buttons):
        for button in buttons:
            button.show()

    def hide_buttons(self, *buttons):
        for button in buttons:
            button.hide()

    # THE LOGIC OF THE ERRORS
    def show_error(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Уведомление')
        msg.setText('У вас максимальное кол-во заметок, чтобы добавить еще одну заметку придется чота удалить')
        eror = msg.exec_()

    def keyPressEvent(self, event):
        if event.key() in [QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter]:
            self.add_note()

        else:
            super(NotesTracker, self).keyPressEvent(event)





# Главная логика приложения
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = NotesTracker()
    window_login = AuthWindow()


    # Открытие главного окна при успешной аутентификации
    def show_main_window():
        window.show()


    window_login.authenticated.connect(show_main_window)
    window_login.show()
    sys.exit(app.exec())
