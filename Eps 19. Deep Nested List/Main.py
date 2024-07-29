# Kita belajar deep nested list

# kita mekaren belajar nested list yang sederhana yak

print("\n"+" Deep Nested List ".center(40,"="))
data_0 = [1,2]
data_1 = [3,4]

data_2L = [data_0,data_1]
data_2L_copy = data_2L.copy() 
print(f"data : {data_2L}")
print(f"data : {data_2L_copy}")

## Cara Mengambil data dari nested list

# jadi ini data_2L[list keberapa][dalam list]
data = data_2L[0][1] 
print(f"Data yang diambil : {data}")

# kita check address nya semua dulu 
print("\n"+" Addres data ".center(40,"="))

print(f"Address dari data         : {hex(id(data))}")
print(f"Address dari data_2L      : {hex(id(data_2L))}")
print(f"Address dari data_2L_copy : {hex(id(data_2L_copy))}")

'''
Bisa dilihat bahwa addres dari data_2L dan data copy an nya
itu sudah berbeda, namun data didalam nya masih sama address nya
nanti jika kita ubah maka akan mengubah semuanya. jadi gimana?
'''

print("\n"+"Data yang sudah kita ambil".center(40,"="))
print(f"Address dari data_2L      : {hex(id(data_2L[0]))}")
print(f"Address dari data_2L_copy : {hex(id(data_2L_copy[0]))}")

'''
bisa dilihat dibawah ini
'''

data_2L[0][1] = 5 # angka 2 dalam data_0 ku ubah jadi 5
data_2L[1] = 9 # angka 2 dalam data_0 ku ubah jadi 5
print(f"data 2L      : {data_2L}")
print(f"data 2L Copy : {data_2L_copy}")

'''
kesimpulanya adalah didalam copy :
list 1. nya bisa di copy
list 2. nya bisa juga
dan angka nya juga

maka dari itu kita perlu menggunakan dep.copy setelah ini
'''

print("\n"+" Deep Copy ".center(40,"="))
# Kita pakai deepcopy

from copy import deepcopy

data_2L = [data_0,data_1]
data_2L_deepcopy = deepcopy(data_2L)

print(f"Address dari data_2L          : {hex(id(data_2L))}")
print(f"Address dari data_2L_deepcopy : {hex(id(data_2L_deepcopy))}")
print("\n"+" deep list terbukti ".center(40,"="))
print(f"Address dari data_2L          : {hex(id(data_2L[0]))}")
print(f"Address dari data_2L_deepcopy : {hex(id(data_2L_deepcopy[0]))}")

print("\n"+" Pengubahan data 2 ".center(40,"="))
data_2L[0][1] = 30
print(f"data 2L            : {data_2L}")
print(f"data 2L Copy       : {data_2L_copy}")
print(f"data 2L deep copy  : {data_2L_deepcopy}")
