# -*- coding: utf-8 -*-
from ui.DKTable import Ui_LoginDialog
from src.DKInput import LoginDialog as Ipt
from src.DKUpdate import LoginDialog as Upd
from src.DKSubTable import TablePage as Stb
from src.DKOWNTable import LoginDialog as OWN
from src.Message import critical
from PyQt5 import QtWidgets as Qtt
from PyQt5 import QtCore

class TablePage(Qtt.QDialog):
    ui = None
    db = None
    dbName = None
    parent = None
    res1 = None
    res2 = None
    
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
        self.ui.title.setText(self.dbName + " - 账户管理")
        self.ui.table.setColumnCount(6) # 不设置不显示这些列
        self.ui.table.setHorizontalHeaderLabels(['贷款号', '支行名', '总额度', '已发放额度', '贷款状态', '操作'])
        self.ui.table.horizontalHeader().setSectionResizeMode(Qtt.QHeaderView.Stretch) #设置表格等宽
        self.ui.table.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")
        self.ui.tablepay.setColumnCount(4) # 不设置不显示这些列
        self.ui.tablepay.setHorizontalHeaderLabels(['发放编号', '贷款号', '发放金额', '发放日期'])
        self.ui.tablepay.horizontalHeader().setSectionResizeMode(Qtt.QHeaderView.Stretch) #设置表格等宽
        self.ui.tablepay.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")

    def initBinding(self):
        # 将主界面按钮点击动作绑定到函数
        self.ui.AddBtn.clicked.connect(self.AddButton)
        self.ui.SearchBtn.clicked.connect(self.SearchButton)  
        self.ui.flushButton.clicked.connect(self.renderTable)  

    # all the function to bind with

    def renderTable(self):
        self.renderTable1()
        self.renderTable2()

    def renderTable1(self):
        self.ui.table.setRowCount(0)
        self.res1 = self.db.execute("select * from Loan;")
        currentRowCount = self.ui.table.rowCount()
        for row in self.res1:
            ro = []
            item = []
            self.ui.table.insertRow(currentRowCount)
            for i in range(0, 5):
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

    def renderTable2(self):
        self.ui.tablepay.setRowCount(0)
        self.res2 = self.db.execute("select * from pay;")
        currentRowCount = self.ui.tablepay.rowCount()
        for row in self.res2:
            ro = []
            item = []
            self.ui.tablepay.insertRow(currentRowCount)
            for i in range(0, 4):
                if row[i] is None:
                    ro.append('')
                else:
                    ro.append(str(row[i]).upper())
            for i in range(0, len(ro)):
                item.append(Qtt.QTableWidgetItem(ro[i]))
                item[i].setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tablepay.setItem(currentRowCount, i, item[i])
            currentRowCount += 1
            self.ui.tablepay.setRowCount(currentRowCount)
            self.ui.tablepay.setEditTriggers(Qtt.QTableWidget.NoEditTriggers)
            self.ui.tablepay.setSelectionMode(Qtt.QAbstractItemView.NoSelection)

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

    def OwnerBtn(self):
        button = self.sender()
        if button:
            row = self.ui.table.indexAt(button.parent().pos()).row()
            dialog = OWN(self, self.res1[row][0])
            dialog.exec_()

    def AddButton(self):
        dialog = Ipt(self)
        dialog.exec_()

    def UpdateButton(self):
        button = self.sender()
        if button:
            row = self.ui.table.indexAt(button.parent().pos()).row()
            status = self.res1[row][4]
            if status == '已发放':
                critical(self, "此贷款已发放完毕，不能再次发放")
            else:
                dialog = Upd(self, self.res1[row][0])
                dialog.exec_()
                self.renderTable()

    def SearchButton(self):
        Vals = []
        Vats = ['Loan_ID', 'Bank_Name', 'Loan_Status', 'Loan_Amount', 'Pay_already']
        Bs = []
        Vals.append(self.ui.Id.text())
        Vals.append(self.ui.Name.text())
        Vals.append(self.ui.status.currentText())

        Vals.append(self.ui.amountL.text())
        Vals.append(self.ui.amountM.text())
        Vals.append(self.ui.payL.text())
        Vals.append(self.ui.payM.text())

        Vals.append(self.ui.Owner.text())
        epy = [1, 1, 0, 0, 0, 0, 0]
        if self.ui.nstatus.isChecked():
            epy[2] = 1
        if self.ui.namountL.isChecked():
            epy[3] = 1
        if self.ui.namountM.isChecked():
            epy[4] = 1
        if self.ui.npayL.isChecked():
            epy[5] = 1
        if self.ui.npayM.isChecked():
            epy[6] = 1
        for i in range(0, 3):
            if epy[i] == 1 and Vals[i] is not '':
                Bs.append(Vats[i] + " = '" + Vals[i] + "'")
        for i in range(3, 7, 2):
            if epy[i] == 1:
                Bs.append(Vats[(i + 3) // 2] + " >= '" + Vals[i] + "'")
            if epy[i + 1] == 1:
                Bs.append(Vats[(i + 3) // 2] + " <= '" + Vals[i + 1] + "'")
        if Vals[7] is not '':
            Bs.append("Loan_ID in (select Loan_ID from Bear where Client_ID = '" + Vals[7] + "')")
        if len(Bs) > 0:
            st = ' and '
            sql = 'select * from Loan where ' + st.join(Bs) + ';'
            mtl = ['贷款号', '支行名', '总额度', '已发放额度', '贷款状态', '操作']
            dialog = Stb(self, sql, mtl, "贷款")
            dialog.exec_()

    def DeleteButton(self):
        button = self.sender()
        if button:
            row = self.ui.table.indexAt(button.parent().pos()).row()
            status = self.res1[row][4]
            if status == '发放中':
                critical(self, "不能删除处于发放中状态的贷款记录")
            else:
                lid = self.res1[row][0]
                self.db.execute("alter table Pay drop constraint FK_Apply;")
                self.db.execute("alter table Bear drop constraint FK_Bear1;")
                self.db.execute("alter table Bear drop constraint FK_Bear2;")

                self.db.execute("delete from Loan where Loan_ID = '" + lid + "';")
                self.db.execute("delete from Pay where Loan_ID = '" + lid + "';")
                self.db.execute("delete from Bear where Loan_ID = '" + lid + "';")

                self.db.execute(
                    "alter table Pay add constraint FK_Apply foreign key (Loan_ID) references Loan (Loan_ID);")
                self.db.execute(
                    "alter table Bear add constraint FK_Bear1 foreign key (Client_ID) references Client (Client_ID);")
                self.db.execute(
                    "alter table Bear add constraint FK_Bear2 foreign key (Loan_ID) references Loan (Loan_ID);")
                self.renderTable()
