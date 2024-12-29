import tkinter as tk
from tkinter import PhotoImage, ttk
from View import Sidebar, NguoiDungForm, View_dang_nhap, View_dang_ky, StudioForm, PhongBanForm, DuAnForm, NhanVienForm, \
    CongViecForm
from controllers.controller_dang_ky import controller_dang_ky
from controllers.controller_dang_nhap import controller_dang_nhap


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
        self.root.geometry("1200x800")
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

        form = {
            "Người dùng": NguoiDungForm,
            "Studio": StudioForm,
            "Phòng ban": PhongBanForm,
            "Dự án": DuAnForm,
            "Nhân viên": NhanVienForm,
            "Công việc": CongViecForm,
        }

        form_class = form.get(form_name)
        if form_class:
            self.current_frame = form_class(self.root).frame
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
