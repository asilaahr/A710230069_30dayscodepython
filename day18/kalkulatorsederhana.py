#PYTHON DASAR

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

print("Pilih operasi: +, -, *, /")
operasi = input("Masukkan operasi: ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if operasi == '+':
    hasil = tambah(angka1, angka2)
elif operasi == '-':
    hasil = kurang(angka1, angka2)
elif operasi == '*':
    hasil = kali(angka1, angka2)
elif operasi == '/':
    hasil = bagi(angka1, angka2)
else:
    hasil = "Operasi tidak valid"

print("Hasil: ", hasil)
