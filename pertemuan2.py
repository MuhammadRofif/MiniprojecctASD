class Node:
    def __init__(self, siswa=None):
        self.siswa = siswa
        self.next = None

class Siswa:
    def __init__(self, nama, usia, kelas, jenis_kelamin, alamat):
        self.nama = nama
        self.usia = usia
        self.kelas = kelas
        self.jenis_kelamin = jenis_kelamin
        self.alamat = alamat

class ManajemenSekolah: #kelas singlelinkedlist
    def __init__(self):
        self.head = None

    def tambah_siswa_awal(self, siswa):
        new_node = Node(siswa)
        new_node.next = self.head
        self.head = new_node

    def tambah_siswa_akhir(self, siswa):
        new_node = Node(siswa)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def tambah_siswa_di_antara(self, siswa, posisi):
        if posisi == 1:
            self.tambah_siswa_awal(siswa)
            return
        new_node = Node(siswa)
        current = self.head
        for _ in range(1, posisi - 1):
            if current is None:
                print("Posisi tidak valid")
                return
            current = current.next
        if current is None:
            print("Posisi tidak valid")
            return
        new_node.next = current.next
        current.next = new_node

    def hapus_siswa_awal(self):
        if not self.head:
            print("Linked list kosong")
            return
        self.head = self.head.next

    def hapus_siswa_akhir(self):
        if not self.head:
            print("Linked list kosong")
            return
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def hapus_siswa_di_antara(self, posisi):
        if not self.head:
            print("Linked list kosong")
            return
        temp = self.head
        if posisi == 1:
            self.head = temp.next
            temp = None
            return
        for _ in range(posisi - 1):
            if temp is None:
                print("Posisi tidak valid")
                return
            prev = temp
            temp = temp.next
        if temp is None:
            print("Posisi tidak valid")
            return
        prev.next = temp.next
        temp = None

    def tampilkan_info_siswa(self):
        current = self.head
        while current:
            siswa = current.siswa
            print("Nama:", siswa.nama)
            print("Usia:", siswa.usia)
            print("Kelas:", siswa.kelas)
            print("Jenis Kelamin:", siswa.jenis_kelamin)
            print("Alamat:", siswa.alamat)
            print("-" * 20)
            current = current.next

def main():
    sekolah = ManajemenSekolah()
    while True:
        print("\nMenu:")
        print("1. Tambah Siswa di Awal")
        print("2. Tambah Siswa di Akhir")
        print("3. Tambah Siswa di Tengah")
        print("4. Tampilkan Info Siswa")
        print("5. Hapus Siswa di Awal")
        print("6. Hapus Siswa di Akhir")
        print("7. Hapus Siswa di Tengah")
        print("8. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5/6/7/8): ")
        if pilihan == "1":
            nama = input("Masukkan nama siswa: ")
            usia = int(input("Masukkan usia siswa: "))
            kelas = int(input("Masukkan kelas siswa: "))
            jenis_kelamin = input("Masukkan jenis kelamin siswa: ")
            alamat = input("Masukkan alamat siswa: ")
            siswa_baru = Siswa(nama, usia, kelas, jenis_kelamin, alamat)
            sekolah.tambah_siswa_awal(siswa_baru)
            print("Siswa berhasil ditambahkan di awal.")
        elif pilihan == "2":
            nama = input("Masukkan nama siswa: ")
            usia = int(input("Masukkan usia siswa: "))
            kelas = int(input("Masukkan kelas siswa: "))
            jenis_kelamin = input("Masukkan jenis kelamin siswa: ")
            alamat = input("Masukkan alamat siswa: ")
            siswa_baru = Siswa(nama, usia, kelas, jenis_kelamin, alamat)
            sekolah.tambah_siswa_akhir(siswa_baru)
            print("Siswa berhasil ditambahkan di akhir.")
        elif pilihan == "3":
            nama = input("Masukkan nama siswa: ")
            usia = int(input("Masukkan usia siswa: "))
            kelas = int(input("Masukkan kelas siswa: "))
            jenis_kelamin = input("Masukkan jenis kelamin siswa: ")
            alamat = input("Masukkan alamat siswa: ")
            posisi = int(input("Masukkan posisi siswa: "))
            siswa_baru = Siswa(nama, usia, kelas, jenis_kelamin, alamat)
            sekolah.tambah_siswa_di_antara(siswa_baru, posisi)
            print("Siswa berhasil ditambahkan di tengah.")
        elif pilihan == "4":
            sekolah.tampilkan_info_siswa()
        elif pilihan == "5":
            sekolah.hapus_siswa_awal()
            print("Siswa pertama berhasil dihapus.")
        elif pilihan == "6":
            sekolah.hapus_siswa_akhir()
            print("Siswa terakhir berhasil dihapus.")
        elif pilihan == "7":
            posisi = int(input("Masukkan posisi siswa yang ingin dihapus: "))
            sekolah.hapus_siswa_di_antara(posisi)
            print("Siswa di posisi tertentu berhasil dihapus.")
        elif pilihan == "8":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")

if __name__ == "__main__":
    main()
