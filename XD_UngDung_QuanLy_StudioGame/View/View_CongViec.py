import tkinter as tk
from tkinter import ttk

from View.View_BaseForm import KhungCoSo
from controllers import CongViecFormController

class CongViecForm(KhungCoSo):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.frame = tk.Frame(master, bg="#f8f9fa")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.controller = CongViecFormController(self)

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
        columns_congviec = ("Số thứ tự", "Mã công việc", "Tên công việc", "Mô tả công việc", "Giao cho", "Hạn cuối", "Trạng thái")
        self.tree_congviec = ttk.Treeview(parent_frame, columns=columns_congviec, show="headings")

        for col in columns_congviec:
            self.tree_congviec.heading(col, text=col)
            self.tree_congviec.column(col, width=100)  # Auto fit các cột

        self.tree_congviec.pack(fill=tk.BOTH, expand=True)

        h_scroll = ttk.Scrollbar(parent_frame, orient="horizontal", command=self.tree_congviec.xview)
        self.tree_congviec.configure(xscrollcommand=h_scroll.set)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Công việc")
    root.geometry("800x600")
    app = CongViecForm(root)
    root.mainloop()
