# Input jumlah deret Fibonacci dari user
jumlah = int(input("Masukkan jumlah deret Fibonacci: "))

# Inisialisasi dua nilai pertama
a, b = 0, 1

print("Deret Fibonacci:")
for i in range(jumlah):
    print(a, end=", ")
    a, b = b, a + b  # update nilai a dan b
