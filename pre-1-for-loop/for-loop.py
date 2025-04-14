# perulangan (LOOP)

#for_loop
#for kondisi 
#    aksi

a = 0 
a += 1 # a = a = 1
print(a)
a += 1 
print(a)
a += 1
print(a)

angka_list = [0,1,2,4,8,10]
for i in angka_list :
   print(f"i sekarang -> {i}")
    
print("ini akhir for 1/n")

#perulangan dengan range 
angka_range = range # diulang 5

for i in angka_range:
    print(f"i sekarang -> {i}")

print("ini akhir for 2 \n")

angka_range2 = range(1,10) # diulang 9/10
for i in angka_range2:
    print(f"i sekarang -> {i}")
    
print("ini akhir for 3 \n")


data_str = "Dikta"
for huruf in data_str:
    print(huruf)

print("akhir perulangan string\n")