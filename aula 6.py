a = (input('Digite algo: '))

print('O tipo primitivo é ', type(a))
print(f'Oque você digitou é numerico?  ', {a.isnumeric()})
print(f'Oque você digitou é alfabetico? ', {a.isalpha()})
print('Oque voce digitou é alfanumerico?' ,{a.isalnum()})
