import hashlib
import random


def generate_wallet(seed):
    random.seed(seed)
    return random.getrandbits(256)


def generate_public_key(private_key):
    return hashlib.sha256(str(private_key).encode()).hexdigest()


def generate_wallet_address(public_key):
    wallet_address = hashlib.sha256(public_key.encode()).hexdigest()[:32]
    return "WALLET-" + wallet_address




seed = 42
private_key = generate_wallet(seed)
public_key = generate_public_key(private_key)
wallet_address = generate_wallet_address(public_key)

if __name__ == "__main__":
    print(f"Seed: {seed}")
    print(f"Private Key (int): {private_key}")
    print(f"Public Key: {public_key}")
    print(f"Wallet Address: {wallet_address}")