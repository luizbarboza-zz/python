def NotaConceito(nota):
    if nota >=9  :
        return "A"
    elif nota<9 and nota>=7:
        return "B"
    elif nota<7 and nota>=5 :
        return "D"
    else:
        return "F"

print(NotaConceito(6))
