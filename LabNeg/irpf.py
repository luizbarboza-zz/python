
def IRPF(salario):
    if salario <= 1499.15:
        return 0
    elif salario > 1499.15 and salario <= 2246.75:
        return 7.5/100 * salario - 112.43
    elif salario > 2246.75 and salario <=2995.70:
        return 15/100 *salario - 280.94
    elif salario > 2995.70 and salario <= 3743.19:
        return 22.5/100*salario - 505.62
    else :
        return 27.5/100 * salario - 692.78

print(IRPF(5000))