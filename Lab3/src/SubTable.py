# -*- coding: utf-8 -*-
from ui.UiST import Ui_LoginDialog
from PyQt5 import QtWidgets as Qtt
from src.KHUpdate import LoginDialog as Upd
from src.Message import critical
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
            for i in range(0, self.width - 1):
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
        # 删除
        self.deleteBtn = Qtt.QPushButton('删除')
        self.deleteBtn.setStyleSheet(''' text-align : center;
                                    height : 30px;
                                    background-color : LightCoral;
                                    border-style: outset;
                                    font : 13px; ''')
        self.updateBtn.clicked.connect(self.UpdateButton)
        self.deleteBtn.clicked.connect(self.DeleteButton)
        hLayout = Qtt.QHBoxLayout()
        hLayout.addWidget(self.updateBtn)
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def UpdateButton(self):
        button = self.sender()
        if button:
            row = self.ui.table.indexAt(button.parent().pos()).row()
            dialog = Upd(self, self.res[row][0].replace("'", "''"))
            dialog.exec_()
            self.renderTable()
            self.parent.renderTable()

    def DeleteButton(self):
        button = self.sender()
        if button:
            row = self.ui.table.indexAt(button.parent().pos()).row()
            tid = self.res[row][0].replace("'", "''")
            rt1 = self.db.execute("select count(*) from own where client_id = '" + tid + "';")
            rt2 = self.db.execute("select count(*) from bear where client_id = '" + tid + "';")
            rt3 = self.db.execute("select count(*) from checking where client_id = '" + tid + "';")
            if rt1[0][0] > 0 or rt3[0][0] > 0:
                critical(self, "存在关联账户，不能删除")
            elif rt2[0][0] > 0:
                critical(self, "存在贷款记录，不能删除")
            else:
                self.db.execute("alter table own drop constraint fk_own1;")
                self.db.execute("alter table bear drop constraint fk_bear1;")
                self.db.execute("alter table checking drop constraint fk_checking1;")
                self.db.execute("alter table Service drop constraint FK_Service;")
                self.db.execute("delete from Client where Client_ID = '" + tid + "';")
                self.db.execute("delete from Service where Client_ID = '" + tid + "';")
                self.db.execute(
                    "alter table Own add constraint FK_Own1 foreign key (Client_ID) references Client (Client_ID);")
                self.db.execute(
                    "alter table Bear add constraint FK_Bear1 foreign key (Client_ID) references Client (Client_ID);")
                self.db.execute(
                    "alter table Checking add constraint FK_Checking1 foreign key (Client_ID) references Client (Client_ID);")
                self.db.execute(
                    "alter table Service add constraint FK_Service foreign key (Client_ID) references Client (Client_ID);")
                self.renderTable()
                self.parent.renderTable()

            
