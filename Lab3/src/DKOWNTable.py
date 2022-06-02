# -*- coding: utf-8 -*-
from ui.UiST import Ui_LoginDialog
from PyQt5 import QtWidgets as Qtt
from PyQt5 import QtCore
from src.Message import critical

class LoginDialog(Qtt.QDialog):
    ui = None
    db = None
    parent = None
    res = None
    title = None
    bank = None

    def __init__(self, parent, title) -> None:
        super().__init__(parent)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.db = parent.db
        self.title = title
        bak = self.db.execute("select Bank_Name from Loan where Loan_ID = '" + self.title + "';")
        self.bank = bak[0][0].replace("'", "''")
        # 初始化配置
        self.initLayout()
        self.renderTable()


    def initLayout(self):
        # 设置主窗口UI界面的初始布局
        self.ui.table.setColumnCount(8) # 不设置不显示这些列
        self.ui.title.setText(self.title + " - 持有者")
        self.ui.table.setHorizontalHeaderLabels(['身份证号', '姓名', '电话', '住址', '联系人姓名', '联系人电话', '联系人邮箱', '关系'])
        self.ui.table.horizontalHeader().setSectionResizeMode(Qtt.QHeaderView.Stretch) #设置表格等宽
        self.ui.table.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")

    # all the function to bind with

    def renderTable(self):
        self.ui.table.setRowCount(0)
        self.res = self.db.execute("select * from Client where Client_ID in (select Client_ID from Bear where Loan_ID = '" + self.title + "');")
        currentRowCount = self.ui.table.rowCount()
        for row in self.res:
            ro = []
            item = []
            self.ui.table.insertRow(currentRowCount)
            for i in range(0, 8):
                if row[i] is None:
                    ro.append('')
                else:
                    ro.append(str(row[i]).upper())
            for i in range(0, len(ro)):
                item.append(Qtt.QTableWidgetItem(ro[i]))
                item[i].setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.table.setItem(currentRowCount, i, item[i])
            currentRowCount += 1
            self.ui.table.setRowCount(currentRowCount)
            self.ui.table.setEditTriggers(Qtt.QTableWidget.NoEditTriggers)
            self.ui.table.setSelectionMode(Qtt.QAbstractItemView.NoSelection)
