# PyQt imports
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUiType
import mysql.connector

ui, _ = loadUiType('homepage.ui')

# SQL Imports


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="baryeh1122",
    database="church"
)


# main class for homepage
class Homepage(QMainWindow, ui):
    def __init__(self):
        super(Homepage, self).__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    window = Homepage()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
