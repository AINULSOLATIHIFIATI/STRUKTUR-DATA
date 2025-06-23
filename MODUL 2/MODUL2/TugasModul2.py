# Node class untuk double linked-list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Double Linked List class
class DoubleLinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node di akhir
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    # Menampilkan isi list
    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" <-> " if cur.next else "\n")
            cur = cur.next

    # 1. Menghapus node awal
    def delete_first(self):
        if self.head is None:
            print("List kosong")
            return
        print(f"Menghapus node awal: {self.head.data}")
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    # 2. Menghapus node akhir
    def delete_last(self):
        if self.head is None:
            print("List kosong")
            return
        cur = self.head
        if cur.next is None:
            print(f"Menghapus node terakhir: {cur.data}")
            self.head = None
            return
        while cur.next:
            cur = cur.next
        print(f"Menghapus node terakhir: {cur.data}")
        cur.prev.next = None

    # 3. Menghapus node berdasarkan nilai data
    def delete_by_value(self, value):
        if self.head is None:
            print("List kosong")
            return
        cur = self.head
        while cur:
            if cur.data == value:
                print(f"Menghapus node dengan nilai: {value}")
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                return
            cur = cur.next
        print(f"Data {value} tidak ditemukan dalam list.")

# Contoh penggunaan
dll = DoubleLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Isi awal:")
dll.display()

dll.delete_first()
dll.display()

dll.delete_last()
dll.display()

dll.delete_by_value(20)
dll.display()

dll.delete_by_value(99)  # Kasus data tidak ditemukan
