def Aprovacao(nota, freq):
    if nota>=7 and freq >= 0.75:
        return "Aprovado"
    else:
        return "Reprovado"

print(Aprovacao(9,1))

