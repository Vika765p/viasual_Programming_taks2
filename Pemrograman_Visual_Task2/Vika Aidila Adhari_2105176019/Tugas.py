# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_input.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1030, 599)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -40, 1031, 761))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 201, 51))
        self.label_2.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(245, 163, 188);")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(450, -70, 581, 831))
        self.label_5.setStyleSheet("image: url(:/newPrefix/download (32).jpg);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 240, 341, 251))
        self.label_4.setStyleSheet("background-color: rgb(245, 163, 188);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 260, 321, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setStyleSheet("color: rgb(170, 170, 127)")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setStyleSheet("color: rgb(170, 170, 127)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setStyleSheet("color: rgb(170, 170, 127)")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setStyleSheet("color: rgb(170, 170, 127)")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 520, 93, 28))
        self.pushButton.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
"background-color: rgb(245, 163, 188);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 281, 121))
        self.label_3.setStyleSheet("image: url(:/newPrefix/logo bp.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Pendaftaran Trainee"))
        self.lineEdit.setText(_translate("Form", "Nama :"))
        self.lineEdit_2.setText(_translate("Form", "Usia :"))
        self.lineEdit_4.setText(_translate("Form", "Tinggi badan dan berat badan :"))
        self.lineEdit_3.setText(_translate("Form", "keahlian :"))
        self.pushButton.setText(_translate("Form", "Submit"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
