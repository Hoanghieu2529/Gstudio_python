import tkinter as tk
from tkinter import ttk
from controllers import DuAnFormController

class DuAnForm:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#f8f9fa")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.controller = DuAnFormController(self)

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
        columns_duan = ("Số thứ tự", "Mã dự án", "Tên dự án", "Mô tả dự án", "Ngày bắt đầu", "Ngày kết thúc", "Trạng thái")
        self.tree_duan = ttk.Treeview(parent_frame, columns=columns_duan, show="headings")

        for col in columns_duan:
            self.tree_duan.heading(col, text=col)
            self.tree_duan.column(col, width=100)  # Auto fit các cột

        self.tree_duan.pack(fill=tk.BOTH, expand=True)

        h_scroll = ttk.Scrollbar(parent_frame, orient="horizontal", command=self.tree_duan.xview)
        self.tree_duan.configure(xscrollcommand=h_scroll.set)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Dự án")
    root.geometry("800x600")
    app = DuAnForm(root)
    root.mainloop()
