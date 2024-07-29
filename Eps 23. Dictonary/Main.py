# list --> array 
# mengakses dengan menggunakan index

# List
data_list = ["azka","marsa","nana",]

print("\n"+" List ".center(32,"="))
print(f"ini data list : {data_list[2]}")

# dictonary (dict) --> associative array
# identifier -> key

"""
Bedangnya dengan list adalah jika list pakai index
kalai dictonary menggunakan panggilan alam wahahahaha...
pake key ya manteman, "ka" adalah key nya, "azka" Value nya.
kekgitu lah yaa...
"""

# Dictonary
data_dict = {
    'ka' : 'azka',
    'ms' : 'marsa',
    'na' : 'nana',
    'no' : 123, # angka pun bisa gaes, GG mang ogh
    'list' : data_list # bisa masukkin data list juga, mantep
}

print("\n"+" Dictonary ".center(32,"="))
print(data_dict)
print(f"ini data dict ka : {data_dict["ka"]}")
print(f"ini data dict no : {data_dict["no"]}")
print(f"ini data dict list : {data_dict["list"]}")