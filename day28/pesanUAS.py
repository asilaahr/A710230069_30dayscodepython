#PYQT

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aplikasi Sederhana PyQt5')
        self.setGeometry(100, 100, 300, 200)
        
        self.layout = QVBoxLayout()
        
        self.nimInput = QLineEdit(self)
        self.nimInput.setPlaceholderText('Masukkan NIM')
        self.layout.addWidget(self.nimInput)
        
        self.btn = QPushButton('Submit', self)
        self.btn.clicked.connect(self.showMessage)
        self.layout.addWidget(self.btn)
        
        self.setLayout(self.layout)
        self.show()

    def showMessage(self):
        nim = self.nimInput.text()
        if nim:
            QMessageBox.information(self, 'Pesan', f'Selamat mengerjakan UAS!!!, NIM: {nim}!')
        else:
            QMessageBox.warning(self, 'Pesan', 'Silakan masukkan NIM terlebih dahulu.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
