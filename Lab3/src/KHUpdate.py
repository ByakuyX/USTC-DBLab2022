# -*- coding: utf-8 -*-
from ui.UiKUP import Ui_LoginDialog
from PyQt5.QtWidgets import QDialog
from src.Message import critical

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
        Vats = ['Client_ID', 'Client_Name', 'Client_Tel', 'Client_Address', 'Contact_Name', 'Contact_Tel', 'Contact_Email', 'Relation']
        Vals.append(self.ui.Id.text().replace("'", "''"))
        Vals.append(self.ui.Name.text().replace("'", "''"))
        Vals.append(self.ui.Tel.text().replace("'", "''"))
        Vals.append(self.ui.Addr.text().replace("'", "''"))
        Vals.append(self.ui.CName.text().replace("'", "''"))
        Vals.append(self.ui.CEm.text().replace("'", "''"))
        Vals.append(self.ui.CTel.text().replace("'", "''"))
        Vals.append(self.ui.Rel.text().replace("'", "''"))
        epy = [0, 0, 0, 0, 0, 0, 0, 0]
        if self.ui.nId.isChecked():
            epy[0] = 1
        if self.ui.nName.isChecked():
            epy[1] = 1
        if self.ui.nTel.isChecked():
            epy[2] = 1
        if self.ui.nAddr.isChecked():
            epy[3] = 1
        if self.ui.nCName.isChecked():
            epy[4] = 1
        if self.ui.nCEm.isChecked():
            epy[5] = 1
        if self.ui.nCTel.isChecked():
            epy[6] = 1
        if self.ui.nRel.isChecked():
            epy[7] = 1
        res = self.db.execute("select count(*) from Client where Client_ID = '" + Vals[0] + "';")
        if res[0][0] > 0 and epy[0] == 1:
            critical(self, "身份证号不能重复或与原身份证号相同")
        elif Vals[0] is '' and epy[0] == 1:
            critical(self, "身份证号不能为空")
        elif Vals[1] is '' and epy[1] == 1:
            critical(self, "姓名不能为空")
        elif Vals[4] is '' and epy[4] == 1:
            critical(self, "联系人姓名不能为空")
        else:
            for i in range(1, 8):
                if epy[i] == 1:
                    if Vals[i] is not '':
                        self.db.execute("update Client set " + Vats[i] + " = '" + Vals[i] + "' where Client_ID = '" + self.IDf + "';")
                    else:
                        self.db.execute("update Client set " + Vats[i] + " = null where Client_ID = '" + self.IDf + "';")
            if epy[0] == 1:
                self.db.execute("alter table own drop constraint fk_own1;")
                self.db.execute("alter table bear drop constraint fk_bear1;")
                self.db.execute("alter table checking drop constraint fk_checking1;")
                self.db.execute("alter table Service drop constraint FK_Service;")
                self.db.execute("update Client set Client_ID = '" + Vals[0] + "' where Client_ID = '" + self.IDf + "';")
                self.db.execute("update Own set Client_ID = '" + Vals[0] + "' where Client_ID = '" + self.IDf + "';")
                self.db.execute("update Bear set Client_ID = '" + Vals[0] + "' where Client_ID = '" + self.IDf + "';")
                self.db.execute("update Checking set Client_ID = '" + Vals[0] + "' where Client_ID = '" + self.IDf + "';")
                self.db.execute("update Service set Client_ID = '" + Vals[0] + "' where Client_ID = '" + self.IDf + "';")
                self.db.execute("alter table Own add constraint FK_Own1 foreign key (Client_ID) references Client (Client_ID);")
                self.db.execute("alter table Bear add constraint FK_Bear1 foreign key (Client_ID) references Client (Client_ID);")
                self.db.execute("alter table Checking add constraint FK_Checking1 foreign key (Client_ID) references Client (Client_ID);")
                self.db.execute("alter table Service add constraint FK_Service foreign key (Client_ID) references Client (Client_ID);")
                #print("insert into Client values(" + st.join(Bas) + ")")
            self.close()

    def eb(self):
        self.close()



         
   

