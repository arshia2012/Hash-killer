import hashlib
import bcrypt
from hash_algorithm import HashDetector
import BetterRich as brich

class HashCracker:
    def crack(self, target_hash, dictionary_file):
        algo = HashDetector.detect(target_hash)
        brich.good(f"[+] hash algorithm detected: {algo}")
        
        if algo == 'Unknown':
            return brich.warn(f"[-] hash detector didn't find this algorithm in the map, we will add more soon ;)")
        
        with open(dictionary_file, 'r', encoding='utf-8', errors='ignore') as f:
            for word in f:
                word = word.strip()
                
                if algo == 'bcrypt':
                    # bcrypt
                    if self._check_bcrypt(word, target_hash):
                        return brich.good(f"Password found: {word}")
                else:
                    hashed = self._hash_word(word, algo)
                    if hashed == target_hash:
                        return brich.good(f"Password found: {word}")
            else:
                return brich.warn("[-] Password isn't in passwords wordlist")
    def _hash_word(self, word, algo):
        if algo == 'MD5':
            return hashlib.md5(word.encode()).hexdigest()
        elif algo == 'SHA1':
            return hashlib.sha1(word.encode()).hexdigest()
        elif algo == 'SHA256':
            return hashlib.sha256(word.encode()).hexdigest()
        elif algo == 'NTLM':
            return hashlib.new('md4', word.encode('utf-16le')).hexdigest()
        else:
            raise ValueError(f"algorithm not found: {algo}")
    
    def _check_bcrypt(self, word, target_hash):
        try:
            return bcrypt.checkpw(word.encode('utf-8'), target_hash.encode('utf-8'))
        except ValueError:
            return False