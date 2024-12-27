import tkinter as tk
from tkinter import ttk, messagebox
from controllers import PhongBanFormController

class PhongBanForm:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#f8f9fa")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.controller = PhongBanFormController(self)

        self.create_toolbar(self.frame)
        self.create_treeview(self.frame)

    def create_toolbar(self, parent_frame):
        toolbar = tk.Frame(parent_frame, bg="#f8f9fa")
        toolbar.pack(fill=tk.X, pady=10)

        create_btn = tk.Button(toolbar, text="Thêm mới", command=self.controller.create_record, bg="#f8f9fa")
        read_btn = tk.Button(toolbar, text="Đọc", command=self.controller.read_record, bg="#f8f9fa")
        update_btn = tk.Button(toolbar, text="Cập nhật", command=self.controller.update_record, bg="#f8f9fa")
        delete_btn = tk.Button(toolbar, text="Xóa", command=self.controller.delete_record, bg="#f8f9fa")

        create_btn.pack(side=tk.LEFT, padx=10)
        read_btn.pack(side=tk.LEFT, padx=10)
        update_btn.pack(side=tk.LEFT, padx=10)
        delete_btn.pack(side=tk.LEFT, padx=10)

    def create_treeview(self, parent_frame):
        columns_phongban = ("Số thứ tự", "Mã phòng ban", "Tên phòng ban", "Quản lý phòng ban", "Danh sách công việc")
        self.tree_phongban = ttk.Treeview(parent_frame, columns=columns_phongban, show="headings")

        for col in columns_phongban:
            self.tree_phongban.heading(col, text=col)
            self.tree_phongban.column(col, width=100)

        self.tree_phongban.pack(fill=tk.BOTH, expand=True)

        h_scroll = ttk.Scrollbar(parent_frame, orient="horizontal", command=self.tree_phongban.xview)
        self.tree_phongban.configure(xscrollcommand=h_scroll.set)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Phòng Ban")
    root.geometry("800x600")
    app = PhongBanForm(root)
    root.mainloop()
