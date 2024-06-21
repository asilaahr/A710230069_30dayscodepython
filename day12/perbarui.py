import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class AplikasiSaya(QWidget):
    def __init__(self):  # Memperbaiki typo dari '_init_' menjadi '__init__'
        super().__init__()  # Memperbaiki typo dari '_init_' menjadi '__init__'
        self.initUI()

    def initUI(self):
        # Mengatur judul jendela dan ukuran jendela
        self.setWindowTitle('Input dan Label PyQt5')
        self.setGeometry(100, 100, 400, 200)
        
        # Membuat layout vertikal
        layout = QVBoxLayout()
        
        # Membuat label dan menambahkannya ke layout
        self.label = QLabel('Halo, PyQt5!', self)
        layout.addWidget(self.label)
        
        # Membuat QLineEdit dan menambahkannya ke layout
        self.lineEdit = QLineEdit(self)
        layout.addWidget(self.lineEdit)
        
        # Membuat tombol dan menambahkannya ke layout
        btn = QPushButton('Perbarui Label', self)
        btn.clicked.connect(self.updateLabel)
        layout.addWidget(btn)
        
        # Menetapkan layout ke widget utama
        self.setLayout(layout)
        self.show()

    def updateLabel(self):
        # Mengambil teks dari QLineEdit dan menetapkannya ke QLabel
        teks_input = self.lineEdit.text()
        self.label.setText(teks_input)

if __name__ == '__main__':
    # Membuat aplikasi dan menjalankannya
    app = QApplication(sys.argv)
    ex = AplikasiSaya()
    sys.exit(app.exec_())
