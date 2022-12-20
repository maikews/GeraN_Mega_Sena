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

resultado = [4,23,44,12,56,60]
def conferir(jogo):
    acertos = 0
    for i in jogo:
        if i in resultado:
            acertos += 1
    if acertos >= 4:
        print("###################")
    acertos = 0

if __name__ == '__main__':
    volante.append([4, 23, 44, 12, 56, 60])
    for i in range(2332):
        montar(6)
    #print(volante)
    #print(len(volante))
    for i in volante:
        print(i)
        conferir(i)