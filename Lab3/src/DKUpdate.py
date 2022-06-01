# -*- coding: utf-8 -*-
from ui.DKUp import Ui_LoginDialog
from PyQt5.QtWidgets import QDialog
from src.Message import critical
from datetime import date

class LoginDialog(QDialog):
    ui = None
    db = None
    parent = None
    IDf = None

    def __init__(self, parent, IDf) -> None:
        super().__init__(parent)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)
        self.db = parent.db
        self.parent = parent
        self.IDf = IDf
        # 绑定登陆按键
        self.ui.OB.clicked.connect(self.ob)
        self.ui.EB.clicked.connect(self.eb)
    

    def ob(self):
        Vals = []
        Vals.append(self.ui.ID.text())
        Vals.append(self.IDf)
        Vals.append(self.ui.Amount.text())
        if self.ui.nDate.isChecked():
            Vals.append(self.ui.Date.text())
        else:
            Vals.append(str(date.today()))
        #**ID空/重复，金额过大
        res1 = self.db.execute("select count(*) from Pay where Pay_ID = '" + Vals[0] + "';")[0][0]
        preamt = self.db.execute("select Pay_already from Loan where Loan_ID = '" + self.IDf + "';")[0][0]
        maxamt = self.db.execute("select Loan_Amount from Loan where Loan_ID = '" + self.IDf + "';")[0][0]
        if Vals[0] is '':
            critical(self, "发放编号不能为空")
        elif res1 > 0:
            critical(self, "发放编号不能重复")
        elif preamt + float(Vals[2]) >= maxamt + 0.009:
            critical(self, "发放金额不能超过贷款额度")
        else:
            st = "', '"
            self.db.execute("insert into Pay values('" + st.join(Vals) + "');")
            nowamt = preamt + float(Vals[2])
            if nowamt <= maxamt - 0.009:
                self.db.execute("update Loan set Loan_Status = '发放中', Pay_already = '" + str(nowamt) + "' where Loan_ID = '" + self.IDf + "';")
            else:
                self.db.execute("update Loan set Loan_Status = '已发放', Pay_already = '" + str(maxamt) + "' where Loan_ID = '" + self.IDf + "';")
            self.close()

    def eb(self):
        self.close()



         
   

