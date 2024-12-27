import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from View.Sidebar import Sidebar
from View.View_Nguoidung import NguoiDungForm
from View.View_Studio import StudioForm
from View.View_Phongban import PhongBanForm
from View.View_DuAn import DuAnForm
from View.View_NhanVien import NhanVienForm
from View.View_CongViec import CongViecForm
from View.View_dang_nhap import View_dang_nhap
from controllers.controller_dang_ky import controller_dang_ky
from controllers.controller_dang_nhap import controller_dang_nhap
from View.View_dang_ky import View_dang_ky

def center_window(window, width, height):
    """Căn giữa cửa sổ trên màn hình"""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def goi_dang_ky():
    """Hàm gọi giao diện đăng ký"""
    toplevel = tk.Toplevel()  # Tạo cửa sổ mới
    controller = controller_dang_ky()
    View_dang_ky(toplevel, controller)
    toplevel.mainloop()


class MainApp:
    def __init__(self, root):
        """Khởi tạo giao diện chính của ứng dụng"""
        self.root = root
        self.root.title("HỆ THỐNG QUẢN LÝ DỰ ÁN STUDIO")
        # self.root.geometry("1200x800")
        center_window(self.root, 1200, 800)
        try:
            self.root.iconphoto(False, PhotoImage(file="Images/Logo_studio.png"))
        except Exception as e:
            print(f"Lỗi khi tải logo: {e}")

            # Tạo Sidebar và Frame chính
        self.sidebar = Sidebar(self.root, self.show_form)
        self.current_frame = None
        self.show_form("Người dùng")  # Hiển thị giao diện mặc định

    def show_form(self, form_name):
        """Hiển thị giao diện tương ứng dựa trên form_name"""
        if self.current_frame:
            self.current_frame.destroy()  # Xóa frame hiện tại

        forms = {
            "Người dùng": NguoiDungForm,
            "Studio": StudioForm,
            "Phòng ban": PhongBanForm,
            "Dự án": DuAnForm,
            "Nhân viên": NhanVienForm,
            "Công việc": CongViecForm
        }
        form_class = forms.get(form_name)
        if form_class:
            self.current_frame = form_class(self.root).frame
        # if form_name == "Người dùng":
        #     self.current_frame = NguoiDungForm(self.root).frame
        # elif form_name == "Studio":
        #     self.current_frame = StudioForm(self.root).frame
        # elif form_name == "Phòng ban":
        #     self.current_frame = PhongBanForm(self.root).frame
        # elif form_name == "Dự án":
        #     self.current_frame = DuAnForm(self.root).frame
        # elif form_name == "Nhân viên":
        #     self.current_frame = NhanVienForm(self.root).frame
        # elif form_name == "Công việc":
        #     self.current_frame = CongViecForm(self.root).frame
        else:
            self.current_frame = tk.Frame(self.root, bg="#f8f9fa")
            self.current_frame.pack(fill=tk.BOTH, expand=True)
            tk.Label(self.current_frame, text=f"{form_name} đang được phát triển.", bg="#f8f9fa").pack()


def ham_chinh():
    """Chạy ứng dụng sau khi đăng nhập thành công"""
    root = tk.Tk()  # Tạo cửa sổ chính
    app = MainApp(root)  # Khởi tạo ứng dụng chính
    root.mainloop()


if __name__ == "__main__":
    # Khởi chạy giao diện đăng nhập trước
    root = tk.Tk()
    controller_dangnhap = controller_dang_nhap()

    def khi_dang_nhap_thanh_cong():
        """Chuyển sang giao diện chính sau khi đăng nhập thành công"""
        root.destroy()  # Đóng cửa sổ đăng nhập
        ham_chinh()  # Mở giao diện chính

    login_view = View_dang_nhap(root, controller_dangnhap, khi_dang_nhap_thanh_cong)
    root.mainloop()
