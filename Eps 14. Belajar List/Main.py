# Belajar Python : list ketika Abis sakit hati (becyandea wkwk)


# 1. list Number
print("\n"+" List : Number ".center(38,"="))
data_int = [1,2,3,4,5,]
print(f"baris Angka : {data_int}")

# 2. List String
print("\n"+" List : String ".center(38,"="))
data_str = ["halo","kamu","gapapa","kan?"]
print(f"seseorang : {data_str}")

# 3. List Boolean
print("\n"+" List : Boolean ".center(38,"="))
data_bool = [True,True,False,True,False]
print(data_bool)

# 4. List Campuran
print("\n"+" List : Campuran ".center(38,"="))
data_campur = [23,"huyuu",True,2,4,"isna",False]
print(f"campur -> {data_campur}")

# 5. List data dalam range
print("\n"+" List : Range ".center(38,"="))
data_range = list(range(1,10)) # rumusnya range(start,stop,step)
print(data_range)

# 6. List compherension (list menggunakan for)
print("\n"+" List : compherension ".center(38,"="))
data_list_pake_for = [i for i in range(1,10)] 
print(data_list_pake_for) # kao mau **2 (pangkat 2) gabisa disini

data_list_pake_for = [i**2 for i in range(1,10)] # bisanya disini
print(data_list_pake_for) 

# 7. List pake for dan if
print("\n"+" List : For & if ".center(38,"="))
data_list_pake_for_if = [i for i in range(1,10) if i != 5]
print(data_list_pake_for_if,"\n")

data_list_pake_for_if = [i for i in range(1,10) if i%2 ==0]
print(f"Genab  : {data_list_pake_for_if}")

data_list_pake_for_if = [i for i in range(1,10) if i%2 !=0]
print(f"Ganjil : {data_list_pake_for_if}")

