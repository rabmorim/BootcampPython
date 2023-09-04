valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

def juros_compostos( valor , taxa , periodo):
    resultado = valor*( taxa + 1) **periodo
    return resultado

resultado = juros_compostos(valor_inicial, taxa_juros, periodo)
print(f'Valor final do investimento: R${resultado:.2f}')