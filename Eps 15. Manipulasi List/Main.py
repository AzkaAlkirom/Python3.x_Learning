# Belajar Python : Manipulasi list ketika Abis Pisahan (becyandea wkwk)

# dalam list itu ada index, apa itu ?
# index tu kaya gini mentemen:)

# index  0(-2)  1(-1)  
data = ["azka","isnaini"]

# kita coba ambil data dari list
print("\n"+" Index ".center(35,"="))
data_0 = data[0]
print(f"data pertama (index 0) : {data_0}")

data_terakhir = data[-1]
print(f"ini yang terakhir adalah : {data_terakhir}")

# cara mengambil info jumlah list
jumlah_data = len(data)
print(f"Jumlah data : {jumlah_data}")

## manipulasi data si list
print("\n"+" Manipulasi ".center(35,"="))

# menambahkan data pada list data
print(f"data sebelumnya ditambah : \n{data}")

data.insert(2,"zafaa") #jadi insert ini buat nambahin data ya
print(f"Data sesudahnya ditambah : \n{data} ")

# ingin menambah di akhir
data.append("mereka") #ini otomatis di tambah ke urutan akhir
print(f"Ini data sudah ditambah  : \n{data}")

# menambahkan list dengan list
data_baru = ["solo","jogja"]
data.extend(data_baru)

print(f"Ini data gabungan : \n{data}")

## Merubah list yang didalam data
# kita gantikan index 0 jadi "mmarshine" 
data[0] = "mmarshine"

print(f"ada orang baru : \n{data}")

# mau menghapus sala satu dalam list data

data.remove("zafaa") # bisa error kalau tulisan nya berbeda (besar kecil huruf)
print(f"data setelah zafa mati : \n{data}") 

# bisa juga me-remove paling belakang
data.pop()
print(f"gaada lagi kenangan jogja : \n{data}") 

# bisa juga ambil list data data terakhir
data_terakhir = data.pop() # jadi "solo" adalah list terakhir dari data
print(f"ini tempat kita dulu, aku mau pindah kesana : \n{data_terakhir}")


