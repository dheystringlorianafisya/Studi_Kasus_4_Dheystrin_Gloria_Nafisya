# Membuat Dictionary
buku = {
    "judul" : "Tentang Kamu",
    "penulis" : "Tere Liye",
    "tahun terbit" : 2016
}

while True:
    print("\n=== MENU ===")
    print("1. Tampilkan Data Buku")
    print("2. Tambah Data Penerbit")
    print("3. Ubah Data penulis")
    print("4. Hapus Data penerbit")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        print("\n=== DATA BUKU ===")
        print(buku)

    elif pilihan == "2":
        penerbit = input("masukkan nama penerbit : ")
        buku["penerbit"] = penerbit
        print("Data penerbit berhasil ditambahkan")

    elif pilihan == "3":
        penulis_baru = input("masukkan penulis baru : ")
        buku.update({"penulis" : penulis_baru })
        print("data berhasil diubah")
    
    elif pilihan == "4":
        del buku["penerbit"]
        print("Data berhasil dihapus.")

    elif pilihan == "5":
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-5.")

print("setelah perubahan:" )
print(buku)