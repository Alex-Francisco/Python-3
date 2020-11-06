## Exercício 21 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia o nome de um lutador e seu peso. Em seguida, informe a categoria a que pertence o lutador,
conforme o Quadro 3.9 (note que o quadro foi criado para efeito deste exercício e não condiz com qualquer categoria de luta). A
saída do programa deve exibir na tela uma frase com o padrão descrito a seguir:
Nome fornecido: Pepe Jordão
Peso fornecido: 73.4
Frase a ser exibida: O lutador Pepe Jordão pesa 73,4 kg e se enquadra na categoria Ligeiro"""

nome_lutador = input("Digite o nome do lutador: ")
peso = float(input("Digite o peso do lutador: "))
categoria = ""

if peso < 65:
    categoria = "Pena"
elif peso >= 65 and peso <= 72:
    categoria = "Leve"
elif peso > 72 and peso <= 79:
    categoria = "Ligeiro"
elif peso > 79 and peso <= 86:
    categoria = "Meio-médio"
elif peso > 86 and peso <= 93:
    categoria = "Médio"
elif peso > 93 and peso <= 100:
    categoria = "Médio-pesado"
else:
    categoria = "Pesado"

print("O lutador {} pesa {} kg e se enquadra na categoria {}".format(nome_lutador, peso, categoria))

