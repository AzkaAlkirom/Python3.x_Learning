# Latihan dulu kitaa, exercise

'''
        Program Kali ini adalah program sederhana
    dari pelajaran pelajaran yang lalu, seperti if else,
elif, bool, variable, input, dan lain lain. gituu dehh bro 
'''
# kita bikin kalkulator gaess hehehe.. dari dulu kecil bingung kekmana kerjanya hehehe
# walau sederhana i hope i can be like founder of calculator hehe
print("\n"+36*"=")
print("\tKalkulator Sederhana")
print(36*"="+"\n")

angka_1 = float(input("Masukkan Angka Pertama        : "))
operator = input("Silahkan Masukkan (+,-,x,/)   : ")
angka_2 = float(input("Masukkan Angka Kedua          : "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Maka Hasil penjumlahan adalah : {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Maka Hasil Pengurangan adalah : {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"Maka Hasil Perkalian adalah   : {hasil}")
elif operator == "/" or operator == ":":
    hasil = angka_1 / angka_2
    print(f"Maka Hasil Pembagian adalah   : {hasil}")
else:
    print(f"Yang bener aja dongg! Au ah, Pusing!! Masa {operator}?")

print("\n"+36*"=")
print("Program telah selesai, Terima kasih")
print(""+36*"="+"\n")

'''
        Yap, ini lah program kalkulator sederhana
    ngga bisa bagus bagus amat, but i hope this usefull
   for me, for you and for all of us. see you, bye broo!
'''