from PySide.QtCore import *
from PySide.QtGui import *
import sys
import random
import time


class Form(QDialog):
    def __init__(self, parent = None):

        super(Form, self).__init__(parent)
        self.kontrol = [8,2,7,1,5,4,3,9,6,9,6,5,3,2,7,1,4,8,3,4,1,6,8,9,7,5,2,5,9,3,4,6,8,2,7,1,4,7,2,3,1,3,6,8,9,6,1,8,9,7,2,4,3,5,7,8,6,2,3,5,9,1,4,1,5,4,7,9,6,8,2,3,2,3,9,8,4,1,5,6,7]
        self.hra = [8,2,7,1,5,4,3,9,6,9,6,5,3,2,7,1,4,8,3,4,1,6,8,9,7,5,2,5,9,3,4,6,8,2,7,1,4,7,2,3,1,3,6,8,9,6,1,8,9,7,2,4,3,5,7,8,6,2,3,5,9,1,4,1,5,4,7,9,6,8,2,3,2,3,9,8,4,1,5,6,7]
        index = 0
        grid = QGridLayout()
        Uloz = Promena()
        # vytvori hraci plochu 9x9
        Zmenit = [Uloz.zmenit1, Uloz.zmenit2, Uloz.zmenit3, Uloz.zmenit4, Uloz.zmenit5, Uloz.zmenit6, Uloz.zmenit7, Uloz.zmenit8, Uloz.zmenit9]
        self.Pole = [[0 for x in range(9)] for y in range(9)]
        self.Jedazdev = [0 for x in range(9)]
        for i in range(1):
            poradi = random.randint(0,80)
            self.hra[poradi] = 0

        for i in range(9):
            self.Jedazdev[i] = QPushButton("%d" % ( 1 + i))
            self.Jedazdev[i].setStyleSheet("background-color: lightblue")
            self.Jedazdev[i].clicked.connect(lambda i = i: Zmenit[i]())
            grid.addWidget(self.Jedazdev[i], i, 0)
            for j in range(9):
                self.Pole[i][j] = QPushButton()
                grid.addWidget(self.Pole[i][j], i, j + 1)
                self.Pole[i][j].setStyleSheet("background-color: white")
                self.Pole[i][j].setMaximumWidth(70)
                self.Pole[i][j].clicked.connect(lambda i = i, j = j: self.Pole[i][j].setText(Uloz.Hod()))
                self.Pole[i][j].clicked.connect(lambda: Form.kontrola(self))
                self.Jedazdev[i].clicked.connect(lambda j = j: self.Jedazdev[j].setStyleSheet("background-color: lightblue"))
                if i in [0,1,2]:
                    if j in [3,4,5]:
                        self.Pole[i][j].setStyleSheet("background-color: lightgray")
                if i in [3,4,5]:
                    if j in [0,1,2,6,7,8]:
                        self.Pole[i][j].setStyleSheet("background-color: lightgray")
                if i in [6,7,8]:
                    if j in [3,4,5]:
                        self.Pole[i][j].setStyleSheet("background-color: lightgray")
                if self.hra[index] != 0:
                    self.Pole[i][j].setText(str(self.hra[index]))
                    self.Pole[i][j].setEnabled(False)
                index += 1
            self.Jedazdev[i].clicked.connect(lambda i = i: self.Jedazdev[i].setStyleSheet("background-color: lightgreen"))
        self.Smazat = QPushButton("Smazat")
        self.Smazat.setStyleSheet("background-color: pink")
        self.Smazat.clicked.connect(lambda: Uloz.Smazat())
        self.Smazat.clicked.connect(lambda: self.Jedazdev[0].setStyleSheet("background-color: lightblue"))
        self.Smazat.clicked.connect(lambda: self.Jedazdev[1].setStyleSheet("background-color: lightblue"))
        self.Smazat.clicked.connect(lambda: self.Jedazdev[2].setStyleSheet("background-color: lightblue"))
        self.Smazat.clicked.connect(lambda: self.Jedazdev[3].setStyleSheet("background-color: lightblue"))
        self.Smazat.clicked.connect(lambda: self.Jedazdev[4].setStyleSheet("background-color: lightblue"))
        self.Smazat.clicked.connect(lambda: self.Jedazdev[5].setStyleSheet("background-color: lightblue"))
        self.Smazat.clicked.connect(lambda: self.Jedazdev[6].setStyleSheet("background-color: lightblue"))
        self.Smazat.clicked.connect(lambda: self.Jedazdev[7].setStyleSheet("background-color: lightblue"))
        self.Smazat.clicked.connect(lambda: self.Jedazdev[8].setStyleSheet("background-color: lightblue"))
        grid.addWidget(self.Smazat)
        self.setWindowTitle("Sudoku")



        self.setLayout(grid)
    def kontrola(self):
        index2 = 0
        vyhra = [0 for x in range(81)]
        for i in range(9):
            for j in range(9):
                vyhra[index2] = self.Pole[i][j].text() == str(self.kontrol[index2])
                index2 += 1
        if vyhra == [True] * 81:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Vyhra")
            msg.setInformativeText("Doplnkova informace")
            msg.setWindowTitle("Pozor:")
            msg.setDetailedText("Vyhral jste!")


            retval = msg.exec_()

class Promena():
    hodnota = ""
    def zmenit1(self):
        self.hodnota = 1
    def zmenit2(self):
        self.hodnota = 2
    def zmenit3(self):
        self.hodnota = 3
    def zmenit4(self):
        self.hodnota = 4
    def zmenit5(self):
        self.hodnota = 5
    def zmenit6(self):
        self.hodnota = 6
    def zmenit7(self):
        self.hodnota = 7
    def zmenit8(self):
        self.hodnota = 8
    def zmenit9(self):
        self.hodnota = 9
    def Hod(self):
        return str(self.hodnota)
    def Smazat(self):
        self.hodnota = ""

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
