# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1860, 847)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(".QWidget {\n"
"   background-color: beige;\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    background-color: palegoldenrod;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: khaki;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #d0d67c;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font: bold;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"   font: normal;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border-width: 1;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c;\n"
"    selection-background-color: #C19A6B;\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"QLineEdit, QFrame {\n"
"    border-width: 2px;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border-color: darkkhaki;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
"    border-width: 3px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame ... */\n"
"QLabel {\n"
"    border: none;\n"
"    padding: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"/* A QToolTip is a QLabel ... */\n"
"QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    button-layout: 0;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(860, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Linebenzerlik = QtWidgets.QLineEdit(self.centralwidget)
        self.Linebenzerlik.setGeometry(QtCore.QRect(420, 60, 181, 31))
        self.Linebenzerlik.setObjectName("Linebenzerlik")
        self.Linethread = QtWidgets.QLineEdit(self.centralwidget)
        self.Linethread.setGeometry(QtCore.QRect(200, 60, 181, 31))
        self.Linethread.setText("")
        self.Linethread.setObjectName("Linethread")
        self.Checkproduct = QtWidgets.QCheckBox(self.centralwidget)
        self.Checkproduct.setGeometry(QtCore.QRect(820, 60, 81, 20))
        self.Checkproduct.setObjectName("Checkproduct")
        self.Checkissue = QtWidgets.QCheckBox(self.centralwidget)
        self.Checkissue.setGeometry(QtCore.QRect(820, 90, 81, 20))
        self.Checkissue.setObjectName("Checkissue")
        self.Checkcompany = QtWidgets.QCheckBox(self.centralwidget)
        self.Checkcompany.setGeometry(QtCore.QRect(820, 120, 91, 20))
        self.Checkcompany.setObjectName("Checkcompany")
        self.Checkstate = QtWidgets.QCheckBox(self.centralwidget)
        self.Checkstate.setGeometry(QtCore.QRect(930, 60, 81, 20))
        self.Checkstate.setObjectName("Checkstate")
        self.Checkzipcode = QtWidgets.QCheckBox(self.centralwidget)
        self.Checkzipcode.setGeometry(QtCore.QRect(930, 90, 81, 20))
        self.Checkzipcode.setObjectName("Checkzipcode")
        self.Checkcomplaintid = QtWidgets.QCheckBox(self.centralwidget)
        self.Checkcomplaintid.setGeometry(QtCore.QRect(930, 120, 111, 20))
        self.Checkcomplaintid.setObjectName("Checkcomplaintid")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 150, 1881, 641))
        self.tabWidget.setObjectName("tabWidget")
        self.Veriler = QtWidgets.QWidget()
        self.Veriler.setObjectName("Veriler")
        self.Tableveriler = QtWidgets.QTableWidget(self.Veriler)
        self.Tableveriler.setGeometry(QtCore.QRect(-10, -10, 1881, 621))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Tableveriler.setFont(font)
        self.Tableveriler.setRowCount(1000000)
        self.Tableveriler.setObjectName("Tableveriler")
        self.Tableveriler.setColumnCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.Tableveriler.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableveriler.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableveriler.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableveriler.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableveriler.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableveriler.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableveriler.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableveriler.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableveriler.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableveriler.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableveriler.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableveriler.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tableveriler.setHorizontalHeaderItem(12, item)
        self.Tableveriler.horizontalHeader().setDefaultSectionSize(180)
        self.tabWidget.addTab(self.Veriler, "")
        self.Thread = QtWidgets.QWidget()
        self.Thread.setObjectName("Thread")
        self.Tabtime = QtWidgets.QTableWidget(self.Thread)
        self.Tabtime.setGeometry(QtCore.QRect(-10, -10, 1881, 621))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Tabtime.setFont(font)
        self.Tabtime.setRowCount(10000)
        self.Tabtime.setObjectName("Tabtime")
        self.Tabtime.setColumnCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.Tabtime.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabtime.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabtime.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabtime.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabtime.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabtime.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabtime.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabtime.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabtime.setHorizontalHeaderItem(8, item)
        self.Tabtime.horizontalHeader().setDefaultSectionSize(200)
        self.tabWidget.addTab(self.Thread, "")
        self.BtnShow = QtWidgets.QPushButton(self.centralwidget)
        self.BtnShow.setGeometry(QtCore.QRect(1280, 110, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.BtnShow.setFont(font)
        self.BtnShow.setObjectName("BtnShow")
        self.Lineveriadeti = QtWidgets.QLineEdit(self.centralwidget)
        self.Lineveriadeti.setGeometry(QtCore.QRect(1280, 60, 181, 31))
        self.Lineveriadeti.setText("")
        self.Lineveriadeti.setObjectName("Lineveriadeti")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1320, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboOrtak = QtWidgets.QComboBox(self.centralwidget)
        self.comboOrtak.setGeometry(QtCore.QRect(640, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboOrtak.setFont(font)
        self.comboOrtak.setObjectName("comboOrtak")
        self.comboOrtak.addItem("")
        self.comboOrtak.addItem("")
        self.comboOrtak.addItem("")
        self.comboOrtak.addItem("")
        self.comboOrtak.addItem("")
        self.comboOrtak.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(650, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Linecomplaint = QtWidgets.QLineEdit(self.centralwidget)
        self.Linecomplaint.setGeometry(QtCore.QRect(1060, 60, 181, 31))
        self.Linecomplaint.setText("")
        self.Linecomplaint.setObjectName("Linecomplaint")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1090, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1860, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.comboOrtak.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Benzerlik Oranı"))
        self.label_2.setText(_translate("MainWindow", "Benzerlik"))
        self.label_3.setText(_translate("MainWindow", "Thread Sayısı"))
        self.Checkproduct.setText(_translate("MainWindow", "Product"))
        self.Checkissue.setText(_translate("MainWindow", "Issue"))
        self.Checkcompany.setText(_translate("MainWindow", "Company"))
        self.Checkstate.setText(_translate("MainWindow", "State"))
        self.Checkzipcode.setText(_translate("MainWindow", "ZipCode"))
        self.Checkcomplaintid.setText(_translate("MainWindow", "complaintID"))
        item = self.Tableveriler.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product_1"))
        item = self.Tableveriler.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Issue_1"))
        item = self.Tableveriler.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Company_1"))
        item = self.Tableveriler.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "State_1"))
        item = self.Tableveriler.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ZipCode_1"))
        item = self.Tableveriler.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "complaintID_1"))
        item = self.Tableveriler.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Product_2"))
        item = self.Tableveriler.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Issue_2"))
        item = self.Tableveriler.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Company_2"))
        item = self.Tableveriler.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "State_2"))
        item = self.Tableveriler.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "ZipCode_2"))
        item = self.Tableveriler.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "complaintID_2"))
        item = self.Tableveriler.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Oran"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Veriler), _translate("MainWindow", "Tab 1"))
        item = self.Tabtime.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Total_Time"))
        item = self.Tabtime.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Thread_1"))
        item = self.Tabtime.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Thread_2"))
        item = self.Tabtime.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Thread_3"))
        item = self.Tabtime.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Thread_4"))
        item = self.Tabtime.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Thread_5"))
        item = self.Tabtime.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Thread_6"))
        item = self.Tabtime.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Thread_7"))
        item = self.Tabtime.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Thread_8"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Thread), _translate("MainWindow", "Tab 2"))
        self.BtnShow.setText(_translate("MainWindow", "Show"))
        self.label_4.setText(_translate("MainWindow", "Veri Adedi"))
        self.comboOrtak.setItemText(0, _translate("MainWindow", "1.Hiçbiri"))
        self.comboOrtak.setItemText(1, _translate("MainWindow", "2.Product"))
        self.comboOrtak.setItemText(2, _translate("MainWindow", "3.Issue"))
        self.comboOrtak.setItemText(3, _translate("MainWindow", "4.Company"))
        self.comboOrtak.setItemText(4, _translate("MainWindow", "5.State"))
        self.comboOrtak.setItemText(5, _translate("MainWindow", "6.ZipCode"))
        self.label_5.setText(_translate("MainWindow", "Ortak Sütun"))
        self.label_6.setText(_translate("MainWindow", "complaintID"))