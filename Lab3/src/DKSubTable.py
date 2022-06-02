# -*- coding: utf-8 -*-
from ui.UiST import Ui_LoginDialog
from PyQt5 import QtWidgets as Qtt
from src.DKUpdate import LoginDialog as Upd
from src.DKOWNTable import LoginDialog as OWN
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
        # 发放
        self.updateBtn = Qtt.QPushButton('发放')
        self.updateBtn.setStyleSheet(''' text-align : center;
                                            height : 30px;
                                            background-color : NavajoWhite;
                                            border-style: outset;
                                            font : 13px  ''')
        # 查看持有者
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
        self.deleteBtn.clicked.connect(self.DeleteButton)
        self.ownerBtn.clicked.connect(self.OwnerBtn)
        self.updateBtn.clicked.connect(self.UpdateButton)
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
            status = self.res[row][4].replace("'", "''")
            if status == '已发放':
                critical(self, "此贷款已发放完毕，不能再次发放")
            else:
                dialog = Upd(self, self.res[row][0].replace("'", "''"))
                dialog.exec_()
                self.renderTable()
                self.parent.renderTable()

    def OwnerBtn(self):
        button = self.sender()
        if button:
            row = self.ui.table.indexAt(button.parent().pos()).row()
            dialog = OWN(self, self.res[row][0].replace("'", "''"))
            dialog.exec_()

    def DeleteButton(self):
        button = self.sender()
        if button:
            row = self.ui.table.indexAt(button.parent().pos()).row()
            status = self.res[row][4].replace("'", "''")
            if status == '发放中':
                critical(self, "不能删除处于发放中状态的贷款记录")
            else:
                lid = self.res[row][0].replace("'", "''")
                self.db.execute("alter table Pay drop constraint FK_Apply;")
                self.db.execute("alter table Bear drop constraint FK_Bear2;")

                self.db.execute("delete from Loan where Loan_ID = '" + lid + "';")
                self.db.execute("delete from Pay where Loan_ID = '" + lid + "';")
                self.db.execute("delete from Bear where Loan_ID = '" + lid + "';")

                self.db.execute(
                    "alter table Pay add constraint FK_Apply foreign key (Loan_ID) references Loan (Loan_ID);")
                self.db.execute(
                    "alter table Bear add constraint FK_Bear2 foreign key (Loan_ID) references Loan (Loan_ID);")
                self.renderTable()
                self.parent.renderTable()

            
