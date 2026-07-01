#==========================================
#CLASS BARANG
#==========================================
class barang:
    def __init__(self,nama,harga,stok):
        self.nama = nama
        self.harga = harga
        self.__stok = stok  #encapsulation

    def get_stok(self):
        return self.__stok

    def get_stok(self):
        return self.__stok

    def tambah_stok(self,jumlah):
        self.__stok += jumlah

    def kurangi_stok(self,jumlah):
        if jumlah <= self.__stok:
             self.__stok -= jumlah    
        else:
            print("Stok tidak cukup!") 

    def tampilkan_info(self):
        print("Nama Barang:", self.nama)
        print("Harga Barang:", self.harga)
        print("Stok Barang:", self.__stok)

#===========================================
#CLASS TURUNAN
#===========================================
class elektronik(barang):
    def __init__(self,nama,harga,stok,garansi):
        super().__init__(nama,harga,stok)
        self.garansi = garansi

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Garansi:", self.garansi)

#===========================================
#DATA INVENTARIS
#===========================================
inventaris = []

#===========================================
#FUNGSI MENU
#===========================================
def tambah_barang():
    print("\n=== Tambah Barang ===")
    jenis = input("Masukkan jenis barang (1. Barang Umum, 2. Elektronik): ")

    nama = input("Masukkan nama barang: ")
    harga = int(input("Masukkan harga barang: "))
    stok = int(input("Masukkan stok barang: "))

    if jenis == "2":
        garansi = input("Masukkan garansi barang: ")
        item = elektronik(nama, harga, stok, garansi)
    else:
        item = barang(nama, harga, stok)

    inventaris.append(item)
    print("Barang berhasil ditambahkan!")

def tampilkan_barang():
    print("\n=== Daftar Barang ===")
    if not inventaris:
        print("Tidak ada barang dalam inventaris.")
    else:
        for i, barang in enumerate(inventaris):
            print(f"\nIndex[{i}]:")
            barang.tampilkan_info()

def tambah_stok():
    tampilkan_barang()
    index = int(input("pilih index barang: "))
    jumlah = int(input("jumlah tambah stok: "))
    inventaris[index].tambah_stok(jumlah)
    print("Stok berhasil ditambahkan!")

def kurangi_stok():
    index = int(input("pilih index barang: "))
    jumlah = int(input("jumlah kurangi stok: "))
    inventaris[index].kurangi_stok(jumlah)
    print("Stok berhasil dikurangi!")

#===========================================
#MENU UTAMA
#=========================================== 
while True:
    print("\n=== Menu Inventaris ===")
    print("1. Tambah Barang")
    print("2. Tampilkan Barang")
    print("3. Tambah Stok")
    print("4. Kurangi Stok")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2":
        tampilkan_barang()
    elif pilihan == "3":
        tambah_stok()
    elif pilihan == "4":
        kurangi_stok()
    elif pilihan == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")   