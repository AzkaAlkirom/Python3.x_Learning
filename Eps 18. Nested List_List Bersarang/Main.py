# Kita belajar nested list
# Nested list adalah list didalam list

a = [1,2]
b = [3,4]

data_list_bsw = [1,2,3,4,5,6]

print("\n"+" Nested List ".center(37,"="))
print(f"ini data list bsw : {data_list_bsw}")

c = [a,b,5,6,7]

print(f"ini data list Campuran : {c}")

# Contoh Penggunaan

peserta_0 = ["azka",20,"lelaki"]
peserta_1 = ["isnaini",20,"Perempuan"]
peserta_2 = ["mmarshine",20,"lelaki"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"Pseserta : {list_peserta}")

print("\n"+" List Peserta ".center(37,"="))
for peserta in list_peserta :
    print(f"Nama    : {peserta[0]}")
    print(f"Umur    : {peserta[1]}")
    print(f"Kelamin : {peserta[2]}\n")


# dengan reference

list_copy = list_peserta.copy()
print(f"Pseserta : {list_copy}")
peserta_0[0] = "mmarshine"
print(f"Pseserta : {list_copy}")
print(f"Pseserta : {list_peserta}")

