from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.metrics import classification_report

df = pd.read_csv("heart-disease.csv")

print(df.head())

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

#print(X_train.head())
#print(X_test.head())

model = RandomForestClassifier(random_state=1)

model.fit(X_train, y_train)
Y_pred = model.predict(X_test)
print(classification_report(y_test, Y_pred))