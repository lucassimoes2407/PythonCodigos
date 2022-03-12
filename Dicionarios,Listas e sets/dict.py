## Característica dos dicionários
# São estruturas de dados de mapeamento, de de-para, chave-valor
# Começam com {} e tem : que dividem os partes de chave:valor e vírgula separando um par de chave e valor do outro

sigla_estado = {"CE" : "Ceara", "MG" : "Minas Gerais"}

#Também é possível criar diciionários idênticos com a função dict()
sigla_estado_fun=dict(CE="Ceara", MG="Minas Gerais")

print(sigla_estado)
print(sigla_estado_fun)

#Métodos mais comuns de dicionários
print(f"\nTransformando as chaves em uma lista: {list(sigla_estado)}")
print(f"\nTransformando as chaves em um outro objeto: {sigla_estado.keys()}")

#Retornando os valores do dicionário
print(f"\nValores do meu dicionario: {sigla_estado.values()}")

# Retornando os pares de chave-valor
print(f"\nPares de chave-valor: {sigla_estado.items()}")
### CHECANDO EXISTENCIA DE ITENS NO DICIONÁRIO
check_ce = "CE" in sigla_estado
print(f"\nA sigla SP esta nas chaves? Resposta: {check_ce}")

check_se = "SE" in sigla_estado
print(f"\nA sigla SE esta nas chaves? Resposta: {check_se}")
