# Kelas Node untuk membuat node pada Double Linked List
class Node:
    def __init__(self, data):
        self.data = data     # Menyimpan nilai data
        self.prev = None     # Menyimpan alamat node sebelumnya
        self.next = None     # Menyimpan alamat node berikutnya

# Kelas DoubleLinkedList untuk operasi-operasi pada DLL
class DoubleLinkedList:
    def __init__(self):
        self.head = None     # Awal dari list

    # Menambahkan node di akhir list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr

    # Menghapus node awal
    def delete_from_beginning(self):
        if self.head is None:
            print("List kosong.")
            return
        print(f"Menghapus node awal: {self.head.data}")
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # Menghapus node akhir
    def delete_from_end(self):
        if self.head is None:
            print("List kosong.")
            return
        curr = self.head
        if curr.next is None:
            print(f"Menghapus node akhir (satu-satunya): {curr.data}")
            self.head = None
            return
        while curr.next:
            curr = curr.next
        print(f"Menghapus node akhir: {curr.data}")
        curr.prev.next = None

    # Menghapus node berdasarkan nilai
    def delete_by_value(self, value):
        if self.head is None:
            print("List kosong.")
            return
        curr = self.head

        # Jika nilai ada di head
        if curr.data == value:
            print(f"Menghapus node dengan nilai {value} (di awal)")
            self.head = curr.next
            if self.head:
                self.head.prev = None
            return

        # Cari node dengan data yang cocok
        while curr and curr.data != value:
            curr = curr.next

        # Jika tidak ditemukan
        if curr is None:
            print(f"Node dengan nilai {value} tidak ditemukan.")
            return

        # Hapus node
        print(f"Menghapus node dengan nilai {value}")
        if curr.next:
            curr.next.prev = curr.prev
        if curr.prev:
            curr.prev.next = curr.next

    # Menampilkan isi linked list
    def display(self):
        curr = self.head
        print("Isi List: ", end="")
        while curr:
            print(curr.data, end=" <=> ")
            curr = curr.next
        print("None")

# Contoh penggunaan
dll = DoubleLinkedList()
dll.append(5)
dll.append(10)
dll.append(15)
dll.append(20)

dll.display()  # Tampilkan awal

dll.delete_from_beginning()
dll.display()

dll.delete_from_end()
dll.display()

dll.delete_by_value(10)
dll.display()

dll.delete_by_value(100)  # Nilai tidak ada