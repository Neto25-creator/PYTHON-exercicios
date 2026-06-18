# Crie um módulo matematica.py com funções utilitárias (mdc, mmc, potência, raiz) e importe-as em outro script.

import math

def potencia(base, expoente):
    return base ** expoente

def raiz(numero):
    return numero ** 0.5

def mdc(a, b):
    return math.gcd(a, b)

def mmc(a, b):
    return abs(a * b) // math.gcd(a, b)