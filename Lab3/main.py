from src.Menu import Menu
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = Menu()
    a.show()
    sys.exit(app.exec_())
