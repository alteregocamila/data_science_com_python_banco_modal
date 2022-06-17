# função que recebe a, b e c e entrega a solução x1 e x2 de uma equação de segundo grau (ax^2 + bx + c =0)
import re


def cls():
    import os
    os.system('cls')


def equacao2(a, b, c):
    d = b**2 - 4*a*c
    x1 = (-b + d**(1/2)) / (2*a)
    x2 = (-b - d**(1/2)) / (2*a)
    return {"x1": x1, "x2": x2}


cls()

coeficientes = []

for var in ['a', 'b', 'c']:
    while True:
        coe = input(f"Digite o coeficiente {var}: ")
        if not re.search("\d+", coe):
            print('Digite apenas números!')
        elif var == "a" and float(coe) == 0:
            print('O coeficiente "a" deve ser diferente de 0!')
        else:
            break

    coeficientes.append(float(coe))

a, b, c = coeficientes

raizes = equacao2(a, b, c)
print(f"\nRaiz x1 {raizes['x1']}\nRaiz x2 {raizes['x2']}\n")
