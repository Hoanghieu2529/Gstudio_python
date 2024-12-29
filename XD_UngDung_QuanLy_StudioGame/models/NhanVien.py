# from models import PhongBan, CongViec
#
# class NhanVien:
#     def __init__(self, ma_nhanvien: int, ten_nhanvien: str, vaitro: str, phongban: PhongBan, email_nhanvien: str):
#         if not isinstance(phongban, PhongBan):
#             raise TypeError('phongban phải là kiểu PhongBan')
#
#         self.__ma_nhanvien = ma_nhanvien
#         self._ten_nhanvien = ten_nhanvien
#         self._vaitro = vaitro
#         self._phongban = phongban
#         self._email_nhanvien = email_nhanvien
#         self._congviec = []
#
#     def them_nhanvien(self):
#         pass
#
#     def giao_congviec(self, congviec: CongViec):
#         if not isinstance(congviec, CongViec):
#             raise TypeError('congviec phải là kiểu CongViec')
#         self._congviec.append(congviec)
#
#     def lietke_congviec(self):
#         return [cv.ten_congviec for cv in self._congviec]
#
#     def __str__(self):
#         return (f"Nhân viên: {self._ten_nhanvien}, Vai trò: {self._vaitro}, "
#                 f"Email: {self._email_nhanvien}, Công việc: {', '.join(self.lietke_congviec())}")
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class NhanVienForm:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#f8f9fa")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.master = master

        self.create_toolbar(self.frame)
        self.create_treeview(self.frame)

    def create_toolbar(self, parent_frame):
        toolbar = tk.Frame(parent_frame, bg="#f8f9fa")
        toolbar.pack(fill=tk.X, pady=10)

        create_btn = tk.Button(toolbar, text="Thêm mới", command=self.open_create_form, bg="#f8f9fa")
        read_btn = tk.Button(toolbar, text="Đọc", command=self.open_read_form, bg="#f8f9fa")
        update_btn = tk.Button(toolbar, text="Cập nhật", command=self.open_update_form, bg="#f8f9fa")
        delete_btn = tk.Button(toolbar, text="Xóa", command=self.open_delete_form, bg="#f8f9fa")

        create_btn.pack(side=tk.LEFT, padx=10)
        read_btn.pack(side=tk.LEFT, padx=10)
        update_btn.pack(side=tk.LEFT, padx=10)
        delete_btn.pack(side=tk.LEFT, padx=10)

    def create_treeview(self, parent_frame):
        columns_nhanvien = ("Số thứ tự", "Mã nhân viên", "Tên nhân viên", "Vai trò", "Phòng ban", "Email")
        self.tree_nhanvien = ttk.Treeview(parent_frame, columns=columns_nhanvien, show="headings")

        for col in columns_nhanvien:
            self.tree_nhanvien.heading(col, text=col)
            self.tree_nhanvien.column(col, width=100)

        self.tree_nhanvien.pack(fill=tk.BOTH, expand=True)

        h_scroll = ttk.Scrollbar(parent_frame, orient="horizontal", command=self.tree_nhanvien.xview)
        self.tree_nhanvien.configure(xscrollcommand=h_scroll.set)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    def open_centered_window(self, title, fields, submit_callback):
        form = tk.Toplevel(self.master)
        form.title(title)

        window_width, window_height = 400, 300
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        form.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        entries = {}

        for i, (field_name, field_type, options) in enumerate(fields):
            tk.Label(form, text=f"{field_name}:").grid(row=i, column=0, padx=10, pady=5, sticky="e")
            if field_type == "entry":
                entry = tk.Entry(form)
            elif field_type == "date":
                entry = DateEntry(form, date_pattern='dd/mm/yyyy')
            elif field_type == "dropdown":
                entry = ttk.Combobox(form, values=options, width=30)  # Điều chỉnh độ rộng combobox
                entry.current(0)
            else:
                entry = tk.Entry(form)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[field_name] = entry

        submit_btn = tk.Button(form, text="Lưu", command=lambda: submit_callback(entries))
        submit_btn.grid(row=len(fields), column=0, columnspan=2, pady=10)

    def open_create_form(self):
        fields = [
            ("Mã nhân viên", "entry", None),
            ("Tên nhân viên", "entry", None),
            ("Vai trò", "dropdown", ['quan tri vien', 'lap trinh vien', 'kiem thu', 'nguoi dung', 'khach hang']),
            ("Phòng ban", "dropdown", ['Ban Điều Hành', 'IT', 'Nhân sự', 'Tài chính', 'Marketing', 'Bán hàng']),
            ("Email", "entry", None)
        ]

        def submit(entries):
            print("Thêm mới:", {key: entry.get() for key, entry in entries.items()})

        self.open_centered_window("Thêm mới nhân viên", fields, submit)

    def open_read_form(self):
        selected_item = self.tree_nhanvien.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một nhân viên để xem chi tiết")
            return
        item = self.tree_nhanvien.item(selected_item)
        values = item["values"]
        messagebox.showinfo("Thông tin nhân viên", f"Thông tin: {values}")

    def open_update_form(self):
        fields = [
            ("Mã nhân viên", "entry", None),
            ("Tên nhân viên", "entry", None),
            ("Vai trò", "dropdown", ['quan tri vien', 'lap trinh vien', 'kiem thu', 'nguoi dung', 'khach hang']),
            ("Phòng ban", "dropdown", ['Ban Điều Hành', 'IT', 'Nhân sự', 'Tài chính', 'Marketing', 'Bán hàng']),
            ("Email", "entry", None)
        ]

        def submit(entries):
            print("Cập nhật:", {key: entry.get() for key, entry in entries.items()})

        self.open_centered_window("Cập nhật nhân viên", fields, submit)

    def open_delete_form(self):
        selected_item = self.tree_nhanvien.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một nhân viên để xóa")
            return

        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa nhân viên này?")
        if confirm:
            self.tree_nhanvien.delete(selected_item)
            messagebox.showinfo("Thành công", "Đã xóa nhân viên thành công!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Nhân viên")
    root.geometry("800x600")
    app = NhanVienForm(root)
    root.mainloop()
