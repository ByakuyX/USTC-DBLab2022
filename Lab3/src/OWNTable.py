# -*- coding: utf-8 -*-
from ui.OWNT import Ui_LoginDialog
from PyQt5 import QtWidgets as Qtt
from PyQt5 import QtCore
from src.Message import critical
from datetime import date

class LoginDialog(Qtt.QDialog):
    ui = None
    db = None
    parent = None
    res = None
    title = None
    type = None
    bank = None

    def __init__(self, parent, title, type) -> None:
        super().__init__(parent)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.db = parent.db
        self.title = title
        self.type = type
        bak = self.db.execute("select Bank_Name from Account where Account_ID = '" + self.title + "';")
        self.bank = bak[0][0].replace("'", "''")
        # 初始化配置
        self.initLayout()
        self.initBinding()
        self.renderTable()


    def initLayout(self):
        # 设置主窗口UI界面的初始布局
        self.ui.table.setColumnCount(9) # 不设置不显示这些列
        self.ui.title.setText(self.title + " - 持有者")
        self.ui.table.setHorizontalHeaderLabels(['身份证号', '姓名', '电话', '住址', '联系人姓名', '联系人电话', '联系人邮箱', '关系', '操作'])
        self.ui.table.horizontalHeader().setSectionResizeMode(Qtt.QHeaderView.Stretch) #设置表格等宽
        self.ui.table.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")
    
    def initBinding(self):
        # 将主界面按钮点击动作绑定到函数
        self.ui.AddBtn.clicked.connect(self.AddButton)

    # all the function to bind with

    def renderTable(self):
        self.ui.table.setRowCount(0)
        self.res = self.db.execute("select * from Client where Client_ID in (select Client_ID from Own where Account_ID = '" + self.title + "');")
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
            self.ui.table.setCellWidget(currentRowCount, len(ro), self.buttonForRow())
            currentRowCount += 1
            self.ui.table.setRowCount(currentRowCount)
            self.ui.table.setEditTriggers(Qtt.QTableWidget.NoEditTriggers)
            self.ui.table.setSelectionMode(Qtt.QAbstractItemView.NoSelection) 

    def buttonForRow(self):
        widget = Qtt.QWidget()
        # 删除
        self.deleteBtn = Qtt.QPushButton('删除')
        self.deleteBtn.setStyleSheet(''' text-align : center;
                                    height : 30px;
                                    background-color : LightCoral;
                                    border-style: outset;
                                    font : 13px; ''')
        self.deleteBtn.clicked.connect(self.DeleteButton)
        hLayout = Qtt.QHBoxLayout()
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def DeleteButton(self):
        button = self.sender()
        if button:
            row = self.ui.table.indexAt(button.parent().pos()).row()
            tid = self.res[row][0].replace("'", "''")
            self.db.execute("delete from Own where Client_ID = '" + tid + "' and Account_ID = '" + self.title + "';")
            self.db.execute("delete from Checking where Client_ID = '" + tid + "' and Account_Type = '" + self.type + "' and Bank_Name = '" + self.bank + "';")
            self.renderTable()
    
    def AddButton(self):
        # 人不存在，人已经持有此账户，人已经在此银行持有同类账户
        tid = self.ui.addedit.text().replace("'", "''")
        r1 = self.db.execute("select count(*) from Client where Client_ID = '" + tid + "';")
        r2 = self.db.execute("select count(*) from Own where Client_ID = '" + tid + "' and Account_ID = '" + self.title + "';")
        r3 = self.db.execute("select count(*) from Checking where Client_ID = '" + tid + "' and Account_Type = '" + self.type + "' and Bank_Name = '" + self.bank + "';")
        if tid == '':
            critical(self, "请输入客户身份证号")
        elif r1[0][0] < 1:
            critical(self, "此客户不存在")
        elif r2[0][0] > 0:
            critical(self, "此客户已持有本账户")
        elif r3[0][0] > 0:
            critical(self, "此客户在同一银行已持有同类账户")
        else:
            self.db.execute("insert into Own value('" + tid + "', '" + self.title + "', '" + str(date.today()) + "');")
            self.db.execute("insert into Checking value('" + tid + "', '" + self.bank + "', '" + self.type + "');")
            self.renderTable()
