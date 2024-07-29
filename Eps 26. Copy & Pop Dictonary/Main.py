# Belajar Copy Dictonary

teman_teman = {
    'cup' : 'ucup surucup',
    'tong' : 'otong surotong',
    'dung' : 'dudung surudung',
    'sep' : 'asep surecep',
    'cuy' : 'ucuy surucuy'
}

# mengcopy data dengan .copy
print("\n"+" Copy ".center(70,"="))
friend = teman_teman.copy() # kalo ga pake copy nanti bakal keubah

print(f"teman teman : {teman_teman}\n")
print(f"Friend : {friend}\n")

# ini yang keubah
teman_teman['cup'] = "ucup si kerenn"
print(f"teman teman : {teman_teman}\n")
print(f"Friend : {friend}\n")

# mengambil data dengan key nya
print(" Pop ".center(70,"="))
DataAsep = friend.pop("sep")

print(f"Data asep : {DataAsep}")
print(f"Friend : {friend}\n")

# popitem dictonary (mengambil daya terakhir aja)
lastdata = friend.popitem()
print(f"Data Akhir : {lastdata}")
print(f"Friend : {friend}\n")
