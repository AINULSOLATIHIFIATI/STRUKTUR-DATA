# Input jumlah deret dari user
jumlah = int(input("2, 4, 6, 8, 10.: "))

# Cetak deret bilangan genap
for i in range(1, jumlah + 1):
    print(i * 2, end=", ")
