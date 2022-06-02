# -*- coding: utf-8 -*-
from ui.UiKIS import Ui_LoginDialog
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
        Vals = []
        Vats = ['Client_ID', 'Client_Name', 'Client_Tel', 'Client_Address', 'Contact_Name', 'Contact_Email', 'Contact_Tel', 'Relation']
        Vals.append(self.ui.Id.text().replace("'", "''"))
        Vals.append(self.ui.Name.text().replace("'", "''"))
        Vals.append(self.ui.Tel.text().replace("'", "''"))
        Vals.append(self.ui.Addr.text().replace("'", "''"))
        Vals.append(self.ui.CName.text().replace("'", "''"))
        Vals.append(self.ui.CTel.text().replace("'", "''"))
        Vals.append(self.ui.CEm.text().replace("'", "''"))
        Vals.append(self.ui.Rel.text().replace("'", "''"))
        res = self.db.execute("select count(*) from Client where Client_ID = '" + Vals[0] + "';")
        if Vals[0] is '':
            critical(self, "身份证号不能为空")         
        elif Vals[1] is '':
            critical(self, "姓名不能为空")
        elif Vals[4] is '':
            critical(self, "联系人姓名不能为空")
        elif res[0][0] > 0:
            critical(self, "身份证号不能重复")
        else:
            Bas = []
            Bat = []
            for i in range(0, 8):
                if Vals[i] is not '':
                    Bas.append("'" + Vals[i] + "'")
                    Bat.append(Vats[i])
            st = ', '
            #print("insert into Client values(" + st.join(Bas) + ")")
            self.db.execute("insert into Client(" + st.join(Bat) + ") values(" + st.join(Bas) + ");")
            self.parent.renderTable()

    def eb(self):
        self.close()
        



         
   

