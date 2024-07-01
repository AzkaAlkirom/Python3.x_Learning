#  kita belajar String width and Alignment

# Data
data_nama = "Zafaa Abid Hibbanillah"
data_umur = 15
data_tinggi = 165.5
data_nomor_sepatu = 40

# String Standard
data_string = f"Nama : {data_nama}. Umur : {data_umur}. Tinggi : {data_tinggi}. Size Sepatu : {data_nomor_sepatu}"
print("\n"+7*"="+" Data String Standard "+"="*7)
print(data_string)

# String Multiline Menggunakan Enter atau Newline -> \n
data_string = f"Nama : {data_nama}.\nUmur : {data_umur}.\nTinggi : {data_tinggi}.\nSize Sepatu : {data_nomor_sepatu}"
print("\n"+7*"="+" Data String Multiline "+"="*7)
print(data_string)


# String Multiline (Kutip Triplets)
data_string = f"""Nama : {data_nama}
Umur : {data_umur}
Tinggi : {data_tinggi}
Nomor Sepatu : {data_nomor_sepatu}
""" 
print("\n"+7*"="+" Data String Multiline "+"="*7)
print(data_string)

# Mengatur Lebar
data_nama = "Zafaa"
data_string = f"""
Nama   : {data_nama:>5}
Umur   : {data_umur:>5}
Tinggi : {data_tinggi:>5}
Sepatu : {data_nomor_sepatu:>5}
""" 
print("\n"+7*"="+" Data String Multiline "+"="*7)
print(data_string)
