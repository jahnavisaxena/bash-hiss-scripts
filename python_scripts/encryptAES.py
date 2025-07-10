from Crypto.Cipher import AES , PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import os

ZIP_FILE = "XX.zip"
ENCRYPTED_FILE = "XX_encrypted.bin"
ENCRYPTED_AES_KEY = "aes_key_encrypted.bin"
PUBLIC_KEY = "public_key.pem"
PRIVATE_KEY = "private_key.pem"

def generate_rsa_keys():
    if not os.path.exists(PUBLIC_KEY) or not os.path.exists(PRIVATE_KEY):
        key = RSA.generate(2048)
        with open(PRIVATE_KEY, 'wb') as f:
            f.write(key.export_key())
        with open(PUBLIC_KEY, 'wb') as f:
            f.write(key.publickey().export_key())
        print("[+] RSA Key pair generated.")

def encrypt_zip_file():
    aes_key = get_random_bytes(16)  # AES-128
    iv = get_random_bytes(16)

    with open(ZIP_FILE, 'rb') as f:
        zip_data = f.read()

    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(zip_data, AES.block_size))

    with open(ENCRYPTED_FILE, 'wb') as f:
        f.write(iv + encrypted_data)

    print(f"[+] Encrypted file saved as: {ENCRYPTED_FILE}")
    return aes_key

def encrypt_aes_key(aes_key):
    with open(PUBLIC_KEY, 'rb') as f:
        rsa_key = RSA.import_key(f.read())
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    encrypted_key = cipher_rsa.encrypt(aes_key)
    with open(ENCRYPTED_AES_KEY, 'wb') as f:
        f.write(encrypted_key)
    print(f"[+] AES key encrypted as: {ENCRYPTED_AES_KEY}")

def main():
    generate_rsa_keys()                # Step 1: RSA Key generation (if not already done)
    aes_key = encrypt_zip_file()       # Step 2: Encrypt zip using AES
    encrypt_aes_key(aes_key)           # Step 3: Encrypt AES key with RSA

    print("\n Encryption complete. Send:")
    print(f"- {ENCRYPTED_FILE}")
    print(f"- {ENCRYPTED_AES_KEY}")

if __name__ == "__main__":
    main()
