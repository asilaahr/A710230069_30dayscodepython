from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def nyalakan_mesin(self):
        pass

    @abstractmethod
    def matikan_mesin(self):
        pass

class SepedaMotor(Kendaraan):
    def nyalakan_mesin(self):
        print("Mesin sepeda motor dinyalakan")

    def matikan_mesin(self):
        print("Mesin sepeda motor dimatikan")

class Truk(Kendaraan):
    def nyalakan_mesin(self):
        print("Mesin truk dinyalakan")

    def matikan_mesin(self):
        print("Mesin truk dimatikan")

# Membuat objek dari kelas SepedaMotor dan Truk
sepeda_motor = SepedaMotor()
truk = Truk()

# Memanggil metode pada objek
sepeda_motor.nyalakan_mesin()  # Output: Mesin sepeda motor dinyalakan
sepeda_motor.matikan_mesin()   # Output: Mesin sepeda motor dimatikan
truk.nyalakan_mesin()          # Output: Mesin truk dinyalakan
truk.matikan_mesin()           # Output: Mesin truk dimatikan