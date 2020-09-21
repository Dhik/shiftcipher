def enkrip(string, shift):
    enc = ''
    for char in string:
        if char == ' ': 
            enc = enc + char #untuk menambahkan char kedalam variabel
        elif char.isupper(): #isupper untuk mengecek uppercase, kalau uppercase akan dikembalikan nilai true
            enc = enc + chr((ord(char) + shift - 65) % 26 + 65) #dijumlah 65 karena huruf uppercase berawal dari angka ASCII 65
        else:  #untuk kasus lowercase
            enc = enc + chr((ord(char) + shift - 97) % 26 + 97) #dijumlah 97 karena huruf lowercase berawal dari angka ASCII 97 
    return enc

text = input("Masukan string: ")
s = int(input("Masukan key shift: "))
print("Plaintext: ", text)
print("Ciphertext: ", enkrip(text, s))