#OOP

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = 'Selesai' if self.completed else 'Belum Selesai'
        return f"{self.title} - {self.description} [{status}]"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Tugas '{title}' ditambahkan.")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Tugas '{title}' dihapus.")
                return
        print(f"Tugas '{title}' tidak ditemukan.")

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"Tugas '{title}' ditandai sebagai selesai.")
                return
        print(f"Tugas '{title}' tidak ditemukan.")

    def list_tasks(self):
        if not self.tasks:
            print("Tidak ada tugas.")
        else:
            for task in self.tasks:
                print(task)


def main():
    manager = TaskManager()

    while True:
        print("\n1. Tambah Tugas")
        print("2. Hapus Tugas")
        print("3. Selesaikan Tugas")
        print("4. Daftar Tugas")
        print("5. Keluar")
        choice = input("Pilih opsi: ")

        if choice == '1':
            title = input("Masukkan judul tugas: ")
            description = input("Masukkan deskripsi tugas: ")
            manager.add_task(title, description)
        elif choice == '2':
            title = input("Masukkan judul tugas yang ingin dihapus: ")
            manager.remove_task(title)
        elif choice == '3':
            title = input("Masukkan judul tugas yang ingin diselesaikan: ")
            manager.complete_task(title)
        elif choice == '4':
            manager.list_tasks()
        elif choice == '5':
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
