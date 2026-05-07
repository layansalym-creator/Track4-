import hashlib
import random
import time


def generate_wallet(seed):
    
    random.seed(seed)
    return random.getrandbits(256)

def generate_public_key(private_key):
    # Generating Public Key using SHA-256
    return hashlib.sha256(str(private_key).encode()).hexdigest()

def generate_wallet_address(public_key):
    # Wallet address is derived from the first 32 characters of the hash
    wallet_address = hashlib.sha256(public_key.encode()).hexdigest()[:32]
    return "WALLET-" + wallet_address


def brute_force_attack(target_address, max_seed_range):
    start_time = time.time() 
    print(f"Starting brute force attack on: {target_address}...")
    
    for trial_seed in range(max_seed_range):
        # Attempting to recreate the wallet using sequential seeds
        trial_private_key = generate_wallet(trial_seed)
        trial_public_key = generate_public_key(trial_private_key)
        trial_address = generate_wallet_address(trial_public_key)
        
        
        if trial_address == target_address:
            end_time = time.time()
            duration = end_time - start_time
            print("\n" + "="*40)
            print(f"SUCCESS! Seed found: {trial_seed}")
            print(f"Private Key (int): {trial_private_key}")
            print(f"Time taken: {duration:.6f} seconds")
            print("="*40)
            return trial_seed, duration
            
    print(f"Attack failed. Seed not found within range: {max_seed_range}")
    return None


if __name__ == "__main__":
    
    
    target_wallet = "WALLET-699a7e35028cdb1ee366ca6ddb136fa3"
    
    
    brute_force_attack(target_wallet, 1000)