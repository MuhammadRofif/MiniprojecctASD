class Siswa:
    def __init__(self, nama, usia, kelas, jenis_kelamin, alamat):
        self.nama = nama
        self.usia = usia
        self.kelas = kelas
        self.jenis_kelamin = jenis_kelamin
        self.alamat = alamat

class ManajemenSekolah:
    def __init__(self):
        self.data_siswa = {}
        
    def tambah_siswa(self, id_siswa, siswa):
        self.data_siswa[id_siswa] = siswa

    def hapus_siswa(self, id_siswa):
        if id_siswa in self.data_siswa:
            del self.data_siswa[id_siswa]
            print("Data siswa berhasil dihapus.")
        else:
            print("ID siswa tidak ditemukan.")

    def tampilkan_info_siswa(self):
        if self.data_siswa:
            print("Daftar semua siswa:")
            for id_siswa, siswa in self.data_siswa.items():
                print(f"ID Siswa: {id_siswa}")
                print("Nama:", siswa.nama)
                print("Usia:", siswa.usia)
                print("Kelas:", siswa.kelas)
                print("Jenis Kelamin:", siswa.jenis_kelamin)
                print("Alamat:", siswa.alamat)
                print("-" * 20)
        else:
            print("ID siswa tidak ditemukan.")

    def update_info_siswa(self, id_siswa, nama=None, usia=None, kelas=None, jenis_kelamin=None, alamat=None):
        if id_siswa in self.data_siswa:
            siswa = self.data_siswa[id_siswa]
            if nama:
                siswa.nama = nama
            if usia:
                siswa.usia = usia
            if kelas:
                siswa.kelas = kelas
            if jenis_kelamin:
                siswa.jenis_kelamin = jenis_kelamin
            if alamat:
                siswa.alamat = alamat
            print("Info siswa berhasil diperbarui.")
        else:
            print("ID siswa tidak ditemukan. Perbarui gagal.")

def main():
    sekolah = ManajemenSekolah()
    while True:
        print("\nMenu:")
        print("1. Tambah Siswa")
        print("2. Tampilkan Info Siswa")
        print("3. Perbarui Info Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        if pilihan == "1":
            nama = input("Masukkan nama siswa: ")
            usia = int(input("Masukkan usia siswa: "))
            kelas = int(input("Masukkan kelas siswa: "))
            jenis_kelamin = input("Masukkan jenis kelamin siswa: ")
            alamat = input("Masukkan alamat siswa: ")
            siswa_baru = Siswa(nama, usia, kelas, jenis_kelamin, alamat)
            id_siswa = len(sekolah.data_siswa) + 1
            sekolah.tambah_siswa(id_siswa, siswa_baru)
            print("Siswa berhasil ditambahkan dengan ID:", id_siswa)
        elif pilihan == "2":
            sekolah.tampilkan_info_siswa()
        elif pilihan == "3":
            sekolah.tampilkan_info_siswa()
            id_siswa = int(input("Masukkan ID siswa yang ingin diperbarui: "))
            print("Masukkan info baru (biarkan kosong jika tidak ingin mengubah)")
            nama = input("Nama baru: ")
            usia = int(input("Usia baru: "))
            kelas = int(input("Kelas baru: "))
            jenis_kelamin = input("Jenis kelamin baru: ")
            alamat = input("Alamat baru: ")
            sekolah.update_info_siswa(id_siswa, nama, usia, kelas, jenis_kelamin, alamat)
        elif pilihan == "4":
            sekolah.tampilkan_info_siswa()
            id_siswa = int(input("Masukkan ID siswa yang ingin dihapus: "))
            sekolah.hapus_siswa(id_siswa)
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")

if __name__ == "__main__":
    main()

