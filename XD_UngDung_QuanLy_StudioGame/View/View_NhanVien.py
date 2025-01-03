import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from View.View_BaseForm import KhungCoSo
from models.models_NhanVien import ModelNhanVien


class Nhanvienform(KhungCoSo):
    """Tạo lớp quản lý giao diện Nhân Viên"""
    def __init__(self, master):
        """
        Khởi tạo giao diện quản lý Nhân Viên.

        Args:
            master: Cửa sổ hoặc khung chứa giao diện.
            controller: Đối tượng điều khiển để xử lý logic và giao tiếp với mô hình dữ liệu.
        """
        super().__init__(master, bg="#f8f9fa")
        self.pack(fill=tk.BOTH, expand=True)
        self.bang_nhan_vien = None

        # Tiêu đề cho giao diện này
        self.tao_tieu_de("Quản lý Nhân viên")

        # List giá trị dropdown
        self.vai_tro = ['quan tri vien', 'lap trinh vien', 'kiem thu', 'nguoi dung', 'khach hang']
        self.phong_ban = ['Ban Điều Hành', 'IT', 'Nhân sự', 'Tài chính', 'Marketing', 'Bán hàng']

        # Tạo giao diện chính
        self.tao_thanh_cong_cu()
        self.tao_bang_du_lieu()
        self.cap_nhat_du_lieu()

        # Đảm bảo đường dẫn đúng đến thư mục Images
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Lấy đường dẫn cha của thư mục View
        icon_path = os.path.join(base_path, "Images", "chinh_sua.png")

        # Tải ảnh từ đường dẫn chính xác
        self.icon_edit = ImageTk.PhotoImage(Image.open(icon_path).resize((20, 20)))

    def tao_tieu_de(self, tieu_de_text):
        """Tạo tiêu đề ở phía trên giao diện"""
        tieu_de = tk.Label(self, text=tieu_de_text, font=("San Francisco", 16, "bold"), bg="#f8f9fa", fg="#333")
        tieu_de.pack(pady=10)

    def tao_thanh_cong_cu(self):
        """Tạo thanh công cụ"""
        thanh_cong_cu = tk.Frame(self, bg="#f8f9fa")
        thanh_cong_cu.pack(fill=tk.X, pady=10)

        hanh_dong = [
            ("Thêm mới", self.mo_them_moi),
            ("Đọc", self.mo_doc),
            ("Cập nhật", self.mo_cap_nhat),
            ("Xóa", self.mo_xoa)
        ]

        for chu, hanh_dong in hanh_dong:
            tk.Button(thanh_cong_cu, text=chu, command=hanh_dong, bg="#f8f9fa").pack(side=tk.LEFT, padx=10)

    def tao_bang_du_lieu(self):
        """Tạo bảng hiển thị danh sách nhân viên"""
        cot = ("Số thứ tự", "Mã nhân viên", "Tên nhân viên", "Vai trò", "Phòng ban", "Email", "Chỉnh Sửa")
        self.bang_nhan_vien = ttk.Treeview(self, columns=cot, show="headings")

        for c in cot[:-1]:
            self.bang_nhan_vien.heading(c, text=c)
            self.bang_nhan_vien.column(c, width=100, anchor="center")
        self.bang_nhan_vien.heading("Chỉnh Sửa", text="")
        self.bang_nhan_vien.column("Chỉnh Sửa", width=50, anchor="center")

        self.bang_nhan_vien.pack(fill=tk.BOTH, expand=True)

        cuon_ngang = ttk.Scrollbar(self, orient="horizontal", command=self.bang_nhan_vien.xview)
        self.bang_nhan_vien.configure(xscrollcommand=cuon_ngang.set)
        cuon_ngang.pack(side=tk.BOTTOM, fill=tk.X)

        self.bang_nhan_vien.bind("<Double-1>", self.mo_cap_nhat_tu_bang)

    def mo_them_moi(self):
        """Mở form thêm nhân viên"""
        truong = [
            ("Mã nhân viên", "nhap", None),
            ("Tên nhân viên", "nhap", None),
            ("Vai trò", "chon", self.vai_tro),
            ("Phòng ban", "chon", self.phong_ban),
            ("Email", "nhap", None)
        ]

        def gui(o_nhap):
            ho_ten = o_nhap["Họ tên"].get()
            chuc_vu = o_nhap["Chức vụ"].get()
            ten_phong_ban = o_nhap["Phòng ban"].get()
            email = o_nhap["Email"].get()

            mapb = next(
                (pb["mapb"] for pb in ModelNhanVien().lay_danh_sach_phong_ban() if
                 pb["ten_phong_ban"] == ten_phong_ban),
                None
            )

            ModelNhanVien().them_nhan_vien(ho_ten, chuc_vu, mapb, email)  # Thêm nhân viên vào CSDL
            self.cap_nhat_du_lieu()  # Cập nhật lại Treeview
            messagebox.showinfo("Thành công", "Thêm nhân viên thành công!")

        self.mo_cua_so("Thêm mới nhân viên", truong, gui)

    def mo_doc(self):
        """Hiển thị thông tin nhân viên đã chọn"""
        muc_chon = self.bang_nhan_vien.selection()
        if not muc_chon:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một nhân viên để xem chi tiết")
            return
        muc = self.bang_nhan_vien.item(muc_chon)
        gia_tri = muc["values"]
        messagebox.showinfo("Thông tin nhân viên", f"Thông tin: {gia_tri}")

    def mo_cap_nhat(self):
        """Mở form cập nhật nhân viên"""
        muc_chon = self.bang_nhan_vien.selection()
        if not muc_chon:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một nhân viên để cập nhật")
            return
        item = muc_chon[0]
        values = self.bang_nhan_vien.item(item, "values")
        self.mo_form_chinh_sua(item, values)

    def mo_xoa(self):
        """Xóa nhân viên đã chọn"""
        muc_chon = self.bang_nhan_vien.selection()
        if not muc_chon:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một nhân viên để xóa")
            return

        xac_nhan = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa nhân viên này?")
        if xac_nhan:
            item = muc_chon[0]
            manv = self.bang_nhan_vien.item(item, "values")[1]  # Lấy Mã nhân viên
            ModelNhanVien().xoa_nhan_vien(manv)  # Xóa nhân viên trong CSDL
            self.cap_nhat_du_lieu()  # Cập nhật lại Treeview
            messagebox.showinfo("Thành công", "Đã xóa nhân viên thành công!")

    def cap_nhat_du_lieu(self):
        """Cập nhật dữ liệu trong bảng Treeview"""
        for hang in self.bang_nhan_vien.get_children():
            self.bang_nhan_vien.delete(hang)

        danh_sach = ModelNhanVien().lay_danh_sach_nhan_vien()
        if not danh_sach:
            messagebox.showwarning("Thông báo", "Không có dữ liệu từ cơ sở dữ liệu.")
            return

        for stt, nv in enumerate(danh_sach, start=1):
            self.bang_nhan_vien.insert(
                "", "end", values=(stt, nv["manv"], nv["ho_ten"], nv["chuc_vu"], nv["ten_phong_ban"], nv["email"], ""),
                tags=("editable",)
            )

    def mo_cap_nhat_tu_bang(self, event):
        """Mở form cập nhật khi nhấp đúp hoặc nhấp vào icon chỉnh sửa"""
        item = self.bang_nhan_vien.identify_row(event.y)
        if not item:
            return

        values = self.bang_nhan_vien.item(item, "values")
        self.mo_form_chinh_sua(item, values)

    def mo_form_chinh_sua(self, item, values):
        """Hàm mở form chỉnh sửa thông tin nhân viên"""
        form = tk.Toplevel(self)
        form.title("Chỉnh sửa nhân viên")

        fields = ["Họ tên", "Chức vụ", "Phòng ban", "Email"]
        entries = {}

        for i, field in enumerate(fields):
            tk.Label(form, text=field).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(form, width=30)
            entry.insert(0, values[i + 1])
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[field] = entry

        def cap_nhat():
            manv = values[1]
            ho_ten = entries["Họ tên"].get()
            chuc_vu = entries["Chức vụ"].get()
            ten_phong_ban = entries["Phòng ban"].get()
            email = entries["Email"].get()

            mapb = next(
                (pb["mapb"] for pb in ModelNhanVien().lay_danh_sach_phong_ban() if
                 pb["ten_phong_ban"] == ten_phong_ban),
                None
            )

            ModelNhanVien().cap_nhat_nhan_vien(manv, ho_ten, chuc_vu, mapb, email)  # Cập nhật CSDL
            self.cap_nhat_du_lieu()  # Cập nhật lại Treeview
            form.destroy()
            messagebox.showinfo("Thành công", "Cập nhật nhân viên thành công!")

        tk.Button(form, text="Cập nhật", command=cap_nhat).grid(row=len(fields), column=0, columnspan=2, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Nhân viên")
    root.geometry("800x600")
    app = Nhanvienform(root)
    root.mainloop()
