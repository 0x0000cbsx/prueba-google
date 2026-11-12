"""Ejercicio 5 

Uso: python solve.py < entrada.txt


"""
import sys
from collections import defaultdict


def ultima_persona(n, k):
    tramos = defaultdict(int)
    tramos[n] = 1
    while True:
        x = max(tramos)
        cuantos = tramos.pop(x)
        izq, der = (x - 1) // 2, x // 2
        if k <= cuantos:
            return der, izq  # max, min
        k -= cuantos
        tramos[der] += cuantos
        tramos[izq] += cuantos


def main():
    datos = sys.stdin.read().split()
    t = int(datos[0])
    out = []
    for caso in range(1, t + 1):
        n, k = int(datos[2 * caso - 1]), int(datos[2 * caso])
        mx, mn = ultima_persona(n, k)
        out.append(f"Case #{caso}: {mx} {mn}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
