import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

class AplikasiSederhana(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Contoh PyQt Sederhana')
        
        # Membuat layout
        layout = QVBoxLayout()
        
        # Membuat tombol
        self.tombol = QPushButton('Klik Saya', self)
        self.tombol.clicked.connect(self.tampilkanPesan)
        
        # Menambahkan tombol ke layout
        layout.addWidget(self.tombol)
        
        # Mengatur layout pada jendela
        self.setLayout(layout)
        
        # Menentukan ukuran jendela
        self.setGeometry(300, 300, 300, 200)

    def tampilkanPesan(self):
        QMessageBox.information(self, 'Pesan', 'Tombol telah diklik!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AplikasiSederhana()
    ex.show()
    sys.exit(app.exec_())
