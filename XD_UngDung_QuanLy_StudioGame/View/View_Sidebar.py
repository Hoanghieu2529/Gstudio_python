import os
from PIL import Image, ImageTk
import tkinter as tk

class Sidebar(tk.Frame):
    def __init__(self, master, hien_thi_form):
        super().__init__(master, bg="#2C2C2E", width=200, height=600)
        self.pack(side=tk.LEFT, fill=tk.Y, padx=0)

        self.nut_chinh = {}
        self.khung_menu_con = {}  # Lưu trữ frame cho từng submenu
        self.nut_duoc_chon = None  # Theo dõi nút được chọn hiện tại
        self.icons = {}  # Lưu trữ các hình ảnh để tránh load lại nhiều lần

        # Đường dẫn tới thư mục Images
        self.icon_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Images")

        # Cấu trúc các menu chính và phụ với icon tương ứng
        cau_truc_menu = {
            "Điều hành": [("Quản trị", "quan_tri.png"), ("Studio - Báo cáo", "studio.png"), ("Phòng ban", "phong_ban.png")],
            "Nhân sự": [("Nhân viên", "nhan_vien.png"),  ("Báo cáo nhân sự", "bao_cao.png"), ("Tính lương", "tinh_luong.png")],
            "Công việc": [("Dự án", "du_an.png"), ("Báo cáo tiến độ", "bao_cao_tien_do.png")],
            "Tài chính": [("Chi phí", "chi_phi.png"), ("Doanh thu", "doanh_thu.png"), ("Báo cáo tổng hợp", "tong_hop.png")]
        }

        for menu_chinh, menu_phu in cau_truc_menu.items():
            # Thêm menu chính
            nut_menu_chinh = tk.Button(
                self,
                text=menu_chinh,
                bg="#1C1C1E",  # Màu nền tối
                fg="white",  # Màu chữ sáng
                bd=0,
                pady=12,
                padx=10,
                anchor="w",
                font=("San Francisco", 14, "bold"),  # Font in đậm
                activebackground="#007AFF",  # Màu khi nhấn
                activeforeground="white",
                highlightthickness=0,  # Tắt đường viền khi chọn
                relief="flat",
                command=lambda opt=menu_chinh: self.mo_menu_con(opt)
            )
            nut_menu_chinh.pack(fill=tk.X, padx=0, pady=5)
            self.nut_chinh[menu_chinh] = nut_menu_chinh

            # Frame chứa các menu con
            khung_menu_con = tk.Frame(self, bg="#2C2C2E")
            khung_menu_con.pack(fill=tk.X, padx=0, pady=0)
            khung_menu_con.pack_forget()
            self.khung_menu_con[menu_chinh] = khung_menu_con

            for menu, icon in menu_phu:
                # Đường dẫn icon
                icon_path = os.path.join(self.icon_folder, icon)

                try:
                    img = Image.open(icon_path).resize((20, 20), Image.Resampling.LANCZOS)
                    img = ImageTk.PhotoImage(img)
                    self.icons[menu] = img
                except FileNotFoundError:
                    print(f"Lỗi: Không tìm thấy file ảnh {icon_path}")
                    img = None

                nut_menu_phu = tk.Button(
                    khung_menu_con,
                    text=f"  {menu}",  # Thụt lề để phân biệt
                    image=img,
                    compound=tk.LEFT,  # Đặt icon bên trái
                    bg="#333333",  # Màu nhạt hơn cho submenu
                    fg="white",
                    bd=0,
                    pady=8,
                    padx=10,
                    anchor="w",  # Căn text sát lề trái
                    font=("San Francisco", 12),
                    activebackground="#007AFF",
                    activeforeground="white",
                    highlightthickness=0,
                    relief="flat",
                    command=lambda opt=menu: self.tuy_chon_mau(opt, hien_thi_form)
                )
                nut_menu_phu.pack(fill=tk.X, padx=0, pady=2)
                self.nut_chinh[menu] = nut_menu_phu

        # Thêm nút chức năng bổ sung
        self.them_nut_bo_sung(hien_thi_form)

    def mo_menu_con(self, menu_chinh):
        """Hiển thị hoặc ẩn submenu khi bấm vào menu chính"""
        khung_menu_con = self.khung_menu_con[menu_chinh]
        if khung_menu_con.winfo_ismapped():
            khung_menu_con.pack_forget()  # Ẩn submenu
        else:
            # Tìm vị trí để hiển thị submenu ngay dưới nút chính
            for khung in self.khung_menu_con.values():
                khung.pack_forget()
            khung_menu_con.pack(after=self.nut_chinh[menu_chinh])  # Hiển thị submenu ngay dưới nút chính

    def tuy_chon_mau(self, tuy_chon, hien_thi_form):
        """Thay đổi màu nút khi được chọn"""
        # Reset màu tất cả các nút
        for nut, _ in self.nut_chinh.items():
            if nut in self.khung_menu_con:
                self.nut_chinh[nut].config(bg="#1C1C1E", fg="white")
            else:
                self.nut_chinh[nut].config(bg="#333333", fg="white")

        # Đổi màu nút được chọn
        nut_duoc_chon = self.nut_chinh[tuy_chon]
        nut_duoc_chon.config(bg="#007AFF", fg="white")  # Màu xanh iOS

        # Lưu trạng thái nút được chọn
        self.nut_duoc_chon = nut_duoc_chon

        # Gọi callback để hiển thị form tương ứng
        hien_thi_form(tuy_chon)

    def them_nut_bo_sung(self, hien_thi_form):
        """Thêm nút chức năng bổ sung (Cài đặt, Đăng xuất)"""
        ngan_cach = tk.Frame(self, bg="#2C2C2E", height=2)
        ngan_cach.pack(fill=tk.X, pady=5)

        # Nút cài đặt
        tk.Button(
            self,
            text="Cài đặt",
            bg="#1C1C1E",
            fg="white",
            bd=0,
            pady=12,
            padx=10,
            anchor="w",
            font=("San Francisco", 14, "bold"),
            activebackground="#007AFF",
            activeforeground="white",
            relief="flat",
            command=lambda: hien_thi_form("Cài đặt")
        ).pack(fill=tk.X, padx=0, pady=5)

        # Nút đăng xuất
        tk.Button(
            self,
            text="Đăng xuất",
            bg="#D32F2F",  # Màu đỏ cảnh báo
            fg="white",
            bd=0,
            pady=12,
            padx=10,
            anchor="w",
            font=("San Francisco", 14, "bold"),
            activebackground="#FF5252",
            activeforeground="white",
            relief="flat",
            command=lambda: hien_thi_form("Đăng xuất")
        ).pack(fill=tk.X, padx=0, pady=5)

# Test
if __name__ == "__main__":
    def mock_callback(option):
        print(f"Selected: {option}")

    root = tk.Tk()
    root.geometry("300x600")
    sidebar = Sidebar(root, mock_callback)
    root.mainloop()
