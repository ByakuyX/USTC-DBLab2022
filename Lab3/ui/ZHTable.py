# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhtable.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(1127, 488)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginDialog.sizePolicy().hasHeightForWidth())
        LoginDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(LoginDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tablezp = QtWidgets.QTableWidget(LoginDialog)
        self.tablezp.setObjectName("tablezp")
        self.tablezp.setColumnCount(0)
        self.tablezp.setRowCount(0)
        self.gridLayout_4.addWidget(self.tablezp, 1, 0, 1, 1)
        self.tableck = QtWidgets.QTableWidget(LoginDialog)
        self.tableck.setMinimumSize(QtCore.QSize(0, 300))
        self.tableck.setObjectName("tableck")
        self.tableck.setColumnCount(0)
        self.tableck.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableck, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(LoginDialog)
        font = QtGui.QFont()
        font.setFamily("方正清刻本悦宋简体")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(LoginDialog)
        font = QtGui.QFont()
        font.setFamily("方正清刻本悦宋简体")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 3, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.line = QtWidgets.QFrame(LoginDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout.addLayout(self.verticalLayout, 1, 3, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.nLLM = QtWidgets.QCheckBox(LoginDialog)
        self.nLLM.setObjectName("nLLM")
        self.gridLayout_3.addWidget(self.nLLM, 5, 4, 1, 1)
        self.YEM = QtWidgets.QDoubleSpinBox(LoginDialog)
        self.YEM.setMaximum(999999999999.0)
        self.YEM.setObjectName("YEM")
        self.gridLayout_3.addWidget(self.YEM, 1, 3, 1, 1)
        self.LLM = QtWidgets.QDoubleSpinBox(LoginDialog)
        self.LLM.setMaximum(999999999999.0)
        self.LLM.setObjectName("LLM")
        self.gridLayout_3.addWidget(self.LLM, 1, 4, 1, 1)
        self.DateM = QtWidgets.QDateEdit(LoginDialog)
        self.DateM.setObjectName("DateM")
        self.gridLayout_3.addWidget(self.DateM, 1, 15, 1, 1)
        self.label = QtWidgets.QLabel(LoginDialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 5, 1, 1, 1)
        self.TZM = QtWidgets.QDoubleSpinBox(LoginDialog)
        self.TZM.setMaximum(999999999999.0)
        self.TZM.setObjectName("TZM")
        self.gridLayout_3.addWidget(self.TZM, 1, 5, 1, 1)
        self.nLLL = QtWidgets.QCheckBox(LoginDialog)
        self.nLLL.setObjectName("nLLL")
        self.gridLayout_3.addWidget(self.nLLL, 8, 4, 1, 1)
        self.nYEL = QtWidgets.QCheckBox(LoginDialog)
        self.nYEL.setObjectName("nYEL")
        self.gridLayout_3.addWidget(self.nYEL, 8, 3, 1, 1)
        self.nDateL = QtWidgets.QCheckBox(LoginDialog)
        self.nDateL.setObjectName("nDateL")
        self.gridLayout_3.addWidget(self.nDateL, 8, 15, 1, 1)
        self.YEL = QtWidgets.QDoubleSpinBox(LoginDialog)
        self.YEL.setMaximum(999999999999.0)
        self.YEL.setObjectName("YEL")
        self.gridLayout_3.addWidget(self.YEL, 6, 3, 1, 1)
        self.Name = QtWidgets.QLineEdit(LoginDialog)
        self.Name.setText("")
        self.Name.setObjectName("Name")
        self.gridLayout_3.addWidget(self.Name, 6, 1, 1, 1)
        self.nDateM = QtWidgets.QCheckBox(LoginDialog)
        self.nDateM.setObjectName("nDateM")
        self.gridLayout_3.addWidget(self.nDateM, 5, 15, 1, 1)
        self.Id = QtWidgets.QLineEdit(LoginDialog)
        self.Id.setInputMask("")
        self.Id.setText("")
        self.Id.setObjectName("Id")
        self.gridLayout_3.addWidget(self.Id, 1, 1, 1, 1)
        self.TZL = QtWidgets.QDoubleSpinBox(LoginDialog)
        self.TZL.setMaximum(999999999999.0)
        self.TZL.setObjectName("TZL")
        self.gridLayout_3.addWidget(self.TZL, 6, 5, 1, 1)
        self.nTZM = QtWidgets.QCheckBox(LoginDialog)
        self.nTZM.setObjectName("nTZM")
        self.gridLayout_3.addWidget(self.nTZM, 5, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(LoginDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 8, 1, 1, 1)
        self.LLL = QtWidgets.QDoubleSpinBox(LoginDialog)
        self.LLL.setMaximum(999999999999.0)
        self.LLL.setObjectName("LLL")
        self.gridLayout_3.addWidget(self.LLL, 6, 4, 1, 1)
        self.nYEM = QtWidgets.QCheckBox(LoginDialog)
        self.nYEM.setObjectName("nYEM")
        self.gridLayout_3.addWidget(self.nYEM, 5, 3, 1, 1)
        self.DateL = QtWidgets.QDateEdit(LoginDialog)
        self.DateL.setObjectName("DateL")
        self.gridLayout_3.addWidget(self.DateL, 6, 15, 1, 1)
        self.nTZL = QtWidgets.QCheckBox(LoginDialog)
        self.nTZL.setObjectName("nTZL")
        self.gridLayout_3.addWidget(self.nTZL, 8, 5, 1, 1)
        self.Type = QtWidgets.QLineEdit(LoginDialog)
        self.Type.setObjectName("Type")
        self.gridLayout_3.addWidget(self.Type, 1, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(LoginDialog)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 5, 2, 1, 1)
        self.Owner = QtWidgets.QLineEdit(LoginDialog)
        self.Owner.setObjectName("Owner")
        self.gridLayout_3.addWidget(self.Owner, 6, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(LoginDialog)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 8, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 8, 3, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.flushButton = QtWidgets.QPushButton(LoginDialog)
        self.flushButton.setObjectName("flushButton")
        self.verticalLayout_2.addWidget(self.flushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.AddBtn = QtWidgets.QPushButton(LoginDialog)
        self.AddBtn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.AddBtn.setObjectName("AddBtn")
        self.verticalLayout_2.addWidget(self.AddBtn)
        self.AddCho = QtWidgets.QComboBox(LoginDialog)
        self.AddCho.setObjectName("AddCho")
        self.AddCho.addItem("")
        self.AddCho.addItem("")
        self.verticalLayout_2.addWidget(self.AddCho)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.SearchBtn = QtWidgets.QPushButton(LoginDialog)
        self.SearchBtn.setMaximumSize(QtCore.QSize(150, 16777215))
        self.SearchBtn.setObjectName("SearchBtn")
        self.verticalLayout_3.addWidget(self.SearchBtn)
        self.comboBox = QtWidgets.QComboBox(LoginDialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout_3, 8, 1, 1, 1)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "账户管理"))
        self.label_14.setText(_translate("LoginDialog", "存款账户"))
        self.label_13.setText(_translate("LoginDialog", "支票账户"))
        self.title.setText(_translate("LoginDialog", "账户管理"))
        self.nLLM.setText(_translate("LoginDialog", "最高利率"))
        self.label.setText(_translate("LoginDialog", "账户号"))
        self.nLLL.setText(_translate("LoginDialog", "最低利率"))
        self.nYEL.setText(_translate("LoginDialog", "最低余额"))
        self.nDateL.setText(_translate("LoginDialog", "最早日期"))
        self.nDateM.setText(_translate("LoginDialog", "最晚日期"))
        self.nTZM.setText(_translate("LoginDialog", "最高透支"))
        self.label_2.setText(_translate("LoginDialog", "支行名"))
        self.nYEM.setText(_translate("LoginDialog", "最高余额"))
        self.nTZL.setText(_translate("LoginDialog", "最低透支"))
        self.label_10.setText(_translate("LoginDialog", "货币类型"))
        self.label_15.setText(_translate("LoginDialog", "持有者"))
        self.flushButton.setText(_translate("LoginDialog", "刷新"))
        self.AddBtn.setText(_translate("LoginDialog", "添加"))
        self.AddCho.setItemText(0, _translate("LoginDialog", "存款账户"))
        self.AddCho.setItemText(1, _translate("LoginDialog", "支票账户"))
        self.SearchBtn.setText(_translate("LoginDialog", "查询"))
        self.comboBox.setItemText(0, _translate("LoginDialog", "存款账户"))
        self.comboBox.setItemText(1, _translate("LoginDialog", "支票账户"))
        self.comboBox.setItemText(2, _translate("LoginDialog", "所有类型"))
