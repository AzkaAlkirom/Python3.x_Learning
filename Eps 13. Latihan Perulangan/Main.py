# Latihan perulangan membuat segitiga


sisi = 15

# 1. Menggunakan For

# Dummy Variable
print("\n"+" Awal For ".center(20,"="))
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print(" Akhir For ".center(25,"=")+"\n")

# 2. Menggunakan while
print("\n"+" Awal While ".center(25,"="))

count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print(" Akhir while ".center(25,"=")+"\n")

# 3. Menggunakan while hanya ganjil
print("\n"+" Ganjil saja ".center(25,"="))

count = 1
while True:
    if count%2:
        # Print Jika ganjil
        print("*"*count)
        count += 1
    
    else:
        # Akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print(" Ganjil Saja ".center(25,"=")+"\n")

# 4. Menggunakan while hanya ganjil dengan spasi
print("\n"+" Ganjil dan Spasi ".center(25,"="))

count = 1
spasi = int(sisi/2)
while True:
    if count%2:
        # Print Jika ganjil
        print(" "*spasi,"*"*count)
        count += 1
        spasi -= 1
    else:
        # Akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break

print(" Ganjil dan Spasi ".center(25,"=")+"\n")

# 5. Ketupat
print("\n"+" Bentuk Ketupat ".center(25,"="))
y = int(input('Masukkan Angka :'))
x = 1
a = x
b = y
c = b
while x < y:
    print(('*'*x).center((y),' '))
    x += 2
while a <= b:
    print(('*'*b).center((c),' '))
    b -= 2

print(" Bentuk Ketupat ".center(25,"=")+"\n")


