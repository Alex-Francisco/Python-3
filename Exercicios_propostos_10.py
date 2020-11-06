## Exercício 10 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Um vendedor ambulante vendeu os produtos indicados na tabela a seguir. Informe quanto ele faturou com cada produto
e quanto ele faturou no total.

Boneco Malandrino - Vendeu 17 - Cada um por 18,50
Spinner Pequeno - Vendeu 36 - Cada um por 12,00
Cubo Mágico - Vendeu 7 - Cada um por 5,90

Todos os dados devem ser lidos do teclado, sendo que o nome do produto é string, a quantidade vendida é um número inteiro
e o valor unitário é um número real. """

Total_Geral = 0

NomeProd = input("Digite o nome do produto: ")
Quant_Vendida = int(input("Digite a quantidade vendida: "))
Valor_Unit = float(input("Digite o valor unitário: "))
Total_Venda = Quant_Vendida * Valor_Unit
Total_Geral += Total_Venda

print("")
print("Foram vendidas {} unidades do produto {}, cada uma por R${:.2f}, totalizando R${:.2f}".format(Quant_Vendida, NomeProd, Valor_Unit, Total_Venda))
print("")

NomeProd = input("Digite o nome do produto: ")
Quant_Vendida = int(input("Digite a quantidade vendida: "))
Valor_Unit = float(input("Digite o valor unitário: "))
Total_Venda = Quant_Vendida * Valor_Unit
Total_Geral += Total_Venda

print("")
print("Foram vendidas {} unidades do produto {}, cada uma por R${:.2f}, totalizando R${:.2f}".format(Quant_Vendida, NomeProd, Valor_Unit, Total_Venda))
print("")

NomeProd = input("Digite o nome do produto: ")
Quant_Vendida = int(input("Digite a quantidade vendida: "))
Valor_Unit = float(input("Digite o valor unitário: "))
Total_Venda = Quant_Vendida * Valor_Unit
Total_Geral += Total_Venda

print("")
print("Foram vendidas {} unidades do produto {}, cada uma por R${:.2f}, totalizando R${:.2f}".format(Quant_Vendida, NomeProd, Valor_Unit, Total_Venda))
print("")

print("O faturamento total do vendedor foi de R${:.2f}".format(Total_Geral))
