# -*- coding: utf-8 -*-
from ui.ZHUpZP import Ui_LoginDialog
from PyQt5.QtWidgets import QDialog
from src.Message import critical

class LoginDialog(QDialog):
    ui = None
    db = None
    parent = None
    IDf = None
    bank = None

    def __init__(self, parent, IDf) -> None:
        super().__init__(parent)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.db = parent.db
        self.parent = parent
        self.IDf = IDf
        bak = self.db.execute("select Bank_Name from Account where Account_ID = '" + self.IDf + "';")
        self.bank = bak[0][0]
        # 绑定登陆按键
        self.ui.OB.clicked.connect(self.ob)
        self.ui.EB.clicked.connect(self.eb)
    

    def ob(self):
        Vals = []
        Vats = ['Bank_Name', 'Balance', 'Opening_Date', 'Overdraft']
        Vals.append(self.ui.Bank_Name.text())
        Vals.append(self.ui.Balance.text())
        Vals.append(self.ui.Opening_Date.text())
        Vals.append(self.ui.Overdraft.text())
        epy = [0, 0, 0, 0]
        if self.ui.nBank_Name.isChecked():
            epy[0] = 1
        if self.ui.nBalance.isChecked():
            epy[1] = 1
        if self.ui.nOpening_Date.isChecked():
            epy[2] = 1
        if self.ui.nOverdraft.isChecked():
            epy[3] = 1

        res1 = self.db.execute("select count(*) from Checking where Account_Type = '2' and Bank_Name = '" + Vals[0] + "' and Client_ID in (select Client_ID from Own where Account_ID = '" + self.IDf + "');")
        res2 = self.db.execute("select count(*) from Bank where Bank_Name = '" + Vals[0] + "';")
        if res1[0][0] > 0 and epy[0] == 1:
            critical(self, "此账户的持有者之一已在该银行持有支票账户")
        elif Vals[0] is '' and epy[0] == 1:
            critical(self, "支行名不能为空")
        elif res2[0][0] < 1 and epy[0] == 1:
            critical(self, "此支行不存在")
        else:
            for i in range(1, 3):
                if epy[i] == 1:
                    self.db.execute("update Account set " + Vats[i] + " = '" + Vals[i] + "' where Account_ID = '" + self.IDf + "';")
            for i in range(3, 4):
                if epy[i] == 1:
                    if Vals[i] is not '':
                        self.db.execute("update Checking_Account set " + Vats[i] + " = '" + Vals[i] + "' where Account_ID = '" + self.IDf + "';")
                    else:
                        self.db.execute("update Checking_Account set " + Vats[i] + " = null where Account_ID = '" + self.IDf + "';")
            if epy[0] == 1:
                self.db.execute("alter table Checking drop constraint FK_Checking2;")
                self.db.execute("update Checking set Bank_Name = '" + Vals[0] + "' where Account_Type = '1' and Bank_Name = '" + self.bank + "' and Client_ID in (select Client_ID from Own where Account_ID = '" + self.IDf + "');")
                self.db.execute("alter table Checking add constraint FK_Checking2 foreign key (Bank_Name) references Bank (Bank_Name);")
                self.db.execute("alter table Account drop constraint FK_Open;")
                self.db.execute("update Account set Bank_Name = '" + Vals[0] + "' where Account_ID = '" + self.IDf + "';")
                self.db.execute("alter table Account add constraint FK_Open foreign key (Bank_Name) references Bank (Bank_Name);")
                #print("insert into Client values(" + st.join(Bas) + ")")
            self.close()

    def eb(self):
        self.close()



         
   

