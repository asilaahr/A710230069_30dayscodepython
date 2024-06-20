import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTextEdit, QLineEdit, QMessageBox, QListWidget

class DiaryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Title layout
        self.title_layout = QHBoxLayout()
        self.title_label = QLabel("Title:")
        self.title_input = QLineEdit()
        self.title_layout.addWidget(self.title_label)
        self.title_layout.addWidget(self.title_input)
        self.layout.addLayout(self.title_layout)

        # Text layout
        self.text_label = QLabel("Content:")
        self.layout.addWidget(self.text_label)
        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        # Buttons layout
        self.buttons_layout = QHBoxLayout()
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_note)
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_note)
        self.buttons_layout.addWidget(self.save_button)
        self.buttons_layout.addWidget(self.clear_button)
        self.layout.addLayout(self.buttons_layout)

        # Notes list
        self.notes_list = QListWidget()
        self.notes_list.itemClicked.connect(self.load_note)
        self.layout.addWidget(self.notes_list)

        self.setLayout(self.layout)
        self.setWindowTitle("Diary App")
        self.show()

        # Storage for notes
        self.notes = {}

    def save_note(self):
        title = self.title_input.text()
        content = self.text_edit.toPlainText()

        if title and content:
            self.notes[title] = content
            self.update_notes_list()
            self.clear_note()
        else:
            QMessageBox.warning(self, "Incomplete Data", "Please provide both title and content.")

    def clear_note(self):
        self.title_input.clear()
        self.text_edit.clear()

    def update_notes_list(self):
        self.notes_list.clear()
        for title in self.notes.keys():
            self.notes_list.addItem(title)

    def load_note(self, item):
        title = item.text()
        content = self.notes.get(title, "")
        self.title_input.setText(title)
        self.text_edit.setPlainText(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DiaryApp()
    sys.exit(app.exec_())
