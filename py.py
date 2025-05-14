# vencimento_atual = int(input('Digite o vencimento atual: '))
# vencimento_novo = int(input('Digite o novo vencimento: '))
# valor_plano = float(input('Digite o valor atual do plano: '))

# if(vencimento_atual < vencimento_novo):
#     dias_proporcionais = vencimento_novo - vencimento_atual
# else:
#     dias_proporcionais = (30 - vencimento_atual) + vencimento_novo

# diaria_plano = valor_plano / 30
# proporcional = diaria_plano * dias_proporcionais
# valor_total = proporcional + valor_plano
# print(valor_total)


valorAntigo = float(input('Digite o valor do plano antigo: '))
valorNovo = float(input('Digite o valor do plano novo: '))
vencimento = int(input('Digite a data do vencimento: '))
dataTroca = int(input('Digite a data da troca: '))

diariaAntigo = valorAntigo / 30
diariaNovo = valorNovo / 30

diasPlanoAntigo = dataTroca - vencimento 
diasPlanoNovo = vencimento - dataTroca + 30

proporcionalAntigo = diariaAntigo * diasPlanoAntigo
proporcionalNovo = diariaNovo * diasPlanoNovo

valorTotal = proporcionalAntigo + proporcionalNovo

print('Proporcional do plano antigo',proporcionalAntigo)
print('Proporcional do plano novo',proporcionalNovo)
print('Valor total do proporcional',valorTotal)

