import tkinter as tk
from tkinter import ttk

class ViewTinhLuong(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pack(fill=tk.BOTH, expand=True)
        self.tao_giao_dien()

    def tao_giao_dien(self):
        """Tạo giao diện chính của bảng tính lương"""

        # Thêm tiêu đề
        self.tao_tieu_de("Bảng tính lương tháng")

        # Thanh công cụ
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

        # Bảng hiển thị dữ liệu lương
        cot = ("Mã NV", "Họ Tên", "Chức Vụ", "Lương Cơ Bản", "Ngày Công", "Tổng Lương")
        self.bang_luong = ttk.Treeview(self, columns=cot, show="headings")

        for c in cot:
            self.bang_luong.heading(c, text=c)
            if c in ("Mã NV", "Lương Cơ Bản", "Ngày Công", "Tổng Lương"):
                self.bang_luong.column(c, anchor="center", width=120)
            else:
                self.bang_luong.column(c, anchor="w", width=100)

        self.bang_luong.pack(fill=tk.BOTH, expand=True)

    def tao_tieu_de(self, tieu_de_text):
        """Tạo tiêu đề ở phía trên giao diện"""
        tieu_de = tk.Label(self, text=tieu_de_text, font=("Arial", 16, "bold"), bg="#f8f9fa", fg="#333")
        tieu_de.pack(pady=10)

    def hien_thi_du_lieu(self, du_lieu):
        """Hiển thị dữ liệu lên bảng Treeview."""
        # Xóa các dòng cũ
        for row in self.bang_luong.get_children():
            self.bang_luong.delete(row)

        # Thêm dữ liệu mới vào bảng
        for nv in du_lieu:
            tong_luong = int((nv["luong_cb"] / 22) * nv["ngay_cong"])  # Tính tổng lương
            self.bang_luong.insert("", "end", values=(
                nv["manv"],
                nv["ho_ten"],
                nv["chuc_vu"],  # Thay 'ten_phong_ban' thành 'chuc_vu'
                "{:,} VNĐ".format(int(nv["luong_cb"])),  # Định dạng lương cơ bản
                nv["ngay_cong"],
                "{:,} VNĐ".format(tong_luong)  # Định dạng tổng lương
            ))

# Kiểm thử giao dien tinh luong
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bảng tính lương")
    root.geometry("800x600")

    # Dữ liệu mẫu
    du_lieu_mau = [
        {"manv": 101, "ho_ten": "Nguyễn Văn A", "chuc_vu": "Nhân viên", "luong_cb": 8000000, "ngay_cong": 20},
        {"manv": 102, "ho_ten": "Trần Thị B", "chuc_vu": "Trưởng phòng", "luong_cb": 12000000, "ngay_cong": 22},
        {"manv": 103, "ho_ten": "Lê Văn C", "chuc_vu": "Nhân viên", "luong_cb": 7000000, "ngay_cong": 18},
    ]

    # Hiển thị giao diện
    app = ViewTinhLuong(root, None)
    app.hien_thi_du_lieu(du_lieu_mau)

    root.mainloop()

