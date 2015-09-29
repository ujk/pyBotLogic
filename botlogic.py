# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyglet, os.path
from main_ui import *
from level1_ui import *


play = False
liste = []
listeIndex = 0
sonPos = 0
brakeSound = pyglet.resource.media("brake.wav", streaming=False)
driveSound = pyglet.resource.media("drive.wav", streaming=False)
crashSound = pyglet.resource.media("crash.wav", streaming=False)
applauseSound = pyglet.resource.media("applause.wav", streaming=False)


def startLevel1(object,pos):
	global dialog
	dialog = QtWidgets.QDialog()
	dialog.ui = Ui_level1Dialog()
	dialog.ui.setupUi(dialog)
	dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
	for i in range(4):
		dialog.ui.map.setRowHeight(i,40)
	for i in range(8):
		dialog.ui.map.setColumnWidth(i,40)
	dialog.ui.carButton.move(dialog.ui.map.x(), dialog.ui.map.y())
	dialog.ui.homeButton.move(dialog.ui.map.x() + 7*40, dialog.ui.map.y() + 3*40)
	fileName = dialog.windowTitle() + '.sav'
	if os.path.isfile(fileName):
		f = open(fileName, "r")
		dialog.ui.prgText.setPlainText(f.read())
		f.close()
	dialog.exec_()


def sağa(x = 1):
	global liste
	
	for i in range(x):
		liste.append(1)


def aşağı(x = 1):
	global liste
	
	for i in range(x):
		liste.append(2)


def timer_func():
	global dialog, xex, yex, adım, movr, movd, adımHedef
	global brakeSound, driveSound, crashSound, applauseSound
	global listeIndex, play, sonPos
	
	if play and (listeIndex < len(liste)):
		if liste[listeIndex] == 1:			#sağa
			car = dialog.ui.carButton
			car.move(car.x() + 4, car.y())
			if car.x() >= (xex + 40):
				xex = car.x()
				sonPos = liste[listeIndex]
				listeIndex += 1
				if (listeIndex < len(liste)) and liste[listeIndex] == sonPos:
					driveSound.play()
				else:
					brakeSound.play()
					
		elif liste[listeIndex] == 2:			#aşağı
			car = dialog.ui.carButton
			car.move(car.x(), car.y() + 4)
			if car.y() >= (yex + 40):
				yex = car.y()
				sonPos = liste[listeIndex]
				listeIndex += 1
				if (listeIndex < len(liste)) and liste[listeIndex] == sonPos:
					driveSound.play()
				else:
					brakeSound.play()
	
	if play and (dialog.ui.carButton.x() == dialog.ui.homeButton.x()) and (dialog.ui.carButton.y() == dialog.ui.homeButton.y()):
		applauseSound.play()
		play = False
					
				
	if play and (dialog.ui.carButton.x() > dialog.ui.map.x() + dialog.ui.map.width() - 35):
		crashSound.play()
		play = False
					
				
	if listeIndex >= len(liste):
		play = False
				
				
def playClicked(object,pos):
	global liste, xex, yex, dialog, play, sonPos, listeIndex
	
	car = dialog.ui.carButton
	xex = car.x()
	yex = car.y()
	liste = []
	try:
		exec(dialog.ui.prgText.toPlainText())
	except:
		QtWidgets.QMessageBox.critical(dialog,"DİKKAT","Yazılan programda hata var")
	listeIndex = 0
	if len(liste) > 0:
		sonPos = liste[0]
		play = True
	


def saveClicked(object,pos):
	global dialog
	
	fileName = dialog.windowTitle() + ".sav"
	f = open(fileName, "w")
	f.write(dialog.ui.prgText.toPlainText())
	f.close()



QtWidgets.QDialog.playClicked = playClicked	
QtWidgets.QDialog.saveClicked = saveClicked	
QtWidgets.QWidget.startLevel1 = startLevel1	

import sys
app = QtWidgets.QApplication(sys.argv)

dialog = QtWidgets.QDialog()
dialog.ui = Ui_level1Dialog()
dialog.ui.setupUi(dialog)
dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)

Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
timer = QtCore.QTimer()	
timer.timeout.connect(timer_func)
timer.start(100)
sys.exit(app.exec_())

