#OOP

class PenggunaanHandphone:
    def __init__(self, nama_pemilik, batas_waktu):
        self.nama_pemilik = nama_pemilik
        self.batas_waktu = batas_waktu  # dalam menit
        self.total_waktu = 0

    def tambah_waktu(self, waktu):
        self.total_waktu += waktu
        print(f"Menambahkan {waktu} menit ke waktu bermain. Total waktu bermain sekarang: {self.total_waktu} menit.")
        self.cek_batas()

    def cek_batas(self):
        if self.total_waktu > self.batas_waktu:
            print(f"Peringatan: {self.nama_pemilik}, Anda telah melebihi batas waktu bermain {self.batas_waktu} menit!")

    def reset_waktu(self):
        self.total_waktu = 0
        print("Waktu bermain telah direset.")

# Contoh penggunaan
penggunaan = PenggunaanHandphone("Na Hee Do", 120)

penggunaan.tambah_waktu(30)
penggunaan.tambah_waktu(50)
penggunaan.tambah_waktu(60)
penggunaan.reset_waktu()
penggunaan.tambah_waktu(100)
