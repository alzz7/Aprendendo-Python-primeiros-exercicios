dias = int(input('Quantos dias alugados?:'))
km = int(input('Quantos Km rodados:'))

valor = (dias*60) + (km*0.15)

print(f'O valor total a pagar é de: R${valor}')
