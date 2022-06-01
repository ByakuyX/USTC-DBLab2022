# -*- coding: utf-8 -*-
from ui.UiYW import Ui_Dialog
from PyQt5 import QtWidgets as Qtt
from datetime import date
from PyQt5 import QtCore
from decimal import Decimal

class TablePage(Qtt.QDialog):
    ui = None
    db = None
    dbName = None
    parent = None
    res = None
    bank = None
    box = [None, None, None, None]

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.db = parent.db
        self.dbName = parent.dbName
        self.box = ['select year(opening_date) as y, ',
                    'select year(pay_date) as y, ',
                    ' group by y;', 'y']
        self.initLayout()
        self.initBinding()

    def initLayout(self):
        self.ui.label.setText(self.dbName + " - 业务统计 - 请选择支行")

        self.ui.table.setColumnCount(5)
        self.ui.table.setHorizontalHeaderLabels(['时间', '储蓄金额', '储蓄客户人次', '贷款金额', '贷款客户人次'])
        self.ui.table.horizontalHeader().setSectionResizeMode(Qtt.QHeaderView.Stretch)
        self.ui.table.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;}")

        items = self.db.execute("select Bank_Name from Bank;")
        for item in items:
            self.ui.list.addItem(item[0])

    def initBinding(self):
        self.ui.list.itemClicked.connect(self.listclick)
        self.ui.box.currentIndexChanged.connect(self.boxclick)

    def listclick(self, item):
        self.ui.label.setText(self.dbName + " - 业务统计 - " + item.text())
        self.bank = "'" + item.text() + "'"
        self.renderTable()

    def boxclick(self):
        if self.ui.box.currentText() == '年度统计':
            self.box = ['select year(opening_date) as y, ',
                        'select year(pay_date) as y, ',
                        ' group by y;', 'y']
        elif self.ui.box.currentText() == '季度统计':
            self.box = ['select year(opening_date) as y, quarter(opening_date) as q, ',
                        'select year(pay_date) as y, quarter(pay_date) as q, ',
                        ' group by y, q;', 'q']
        else:
            self.box = ['select year(opening_date) as y, month(opening_date) as m, ',
                        'select year(pay_date) as y, month(pay_date) as m, ',
                        ' group by y, m;', 'm']
        self.renderTable()

    def renderTable(self):
        self.ui.table.setRowCount(0)
        currentRowCount = self.ui.table.rowCount()
        list = [None, None, None, None]
        list[0] = self.db.execute(self.box[0] + "sum(balance) from account where account_id in (select account_id from saving_account) and bank_name = " + self.bank + self.box[2])
        list[1] = self.db.execute(self.box[0] + "count(client_id) from own, account where account.account_id = own.account_id and account.account_id in (select account_id from saving_account) and bank_name = " + self.bank + self.box[2])
        list[2] = self.db.execute(self.box[1] + "sum(pay_amount) from pay where loan_id in (select loan_id from loan where bank_name = " + self.bank + ")" + self.box[2])
        list[3] = self.db.execute(self.box[1] + "count(client_id) from bear, pay where bear.loan_id = pay.loan_id and pay.loan_id in (select loan_id from loan where bank_name = " + self.bank + ")" + self.box[2])
        tab = []
        for i in range(0, 4):
            for ls in list[i]:
                if self.box[3] == 'y':
                    tmp = date(ls[0], 1, 1)
                else:
                    tmp = date(ls[0], ls[1], 1)
                if tmp not in tab:
                    tab.append(tmp)
        tab = [[x, '', '', '', ''] for x in tab]
        for tas in tab:
            for i in range(0, 4):
                for ls in list[i]:
                    if self.box[3] == 'y':
                        tmp = date(ls[0], 1, 1)
                    else:
                        tmp = date(ls[0], ls[1], 1)
                    if tas[0] == tmp:
                        if i == 1 or i == 3:
                            tas[i + 1] = str(ls[-1])
                        else:
                            tas[i + 1] = str(Decimal(ls[-1]).quantize(Decimal("0.00")))
        if len(tab) > 0:
            tab = [value for index, value in sorted(enumerate(tab), key=lambda tab: tab[1])]
            for ro in tab:
                item = []
                self.ui.table.insertRow(currentRowCount)
                tmp = str(ro[0]).split('-')
                if self.box[3] == 'y':
                    ro[0] = tmp[0] + ' 年'
                elif self.box[3] == 'q':
                    ro[0] = tmp[0] + ' 年 ' + tmp[1] + ' 季度'
                else:
                    ro[0] = tmp[0] + ' 年 ' + tmp[1] + ' 月'
                for i in range(0, len(ro)):
                    item.append(Qtt.QTableWidgetItem(ro[i]))
                    item[i].setTextAlignment(QtCore.Qt.AlignCenter)
                    self.ui.table.setItem(currentRowCount, i, item[i])
                currentRowCount += 1
                self.ui.table.setRowCount(currentRowCount)
                self.ui.table.setEditTriggers(Qtt.QTableWidget.NoEditTriggers)
                self.ui.table.setSelectionMode(Qtt.QAbstractItemView.NoSelection)

