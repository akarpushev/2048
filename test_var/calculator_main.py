from PySide6 import QtWidgets, QtGui, QtCore
from test_var.calculator import Ui_Form
class Window(QtWidgets.QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #self.ui.equal.eventFilter()

        self.ui.n1.clicked.connect(lambda: self.input("1"))
        self.ui.n2.clicked.connect(lambda: self.input("2"))
        self.ui.n3.clicked.connect(lambda: self.input("3"))
        self.ui.n4.clicked.connect(lambda: self.input("4"))
        self.ui.n5.clicked.connect(lambda: self.input("5"))
        self.ui.n6.clicked.connect(lambda: self.input("6"))
        self.ui.n7.clicked.connect(lambda: self.input("7"))
        self.ui.n8.clicked.connect(lambda: self.input("8"))
        self.ui.n9.clicked.connect(lambda: self.input("9"))
        self.ui.n0.clicked.connect(lambda: self.input("0"))
        self.ui.plus.clicked.connect(lambda: self.input("+"))
        self.ui.minus.clicked.connect(lambda: self.input("-"))
        self.ui.multiply.clicked.connect(lambda: self.input("*"))
        self.ui.divide.clicked.connect(lambda: self.input("/"))
        self.ui.equal.clicked.connect(lambda: self.equal())
        self.ui.C.clicked.connect(lambda: self.delete())

    def input(self, number):
        self.ui.lineEdit.setText(self.ui.lineEdit.text() + number)

    def equal(self):
        self.ui.lineEdit.setText(str(eval(self.ui.lineEdit.text())))

    def delete(self):
        self.ui.lineEdit.clear()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.text() in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/'):
            self.input(event.text())
        elif event.text() in ('=', '\r'):
            self.equal()
        print(event.text())

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self.ui.equal:
            if event.type() == QtCore.QEvent.Type.Enter:
                print(f"Что-то произошло {event}")
        return super().eventFilter(watched, event)



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()