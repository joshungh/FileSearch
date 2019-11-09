import sys, os, re
from threading import Thread
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
        self.all_drives = self.get_drives()
        self.initUI()

    def initUI(self):
        self.all_drives = self.get_drives()

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
        self.response_box.setText('')
        chosen_path = self.combo.currentText()
        self.combo.clear()
        self.response_box.setText(chosen_path)

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        li = self.search_directory(textboxValue)
        self.combo.addItems(li)
        self.textbox.setText("")

    @staticmethod
    def get_drives():
        response = os.popen("wmic logicaldisk get caption")
        list1 = []
        for line in response.readlines():
            line = line.strip("\n")
            line = line.strip("\r")
            line = line.strip(" ")
            if (line == "Caption" or line == ""):
                continue
            list1.append(line)
        print(drive for drive in list1)
        return list1

    def search_directory(self, keyword):
        results = []
        for each in self.all_drives:
            for root, dir, files in os.walk(each, topdown=True):
                for f in files:
                    if os.path.splitext(f)[1] == '.txt':
                        if re.compile(keyword).search(os.path.join(root, f)):
                            results.append(os.path.join(root, f))
        return results




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())