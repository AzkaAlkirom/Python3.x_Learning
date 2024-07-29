# kita belajar pasal Break


# Kita Buat seperti kemaren dulu (continue dan pass)

# Contoh 1 untuk penggunaan break
angka = 0

print("\n"+"Finihs".center(22,"="))
while angka < 5:
    angka += 1
    print(f"Ini angka ke --> {angka}")

    if angka == 3:
        print("Yuhuu!! nice!")
        break #ini akan memberhentikan program

    print("Mantepp!!")

print("Finihs".center(22,"=")+"\n")


# Contoh 2 untuk Penggunaan Break
data_int = int(input("MAsukkan angka = "))
angka = 0

print("\n"+"Finihs".center(22,"="))
while True:
    angka += 1
    print(f"Count {angka}")

    if angka == data_int:
        print("Yuhuu!! nice!")
        break 

    print("Mantepp!!")

print("Finihs".center(22,"=")+"\n")
 
