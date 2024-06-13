from PySide6 import QtCore, QtWidgets
from full_text import Text4Note
from PySide6.QtCore import Signal, QObject, QTimer, QSize
from PySide6.QtGui import QIcon
from datetime import datetime, timedelta

class RemindManager(QObject):
    note_unremind = Signal(str)

    def __init__(self, remind_window):
        super().__init__()
        self.remind_window = remind_window
        self.current_x = 250
        self.current_y = 20
        self.notes = []

    def add_note_to_remind(self, note_text):
        if not note_text.strip():
            return
        self.notes.append(note_text)  # Add note with archived status True

    def restore_notes(self):
        self.current_x, self.current_y = 250, 20
        self.reposition_notes()

    def reposition_notes(self):
        for widget in self.remind_window.findChildren(QtWidgets.QFrame):
            widget.deleteLater()

        self.current_x, self.current_y = 250, 20
        for note_text in self.notes:
            self.display_note_in_remind(note_text)

    def display_note_in_remind(self, note_text):
        max_length = 298
        display_text = note_text if len(note_text) <= max_length else note_text[:max_length - 1] + '...'

        remind_note = QtWidgets.QFrame(self.remind_window)
        remind_note.setStyleSheet(
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
        remind_note.setGeometry(self.current_x, self.current_y, 250, 170)
        remind_note.show()

        label = QtWidgets.QLabel(remind_note)
        label.setText(display_text)
        label.setWordWrap(True)
        label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        label.setGeometry(0, 0, 250, 170)
        label.show()

        # Create buttons
        remind_button = QtWidgets.QPushButton(remind_note)
        show_text_button = QtWidgets.QPushButton("...", remind_note)
        set_reminder_button = QtWidgets.QPushButton(remind_note)

        # Style and position buttons
        button_style = """
                       QPushButton {
                           background-color: rgba(255, 255, 255, 0.8);
                           border: 1px solid rgb(150, 150, 150);
                           border-radius: 5px;
                       }
                       """
        icon = QIcon()
        icon.addFile(u"icons/close_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        remind_button.setIcon(icon)
        remind_button.setIconSize(QSize(24, 24))
        icon2 = QIcon()
        icon2.addFile(u"icons/notifications_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        set_reminder_button.setIcon(icon2)
        set_reminder_button.setIconSize(QSize(24, 24))

        remind_button.setStyleSheet(button_style)
        show_text_button.setStyleSheet(button_style)
        set_reminder_button.setStyleSheet(button_style)

        set_reminder_button.setGeometry(127, 135, 55, 30)
        remind_button.setGeometry(67, 135, 55, 30)
        show_text_button.setGeometry(187, 135, 55, 30)

        # Initially hide buttons
        remind_button.hide()
        show_text_button.hide()
        set_reminder_button.hide()

        # Assign event handlers
        remind_note.enterEvent = self.create_enter_event_handler(remind_button, show_text_button, set_reminder_button)
        remind_note.leaveEvent = self.create_leave_event_handler(remind_button, show_text_button, set_reminder_button)

        remind_button.clicked.connect(self.create_unremind_event_handler(remind_note, note_text))
        show_text_button.clicked.connect(self.create_show_text_event_handler(note_text))
        set_reminder_button.clicked.connect(self.create_set_reminder_event_handler(note_text))

        self.current_x += 285
        if self.current_x >= 1105:
            self.current_x = 250
            self.current_y += 185

    def create_unremind_event_handler(self, note, full_note_text):
        def unremind_note():
            try:
                self.notes.remove(full_note_text)
            except ValueError:
                return
            self.note_unremind.emit(full_note_text)
            note.deleteLater()
            QTimer.singleShot(250, self.reposition_notes)

        return unremind_note

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

    def create_set_reminder_event_handler(self, note_text):
        def set_reminder_event_handler():
            minutes, ok = self.get_reminder_time()
            if ok:
                reminder_time = datetime.now() + timedelta(minutes=minutes)
                QTimer.singleShot(minutes * 60000, self.create_show_reminder(note_text))
                print(f"Напоминания установлено на  {reminder_time.strftime('%Y-%m-%d %H:%M:%S')}")

        return set_reminder_event_handler

    def get_reminder_time(self):
        remind = QtWidgets.QInputDialog.getInt(
            self.remind_window, "Напоминание", "Напомнить через:", minValue=1

        )
        return remind

    def create_show_reminder(self, note_text):
        def show_reminder():
            reminder_dialog = QtWidgets.QMessageBox(self.remind_window)
            reminder_dialog.setWindowTitle("Напоминание")
            reminder_dialog.setStyleSheet("""
                                                    background-color: qlineargradient(x1: 0, y1: 0, 
                                                                                      x2: 0, y2: 1, 
                                                                                      stop: 0 rgba(255, 248, 220, 204),
                                                                                      stop: 1 rgba(245, 222, 179, 204));
                                                    font: 12pt "Times New Roman";
                                                """)
            reminder_dialog.setText(f"Напоминание о заметке: {note_text}")
            reminder_dialog.setIcon(QtWidgets.QMessageBox.Information)
            reminder_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
            reminder_dialog.exec_()

        return show_reminder
