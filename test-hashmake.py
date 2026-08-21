from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


digest = hashes.Hash(
    hashes.MD5(), #change the algorithm if you wanted to get other types of hashed text
    backend=default_backend
)

print("Write your text down")
text = input()

digest.update(text.encode())

result = digest.finalize()

print(result.hex())
