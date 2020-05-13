import math

def wspolczynnik_k(Cd, d):
    # rho - gęstość powietrza w kg/m^3
    rho = 1.2
    # A - pole powierzchni rakiety w m^2
    A = math.pi * (0.5 * d)**2
    k = 0.5 * rho * Cd * A
    
    return k

def wspolczynnik_q(T, M, k):
    # g - przyśpieszenie grawitacyjne m/s^2
    g = 9.81
    q = math.sqrt((T - M*g)/k)
    
    return q

def wspolczynnik_x(k, q, M):
    x = (2 * k * q) / M
    
    return x

def predkosc_max(I, T, q, x):
    # t - czas pracy silnika
    t = I/T
    v = q * (1-math.exp(-x*t))/(1+math.exp(-x*t))

    return v

def wysokosc_b(k, M, T, v):
    # g - przyśpieszenie grawitacyjne m/s^2
    g = 9.81
    hb = (-M/(2*k)) * math.log10((T - M*g - k*v**2)/(T - M*g))

    return hb

def wysokosc_c(k, M, v):
    # g - przyśpieszenie grawitacyjne m/s^2
    g = 9.81
    hc = (M/(2*k)) * math.log10((M*g + k*v**2)/(M*g))

    return hc
