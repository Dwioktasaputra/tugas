# Class
class Mobil:
    # Instance
    def __init__(self, merk):
        self.merk = merk
        self.plat_nomor = ""
        self.tahun = ""

    # Method 1
    def printMobil(self):
        print("Plat Nomor : ", self.plat_nomor)
        print("Merk Mobil : ", self.merk)
        print("Tahun Mobil : ", self.tahun)
    
    # Method 2
    def servis(self, kondisi):
        print("Mobil telah diservis")
        print(kondisi)

# Objek
mobil1 = Mobil("Toyota")
mobil2 = Mobil("Honda")

# Value
mobil1.plat_nomor = "B 1234 XYZ"
mobil1.tahun = "2020"
mobil2.plat_nomor = "B 5678 ABC"
mobil2.tahun = "2019"

# Pemanggilan Method
mobil1.printMobil()
mobil1.servis("Ganti oli dan cek rem")
mobil2.printMobil()
mobil2.servis("Ganti oli dan cek rem")