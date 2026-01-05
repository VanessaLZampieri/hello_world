valor_conta = float(input('Digite o valor da conta: '))
porcentagem_gorgeta = float(input('Digite a porcentagem da gorgeta: '))

valor_gorgeta = (valor_conta * porcentagem_gorgeta) /100
valor_total = valor_conta + valor_gorgeta

print(f'Gorgeta: {valor_gorgeta}, Total: {valor_total}')