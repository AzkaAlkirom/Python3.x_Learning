# nesting dictonary

import datetime

mahasiswa1 = {
    'nama' : "azka Alkirom",
    'nim' : "140221234",
    'sks_lulus' : 130,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2004,6,13)
}

mahasiswa2 = {
    'nama' : "Otong surotong",
    'nim' : "140221234",
    'sks_lulus' : 140,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2002,10,10)
}

mahasiswa3 = {
    'nama' : "Asep si Kasyep",
    'nim' : "140221234",
    'sks_lulus' : 100,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2000,2,29)
}

data_mahasiswa = {
    'MAH001' : mahasiswa1,
    'MAH002' : mahasiswa2,
    'MAH003' : mahasiswa3
}

print(f"{'key':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")

