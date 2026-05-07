import hashlib
import random
import csv

def generate_wallet(seed):
    random.seed(seed)

    # weak predictable key
    return random.randint(1000, 9999)

def generate_public_key(private_key):
    return hashlib.sha256(str(private_key).encode()).hexdigest()

def generate_wallet_address(public_key):
    wallet_address = hashlib.sha256(public_key.encode()).hexdigest()[:32]
    return "WALLET-" + wallet_address


with open("data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["seed", "private_key"])

    for seed in range(1000):

        private_key = generate_wallet(seed)

        writer.writerow([seed, private_key])


seed = 42

private_key = generate_wallet(seed)

public_key = generate_public_key(private_key)

wallet_address = generate_wallet_address(public_key)

print(f"Seed: {seed}")

print(f"Private Key: {private_key}")

print(f"Wallet Address: {wallet_address}")