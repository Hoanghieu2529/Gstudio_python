import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class DuAnForm:
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
        columns_duan = ("Số thứ tự", "Mã dự án", "Tên dự án", "Mô tả dự án", "Ngày bắt đầu", "Ngày kết thúc", "Trạng thái")
        self.tree_duan = ttk.Treeview(parent_frame, columns=columns_duan, show="headings")

        for col in columns_duan:
            self.tree_duan.heading(col, text=col)
            self.tree_duan.column(col, width=100)  # Auto fit các cột

        self.tree_duan.pack(fill=tk.BOTH, expand=True)

        h_scroll = ttk.Scrollbar(parent_frame, orient="horizontal", command=self.tree_duan.xview)
        self.tree_duan.configure(xscrollcommand=h_scroll.set)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        self.auto_generate_stt = 1  # Tự động tạo số thứ tự

    def create_record(self):
        form = tk.Toplevel(self.frame)
        form.title("Thêm mới dự án")

        labels = ["Mã dự án", "Tên dự án", "Mô tả dự án", "Ngày bắt đầu", "Ngày kết thúc", "Trạng thái"]
        entries = []

        for i, label in enumerate(labels):
            tk.Label(form, text=label).grid(row=i, column=0, padx=10, pady=5)
            if "Ngày" in label:
                entry = DateEntry(form, date_pattern='dd/mm/yyyy')
            elif "Trạng thái" in label:
                entry = ttk.Combobox(form, values=["Đang thực hiện", "Hoàn thành", "Hủy bỏ"])
                entry.current(0)
            else:
                entry = tk.Entry(form)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)
            entries.append(entry)

        def save_record():
            new_record = [self.auto_generate_stt] + [entry.get() for entry in entries]
            self.tree_duan.insert("", "end", values=new_record)
            self.auto_generate_stt += 1  # Tăng số thứ tự tự động
            form.destroy()

        save_btn = tk.Button(form, text="Lưu", command=save_record)
        save_btn.grid(row=len(labels), columnspan=2, pady=10)

    def read_record(self):
        selected_item = self.tree_duan.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một dự án để xem chi tiết")
            return
        item = self.tree_duan.item(selected_item)
        values = item["values"]
        messagebox.showinfo("Thông tin dự án",
                            f"Mã dự án: {values[1]}\n"
                            f"Tên dự án: {values[2]}\n"
                            f"Mô tả dự án: {values[3]}\n"
                            f"Ngày bắt đầu: {values[4]}\n"
                            f"Ngày kết thúc: {values[5]}\n"
                            f"Trạng thái: {values[6]}")

    def update_record(self):
        selected_item = self.tree_duan.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một dự án để cập nhật")
            return
        item = self.tree_duan.item(selected_item)
        values = item["values"]
        new_values = (values[0], values[1], values[2], values[3], values[4], values[5], "Hoàn thành")
        self.tree_duan.item(selected_item, values=new_values)

    def delete_record(self):
        selected_item = self.tree_duan.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một dự án để xóa")
            return
        self.tree_duan.delete(selected_item)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Dự án")
    root.geometry("800x600")
    app = DuAnForm(root)
    root.mainloop()
