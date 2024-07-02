#PYQT

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox

class Perkenalan(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Buat label dan tombol
        self.label = QLabel("Tekan tombol untuk perkenalan", self)
        self.button = QPushButton("Perkenalkan", self)
        
        # Menghubungkan sinyal klik tombol ke fungsi perkenalan
        self.button.clicked.connect(self.show_message)

        # Mengatur layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.button)

        self.setLayout(vbox)
        
        # Pengaturan jendela
        self.setWindowTitle('Perkenalan Nama dan NIM')
        self.setGeometry(100, 100, 300, 200)

    def show_message(self):
        # Pesan perkenalan
        name = "Nama: Taylor"
        nim = "NIM: 64683278"

        # Menampilkan pesan dalam kotak dialog
        QMessageBox.information(self, "Perkenalan", f"{name}\n{nim}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    perkenalan = Perkenalan()
    perkenalan.show()
    sys.exit(app.exec_())
