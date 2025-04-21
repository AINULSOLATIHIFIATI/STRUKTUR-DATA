# Variabel global untuk menyimpan data buku
buku = []

# Fungsi untuk menampilkan semua data buku
def show_data():
    if len(buku) == 0:
        print("DATA BUKU BELUM ADA")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))

# Fungsi untuk menambahkan data buku
def insert_data():
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)
    print("Data buku berhasil ditambahkan!")

# Fungsi untuk mengedit data buku
def edit_data():
    show_data()
    try:
        indeks = int(input("Inputkan ID Buku : "))
        if indeks < 0 or indeks >= len(buku):
            print("ID Buku Tidak Ditemukan")
        else:
            judul_baru = input("Judul Baru : ")
            buku[indeks] = judul_baru
            print("Data buku berhasil diubah!")
    except ValueError:
        print("Input tidak valid!")

# Fungsi untuk menghapus data buku
def delete_data():
    show_data()
    try:
        indeks = int(input("Inputkan ID Buku : "))
        if indeks < 0 or indeks >= len(buku):
            print("ID Buku Tidak Ditemukan")
        else:
            buku_terhapus = buku.pop(indeks)
            print(f"Buku '{buku_terhapus}' dengan ID {indeks} terhapus")
    except ValueError:
        print("Input tidak valid!")

# Fungsi untuk menampilkan menu
def show_menu():
    print("\n", 5*"-", "MENU", 5*"-")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    
    try:
        menu = int(input("PILIH MENU : "))
        print()
        if menu == 1:
            show_data()
        elif menu == 2:
            insert_data()
        elif menu == 3:
            edit_data()
        elif menu == 4:
            delete_data()
        elif menu == 5:
            print("Terima kasih telah menggunakan program ini.")
            exit()
        else:
            print("Pilihan Anda Salah!")
    except ValueError:
        print("Input harus berupa angka!")

# Program utama
if __name__ == "__main__":
    while True:
        show_menu()
