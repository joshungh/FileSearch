import sys, os, re
import openpyxl as xl
from threading import Thread
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QBrush, QColor
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
        self.combo.resize(500, 25)
        self.combo.move(20, 80)

        self.button2 = QPushButton('Go', self)
        self.button2.move(550, 77)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(500, 40)

        self.response_box = QTextEdit(self)
        self.response_box.setReadOnly(True)
        self.response_box.move(20, 120)
        self.response_box.resize(640, 500)

        self.textbox.returnPressed.connect(self.button.click)
        self.combo.activated.connect(self.button2.click)
        self.button2.clicked.connect(self.get_text)
        self.button.clicked.connect(self.on_click)

        self.show()


    @pyqtSlot()
    def get_text(self):
        self.response_box.setPlainText('')
        chosen_path = self.combo.currentText()
        text_content = ""
        print("chosen_path: ", chosen_path)
        if chosen_path is not "":
            if chosen_path.endswith('.txt'):
                with open(chosen_path) as f:
                    text = f.readlines()
                    for line in text:
                        words = line.split(" ")
                        print(words)
                        for word in words:
                            newWord = word

                            # get a list of the extra letters and symbols that come after the keyword
                            wordList = re.split(self.keyword, newWord)

                            # regex and strip for taking out all random symbols, new lines, etc..
                            newWord = re.sub(r'[^\w]', ' ', newWord)
                            newWord = newWord.strip("\n")
                            newWord = newWord.strip("\r")
                            newWord = newWord.strip(" ")

                            # check if the keyword is contained in the current word we're checking
                            if self.keyword in newWord:
                                # set text color to red and then print out to response_box
                                self.response_box.setTextColor(QColor(255, 0, 0))
                                self.response_box.insertPlainText(self.keyword)
                                
                                # insert the rest of the characters that aren't in the keyword in black
                                for extra in wordList:
                                    if extra is not '':
                                        self.response_box.setTextColor(QColor(0 ,0 ,0))
                                        self.response_box.insertPlainText(extra)

                            # all the other words that aren't the keyword (inserted in black)
                            else:
                                self.response_box.setTextColor(QColor(0, 0, 0))
                                self.response_box.insertPlainText(word + " ")
        self.combo.clear()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        self.keyword = textboxValue
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
            list1.append(line + '/')
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