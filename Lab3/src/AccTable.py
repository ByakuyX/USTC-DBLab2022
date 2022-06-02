# -*- coding: utf-8 -*-
from ui.ZHTable import Ui_LoginDialog
from src.ZHInputck import LoginDialog as Iptck
from src.ZHInputzp import LoginDialog as Iptzp
from src.ZHUpdateck import LoginDialog as Updck
from src.ZHUpdatezp import LoginDialog as Updzp
from src.CKSubTable import TablePage as StbCK
from src.ZPSubTable import TablePage as StbZP
from src.OWNTable import LoginDialog as OWN
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
        self.ui.tableck.setColumnCount(7) # 不设置不显示这些列
        self.ui.tableck.setHorizontalHeaderLabels(['账户号', '支行名', '余额', '开户日期', '利率', '货币类型', '操作'])
        #跳过'开户日期' 和 '利率' 之间的 '账户号'
        self.ui.tableck.horizontalHeader().setSectionResizeMode(Qtt.QHeaderView.Stretch) #设置表格等宽
        self.ui.tableck.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")
        self.ui.tablezp.setColumnCount(6) # 不设置不显示这些列
        self.ui.tablezp.setHorizontalHeaderLabels(['账户号', '支行名', '余额', '开户日期', '透支额', '操作'])
        self.ui.tablezp.horizontalHeader().setSectionResizeMode(Qtt.QHeaderView.Stretch) #设置表格等宽
        self.ui.tablezp.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")
    
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
        self.ui.tableck.setRowCount(0)
        self.res1 = self.db.execute("select * from Account, Saving_Account where Account.Account_ID = Saving_Account.Account_ID;")
        currentRowCount = self.ui.tableck.rowCount()
        for row in self.res1:
            ro = []
            item = []
            self.ui.tableck.insertRow(currentRowCount)
            for i in range(0, 7):
                if i == 4:
                    continue
                if row[i] is None:
                    ro.append('')
                else:
                    ro.append(str(row[i]).upper())
            for i in range(0, len(ro)):
                item.append(Qtt.QTableWidgetItem(ro[i]))
                item[i].setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tableck.setItem(currentRowCount, i, item[i])
            self.ui.tableck.setCellWidget(currentRowCount, len(ro), self.buttonForRow(1))
            currentRowCount += 1
            self.ui.tableck.setRowCount(currentRowCount)
            self.ui.tableck.setEditTriggers(Qtt.QTableWidget.NoEditTriggers)
            self.ui.tableck.setSelectionMode(Qtt.QAbstractItemView.NoSelection)

    def renderTable2(self):
        self.ui.tablezp.setRowCount(0)
        self.res2 = self.db.execute("select * from Account, Checking_Account where Account.Account_ID = Checking_Account.Account_ID;")
        currentRowCount = self.ui.tablezp.rowCount()
        for row in self.res2:
            ro = []
            item = []
            self.ui.tablezp.insertRow(currentRowCount)
            for i in range(0, 6):
                if i == 4:
                    continue
                if row[i] is None:
                    ro.append('')
                else:
                    ro.append(str(row[i]).upper())
            for i in range(0, len(ro)):
                item.append(Qtt.QTableWidgetItem(ro[i]))
                item[i].setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.tablezp.setItem(currentRowCount, i, item[i])
            self.ui.tablezp.setCellWidget(currentRowCount, len(ro), self.buttonForRow(2))
            currentRowCount += 1
            self.ui.tablezp.setRowCount(currentRowCount)
            self.ui.tablezp.setEditTriggers(Qtt.QTableWidget.NoEditTriggers)
            self.ui.tablezp.setSelectionMode(Qtt.QAbstractItemView.NoSelection)

    def buttonForRow(self, id):
        widget = Qtt.QWidget()
        # 修改
        self.updateBtn = Qtt.QPushButton('修改')
        self.updateBtn.setStyleSheet(''' text-align : center;
                                    height : 30px;
                                    background-color : NavajoWhite;
                                    border-style: outset;
                                    font : 13px  ''')
        # 查看/修改持有者
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
        if id == 1:
            self.deleteBtn.clicked.connect(self.DeleteButton1)
            self.ownerBtn.clicked.connect(self.OwnerBtn1)
            self.updateBtn.clicked.connect(self.UpdateButton1)
        else:
            self.deleteBtn.clicked.connect(self.DeleteButton2)
            self.ownerBtn.clicked.connect(self.OwnerBtn2)
            self.updateBtn.clicked.connect(self.UpdateButton2)
        hLayout = Qtt.QHBoxLayout()
        hLayout.addWidget(self.updateBtn)
        hLayout.addWidget(self.ownerBtn)
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def OwnerBtn1(self):
        button = self.sender()
        if button:
            row = self.ui.tableck.indexAt(button.parent().pos()).row()
            dialog = OWN(self, self.res1[row][0], '1')
            dialog.exec_()
    
    def OwnerBtn2(self):
        button = self.sender()
        if button:
            row = self.ui.tableck.indexAt(button.parent().pos()).row()
            dialog = OWN(self, self.res2[row][0], '2')
            dialog.exec_()

    def AddButton(self):
        if self.ui.AddCho.currentText() == "存款账户":
            dialog = Iptck(self)
            dialog.exec_()
        elif self.ui.AddCho.currentText() == "支票账户":
            dialog = Iptzp(self)
            dialog.exec_()

    def UpdateButton1(self):
        button = self.sender()
        if button:
            row = self.ui.tableck.indexAt(button.parent().pos()).row()
            dialog = Updck(self, self.res1[row][0])
            dialog.exec_()
            self.renderTable1()

    def UpdateButton2(self):
        button = self.sender()
        if button:
            row = self.ui.tableck.indexAt(button.parent().pos()).row()
            dialog = Updzp(self, self.res2[row][0])
            dialog.exec_()
            self.renderTable2()

    def SearchButton(self):
        Vals = []
        Vals.append(self.ui.Id.text())
        Vals.append(self.ui.Name.text())
        Vals.append(self.ui.Type.text())
        Vals.append(self.ui.YEL.text())
        Vals.append(self.ui.YEM.text())
        Vals.append(self.ui.DateL.text())
        Vals.append(self.ui.DateM.text())
        Vals.append(self.ui.LLL.text())
        Vals.append(self.ui.LLM.text())
        Vals.append(self.ui.TZL.text())
        Vals.append(self.ui.TZM.text())
        Vals.append(self.ui.Owner.text())
        if self.ui.comboBox.currentText() == "存款账户":
            self.SearchButton1(Vals[0:9] + Vals[11:])
        elif self.ui.comboBox.currentText() == "支票账户":
            self.SearchButton2(Vals[0:2] + Vals[3:7] + Vals[9:])
        elif self.ui.comboBox.currentText() == "所有类型":
            self.SearchButton1(Vals[0:9] + Vals[11:])
            self.SearchButton2(Vals[0:2] + Vals[3:7] + Vals[9:])
        
    def SearchButton1(self, Vals):
        if not self.ui.nTZL.isChecked() and not self.ui.nTZM.isChecked():
            Vats = ['Account.Account_ID', 'Bank_Name', 'Currency_Type', 'Balance', 'Opening_Date', 'Interest_Rate']
            Bs = []
            epy = [0, 0, 0, 0, 0, 0]
            if self.ui.nYEL.isChecked():
                epy[0] = 1
            if self.ui.nYEM.isChecked():
                epy[1] = 1
            if self.ui.nDateL.isChecked():
                epy[2] = 1
            if self.ui.nDateM.isChecked():
                epy[3] = 1
            if self.ui.nLLL.isChecked():
                epy[4] = 1
            if self.ui.nLLM.isChecked():
                epy[5] = 1
            for i in range(0, 3):
                if Vals[i] is not '':
                    Bs.append(Vats[i] + " = '" + Vals[i] + "'")
            for i in range (3, 9, 2):
                if epy[i - 3] == 1:
                    Bs.append(Vats[(i + 3) // 2] + " >= '" + Vals[i] + "'")
                if epy[i - 2] == 1:
                    Bs.append(Vats[(i + 3) // 2] + " <= '" + Vals[i + 1] + "'")
            if Vals[9] is not '':
                Bs.append("Account.Account_ID in (select Account_ID from Own where Client_ID = '" + Vals[9] + "')")

            st = ' and '
            sql = 'select * from Account, Saving_Account where Account.Account_ID = Saving_Account.Account_ID and ' + st.join(Bs) + ';'

            mtl = ['账户号', '支行名', '余额', '开户日期', '利率', '货币类型', '操作']
            if len(Bs) > 0:
                dialog = StbCK(self, sql, mtl, '存款账户')
                dialog.exec_()

    def SearchButton2(self, Vals):
        if self.ui.Type.text() is '' and not self.ui.nLLL.isChecked() and not self.ui.nLLM.isChecked():
            Vats = ['Account.Account_ID', 'Bank_Name', 'Balance', 'Opening_Date', 'Overdraft']
            Bs = []
            epy = [0, 0, 0, 0, 0, 0]
            if self.ui.nYEL.isChecked():
                epy[0] = 1
            if self.ui.nYEM.isChecked():
                epy[1] = 1
            if self.ui.nDateL.isChecked():
                epy[2] = 1
            if self.ui.nDateM.isChecked():
                epy[3] = 1
            if self.ui.nTZL.isChecked():
                epy[4] = 1
            if self.ui.nTZM.isChecked():
                epy[5] = 1
            for i in range(0, 2):
                if Vals[i] is not '':
                    Bs.append(Vats[i] + " = '" + Vals[i] + "'")
            for i in range (2, 8, 2):
                if epy[i - 2] == 1:
                    Bs.append(Vats[(i + 2) // 2] + " >= '" + Vals[i] + "'")
                if epy[i - 1] == 1:
                    Bs.append(Vats[(i + 2) // 2] + " <= '" + Vals[i + 1] + "'")
            if Vals[8] is not '':
                Bs.append("Account.Account_ID in (select Account_ID from Own where Client_ID = '" + Vals[8] + "')")

            st = ' and '
            sql = 'select * from Account, Checking_Account where Account.Account_ID = Checking_Account.Account_ID and ' + st.join(Bs) + ';'

            mtl = ['账户号', '支行名', '余额', '开户日期', '透支额', '操作']
            if len(Bs) > 0:
                dialog = StbZP(self, sql, mtl, '支票账户')
                dialog.exec_()

    def DeleteButton1(self):
        button = self.sender()
        if button:
            row = self.ui.tableck.indexAt(button.parent().pos()).row()
            tid = self.res1[row][0]
            rn2 = self.db.execute("select Bank_Name from Account where Account_ID = '" + tid + "';")

            self.db.execute("alter table Saving_Account drop constraint FK_Account_Type1;")
            self.db.execute("alter table Own drop constraint FK_Own2;")

            self.db.execute("delete from Account where Account_ID = '" + tid + "';")
            self.db.execute("delete from Saving_Account where Account_ID = '" + tid + "';")
            self.db.execute("delete from Own where Account_ID = '" + tid + "';")
            self.db.execute("delete from Checking where Client_ID in (select Client_ID from Own where Account_ID = '" + tid + "') and Bank_Name = '" + str(rn2[0][0]) + "' and Account_Type = 2")

            self.db.execute("alter table Saving_Account add constraint FK_Account_Type1 foreign key (Account_ID) references Account (Account_ID);")
            self.db.execute("alter table Own add constraint FK_Own2 foreign key (Account_ID) references Account (Account_ID);")
            self.renderTable1()

    def DeleteButton2(self):
        button = self.sender()
        if button:
            row = self.ui.tablezp.indexAt(button.parent().pos()).row()
            tid = self.res2[row][0]
            rn2 = self.db.execute("select Bank_Name from Account where Account_ID = '" + tid + "';")

            self.db.execute("alter table Checking_Account drop constraint FK_Account_Type2;")
            self.db.execute("alter table Own drop constraint FK_Own2;")

            self.db.execute("delete from Account where Account_ID = '" + tid + "';")
            self.db.execute("delete from Checking_Account where Account_ID = '" + tid + "';")
            self.db.execute("delete from Own where Account_ID = '" + tid + "';")
            self.db.execute("delete from Checking where Client_ID in (select Client_ID from Own where Account_ID = '" + tid + "') and Bank_Name = '" + str(rn2[0][0]) + "' and Account_Type = 2")

            self.db.execute("alter table Checking_Account add constraint FK_Account_Type2 foreign key (Account_ID) references Account (Account_ID);")
            self.db.execute("alter table Own add constraint FK_Own2 foreign key (Account_ID) references Account (Account_ID);")
            self.renderTable2()

