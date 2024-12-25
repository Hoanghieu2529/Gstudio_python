import tkinter as tk
from tkinter import ttk, messagebox

class NguoiDungForm:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#f8f9fa")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.create_toolbar(self.frame)
        self.create_treeview(self.frame)

    def create_toolbar(self, parent_frame):
        toolbar = tk.Frame(parent_frame, bg="#f8f9fa")
        toolbar.pack(fill=tk.X, pady=10)

        create_btn = tk.Button(toolbar, text="Thêm mới", command=self.create_record, bg="#f8f9fa")
        read_btn = tk.Button(toolbar, text="Đọc", command=self.read_record, bg="#f8f9fa")
        update_btn = tk.Button(toolbar, text="Cập nhật", command=self.update_record, bg="#f8f9fa")
        delete_btn = tk.Button(toolbar, text="Xóa", command=self.delete_record, bg="#f8f9fa")

        create_btn.pack(side=tk.LEFT, padx=10)
        read_btn.pack(side=tk.LEFT, padx=10)
        update_btn.pack(side=tk.LEFT, padx=10)
        delete_btn.pack(side=tk.LEFT, padx=10)

    def create_treeview(self, parent_frame):
        columns_nguoidung = ("ID", "Tên", "Email", "Điện thoại")
        self.tree_nguoidung = ttk.Treeview(parent_frame, columns=columns_nguoidung, show="headings")

        for col in columns_nguoidung:
            self.tree_nguoidung.heading(col, text=col)

        self.tree_nguoidung.pack(fill=tk.BOTH, expand=True)

        h_scroll = ttk.Scrollbar(parent_frame, orient="horizontal", command=self.tree_nguoidung.xview)
        self.tree_nguoidung.configure(xscrollcommand=h_scroll.set)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    def create_record(self):
        new_id = "1"
        new_name = "John Doe"
        new_email = "john@example.com"
        new_phone = "0123456789"
        self.tree_nguoidung.insert("", "end", values=(new_id, new_name, new_email, new_phone))

    def read_record(self):
        selected_item = self.tree_nguoidung.selection()
        if not selected_item:
            tk.messagebox.showwarning("Cảnh báo", "Vui lòng chọn một người dùng để xem chi tiết")
            return
        item = self.tree_nguoidung.item(selected_item)
        values = item["values"]
        tk.messagebox.showinfo("Thông tin người dùng", f"ID: {values[0]}\nTên: {values[1]}\nEmail: {values[2]}\nĐiện thoại: {values[3]}")

    def update_record(self):
        selected_item = self.tree_nguoidung.selection()
        if not selected_item:
            tk.messagebox.showwarning("Cảnh báo", "Vui lòng chọn một người dùng để cập nhật")
            return
        item = self.tree_nguoidung.item(selected_item)
        values = item["values"]
        new_values = (values[0], "Jane Doe", values[2], values[3])
        self.tree_nguoidung.item(selected_item, values=new_values)

    def delete_record(self):
        selected_item = self.tree_nguoidung.selection()
        if not selected_item:
            tk.messagebox.showwarning("Cảnh báo", "Vui lòng chọn một người dùng để xóa")
            return
        self.tree_nguoidung.delete(selected_item)
