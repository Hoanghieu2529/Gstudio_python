import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class DuAnFormController:
    def __init__(self, view):
        self.view = view
        self.auto_generate_stt = 1  # Tự động tạo số thứ tự

    def create_record(self):
        form = tk.Toplevel(self.view.frame)
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
            self.view.tree_duan.insert("", "end", values=new_record)
            self.auto_generate_stt += 1  # Tăng số thứ tự tự động
            form.destroy()

        save_btn = tk.Button(form, text="Lưu", command=save_record)
        save_btn.grid(row=len(labels), columnspan=2, pady=10)

    def read_record(self):
        selected_item = self.view.tree_duan.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một dự án để xem chi tiết")
            return
        item = self.view.tree_duan.item(selected_item)
        values = item["values"]
        messagebox.showinfo("Thông tin dự án",
                            f"Mã dự án: {values[1]}\n"
                            f"Tên dự án: {values[2]}\n"
                            f"Mô tả dự án: {values[3]}\n"
                            f"Ngày bắt đầu: {values[4]}\n"
                            f"Ngày kết thúc: {values[5]}\n"
                            f"Trạng thái: {values[6]}")

    def update_record(self):
        selected_item = self.view.tree_duan.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một dự án để cập nhật")
            return
        item = self.view.tree_duan.item(selected_item)
        values = item["values"]
        new_values = (values[0], values[1], values[2], values[3], values[4], values[5], "Hoàn thành")
        self.view.tree_duan.item(selected_item, values=new_values)

    def delete_record(self):
        selected_item = self.view.tree_duan.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một dự án để xóa")
            return
        self.view.tree_duan.delete(selected_item)
