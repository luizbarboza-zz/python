def CalcMedia():
    Notas = [5,7, 5, 8, 5,9, 9, 5,10, 5]
    Soma =0
    for i in range(0, 10, 1):
        Soma = Soma + Notas[i]
    return Soma / 10

med = CalcMedia()

