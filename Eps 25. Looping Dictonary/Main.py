# Belajar looping dictonary

teman_teman = {
    'cup' : 'ucup surucup',
    'tong' : 'otong surotong',
    'dung' : 'dudung surudung',
    'sep' : 'asep surecep',
    'cuy' : 'ucuy surucuy'
}

print("\n"+" Looping 1 ".center(40,"="))

# Looping Percobaan pertama (yang keluar adalah key nya) 
for teman in teman_teman:
    print(teman) 


print("\n"+" Looping 2 ".center(40,"="))

# Operator untuk mengambil ke / iterable
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)

item = teman_teman.items()
print(item)

for item in teman_teman.items():
    print(item)

for key,value in teman_teman.items():
    print(f"Key : {key}. value : {value}")


