from hashlib import sha256

texto = "Coração"
cod = texto.encode('utf-8')

print(cod)
print(sha256(cod).hexdigest())
htexto = sha256(cod).hexdigest()