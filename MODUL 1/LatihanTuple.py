matkul_list = []
jumlah = int(input("Input jumlah mata kuliah: "))
for i in range(jumlah):
    print(f"\nMata kuliah ke-{i+1}:")
    kode = input("Kode: ")
    nama = input("Nama: ")
    sks = int(input("SKS: "))
    matkul = (kode, nama, sks)
    matkul_list.append(matkul)
print("\nDaftar Mata Kuliah:")
for m in matkul_list:
    print(m)
('CS101', 'Algoritma', 3)
('CS102', 'Basis Data', 4)
('CS103', 'AI', 3)
total_sks = sum(m[2] for m in matkul_list)
print(f"\nTotal SKS: {total_sks}")
