from PySide6 import QtCore, QtWidgets

class RemindManager:
    def __init__(self, remind_window):
        self.remind_window = remind_window
        self.current_x = 250
        self.current_y = 120
        self.notes = []

    def add_note_to_remind(self, note_text):
        if not note_text.strip():
            return

        max_length = 298
        if len(note_text) > max_length:
            note_text = note_text[:max_length - 1] + '...'
        remind_note = QtWidgets.QFrame(self.remind_window)
        remind_note.setStyleSheet(
            "border: 1px solid rgb(0,0,0);"
            "background-color: rgb(255, 239, 205);"
        )
        remind_note.setGeometry(self.current_x, self.current_y, 250, 170)
        remind_note.show()

        label = QtWidgets.QLabel(remind_note)
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


        QtWidgets.QApplication.processEvents() # doesnt work

        # Creating buttons
        delete_button = QtWidgets.QPushButton("Удалить", remind_note)
        archive_button = QtWidgets.QPushButton("Архивировать", remind_note)
        remind_button = QtWidgets.QPushButton("Напомнить", remind_note)
        show_text_button = QtWidgets.QPushButton("...", remind_note)

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
        remind_note.enterEvent = self.create_enter_event_handler(delete_button, archive_button, remind_button,
                                                                 show_text_button)
        remind_note.leaveEvent = self.create_leave_event_handler(delete_button, archive_button, remind_button,
                                                                 show_text_button)


    def restore_notes(self):
        for note_text, x, y in self.notes:
            remind_note = QtWidgets.QFrame(self.remind_window)
            remind_note.setStyleSheet(
                "border: 1px solid rgb(0,0,0);"
                "background-color: rgb(255, 239, 205);"
            )
            remind_note.setGeometry(x, y, 250, 170)
            remind_note.show()

            label = QtWidgets.QLabel(remind_note)
            label.setText(note_text)
            label.setWordWrap(True)
            label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
            label.setGeometry(0, 0, 250, 170)
            label.show()

            # Creating buttons
            delete_button = QtWidgets.QPushButton("Удалить", remind_note)
            archive_button = QtWidgets.QPushButton("Архивировать", remind_note)
            remind_button = QtWidgets.QPushButton("Напомнить", remind_note)
            show_text_button = QtWidgets.QPushButton("...", remind_note)

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
            remind_note.enterEvent = self.create_enter_event_handler(delete_button, archive_button, remind_button,
                                                                     show_text_button)
            remind_note.leaveEvent = self.create_leave_event_handler(delete_button, archive_button, remind_button,
                                                                     show_text_button)
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
