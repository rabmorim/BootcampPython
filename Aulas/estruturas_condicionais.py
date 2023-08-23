MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Digite sua idade: '))

if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar a habilitação')
elif idade == IDADE_ESPECIAL:
    print('Pode fazer as aulas teóricas, porém não as práticas')
else:
    print('Menor de idade, nao pode tirar a habilitação')