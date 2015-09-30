# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'level1.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_level1Dialog(object):
    def setupUi(self, level1Dialog):
        level1Dialog.setObjectName("level1Dialog")
        level1Dialog.resize(526, 300)
        self.map = QtWidgets.QTableWidget(level1Dialog)
        self.map.setGeometry(QtCore.QRect(10, 10, 320, 160))
        self.map.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.map.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.map.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.map.setRowCount(4)
        self.map.setColumnCount(8)
        self.map.setObjectName("map")
        self.map.horizontalHeader().setVisible(False)
        self.map.verticalHeader().setVisible(False)
        self.textEdit = QtWidgets.QTextEdit(level1Dialog)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(10, 180, 321, 111))
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")
        self.carButton = QtWidgets.QPushButton(level1Dialog)
        self.carButton.setEnabled(False)
        self.carButton.setGeometry(QtCore.QRect(130, 40, 40, 40))
        self.carButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("car.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.carButton.setIcon(icon)
        self.carButton.setIconSize(QtCore.QSize(36, 36))
        self.carButton.setCheckable(False)
        self.carButton.setFlat(True)
        self.carButton.setObjectName("carButton")
        self.homeButton = QtWidgets.QPushButton(level1Dialog)
        self.homeButton.setEnabled(False)
        self.homeButton.setGeometry(QtCore.QRect(150, 100, 40, 40))
        self.homeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon1)
        self.homeButton.setIconSize(QtCore.QSize(36, 36))
        self.homeButton.setCheckable(False)
        self.homeButton.setFlat(True)
        self.homeButton.setObjectName("homeButton")
        self.prgText = QtWidgets.QTextEdit(level1Dialog)
        self.prgText.setGeometry(QtCore.QRect(340, 60, 171, 191))
        self.prgText.setObjectName("prgText")
        self.pushButton = QtWidgets.QPushButton(level1Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 260, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(level1Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 260, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(level1Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 260, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.powerLcd = QtWidgets.QLCDNumber(level1Dialog)
        self.powerLcd.setGeometry(QtCore.QRect(340, 10, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.powerLcd.setPalette(palette)
        self.powerLcd.setAutoFillBackground(True)
        self.powerLcd.setDigitCount(2)
        self.powerLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.powerLcd.setProperty("intValue", 99)
        self.powerLcd.setObjectName("powerLcd")

        self.retranslateUi(level1Dialog)
        self.pushButton.clicked.connect(level1Dialog.playClicked)
        self.pushButton_2.clicked.connect(level1Dialog.saveClicked)
        self.pushButton_3.clicked.connect(level1Dialog.resetClicked)
        QtCore.QMetaObject.connectSlotsByName(level1Dialog)

    def retranslateUi(self, level1Dialog):
        _translate = QtCore.QCoreApplication.translate
        level1Dialog.setWindowTitle(_translate("level1Dialog", "LEVEL 1"))
        self.textEdit.setHtml(_translate("level1Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Seviye 1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Bu oyunda amaç program yazarak aracı eve ulaştırmak. Puanlama ile ilgilenmiyoruz.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">İlk bölümde kullanabileceğiniz komutlar:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">sağa(x):</span><span style=\" font-size:8pt;\"> bu komutu kullanırsanız sağa doğru x adım atarsınız eğer x değeri girmezseniz 1 adım atılacaktır. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">sola(x): </span><span style=\" font-size:8pt;\">sola doğru x adım atmak için kullanılır.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">yukarı(x):</span><span style=\" font-size:8pt;\"> yukarı doğru x adım atmak için kullanılır.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">aşağı(x):</span><span style=\" font-size:8pt;\"> aşağı doğru x adım atmak için kullanılır.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">play </span><span style=\" font-size:8pt;\">tuşu ile yazdığınız kodu deneyebilirsiniz. Kolay gelsin..</span></p></body></html>"))
        self.prgText.setPlaceholderText(_translate("level1Dialog", "Kodunuzu buraya yazın.."))
        self.pushButton.setText(_translate("level1Dialog", "PLAY"))
        self.pushButton_2.setText(_translate("level1Dialog", "SAVE"))
        self.pushButton_3.setText(_translate("level1Dialog", "RESET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    level1Dialog = QtWidgets.QDialog()
    ui = Ui_level1Dialog()
    ui.setupUi(level1Dialog)
    level1Dialog.show()
    sys.exit(app.exec_())

