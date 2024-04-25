'''
3. Simulador de Salário:
• Peça o valor da hora trabalhada.
• Peça a quantidade de horas trabalhadas por semana.
• Calcule o salário bruto (horas trabalhadas x valor da hora).
• Descreva os descontos (INSS, imposto de renda, etc.).
• Calcule o salário líquido (salário bruto - descontos).
• Exiba o salário líquido.
Como funciona o desconto do INSS em 2024? As alíquotas são de 
7,5% para aqueles que 
ganham até R$ 1.412,00; de 9% para quem ganha entre
 R$ 1.412,01 até R$ 2.666,68; de 12% para os que ganham entre 
 R$ 2.666,69 até R$ 4.000,03; e de 14% para quem ganha de
   R$ 4.000,04 até R$ 7.786,02.
   Quanto é descontado de IR?
3. Faça o desconto do IRRF
Rendimentos	Alíquota
Até R$ 2.259,20	Isento
De R$ 2.259,21 até R$ 2.826,65	7,5%
De R$ 2.826,66 até R$ 3.751,05	15%
De R$ 3.751,06 até R$ 4.664,68	22,5%
valor salario bruto - inss-ir
'''
hora_trabalhada = float(input("Digite o valor da hora trabalhada: R$ "))
quantidade_horas = int(input("Digite a quantidade de horas trabalhadas por semana: "))
salario_bruto = (hora_trabalhada * quantidade_horas) * 4
print("O valor do salário bruto mensal é: R$",salario_bruto)

def desconto_Inss(salario_bruto):
    if salario_bruto <= 1412:
       return salario_bruto * 0.075
    elif salario_bruto >= 1412.01:
       return salario_bruto * 0.09
    elif salario_bruto >= 2666.69:
       return salario_bruto * 0.12
    else:
       return salario_bruto * 0.14
    
def desconto_IR(salario_bruto):
    if salario_bruto <= 2259.20:
       return 0
    elif salario_bruto >= 2259.21:
       return salario_bruto * 0.075
    elif salario_bruto >= 2826.65:
       return salario_bruto * 0.15
    elif salario_bruto >= 3371.06:
        return salario_bruto * 0.225
    else:
        return salario_bruto * 0.275
    
inss = desconto_Inss(salario_bruto)
ir = desconto_IR(salario_bruto)
salario_liquido = salario_bruto - inss - ir

print(f'O salário líquido é: R$ {salario_liquido:.2f}')
             
   
    

    


      
 
