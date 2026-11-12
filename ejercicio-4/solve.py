"""Ejercicio 4 

Uso: python solve.py < entrada.txt

"""
import sys


def diversion_total(f, p):
    n = len(f)
    hijos = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        hijos[p[i - 1]].append(i)

    valor = [0] * (n + 1)
    total = 0
    for i in range(n, 0, -1):
        if not hijos[i]:
            valor[i] = f[i - 1]
        else:
            vals = [valor[h] for h in hijos[i]]
            m = min(vals)
            total += sum(vals) - m
            valor[i] = max(f[i - 1], m)
        if p[i - 1] == 0:
            total += valor[i]
    return total


def main():
    datos = sys.stdin.read().split()
    pos = 0
    t = int(datos[pos]); pos += 1
    out = []
    for caso in range(1, t + 1):
        n = int(datos[pos]); pos += 1
        f = list(map(int, datos[pos:pos + n])); pos += n
        p = list(map(int, datos[pos:pos + n])); pos += n
        out.append(f"Case #{caso}: {diversion_total(f, p)}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
