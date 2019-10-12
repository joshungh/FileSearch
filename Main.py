from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os
import re

# class Window(QMainWindow):
    # def __init__(self):
    #     super().__init__()
    #     self.title = "PyQt5 Window"
    #     self.top = 200
    #     self.left = 500
    #     self.width = 400
    #     self.height = 300
    #     self.InitWindow()


def search_directory(root_dir, keyword):
    res = {}
    for root, dirs, files in os.walk(root_dir):
        count = 0
        for f in files:
            if re.compile(keyword).search(f):
                count += 1
        res[root] = count

    return res


    # def InitWindow(self):
    #     self.setWindowIcon(QtGui.QIcon("icon.png"))
    #     self.setWindowTitle(self.title)
    #     self.setGeometry(self.left, self.top, self.width, self.height)
    #     self.show()


def main():
    data = search_directory(sys.argv[1], sys.argv[2])
    print(data)

if __name__ == '__main__':
    main()

# App = QApplication(sys.argv)
# window = Window()
# sys.exit(App.exec())
