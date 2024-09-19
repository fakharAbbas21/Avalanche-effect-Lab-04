import hashlib


def calculate_sha256(filename):
    with open(filename, 'rb') as file:
        
        while items := file.read(4096):
            sha256.update(items)
    return sha256.hexdigest()


with open('file.txt', 'w') as file:
    file.write("This is a sample text file.")



sha256 = hashlib.sha256()
original_hash = calculate_sha256('file.txt')
print("Original SHA-256 hash:", original_hash)


with open('file.txt', 'rb+') as file:
  
    file.seek(0)
    data = bytearray(file.read())
    
    
    data[0] ^= 0b10000000
    # print(data)
    
    
    file.seek(0)
    file.write(data)


modified_hash = calculate_sha256('file.txt')
print("Modified SHA-256 hash:", modified_hash)

print("Avalanche effect : ")

    
    

