from sklearn.datasets import fetch_california_housing

# Carrega o dataset como DataFrame
housing = fetch_california_housing(as_frame=True)
df = housing.frame

print(df.head())        # primeiras linhas
print(housing.DESCR)    # descrição completa

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Separa variáveis preditoras (X) e alvo (y)
X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

# Divide em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Cria e treina o modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Faz previsões
y_pred = modelo.predict(X_test)

# Avalia desempenho
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.2f}")
print(f"R²: {r2:.2f}")

import seaborn as sns
sns.scatterplot(x=df["MedInc"], y=df["MedHouseVal"])
