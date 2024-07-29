# Kita belajar pasa looping list dan Enumerate


# for looping 
print("\n"+" for Looping ".center(40,"="))

kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
    print(f"Angka : {angka}")

peserta = ["azka","kaka","kazka"]

for nama in peserta:
    print(f"Nama : {nama}")

# For loop dan For range 
print("\n"+" For loop dan For Range ".center(40,"="))

kumpulan_angka = [10,5,4,6,2,5]

panjang = len(kumpulan_angka)

for i in range(panjang) : # ini yang mode agak panjang nya
    print(f"jumlah Angka : {kumpulan_angka[i]}") # pendeknya diatas


# while loop
print("\n"+" while list ".center(40,"="))
kumpulan_angka = [10,5,4,6,2,5]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"jumlah Angka : {kumpulan_angka[i]}")    
    i += 1


# kalo pake compherention
print("\n"+" list Compherention ".center(40,"="))
data = ["ucup",1,2,3,"azka"]

[print(f"data : {i}")for i in data]

kumpulan_angka = [10,5,4,6,2,5]

angka_kuadrat = [i**2 for i in kumpulan_angka]
print(angka_kuadrat)


# enumerate
print("\n"+" list enumarate ".center(40,"="))
data = ["ucup",1,2,3,"azka"]

for index,data in enumerate(data):
    print(f"index  : {index}    data : {data}")

