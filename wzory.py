import math

def wspolczynnik_k(Cd, d):
    # rho - gęstość powietrza w kg/m^3
    rho = 1.2
    # A - pole powierzchni rakiety w m^2
    A = math.pi * (0.5 * d)**2
    k = 0.5 * rho * Cd * A
    
    return k

def wspolczynnik_q(T, M):
    # g - przyśpieszenie grawitacyjne m/s^2
    g = 9.81
    q = math.sqrt((T - M*g)/k)
    
    return q

def wspolczynnik_x(M):
    x = (2 * k * q) / M
    
    return x