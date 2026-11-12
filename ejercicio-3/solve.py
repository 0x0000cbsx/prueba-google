"""Ejercicio 3 

"""
import sys


def asignar(actividades):
    orden = sorted(range(len(actividades)), key=lambda i: actividades[i])
    fin = {"C": 0, "J": 0}
    res = [""] * len(actividades)
    for i in orden:
        s, e = actividades[i]
        if fin["C"] <= s:
            quien = "C"
        elif fin["J"] <= s:
            quien = "J"
        else:
            return "IMPOSSIBLE"
        fin[quien] = e
        res[i] = quien
    return "".join(res)


def main():
    datos = sys.stdin.read().split()
    pos = 0
    t = int(datos[pos]); pos += 1
    out = []
    for caso in range(1, t + 1):
        n = int(datos[pos]); pos += 1
        acts = []
        for _ in range(n):
            acts.append((int(datos[pos]), int(datos[pos + 1])))
            pos += 2
        out.append(f"Case #{caso}: {asignar(acts)}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
