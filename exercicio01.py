# Criar 5 variaveis
# Nome
# Rua
# Número
# CEP
# Cidade
# com valores lidos do input(), para cada item exibir a seguinte mensagem
# ENVIAR PARA: Maria
# ENDEREÇO: Rua das Flores, 15 | CEP: 1200-001
# CIDADE: Lisboa

nome = input("Digite seu nome: ")
rua = input("Digite sua rua: ")
numero = input("Digite o número: ")
cep = input("Digite seu CEP: ")
cidade = input("Digite sua cidade: ")

print(f"ENVIAR PARA: {nome}")
print(f"ENDEREÇO: {rua}, {numero} | {cep}")
print(f"CIDADE: {cidade}")
