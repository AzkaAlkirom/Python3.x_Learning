# Belajar Operasi List


print("\n"+" Operasi List ".center(38,"="))
data_angka = [3,4,2,1,4,6,5,2,8,9,5,4,3,2]

print(f"data angka : \n{data_angka}")

## cara Count data
jumlah_angka_2 = data_angka.count(2)
jumlah_angka_5 = data_angka.count(5)

print(f"Jumlah Angka 2 : {jumlah_angka_2}")
print(f"Jumlah Angka 5 : {jumlah_angka_5}")

# ambil posisi data  (index) 
# jadi kita bisa cari tau index dalam list itu
print("\n"+" Operasi List 2 ".center(38,"="))

data = ["azka","isnaini","mereka","solo","jogja"]

print(f"data : \n{data}")

index_isnaini = data.index("isnaini") 
index_azka = data.index("azka") 
print(f"dimana isnaini : {index_isnaini}")
# akhirnya bisa tau lokasi dia:) bercanda hehehe..
print(f"dimana Azka    : {index_azka}")

# Mengurutkan List
print("\n"+" Operasi List 3 ".center(38,"="))
print(f"Data sebelum di short : \n{data_angka}")
data_angka.sort()
print(f"sesudah di sort : \n {data_angka}")

# string juga bisa di sort
print(f"data sebelum sort : \n{data}")
data.sort()
print(f"data sesudah sort : \n{data}")

# cara membalik sort list nya
data_angka.reverse()
print(f"Data sesudah di reverse : \n{data_angka}")
data.reverse()
print(f"data sesudah di reverse : \n{data}")






