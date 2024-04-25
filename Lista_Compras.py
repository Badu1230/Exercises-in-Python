'''
6. Lista de Compras:
• Crie uma lista vazia.
• Peça ao usuário para adicionar itens à lista.
• Exiba a lista de compras.
• Pergunte ao usuário se ele deseja remover algum item da lista.
• Exiba a lista de compras atualizada.
'''
# Crie uma lista vazia para a lista de compras
lista_compras = []

# Peça ao usuário para adicionar itens à lista - estava fazendo com for in
while True:
    item = input("Digite um item para adicionar à lista de compras (ou digite 'fim' para sair): ") # fiz assim
    if item.lower() == "fim": # nao conhecia este metodo
        break  # Se o usuário digitar "fim", saia do loop
    lista_compras.append(item)  # Adicione o item à lista de compras

# Exiba a lista de compras
print("Lista de Compras:")
for item in lista_compras:
    print("- " + item) # nao fiz assim

# Pergunte ao usuário se ele deseja remover algum item da lista
while True:
    remover = input("Deseja remover algum item da lista? (sim/não): ") # fiz assim
    if remover.lower() == "não":  #nao conhecia este metodo
        break  # Se o usuário disser "não", saia do loop
    elif remover.lower() == "sim":
        item_remover = input("Qual item você gostaria de remover? ")
        if item_remover in lista_compras:
            lista_compras.remove(item_remover)  # Remova o item da lista de compras, se existir
        else:
            print("O item não está na lista de compras.")
    else:
        print("Opção inválida. Por favor, responda 'sim' ou 'não'.")

# Exiba a lista de compras atualizada
print("Lista de Compras Atualizada:")
for item in lista_compras:
    print("- " + item)



#estava fazendo funcoes com ,def lista-compras(compras) , def lista_atualizada(compras)


    
