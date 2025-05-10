def main():
    data_mahasiswa = {}
    
    # Meminta jumlah mahasiswa
    jumlah = int(input("Masukkan jumlah mahasiswa: "))

    for i in range(jumlah):
        print(f"\nMahasiswa ke-{i+1}")
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")

        nilai_mk = []
        jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))
        for j in range(jumlah_mk):
            mk = input(f"  Nama Mata Kuliah ke-{j+1}: ")
            nilai = float(input(f"  Nilai {mk}: "))
            nilai_mk.append((mk, nilai))

        data_mahasiswa[nim] = {
            'nama': nama,
            'nilai_mk': nilai_mk
        }

    print("\n=== Rekap Nilai Mahasiswa ===")
    for nim, info in data_mahasiswa.items():
        nama = info['nama']
        nilai_mk = info['nilai_mk']
        total_nilai = sum([nilai for _, nilai in nilai_mk])
        rata_rata = total_nilai / len(nilai_mk) if nilai_mk else 0

        print(f"\nNIM   : {nim}")
        print(f"Nama  : {nama}")
        print("Nilai Mata Kuliah:")
        for mk, nilai in nilai_mk:
            print(f"  {mk}: {nilai}")
        print(f"Rata-rata nilai: {rata_rata:.2f}")

if __name__ == "__main__":
    main()
