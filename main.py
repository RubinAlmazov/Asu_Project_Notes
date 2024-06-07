import sys
from PySide6 import QtCore, QtWidgets
from main_window import Ui_MainWindow
from archive_window2 import Ui_ArchiveWindow
from reminders_window2 import RemindWindow
from trash_window2 import Ui_TrashWindow
from register_manage import AuthWindow
from full_text import Text4Note
from archive_manager import ArchiveManager
from remind_manage import RemindManager
from delete_manager import DeleteManager
from PySide6.QtCore import QTimer, QSize
from PySide6.QtGui import QIcon


class NotesTracker(QtWidgets.QMainWindow):
    def __init__(self):
        super(NotesTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.MainWindowButtMW.setCheckable(True)
        self.ui.ArchiveButtMW_2.clicked.connect(self.open_archive_window)
        self.ui.RemindButtMW_2.clicked.connect(self.open_remind_window)
        self.ui.TrashButtMW.clicked.connect(self.open_trash_window)

        self.current_x = 250
        self.current_y = 120
        self.notes = []  # Store (note_text, note) tuples

        self.ui.NotesLineMW.returnPressed.connect(self.add_note)

        # initialize instance attributes
        self.window3 = None
        self.window4 = None
        self.window5 = None
        self.archive_manager = None
        self.remind_manager = None
        self.delete_manager = None
        self.archive_manager = ArchiveManager(None)  # Singleton-like initialization
        self.remind_manager = RemindManager(None)
        self.delete_manager = DeleteManager(None)

        self.archive_manager.note_unarchived.connect(self.add_note_from_remove)
        self.remind_manager.note_unremind.connect(self.add_note_from_remove)
        self.delete_manager.note_undelete.connect(self.add_note_from_remove)

    #TODO: unnecessary code / delete
    def handle_note_remove(self, note_text):
        self.add_note_with_text(note_text)
        for i, (text, is_archived) in enumerate(self.archive_manager.notes):
            if text == note_text:
                self.archive_manager.notes[i] = (text, False)

    def add_note_from_remove(self, note_text):
        self.add_note_with_text(note_text)

    def add_note_with_text(self, note_text):
        note_text_short = note_text
        if len(note_text) > 297:
            note_text_short = note_text[:296] + '...'

        x, y = self.current_x, self.current_y

        note = QtWidgets.QFrame(self)
        note.setStyleSheet(
            "border: 1px solid rgb(0,0,0);"
            "background-color: rgb(255, 239, 205);"
        )
        note.setGeometry(x, y, 250, 170)
        note.show()

        label = QtWidgets.QLabel(note)
        label.setText(note_text_short)
        label.setWordWrap(True)
        label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        label.setGeometry(0, 0, 250, 170)
        label.show()

        # Create and position buttons
        delete_button = QtWidgets.QPushButton(note)
        archive_button = QtWidgets.QPushButton(note)
        remind_button = QtWidgets.QPushButton(note)
        show_text_button = QtWidgets.QPushButton("...", note)

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

        icon2 = QIcon()
        icon2.addFile(u"icons/notifications_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        remind_button.setIcon(icon2)
        remind_button.setIconSize(QSize(24, 24))
        icon1 = QIcon()
        icon1.addFile(u"icons/archive_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        archive_button.setIcon(icon1)
        archive_button.setIconSize(QSize(24, 24))
        icon3 = QIcon()
        icon3.addFile(u"icons/delete_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        delete_button.setIcon(icon3)
        delete_button.setIconSize(QSize(24, 24))

        delete_button.setGeometry(7, 135, 55, 30)
        archive_button.setGeometry(67, 135, 55, 30)
        remind_button.setGeometry(127, 135, 55, 30)
        show_text_button.setGeometry(187, 135, 55, 30)

        # Initially hide buttons
        delete_button.hide()
        archive_button.hide()
        remind_button.hide()
        show_text_button.hide()

        # Connect hover events
        note.enterEvent = self.create_enter_event_handler(delete_button, archive_button, remind_button,
                                                          show_text_button)
        note.leaveEvent = self.create_leave_event_handler(delete_button, archive_button, remind_button,
                                                          show_text_button)

        # Connect button events
        delete_button.clicked.connect(self.create_delete_event_handler(note, note_text))
        archive_button.clicked.connect(self.create_archive_event_handler(note, note_text))
        remind_button.clicked.connect(self.create_remind_event_handler(note, note_text))
        show_text_button.clicked.connect(self.create_show_text_event_handler(note_text))

        self.notes.append((note_text, note))
        self.reposition_notes()

    # moves notes to fill in the gaps after deletion.
    def reposition_notes(self):
        x, y = 250, 120
        for note_text, note in self.notes:
            note.setGeometry(x, y, 250, 170)
            x += 285
            if x >= 1105:
                x = 250
                y += 185

    def create_archive_event_handler(self, note, note_text):
        def archive_event_handler():
            self.archive_manager.add_note_to_archive(note_text)
            self.notes.remove((note_text, note))
            note.deleteLater()
            QTimer.singleShot(250, self.reposition_notes)


        return archive_event_handler

    def open_archive_window(self):
        self.window3 = QtWidgets.QMainWindow()
        ui3 = Ui_ArchiveWindow()
        ui3.setupUi(self.window3)
        self.close()
        self.window3.show()

        # Checking whether the archive manager was previously created If not, a new archive manager is created
        # If the archive manager already exists, the link to the new archive window is updated
        if self.archive_manager is None:
            self.archive_manager = ArchiveManager(self.window3)
        else:
            self.archive_manager.archive_window = self.window3

        self.archive_manager.restore_notes()  # Notes are restored from the archive using the archive manager

        ui3.MainWindowButtAW.clicked.connect(self.return_to_main_window)
        ui3.RemindButtAW.clicked.connect(self.open_remind_window)
        ui3.TrashButtAW.clicked.connect(self.open_trash_window)
        if self.window4:
            self.window4.close()
        if self.window5:
            self.window5.close()

    def return_to_main_window(self):
        self.window3.close()
        self.show()

    def open_remind_window(self):
        self.window4 = QtWidgets.QMainWindow()
        ui4 = RemindWindow()
        ui4.setupUi(self.window4)
        self.close()
        self.window4.show()

        if self.remind_manager is None:
            self.remind_manager = RemindManager(self.window4)
        else:
            self.remind_manager.remind_window = self.window4

        self.remind_manager.restore_notes()

        ui4.Main_Page_butt.clicked.connect(self.return_to_main_window2)
        ui4.Archive_butt.clicked.connect(self.open_archive_window)
        ui4.Trash_butt.clicked.connect(self.open_trash_window)
        if self.window3:
            self.window3.close()
        if self.window5:
            self.window5.close()

    def return_to_main_window2(self):
        self.window4.close()
        self.show()

    def open_trash_window(self):
        self.window5 = QtWidgets.QMainWindow()
        ui5 = Ui_TrashWindow()
        ui5.setupUi(self.window5)
        self.close()
        self.window5.show()

        if self.delete_manager is None:
            self.delete_manager = DeleteManager(self.window5)
        else:
            self.delete_manager.delete_window = self.window5

        self.delete_manager.restore_notes()

        ui5.Main_page_butt_TW.clicked.connect(self.return_to_main_window3)
        ui5.Archive_butt_TW.clicked.connect(self.open_archive_window)
        ui5.Remindes_butt_TW.clicked.connect(self.open_remind_window)
        if self.window3:
            self.window3.close()
        if self.window4:
            self.window4.close()

    def return_to_main_window3(self):
        self.window5.close()
        self.show()

    # For creating Notes / NOTES LOGIC
    def add_note(self):
        note_text = self.ui.NotesLineMW.text()
        full_note_text = self.ui.NotesLineMW.text()
        if not note_text.strip():
            return

        x, y = self.current_x, self.current_y
        max_length = 297
        if len(note_text) > max_length:
            note_text = note_text[:max_length - 1] + '...'  # TODO: SET A LIMIT AND DISPLAY IN TEXT_AREA 2 (TWO)

        note = QtWidgets.QFrame(self)
        note.setStyleSheet(
            "border: 1px solid rgb(0,0,0);"
            "background-color: rgb(255, 239, 205);"
        )
        note.setGeometry(x, y, 250, 170)
        note.show()

        label = QtWidgets.QLabel(note)
        label.setText(note_text)
        label.setWordWrap(True)
        label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        label.setGeometry(0, 0, 250, 170)
        label.show()

        delete_button = QtWidgets.QPushButton(note)
        archive_button = QtWidgets.QPushButton(note)
        remind_button = QtWidgets.QPushButton(note)
        show_text_button = QtWidgets.QPushButton("...", note)

        icon2 = QIcon()
        icon2.addFile(u"icons/notifications_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        remind_button.setIcon(icon2)
        remind_button.setIconSize(QSize(24, 24))
        icon1 = QIcon()
        icon1.addFile(u"icons/archive_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        archive_button.setIcon(icon1)
        archive_button.setIconSize(QSize(24, 24))
        icon3 = QIcon()
        icon3.addFile(u"icons/delete_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        delete_button.setIcon(icon3)
        delete_button.setIconSize(QSize(24, 24))


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

        # Connect hover events
        note.enterEvent = self.create_enter_event_handler(delete_button, archive_button, remind_button,
                                                          show_text_button)
        note.leaveEvent = self.create_leave_event_handler(delete_button, archive_button, remind_button,
                                                          show_text_button)

        # Connect button events
        delete_button.clicked.connect(self.create_delete_event_handler(note, full_note_text))
        archive_button.clicked.connect(self.create_archive_event_handler(note, full_note_text))
        remind_button.clicked.connect(self.create_remind_event_handler(note, full_note_text))
        show_text_button.clicked.connect(self.create_show_text_event_handler(full_note_text))

        self.notes.append((full_note_text, note))
        self.ui.NotesLineMW.clear()
        self.reposition_notes()

        self.current_x += 285
        if self.current_x >= 1105:
            self.current_x = 250
            self.current_y += 185



    # creates a note deletion event handler that deletes a note from the list and calls a function to move notes with a delay.
    def create_delete_event_handler(self, note, note_text):
        def delete_event_handler():
            self.delete_manager.add_note_to_delete(note_text)
            self.notes.remove((note_text, note))
            note.deleteLater()
            QTimer.singleShot(250, self.reposition_notes)

        return delete_event_handler

    def create_remind_event_handler(self, note, note_text):
        def remind_event_handler():
            self.remind_manager.add_note_to_remind(note_text)
            self.notes.remove((note_text, note))
            note.deleteLater()
            QTimer.singleShot(250, self.reposition_notes)

        return remind_event_handler

    def create_enter_event_handler(self, delete_button, archive_button, remind_button, show_text_button):
        def enter_event_handler(event):
            delete_button.show()
            archive_button.show()
            remind_button.show()
            show_text_button.show()

        return enter_event_handler

    def create_leave_event_handler(self, delete_button, archive_button, remind_button, show_text_button):
        def leave_event_handler(event):
            delete_button.hide()
            archive_button.hide()
            remind_button.hide()
            show_text_button.hide()

        return leave_event_handler

    def create_show_text_event_handler(self, note_text):
        def show_text_event_handler():
            self.open_full_text(note_text)

        return show_text_event_handler

    def open_full_text(self, full_note_text):
        global window7
        window7 = QtWidgets.QMainWindow()
        ui7 = Text4Note()
        ui7.setupUi(window7)
        ui7.label.setText(full_note_text)
        window7.show()

        frame = QtWidgets.QFrame(window7)
        frame.setStyleSheet("background-color: rgb(255, 239, 205);")
        frame.setGeometry(0, 0, 1000, 1000)
        frame.show()

        label = QtWidgets.QLabel(frame)
        label.setText(full_note_text)
        label.setWordWrap(True)
        label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        label.setGeometry(0, 0, 1000, 1000)
        label.show()


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
