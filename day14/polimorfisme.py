class Kucing:
    def bersuara(self):
        print("Meong! Meong!")

class Anjing:
    def bersuara(self):
        print("Guk! Guk!")

def buat_suara(hewan):
    hewan.bersuara()

anjing = Kucing()
kucing = Anjing()

buat_suara(anjing)
buat_suara(kucing)
