class Karyawan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        self.jenisKelamin = None
        self.upahPerHari = None

    def setJenisKelamin(self, jenisKelamin):
        self.jenisKelamin = jenisKelamin

    def setUpahPerHari(self, upahPerHari):
        self.upahPerHari = upahPerHari

    def printInfo(self):
        print("===========Info===========")
        print("Nama\t\t:", self.nama)
        print("Umur\t\t:", self.umur)
        print("Jenis Kelamin\t:", self.jenisKelamin if self.jenisKelamin else "none")
        print("Upah per hari\t:", self.upahPerHari if self.upahPerHari else "None")

    def hitungGajiBulanan(self, jumlahHari):
        if self.upahPerHari is None:
            print("ERROR! Upah perhari belum di inputkan")
        else:
            gaji = self.upahPerHari * jumlahHari
            print("Gaji bulan ini\t: Rp", gaji)

pegawaipertama = Karyawan("Haniif", 90)
pegawaipertama.printInfo()

pegawaikedua = Karyawan("Sindu", 190)
pegawaikedua.setJenisKelamin("Laki-laki")
pegawaikedua.setUpahPerHari(30000)
pegawaikedua.printInfo()

pegawaipertama.hitungGajiBulanan(28)
pegawaikedua.hitungGajiBulanan(30)
