def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print(f"Valor de {valor} foi sacado" )
        saldo -= valor


sacar(100)