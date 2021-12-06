# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:29:19 2021

@author: jofi
"""

class mahasiswa :
    mahasiswacount = 0 
    
    def __init__(self ,nama,nim,tahun):
        self.nama = nama
        self.nim = nim
        self.tahun = tahun
        mahasiswa.mahasiswacount += 1
        
        
    def printmahasiswa(self):
        print("Nama Mahasiswa : " +self.nama)
        print("NIM Mahasiswa :" + self.nim)
        print("Angkatan Tahun :" + self.tahun)


nama = input("Masukkan Nama Mahasiswa :")
nim  = str(input("NIM Mahasiswa :"))
tahun =str(input("Tahun Angkatan :"))


maha = mahasiswa(nama,nim,tahun)
maha.printmahasiswa()

nama2 = input("Nama Mahasiswa :")
nim2  = input("NIM Mahasiswa :")
tahun2= input("Angkatan Tahun :")

maha2 = mahasiswa(nama2,nim2,tahun2)
maha2.printmahasiswa()