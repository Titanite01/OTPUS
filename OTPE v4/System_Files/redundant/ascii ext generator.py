charset =""

for i in range(10, 256):
    x = (f"{bytes([i]).decode('cp1252', errors='replace')}")
    charset = charset + x

print(charset)