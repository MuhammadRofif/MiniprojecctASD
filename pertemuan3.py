class Node:
    def __init__(self, siswa=None):
        self.siswa = siswa
        self.next = None

class Siswa:
    def __init__(self, nama, usia, kelas, jenis_kelamin, alamat, id):
        self.nama = nama
        self.usia = usia
        self.kelas = kelas
        self.jenis_kelamin = jenis_kelamin
        self.alamat = alamat
        self.id = id

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
            print("id_siswa:", siswa.id)
            print("-" * 20)
            current = current.next

    def get_siswa_list(self):
        siswa_list = []
        current = self.head
        while current:
            siswa_list.append(current.siswa)
            current = current.next
        return siswa_list
    
    def quick_sort(self, arr, key, ascending=True):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        if key == "nama":
            pivot_key = pivot.nama
        else:
            pivot_key = pivot.id
        left = [x for x in arr if (x.nama if key == "nama" else x.id) < pivot_key]
        middle = [x for x in arr if (x.nama if key == "nama" else x.id) == pivot_key]
        right = [x for x in arr if (x.nama if key == "nama" else x.id) > pivot_key]

        if ascending:
            return self.quick_sort(left, key, ascending) + middle + self.quick_sort(right, key, ascending)
        else:
            return self.quick_sort(right, key, ascending) + middle + self.quick_sort(left, key, ascending)

    
    def tampilkan_info_siswa_urut(self, key="nama", ascending=True):
        siswa_list = self.get_siswa_list()
        sorted_siswa = self.quick_sort(siswa_list, key, ascending)
        for siswa in sorted_siswa:
            print("Nama:", siswa.nama)
            print("Usia:", siswa.usia)
            print("Kelas:", siswa.kelas)
            print("Jenis Kelamin:", siswa.jenis_kelamin)
            print("Alamat:", siswa.alamat)
            print("id_siswa:", siswa.id)
            print("-" * 20)

def main():
    sekolah = ManajemenSekolah()
    siswa_jono = Siswa("Jono", 1, 1, "cowo", "alamat 1", 1)
    sekolah.tambah_siswa_akhir(siswa_jono)
    siswa_jini = Siswa("Jini", 2, 2, "lk", "alamat 2", 1)
    sekolah.tambah_siswa_akhir(siswa_jini)
    while True:
        print("\nMenu:")
        print("1. Tambah Siswa di Awal")
        print("2. Tambah Siswa di Akhir")
        print("3. Tambah Siswa di Tengah")
        print("4. Tampilkan Info Siswa")
        print("5. Tampilkan Info Siswa diurutkan Ascending berdasarkan Nama")
        print("6. Tampilkan Info Siswa diurutkan Descending berdasarkan Nama")
        print("7. Tampilkan Info Siswa diurutkan Ascending berdasarkan ID")
        print("8. Tampilkan Info Siswa diurutkan Descending berdasarkan ID")
        print("9. Hapus Siswa di Awal")
        print("10. Hapus Siswa di Akhir")
        print("11. Hapus Siswa di Tengah")
        print("12. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5/6/7/8/9/10/11/12): ")
        if pilihan == "1":
            nama = input("Masukkan nama siswa: ")
            usia = int(input("Masukkan usia siswa: "))
            kelas = int(input("Masukkan kelas siswa: "))
            jenis_kelamin = input("Masukkan jenis kelamin siswa: ")
            alamat = input("Masukkan alamat siswa: ")
            id = int(input("Masukkan ID siswa: "))
            siswa_baru = Siswa(nama, usia, kelas, jenis_kelamin, alamat, id)
            sekolah.tambah_siswa_awal(siswa_baru)
            print("Siswa berhasil ditambahkan di awal.")
        elif pilihan == "2":
            nama = input("Masukkan nama siswa: ")
            usia = int(input("Masukkan usia siswa: "))
            kelas = int(input("Masukkan kelas siswa: "))
            jenis_kelamin = input("Masukkan jenis kelamin siswa: ")
            alamat = input("Masukkan alamat siswa: ")
            id = int(input("Masukkan ID siswa: "))
            siswa_baru = Siswa(nama, usia, kelas, jenis_kelamin, alamat, id)
            sekolah.tambah_siswa_akhir(siswa_baru)
            print("Siswa berhasil ditambahkan di akhir.")
        elif pilihan == "3":
            nama = input("Masukkan nama siswa: ")
            usia = int(input("Masukkan usia siswa: "))
            kelas = int(input("Masukkan kelas siswa: "))
            jenis_kelamin = input("Masukkan jenis kelamin siswa: ")
            alamat = input("Masukkan alamat siswa: ")
            id = int(input("Masukkan ID siswa: "))
            posisi = int(input("Masukkan posisi siswa: "))
            siswa_baru = Siswa(nama, usia, kelas, jenis_kelamin, alamat, id)
            sekolah.tambah_siswa_di_antara(siswa_baru, posisi)
            print("Siswa berhasil ditambahkan di tengah.")
        elif pilihan == "4":
            sekolah.tampilkan_info_siswa()
        elif pilihan == "5":
            sekolah.tampilkan_info_siswa_urut(key="nama", ascending=True)
        elif pilihan == "6":
            sekolah.tampilkan_info_siswa_urut(key="nama", ascending=False)
        elif pilihan == "7":
            sekolah.tampilkan_info_siswa_urut(key="id", ascending=True)
        elif pilihan == "8":
            sekolah.tampilkan_info_siswa_urut(key="id", ascending=False)
        elif pilihan == "9":
            sekolah.hapus_siswa_awal()
            print("Siswa pertama berhasil dihapus.")
        elif pilihan == "10":
            sekolah.hapus_siswa_akhir()
            print("Siswa terakhir berhasil dihapus.")
        elif pilihan == "11":
            posisi = int(input("Masukkan posisi siswa yang ingin dihapus: "))
            sekolah.hapus_siswa_di_antara(posisi)
            print("Siswa di posisi tertentu berhasil dihapus.")
        elif pilihan == "12":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")

if __name__ == "__main__":
    main()
