# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alexaUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_alexaUI(object):
    def setupUi(self, alexaUI):

        alexaUI.setObjectName("alexaUI")
        alexaUI.resize(908, 629)

        self.label = QtWidgets.QLabel(alexaUI)
        self.label.setGeometry(QtCore.QRect(-10, 0, 921, 631))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("uicomponents\\background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(alexaUI)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 351, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("uicomponents\\initiating image.gif"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(alexaUI)
        self.label_3.setGeometry(QtCore.QRect(0, 100, 251, 131))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("uicomponents\\rectangle 2 copy.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(alexaUI)
        self.label_4.setGeometry(QtCore.QRect(0, 220, 251, 131))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("uicomponents\\rectangle 2 copy.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(alexaUI)
        self.label_5.setGeometry(QtCore.QRect(0, 350, 251, 131))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("uicomponents\\rectangle 2 copy.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(alexaUI)
        self.label_6.setGeometry(QtCore.QRect(0, 490, 251, 131))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("uicomponents\\rectangle 2 copy.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.hi = QtWidgets.QLabel(alexaUI)
        self.hi.setGeometry(QtCore.QRect(430, -40, 270, 220))
        self.hi.setText("")
        self.hi.setPixmap(QtGui.QPixmap("uicomponents\\hi.gif"))
        self.hi.setScaledContents(True)
        self.hi.setObjectName("hi")

        self.mainlabel = QtWidgets.QLabel(alexaUI)
        self.mainlabel.setGeometry(QtCore.QRect(280, 140, 351, 311))
        self.mainlabel.setText("")
        self.mainlabel.setPixmap(QtGui.QPixmap("uicomponents\\Circle2.gif"))
        self.mainlabel.setScaledContents(True)
        self.mainlabel.setObjectName("uicomponents\\mainlabel")

        self.tenor = QtWidgets.QLabel(alexaUI)
        self.tenor.setGeometry(QtCore.QRect(710, 0, 181, 161))
        self.tenor.setText("")
        self.tenor.setPixmap(QtGui.QPixmap("uicomponents\\tenor.gif"))
        self.tenor.setScaledContents(True)
        self.tenor.setObjectName("tenor")

        self.newLabel = QtWidgets.QLabel(alexaUI)
        self.newLabel.setGeometry(QtCore.QRect(680, 220, 201, 171))
        self.newLabel.setText("")
        self.newLabel.setPixmap(QtGui.QPixmap("uicomponents\\rectangle copy.jpg"))
        self.newLabel.setScaledContents(True)
        self.newLabel.setObjectName("newLabel")
        self.newLabel_2 = QtWidgets.QLabel(alexaUI)
        self.newLabel_2.setGeometry(QtCore.QRect(680, 390, 201, 171))
        self.newLabel_2.setText("")
        self.newLabel_2.setPixmap(QtGui.QPixmap("uicomponents\\rectangle copy.jpg"))
        self.newLabel_2.setScaledContents(True)
        self.newLabel_2.setObjectName("newLabel_2")
        self.textBrowser = QtWidgets.QTextBrowser(alexaUI)
        self.textBrowser.setGeometry(QtCore.QRect(50, 155, 160, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:16px")
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_1 = QtWidgets.QTextBrowser(alexaUI)
        self.textBrowser_1.setGeometry(QtCore.QRect(50, 274, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_1.setFont(font)
        self.textBrowser_1.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:16px")
        self.textBrowser_1.setObjectName("textBrowser_1")

        self.textBrowser_2 = QtWidgets.QTextBrowser(alexaUI)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 407, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:16px")
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.textBrowser_3 = QtWidgets.QTextBrowser(alexaUI)
        self.textBrowser_3.setGeometry(QtCore.QRect(30, 545, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(65)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:16px")
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.textBrowser_4 = QtWidgets.QTextBrowser(alexaUI)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(65)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setGeometry(QtCore.QRect(706, 275, 164, 65))
        self.textBrowser_4.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:16px")
        self.textBrowser_4.setObjectName("textBrowser_4")

        self.textBrowser_41 = QtWidgets.QTextBrowser(alexaUI)
        self.textBrowser_41.setGeometry(QtCore.QRect(695, 230, 184, 65))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(68)
        self.textBrowser_41.setFont(font)
        self.textBrowser_41.setText("Today's Inspiration")#The present inspiration
        self.textBrowser_41.setStyleSheet("background:transparent;\n"
                                         "border-radius:none;\n"
                                         "color:white;\n"
                                         "font-size:16px")

        self.textBrowser_5 = QtWidgets.QTextBrowser(alexaUI)
        self.textBrowser_5.setGeometry(QtCore.QRect(710, 455, 164, 64))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(65)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:16px")
        self.textBrowser_5.setObjectName("textBrowser_5")

        self.textBrowser_51 = QtWidgets.QTextBrowser(alexaUI)
        self.textBrowser_51.setGeometry(QtCore.QRect(705, 405, 190, 65))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(68)
        self.textBrowser_51.setFont(font)
        self.textBrowser_51.setText("Present Location")  # The present inspiration
        self.textBrowser_51.setStyleSheet("background:transparent;\n"
                                          "border-radius:none;\n"
                                          "color:white;\n"
                                          "font-size:16px")

        self.textBrowser_6 = QtWidgets.QTextBrowser(alexaUI)
        self.textBrowser_6.setGeometry(QtCore.QRect(270, 480, 391, 141))
        self.textBrowser_6.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:16px")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.retranslateUi(alexaUI)
        QtCore.QMetaObject.connectSlotsByName(alexaUI)

    def retranslateUi(self, alexaUI):
        _translate = QtCore.QCoreApplication.translate
        alexaUI.setWindowTitle(_translate("alexaUI", "Alexa"))
        alexaUI.setWindowIcon(QtGui.QIcon("logo.ico"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    alexaUI = QtWidgets.QWidget()

    ui = Ui_alexaUI()
    ui.setupUi(alexaUI)
    alexaUI.show()
    sys.exit(app.exec_())
