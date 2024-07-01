# Kita belajar pasal while loop (perulangan) 

"""
            Dalam perulangan kita menggunakan While
    kenapa while? itu buat perulangan ya gaes
 gapapaa, nanti jugaa sembuh kalo luka diulang ulang hehehehe...
"""

# while kondisi :
#     aksi 1
#     aksi 2

# Perulangan ke 1 
angka = 10

while angka > 5 :
    print(f"ini ke-{angka} kamu udah berjuang")

print("kamu boleh rehat kok")


# Perulangan ke 2 
angka = 0 # ini nanti di check sama while (lebih ato kurang?)
print(f"ini angka ke ->{angka}\n")

while angka < 5 : # setelah di check rupanya kurang bro!
    angka += 1 # kalo angka masih kurang dari 5 nanti di tambahin 1
    print(f"ini angka ke ->{angka}")
    print("Kamu bisa, Jangan Galau lagi yaa")

print("\nHopp Kamu udah ga Galau kan? hehehe..")

# Ada satu lagi nih, sama kek tadi tapi di pakein (if) dan (break) 
i = 0
while i < 100:
    print(f"haii ini hari ke-{i} setelah kamu pisah")
    i += 1
    if i == 15:
        break # break belum kita pelajari di bab sebelumnya tapi gapapa

print("hooopppp!!!")

"""
Jadi, kalo hasilnyaTrue maka akan berulang tanpa henti
trus gimana biar false, kita tambahin deh sampe angka = 0 itu jadi
angka yang sama dengan 5 hehehe, jadi False kalo angka nya dia udah sama
dengan 5 atau lebih hehehe. kasian yaa 5, dia cuma mau berhenti kalu udah ada yang
lebih dari dia. baik banget rupanyaa hehehehe.. semangat 5, kamu udah banyak banget effort kok
"""

# Begitu lahh hehehe...