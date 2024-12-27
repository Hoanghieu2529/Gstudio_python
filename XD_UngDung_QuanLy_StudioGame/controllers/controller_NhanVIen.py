import tkinter as tk
from tkinter import ttk, messagebox

class NhanVienFormController:
    def __init__(self, view):
        self.view = view
        self.auto_generate_stt = 1

    def create_record(self):
        form = tk.Toplevel(self.view.frame)
        form.title("Thêm mới nhân viên")

        labels = ["Mã nhân viên", "Tên nhân viên", "Vai trò", "Phòng ban", "Email"]
        entries = []

        for i, label in enumerate(labels):
            tk.Label(form, text=label).grid(row=i, column=0, padx=10, pady=5)

            if "Vai trò" in label:
                entry = ttk.Combobox(form, values=["Lập trình viên", "Nhà thiết kế", "Quản trị"])
            elif "Phòng ban" in label:
                entry = ttk.Combobox(form,
                                     values=["Phòng lập trình", "Phòng thiết kế", "Phòng Giám Đốc", "Phòng nhân sự"])
                entry.current(0)
            else:
                entry = tk.Entry(form)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)
            entries.append(entry)

        def save_record():
            new_record = [self.auto_generate_stt] + [entry.get() for entry in entries]
            self.view.tree_nhanvien.insert("", "end", values=new_record)
            self.auto_generate_stt += 1  # Tăng số thứ tự tự động
            form.destroy()

        save_btn = tk.Button(form, text="Lưu", command=save_record)
        save_btn.grid(row=len(labels), columnspan=2, pady=10)

    def read_record(self):
        selected_item = self.view.tree_nhanvien.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một nhân viên để xem chi tiết")
            return
        item = self.view.tree_nhanvien.item(selected_item)
        values = item["values"]
        messagebox.showinfo("Thông tin nhân viên",
                            f"Mã nhân viên: {values[1]}\n"
                            f"Tên nhân viên: {values[2]}\n"
                            f"Vai trò: {values[3]}\n"
                            f"Phòng ban: {values[4]}\n"
                            f"Email: {values[5]}")

    def update_record(self):
        selected_item = self.view.tree_nhanvien.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một nhân viên để cập nhật")
            return
        item = self.view.tree_nhanvien.item(selected_item)
        values = item["values"]

        # Tạo form cập nhật
        form = tk.Toplevel(self.view.frame)
        form.title("Cập nhật thông tin nhân viên")

        labels = ["Mã nhân viên", "Tên nhân viên", "Vai trò", "Phòng ban", "Email"]
        entries = []

        for i, label in enumerate(labels):
            tk.Label(form, text=label).grid(row=i, column=0, padx=10, pady=5)

            if "Vai trò" in label:
                entry = ttk.Combobox(form, values=["Lập trình viên", "Nhà thiết kế", "Quản trị"])
                entry.set(values[3])
            elif "Phòng ban" in label:
                entry = ttk.Combobox(form,
                                     values=["Phòng lập trình", "Phòng thiết kế", "Phòng Giám Đốc", "Phòng nhân sự"])
                entry.set(values[4])
            else:
                entry = tk.Entry(form)
                entry.insert(0, values[i + 1])
            entry.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)
            entries.append(entry)

        def save_changes():
            new_values = [values[0]] + [entry.get() for entry in entries]
            self.view.tree_nhanvien.item(selected_item, values=new_values)
            form.destroy()

        save_btn = tk.Button(form, text="Lưu thay đổi", command=save_changes)
        save_btn.grid(row=len(labels), columnspan=2, pady=10)

    def delete_record(self):
        selected_item = self.view.tree_nhanvien.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một nhân viên để xóa")
            return
        confirm = messagebox.askyesno("Xác nhận", "Bạn thật sự muốn xóa nhân viên này không?")
        if confirm:
            self.view.tree_nhanvien.delete(selected_item)
