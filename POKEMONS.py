import pandas as pd
import os
import sqlite3


caminho_arquivo = os.path.join('../database', 'Pokemon.csv')
caminho_absoluto=os.path.abspath(caminho_arquivo)
dados = pd.read_csv('/mnt/c/Users/labcaxias/Documents/DS202/BD/LTE-pokemon/dar')
dados=pd.DataFrame(dados)
filtro = dados.loc[dados['Name'].str.contains('Mega')]

print(filtro.head())