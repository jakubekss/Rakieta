from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QMessageBox
import sys
import math
import wzory

class Aplikacja(QWidget):
    def __init__(self):
        super(Aplikacja, self).__init__()
        
        self.interfejs()
        self.obliczenia()

    def interfejs(self):

        # etykiety
        etykieta1 = QLabel("Masa rakiety w [kg]", self)
        etykieta2 = QLabel("Średnica rakiety w [m]", self)
        etykieta3 = QLabel("Współczynnik oporu aerodynamicznego", self)
        etykieta4 = QLabel("Impuls silnika w [Ns]", self)
        etykieta5 = QLabel("Ciąg rakiety w [N]", self)
        etykieta6 = QLabel("Pułap na który wzniesie się rakieta w [m]", self)

        # przypisanie widgetów do układu tabeli
        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 1, 0)
        ukladT.addWidget(etykieta3, 2, 0)
        ukladT.addWidget(etykieta4, 3, 0)
        ukladT.addWidget(etykieta5, 4, 0)
        ukladT.addWidget(etykieta6, 5, 0)

        # 1-liniowe pola edycyjne
        self.masa = QLineEdit()
        self.srednica = QLineEdit()
        self.opor = QLineEdit()
        self.impuls = QLineEdit()
        self.ciag = QLineEdit()
        self.wynik = QLineEdit()
        
        self.wynik.setDisabled(True)
        
        self.masa.setToolTip('Wpisując masę używaj kropki')
        self.srednica.setToolTip('Wpisując średnicę używaj kropki')
        self.opor.setToolTip('Wpisując wspólczynnik oporu używaj kropki')

        ukladT.addWidget(self.masa, 0, 1)
        ukladT.addWidget(self.srednica, 1, 1)
        ukladT.addWidget(self.opor, 2, 1)
        ukladT.addWidget(self.impuls, 3, 1)
        ukladT.addWidget(self.ciag, 4, 1)
        ukladT.addWidget(self.wynik, 5, 1)

        # przyciski
        obliczBtn = QPushButton("&Oblicz", self)
        obliczBtn.clicked.connect(self.obliczenia)
        obliczBtn.resize(obliczBtn.sizeHint())

        zamknijBtn = QPushButton("&Zamknij", self)
        zamknijBtn.clicked.connect(quit)

        ukladT.addWidget(obliczBtn, 6, 0, 1, 2)
        ukladT.addWidget(zamknijBtn, 7, 1)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)
    

        self.resize(300, 150)
        self.setWindowTitle("Rakieta")
        self.show()
    
    def obliczenia(self):

        nadawca = self.sender()

        try:
            M = float(self.masa.text())
            d = float(self.srednica.text())
            Cd = float(self.opor.text())
            I = float(self.impuls.text())
            T = float(self.ciag.text())
            wynik = ""

            if nadawca.text() == "&Oblicz":        

                k = wzory.wspolczynnik_k(Cd, d)
                q = wzory.wspolczynnik_q(T, M, k)
                x = wzory.wspolczynnik_x(k, q, M)
                v = wzory.predkosc_max(I, T, q, x)
                hb = wzory.wysokosc_b(k, M, T, v)
                hc = wzory.wysokosc_c(k, M, v)

                wynik = hb + hc
            else:
                pass

            self.wynik.setText(str(wynik))

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Aplikacja = Aplikacja()
    sys.exit(app.exec_())