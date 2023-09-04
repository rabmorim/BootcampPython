saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

def contas( saldo , deposito , saque):
    saldo += deposito
    saldo -= saque
    return saldo
   

resultado = contas(saldo_atual, valor_deposito, valor_retirada)
print(f'Saldo atualizado na conta: {resultado:.1f}')