# -*- coding: utf-8 -*-
import imp
from ui.UiLogin import Ui_LoginDialog
from PyQt5.QtWidgets import  QDialog
from src.Database import Database
from src.Message import information, critical


class LoginDialog(QDialog):
    ui = None
    db = None
    dbName = None
    parent = None

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)

        self.parent = parent

        # 绑定登陆按键
        self.ui.LoginBtn.clicked.connect(self.login)
   

    def login(self):
        ipaddr = 'localhost'
        dbname = 'db'
        username = self.ui.username.text()
        password = self.ui.password.text()

        self.db = Database()
        self.db.login(username, password, ipaddr, dbname)

        if self.db.isConnected():
            information(self, "登陆成功")
            self.dbName = dbname
            self.parent.db = self.db
            self.parent.dbName = self.dbName
            self.close()
        else:
            critical(self, "用户名或密码错误，登陆失败")
                   
   

