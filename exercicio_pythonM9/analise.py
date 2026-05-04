# combinação dos scripts de extração e visualização
import os
import time
import json
import csv
from random import random
from datetime import datetime
from sys import argv

import requests
import pandas as pd
import seaborn as sns

# --- PARTE 1: Extração e Salvamento de Dados ---

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'

# Captando a taxa CDI atual do site do BCB (SGS)
try:
    response = requests.get(url=URL)
    response.raise_for_status()
except requests.HTTPError as exc:
    print("Dado não encontrado, continuando.")
    cdi_base = None
except Exception as exc:
    print("Erro grave, parando a execução.")
    raise exc
else:
    # Pega o valor do último registro da lista
    cdi_base = json.loads(response.text)[-1]['valor']

# Loop para gerar 10 entradas simuladas e salvar no CSV
for _ in range(0, 10):
    data_e_hora = datetime.now()
    data = datetime.strftime(data_e_hora, '%Y/%m/%d')
    hora = datetime.strftime(data_e_hora, '%H:%M:%S')
    
    # Simula uma variação na taxa para o gráfico não ser uma linha reta
    cdi_simulado = float(cdi_base) + (random() - 0.5)
    
    # Verifica se o arquivo existe para escrever o cabeçalho
    if not os.path.exists('./taxa-cdi.csv'):
        with open(file='./taxa-cdi.csv', mode='w', encoding='utf8') as fp:
            fp.write('data,hora,taxa\n')
    
    # Salva o dado no arquivo CSV
    with open(file='./taxa-cdi.csv', mode='a', encoding='utf8') as fp:
        fp.write(f'{data},{hora},{cdi_simulado}\n')
    
    time.sleep(1)

print("Dados extraídos com sucesso.")

# --- PARTE 2: Geração do Gráfico ---

# Verifica se o usuário passou um nome para o gráfico via linha de comando
if len(argv) < 2:
    nome_grafico = "grafico_cdi"
else:
    nome_grafico = argv[1]

print(f"Gerando gráfico: {nome_grafico}.png...")

# Extraindo as colunas do arquivo criado
df = pd.read_csv('./taxa-cdi.csv')

# Criando e formatando o gráfico
sns.set_theme(style="darkgrid") # Opcional: deixa o gráfico mais bonito
grafico = sns.lineplot(x='hora', y='taxa', data=df)
grafico.set_xticklabels(labels=df['hora'], rotation=90)
grafico.set_title("Variação da Taxa CDI (Simulada)")

# Salvando a figura
grafico.get_figure().savefig(f"{nome_grafico}.png")

print("Sucesso!")