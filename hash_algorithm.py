import re

class HashDetector:
    @staticmethod
    def detect(hash_string):
        h = hash_string.strip()
        length = len(h)
        
        patterns = {
            'MD5': {
                'length': 32,
                'pattern': r'^[a-fA-F0-9]{32}$'
            },
            'SHA1': {
                'length': 40,
                'pattern': r'^[a-fA-F0-9]{40}$'
            },
            'SHA256': {
                'length': 64,
                'pattern': r'^[a-fA-F0-9]{64}$'
            },
            'NTLM': {
                'length': 32,
                'pattern': r'^[a-fA-F0-9]{32}$'
            },
            'bcrypt': {
                'pattern': r'^\$2[ayb]\$.{56}$'
            },
            'MD5-crypt': {
                'pattern': r'^\$1\$[A-Za-z0-9./]{8}\$[A-Za-z0-9./]{22}$'
            },
            'SHA256-crypt': {
                'pattern': r'^\$5\$[A-Za-z0-9./]{8}\$[A-Za-z0-9./]{43}$'
            },
            'SHA512-crypt': {
                'pattern': r'^\$6\$[A-Za-z0-9./]{8}\$[A-Za-z0-9./]{86}$'
            }
        }
        
        detected = []
        for algo, info in patterns.items():
            if 'pattern' in info and re.match(info['pattern'], h):
                detected.append(algo)
        
        if not detected:
            for algo, info in patterns.items():
                if info.get('length') == length:
                    detected.append(algo)
        
        if len(detected) > 1 and 'MD5' in detected and 'NTLM' in detected:
            detected.remove('NTLM')
        
        return detected[0] if detected else 'Unknown'