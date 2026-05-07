from wallet import private_key
import time
import numpy as np
from sklearn.linear_model import LinearRegression


def rsa_decrypt_vulnerable(ciphertext, private_key, mod):
    result = 1
    for bit in bin(private_key)[2:]:
        result = (result * result) % mod
        time.sleep(0.0001)

        if bit == '1':
            result = (result * ciphertext) % mod
            time.sleep(0.0002)

    return result



print("[*] Collecting timing data for training...")

X_times = []
y_lengths = []

for length in [8, 16, 24, 32]:
    for _ in range(10):
        key = np.random.randint(1 << (length - 1), (1 << length) - 1)

        start = time.perf_counter()
        rsa_decrypt_vulnerable(12345, key, 1000000007)
        elapsed = time.perf_counter() - start

        X_times.append([elapsed])
        y_lengths.append(length)

model = LinearRegression()
model.fit(X_times, y_lengths)

print("[+] Model trained successfully.")



print("\n--- Simulating attack on unknown key ---")

secret_length = 20
secret_key = np.random.randint(
    1 << (secret_length - 1),
    (1 << secret_length) - 1
)

with open("key.txt", "w") as f:
    f.write(str(secret_key))

start = time.perf_counter()
rsa_decrypt_vulnerable(12345, secret_key, 1000000007)
measured_time = time.perf_counter() - start

predicted = model.predict([[measured_time]])[0]

print(f"Measured time: {measured_time:.6f} seconds")
print(f"Actual key length: {secret_length} bits")
print(f"Predicted by AI: {round(predicted)} bits")