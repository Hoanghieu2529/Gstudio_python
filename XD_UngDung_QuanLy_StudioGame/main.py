import tkinter as tk
from tkinter import PhotoImage, messagebox
from View import Sidebar, View_dang_nhap, View_dang_ky, StudioForm, PhongBanForm, Nhanvienform, CongViecForm
from View.View_DuAn import DuAnForm
from controllers.controller_dang_ky import controller_dang_ky
from controllers.controller_dang_nhap import controller_dang_nhap
from View.View_quan_tri import ViewQuanTri
from View.View_Nguoidung import NguoiDungForm
from controllers.controller_quan_tri import ControllerQuanTri
from View.View_tinh_luong import ViewTinhLuong
from controllers.controller_tinh_luong import ControllerTinhLuong
from controllers.controller_DuAn import DuAnFormController
from controllers.controller_BaoCaoNhanSu import ControllerBaoCaoNhanSu


def goi_dang_ky():
    """Hàm gọi giao diện đăng ký
    - Đầu ra: Hiển thị cửa sổ giao diện đăng ký (View_dang_ky)."""
    toplevel = tk.Toplevel()
    controller = controller_dang_ky()
    View_dang_ky(toplevel, controller)
    toplevel.mainloop()

class MainApp:
    """
    Lớp quản lý giao diện chính của ứng dụng.
    """
    def __init__(self, root, vai_tro):
        """ Khởi tạo giao diện chính của ứng dụng.
        - Đầu vào:
            + root: Cửa sổ chính của tkinter.
            + vai_tro: Vai trò của người dùng (vd: Quản trị, Nhân viên, v.v.).
        - Đầu ra: Hiển thị giao diện chính với Sidebar và nội dung tương ứng
        """
        self.root = root
        self.vai_tro = vai_tro
        self.root.title("HỆ THỐNG QUẢN LÝ DỰ ÁN STUDIO")
        self.root.geometry("1200x800")

        try:
            self.root.iconphoto(False, PhotoImage(file="Images/Logo_studio.png"))
        except Exception as e:
            print(f"Lỗi khi tải logo: {e}")

        # Tạo Sidebar và Frame chính
        self.sidebar = Sidebar(self.root, self.show_form, self.vai_tro)
        self.current_frame = None

        # Hiển thị giao diện mặc định
        self.show_form("Phòng ban")  # Mặc định hiển thị giao diện Dự án

    # def init_database(self):
    #     """Khởi tạo """
    #     from models.database import Database
    #     return Database()

    def show_form(self, form_name):
        """Hiển thị giao diện tương ứng với tên form.

        - Đầu vào:
            + form_name: Tên form cần hiển thị (vd: "Phòng ban", "Nhân viên", v.v.).
        - Đầu ra:
            + Hiển thị nội dung tương ứng trên giao diện chính.
            + Hiển thị thông báo nếu form đang được phát triển hoặc không tồn tại."""
        if self.current_frame:
            self.current_frame.destroy()
        from models.database import Database
        database = Database()

        # Tạo các class liên quan đến form
        form_classes = {
            "Người dùng": NguoiDungForm,
            "Studio": lambda: StudioForm(self.root, None),
            "Phòng ban": PhongBanForm,
            "Dự án": DuAnForm,
            # "Nhân viên": lambda: Nhanvienform(self.root, ControllerQuanTri(self.root)),
            "Nhân viên": Nhanvienform,
            "Công việc": lambda: CongViecForm(self.root, None),
            "Quản trị": self.show_quan_tri,
            "Tính lương": lambda: self.create_tinh_luong_form(database),
            "Báo cáo nhân sự": self.show_bao_cao_nhan_su,
        }
        # form_classes = {
        #     "Người dùng": NguoiDungForm,
        #     "Studio": StudioForm,
        #     "Phòng ban": PhongBanForm,
        #     "Dự án": DuAnForm,
        #     "Nhân viên": Nhanvienform,
        #     "Công việc": CongViecForm,
        #     "Quản trị": ControllerQuanTri,
        #     "Tính lương": ControllerTinhLuong,
        #     # "Báo cáo nhân sự": self.show_bao_cao_nhan_su,
        #     "Báo cáo nhân sự": lambda: self.show_bao_cao_nhan_su(),
        # }
        # if form_name == "Đăng xuất":
        #     self.sidebar.dang_xuat()  # Gọi hàm đăng xuất
        #     return

        if form_name == "Đăng xuất":
            if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn đăng xuất không?"):
                self.sidebar.dang_xuat()
                self.root.destroy()
            return

        # Kiểm tra và xử lý từng form
        if form_name in form_classes:
            form_class = form_classes[form_name]
            if form_name == "Quản trị":
                self.show_quan_tri()

            elif form_name == "Dự án":
                self.show_du_an()
            elif form_name == "Tính lương":
                self.show_tinh_luong()
            elif form_name == "Báo cáo nhân sự":
                bao_cao_controller = ControllerBaoCaoNhanSu(self.root)
                self.current_frame = bao_cao_controller.view  # Sử dụng thuộc tính `view` thay vì `_view`
                self.current_frame.pack(fill=tk.BOTH, expand=True)
            else:
                # Hiển thị các form khác
                form_instance = form_class(self.root)
                self.current_frame = form_instance.frame if hasattr(form_instance, 'frame') else form_instance
                self.current_frame.pack(fill=tk.BOTH, expand=True)
        else:
            # Form chưa phát triển
            self.current_frame = tk.Frame(self.root, bg="#f8f9fa")
            self.current_frame.pack(fill=tk.BOTH, expand=True)
            tk.Label(self.current_frame, text=f"{form_name} đang được phát triển.", bg="#f8f9fa").pack()

    def show_quan_tri(self):
        """
        Hiển thị giao diện quản trị.
        - Đầu vào: Không có.
        - Đầu ra: Hiển thị giao diện quản lý cho quản trị viên.
        """
        # if hasattr(self, "_current_form") and self._current_form == "Quản trị":
        #     return
        if self.current_frame:
            self.current_frame.destroy()  # Hủy frame cũ nếu có

        self._current_form = "Quản trị"  # Cập nhật form hiện tại

        from models.database import Database
        database = Database()

        from View.View_quan_tri import ViewQuanTri
        from controllers.controller_quan_tri import ControllerQuanTri

        view = ViewQuanTri(self.root, None)
        controller = ControllerQuanTri(view, database)
        view.controller = controller

        self.current_frame = view
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_du_an(self):
        """
        Hiển thị giao diện quản lý dự án.
        - Đầu vào: Không có.
        - Đầu ra: Hiển thị giao diện quản lý dự án và liên kết với controller của Dự án.
        """
        view_du_an = DuAnForm(self.root, None)
        controller_du_an = DuAnFormController(view_du_an)  # Liên kết controller với view
        view_du_an.controller = controller_du_an
        self.current_frame = view_du_an
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_tinh_luong(self):
        """
        Hiển thị giao diện tính lương.
        - Đầu ra: Hiển thị giao diện tính lương và liên kết với controller tính lương.
        """
        view_tinh_luong = ViewTinhLuong(self.root, None)
        controller_tinh_luong = ControllerTinhLuong(view_tinh_luong)
        view_tinh_luong.controller = controller_tinh_luong
        self.current_frame = view_tinh_luong
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_bao_cao_nhan_su(self):
        """
        Hiển thị giao diện báo cáo nhân sự.

        - Đầu vào: Không có.
        - Đầu ra: Hiển thị giao diện báo cáo nhân sự với các biểu đồ liên quan.
        """
        if self.current_frame:
            self.current_frame.destroy()

        if not hasattr(self, "_bao_cao_controller"):
            self._bao_cao_controller = ControllerBaoCaoNhanSu(self.root)

        self.current_frame = self._bao_cao_controller.view
        self.current_frame.pack(fill=tk.BOTH, expand=True)


