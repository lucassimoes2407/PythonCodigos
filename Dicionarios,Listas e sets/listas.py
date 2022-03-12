# Introdução à Listas
## Listas começam com []. Sempre que tiver dúvida sobre o tipo da variável, use o type ()
notas=[4,5,6,10,9,8]
print(f"A lista de notas sao: {notas}")

## Para criar Tuplas, utiliza-se o ()
notas_tup=(1,2,3,4) #Aqui é criado uma tupla
# Para transformar listas em tuplas, podemos utilizar a função list()
notasTup=list(notas_tup)
print(f"As notas agora sao uma lista {notas}")

#Uma lista pode armazenar vários tipos de objetos.
#Aqui temos um exemplo de uma lista que armazena string, int, float, booleando e outra lista.

lista_obj_variados=["Lucas Simoes", 24, 1.75, True, ["Carne", "Sushi", "Peixe"]]
print(lista_obj_variados)

# A funçao len retorna o coprimento da lista
print(len(lista_obj_variados)) # O resultado será 5.

# Para acessar os elementos da lista, devemos notar que lista[0] é o primeiro elemento e assim por diante.
primeiro_elemento = lista_obj_variados[0]
print(f"\nO primeiro elemento da lista e {primeiro_elemento}")
segundo_elemento = lista_obj_variados[1]
print(f"\nO segundo elemento da lista e {segundo_elemento}")

ultimo_elemento  = lista_obj_variados[-1]
penultimo_elemento = lista_obj_variados[-2]
print(f"\nO ultimo elemento da lista e {ultimo_elemento} e o penúltimo e {penultimo_elemento}")

##Metodos mais comuns para listas
#Adicionar elemento na lista:
lista_obj_variados.append([9,9,1])
print(f"\nO elemento [9,9,9] foi adicionado ao final da lista: {lista_obj_variados}")

#Adicionando um objeto inteiro em uma determinada posição
lista_obj_variados.insert(0, "Index 0")
print(f"\nA string foi adicionada na primeira posição da lista, de índice 0: {lista_obj_variados}")


# Removendo o primeiro elemento encontrado da lista, retorna erro se não encontrar o elemento
lista_obj_variados.remove([9,9,9])
print(f"\nO objeto [9,9,9] agora foi removido da lista: {lista_obj_variados}")

# Coletando um elemento da lista e salvando em uma variável a partir de um índice
# O .pop() permite salvar o elemento removido em uma variável, o .remove() não permite!
elemento_coletado = lista_obj_variados.pop(0)
print(f"\nO elemento no índice 0 foi removido da lista: {lista_obj_variados}")
print(f"\nO elemento coletado é {elemento_coletado}")

# Ordenando os valores de uma lista
notas.sort()
print(f"\nNotas ordenadas: {notas}")