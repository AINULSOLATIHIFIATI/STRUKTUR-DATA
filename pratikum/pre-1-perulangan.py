# Menentukan jumlah baris
n = 5  # kamu bisa ubah sesuai kebutuhan

for i in range(1, n + 1):
    bintang = '*' * (2 * i - 1)  # jumlah bintang ganjil: 1, 3, 5, ...
    print(bintang)
