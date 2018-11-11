
def MaiorNota():
    Notas = [5,7, 5, 8, 5,9, 9, 5,9, 5]
    Maior = 0
    for i in range(0,10,1):
        if Notas[i] > Maior:
            Maior = Notas[i]
    return Maior

print(MaiorNota())

