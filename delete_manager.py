from PySide6 import QtCore, QtWidgets
from full_text import Text4Note
from PySide6.QtCore import Signal, QObject,  QTimer, QSize
from PySide6.QtGui import QIcon
from notes_manager import update_note_state

class DeleteManager(QObject):
    note_undelete = Signal(str)

    def __init__(self, delete_window,user_login):
        super().__init__()
        self.delete_window = delete_window
        self.user_login = user_login
        self.current_x = 250
        self.current_y = 20
        self.notes = []


    def remove_note(self, note_text):
        if note_text in self.notes:
            self.notes.remove(note_text)

    def add_note_to_delete(self, note_text):
        if not note_text.strip():
            return
        self.notes.append(note_text)  # Add note text to the list

    def restore_notes(self):
        self.current_x, self.current_y = 250, 20
        self.reposition_notes()

    def reposition_notes(self):
        for widget in self.delete_window.findChildren(QtWidgets.QFrame):
            widget.deleteLater()

        self.current_x, self.current_y = 250, 20
        for note_text in self.notes:
            self.display_note_in_delete(note_text)

    def display_note_in_delete(self, note_text):
        max_length = 310
        display_text = note_text if len(note_text) <= max_length else note_text[:max_length - 1] + '...'

        delete_note = QtWidgets.QFrame(self.delete_window)
        delete_note.setStyleSheet(
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
        delete_note.setGeometry(self.current_x, self.current_y, 250, 170)
        delete_note.show()

        label = QtWidgets.QLabel(delete_note)
        label.setText(display_text)
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

        # Create buttons
        delete_button = QtWidgets.QPushButton(delete_note)
        show_text_button = QtWidgets.QPushButton("...", delete_note)
        delete_db_button = QtWidgets.QPushButton(delete_note)

        icon = QIcon()
        icon.addFile(u"icons/close_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2 = QIcon()
        icon2.addFile(u"icons/delete_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        delete_db_button.setIcon(icon2)
        delete_button.setIcon(icon)
        delete_button.setIconSize(QSize(24, 24))
        delete_db_button.setIconSize(QSize(24, 24))

        # Style and position buttons
        button_style = """
                       QPushButton {
                           background-color: rgba(255, 255, 255, 0.8);
                           border: 1px solid rgb(150, 150, 150);
                           border-radius: 5px;
                       }
                       """
        delete_button.setStyleSheet(button_style)
        show_text_button.setStyleSheet(button_style)
        delete_db_button.setStyleSheet(button_style)  # Style the new button

        delete_button.setGeometry(127, 135, 55, 30)
        show_text_button.setGeometry(187, 135, 55, 30)
        delete_db_button.setGeometry(67, 135, 55, 30)  # Position the new button

        # Initially hide buttons
        delete_button.hide()
        show_text_button.hide()
        delete_db_button.hide()  # Hide the new button

        # Assign event handlers
        delete_note.enterEvent = self.create_enter_event_handler(delete_button, show_text_button, delete_db_button)
        delete_note.leaveEvent = self.create_leave_event_handler(delete_button, show_text_button, delete_db_button)

        delete_button.clicked.connect(self.create_undelete_event_handler(delete_note, note_text))
        show_text_button.clicked.connect(self.create_show_text_event_handler(note_text))
        delete_db_button.clicked.connect(
            self.create_delete_from_db_event_handler(delete_note, note_text))  # Event handler for the new button

        self.current_x += 285
        if self.current_x >= 1105:
            self.current_x = 250
            self.current_y += 185

    def create_delete_from_db_event_handler(self, note, note_text):
        def delete_from_db():
            dialog = ConfirmDelete(self.delete_window)
            if dialog.exec() == QtWidgets.QDialog.Accepted:
                update_note_state(self.user_login, note_text, 'deleted')  # Помечаем как удаленную
                self.notes.remove(note_text)
                note.deleteLater()
                QTimer.singleShot(250, self.reposition_notes)
            else:
                dialog.close()

        return delete_from_db

    def create_undelete_event_handler(self, note, full_note_text):
        def undelete_note():
            try:
                self.notes.remove(full_note_text)
            except ValueError:
                return
            self.note_undelete.emit(full_note_text)
            note.deleteLater()
            QTimer.singleShot(250, self.reposition_notes)

        return undelete_note

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




class ConfirmDelete(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Подтвердите удаление")
        self.setFixedSize(300, 100)

        self.setStyleSheet("""
                            background-color: qlineargradient(x1: 0, y1: 0, 
                                                              x2: 0, y2: 1, 
                                                              stop: 0 rgba(255, 248, 220, 204),
                                                              stop: 1 rgba(245, 222, 179, 204));
                            font: 12pt "Times New Roman";
                           
                        """)
        self.label = QtWidgets.QLabel("Вы уверены, что хотите удалить заметку?", self)
        self.label.move(10, 10)
        self.label.adjustSize()

        button_style = """
                               QPushButton {
                                   background-color: rgba(255, 255, 255, 0.8);
                                   border: 1px solid rgb(150, 150, 150);
                                   border-radius: 5px;
                               }
                               """

        self.yes_button = QtWidgets.QPushButton("Да", self)
        self.yes_button.setStyleSheet(button_style)
        self.yes_button.setGeometry(40, 60, 100, 30)
        self.yes_button.clicked.connect(self.accept)

        self.no_button = QtWidgets.QPushButton("Нет", self)
        self.no_button.setStyleSheet(button_style)
        self.no_button.setGeometry(160, 60, 100, 30)
        self.no_button.clicked.connect(self.reject)

