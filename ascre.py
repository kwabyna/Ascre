# PyQt imports
import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

from homepage import Homepage
# connect to database
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="baryeh1122",
    database="church"
)

cur = db.cursor()
ui, _ = loadUiType('logIn_take2.ui')


class Ascre_login(QWidget, ui):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self._homepage = Homepage()
        self.ui_effects()
        self.Handle_buttons()

    def ui_effects(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))

    def Handle_buttons(self):
        self.pushButton.clicked.connect(self.open_Homepage)

    def open_Homepage(self):
        username = self.username.text()
        password = self.password.text()
# Authentication for the password and username
        if len(username) == 0 or len(password) == 0:
            self.errorfield.setText("Input Username and Password")
        else:
            authenticate_query = 'SELECT user_password FROM users WHERE user_name = \'' + username + '\' '
            cur.execute(authenticate_query)
            password_results = cur.fetchone()[0]
            if password_results == password:
                self.errorfield.setText(" Sign In Successful")
                self._homepage.show()
                self.close()
            elif password_results != password:
                self.errorfield.setText(" Incorrect Username or Password")

            else:
                self.errorfield.setText(" Some other error")


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Ascre_login()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
