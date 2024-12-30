import tkinter as tk
from tkinter import ttk

class ViewTinhLuong(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pack(fill=tk.BOTH, expand=True)
        self.tao_giao_dien()

    def tao_giao_dien(self):
        thanh_cong_cu = tk.Frame(self, bg="#f8f9fa")
        thanh_cong_cu.pack(fill=tk.X, pady=10)

        tk.Button(
            thanh_cong_cu,
            text="Xuất Excel",
            command=lambda: self.controller.xuat_excel() if self.controller else None
        ).pack(side=tk.LEFT, padx=10)

        tk.Button(
            thanh_cong_cu,
            text="Xuất PDF",
            command=lambda: self.controller.xuat_pdf() if self.controller else None
        ).pack(side=tk.LEFT, padx=10)

        cot = ("Mã NV", "Họ Tên", "Phòng Ban", "Lương Cơ Bản", "Ngày Công", "Tổng Lương")
        self.bang_luong = ttk.Treeview(self, columns=cot, show="headings")

        for c in cot:
            self.bang_luong.heading(c, text=c)
            self.bang_luong.column(c, width=100)

        self.bang_luong.pack(fill=tk.BOTH, expand=True)

    def hien_thi_du_lieu(self, du_lieu):
        """Hiển thị dữ liệu lên bảng Treeview."""
        if not du_lieu:
            return

        for row in self.bang_luong.get_children():
            self.bang_luong.delete(row)

        for nv in du_lieu:
            tong_luong = nv["luong_co_ban"] * nv["ngay_cong"] / 22
            self.bang_luong.insert("", "end", values=(
                nv["manv"], nv["ho_ten"], nv["ten_phong_ban"], nv["luong_co_ban"], nv["ngay_cong"], tong_luong
            ))


