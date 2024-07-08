#PYQT PENGHITUNG WAKTU

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer, QTime

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.time = QTime(0, 0, 0)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.label = QLabel(self.time.toString('hh:mm:ss'), self)

        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.start_timer)

        self.stop_button = QPushButton('Stop', self)
        self.stop_button.clicked.connect(self.stop_timer)

        self.reset_button = QPushButton('Reset', self)
        self.reset_button.clicked.connect(self.reset_timer)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)

        self.setLayout(vbox)
        self.setWindowTitle('Timer App')
        self.show()

    def update_timer(self):
        self.time = self.time.addSecs(1)
        self.label.setText(self.time.toString('hh:mm:ss'))

    def start_timer(self):
        self.timer.start(1000)

    def stop_timer(self):
        self.timer.stop()

    def reset_timer(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0)
        self.label.setText(self.time.toString('hh:mm:ss'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TimerApp()
    sys.exit(app.exec_())
