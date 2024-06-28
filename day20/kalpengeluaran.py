# PYTHON DASAR
# Kalkulator Pengeluaran Harian

def tampilkan_menu():
    print("\n1. Tambah pengeluaran\n2. Tampilkan total pengeluaran\n3. Keluar")

def main():
    pengeluaran = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == '1':
            try:
                jumlah = float(input("Masukkan jumlah pengeluaran: "))
                deskripsi = input("Masukkan deskripsi pengeluaran: ")
                pengeluaran.append((deskripsi, jumlah))
                print(f"Pengeluaran '{deskripsi}' sebesar {jumlah} telah ditambahkan.")
            except ValueError:
                print("Jumlah pengeluaran harus berupa angka.")
                
        elif pilihan == '2':
            total = sum(jumlah for _, jumlah in pengeluaran)
            print("\nDaftar Pengeluaran:")
            for deskripsi, jumlah in pengeluaran:
                print(f"{deskripsi}: {jumlah}")
            print(f"Total pengeluaran: {total}")
                
        elif pilihan == '3':
            print("Terima kasih telah menggunakan kalkulator pengeluaran harian!")
            break
                
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()
