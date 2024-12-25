import tkinter as tk
from tkinter import ttk, messagebox


class PhongBanForm:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#f8f9fa")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.create_toolbar(self.frame)
        self.create_treeview(self.frame)

    def create_toolbar(self, parent_frame):
        toolbar = tk.Frame(parent_frame, bg="#f8f9fa")
        toolbar.pack(fill=tk.X, pady=10)

        create_btn = tk.Button(toolbar, text="Thêm mới", command=self.create_record, bg="#d1e7dd")
        read_btn = tk.Button(toolbar, text="Đọc", command=self.read_record, bg="#fff3cd")
        update_btn = tk.Button(toolbar, text="Cập nhật", command=self.update_record, bg="#cff4fc")
        delete_btn = tk.Button(toolbar, text="Xóa", command=self.delete_record, bg="#f8d7da")

        create_btn.pack(side=tk.LEFT, padx=10, pady=5)
        read_btn.pack(side=tk.LEFT, padx=10, pady=5)
        update_btn.pack(side=tk.LEFT, padx=10, pady=5)
        delete_btn.pack(side=tk.LEFT, padx=10, pady=5)

    def create_treeview(self, parent_frame):
        columns_studio = ("Mã nhân viên", "Tên nhân viên", "Mô tả", "Điện thoại")
        self.tree_studio = ttk.Treeview(parent_frame, columns=columns_studio, show="headings", selectmode="browse")

        for col in columns_studio:
            self.tree_studio.heading(col, text=col)
            self.tree_studio.column(col, width=150, anchor=tk.W)

        self.tree_studio.pack(fill=tk.BOTH, expand=True, pady=5)

        h_scroll = ttk.Scrollbar(parent_frame, orient="horizontal", command=self.tree_studio.xview)
        self.tree_studio.configure(xscrollcommand=h_scroll.set)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    def create_record(self):
        # Giá trị mẫu mới
        new_id = self.tree_studio.get_children().__len__() + 1  # Tự tăng ID
        new_name = "Dự án A"
        new_description = "Mô tả dự án mẫu"
        new_phone = "0123456789"
        self.tree_studio.insert("", "end", values=(new_id, new_name, new_description, new_phone))

    def read_record(self):
        try:
            selected_item = self.tree_studio.selection()[0]
            item = self.tree_studio.item(selected_item)
            values = item["values"]
            tk.messagebox.showinfo(
                "Thông tin dự án",
                f"ID: {values[0]}\nTên dự án: {values[1]}\nMô tả: {values[2]}\nĐiện thoại: {values[3]}"
            )
        except IndexError:
            tk.messagebox.showwarning("Cảnh báo", "Vui lòng chọn một dự án để xem chi tiết")

    def update_record(self):
        try:
            selected_item = self.tree_studio.selection()[0]
            item = self.tree_studio.item(selected_item)
            values = item["values"]
            # Cập nhật với dữ liệu mẫu
            new_values = (values[0], "Dự án B (Cập nhật)", "Mô tả đã cập nhật", values[3])
            self.tree_studio.item(selected_item, values=new_values)
            tk.messagebox.showinfo("Thông báo", "Cập nhật thành công!")
        except IndexError:
            tk.messagebox.showwarning("Cảnh báo", "Vui lòng chọn một dự án để cập nhật")

    def delete_record(self):
        try:
            selected_item = self.tree_studio.selection()[0]
            self.tree_studio.delete(selected_item)
            tk.messagebox.showinfo("Thông báo", "Xóa thành công!")
        except IndexError:
            tk.messagebox.showwarning("Cảnh báo", "Vui lòng chọn một dự án để xóa")
