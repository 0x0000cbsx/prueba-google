"""Ejercicio 1 

Uso: python solve.py < entrada.txt
"""
import sys


def escalera(caras):
    largo = 0
    for s in sorted(caras):
        if s > largo:
            largo += 1
    return largo


def main():
    datos = sys.stdin.read().split()
    pos = 0
    t = int(datos[pos]); pos += 1
    out = []
    for caso in range(1, t + 1):
        n = int(datos[pos]); pos += 1
        caras = list(map(int, datos[pos:pos + n])); pos += n
        out.append(f"Case #{caso}: {escalera(caras)}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
