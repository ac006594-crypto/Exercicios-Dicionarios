
estados = {}

quantidade = int(input("Quantos estados deseja cadastrar? "))

for i in range(quantidade):
    nome = input("Digite o nome do estado: ")
    percentual = float(input("Digite o percentual: "))

    estados[nome] = percentual

print("\nEstados e seus respectivos percentuais:")

for estado, percentual in estados.items():
    print(estado, "-", percentual, "%")
