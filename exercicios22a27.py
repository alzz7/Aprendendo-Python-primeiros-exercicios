nome = input('Digite seu nome completo:')

print(f'Maiusculo:{nome.upper()}')
print(f'Minusculo:{nome.lower()}')
print(f'Letras sem espaço {len(nome.replace(' ', ''))}')
print(f'O primeiro nome tem {len(nome.split()[0])} letras')

# exercicio 23
numero = input('Digite um número de 4 digitos:')

print(f'unidade: {numero[3]}')
print(f'dezena: {numero[2]}')
print(f'centena: {numero[1]}')
print(f'milhar: {numero[0]}')

#exercicio 24
cidade = input('Digite o nome da sua Cidade:')
cidade = cidade.lower().split()[0]

print(cidade)
print(f'Tem a palavra santo?: {'santo' in cidade}')

# exercicio 25
nomecompleto = input('Digite o seu nome:')
nomecompleto = nomecompleto.lower()

print(f'Tem a palavra silva no nome?: {'silva' in nomecompleto}')

#exercicio 26

frase = input('Digite uma frase: ')

frase = frase.lower()

print(f'Apareceram {frase.count('a')} vezes o A, a primeira vez que ele aparece é na posição {frase.find('a')} e a ultima vez foi na posição {frase.rfind('a')}')

# exercicio 27

nomepessoa = input('Digite o nome Completo: ')

print(f'O primeiro nome é {nomepessoa.rsplit()[0]} o ultimo nome é {nomepessoa.split()[-1]}')




