import numpy as np

# Projto NumPy - análise de vendas

# Criando dados para simular uma tabela de 5 produtos vendidos por uma empresa durante 30d

np.random.seed(42)
vendas_mes = np.random.randint(low= 0, high=49, size=(30, 5))
preços = np.random.uniform(low=0, high=100, size=(5))
np.set_printoptions(precision=2, suppress=True) 

print(f"Matriz de vendas (30 dias x 5 produtos): \n{vendas_mes}.")
print(f"Matriz de preços dos 5 produtos: \n{preços}.")

# Roteiro da análise estatística
'''
1) Calculando a média, soma e o desvio-padrão de cada produto no mês 
2) Selecionando os maiores e menores valores de cada produto no mês 
3) Dia de maior venda 
4) Produto mais vendido 
5) Dias acima da média geral
6) Top 3 produtos mais vendidos
7) Submatriz filtrada (dias acima da média x top 3 produtos)
8) Normalização e padronização
9) Receita diária e top 3 dias de vendas
10) Transformações 2D
'''

# Estatísticas básicas

média = np.mean(vendas_mes, axis=0)
total_por_produto = np.sum(vendas_mes, axis=0)
total_por_produto_por_dia = np.sum(vendas_mes, axis=1)
dp = np.std(vendas_mes, axis=0)
maior_valor_por_produto = np.max(vendas_mes, axis=0)
menor_valor_por_produto = np.min(vendas_mes, axis=0)
prod_mais_vendido = np.argmax(total_por_produto)
indice_prod_mais_vendido = np.unravel_index(np.argmax(vendas_mes), vendas_mes.shape)

print("------ Estatísticas ------")
print(f"A média de unidades vendidas de cada produto: \n{média}.")
print(f"Total de unidades vendidas em relação a cada produto: \n{total_por_produto}.")
print(f"Desvio-padrão por produto: {dp}.")
print(f"A maior quantidade de unidades vendidas por produto foi de {maior_valor_por_produto}.")
print(f"A menor quantidade de unidades vendidas por produto foi de {menor_valor_por_produto}.")
print(f" O produto {prod_mais_vendido} foi o mais vendido no mês.")
print(f"A maior venda individual aconteceu no índice {indice_prod_mais_vendido} (dia, produto).")

# Selecionando os dias de venda acima da média geral

média_por_dia = np.mean(vendas_mes, axis=1) 
filtro = total_por_produto_por_dia > média_por_dia
vendas_acima_média = vendas_mes[filtro]

print("------ Dias acima da média geral ------")
print(f"Média geral de vendas diárias: \n{média_por_dia}")
print(f"Total de vendas diárias: \n{total_por_produto_por_dia}")
print(f"Dias com total de vendas acima da média: \n{np.where(filtro)[0]}")
print(f"Vendas nesses dias:\n", vendas_acima_média)

# Top 3 produtos mais vendidos

top3_acima_média = np.argpartition(total_por_produto, -3) [-3:]
print(f"Os 3 produtos mais vendidos no mês foram {top3_acima_média}.")

# Submatriz (dias acima da média x top 3 produtos)

submatriz = vendas_mes[np.ix_(filtro, top3_acima_média)]
print(f"Submatriz (dias acima da média x top 3 produtos): \n{submatriz}")

# Achando o dia de maior venda total (dia = índice)

dia_maior_venda = np.argmax(total_por_produto_por_dia)
print(f"O dia de maior venda total foi o dia {dia_maior_venda}.")

# Padronizando e normalizando a matriz de vendas

matriz_normalizada = (vendas_mes - (np.min(vendas_mes, axis=0))) / (np.max(vendas_mes, axis=0)) - (np.min(vendas_mes, axis=0))
matriz_padronizada = (vendas_mes - média) / dp

print(f"A matriz nomarlizada (0-1) é representada por: \n{np.round(matriz_normalizada, 2)}")
print(f"A matriz padronizada (z-score) é representada por: \n{np.round(matriz_padronizada, 2)}")

# Calculando a receita diária >> receita = vendas * preços

receita_diária = np.matmul(vendas_mes, preços)
print(f"A receita diária foi de: \n{np.round(receita_diária, 2)}.")

# Achando os top 3 dias de vendas

top3_por_receita = np.argpartition(receita_diária, -3)[-3:]
unidades_top3 = receita_diária[top3_por_receita]
print(f"Os 3 produtos mais vendidos no mês foram {unidades_top3} e os 3 dias com maior receita foram {top3_por_receita}.")

# Considerações finais

print("Após realizar análise minuciosa sobre os dados coletados, pode-se perceber que:")
print(f"O produto mais vendido {prod_mais_vendido} apresentou o maior total de vendas no mês.")
print(f"O dia {dia_maior_venda} foi o dia com maior volume total de vendas.")
print(f"Os dias mais lucrativos tendem a coincidir com os dias de maior receita ({top3_acima_média}).")
print(f"Após a padronização da matriz, as colunas ficaram centradas em 0 e com desvio ≈ 1, o que confirma a análise.")

# Transformações 2D

matriz_transformação = np.random.randint(low=0, high= 11, size=(4,4))

print(f"Matriz original: \n{matriz_transformação}")
print(f"Matriz rotacionada em 90º: \n{np.rot90(matriz_transformação)}")
print(f"Matriz rotacionada em 180º: \n{np.rot90(matriz_transformação, 2)}")