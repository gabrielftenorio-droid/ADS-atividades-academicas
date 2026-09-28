import sqlite3

conexao = sqlite3.connect('dados_vendas.db')

cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
data_venda DATE,
produto TEXT,
categoria TEXT,
valor_venda REAL
)
''')

cursor.execute("SELECT COUNT(*) FROM vendas1")
quantidade_registros = cursor.fetchone()[0]

if quantidade_registros == 0:
    cursor.executemany('''
        INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
        (?, ?, ?, ?)
    ''', [
        ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
        ('2023-01-05', 'Produto B', 'Roupas', 150.00),
        ('2023-02-17', 'Produto C', 'Eletrônicos', 1200.00),
        ('2023-03-15', 'Produto D', 'Livros', 200.00),
        ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
        ('2023-04-02', 'Produto F', 'Roupas', 400.00),
        ('2023-05-05', 'Produto G', 'Livros', 150.00),
        ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
        ('2023-07-27', 'Produto I', 'Roupas', 600.00),
        ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
        ('2023-09-09', 'Produto K', 'Livros', 300.00),
        ('2023-10-15', 'Produto L', 'Roupas', 450.00),
        ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
        ('2023-12-20', 'Produto N', 'Livros', 250.00)
    ])

conexao.commit()

import pandas as pd

df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)

df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])

print("DataFrame Carregado:")
print(df_vendas.head())

print("\nInformações do DataFrame:")
print(df_vendas.info())

vendas_por_categoria = df_vendas.groupby('categoria')['valor_venda'].sum().sort_values(ascending=False)

print("\nTotal de Vendas por Categoria:")
print(vendas_por_categoria)

df_vendas['mes'] = df_vendas['data_venda'].dt.month
vendas_por_mes = df_vendas.groupby('mes')['valor_venda'].sum()

print("\nTotal de Vendas por Mês:")
print(vendas_por_mes)

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8-whitegrid')

plt.figure(figsize=(10, 6))
sns.barplot(x=vendas_por_categoria.index, y=vendas_por_categoria.values, palette='viridis')
plt.title('Total de Vendas por Categoria', fontsize=16)
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Valor Total de Vendas (R$)', fontsize=12)
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(x=vendas_por_mes.index, y=vendas_por_mes.values, marker='o', color='b')
plt.title('Vendas Totais ao Longo do Ano', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Valor Total de Vendas (R$)', fontsize=12)
plt.xticks(range(1, 13))
plt.show()