# -*- coding: utf-8 -*-
from ui.UiKHT import Ui_LoginDialog
from src.KHInput import LoginDialog as Ipt
from src.SubTable import TablePage as Stb
from src.KHUpdate import LoginDialog as Upd
from src.Message import critical
from PyQt5 import QtWidgets as Qtt
from PyQt5 import QtCore

class TablePage(Qtt.QDialog):
    ui = None
    db = None
    dbName = None
    parent = None
    res = None
    
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.db = parent.db
        self.dbName = parent.dbName
        # 初始化配置
        self.initLayout()
        self.initBinding()
        self.renderTable()


    def initLayout(self):
        # 设置主窗口UI界面的初始布局
        self.ui.table.setColumnCount(9) # 不设置不显示这些列
        self.ui.title.setText(self.dbName + " - 客户管理")
        self.ui.table.setHorizontalHeaderLabels(['身份证号', '姓名', '电话', '住址', '联系人姓名', '联系人电话', '联系人邮箱', '关系', '操作'])
        self.ui.table.horizontalHeader().setSectionResizeMode(Qtt.QHeaderView.Stretch) #设置表格等宽
        self.ui.table.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")
    
    def initBinding(self):
        # 将主界面按钮点击动作绑定到函数
        self.ui.AddBtn.clicked.connect(self.AddButton)
        self.ui.SearchBtn.clicked.connect(self.SearchButton)  
        self.ui.flushButton.clicked.connect(self.renderTable)  

    # all the function to bind with

    def renderTable(self):
        self.ui.table.setRowCount(0)
        self.res = self.db.execute("select * from Client;")
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

    def AddButton(self):
        dialog = Ipt(self)
        dialog.exec_()
        self.renderTable()

    def UpdateButton(self):
        button = self.sender()
        if button:
            row = self.ui.table.indexAt(button.parent().pos()).row()
            dialog = Upd(self, self.res[row][0])
            dialog.exec_()
            self.renderTable()

    def SearchButton(self):
        Vals = []
        Vats = ['Client_ID', 'Client_Name', 'Client_Tel', 'Client_Address', 'Contact_Name', 'Contact_Email', 'Contact_Tel', 'Relation']
        Bs = []
        Vals.append(self.ui.Id.text())
        Vals.append(self.ui.Name.text())
        Vals.append(self.ui.Tel.text())
        Vals.append(self.ui.Addr.text())
        Vals.append(self.ui.CName.text())
        Vals.append(self.ui.CTel.text())
        Vals.append(self.ui.CEm.text())
        Vals.append(self.ui.Rel.text())
        for i in range(0, 8):
            if Vals[i] is not '':
                Bs.append(Vats[i] + " = '" + Vals[i] + "'")
        if len(Bs) > 0:
            st = ' and '
            sql = 'select * from Client where ' + st.join(Bs) + ';'
            mtl = ['身份证号', '姓名', '电话', '住址', '联系人姓名', '联系人电话', '联系人邮箱', '关系', '操作']
            dialog = Stb(self, sql, mtl, "客户")
            dialog.exec_()

    def DeleteButton(self):
        button = self.sender()
        if button:
            row = self.ui.table.indexAt(button.parent().pos()).row()
            tid = self.res[row][0]
            rtt = self.db.execute(
                "select count(*) from own, bear where own.client_id = '" + tid + "' or bear.client_id = '" + tid + "';")
            if rtt[0][0] > 0:
                critical(self, "存在关联账户或贷款记录，不能删除")
            else:
                self.db.execute("delete from Client where Client_ID = '" + tid + "';")
                self.renderTable()

            
