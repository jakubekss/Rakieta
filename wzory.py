import math

def wspolczynnik_k(Cd, d):
    # rho - gęstość powietrza w kg/m^3
    rho = 1.2
    # A - pole powierzchni rakiety w m^2
    A = math.pi * (0.5 * d)**2
    k = 0.5 * rho * Cd * A

    return k