from PyQt5.QtWidgets import QApplication, QWidget
import sys

class Aplikacja(QWidget):
    def __init__(self):
        super(Aplikacja, self).__init__()
        self.interfejs()

    def interfejs(self):

        self.resize(300, 300)
        self.setWindowTitle("Rakieta")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Aplikacja = Aplikacja()
    sys.exit(app.exec_())