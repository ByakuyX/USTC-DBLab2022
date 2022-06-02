# -*- coding: UTF-8 -*-
from PyQt5.QtWidgets import QMessageBox


def information(self, alarm):
    self.alarm = alarm
    QMessageBox.information(self, '提示', self.alarm, QMessageBox.Ok)

def critical(self, alarm):
    self.alarm = alarm
    QMessageBox.critical(self, '错误', self.alarm, QMessageBox.Ok)