def ham_chinh(vai_tro):
    """
    Chạy ứng dụng chính sau khi đăng nhập thành công.

    - Đầu vào:
        + vai_tro: Vai trò của người dùng sau khi đăng nhập.
    - Đầu ra: Khởi chạy giao diện chính của ứng dụng.
    """
    root = tk.Tk()  # Tạo cửa sổ chính
    app = MainApp(root, vai_tro)  # Khởi tạo ứng dụng chính
    root.mainloop()

if __name__ == "__main__":
    """
        Khởi chạy ứng dụng với giao diện đăng nhập.
        """
    root = tk.Tk()
    controller_dangnhap = controller_dang_nhap()

    def khi_dang_nhap_thanh_cong(vai_tro):
        """
        Chuyển sang giao diện chính sau khi đăng nhập thành công.

        - Đầu vào:
            + vai_tro: Vai trò của người dùng (vd: Quản trị, Nhân viên, v.v.).
        - Đầu ra: Đóng giao diện đăng nhập và khởi chạy giao diện chính.
        """
        root.destroy()  # Đóng cửa sổ đăng nhập
        ham_chinh(vai_tro)

    def xu_ly_dang_nhap():
        """
        Xử lý đăng nhập khi người dùng nhấn nút đăng nhập.
        - Đầu vào: Không có.
        - Đầu ra:
            + Nếu đăng nhập thành công, chuyển đến giao diện chính.
            + Nếu đăng nhập thất bại, hiển thị thông báo lỗi.
        """
        ten_dang_nhap = login_view.ten_dang_nhap.get()
        mat_khau = login_view.mat_khau.get()
        vai_tro = controller_dangnhap.xac_dinh_vai_tro(ten_dang_nhap, mat_khau)
        if vai_tro:
            khi_dang_nhap_thanh_cong(vai_tro)
        else:
            messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng.")

    login_view = View_dang_nhap(root, controller_dangnhap, khi_dang_nhap_thanh_cong)
    root.mainloop()

