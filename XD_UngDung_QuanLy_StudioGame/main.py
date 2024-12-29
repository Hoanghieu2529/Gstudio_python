import tkinter as tk
from tkinter import PhotoImage, ttk
from View import Sidebar, NguoiDungForm, View_dang_nhap, View_dang_ky, StudioForm, PhongBanForm, DuAnForm, Nhan_vien_form, CongViecForm
from controllers.controller_dang_ky import controller_dang_ky
from controllers.controller_dang_nhap import controller_dang_nhap
from models.models_NhanVien import model_NhanVien
from View.View_quan_tri import ViewQuanTri
from controllers.controller_quan_tri import ControllerQuanTri

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
        self.controller_quan_tri = None

        # Hiển thị giao diện mặc định
        self.show_form("Người dùng")

    def show_form(self, form_name):
        """Hiển thị giao diện tương ứng dựa trên form_name"""
        if self.current_frame:
            self.current_frame.destroy()

        form_classes = {
            "Người dùng": NguoiDungForm,
            "Studio": StudioForm,
            "Phòng ban": PhongBanForm,
            "Dự án": DuAnForm,
            "Nhân viên": Nhan_vien_form,
            "Công việc": CongViecForm,
            "Quản trị": ViewQuanTri,
        }

        if form_name in form_classes:
            form_class = form_classes[form_name]
            if form_name == "Quản trị":
                self.show_quan_tri()
            else:
                form_instance = form_class(self.root)
                self.current_frame = form_instance.frame if hasattr(form_instance, 'frame') else form_instance
                self.current_frame.pack(fill=tk.BOTH, expand=True)
        else:
            self.current_frame = tk.Frame(self.root, bg="#f8f9fa")
            self.current_frame.pack(fill=tk.BOTH, expand=True)
            tk.Label(self.current_frame, text=f"{form_name} đang được phát triển.", bg="#f8f9fa").pack()

    def show_quan_tri(self):
        """Hiển thị giao diện Quản trị"""
        # Khởi tạo view trước
        view_quan_tri = ViewQuanTri(self.root, None)

        # Khởi tạo controller và truyền view vào controller
        controller_quan_tri = ControllerQuanTri(view_quan_tri)

        # Gán controller vào view
        view_quan_tri.controller = controller_quan_tri

        # Hiển thị view
        self.current_frame = view_quan_tri
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_nhanvien_form(self):
        """Hiển thị và cập nhật dữ liệu Nhân Viên"""
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root, bg="#f8f9fa")
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        tree_nhanvien = ttk.Treeview(
            self.current_frame,
            columns=("manv", "ho_ten", "chuc_vu", "email", "ten_phong_ban"),
            show="headings"
        )
        tree_nhanvien.heading("manv", text="ID")
        tree_nhanvien.heading("ho_ten", text="Họ Tên")
        tree_nhanvien.heading("chuc_vu", text="Chức Vụ")
        tree_nhanvien.heading("email", text="Email")
        tree_nhanvien.heading("ten_phong_ban", text="Phòng Ban")
        tree_nhanvien.pack(fill=tk.BOTH, expand=True)

        # Lấy dữ liệu từ model
        nhan_vien_model = model_NhanVien()
        danh_sach = nhan_vien_model.lay_danh_sach_nhan_vien()

        for nv in danh_sach:
            tree_nhanvien.insert("", "end", values=(
                nv["manv"], nv["ho_ten"], nv["chuc_vu"], nv["email"], nv["ten_phong_ban"]))

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
