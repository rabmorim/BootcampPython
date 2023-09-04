# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

def contas(saldo , saque):
    if saldo >= saque:
        saldo -= saque
        print(f'Saque Realizado com Sucesso. Novo saldo: {saldo}')
    else:
        print('Saldo insuficiente. Saque nao realizado!')


contas(saldo_total, valor_saque)

