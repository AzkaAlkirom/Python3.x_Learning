# Belajar Operasi dictonary


data_dict = {
    'cup' : 'ucup surucup',
    'tong' : 'otong surotong',
    'dung' : 'dudung surudung'
}

# Mencari tau panjang dictonary
print("\n"+" Lendict ".center(40,"="))
Lendict = len(data_dict)
print(f"panjang data adalah : {Lendict}")

# mengecheck key exist atau tidak
print("\n"+" Check key ".center(40,"="))
key = 'cup'
checkkey =  key in data_dict
print(f"apakah {key} ada di data : {checkkey}")

# Mengakses value (read) dengan get
print("\n"+" Read with get ".center(40,"="))
print(data_dict["cup"])
print(data_dict.get('cup'))
print(data_dict.get('kiw','duh, gaada nih key itu'))

# Mengupdate data
print("\n"+" Update data ".center(40,"="))
data_dict["cup"] = "ucup asoy abiesz"
print(data_dict)
data_dict["tong"] = "otong slebey anjay"
print(data_dict)

data_dict.update({'cup':"ucup surucup"})
print(data_dict)
data_dict.update({'kaa':"Azka alkirom"})
print(data_dict)

# mendelete data di dictonary
print("\n"+" Delete data ".center(40,"="))
del data_dict['kaa']
print(data_dict)