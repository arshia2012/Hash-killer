from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


digest = hashes.Hash(
    hashes.MD5(),
    backend=default_backend
)

text = input()

digest.update(text.encode())

result = digest.finalize()

print(result.hex())