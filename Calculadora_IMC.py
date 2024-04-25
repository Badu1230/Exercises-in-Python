'''
7. Calculadora de IMC:
• Peça o peso do usuário.
• Peça a altura do usuário.
• Calcule o IMC (peso / altura2).
• Exiba o IMC do usuário e sua classificação (abaixo do peso, normal, acima do peso, obeso).  IMC ideal está na faixa de 18,6 a 24,9.

Seu IMC é: 44.44
Você está acima do peso! - não dava - "vc esta obeso"
'''
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = float(peso / (altura**2))

print(f'Seu IMC é: {imc:.2f}')

if imc <= 18.4:
    print('Você está abaixo do peso!')
elif imc < 18.5:
    print('Seu peso é ideal!')
elif imc > 25:
    print('Você está acima do peso!')        
else:
  imc > 30
  print('Atenção, você está obeso(a)')  

