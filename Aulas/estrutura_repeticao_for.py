texto = input("Informe um texto qualquer: ")
VOGAIS = "AEIOU"
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end ="")

print()    #adiciona uma quebra de linha