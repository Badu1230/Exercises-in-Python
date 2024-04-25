import random

# Nao conhecia este modulo. Fiz com for in e if else
# Eu não fiz o código. Fui no ChatGpt, achei mais simples e rápido

# Escolhe um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

#Por exemplo, se você quiser gerar um número aleatório entre 1 e 100, você usaria random.randint(1, 100). 
#Essa função retornará um número inteiro aleatório dentro do intervalo especificado

print('Pense em um número de 1 à 100')
print('Tente adivinhar este número')

while True:
    # Solicita ao usuário para adivinhar o número
    palpite = int(input('Digite um número: '))
    
    # Verifica se o palpite é menor, maior ou igual ao número secreto
    if palpite < numero_secreto:
        print('Tente um número maior!')
    elif palpite > numero_secreto:
        print('Tente um número menor!')
    else:
        print('Parabéns, você acertou o número!')
        break  # Encerra o loop quando o usuário acerta o número

            

    
       



