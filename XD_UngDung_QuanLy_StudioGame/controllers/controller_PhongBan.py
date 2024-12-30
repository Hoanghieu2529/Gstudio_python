# import tkinter as tk
# from tkinter import ttk, messagebox
#
# class PhongBanFormController:
#     def __init__(self, view):
#         self.view = view
#         self.auto_generate_stt = 1  # Tự động tạo số thứ tự
#
#     def create_record(self):
#         form = tk.Toplevel(self.view.frame)
#         form.title("Thêm mới phòng ban")
#
#         labels = ["Mã phòng ban", "Tên phòng ban", "Quản lý phòng ban", "Danh sách công việc"]
#         entries = self.generate_form_entries(form, labels)
#
#         save_btn = tk.Button(form, text="Lưu", command=lambda: self.save_record(entries, form))
#         save_btn.grid(row=len(labels) + 1, columnspan=2, pady=10)
#
#     def update_record(self):
#         selected_item = self.view.tree_phongban.selection()
#         if not selected_item:
#             messagebox.showwarning("Cảnh báo", "Vui lòng chọn một phòng ban để cập nhật")
#             return
#         item = self.view.tree_phongban.item(selected_item)
#         values = item["values"]
#
#         form = tk.Toplevel(self.view.frame)
#         form.title("Cập nhật thông tin phòng ban")
#
#         labels = ["Mã phòng ban", "Tên phòng ban", "Quản lý phòng ban", "Danh sách công việc"]
#         entries = self.generate_form_entries(form, labels, values)
#
#         save_btn = tk.Button(form, text="Lưu thay đổi", command=lambda: self.save_changes(entries, selected_item, form))
#         save_btn.grid(row=len(labels) + 1, columnspan=2, pady=10)
#
#     def generate_form_entries(self, form, labels, values=None):
#         entries = []
#         for i, label in enumerate(labels):
#             tk.Label(form, text=label).grid(row=i, column=0, padx=10, pady=5)
#             if label == "Danh sách công việc":
#                 entry = tk.Listbox(form, selectmode="multiple")
#                 jobs = ["Lập trình", "Front end", "Back end", "Tester"]
#                 for job in jobs:
#                     entry.insert(tk.END, job)
#                 if values:
#                     selected_jobs = values[i + 1].split(", ")
#                     for job in selected_jobs:
#                         idx = jobs.index(job)
#                         entry.select_set(idx)
#             else:
#                 entry = tk.Entry(form)
#                 if values:
#                     entry.insert(0, values[i + 1])
#             entry.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)
#             entries.append(entry)
#         return entries
#
#     def save_record(self, entries, form):
#         new_record = [self.auto_generate_stt] + [self.get_entry_value(entry) for entry in entries]
#         self.view.tree_phongban.insert("", "end", values=new_record)
#         self.auto_generate_stt += 1
#         form.destroy()
#
#     def save_changes(self, entries, selected_item, form):
#         new_values = [selected_item[0]] + [self.get_entry_value(entry) for entry in entries]
#         self.view.tree_phongban.item(selected_item, values=new_values)
#         form.destroy()
#
#     def get_entry_value(self, entry):
#         if isinstance(entry, tk.Listbox):
#             return ", ".join(entry.get(idx) for idx in entry.curselection())
#         return entry.get()
#
#     def read_record(self):
#         selected_item = self.view.tree_phongban.selection()
#         if not selected_item:
#             messagebox.showwarning("Cảnh báo", "Vui lòng chọn một phòng ban để xem chi tiết")
#             return
#         item = self.view.tree_phongban.item(selected_item)
#         values = item["values"]
#         messagebox.showinfo("Thông tin phòng ban",
#                             f"Mã phòng ban: {values[1]}\n"
#                             f"Tên phòng ban: {values[2]}\n"
#                             f"Quản lý phòng ban: {values[3]}\n"
#                             f"Danh sách công việc: {values[4]}")
#
#     def delete_record(self):
#         selected_item = self.view.tree_phongban.selection()
#         if not selected_item:
#             messagebox.showwarning("Cảnh báo", "Vui lòng chọn một phòng ban để xóa")
#             return
#         confirm = messagebox.askyesno("Xác nhận", "Bạn thật sự muốn xóa phòng ban này không?")
#         if confirm:
#             self.view.tree_phongban.delete(selected_item)

from models.models_phong_ban import PhongBanModel

class PhongBanFormController:
    def __init__(self, view):
        self.view = view
        self.model = PhongBanModel()  # Kết nối với model PhongBan

    def tao_pb_moi(self):
        """Thêm một phòng ban mới"""
        messagebox.showinfo("Thông báo", "Chức năng thêm phòng ban đang được phát triển.")

    def doc_pb(self):
        """Xem chi tiết một phòng ban"""
        selected_item = self.view.tree_phongban.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một phòng ban để xem chi tiết")
            return
        item = self.view.tree_phongban.item(selected_item)
        values = item["values"]
        messagebox.showinfo("Thông tin phòng ban",
                            f"Mã phòng ban: {values[1]}\n"
                            f"Tên phòng ban: {values[2]}\n"
                            f"Mô tả: {values[3]}")

    def cap_nhat_pb(self):
        """Cập nhật thông tin một phòng ban"""
        messagebox.showinfo("Thông báo", "Chức năng cập nhật phòng ban đang được phát triển.")

    def xoa_pb(self):
        """Xóa một phòng ban"""
        selected_item = self.view.tree_phongban.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một phòng ban để xóa")
            return
        confirm = messagebox.askyesno("Xác nhận", "Bạn thật sự muốn xóa phòng ban này không?")
        if confirm:
            self.view.tree_phongban.delete(selected_item)

    def tai_dl(self):
        """Tải dữ liệu từ CSDL và hiển thị trong Treeview"""
        self.view.tree_phongban.delete(*self.view.tree_phongban.get_children())  # Xóa dữ liệu cũ
        danh_sach_phong_ban = self.model.lay_danh_sach_phong_ban()  # Lấy dữ liệu từ model
        for idx, phong_ban in enumerate(danh_sach_phong_ban, start=1):
            self.view.tree_phongban.insert("", "end", values=(idx, phong_ban['mapb'], phong_ban['ten_phong_ban'], phong_ban['mo_ta']))
