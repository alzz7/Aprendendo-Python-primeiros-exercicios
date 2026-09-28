n1 = int(input('Digite a idade do primeiro aluno:'))
n2 = int(input('Digite a idade do segundo aluno: '))
n3 = int(input('Digite a idade do terceiro aluno: '))
n4 = int(input('Digite a idade do quarto aluno: '))

frase = 'Alz é o 00'

idade = [n1, n2, n3, n4]

print('As idade respectivamente digitadas foram:', idade)
print(frase[0:3])
print(idade[0])
print(len(frase))

palavra = 'Presidente Lula decreta fim das Bets'

print(f'A quantidade de letras E da frase {palavra} é {palavra.count('e')}, a quantidade de caracteres é {len(palavra)}')
print(f'Lula está na posição {palavra.find('Lula')}, existe a palavra Cão na frase? {'Cão' in palavra} e a palavra Lula? {'Lula' in palavra}')

print(f'A frase maiuscula é {frase.upper()} e em minusculo {frase.lower()}')
print(f'Split indice 0 da frase:{frase} é: {frase.split()[0]}')

print(palavra.replace('Lula', 'Bolso'))
print(frase.find('alz'))
print(frase.lower().find('alz'))