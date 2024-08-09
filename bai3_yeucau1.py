import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox,QHBoxLayout,QVBoxLayout
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle('Game ')
        self.setGeometry(300, 300, 300, 200)
        
# Tạo các nút
        btnStart = QPushButton('Bắt đầu game', self)
        btnStart.clicked.connect(self.startGame)
        btnEnd = QPushButton('Thoát game', self)
        btnEnd.clicked.connect(self.endGame)

        # Căn giữa các nút có trong widget
        hbox = QVBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btnStart)
        hbox.addWidget(btnEnd)
        hbox.addStretch(1)

        # Thêm layout vào widget
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.show()

    def startGame(self):
        QMessageBox.information(self, 'Thông báo', 'Chương trình bắt đầu chạy')

    def endGame(self):
        reply = QMessageBox.question(self, 'Thoát game', 'Bạn có muốn thoát game không?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)   

    ex = MyApp()
    sys.exit(app.exec_())
