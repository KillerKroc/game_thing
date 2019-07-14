import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtGui import *
import os


class create(QWidget):
    def __init__(self):
        super(create, self).__init__()
        loadUi("create.ui", self)
        #sets up checking variables to see if stat increases or decreases
        self.intv = self.int_2.value()
        self.athv = self.ath.value()
        self.chav = self.cha.value()
        self.attv = self.att.value()
        self.dexv = self.dex.value()
        #Set up Choiceboxes
        self.Race.addItems(["Caucasian", "Black", "Indian", "Arab", "Japanese",
                       "Chinese", "Mexican", "Latino", "Slavic", "Jewish"])
        self.Gender.addItems(["Male", "Female"])
        self.Co.addItems(["United States", "Canada", "China", "India", "Russia",
                     "France", "Mexico", "North Korea", "Nigeria",
                     "Saudi Arabia", "Syria"])
        self.Religion.addItems(["Atheist", "Christian", "Catholic", "Muslim",
                           "Hindu", "Bhuddist"])
        #Connect Debuffs and Done
        self.done.clicked.connect(self.done_clicked)
        self.anxiety.clicked.connect(self.anxiety_clicked)
        self.depression.clicked.connect(self.depression_clicked)
        self.schizophrenia.clicked.connect(self.schizophrenia_clicked)
        self.adhd.clicked.connect(self.adhd_clicked)
        self.uwalk.clicked.connect(self.uwalk_clicked)
        self.cancer.clicked.connect(self.cancer_clicked)
        self.pinjury.clicked.connect(self.pinjury_clicked)
        #connects stats
        self.int_2.valueChanged.connect(self.int_clicked)
        self.ath.valueChanged.connect(self.ath_clicked)
        self.cha.valueChanged.connect(self.cha_clicked)
        self.att.valueChanged.connect(self.att_clicked)
        self.dex.valueChanged.connect(self.dex_clicked)
        #set default point amount
        self.pts.setValue(15)
    #Change #ofpoints when disability is checked
    @pyqtSlot()
    def anxiety_clicked(self):
        if self.anxiety.isChecked():
            self.pts.setValue(self.pts.value() + 3)
        else:
            self.pts.setValue(self.pts.value() - 3)
    @pyqtSlot()
    def depression_clicked(self):
        if self.depression.isChecked():
            self.pts.setValue(self.pts.value() + 4)
        else:
            self.pts.setValue(self.pts.value() - 4)
    @pyqtSlot()
    def schizophrenia_clicked(self):
        if self.schizophrenia.isChecked():
            self.pts.setValue(self.pts.value() + 5)
        else:
            self.pts.setValue(self.pts.value() - 5)
    @pyqtSlot()
    def adhd_clicked(self):
        if self.adhd.isChecked():
            self.pts.setValue(self.pts.value() + 2)
        else:
            self.pts.setValue(self.pts.value() - 2)
    @pyqtSlot()
    def uwalk_clicked(self):
        if self.uwalk.isChecked():
            self.pts.setValue(self.pts.value() + 6)
        else:
            self.pts.setValue(self.pts.value() - 6)
    @pyqtSlot()
    def cancer_clicked(self):
        if self.cancer.isChecked():
            self.pts.setValue(self.pts.value() + 5)
        else:
            self.pts.setValue(self.pts.value() - 5)
    @pyqtSlot()
    def pinjury_clicked(self):
        if self.pinjury.isChecked():
            self.pts.setValue(self.pts.value() + 3)
        else:
            self.pts.setValue(self.pts.value() - 3)

    #ensures there are enough points to change values
    @pyqtSlot()
    def int_clicked(self):
        if self.int_2.value() > self.intv:
            if self.pts.value == 0:
                self.int_2.setValue(self.int.value() - 1)
            else:
                self.pts.setValue(self.pts.value() - 1)
                self.intv = self.int_2.value()
        elif self.int_2.value() < self.intv:
            self.pts.setValue(self.pts.value() + 1)
            self.intv = self.int_2.value()
    @pyqtSlot()
    def ath_clicked(self):
        if self.ath.value() > self.athv:
            if self.pts.value == 0:
                self.ath.setValue(self.ath.value() - 1)
            else:
                self.pts.setValue(self.pts.value() - 1)
                self.athv = self.ath.value()
        elif self.cha.value() < self.chav:
            self.pts.setValue(self.cha.value() + 1)
            self.chav = self.cha.value()
    @pyqtSlot()
    def cha_clicked(self):
        if self.cha.value() > self.chav:
            if self.pts.value() == 0:
                self.cha.setValue(self.cha.value() - 1)
            else:
                self.pts.setValue(self.pts.value() - 1)
                self.chav = self.cha.value()
        elif self.cha.value() < self.chav:
            self.pts.setValue(self.pts.value() + 1)
            self.chav = self.cha.value()
    @pyqtSlot()
    def att_clicked(self):
        if self.att.value() > self.attv:
            if self.pts.value() == 0:
                self.att.setValue(self.att.value - 1)
            else:
                self.pts.setValue(self.pts.value() - 1)
                self.attv = self.att.value()
        elif self.att.value() < self.attv:
            self.pts.setValue(self.pts.value() + 1)
            self.attv = self.att.value()
    @pyqtSlot()
    def dex_clicked(self):
        if self.dex.value() > self.dexv:
            if self.pts.value() == 0:
                self.dex.setValue(self.dex.value() - 1)
            else:
                self.pts.setValue(self.pts.value() - 1)
                self.dexv = self.dex.value()
        elif self.dex.value() < self.dexv:
            self.pts.setValue(self.pts.value() + 1)
            self.dexv = self.dex.value()
    #moves to next window/saves data when next_clicked is clicked
    @pyqtSlot()
    def done_clicked(self):
        if os.path.exists("savedata.txt"):
            os.remove("savedata.txt")
        savedata = open("savedata.txt", "w+")
        savedata.write(str(self.int_2.value()) + "/" + str(self.ath.value()) + "/" + str(self.cha.value()) + "/" + str(self.att.value()) + "/" + str(self.dex.value()) + "/")
        savedata.write(self.Race.currentText() + "/" + self.Gender.currentText() + "/" + self.Co.currentText() + "/"+ self.Religion.currentText() + "/")
        savedata.write(self.F_Name.text() + "/" + self.L_Name.text() + "/")

        savedata.close()
        self.hide()
        main.show()

#main game window
class main(QWidget):
    def __init__(self):
        super(main, self).__init__()
        loadUi("main.ui", self)
        self.stats.clicked.connect(self.stats_clicked)

    @pyqtSlot()
    def stats_clicked(self):
        self.hide()

app = QApplication(sys.argv)

main = main()
widget = create()
main.hide()
widget.show()
sys.exit(app.exec_())
