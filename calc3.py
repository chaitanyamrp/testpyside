# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\chaitanya\Sandbox\calc.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from __future__ import division

from PySide import QtCore, QtGui
import qdarkstyle


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(321, 484)
        Form.setAutoFillBackground(False)
        self.cancelclear = QtGui.QPushButton(Form)
        self.cancelclear.setGeometry(QtCore.QRect(0, 90, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cancelclear.setFont(font)
        self.cancelclear.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cancelclear.setObjectName(_fromUtf8("cancelclear"))
        self.plusminus = QtGui.QPushButton(Form)
        self.plusminus.setGeometry(QtCore.QRect(80, 90, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.plusminus.setFont(font)
        self.plusminus.setObjectName(_fromUtf8("plusminus"))
        self.percent = QtGui.QPushButton(Form)
        self.percent.setGeometry(QtCore.QRect(160, 90, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.percent.setFont(font)
        self.percent.setObjectName(_fromUtf8("percent"))
        self.seven = QtGui.QPushButton(Form)
        self.seven.setGeometry(QtCore.QRect(0, 170, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.seven.setFont(font)
        self.seven.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.seven.setObjectName(_fromUtf8("seven"))
        self.eight = QtGui.QPushButton(Form)
        self.eight.setGeometry(QtCore.QRect(80, 170, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eight.setFont(font)
        self.eight.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.eight.setObjectName(_fromUtf8("eight"))
        self.nine = QtGui.QPushButton(Form)
        self.nine.setGeometry(QtCore.QRect(160, 170, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nine.setFont(font)
        self.nine.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nine.setObjectName(_fromUtf8("nine"))
        self.four = QtGui.QPushButton(Form)
        self.four.setGeometry(QtCore.QRect(0, 250, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.four.setFont(font)
        self.four.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.four.setObjectName(_fromUtf8("four"))
        self.five = QtGui.QPushButton(Form)
        self.five.setGeometry(QtCore.QRect(80, 250, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.five.setFont(font)
        self.five.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.five.setObjectName(_fromUtf8("five"))
        self.six = QtGui.QPushButton(Form)
        self.six.setGeometry(QtCore.QRect(160, 250, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.six.setFont(font)
        self.six.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.six.setFlat(False)
        self.six.setObjectName(_fromUtf8("six"))
        self.one = QtGui.QPushButton(Form)
        self.one.setGeometry(QtCore.QRect(0, 330, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.one.setFont(font)
        self.one.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.one.setObjectName(_fromUtf8("one"))
        self.two = QtGui.QPushButton(Form)
        self.two.setGeometry(QtCore.QRect(80, 330, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.two.setFont(font)
        self.two.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.two.setFlat(False)
        self.two.setObjectName(_fromUtf8("two"))
        self.three = QtGui.QPushButton(Form)
        self.three.setGeometry(QtCore.QRect(160, 330, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.three.setFont(font)
        self.three.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.three.setFlat(False)
        self.three.setObjectName(_fromUtf8("three"))
        self.minus = QtGui.QPushButton(Form)
        self.minus.setGeometry(QtCore.QRect(240, 330, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.minus.setFont(font)
        self.minus.setObjectName(_fromUtf8("minus"))
        self.into = QtGui.QPushButton(Form)
        self.into.setGeometry(QtCore.QRect(240, 250, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.into.setFont(font)
        self.into.setObjectName(_fromUtf8("into"))
        self.by = QtGui.QPushButton(Form)
        self.by.setGeometry(QtCore.QRect(240, 170, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.by.setFont(font)
        self.by.setObjectName(_fromUtf8("by"))
        self.backspace = QtGui.QPushButton(Form)
        self.backspace.setGeometry(QtCore.QRect(240, 90, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.backspace.setFont(font)
        self.backspace.setObjectName(_fromUtf8("backspace"))
        self.zero = QtGui.QPushButton(Form)
        self.zero.setGeometry(QtCore.QRect(0, 410, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.zero.setFont(font)
        self.zero.setObjectName(_fromUtf8("zero"))
        self.dot = QtGui.QPushButton(Form)
        self.dot.setGeometry(QtCore.QRect(80, 410, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dot.setFont(font)
        self.dot.setObjectName(_fromUtf8("dot"))
        self.plus = QtGui.QPushButton(Form)
        self.plus.setGeometry(QtCore.QRect(160, 410, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.plus.setFont(font)
        self.plus.setObjectName(_fromUtf8("plus"))
        self.equals = QtGui.QPushButton(Form)
        self.equals.setGeometry(QtCore.QRect(240, 410, 81, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.equals.setFont(font)
        self.equals.setObjectName(_fromUtf8("equals"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.textEdit.setFont(font)
        self.textEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.cancelclear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit.clear)
        QtCore.QObject.connect(self.zero, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum(0))
        QtCore.QObject.connect(self.one, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum(1))
        QtCore.QObject.connect(self.two, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum(2))
        QtCore.QObject.connect(self.three, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum(3))
        QtCore.QObject.connect(self.four, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum(4))
        QtCore.QObject.connect(self.five, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum(5))
        QtCore.QObject.connect(self.six, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum(6))
        QtCore.QObject.connect(self.seven, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum(7))
        QtCore.QObject.connect(self.eight, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum(8))
        QtCore.QObject.connect(self.nine, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum(9))
        QtCore.QObject.connect(self.dot, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum("."))
        QtCore.QObject.connect(self.plus, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum("+"))
        QtCore.QObject.connect(self.minus, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum("-"))
        QtCore.QObject.connect(self.by, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum("/"))
        QtCore.QObject.connect(self.percent, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum("%"))
        QtCore.QObject.connect(self.into, QtCore.SIGNAL(_fromUtf8("clicked()")), lambda: self.updatenum("*"))
        QtCore.QObject.connect(self.equals, QtCore.SIGNAL(_fromUtf8("clicked()")), self.output)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.cancelclear.setText(_translate("Form", "C", None))
        self.plusminus.setText(_translate("Form", "+ / -", None))
        self.percent.setText(_translate("Form", "%", None))
        self.seven.setText(_translate("Form", "7", None))
        self.eight.setText(_translate("Form", "8", None))
        self.nine.setText(_translate("Form", "9", None))
        self.four.setText(_translate("Form", "4", None))
        self.five.setText(_translate("Form", "5", None))
        self.six.setText(_translate("Form", "6", None))
        self.one.setText(_translate("Form", "1", None))
        self.two.setText(_translate("Form", "2", None))
        self.three.setText(_translate("Form", "3", None))
        self.minus.setText(_translate("Form", "-", None))
        self.into.setText(_translate("Form", "x", None))
        self.by.setText(_translate("Form", "/", None))
        self.backspace.setText(_translate("Form", "DEL", None))
        self.zero.setText(_translate("Form", "0", None))
        self.dot.setText(_translate("Form", ".", None))
        self.plus.setText(_translate("Form", "+", None))
        self.equals.setText(_translate("Form", "=", None))

    def updatenum(self,num):
        self.textEdit.setText(self.textEdit.toPlainText()+str(num))
        self.textEdit.setAlignment(QtCore.Qt.AlignRight)
    def output(self):
        print eval(str(self.textEdit.toPlainText()))
        if ('/') in str(self.textEdit.toPlainText()):
            str(self.textEdit.toPlainText()).split('/')
        self.textEdit.setText(str(eval(str(self.textEdit.toPlainText()))))
        self.textEdit.setAlignment(QtCore.Qt.AlignRight)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

