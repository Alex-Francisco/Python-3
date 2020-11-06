## Exercício 22 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva um programa que leia o valor hora que um profissional ganha na empresa onde trabalha. Leia também as quantidades
de horas normais e horas extras trabalhadas em um mês. Calcule o valor a ser recebido pelo profissional nesse mês, sabendo
que nas horas extras o pagamento é dobrado."""

ganho_hora = float(input("Digite quanto o profissional ganha por hora (Exemplo: 12.98): "))
qtde_normais = float(input("Digite a quantidade de horas normais trabalhadas: "))
qtde_extras = float(input("Digite a quantidade de horas extras trabalhadas: "))

extras = ganho_hora * 2
total = (ganho_hora * qtde_normais) + (extras * qtde_extras)

print("O profissional que recebe R$ {:.2f}/h, trabalhou {} horas normais e {} horas extras vai receber a quantia de R$ {:.2f}".format(ganho_hora, qtde_normais, qtde_extras, total))

