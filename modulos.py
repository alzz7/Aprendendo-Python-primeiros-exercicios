from math import sqrt
n = int(input('Digite um número:'))
raiz = sqrt(n)
a = n*2+1.05
print(f'A raiz é {raiz:.2f}, O valor de A é:{a} ,Arredondado cima {math.ceil(a)}, Pra baixo {math.floor(a)}, inteiro {math.trunc(a)}')