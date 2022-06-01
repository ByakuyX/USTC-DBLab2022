# -*- coding: utf-8 -*-
from ui.DKIn import Ui_LoginDialog
from PyQt5.QtWidgets import QDialog
from src.Message import critical

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
        Vals.append(self.ui.Loan_ID.text())
        Vals.append(self.ui.Bank_Name.text())
        Vals.append(self.ui.Loan_Amount.text())
        Vals.append('0')
        Vals.append('未发放')
        Clis = self.ui.Owners.document().toPlainText().split('\n')
        Clis = list(set(Clis))
        #**为空，**账户号重复，**银行不存在，**持有者不存在
        res1 = self.db.execute("select count(*) from Loan where Loan_ID = '" + Vals[0] + "';")
        res2 = self.db.execute("select count(*) from Bank where Bank_name = '" + Vals[1] + "';")
        if Vals[0] is '':
            critical(self, "贷款号不能为空")
            flag = False
        elif res1[0][0] > 0:
            critical(self, "贷款号不能重复")
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
                if res3[0][0] < 1:
                    critical(self, "客户 " + cli + " 不存在")
                    flag = False
                    break

        # **账户，**持有
        if flag:
            st = "', '"
            self.db.execute("insert into Loan values('" + st.join(Vals) + "');")
            for cli in Clis:
                if cli is '':
                    continue
                self.db.execute("insert into Bear values('" + cli + "', '" + Vals[0] + "');")
            self.parent.renderTable()

    def eb(self):
        self.close()



         
   

