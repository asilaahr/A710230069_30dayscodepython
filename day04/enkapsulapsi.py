#enkapsulapsi [oop python]

class RekeningBank:
    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.__saldo = saldo  # Atribut privat

    def deposit(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            return True
        return False

    def tarik_tunai(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            return True
        return False

    def get_saldo(self):
        return self.__saldo

# Membuat objek RekeningBank
rekening = RekeningBank("Alice", 1000)
rekening.deposit(500)
print(rekening.get_saldo())  # Output: 1500
print(rekening.tarik_tunai(2000)) # Output: False
print(rekening.get_saldo())  # Output: 1500
