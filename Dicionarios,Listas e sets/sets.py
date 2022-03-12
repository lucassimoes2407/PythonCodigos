
## Característica dos sets:
# Conjuntos matemáticos 
# Não há como acessar por posição (posições são aleatórias)
# Elementos únicos, exclusivos, sem repetição
# Para a criação do set, utiliza-se {}, note que é diferente do dicionário, pois falta o :
conjunto_a = {1,2,3,4,1,2,3,4,1,2,3,4,5}
print(f"Conjunto A: {conjunto_a}")

# A função set() transforma uma variável em um set
nome=set("LucaS Simoes")
nome_aleatorias=set("Lcas Mnome")

# Pergunta 1: Quais letras em comum temos em `nome` e `nome_aleatorias`?
print(f"Resp 1: {nome.intersection(nome_aleatorias)}")

# Pergunta 2: Quais letras temos em `nome` que não estão em `nome_aleatorias`?
print(f"Resp 2: {nome - nome_aleatorias}")

# Pergunta 3: Quais letras temos em `nome_aleatorias` que não estão em `nome`?
print(f"Resp 3: {nome_aleatorias - nome}")

# Pergunta 4: Quantas letras não repetidas temos ao total, quando consideramos `nome` e `nome_aleatorias`?
print(f"Resp 4: {len(nome.union(nome_aleatorias))}")

# Pergunta 5: Quais letras estão ou em `nome_aleatorias` ou em `nome` mas não em ambos ao mesmo tempo?
print(f"Resp 5: {nome.symmetric_difference(nome_aleatorias)}")

# Pergunta 6: A letra F está em `nome`
print(f"Resp 6: {'F' in nome}")

# Pergunta 7: `nome_aleatorias` é um subconjunto de `nome`? 
# Em outras palavras, `nome_aleatorias` está contida em `nome`?
# ou ainda: `nome` contém TODAS as letras de `nome_aleatorias`?
print(f"Resp 7: {nome_aleatorias.issubset(nome)}")
