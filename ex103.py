
import csv

moedas = {}

with open("moedas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        sigla = linha[0]
        nome = linha[2]
        cotacao = float(linha[3])

        moedas[sigla] = {
            "nome": nome,
            "cotacao": cotacao
        }

valor = float(input("Digite o valor em R$: "))

print("\nMoedas disponíveis:")

for sigla, dados in moedas.items():
    print(sigla, "-", dados["nome"])

destino = input("\nDigite a sigla da moeda desejada: ").upper()

if destino in moedas:
    convertido = valor / moedas[destino]["cotacao"]

    print("\nMoeda:", moedas[destino]["nome"])
    print("Valor convertido: R$", round(convertido, 2))
else:
    print("Moeda não encontrada!")
