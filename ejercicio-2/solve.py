"""Ejercicio 2 
"""
import sys

INF = float("inf")


def costo_minimo(x, y, s):
    dp = {"C": 0, "J": 0}  
    primero = True
    for ch in s:
        opciones = "CJ" if ch == "?" else ch
        nuevo = {"C": INF, "J": INF}
        for c in opciones:
            if primero:
                nuevo[c] = 0
                continue
            for prev, val in dp.items():
                if val == INF:
                    continue
                extra = x if (prev, c) == ("C", "J") else y if (prev, c) == ("J", "C") else 0
                nuevo[c] = min(nuevo[c], val + extra)
        dp = nuevo
        primero = False
    return min(dp.values()) if s else 0


def main():
    lineas = sys.stdin.read().split("\n")
    t = int(lineas[0])
    out = []
    for caso in range(1, t + 1):
        partes = lineas[caso].split()
        x, y = int(partes[0]), int(partes[1])
        s = partes[2] if len(partes) > 2 else ""
        out.append(f"Case #{caso}: {costo_minimo(x, y, s)}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
