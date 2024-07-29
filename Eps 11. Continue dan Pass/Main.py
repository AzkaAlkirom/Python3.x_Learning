#  belajar pasa continue, pass, break 

# pass --->  Dia berfungsi sebagai dummy, tidak akan dijalankan.

# print("\n"+"PASS".center(32,"="))
# angka = 0

# while angka < 5 :
#     angka += 1

#     if angka == 3 :
#         pass # Ini tidak akan di eksekusi

#     print(angka)


# Continue --->  Dia berfungsi sebagai melanjutkan, lihat di program
print("\n"+"Continue".center(32,"="))
nilai = 0
print (f"Ini adalah angka ke -->{nilai}") # Aksi 1

while nilai < 5 :
    nilai += 1
    print (f"Ini adalah angka ke --> {nilai}") # Aksi 1

    if nilai == 3:
        print("Yok bisa yok!!") 
        continue # ini akan membuat loop meloncat ke step selanjutnya

    print("Semangat!!") # Aksi 2

print("Finish!")



