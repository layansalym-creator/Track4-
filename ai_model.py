import pandas as pd
from sklearn.linear_model import LinearRegression
import random

data = pd.read_csv("data.csv")

X = data[["seed"]]
y = data["private_key"]

model = LinearRegression()
model.fit(X, y)

test_seed = pd.DataFrame([[42]], columns=["seed"])

predicted = model.predict(test_seed)

print("Predicted Private Key:", predicted)


random.seed(42)

real_key = random.randint(1000, 9999)

print("Real Private Key:", real_key)