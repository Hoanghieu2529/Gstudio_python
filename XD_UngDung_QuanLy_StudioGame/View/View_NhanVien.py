import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from models.models_NhanVien import model_NhanVien

class KhungCoSo(tk.Frame):
    """Lớp cơ sở để kế thừa"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.goc = master

    def mo_cua_so(self, tieu_de, truong_du_lieu, ham_gui):
        """Cửa sổ động với các trường linh hoạt"""
        cua_so = tk.Toplevel(self.goc)
        cua_so.title(tieu_de)

        # Căn giữa cửa sổ
        rong, cao = 400, 300
        rong_man_hinh = self.goc.winfo_screenwidth()
        cao_man_hinh = self.goc.winfo_screenheight()
        x = (rong_man_hinh // 2) - (rong // 2)
        y = (cao_man_hinh // 2) - (cao // 2)
        cua_so.geometry(f"{rong}x{cao}+{x}+{y}")

        # Tạo các trường nhập liệu
        o_nhap = {}
        do_rong = 25

        for i, (ten_truong, loai_truong, lua_chon) in enumerate(truong_du_lieu):
            tk.Label(cua_so, text=f"{ten_truong}:", anchor="e").grid(row=i, column=0, padx=10, pady=5, sticky="e")
            if loai_truong == "nhap":
                o = tk.Entry(cua_so, width=do_rong)
            elif loai_truong == "ngay":
                o = DateEntry(cua_so, date_pattern='dd/mm/yyyy', width=do_rong)
            elif loai_truong == "chon":
                o = ttk.Combobox(cua_so, values=lua_chon, width=do_rong - 2)
                o.current(0)
            else:
                o = tk.Entry(cua_so, width=do_rong)
            o.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            o_nhap[ten_truong] = o

        nut_gui = tk.Button(cua_so, text="Lưu", command=lambda: ham_gui(o_nhap))
        nut_gui.grid(row=len(truong_du_lieu), column=0, columnspan=2, pady=10)


class Nhan_vien_form(KhungCoSo):
    """Lớp quản lý giao diện Nhân Viên"""
    def __init__(self, master):
        super().__init__(master, bg="#f8f9fa")
        self.pack(fill=tk.BOTH, expand=True)

        # List giá trị dropdown
        self.vai_tro = ['','quan tri vien', 'lap trinh vien', 'kiem thu', 'nguoi dung', 'khach hang']
        self.phong_ban = ['','Ban Điều Hành', 'IT', 'Nhân sự', 'Tài chính', 'Marketing', 'Bán hàng']

        # Tạo giao diện chính
        self.tao_thanh_cong_cu()
        self.tao_bang_du_lieu()
        self.cap_nhat_du_lieu()

    def tao_thanh_cong_cu(self):
        """Tạo thanh công cụ"""
        thanh_cong_cu = tk.Frame(self, bg="#f8f9fa")
        thanh_cong_cu.pack(fill=tk.X, pady=10)

        # List các nút và hàm tương ứng
        hanh_dong = [
            ("Thêm mới", self.mo_them_moi),
            ("Đọc", self.mo_doc),
            ("Cập nhật", self.mo_cap_nhat),
            ("Xóa", self.mo_xoa)
        ]

        # Tạo nút bằng lambda và list
        for chu, hanh_dong in hanh_dong:
            tk.Button(thanh_cong_cu, text=chu, command=hanh_dong, bg="#f8f9fa").pack(side=tk.LEFT, padx=10)

    def tao_bang_du_lieu(self):
        """Tạo bảng hiển thị danh sách nhân viên"""
        cot = ("Số thứ tự", "Mã nhân viên", "Tên nhân viên", "Vai trò", "Phòng ban", "Email")
        self.bang_nhan_vien = ttk.Treeview(self, columns=cot, show="headings")

        for c in cot:
            self.bang_nhan_vien.heading(c, text=c)
            self.bang_nhan_vien.column(c, width=100)

        self.bang_nhan_vien.pack(fill=tk.BOTH, expand=True)

        cuon_ngang = ttk.Scrollbar(self, orient="horizontal", command=self.bang_nhan_vien.xview)
        self.bang_nhan_vien.configure(xscrollcommand=cuon_ngang.set)
        cuon_ngang.pack(side=tk.BOTTOM, fill=tk.X)

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
            print("Thêm mới:", {k: o.get() for k, o in o_nhap.items()})

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
        truong = [
            ("Mã nhân viên", "nhap", None),
            ("Tên nhân viên", "nhap", None),
            ("Vai trò", "chon", self.vai_tro),
            ("Phòng ban", "chon", self.phong_ban),
            ("Email", "nhap", None)
        ]

        def gui(o_nhap):
            print("Cập nhật:", {k: o.get() for k, o in o_nhap.items()})

        self.mo_cua_so("Cập nhật nhân viên", truong, gui)

    def mo_xoa(self):
        """Xóa nhân viên đã chọn"""
        muc_chon = self.bang_nhan_vien.selection()
        if not muc_chon:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một nhân viên để xóa")
            return

        xac_nhan = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa nhân viên này?")
        if xac_nhan:
            self.bang_nhan_vien.delete(muc_chon)
            messagebox.showinfo("Thành công", "Đã xóa nhân viên thành công!")

    def cap_nhat_du_lieu(self):
        """Cập nhật dữ liệu trong bảng Treeview"""
        # Xóa tất cả các hàng hiện tại
        for hang in self.bang_nhan_vien.get_children():
            self.bang_nhan_vien.delete(hang)

        # Lấy dữ liệu từ model
        danh_sach = model_NhanVien().lay_danh_sach_nhan_vien()
        if not danh_sach:
            messagebox.showwarning("Thông báo", "Không có dữ liệu từ cơ sở dữ liệu.")
            return

        # Thêm dữ liệu vào Treeview
        for stt, nv in enumerate(danh_sach, start=1):  # `enumerate` để tự động tạo Số thứ tự
            try:
                self.bang_nhan_vien.insert("", "end", values=(
                    stt, nv["manv"], nv["ho_ten"], nv["chuc_vu"], nv["ten_phong_ban"], nv["email"]))
            except KeyError as e:
                print(f"Lỗi dữ liệu: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Nhân viên")
    root.geometry("800x600")
    app = Nhan_vien_form(root)
    root.mainloop()
