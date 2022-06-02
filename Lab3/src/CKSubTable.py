# -*- coding: utf-8 -*-
from ui.UiST import Ui_LoginDialog
from PyQt5 import QtWidgets as Qtt
from src.ZHUpdateck import LoginDialog as Updck
from src.OWNTable import LoginDialog as OWN
from PyQt5 import QtCore

class TablePage(Qtt.QDialog):
    ui = None
    db = None
    parent = None
    res = None
    sql = None
    width = None
    labels = None
    title = None

    def __init__(self, parent, sql, labels, title) -> None:
        super().__init__(parent)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.db = parent.db
        self.sql = sql
        self.labels = labels
        self.width = len(labels)
        self.title = title
        # 初始化配置
        self.initLayout()
        self.renderTable()


    def initLayout(self):
        # 设置主窗口UI界面的初始布局
        self.ui.table.setColumnCount(self.width) # 不设置不显示这些列
        self.ui.title.setText(self.title + " - 查询结果")
        self.ui.table.setHorizontalHeaderLabels(self.labels)
        self.ui.table.horizontalHeader().setSectionResizeMode(Qtt.QHeaderView.Stretch) #设置表格等宽
        self.ui.table.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")

    # all the function to bind with

    def renderTable(self):
        self.ui.table.setRowCount(0)
        self.res = self.db.execute(self.sql)
        currentRowCount = self.ui.table.rowCount()
        for row in self.res:
            ro = []
            item = []
            self.ui.table.insertRow(currentRowCount)
            for i in range(0, self.width):
                if i == 4:
                    continue
                if row[i] is None:
                    ro.append('')
                else:
                    ro.append(str(row[i]).upper())
            for i in range(0, len(ro)):
                item.append(Qtt.QTableWidgetItem(ro[i]))
                item[i].setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.table.setItem(currentRowCount, i, item[i])
            self.ui.table.setCellWidget(currentRowCount, len(ro), self.buttonForRow())
            currentRowCount += 1
            self.ui.table.setRowCount(currentRowCount)
            self.ui.table.setEditTriggers(Qtt.QTableWidget.NoEditTriggers)
            self.ui.table.setSelectionMode(Qtt.QAbstractItemView.NoSelection)

    def buttonForRow(self):
        widget = Qtt.QWidget()
        # 修改
        self.updateBtn = Qtt.QPushButton('修改')
        self.updateBtn.setStyleSheet(''' text-align : center;
                                    height : 30px;
                                    background-color : NavajoWhite;
                                    border-style: outset;
                                    font : 13px  ''')
        self.ownerBtn = Qtt.QPushButton('持有')
        self.ownerBtn.setStyleSheet(''' text-align : center;
                                    height : 30px;
                                    background-color : lightskyblue;
                                    border-style: outset;
                                    font : 13px; ''')
        # 删除
        self.deleteBtn = Qtt.QPushButton('删除')
        self.deleteBtn.setStyleSheet(''' text-align : center;
                                    height : 30px;
                                    background-color : LightCoral;
                                    border-style: outset;
                                    font : 13px; ''')
        self.updateBtn.clicked.connect(self.UpdateButton)
        self.ownerBtn.clicked.connect(self.OwnerBtn)
        self.deleteBtn.clicked.connect(self.DeleteButton)
        hLayout = Qtt.QHBoxLayout()
        hLayout.addWidget(self.updateBtn)
        hLayout.addWidget(self.ownerBtn)
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def UpdateButton(self):
        button = self.sender()
        if button:
            row = self.ui.table.indexAt(button.parent().pos()).row()
            dialog = Updck(self, self.res[row][0].replace("'", "''"))
            dialog.exec_()
            self.renderTable()
            self.parent.renderTable1()

    def OwnerBtn(self):
        button = self.sender()
        if button:
            row = self.ui.table.indexAt(button.parent().pos()).row()
            dialog = OWN(self, self.res[row][0].replace("'", "''"), '1')
            dialog.exec_()
            self.renderTable()

    def DeleteButton(self):
        button = self.sender()
        if button:
            row = self.ui.table.indexAt(button.parent().pos()).row()
            tid = self.res[row][0].replace("'", "''")
            rn2 = self.db.execute("select Bank_Name from Account where Account_ID = '" + tid + "';")

            self.db.execute("alter table Saving_Account drop constraint FK_Account_Type1;")
            self.db.execute("alter table Own drop constraint FK_Own2;")

            self.db.execute("delete from Account where Account_ID = '" + tid + "';")
            self.db.execute("delete from Saving_Account where Account_ID = '" + tid + "';")
            self.db.execute("delete from Own where Account_ID = '" + tid + "';")
            self.db.execute(
                "delete from Checking where Client_ID in (select Client_ID from Own where Account_ID = '" + tid + "') and Bank_Name = '" + str(
                    rn2[0][0]).replace("'", "''") + "' and Account_Type = 1")

            self.db.execute(
                "alter table Saving_Account add constraint FK_Account_Type1 foreign key (Account_ID) references Account (Account_ID);")
            self.db.execute(
                "alter table Own add constraint FK_Own2 foreign key (Account_ID) references Account (Account_ID);")
            self.renderTable()
            self.parent.renderTable1()

            
