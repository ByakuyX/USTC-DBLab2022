# -*- coding: utf-8 -*-
import imp
from ui.UiMain import Ui_Menu
from PyQt5.QtWidgets import QMainWindow
from src.Login import LoginDialog
from src.CliTable import TablePage as KHT
from src.AccTable import TablePage as ZHT
from src.LoaTable import TablePage as DKT
from src.BuiTable import TablePage as YWT

class Menu(QMainWindow):
    ui = None
    db = None
    dbName = None

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.ui.Daikuan.setEnabled(False)
        self.ui.Zhanghu.setEnabled(False)
        self.ui.Kehu.setEnabled(False)
        self.ui.Yewu.setEnabled(False)
        self.ui.Daikuan.clicked.connect(self.DK)
        self.ui.Zhanghu.clicked.connect(self.ZH)
        self.ui.Kehu.clicked.connect(self.KH)
        self.ui.Yewu.clicked.connect(self.YW)
        self.ui.Denglu.clicked.connect(self.Login)
    
    def KH(self):
        a = KHT(self)
        a.exec_()

    def DK(self):
        a = DKT(self)
        a.exec_()

    def YW(self):
        a = YWT(self)
        a.exec_()

    def ZH(self):
        a = ZHT(self)
        a.exec_()

    def Login(self):
        dialog = LoginDialog(self)
        dialog.exec_()
        if self.db is not None:
            self.ui.Daikuan.setEnabled(True)
            self.ui.Zhanghu.setEnabled(True)
            self.ui.Kehu.setEnabled(True)
            self.ui.Yewu.setEnabled(True)
            self.ui.title.setText(self.dbName + " 已连接")
            self.ui.Denglu.setEnabled(False)
