## Exercício 48 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" A matriz a seguir mostra o custo unitário de cada produto e a quantidade de cada um dos produtos no estoque de três
lojas de uma rede. Escreva um programa que exiba na tela as respostas para as perguntas. Na solução desse problema, elabore
uma maneira de armazenar seus dados utilizando lista e sublistas. Os dados da matriz devem ser lidos do teclado.

             custo unitário          Loja 1          Loja 2          Loja 3
Produto A    R$ 72,35                373             558             358
Produto B    R$ 43,93                1228            1448            907
Produto C    R$ 17,84                4135            2059            3122
Produto D    R$ 23,19                1139            1450            843

a) Qual é o valor total de estoque em cada uma das lojas?
b) Qual é o valor de estoque para cada produto disponível na rede?
c) Qual é o valor total de estoque da rede? """

Produtos = []
tipo = 'A'
ident = 1
continua = 's'

A1, B1, C1, D1 = 0, 0, 0, 0
A2, B2, C2, D2 = 0, 0, 0, 0 
A3, B3, C3, D3 = 0, 0, 0, 0

TA, TB, TC, TD = 0, 0, 0, 0

while continua == 's':
    custo_unit = float(input("\nDigite o custo unitário do Produto {}: R$ ".format(tipo)))
    qtdeL1 = int(input("Digite a quantidade do produto {} em estoque na loja {}: ".format(tipo, ident)))
    ident += 1
    qtdeL2 = int(input("Digite a quantidade do produto {} em estoque na loja {}: ".format(tipo, ident)))
    ident += 1
    qtdeL3 = int(input("Digite a quantidade do produto {} em estoque na loja {}: ".format(tipo, ident)))

    Info = (tipo, custo_unit, qtdeL1, qtdeL2, qtdeL3)
    Produtos.append(Info)
    
    if tipo == 'A' and ident == 3:
        A1 = qtdeL1 * custo_unit
        A2 = qtdeL2 * custo_unit
        A3 = qtdeL3 * custo_unit
        TA = (qtdeL1 + qtdeL2 + qtdeL3) * custo_unit
        tipo = 'B'
        ident = 1      
    elif tipo == 'B' and ident == 3:
        B1 = qtdeL1 * custo_unit
        B2 = qtdeL2 * custo_unit
        B3 = qtdeL3 * custo_unit
        TB = (qtdeL1 + qtdeL2 + qtdeL3) * custo_unit
        tipo = 'C'
        ident = 1        
    elif tipo == 'C' and ident == 3:
        C1 = qtdeL1 * custo_unit
        C2 = qtdeL2 * custo_unit
        C3 = qtdeL3 * custo_unit
        TC = (qtdeL1 + qtdeL2 + qtdeL3) * custo_unit
        tipo = 'D'
        ident = 1
    else:
        D1 = qtdeL1 * custo_unit
        D2 = qtdeL2 * custo_unit
        D3 = qtdeL3 * custo_unit
        TD = (qtdeL1 + qtdeL2 + qtdeL3) * custo_unit
        continua = 'n'

print('Lista de Produtos em Estoque\n')

for(Prod, Custo, Qtde1, Qtde2, Qtde3) in Produtos:  
    print("==*=="*15)
    print("\nProduto referido: ", Prod)
    print("Custo Unitário: ", Custo)
    print("Quantidade em estoque na loja 1: ", Qtde1)
    print("Quantidade em estoque na loja 2: ", Qtde2)
    print("Quantidade em estoque na loja 3: ", Qtde3)
    print("\n")

print("a) Qual o valor de estoque em cada uma das lojas?")
print("\nA loja 1 tem R${:.2f} em estoque, a loja 2 tem R${:.2f} e a loja 3 tem R${:.2f} do produto A".format(A1, A2, A3))
print("A loja 1 tem R${:.2f} em estoque, a loja 2 tem R${:.2f} e a loja 3 tem R${:.2f} do produto B".format(B1, B2, B3))
print("A loja 1 tem R${:.2f} em estoque, a loja 2 tem R${:.2f} e a loja 3 tem R${:.2f} do produto C".format(C1, C2, C3))
print("A loja 1 tem R${:.2f} em estoque, a loja 2 tem R${:.2f} e a loja 3 tem R${:.2f} do produto D".format(D1, D2, D3))

print("\nb) Qual o valor total de estoque p/ cada produto disponível na rede?")
print("\nO valor do produto A em estoque é de R${:.2f}".format(TA))
print("O valor do produto B em estoque é de R${:.2f}".format(TB))
print("O valor do produto C em estoque é de R${:.2f}".format(TC))
print("O valor do produto D em estoque é de R${:.2f}".format(TD))

print("\nc) Qual é o valor total de estoque da rede?")
print("\nO valor total de estoque é de R${:.2f}".format(TA + TB + TC + TD))
