from PySide6 import QtCore, QtWidgets
from full_text import Text4Note
from PySide6.QtCore import Signal, QObject,  QTimer, QSize
from PySide6.QtGui import QIcon

class ArchiveManager(QObject):
    note_unarchived = Signal(str)

    def __init__(self, archive_window):
        super().__init__()
        self.archive_window = archive_window
        self.current_x = 250
        self.current_y = 20
        self.notes = []

    def add_note_to_archive(self, note_text):
        if not note_text.strip():
            return

        self.notes.append(note_text)  # Add note with archived status True

    def restore_notes(self):
        self.current_x, self.current_y = 250, 20
        self.reposition_notes()


    def reposition_notes(self):
        for widget in self.archive_window.findChildren(QtWidgets.QFrame):
            widget.deleteLater()

        self.current_x, self.current_y = 250, 20
        for note_text in self.notes:
            self.display_note_in_archive(note_text)

    def display_note_in_archive(self, note_text):
        max_length = 298
        display_text = note_text if len(note_text) <= max_length else note_text[:max_length - 1] + '...'

        archive_note = QtWidgets.QFrame(self.archive_window)
        archive_note.setStyleSheet(
            "border: 1px solid rgb(0,0,0);"
            "background-color: rgb(255, 239, 205);"
        )
        archive_note.setGeometry(self.current_x, self.current_y, 250, 170)
        archive_note.show()

        label = QtWidgets.QLabel(archive_note)
        label.setText(display_text)
        label.setWordWrap(True)
        label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        label.setGeometry(0, 0, 250, 170)
        label.show()

        # Create buttons
        archive_button = QtWidgets.QPushButton(archive_note)
        show_text_button = QtWidgets.QPushButton("...", archive_note)
        icon = QIcon()
        icon.addFile(u"../../Downloads/unarchive_24dp_FILL0_wght400_GRAD0_opsz24 (2).svg", QSize(), QIcon.Normal, QIcon.Off)
        archive_button.setIcon(icon)
        archive_button.setIconSize(QSize(24, 24))

        # Style and position buttons
        button_style = """
                       QPushButton {
                           background-color: rgba(255, 255, 255, 0.8);
                           border: 1px solid rgb(150, 150, 150);
                           border-radius: 5px;
                       }
                       """
        archive_button.setStyleSheet(button_style)
        show_text_button.setStyleSheet(button_style)

        archive_button.setGeometry(127, 135, 55, 30)
        show_text_button.setGeometry(187, 135, 55, 30)

        # Initially hide buttons
        archive_button.hide()
        show_text_button.hide()

        # Assign event handlers
        archive_note.enterEvent = self.create_enter_event_handler(archive_button, show_text_button)
        archive_note.leaveEvent = self.create_leave_event_handler(archive_button, show_text_button)

        archive_button.clicked.connect(self.create_unarchive_event_handler(archive_note, note_text))
        show_text_button.clicked.connect(self.create_show_text_event_handler(note_text))

        self.current_x += 285
        if self.current_x >= 1105:
            self.current_x = 250
            self.current_y += 185

    def create_unarchive_event_handler(self, note, full_note_text):
        def unarchived_note():
            try:
                self.notes.remove(full_note_text)
            except ValueError:
                return
            self.note_unarchived.emit(full_note_text)
            note.deleteLater()
            QTimer.singleShot(250, self.reposition_notes)

        return unarchived_note

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
