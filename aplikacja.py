from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
import sys

class Aplikacja(QWidget):
    def __init__(self):
        super(Aplikacja, self).__init__()
        self.interfejs()

    def interfejs(self):

        # etykiety
        etykieta1 = QLabel("Masa rakiety w kg", self)
        etykieta2 = QLabel("Średnica rakiety w m", self)
        etykieta3 = QLabel("Współczynnik oporu rakiety", self)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 1, 0)
        ukladT.addWidget(etykieta3, 2, 0)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        self.resize(300, 100)
        self.setWindowTitle("Rakieta")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Aplikacja = Aplikacja()
    sys.exit(app.exec_())