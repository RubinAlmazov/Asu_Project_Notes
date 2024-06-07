from PySide6 import QtCore, QtWidgets
from full_text import Text4Note

class ArchiveManager:
    def __init__(self, archive_window):
        self.archive_window = archive_window
        self.current_x = 250
        self.current_y = 120
        self.notes = []
        self.remind_manager = None
        self.delete_manager = None

    def add_note_to_archive(self, note_text):
        self.full_note_text = note_text
        if not note_text.strip():
            return


        max_length = 298
        if len(note_text) > max_length:
            note_text = note_text[:max_length - 1] + '...'
        archive_note = QtWidgets.QFrame(self.archive_window)
        archive_note.setStyleSheet(
            "border: 1px solid rgb(0,0,0);"
            "background-color: rgb(255, 239, 205);"
        )
        archive_note.setGeometry(self.current_x, self.current_y, 250, 170)
        archive_note.show()

        label = QtWidgets.QLabel(archive_note)
        label.setText(note_text)
        label.setWordWrap(True)
        label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        label.setGeometry(0, 0, 250, 170)
        label.show()

        self.notes.append((note_text, self.current_x, self.current_y))

        self.current_x += 285
        if self.current_x >= 1105:
            self.current_x = 250
            self.current_y += 185


    def restore_notes(self):
        for note_text, x, y in self.notes:
            archive_note = QtWidgets.QFrame(self.archive_window)
            archive_note.setStyleSheet(
                "border: 1px solid rgb(0,0,0);"
                "background-color: rgb(255, 239, 205);"
            )
            archive_note.setGeometry(x, y, 250, 170)
            archive_note.show()

            label = QtWidgets.QLabel(archive_note)
            label.setText(note_text)
            label.setWordWrap(True)
            label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
            label.setGeometry(0, 0, 250, 170)
            label.show()

            # Creating buttons
            delete_button = QtWidgets.QPushButton("Удалить", archive_note)
            archive_button = QtWidgets.QPushButton("Архивировать", archive_note)
            remind_button = QtWidgets.QPushButton("Напомнить", archive_note)
            show_text_button = QtWidgets.QPushButton("...", archive_note)

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

            # Assigning event handlers
            archive_note.enterEvent = self.create_enter_event_handler(delete_button, archive_button, remind_button, show_text_button)
            archive_note.leaveEvent = self.create_leave_event_handler(delete_button, archive_button, remind_button, show_text_button)



            show_text_button.clicked.connect(self.create_show_text_event_handler(self.full_note_text))

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

