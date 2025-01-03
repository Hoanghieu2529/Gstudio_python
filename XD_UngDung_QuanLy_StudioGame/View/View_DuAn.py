import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class DuAnForm(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pack(fill=tk.BOTH, expand=True)
        self.tao_giao_dien()

    def tao_giao_dien(self):
        """Tạo giao diện Quản lý dự án"""
        tk.Label(self, text="Quản lý Dự án", font=("San Francisco", 16)).pack(pady=10)

        # Thanh công cụ
        thanh_cong_cu = tk.Frame(self)
        thanh_cong_cu.pack(fill=tk.X, pady=10)

        tk.Button(thanh_cong_cu, text="Thêm mới", command=self.mo_form_them).pack(side=tk.LEFT, padx=5)
        tk.Button(thanh_cong_cu, text="Cập nhật", command=self.mo_form_cap_nhat).pack(side=tk.LEFT, padx=5)
        tk.Button(thanh_cong_cu, text="Xóa", command=self.xoa_du_an).pack(side=tk.LEFT, padx=5)

        # Bảng dữ liệu
        cot = ("Mã Dự Án", "Tên Dự Án", "Mô Tả", "Ngày Bắt Đầu", "Ngày Kết Thúc", "Trạng Thái")
        self.bang_du_an = ttk.Treeview(self, columns=cot, show="headings")

        for c in cot:
            self.bang_du_an.heading(c, text=c)
            self.bang_du_an.column(c, width=150)

        self.bang_du_an.pack(fill=tk.BOTH, expand=True)

        self.hien_thi_du_lieu()#ban đầu

    # def hien_thi_du_lieu(self, du_lieu):
    #     """Hiển thị dữ liệu từ model"""
    #     for row in self.bang_du_an.get_children():
    #         self.bang_du_an.delete(row)
    #     for du_an in du_lieu:
    #         self.bang_du_an.insert("", "end", values=(du_an["mada"], du_an["ten_du_an"], du_an["mo_ta"],
    #                                                   du_an["ngay_bat_dau"], du_an["ngay_ket_thuc"], du_an["trang_thai"]))
    def hien_thi_du_lieu(self, du_lieu=None):
        """Hiển thị dữ liệu từ model"""
        if du_lieu is None:
            du_lieu = []  # Nếu không có dữ liệu thì dùng danh sách rỗng

        # Xóa dữ liệu cũ trong bảng
        for row in self.bang_du_an.get_children():
            self.bang_du_an.delete(row)

        # Thêm dữ liệu mới vào bảng
        for du_an in du_lieu:
            self.bang_du_an.insert("", "end", values=(
                du_an.get("mada", ""),
                du_an.get("ten_du_an", ""),
                du_an.get("mo_ta", ""),
                du_an.get("ngay_bat_dau", ""),
                du_an.get("ngay_ket_thuc", ""),
                du_an.get("trang_thai", "")
            ))

    def mo_form_them(self):
        """Mở form thêm mới dự án"""
        self.mo_form_chi_tiet("Thêm dự án", {}, self.controller.them_du_an)

    def mo_form_cap_nhat(self):
        """Mở form cập nhật dự án"""
        muc_chon = self.bang_du_an.selection()
        if not muc_chon:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một dự án để cập nhật")
            return
        du_lieu = self.bang_du_an.item(muc_chon)["values"]
        du_an = {
            "mada": du_lieu[0],
            "ten_du_an": du_lieu[1],
            "mo_ta": du_lieu[2],
            "ngay_bat_dau": du_lieu[3],
            "ngay_ket_thuc": du_lieu[4],
            "trang_thai": du_lieu[5],
        }
        self.mo_form_chi_tiet("Cập nhật dự án", du_an, self.controller.cap_nhat_du_an)

    def mo_form_chi_tiet(self, tieu_de, du_an, ham_gui):
        """Mở form chi tiết (Thêm hoặc Cập nhật)"""
        form = tk.Toplevel(self)
        form.title(tieu_de)
        form.geometry("400x300")

        tk.Label(form, text="Tên Dự Án").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        tk.Label(form, text="Mô Tả").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        tk.Label(form, text="Ngày Bắt Đầu").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        tk.Label(form, text="Ngày Kết Thúc").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        tk.Label(form, text="Trạng Thái").grid(row=4, column=0, padx=10, pady=5, sticky="e")

        ten_du_an = tk.Entry(form)
        ten_du_an.grid(row=0, column=1, padx=10, pady=5)
        ten_du_an.insert(0, du_an.get("ten_du_an", ""))

        mo_ta = tk.Entry(form)
        mo_ta.grid(row=1, column=1, padx=10, pady=5)
        mo_ta.insert(0, du_an.get("mo_ta", ""))

        ngay_bat_dau = DateEntry(form, date_pattern="yyyy-mm-dd")
        ngay_bat_dau.grid(row=2, column=1, padx=10, pady=5)
        ngay_bat_dau.set_date(du_an.get("ngay_bat_dau", "2000-01-01"))

        ngay_ket_thuc = DateEntry(form, date_pattern="yyyy-mm-dd")
        ngay_ket_thuc.grid(row=3, column=1, padx=10, pady=5)
        ngay_ket_thuc.set_date(du_an.get("ngay_ket_thuc", "2000-01-01"))

        trang_thai = ttk.Combobox(form, values=["hoàn thành", "đang thực hiện", "chưa hoàn thành", "hủy bỏ"])
        trang_thai.grid(row=4, column=1, padx=10, pady=5)
        trang_thai.set(du_an.get("trang_thai", "hoàn thành"))

        def gui_du_lieu():
            data = {
                "ten_du_an": ten_du_an.get(),
                "mo_ta": mo_ta.get(),
                "ngay_bat_dau": ngay_bat_dau.get(),
                "ngay_ket_thuc": ngay_ket_thuc.get(),
                "trang_thai": trang_thai.get(),
            }
            if "mada" in du_an:
                data["mada"] = du_an["mada"]
            ham_gui(data)
            form.destroy()

        tk.Button(form, text="Lưu", command=gui_du_lieu).grid(row=5, column=0, columnspan=2, pady=10)

    def xoa_du_an(self):
        """Xóa dự án được chọn"""
        muc_chon = self.bang_du_an.selection()
        if not muc_chon:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một dự án để xóa")
            return
        xac_nhan = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa dự án này không?")
        if xac_nhan:
            du_an_id = self.bang_du_an.item(muc_chon)["values"][0]
            self.controller.xoa_du_an(du_an_id)
