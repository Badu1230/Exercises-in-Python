'''10. Jogo da Forca:
• Pense em uma palavra.
• Exiba a palavra com "_" para cada letra.
• Peça ao usuário para adivinhar uma letra.
• Se a letra estiver na palavra, revele a letra na posição correta.
• Se a letra não estiver na palavra, diminua o número de tentativas.
• O usuário perde se o número de tentativas chegar a zero.
• O usuário ganha se adivinhar todas as letras da palavra.
'''
#usei chat GPT para me ajudar a incrementar e deixar meu código mais arrumado
'''print('Pense em uma palavra!')
print('Esta palavra tem estas quantidades de espaços: _ _ _ _')
advinhar = 'amor'
max_tentativas = 3

print(input('Tente advinhar uma letra:'))

for advinhar in range(max_tentativas):
   if 'a' in advinhar:
    print('Esta letra está na primeira posição')
   elif 'm' in advinhar:
    print('Esta letra está na segunda posição')
   elif 'o' in advinhar:
    print('Esta letra está na terceira posição')
   elif  'r' in advinhar: 
    print('Esta letra está na última posição')    
    break
   print("Entrada inválida. Tente novamente.")
else:
    print("Número máximo de tentativas alcançado. Encerrando o programa.")
    '''
# Palavra a ser adivinhada
palavra = 'amor'

# Cria uma lista com '_' para cada letra da palavra
palavra_escondida = ['_'] * len(palavra)

# Número máximo de tentativas
max_tentativas = 5

# Loop principal do jogo
for tentativa in range(max_tentativas):
    # Exibe a palavra com as letras adivinhadas e os '_' para as letras não reveladas
    print(' '.join(palavra_escondida))

    # Solicita ao usuário para adivinhar uma letra
    letra = input('Tente advinhar uma letra: ')

    # Verifica se a letra está na palavra
    if letra in palavra:
        print('Esta letra está na palavra!')
        # Atualiza a palavra escondida com a letra revelada
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_escondida[i] = letra
    else:
        print('Esta letra não está na palavra.')

    # Verifica se todas as letras foram adivinhadas
    if '_' not in palavra_escondida:
        print('Parabéns! Você adivinhou a palavra:', palavra)
        break

# Se o número máximo de tentativas for alcançado
else:
    print("Número máximo de tentativas alcançado. A palavra era:", palavra)



   



