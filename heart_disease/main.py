import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#from sklearn.model_selection import train_test_split

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



