import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'File Explorer'
        self.left = 10
        self.top = 10
        self.width = 680
        self.height = 660
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button = QPushButton('Search', self)
        self.button.move(550, 25)

        self.combo = QComboBox(self)
        self.combo.move(20, 80)

        self.button2 = QPushButton('Go', self)
        self.button2.move(150, 80)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(500, 40)

        self.response_box = QLineEdit(self)
        self.response_box.move(20, 120)
        self.response_box.resize(640, 500)

        self.textbox.returnPressed.connect(self.button.click)
        self.combo.activated.connect(self.button2.click)
        self.button2.clicked.connect(self.get_text)
        self.button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def get_text(self):
        chosen_path = self.combo.currentText()
        self.response_box.setText(chosen_path)


    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        # search fn will create a list of paths which contain the keyword in textboxValue
        li = ['example.html', 'howdy_doody.py', 'no.php', 'ok.js', 'nopenopenope.css']
        li.append(textboxValue)
        self.combo.addItems(li)
        self.textbox.setText("")

    def display(self, wordSearch):
        dialog = QFileDialog()
        dialog.setNameFilter("*{}*".format(wordSearch))
        dialog.exec()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())