# -*- coding: utf-8 -*-
from ui.ZHInCK import Ui_LoginDialog
from PyQt5.QtWidgets import QDialog
from src.Message import critical
from datetime import date

class LoginDialog(QDialog):
    ui = None
    db = None
    parent = None

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.db = parent.db
        self.parent = parent

        # 绑定登陆按键
        self.ui.OB.clicked.connect(self.ob)
        self.ui.EB.clicked.connect(self.eb)
    

    def ob(self):
        flag = True
        Vals = []
        Vats = ['Account_ID', 'Bank_Name', 'Balance', 'Opening_Date', 'Interest_Rate', 'Currency_Type', 'Client_ID']
        Vals.append(self.ui.Account_ID.text().replace("'", "''"))
        Vals.append(self.ui.Bank_Name.text().replace("'", "''"))
        Vals.append(self.ui.Balance.text().replace("'", "''"))
        if self.ui.nOpening_Date.isChecked():
            Vals.append(self.ui.Opening_Date.text().replace("'", "''"))
        else:
            Vals.append(str(date.today()))
        Vals.append(self.ui.Interest_Rate.text().replace("'", "''"))
        Vals.append(self.ui.Currency_Type.text().replace("'", "''"))
        Clis = self.ui.Owners.document().toPlainText().replace("'", "''").split('\n')
        Clis = list(set(Clis))
        # **非空为空，**账户号重复，**银行不存在，**持有者不存在，**判定失败
        res1 = self.db.execute("select count(*) from Account where Account_ID = '" + Vals[0] + "';")
        res2 = self.db.execute("select count(*) from Bank where Bank_name = '" + Vals[1] + "';")
        if Vals[0] is '':
            critical(self, "账户号不能为空")
            flag = False
        elif res1[0][0] > 0:
            critical(self, "账户号不能重复")
            flag = False
        elif Vals[1] is '':
            critical(self, "支行不能为空")
            flag = False
        elif res2[0][0] < 1:
            critical(self, "该支行不存在")
            flag = False
        else:
            for cli in Clis:
                if cli is '':
                    continue
                res3 = self.db.execute("select count(*) from Client where Client_ID = '" + cli + "';")
                res4 = self.db.execute("select count(*) from Checking where Client_ID = '" + cli + "' and Bank_Name = '" + Vals[1] + "' and Account_Type = 1;")
                if res3[0][0] < 1:
                    critical(self, "客户 " + cli + " 不存在")
                    flag = False
                    break
                elif res4[0][0] > 0:
                    critical(self, "客户 " + cli + " 在此支行内已经开设有存款账户")
                    flag = False
                    break

        # **账户，**支票账户，**持有，**判定
        if flag:
            st = ', '
            Bas1 = ["'" + Vals[0] + "'"]
            Bat1 = [Vats[0]]
            for i in range(1, 4):
                if Vals[i] is not '':
                    Bas1.append("'" + Vals[i] + "'")
                    Bat1.append(Vats[i])
            self.db.execute("insert into Account(" + st.join(Bat1) + ") values(" + st.join(Bas1) + ");")
            Bas2 = ["'" + Vals[0] + "'"]
            Bat2 = [Vats[0]]
            if Vals[4] is not '' and self.ui.nInterest_Rate.isChecked():
                Bas2.append("'" + Vals[4] + "'")
                Bat2.append(Vats[4])
            if Vals[5] is not '':
                Bas2.append("'" + Vals[5] + "'")
                Bat2.append(Vats[5])
            self.db.execute("insert into Saving_Account(" + st.join(Bat2) + ") values(" + st.join(Bas2) + ");")
            for cli in Clis:
                if cli is '':
                    continue
                self.db.execute("insert into Own values('" + cli + "', '" + Vals[0] + "', '" + Vals[3] + "');")
                self.db.execute("insert into Checking values('" + cli + "', '" + Vals[1] + "', '1');")
            self.parent.renderTable1()

    def eb(self):
        self.close()

