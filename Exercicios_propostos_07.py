## Exercício 07 do livro Python 3 - Conceitos e Aplicações - Uma Abordagem Didática
""" Escreva a sequência de comandos para calcular o salário bruto de um profissional que ganha por hora, sabendo
que ele ganha R$ 14,25/h e trabalhou 163 horas normais e 20 horas extras (pagam em dobro)."""

Salario_hora = 14.25
Extra_hora = 14.25 * 2

print("O profissional que ganha R${}/hora, trabalhou 163 horas normais e 20 horas extras, recebeu R${}.".format(Salario_hora, (Salario_hora * 163) + (Extra_hora * 20)))
