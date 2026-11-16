
menores = []
maiores = []

for i in range(10):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input("Digite a idade: "))

    pessoa = (nome, idade)

    if idade < 18:
        menores.append(pessoa)
    else:
        maiores.append(pessoa)

print("\nPessoas com menos de 18 anos:")
for pessoa in menores:
    print(pessoa[0], "-", pessoa[1], "anos")

print("\nPessoas com 18 anos ou mais:")
for pessoa in maiores:
    print(pessoa[0], "-", pessoa[1], "anos")
