# exercicio 12
produto = input('Que produto você quer comprar?: ')
preço = float(input('Qual o preço do produto?: '))

print(f'Você comprou o produto {produto} e ganhou um desconto de 5%, o valor Final ficou: R${preço*0.95:.2f}')

# exercicio 13

print('------------------------------------------------')
print('RA, SUPER AUMENTO, AUMENTO DE 15% DO SEU SALARIO ')
print('------------------------------------------------')

salario = int(input('Qual o seu salario:'))
novo_salario = salario *1.15

print('----------------------------')
print(f'Seu novo salario com o aumento de 15% é :R${novo_salario:.2f}')
print(f'O aumento no seu salario foi de R${novo_salario-salario:.2f}')
