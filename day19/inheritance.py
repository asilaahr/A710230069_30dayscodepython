class Kendaraan:
    def __init__(self, merk, model):
        self.merk = merk
        self.model = model
    
    def deskripsi(self):
        print(f"Merk: {self.merk}, Model: {self.model}")

class Mobil(Kendaraan):
    def __init__(self, merk, model, jumlah_pintu):
        super().__init__(merk, model)
        self.jumlah_pintu = jumlah_pintu
    
    def info_mobil(self):
        self.deskripsi()
        print(f"Jumlah Pintu: {self.jumlah_pintu}")

mobil_saya = Mobil("Mitsubishi", "Pajero", 4)
mobil_saya.info_mobil()
