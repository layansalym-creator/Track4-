import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv("data.csv")

X = data[["seed"]]
Y = data["private_key"]

model = LinearRegression()
model.fit(X, Y)

X_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
Y_line = model.predict(X_line)

plt.figure()

plt.scatter(X, Y, label="Actual Data")

plt.plot(X_line, Y_line, color="red", label="AI Prediction Line")

plt.xlabel("Seed")
plt.ylabel("Private Key")
plt.title("Seed vs Private Key with AI Regression Line")
plt.legend()

plt.show()