class Mahasiswa:
    def __init__(self, nama, nim, kelas, jum_sks):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.jum_sks = jum_sks

    def PanggilNama(self):
        print(self.nama)

    def PanggilNim(self):
        print(self.nim)

    def PanggilKelas(self):
        print(self.kelas)

    def PanggilSks(self):
        print(str(self.jum_sks))
    
### BATAS ###

Orang1 = Mahasiswa("Gabriel Fico Darius", "121140069", "RB", 22)

Orang1.PanggilNama()
Orang1.PanggilNim()
Orang1.PanggilKelas()
Orang1.PanggilSks()
