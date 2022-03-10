

from random import uniform

E = 0.00000001


def sqrt_(N):
    assert N >= 0
    r = uniform(0, N)
    while True:
        if abs(N - r*r) <= E:
            return r
        r = (r + N/r) / 2


def main():
    print("Introduza CTRL+C/D ou um número negativo para terminar")
    while True:
        num = float(input('raiz> '))
        if num < 0:
            break
        print(sqrt_(num))


if __name__ == '__main__':
    main()
        


