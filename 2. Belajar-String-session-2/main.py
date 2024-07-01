# Operator dalam bentuk Method

# Merubah Case dalam string


# merubah semua ke uppercase
print("\n======== Uppercase ========")
salam = "bro!"
print("Normal : " + salam)
salam = salam.upper()
print("Upper  : " + salam)

# merubah semua ke Lowercase
print("\n======== Lowercase ========")
alay = "AkU keCe AabbBiiIeszzZzz"
print("Normal : " + alay)
alay = alay.lower()
print("Lower  : " + alay)

print("\n======== Pengecekan ========")     

## Pengecekan dengan isX method

# contoh pengecekan dengan lower
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool : (true/false)
print(salam + " is Lower : " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool : (true/false)
print(salam + " is Upper : " + str(apakah_upper))

# ada banyak method is ini, seperti :
# isalpha()   <-- untuk mengecheck semua huruf
# isalnum()   <-- untuk huruf dan angka
# isdecimal() <-- untuk angka saja (all in angka boloo)
# isspace()   <-- spasi, tab, newline \n
# istitle()   <--  semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # Hasil pasti bool : (true/false)
print(judul + " is title : " + str(cek_judul))

print("\n======== Pengecekan V.2 ========")     
## Ngecheck komponen startswith() endswith() <-- Keren
print("Kalimat awal : 'Sangjangnim Oppa'")
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start : " + str(cek_start)) 
# jadi kata awal dari "Sangjangnim Oppa" itu dimulai dengan kata
# "Sangjangnim", jadi bener yaa kalo true but harus bener bener sama

cek_end = "Sangjangnim Oppa".endswith("Oppa")
print("End   : " + str(cek_end))
# kalo ini kebalikanya, jadi kalimat "Sangjangnim Oppak"
# berakhir dengan kata "Oppak", jadi true.

"""
Jadi dari kesimpulanya itu, startswith() dan endswith()
harus sama dengan isi kalimatnya, uppercase maupun lowecase nya.
Mereka itu sangat sensitif wahahahahahahaha
"""

print("\n======== Penggabungan ========")     
# Penggabungan komponen join() 
pisah = ['aku','kangen','banget']
gabungan = ','.join(pisah)
print(pisah) # awalnya kekgini
print(gabungan) # jadi kekgini

gabungan = ' '.join(pisah)
print(gabungan) # dan jadi kekgini

gabungan = ' ehm '.join(pisah)
print(gabungan) # kekgini jugaa hehehehe
# kesimpulanya join() : cari sendiri, bingung ogh
# tapi paham kan? hehehehe.. WAHAHAHAHAHA..

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

print("\n=========== Alokasi karakter ===========")     
# apa niehh alokasi karakter, hmm...
## Ada juga rjust()  <- untuk ke kanan.
## Ada juga ljust()  <- untuk ke kiri.
## ada juga center() <- untuk ke Tengah.
kanan = "Kanan".rjust(39)
print("'"+kanan+"'") 

kiri = "Kiri".ljust(39)
print("'"+kiri+"'") 

Tengah = "Tengah".center(39) 
print("'"+Tengah+"'") 
print("'"+Tengah+"'") 

# Output nya bisa kita ubah dengan
# Example : 
Tengah = "Tengah".center(39,"=") #Anjayyyyyyyyy GG 
print("'"+Tengah+"'") # berguna buat saya yang suka kerapian

# Kebalikanya --> strip()
Tengah = Tengah.strip("=") # Menghilangkan Tanda "="
print(Tengah) # Begituu kawannkuuuhh!!
