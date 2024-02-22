# Date and time

import datetime as dt

print("Tanggal lahir \n")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("bulan \t\t:"))
tahun = int(input("tahun \t\t:"))

tanggalLahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda {tanggalLahir}")
print(f"Hari nya adalah {tanggalLahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal {hari_ini}")
umur_hari = (hari_ini - tanggalLahir).days // 365

print(f"umur anda sekarang {umur_hari} tahun")


