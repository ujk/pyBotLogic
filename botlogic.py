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
from level2_ui import *


play = False
liste = []
listeIndex = 0
sonPos = 0
brakeSound = pyglet.resource.media("brake.wav", streaming=False)
driveSound = pyglet.resource.media("drive.wav", streaming=False)
crashSound = pyglet.resource.media("crash.wav", streaming=False)
applauseSound = pyglet.resource.media("applause.wav", streaming=False)


def startLevel1(object,pos):
	global dialog, carStartX, carStartY
	
	dialog = QtWidgets.QDialog()
	dialog.ui = Ui_level1Dialog()
	dialog.ui.setupUi(dialog)
	dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
	for i in range(4):
		dialog.ui.map.setRowHeight(i,40)
	for i in range(8):
		dialog.ui.map.setColumnWidth(i,40)
	carStartX = dialog.ui.map.x()
	carStartY = dialog.ui.map.y()
	dialog.ui.carButton.move(carStartX, carStartY)
	dialog.ui.homeButton.move(dialog.ui.map.x() + 7*40, dialog.ui.map.y() + 3*40)
	fileName = dialog.windowTitle() + '.sav'
	if os.path.isfile(fileName):
		f = open(fileName, "r")
		dialog.ui.prgText.setPlainText(f.read())
		f.close()
	dialog.exec_()


def startLevel2(object,pos):
	global dialog, carStartX, carStartY
	
	dialog = QtWidgets.QDialog()
	dialog.ui = Ui_level2Dialog()
	dialog.ui.setupUi(dialog)
	dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
	for i in range(4):
		dialog.ui.map.setRowHeight(i,40)
	for i in range(8):
		dialog.ui.map.setColumnWidth(i,40)
	carStartX = dialog.ui.map.x()
	carStartY = dialog.ui.map.y()
	dialog.ui.carButton.move(carStartX, carStartY)
	dialog.ui.homeButton.move(dialog.ui.map.x() + 6*40, dialog.ui.map.y() + 2*40)
	fileName = dialog.windowTitle() + '.sav'
	if os.path.isfile(fileName):
		f = open(fileName, "r")
		dialog.ui.prgText.setPlainText(f.read())
		f.close()
	dialog.exec_()


def startLevel3(object,pos):
	from level3_ui import Ui_level3Dialog
	global dialog, carStartX, carStartY
	
	dialog = QtWidgets.QDialog()
	dialog.ui = Ui_level3Dialog()
	dialog.ui.setupUi(dialog)
	dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
	for i in range(4):
		dialog.ui.map.setRowHeight(i,40)
	for i in range(8):
		dialog.ui.map.setColumnWidth(i,40)
	carStartX = dialog.ui.map.x()
	carStartY = dialog.ui.map.y()
	dialog.ui.carButton.move(carStartX, carStartY)
	dialog.ui.homeButton.move(dialog.ui.map.x() + 7*40, dialog.ui.map.y() + 1*40)
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


def sola(x = 1):
	global liste
	
	for i in range(x):
		liste.append(3)


def yukarı(x = 1):
	global liste
	
	for i in range(x):
		liste.append(4)


def timer_func():
	global dialog, xex, yex, adım, movr, movd, adımHedef
	global brakeSound, driveSound, crashSound, applauseSound
	global listeIndex, play, sonPos
	global carIcon, carDownIcon, carLeftIcon, carUpIcon
	
	duvarBump = False
	if play and (listeIndex < len(liste)):
		car = dialog.ui.carButton
		xPos = int((car.x() - dialog.ui.map.x()) / 40)
		yPos = int((car.y() - dialog.ui.map.y()) / 40)
		if liste[listeIndex] == 1:			#sağa
			car.move(car.x() + 4, car.y())
			car.setIcon(carIcon)
			try:
				if dialog.ui.map.item(yPos,xPos + 1).background().style() == 14:
					duvarBump = True
			except:
				duvarBump = False
			if car.x() >= (xex + 40):
				xex = car.x()
				sonPos = liste[listeIndex]
				listeIndex += 1
				if (listeIndex < len(liste)) and liste[listeIndex] == sonPos:
					driveSound.play()
				else:
					brakeSound.play()
					
		elif liste[listeIndex] == 2:			#aşağı
			car.move(car.x(), car.y() + 4)
			car.setIcon(carDownIcon)
			try:
				if dialog.ui.map.item(yPos + 1,xPos).background().style() == 14:
					duvarBump = True
			except:
				duvarBump = False
			if car.y() >= (yex + 40):
				yex = car.y()
				sonPos = liste[listeIndex]
				listeIndex += 1
				if (listeIndex < len(liste)) and liste[listeIndex] == sonPos:
					driveSound.play()
				else:
					brakeSound.play()
	
		elif liste[listeIndex] == 3:			#sola
			car.move(car.x() - 4, car.y())
			car.setIcon(carLeftIcon)
			try:
				if dialog.ui.map.item(yPos,xPos).background().style() == 14:
					duvarBump = True
			except:
				duvarBump = False
			if car.x() <= (xex - 40):
				xex = car.x()
				sonPos = liste[listeIndex]
				listeIndex += 1
				if (listeIndex < len(liste)) and liste[listeIndex] == sonPos:
					driveSound.play()
				else:
					brakeSound.play()
					
		elif liste[listeIndex] == 4:			#yukarı
			car.move(car.x(), car.y() - 4)
			car.setIcon(carUpIcon)
			try:
				if dialog.ui.map.item(yPos,xPos).background().style() == 14:
					duvarBump = True
			except:
				duvarBump = False
			if car.y() <= (yex - 40):
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
					
				
	if play and ((dialog.ui.carButton.x() > dialog.ui.map.x() + dialog.ui.map.width() - 35) or 
			(dialog.ui.carButton.y() > dialog.ui.map.y() + dialog.ui.map.height() - 35) or 
			(dialog.ui.carButton.x() < dialog.ui.map.x() - 30) or 
			(dialog.ui.carButton.y() < dialog.ui.map.y() - 30) or duvarBump):
		crashSound.play()
		play = False
		duvarBump = False
		QtWidgets.QMessageBox.critical(dialog,"E BE SALAK!!","Duvara Çarptın Geri Zekalı")
					
				
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



def resetClicked(object,pos):
	global dialog, carStartX, carStartY
	
	dialog.ui.carButton.move(carStartX, carStartY)
	dialog.ui.carButton.setIcon(carIcon)



QtWidgets.QDialog.playClicked = playClicked
QtWidgets.QDialog.saveClicked = saveClicked
QtWidgets.QDialog.resetClicked = resetClicked
QtWidgets.QWidget.startLevel1 = startLevel1
QtWidgets.QWidget.startLevel2 = startLevel2
QtWidgets.QWidget.startLevel3 = startLevel3

import sys
app = QtWidgets.QApplication(sys.argv)

dialog = QtWidgets.QDialog()
dialog.ui = Ui_level2Dialog()
dialog.ui.setupUi(dialog)
dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
carIcon = QtGui.QIcon("car.png")
carDownIcon = QtGui.QIcon("car_down.png")
carLeftIcon = QtGui.QIcon("car_left.png")
carUpIcon = QtGui.QIcon("car_up.png")

Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
timer = QtCore.QTimer()	
timer.timeout.connect(timer_func)
timer.start(100)
sys.exit(app.exec_())

