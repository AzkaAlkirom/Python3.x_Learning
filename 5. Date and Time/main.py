# Date and Time (Exercise)

import datetime as dt

## Ini untuk  Penjelasan aja
hari_ini = dt.date.today() #ini mengeluarkan tanggal hari ini 
print(hari_ini)
print(f"Hari ini adalah hari : {hari_ini:%A}")
# jadi (:%A) itu untuk Hari nya

tanggal = dt.date(2004,6,13)
print(tanggal)
print(f"Hari ini adalah hari : {tanggal:%A}")

"""
    Sekarang Kita coba Buat Pendeteksi Tanggal Lahir
"""

print("\n"+9*"="+"Input Data Anda"+"="*9)
print(" Silahkan Masukkan Tanggal, Bulan \n\tdan tahun lahir anda")
tanggal = int(input("Masukkan Tanggal lahir anda \t: "))
bulan = int(input("Masukkan Bulan lahir anda \t: "))
tahun = int(input("Masukkan Tahun lahir anda \t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"\nTanggal Lahir anda        : {tanggal_lahir}")

hari_ini = dt.date.today() # ini hari ini
print(f"Hari ini Tanggal          : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir 
umur_tahun = umur_hari.days // 365 # kita pake left division
umur_sisa_bulan = (umur_hari.days % 365) // 30
print(f"Hari anda lahir adalah    : {tanggal_lahir:%A}")
print(f"Umur anda sekarang adalah : {umur_tahun} Tahun {umur_sisa_bulan} Bulan1")

"""
    jadi itu ya manteman, kita belajar :
1. datetime (tanggal dan waktu)
2. kita belajar :%A untuk mengoutput kan hari
3. kita udah bikin Pendeteksi tanggal lagir, anjayyy asoyy:)
"""
# Maap ya banyak becanda:(