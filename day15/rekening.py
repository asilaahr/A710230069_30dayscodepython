#oop

class RekeningBank:
    def __init__(self, nama_pemilik, saldo):
        self.nama_pemilik = nama_pemilik
        self.saldo = saldo

    def deposit(self, jumlah):
        self.saldo += jumlah
        print(f"Rp{jumlah} telah didepositkan. Saldo baru: Rp{self.saldo}")

    def penarikan(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi untuk penarikan.")
        else:
            self.saldo -= jumlah
            print(f"Rp{jumlah} telah ditarik. Saldo baru: Rp{self.saldo}")

    def tampilkan_saldo(self):
        print(f"Saldo pemilik {self.nama_pemilik}: Rp{self.saldo}")

# Membuat objek dari kelas RekeningBank
rekening1 = RekeningBank("Nawwaf", 1000000)

# Menampilkan saldo awal
rekening1.tampilkan_saldo()

# Melakukan deposit dan penarikan
rekening1.deposit(600000)
rekening1.penarikan(900000)
rekening1.penarikan(900000)
