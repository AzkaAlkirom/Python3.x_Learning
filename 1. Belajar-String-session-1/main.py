# 1. Cara membuat string 
print('\n=============== Part One ==============')
data = "ini adalah string" 
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. menggunakan single quote '...'
    2. menggunakan double quote "..."
'''

data = 'menggunakan single quote' 
print(data)

data = "menggunakan Double Quote" 
print(data)

print('"apa kabar? Kamu ga kangen?hehehe.."')
print("'kamu makin kuat ya tanpa aku, kerenn..'")
print("iyaa hari ini hari Jum'at, kenapa?")


# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('iyaa hari ini hari Jum\'at, kenapa?')
print('G\'day isn\'t it? but you not with me:\')')

# Backlast
print('C:\\user\\Azka')

# Tab (\t) untuk memberikan jeda
print('Nanaa\t\tAzka, saling berjauhan') #:(

# Backspace (\b) ini untuk mendekatkan
print("Isnaini \bAzka, saling berdekatan") #hehehehe:)

# New line
print("Baris Pertama.\nBaris Kedua.") # LF : Line Feed -> Linux, MacOS
print("Baris Pertama.\rBaris Kedua.") # CR : Carrieage Return -> commadore,acorn, Lips
print("Baris Pertama.\n\rBaris Kedua.") # CRLF : Carrieage Return Line Feed -> Dipake sama Windows

# 3. String Literal atau Raw 
print("C:\new Folder") # Bakal Salah

print("C:\\new Folder") # Bakal susah kalo kebanyakan ini (\\)

print(r'C:\new Folder\fiw') # bisa pake raw string, jadi full string

#  multiline literal string
print('''
Nama : Isnaini
Status : My Last Love 
Pasangan : Azka (Bismillah)
''')

#  multiline literal string dan Raw
print(r"""
Nama : Ucup
Kelas : Kelas 3 SMA
Website : www.UcupMania.com/Home/Hobby/muncak
# """)

'''
                Next Part Two 
        of Operasi dan Manipulasi String
'''
print('\n=========== Part Two ===========')

# 1. Menyambung string (concatenate)
nama_pertama = 'Zafaa'
nama_tengah = 'Abid'
nama_akhir = 'Hibbanillah'

nama_lengkap = nama_pertama +' '+ nama_tengah +' '+ nama_akhir
print('Nama :',nama_lengkap)

# 2. Menghitung Panjang dari String
panjang = len(nama_lengkap)
print('Jumlah Abjat :',panjang)

# 3. Operator Untuk String

# mengechek apakah ada komponen char atau string di string
a = "isnaini"
status = a in nama_lengkap
print(a + " ada di " + nama_lengkap + " : " + str(status))

# is ni=ot itu kebalikanya, we know bout that laaahh :\
b = "Zafaa"
status = b not in nama_lengkap
print(b + " tidak ada di " + nama_lengkap + " : " + str(status))

# Mengulang, pakai kali (*)
print("wkwk"*5)
print(5*"wkwk")

# Indexing : mengambil data dari string (memotong - motong)
print("Index ke-0 : "+ nama_lengkap[0])
print("Index ke-6 : "+ nama_lengkap[6])
print("Index ke-(-1) : "+ nama_lengkap[-1])
print("Index ke-(-2) : "+ nama_lengkap[-2])
print("Index ke-[0,3] : "+ nama_lengkap[0:4])
print("Index ke-[3,7] : "+ nama_lengkap[3:8])
print("Index ke-[0,2,4,6,8,10] : "+ nama_lengkap[0:10:2])

# item paling kecil ASSCI nya
print("paling kecil : " + min(nama_lengkap)) 

# item paling Besar ASSCI nya
print("paling Besar: " + max(nama_lengkap)) 

assci_code = ord(" ") #untuk mengetahui ASSCI nya
print("ASSCI Code untuk spasi adalah " + str(assci_code))
data = 117 # Ini nama ASSCI 
print("Char untuk ASCII 117 adalah : " + chr(data))

# 4. Operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o") # data adalah objekcount adalah method nya
print("Jumlah O pada " + data + " = " + str(jumlah))

"""
String adalah salahsatu tipe data di Python
penting banget karna bakal dipake banyak banget di dalam python
nanti dipake di kelas OOP (Object Oriented Programming)
"""