import math

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

class ManajemenSekolah:
    def __init__(self):
        self.head = None

    def tambah_siswa_awal(self, siswa):
        new_node = Node(siswa)
        new_node.next = self.head
        self.head = new_node

    def tambah_siswa_akhir(self, siswa):
        new_node = Node(siswa)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def tambah_siswa_di_antara(self, siswa):
        new_node = Node(siswa)
        current = self.head
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

    def hapus_siswa_di_antara(self, id):
        if not self.head:
            print("Linked list kosong")
            return
        if self.head.siswa.id == id:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.siswa.id == id:
                current.next = current.next.next
                return
            current = current.next
        print("ID tidak ditemukan")
        
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

    def jump_search(self, arr, key, search_by="usia"):
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        while getattr(arr[min(step, n)-1], search_by) < key:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1
        while getattr(arr[prev], search_by) < key:
            prev += 1
            if prev == min(step, n):
                return -1
        if getattr(arr[prev], search_by) == key:
            return prev
        return -1

    def cari_usia(self, usia):
        siswa_list = self.get_siswa_list()
        index = self.jump_search(siswa_list, usia, search_by="usia")
        if index != -1:
            print("usia ditemukan di indeks:", index)
            print("Info Siswa:")
            self.tampilkan_info_siswa_by_index(index)
        else:
            print("usia tidak ditemukan.")

    def cari_id(self, id):
        siswa_list = self.get_siswa_list()
        index = self.jump_search(siswa_list, id, search_by="id")
        if index != -1:
            print("ID ditemukan di indeks:", index)
            print("Info Siswa:")
            self.tampilkan_info_siswa_by_index(index)
        else:
            print("ID tidak ditemukan.")

    def tampilkan_info_siswa_by_index(self, index):
        siswa = self.get_siswa_list()[index]
        print("Nama:", siswa.nama)
        print("Usia:", siswa.usia)
        print("Kelas:", siswa.kelas)
        print("Jenis Kelamin:", siswa.jenis_kelamin)
        print("Alamat:", siswa.alamat)
        print("id_siswa:", siswa.id)
        print("-" * 20)
    
def main():
    sekolah = ManajemenSekolah()
    siswa_jono = Siswa("Jono", 15, 10, "Laki-laki", "Alamat 1", 1)
    sekolah.tambah_siswa_awal(siswa_jono)
    siswa_joy = Siswa("Joy", 16, 31, "Laki-laki", "Alamat 2", 2)
    sekolah.tambah_siswa_di_antara(siswa_joy)
    siswa_jini = Siswa("Jini", 17, 11, "Laki-laki", "Alamat 3", 3)
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
        print("9. Cari Siswa berdasarkan Usia")
        print("10. Cari Siswa berdasarkan ID")
        print("11. Hapus Siswa di Awal")
        print("12. Hapus Siswa di Akhir")
        print("13. Hapus Siswa di Tengah")
        print("14. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5/6/7/8/9/10/11/12/13/14): ")
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
            siswa_baru = Siswa(nama, usia, kelas, jenis_kelamin, alamat, id)
            sekolah.tambah_siswa_di_antara(siswa_baru)
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
            usia = int(input("Masukkan usia yang ingin dicari: "))
            sekolah.cari_usia(usia)
        elif pilihan == "10":
            id = int(input("Masukkan ID yang ingin dicari: "))
            sekolah.cari_id(id)
        elif pilihan == "11":
            sekolah.hapus_siswa_awal()
            print("Siswa pertama berhasil dihapus.")
        elif pilihan == "12":
            sekolah.hapus_siswa_akhir()
            print("Siswa terakhir berhasil dihapus.")
        elif pilihan == "13":
            id_siswa = int(input("Masukkan ID siswa yang ingin dihapus: "))
            sekolah.hapus_siswa_di_antara(id_siswa)
        elif pilihan == "14":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")

if __name__ == "__main__":
    main()
