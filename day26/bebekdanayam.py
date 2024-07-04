#oop

class Hewan:
  def __init__(self, nama):
    self.nama = nama

  def bersuara(self):
    print(f"{self.nama} bersuara!")

class Bebek(Hewan):
  def bersuara(self):
    print(f"{self.nama} kwek-kwek!")

class Ayam(Hewan):
  def bersuara(self):
    print(f"{self.nama} kukuruyuk!")

bebek = Bebek("bebek")
ayam = Ayam("ayam")

bebek.bersuara()
ayam.bersuara()
