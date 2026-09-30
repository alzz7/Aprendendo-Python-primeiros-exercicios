from math import ceil, floor, sqrt, trunc
import emoji
n = int(input('Digite um número:'))
raiz = sqrt(n)
a = n*2+1.05
print(f'A raiz é {raiz:.2f}, O valor de A é:{a} ,Arredondado cima {ceil(a)}, Pra baixo {floor(a)}, inteiro {trunc(a)}')
print(emoji.emojize('Python :thumbs_up:'))