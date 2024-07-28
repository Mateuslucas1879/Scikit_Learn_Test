# Análise de Doença Cardíaca

Este repositório contém um script Python para análise de um conjunto de dados de doença cardíaca. A análise inclui a visualização e a exploração dos dados, bem como a criação de gráficos informativos.

## Estrutura do Código

1. **Importação de Bibliotecas:**
    ```python
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report
    ```

2. **Leitura e Exibição do DataFrame:**
    ```python
    df = pd.read_csv("heart-disease.csv")
    print(df.head())
    ```

3. **Contagem de Alvos:**
    ```python
    print("=-"*70)
    target_counts = df["target"].value_counts()
    print(target_counts)
    print("=-"*70)
    ```

4. **Contagem de Alvos Normalizada:**
    ```python
    target_counts03 = df["target"].value_counts(normalize=True)
    print(target_counts03)
    ```

5. **Informações sobre o DataFrame:**
    ```python
    print("=-"*70)
    target_counts05 = df.info()
    print(target_counts05)
    print("=-"*70)
    ```

6. **Crosstab de Alvo e Sexo:**
    ```python
    print("=-" * 70)
    target_counts06 = pd.crosstab(df["target"], df["sex"])
    print(target_counts06)
    print("=-" * 70)
    ```

7. **Gráfico de Barras de Alvo e Sexo:**
    ```python
    target_counts07 = pd.crosstab(df["target"], df["sex"])
    target_counts07.plot(kind="bar", figsize=(10, 6), color=("black", "white"))
    plt.title("Frequencia Cardiaca")
    plt.xlabel("0-Não tem Doença, 1-Doença Detectada")
    plt.ylabel("Amostragem")
    plt.legend(["Homem", "Mulher"])
    plt.show()
    ```

8. **Dispersão de Idade e Frequência Cardíaca Máxima:**
    ```python
    plt.figure(figsize=(10, 6))
    plt.scatter(df["age"][df["target"] == 1], df["thalach"][df["target"] == 1], c="salmon")
    plt.scatter(df["age"][df["target"] == 0], df["thalach"][df["target"] == 0], c="blue")
    plt.title("Doença cardiaca em função da idade e da frequencia cardiaca maxima")
    plt.show()
    ```

9. **Gráfico de Barras de Tipo de Dor Torácica:**
    ```python
    target_counts09 = pd.crosstab(df["cp"], df["target"])
    target_counts09.plot(kind="bar", figsize=(10, 6), color=("black", "red"))
    plt.title("Frequencia Da Doença Cardiaca por Tipo de Dor Toracica")
    plt.xlabel("Tipo de Dor no Peito")
    plt.ylabel("Frequencia")
    ```

10. **Matriz de Correlação:**
    ```python
    corr_matrix = df.corr()
    plt.figure(figsize=(15, 10))
    sns.heatmap(corr_matrix, annot=True, linewidth=0.5, fmt=".2f", cmap="YlGnBu")
    plt.show()
    ```

## Como Usar

1. Clone o repositório:
    ```sh
    git clone https://github.com/Mateuslucas1879/HeartDisease.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd HeartDisease
    ```
3. Instale as dependências necessárias:
    ```sh
    pip install -r requirements.txt
    ```
4. Execute o script:
    ```sh
    python analysis.py
    ```

## Conjunto de Dados

O conjunto de dados usado neste projeto é `heart-disease.csv`, que deve estar localizado no diretório raiz do projeto. Este conjunto de dados contém informações sobre pacientes e se eles têm ou não uma doença cardíaca.

## Visualizações

O script gera várias visualizações para ajudar na análise dos dados, incluindo:

- Gráficos de barras para contagens de alvos por sexo.
- Gráficos de dispersão para idade e frequência cardíaca máxima.
- Gráficos de barras para tipos de dor torácica.
- Heatmap para a matriz de correlação dos atributos.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.
