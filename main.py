import random

volante = []


def rolar():
    return random.randint(1, 60)


def montar(n):
    lista = []
    while n > 0:
        numero = rolar()
        if numero not in lista:
            lista.append(numero)
            n -= 1
    lista.sort(reverse=False)
    volante.append(lista)


if __name__ == '__main__':
    montar(6)
    print(volante)
