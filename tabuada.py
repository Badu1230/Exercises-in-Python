'''
4. Tabuada:
• Peça um número.
• Exiba a tabuada do número (de 1 a 10).
#precisei ver no chatGPT por causa do range
for i in range(1, 11) - fiz for x in numero - teria que usar range
'''
numero = int(input("Digite um número: "))

# Exibe a tabuada do número de 1 a 10

print(f"Tabuada do {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
   

