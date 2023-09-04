ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# Ordenação em ordem alfabéticas

def ordenando(ativos):
    ativos.sort()
    return ativos

resultado = ordenando(ativos)

for x in resultado:
    print(x, end="\n")