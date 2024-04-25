'''
1. Calculadora de Desconto:
• Peça o preço original do produto.
• Peça a porcentagem de desconto.
• Calcule o valor do desconto.
• Exiba o preço final do produto com desconto.

'''

preço_Original = float(input("Digite o preço original do produto: R$ "))
porcentagem = float(input("Digite a porcentagem do desconto: "))
porcentagem = porcentagem/100
valor_desconto = "{:.2f}".format(preço_Original * porcentagem)

print("O preço do produto com desconto é de R$",valor_desconto)


