from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_Dialog

print("starting app")
import sys

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
print("ending app")