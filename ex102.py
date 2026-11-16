
menores = []
maiores = []

for i in range(10):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    pessoa = {
        "nome": nome,
        "idade": idade
    }

    if idade < 18:
        menores.append(pessoa)
    else:
        maiores.append(pessoa)

print("\nPessoas menores de 18 anos:")
for pessoa in menores:
    print(pessoa["nome"], "-", pessoa["idade"], "anos")

print("\nPessoas com 18 anos ou mais:")
for pessoa in maiores:
    print(pessoa["nome"], "-", pessoa["idade"], "anos")
