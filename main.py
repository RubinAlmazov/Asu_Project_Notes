import sys
from PySide6 import QtCore, QtWidgets
from main_window4 import Ui_MainWindow
from archive_window3 import Ui_ArchiveWindow
from reminders_window3 import RemindWindow
from trash_window3 import Ui_TrashWindow
from register_manager import AuthWindow
from full_text import Text4Note
from archive_manager import ArchiveManager
from remind_manager import RemindManager
from delete_manager import DeleteManager
from PySide6.QtCore import QTimer, QSize
from PySide6.QtGui import QIcon
from notes_manager import *
import pandas as pd
import sqlite3
import datetime

class NotesTracker(QtWidgets.QMainWindow):
    def __init__(self, user_login):
        super(NotesTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ArchiveButtMW_2.clicked.connect(self.open_archive_window)
        self.ui.RemindButtMW_2.clicked.connect(self.open_remind_window)
        self.ui.TrashButtMW.clicked.connect(self.open_trash_window)
        self.ui.TrashButtMW_2.clicked.connect(self.export_data)

        self.current_x = 250
        self.current_y = 120

        self.notes = []  # Store (note_text, note) tuples
        self.displayed_note_ids = []  # Store IDs of displayed notes

        self.ui.NotesLineMW.returnPressed.connect(self.add_note)

        # initialize instance attributes
        self.current_window = None
        self.window3 = None
        self.window4 = None
        self.window5 = None
        self.archive_manager = ArchiveManager(self)  # Singleton-like initialization
        self.remind_manager = RemindManager(self)
        self.delete_manager = DeleteManager(self, user_login)

        self.archive_manager.note_unarchived.connect(self.add_note_from_remove)
        self.remind_manager.note_unremind.connect(self.add_note_from_remove)
        self.delete_manager.note_undelete.connect(self.add_note_from_remove)

        self.setStyleSheet("""
            QWidget {
                background: QLinearGradient(x1: 0, y1: 0,
                                            x2: 0, y2: 1,
                                            stop: 0   rgba(69, 43, 26, 255),
                                            stop: 0.5 rgba(102, 68, 34, 255),
                                            stop: 1   rgba(122, 101, 82, 255));
            }
        """)
        self.user_login = user_login
        self.load_notes_from_db()

    def load_notes_from_db(self):
        notes = get_notes_from_db(self.user_login)
        for note_text, pos_x, pos_y, note_id in notes:
            self.add_note_with_text(note_text, pos_x, pos_y, note_id)

    def add_note_from_remove(self, note_text):
        self.add_note_with_text(note_text)

    def add_note_with_text(self, note_text, x=None, y=None, note_id=None, window=None):
        if window is None:
            window = self.current_window

        if note_text in [note[0] for note in self.notes]:
            return
        if x is None or y is None:
            x, y = self.get_next_position()

        note_text_short = note_text
        if len(note_text) > 310:
            note_text_short = note_text[:296] + '...'

        x, y = self.current_x, self.current_y

        note = QtWidgets.QFrame(self)
        note.setStyleSheet(
            """
                QFrame {
                    background-color: rgba(255, 239, 205, 204); 
                    border: 1px solid rgb(150, 150, 150);
                    border-radius: 5px;
                }
                QFrame:focus {
                    background-color: rgba(235, 235, 235, 204);  
                    border: 1px solid rgb(90, 90, 90);
                }
                """
        )
        note.setGeometry(x, y, 250, 170)
        note.show()

        label = QtWidgets.QLabel(note)
        label.setText(note_text_short)
        label.setWordWrap(True)
        label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        label.setGeometry(10, 10, 230, 150)
        label.setStyleSheet(
            """
            QLabel {
                padding: 5px;  
                font-size: 12px;
                color: #333;
            }
            """
        )
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
        if note_id is None:
            add_note_to_db(self.user_login, note_text, x, y)
            conn = sqlite3.connect('notestest2.db')
            cur = conn.cursor()
            cur.execute("SELECT ID FROM notes WHERE user_login = ? AND note_text = ? AND pos_x = ? AND pos_y = ?",
                        (self.user_login, note_text, x, y))
            note_id = cur.fetchone()[0]
            conn.close()
        self.displayed_note_ids.append(note_id)
        self.reposition_notes()
    # moves notes to fill in the gaps after deletion.

    def get_next_position(self):
        x, y = 250, 120
        for note_text, note in self.notes:
            x += 285
            if x >= 1105:
                x = 250
                y += 185
        return x, y

    def reposition_notes(self):
        x, y = 250, 120
        for note_text, note in self.notes:
            note.setGeometry(x, y, 250, 170)
            x += 285
            if x >= 1105:
                x = 250
                y += 185

    def export_data(self):
        if not self.displayed_note_ids:
            return


        current_time = datetime.datetime.now().strftime("%H-%M")
        export_file = f'{self.user_login}_{current_time}_.csv'

        conn = sqlite3.connect('notestest2.db')
        placeholder = ', '.join(['?'] * len(self.displayed_note_ids))
        query = f'SELECT ID, user_login, note_text FROM notes WHERE ID IN ({placeholder})'
        df = pd.read_sql(query, conn, params=self.displayed_note_ids)
        df.to_csv(export_file, index=False)
        print(f"Данные успешно преобразованы в файл {export_file}")
        conn.close()

    def create_archive_event_handler(self, note, note_text):
        def archive_event_handler():
            self.archive_manager.add_note_to_archive(note_text)
            self.notes.remove((note_text, note))
            note.deleteLater()
            QTimer.singleShot(250, self.reposition_notes)

        return archive_event_handler

    def open_archive_window(self):
        self.current_window = self.window3
        self.window3 = QtWidgets.QMainWindow()
        ui3 = Ui_ArchiveWindow()
        ui3.setupUi(self.window3)
        self.close()
        self.window3.show()

        if self.archive_manager is None:
            self.archive_manager = ArchiveManager(self.window3)
        else:
            self.archive_manager.archive_window = self.window3

        self.archive_manager.restore_notes()

        ui3.MainWindowButtMW.clicked.connect(self.return_to_main_window)
        ui3.RemindButtMW_2.clicked.connect(self.open_remind_window)
        ui3.TrashButtMW.clicked.connect(self.open_trash_window)
        if self.window4:
            self.window4.close()
        if self.window5:
            self.window5.close()

    def return_to_main_window(self):
        self.window3.close()
        self.show()

    def open_remind_window(self):
        self.current_window = self.window4
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

        ui4.MainWindowButtMW.clicked.connect(self.return_to_main_window2)
        ui4.ArchiveButtMW_2.clicked.connect(self.open_archive_window)
        ui4.TrashButtMW.clicked.connect(self.open_trash_window)
        if self.window3:
            self.window3.close()
        if self.window5:
            self.window5.close()

    def return_to_main_window2(self):
        self.window4.close()
        self.show()

    def open_trash_window(self):
        self.current_window = self.window5
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

        ui5.MainWindowButtMW.clicked.connect(self.return_to_main_window3)
        ui5.ArchiveButtMW_2.clicked.connect(self.open_archive_window)
        ui5.RemindButtMW_2.clicked.connect(self.open_remind_window)
        if self.window3:
            self.window3.close()
        if self.window4:
            self.window4.close()

    def return_to_main_window3(self):
        self.window5.close()
        self.show()

    def add_note(self):
        note_text = self.ui.NotesLineMW.text()
        if note_text.strip() != "":
            self.add_note_with_text(note_text.strip())
        self.ui.NotesLineMW.clear()

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

        # Create a scroll area
        scroll_area = QtWidgets.QScrollArea(window7)
        scroll_area.setWidgetResizable(True)

        # Create a frame to hold the text
        frame = QtWidgets.QFrame()
        frame.setStyleSheet(
            """
            QFrame {
                background-color: rgba(255, 239, 205, 204); 
                border: 1px solid rgb(150, 150, 150);
                border-radius: 5px;
            }
            QFrame:focus {
                background-color: rgba(235, 235, 235, 204);  
                border: 1px solid rgb(90, 90, 90);
            }
            """
        )

        # Create a layout for the frame
        layout = QtWidgets.QVBoxLayout(frame)
        frame.setLayout(layout)

        # Create a label to display the text
        label = QtWidgets.QLabel(frame)
        label.setText(full_note_text)
        label.setWordWrap(True)
        label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        layout.addWidget(label)

        # Set the frame as the widget for the scroll area
        scroll_area.setWidget(frame)

        # Set the scroll area as the central widget of the window
        window7.setCentralWidget(scroll_area)

        window7.show()


# Главная логика приложения
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window_login = AuthWindow()
    window = None


    def show_main_window(user_login):
        global window
        if window is None:
            window = NotesTracker(user_login)
        window.show()
        window_login.hide()


    window_login.authenticated.connect(show_main_window)
    window_login.show()
    sys.exit(app.exec())
