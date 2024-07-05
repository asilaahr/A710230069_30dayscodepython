#python dasar

try:
    angka = int(input("Masukkan sebuah angka: "))
    print(f"Anda memasukkan angka: {angka}")
except ValueError:
    print("Input bukan angka yang valid.")
