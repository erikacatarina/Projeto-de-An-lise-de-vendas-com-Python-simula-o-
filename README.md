# Projeto de Análise de vendas com Python (simulação)


🎯 Objetivo

Simular e analisar o desempenho de vendas de 5 produtos ao longo de 20 dias, através de operações estatísticas, filtragens, padronização, normalização e análises de receita com NumPy.

 🧩 Criação de dados simulados

1. Gerei de uma matriz 30x5 contendo o número de unidades vendidas dos produtos por dia;
2. Criei um vetor com valores aleatórios dos preços unitários de vada produto; e
3. Para que os dados fossem "fixos", simulando uma iteração mais real, utilizei np.random.seed(42) para garantir a reprodutibilidade dos resultados.

📊 Estatísticas

Usei algumas métricas para cada produto com o objetivo de ter uma noção do comportamento das vendas no mês, sendo elas:
- Média de vendas
- Soma total de unidades vendidas
- Desvio-padrão das vendas diárias
- Maior e menor valor de vendas
- Produto mais vendido (np.argmax)
- Maior venda individual (dia, produto, via np.unravel_index)

📈 Análise de desempenho diário

Calculei a média geral diária de vendas e o total vendido por dia. Em seguida, usei uma máscara booleana para selecionar os dias de vendas acima da média geral. Por fim, listei os índices desses dias e suas respectivas vendas.

🏆 Top 3 produtos mais vendidos

Identifiquei os 3 produtos mais vendidos com o uso de np.argpartition, sendo considerados os mais relevantes para o faturamento da empresa.

🧮 Submatriz filtrada

Combinei o filtro de dias acima da média com os top 3 produtos para dar origem à submatriz (np.ix_) que representa apenas as vendas dos produtos mais vendidos nos dias de maior desempenho.

📅 Dia de maior venda

Para achar o dia que representa o pico de desempenho de vendas dentro do período de 30 dias, encontrei o índice do dia com maior volume total de vendas sobre o vetor de totais diários usando np.argmax.

⚙️ Normalização e padronização da matriz

Para comparar produtos em diferentes escalas, fiz uso da padroniação (z-score), que centraliza os dados na média (0) e com desvio-padrão ≈ 1, e da normalização (0-1), que ajusta os valores dentro de um intervalo uniforme.

💰 Receita diária e top 3 dias mais lucrativos

Multipliquei a matriz de vendas pelo vetor de preços para achar a receita diária (np.matmul(vendas_mes, precos)). Do resultado pude identificar os 3 dias de maior receita total (picos de faturamento do mês) e compará-los com os dias de maior volume de vendas para avaliar a correlação entre quantidade e lucratividade.

🧠 Considerações finais
1. O produto mais vendido no mês foi identificado.
2. O dia com maior volume de vendas coincidiu com um dos dias de maior receita.
3. A análise confirmou que a padronização manteve as colunas centradas em 0 com desvio ≈ 1, validando a consistência estatística dos dados.

⏳ Próximos passos: aplicar a uma base de vendas real que coletei de uma empresa pequena da minha cidade e ver quais insights este código me permite extrair a partir dos dados carregados.
