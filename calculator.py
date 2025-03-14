from PyQt5 import QtCore, QtGui, QtWidgets
import math
import re
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 570)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("calc_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(4, 5, 441, 111))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.percentbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.math_calc("percentage"))
        self.percentbutton.setGeometry(QtCore.QRect(10, 130, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.percentbutton.setFont(font)
        self.percentbutton.setObjectName("percentbutton")
        self.CEbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("mod"))
        self.CEbutton.setGeometry(QtCore.QRect(100, 130, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.CEbutton.setFont(font)
        self.CEbutton.setObjectName("CEbutton")
        self.Cbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("C"))
        self.Cbutton.setGeometry(QtCore.QRect(190, 130, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Cbutton.setFont(font)
        self.Cbutton.setObjectName("Cbutton")
        self.undobutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.remove_it())
        self.undobutton.setGeometry(QtCore.QRect(280, 130, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.undobutton.setFont(font)
        self.undobutton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pngegg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undobutton.setIcon(icon1)
        self.undobutton.setIconSize(QtCore.QSize(32, 32))
        self.undobutton.setObjectName("undobutton")
        self.divisonbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("/"))
        self.divisonbutton.setGeometry(QtCore.QRect(370, 130, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.divisonbutton.setFont(font)
        self.divisonbutton.setObjectName("divisonbutton")
        self.multipl_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("*"))
        self.multipl_button.setGeometry(QtCore.QRect(370, 210, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.multipl_button.setFont(font)
        self.multipl_button.setObjectName("multipl_button")
        self.minusbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("-"))
        self.minusbutton.setGeometry(QtCore.QRect(370, 290, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.minusbutton.setFont(font)
        self.minusbutton.setObjectName("minusbutton")
        self.plusbutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("+"))
        self.plusbutton.setGeometry(QtCore.QRect(370, 370, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plusbutton.setFont(font)
        self.plusbutton.setObjectName("plusbutton")
        self.equal_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.math_calc())
        self.equal_button.setGeometry(QtCore.QRect(370, 450, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.equal_button.setFont(font)
        self.equal_button.setObjectName("equal_button")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("7"))
        self.Button_7.setGeometry(QtCore.QRect(100, 210, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Button_7.setFont(font)
        self.Button_7.setObjectName("Button_7")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("8"))
        self.Button_8.setGeometry(QtCore.QRect(190, 210, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Button_8.setFont(font)
        self.Button_8.setObjectName("Button_8")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("9"))
        self.Button_9.setGeometry(QtCore.QRect(280, 210, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Button_9.setFont(font)
        self.Button_9.setObjectName("Button_9")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("4"))
        self.Button_4.setGeometry(QtCore.QRect(100, 290, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Button_4.setFont(font)
        self.Button_4.setObjectName("Button_4")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("5"))
        self.Button_5.setGeometry(QtCore.QRect(190, 290, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Button_5.setFont(font)
        self.Button_5.setObjectName("Button_5")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("6"))
        self.Button_6.setGeometry(QtCore.QRect(280, 290, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Button_6.setFont(font)
        self.Button_6.setObjectName("Button_6")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("1"))
        self.Button_1.setGeometry(QtCore.QRect(100, 370, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Button_1.setFont(font)
        self.Button_1.setObjectName("Button_1")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("2"))
        self.Button_2.setGeometry(QtCore.QRect(190, 370, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Button_2.setFont(font)
        self.Button_2.setObjectName("Button_2")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("3"))
        self.Button_3.setGeometry(QtCore.QRect(280, 370, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Button_3.setFont(font)
        self.Button_3.setObjectName("Button_3")
        self.dot_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.dot_it())
        self.dot_button.setGeometry(QtCore.QRect(280, 450, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.dot_button.setFont(font)
        self.dot_button.setObjectName("dot_button")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.press_it("0"))
        self.Button_0.setGeometry(QtCore.QRect(190, 450, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Button_0.setFont(font)
        self.Button_0.setObjectName("Button_0")
        self.plusminus_button = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.plus_minus())
        self.plusminus_button.setGeometry(QtCore.QRect(100, 450, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plusminus_button.setFont(font)
        self.plusminus_button.setObjectName("plusminus_button")
        self.squarebutton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.math_calc("square"))
        self.squarebutton.setGeometry(QtCore.QRect(10, 210, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.squarebutton.setFont(font)
        self.squarebutton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("xsquare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.squarebutton.setIcon(icon2)
        self.squarebutton.setIconSize(QtCore.QSize(25, 25))
        self.squarebutton.setObjectName("squarebutton")
        self.square_root_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.math_calc("sqrt"))
        self.square_root_button.setGeometry(QtCore.QRect(10, 290, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.square_root_button.setFont(font)
        self.square_root_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("squareroot1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.square_root_button.setIcon(icon3)
        self.square_root_button.setIconSize(QtCore.QSize(32, 32))
        self.square_root_button.setObjectName("square_root_button")
        self.factorial_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.math_calc("factorial"))
        self.factorial_button.setGeometry(QtCore.QRect(10, 370, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.factorial_button.setFont(font)
        self.factorial_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("factorial.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.factorial_button.setIcon(icon4)
        self.factorial_button.setIconSize(QtCore.QSize(20, 20))
        self.factorial_button.setObjectName("factorial_button")
        self.one_overbutton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.math_calc("inverse"))
        self.one_overbutton.setGeometry(QtCore.QRect(10, 450, 75, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.one_overbutton.setFont(font)
        self.one_overbutton.setObjectName("one_overbutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def remove_it(self):
        #ekranda o an ne varsa onu göster
        ekran = self.outputLabel.text()
        if ekran == "0":         #0 ise değiştirme
            return
        # son itemi almayarak kaldıralım
        ekran = ekran[:-1]
        self.outputLabel.setText(ekran if ekran else "0")

    def math_calc(self, operation=None):
        # ekranda o an ne varsa onu göster
        ekran = self.outputLabel.text().strip()
        try:
            if operation == "square":
                sonuc = float(ekran) ** 2
            elif operation == "sqrt":
                sonuc = math.sqrt(float(ekran))
            elif operation == "factorial":
                sonuc = math.factorial(int(ekran))
            elif operation == "inverse":
                sonuc = 1 / float(ekran)
            elif operation == "percentage":
                sonuc = int(ekran) / 100
            else:
                ekran = ekran.replace("x²", "**2")
                ekran = ekran.replace("√", "math.sqrt")
                ekran = ekran.replace("!", "math.factorial")
                ekran = ekran.replace("÷", "/")
                ekran = ekran.replace("×", "*")
                sonuc = eval(ekran, {"math": math, "__builtins__": None})

            self.outputLabel.setText(str(sonuc))
        except Exception:
            self.outputLabel.setText("Error occured.")

    def plus_minus(self):
        #ekranda o an ne varsa onu göster
        ekran = self.outputLabel.text()
        if "-" in ekran:
            self.outputLabel.setText(ekran.replace("-",""))
        else:
            if ekran == "0":    #Ekrandaki değer 0 ise hiç değiştirme
                return
            self.outputLabel.setText(f"-{ekran}")


    def dot_it(self):
        # ekranda o an ne varsa onu göster
        ekran = self.outputLabel.text()
        if not ekran:      #ekran boşsa nokta koyma
            return
        parts = re.split(r'([+\-*/])', ekran)  # Operatörleri ayırdık

        last_part = parts[-1]  # Son sayıyı alalım

        # Eğer son sayı kısımda nokta yoksa ekleyelim
        if "." not in last_part:
            self.outputLabel.setText(ekran + ".")

    def press_it(self, pressed):
        if pressed == "C":
            self.outputLabel.setText("0")
        else:
            #for deleting 0 from outputlabel
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            self.outputLabel.setText(f"{self.outputLabel.text()}{pressed}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percentbutton.setText(_translate("MainWindow", "%"))
        self.CEbutton.setText(_translate("MainWindow", "CE"))
        self.Cbutton.setText(_translate("MainWindow", "C"))
        self.divisonbutton.setText(_translate("MainWindow", "/"))
        self.multipl_button.setText(_translate("MainWindow", "x"))
        self.minusbutton.setText(_translate("MainWindow", "-"))
        self.plusbutton.setText(_translate("MainWindow", "+"))
        self.equal_button.setText(_translate("MainWindow", "="))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.dot_button.setText(_translate("MainWindow", "."))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.plusminus_button.setText(_translate("MainWindow", "+/-"))
        self.one_overbutton.setText(_translate("MainWindow", "1/x"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
