## 🚀 Funcionalidades

- **Extração de Dados:** Consome a API do Banco Central para obter o valor mais recente do CDI.
- **Simulação de Variação:** Gera 10 amostras com pequenas variações aleatórias para fins de demonstração estatística.
- **Armazenamento:** Salva automaticamente os dados em um arquivo `taxa-cdi.csv`.
- **Visualização:** Gera um gráfico de linha formatado (`.png`) utilizando Seaborn e Pandas.

## 🛠️ Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/) (Manipulação de dados)
- [Seaborn](https://seaborn.pydata.org/) / [Matplotlib](https://matplotlib.org/) (Visualização de dados)
- [Requests](https://requests.readthedocs.io/) (Requisições HTTP)

## 📋 Pré-requisitos

Antes de rodar o script, você precisará instalar as bibliotecas necessárias. Abra o seu terminal e execute:

````bash
pip install requests pandas seaborn

Como usar
Clone o repositório:

Bash
git clone [https://github.com/seu-usuario/nome-do-seu-repositorio.git](https://github.com/seu-usuario/nome-do-seu-repositorio.git)

Navegue até a pasta do projeto:

Bash
cd nome-do-seu-repositorio

**Execute o script:**
    Você deve passar o nome desejado para o gráfico como um argumento no comando:
    ```bash
    python seu_script.py meu_grafico_cdi
    ```

  **Resultado:**
    *   Um arquivo `taxa-cdi.csv` será criado ou atualizado.
    *   Um arquivo `meu_grafico_cdi.png` será gerado na pasta.

## 📊 Exemplo de Saída do CSV

| data | hora | taxa |
| :--- | :--- | :--- |
| 2024/05/20 | 14:05:01 | 10.65 |
| 2024/05/20 | 14:05:02 | 10.42 |

---
⭐ Desenvolvido como parte do curso de Python da EBAC.
````
