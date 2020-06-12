# This Python file uses the following encoding: utf-8
import sys
import shiboken2
from PySide2.QtWidgets import (QApplication)
from MainView import MainView
import logging

if __name__ == "__main__":
    app = QApplication([])
    logging.basicConfig(filename='../log/EaraQuake.log', level=logging.WARNING)
    window = MainView(_app=app)
    window.show()
    sys.exit(app.exec_())
