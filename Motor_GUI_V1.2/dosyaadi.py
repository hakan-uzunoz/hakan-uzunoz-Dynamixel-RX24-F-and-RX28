# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_txt_sayi1(object):
    def setupUi(self, txt_sayi1):
        txt_sayi1.setObjectName("txt_sayi1")
        txt_sayi1.resize(800, 600)
        txt_sayi1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        txt_sayi1.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        txt_sayi1.setWindowIcon(icon)
        txt_sayi1.setAutoFillBackground(False)
        txt_sayi1.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        txt_sayi1.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(txt_sayi1)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalSlidr = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlidr.setGeometry(QtCore.QRect(330, 360, 22, 160))
        self.verticalSlidr.setMaximum(1023)
        self.verticalSlidr.setProperty("value", 512)
        self.verticalSlidr.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlidr.setInvertedAppearance(False)
        self.verticalSlidr.setInvertedControls(False)
        self.verticalSlidr.setObjectName("verticalSlidr")
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setGeometry(QtCore.QRect(380, 360, 22, 160))
        self.verticalSlider_2.setMaximum(1023)
        self.verticalSlider_2.setProperty("value", 512)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_3.setGeometry(QtCore.QRect(430, 360, 22, 160))
        self.verticalSlider_3.setMaximum(1023)
        self.verticalSlider_3.setProperty("value", 512)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.verticalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_4.setGeometry(QtCore.QRect(480, 360, 22, 160))
        self.verticalSlider_4.setMaximum(1023)
        self.verticalSlider_4.setProperty("value", 512)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(323, 530, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(376, 530, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(425, 530, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(475, 530, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(338, 340, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(388, 340, 47, 13))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(437, 340, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(487, 340, 47, 13))
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 300, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 50, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 90, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 60, 160, 22))
        self.horizontalSlider.setMaximum(7)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 100, 64, 23))
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 390, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(30, 430, 160, 22))
        self.horizontalSlider_2.setMaximum(1023)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(50, 470, 64, 23))
        self.lcdNumber_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(40, 210, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setAutoFillBackground(False)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(30, 250, 160, 22))
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(80, 290, 64, 23))
        self.lcdNumber_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(640, 0, 160, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout.addWidget(self.label_20)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout.addWidget(self.label_18)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout.addWidget(self.label_22)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.verticalLayout.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.verticalLayout.addWidget(self.label_25)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.verticalLayout.addWidget(self.label_23)
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_26.setObjectName("label_26")
        self.verticalLayout.addWidget(self.label_26)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(620, 0, 20, 551))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(0, 530, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(80, 460, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(320, 130, 160, 22))
        self.horizontalSlider_4.setMaximum(1023)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(360, 160, 64, 23))
        self.lcdNumber_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(310, 190, 160, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_29 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_2.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_2.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_2.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_2.addWidget(self.label_32)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(7, 160, 191, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(20, 350, 191, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(20, 540, 191, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(210, 0, 20, 551))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(227, 180, 391, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(230, 300, 391, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        txt_sayi1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(txt_sayi1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        txt_sayi1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(txt_sayi1)
        self.statusbar.setObjectName("statusbar")
        txt_sayi1.setStatusBar(self.statusbar)

        self.retranslateUi(txt_sayi1)
        QtCore.QMetaObject.connectSlotsByName(txt_sayi1)

    def retranslateUi(self, txt_sayi1):
        _translate = QtCore.QCoreApplication.translate
        txt_sayi1.setWindowTitle(_translate("txt_sayi1", "EED4306 Robotics Dynamixel Control "))
        self.label_3.setText(_translate("txt_sayi1", "motor 1"))
        self.label_4.setText(_translate("txt_sayi1", "motor 2"))
        self.label_5.setText(_translate("txt_sayi1", "motor 3"))
        self.label_6.setText(_translate("txt_sayi1", "motor 4"))
        self.label_7.setText(_translate("txt_sayi1", "0"))
        self.label_8.setText(_translate("txt_sayi1", "0"))
        self.label_9.setText(_translate("txt_sayi1", "0"))
        self.label_10.setText(_translate("txt_sayi1", "0"))
        self.label.setText(_translate("txt_sayi1", "Motor Position Control"))
        self.pushButton.setText(_translate("txt_sayi1", "Torque Disable "))
        self.label_2.setText(_translate("txt_sayi1", "Motor Torque Control"))
        self.pushButton_2.setText(_translate("txt_sayi1", "Torque Enable "))
        self.label_11.setText(_translate("txt_sayi1", "Motor Slope Control"))
        self.label_12.setText(_translate("txt_sayi1", "Motor Speed Control"))
        self.label_13.setText(_translate("txt_sayi1", "Motor Margin Control"))
        self.label_16.setText(_translate("txt_sayi1", "Motor Info"))
        self.label_15.setText(_translate("txt_sayi1", "Motor 1  Model:"))
        self.label_17.setText(_translate("txt_sayi1", "Motor 2  Model:"))
        self.label_19.setText(_translate("txt_sayi1", "Motor 3  Model:"))
        self.label_20.setText(_translate("txt_sayi1", "Motor 4  Model:"))
        self.label_18.setText(_translate("txt_sayi1", "Motor 1 Temp:"))
        self.label_21.setText(_translate("txt_sayi1", "Motor 2 Temp:"))
        self.label_22.setText(_translate("txt_sayi1", "Motor 3 Temp:"))
        self.label_14.setText(_translate("txt_sayi1", "Motor 4 Temp:"))
        self.label_24.setText(_translate("txt_sayi1", "Motor 1 Volt:"))
        self.label_25.setText(_translate("txt_sayi1", "Motor 2 Volt:"))
        self.label_23.setText(_translate("txt_sayi1", "Motor 3 Volt:"))
        self.label_26.setText(_translate("txt_sayi1", "Motor 4 Volt:"))
        self.pushButton_3.setText(_translate("txt_sayi1", "Refresh"))
        self.label_27.setText(_translate("txt_sayi1", "DEU-EEE Hakan Uzunoz "))
        self.label_28.setText(_translate("txt_sayi1", "Rev/Min"))
        self.label_29.setText(_translate("txt_sayi1", "Errors"))
        self.label_30.setText(_translate("txt_sayi1", "Angel Limit: No Error"))
        self.label_31.setText(_translate("txt_sayi1", "Range: No Error"))
        self.label_32.setText(_translate("txt_sayi1", "Overload: No Error"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    txt_sayi1 = QtWidgets.QMainWindow()
    ui = Ui_txt_sayi1()
    ui.setupUi(txt_sayi1)
    txt_sayi1.show()
    sys.exit(app.exec_())

