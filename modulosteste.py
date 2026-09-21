import math
import random
n = float(input('Digite um número: '))

print(f'O número inteiro é: {math.trunc(n)}')

cateto1 = int(input('Digite o lado do primeiro cateto:'))
cateto2 = int(input('Digite o lado do segundo cateto: '))

h = (cateto1**2) + (cateto2**2)
print(f'A hipotenusa é {math.sqrt(h):.2f}')

c = int(input('Digite o valor do angulo:'))

graus = math.radians(c)

print(f'Seno {math.sin(graus):.4f}, Cosceno {math.cos(graus):.4f}, Tangente {math.tan(graus):.4f}')


print('-------------')
a1 = input('Digite o nome do primeiro aluno:')
a2 = input('Digite o nome do segundo aluno:')
a3 = input('Digite o nome do terceiro aluno:')
a4 = input('Digite o nome do quarto aluno:')

lista = [a1, a2, a3, a4]

print('------------')
print('SORTEIO DE ALUNOS')
print('-------------')

random.shuffle(lista)

print(f'Os alunos são: {lista} e o escolhido para apagar o quadro foi o {random.choice(lista)}')

print(f'A ordem é {random.shuffle(lista)}')


