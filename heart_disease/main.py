import pandas as pd
# Linha corrigida
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# MOSTRA A TABELA DE FORMA COMPLETA
df = pd.read_csv("heart-disease.csv")
print(df.head())


# SEGUNDA PARTE DO CODIGO 
print("=-"*70)
target_counts = df["target"].value_counts()
print(target_counts)
print("=-"*70)

# TERCEIRA PARTE DO CODIGO
target_counts03=df["target"].value_counts(normalize=True)
print(target_counts03)

#QUARTA PARTE DO CODIGO
print("=-"*70)
target_counts04 = df["target"].value_counts()
print(target_counts04)

# QUINTA PARTE DO CODIGO
print("=-"*70) 
target_counts05 = df.info()
print(target_counts05)
print("=-"*70)

#SEXTA PARTE DO CODIGO
print("=-" * 70)
target_counts06 = pd.crosstab(df["target"], df["sex"])
print(target_counts06)
print("=-" * 70)

#SETIMA PARTE DO CODIGO
print("=-" * 70)
target_counts07 = pd.crosstab(df["target"], df["sex"])
target_counts07.plot(kind="bar",figsize=(10,6),color=("black","white"))
plt.title("Frequencia Cardiaca")
plt.xlabel("0-Não tem Doença, 1-Doença Detectada")
plt.ylabel("Amostragem")
plt.legend(["Homem","Mulher"])
plt.show()
print(target_counts07)
print("=-" * 70)


#OITAVA PARTE DO CODIGO
plt.figure(figsize=(10,6))
#POSTIVO 
plt.scatter(df["age"][df["target"] == 1],
            df["thalach"] [df["target"] == 1],
            c="salmon")
#NEGATIVO
plt.scatter(df["age"][df["target"] == 0],
            df["thalach"] [df["target"] == 0],
            c="blue")

plt.title("Doença cardiaca em função da idade e da frequencia cardiaca maxima ")
plt.show()


#NONA PARTE DO CODIGO
target_counts09 = pd.crosstab(df["cp"], df["target"])
target_counts09.plot(kind="bar",figsize=(10,6),color=("black","red"))
plt.title("Frequencia Da Doença Cardiaca por ipo de Dor Toracica")
plt.xlabel("Tipo de Dor no Peito")
plt.ylabel("Frequencia")

#DECIMA PARTE DO CODIGO 
corr_matrix = df.corr()
plt.figure(figsize=(15,10))
sns.heatmap(corr_matrix, 
            annot=True, 
            linewidth=0.5, 
            fmt=".2f",
            cmap="YlGnBu")

plt.show()

# 


