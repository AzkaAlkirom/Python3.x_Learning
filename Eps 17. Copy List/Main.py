# belajar pasal menduplikat list

print("\n"+" Menduplikat List ".center(39,"="))

x = ["azka","isnaini","mereka"]
print(f"data x : {x}")

y = x
print(f"data y : {y}")

# kita bakal merubah member x
print("\n"+" Menduplikat List 2 ".center(39,"="))

# ini akan merubah kedua list, dimanapun posisi nya
x[0] = "mmarshine"
y.sort()
print(f"data x : {x}")
print(f"data y : {y}")

# kita check hex addres nya x dan y
print(f"Hex dari x : {hex(id(x))}")
print(f"Hex dari y : {hex(id(y))}")


# menduplikat list dengan copy
print("\n"+" Menduplikat List 3 ".center(39,"="))
z = x.copy() # bertujuan untuk meng copy list

print(f"Hex dari x : {hex(id(x))}")
print(f"Hex dari y : {hex(id(y))}")
print(f"Hex dari z : {hex(id(z))}")

# Kita Buktikan
print(f"data x : {x}")
print(f"data y : {y}")
print(f"data z : {z}")

# Percobaan 1
z[0] = "nana"
print(f"data x : {x}")
print(f"data y : {y}")
print(f"data z : {z}")

# Percobaan 2
x[0] = "ayun"
print(f"data x : {x}")
print(f"data y : {y}")
print(f"data z : {z}")
