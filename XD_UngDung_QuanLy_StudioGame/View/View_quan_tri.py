import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class ViewQuanTri(tk.Frame):
    """
    Lớp giao diện chính cho chức năng quản trị trong ứng dụng.

    Bao gồm:
    - Hiển thị danh sách người dùng.
    - Hiển thị biểu đồ lương theo phòng ban.
    - Hiển thị tổng quan trạng thái dự án.
    - Hiển thị tiến độ các dự án.
    """
    def __init__(self, master, controller):
        """Khởi tạo frame ViewQuanTri.
       Args:
           master (tk.Tk/ tk.Frame): Cửa sổ hoặc frame cha.
           controller (object): Controller để xử lý logic nghiệp vụ và giao tiếp với mô hình (model).
        """
        super().__init__(master)
        self.controller = controller
        self.pack(fill=tk.BOTH, expand=True)
        self.tao_giao_dien()

    def tao_giao_dien(self):
        """
        Tạo giao diện chính gồm:
        - Nút điều hướng trong khung trái.
        - Khung hiển thị nội dung bên phải.
        """
        tk.Label(self, text="Quản lý Quản trị", font=("San Francisco", 16), bg="#f8f9fa").pack(pady=10)
        self.left_frame = tk.Frame(self, bg="#f8f9fa", width=300)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.right_frame = tk.Frame(self, bg="#ffffff")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        buttons = [
            ("Danh sách người dùng", self._goi_ham_controller("hien_thi_danh_sach_nguoi_dung")),
            ("Tổng lương theo phòng ban", self._goi_ham_controller("hien_thi_bieu_do_luong")),
            ("Tổng quan dự án", self._goi_ham_controller("hien_thi_bieu_do_du_an")),
            ("Tiến độ dự án", self._goi_ham_controller("hien_thi_tien_do_du_an")),
        ]

        for text, command in buttons:
            tk.Button(self.left_frame, text=text, command=command).pack(fill=tk.X, pady=5)

    def _goi_ham_controller(self, ten_ham):
        """
        Trả về hàm gọi từ controller nếu tồn tại, nếu không thì trả về hàm rỗng.
        - Đầu vào:
            + ten_ham (str): Tên hàm trong controller cần gọi.
        - Đầu ra:
            + Hàm gọi thực tế từ controller nếu tồn tại.
            + Nếu không tồn tại, in thông báo lỗi.
        """
        def _wrapper():
            if self.controller and hasattr(self.controller, ten_ham):
                try:
                    getattr(self.controller, ten_ham)()
                except Exception as e:
                    print(f"Lỗi khi gọi {ten_ham}: {e}")
            else:
                print(f"Hàm {ten_ham} không tồn tại trong controller")
        return _wrapper

    def hien_thi_danh_sach_nguoi_dung(self, data):
        """
        Hiển thị danh sách người dùng trong bảng từ cơ sở dữ liệu.
        - Đầu vào:
            + data (list): Danh sách người dùng, mỗi phần tử là một từ điển chứa:
                * Mã người dùng
                * Tên đăng nhập
                * Vai trò
                * Email
                * Ngày đăng ký
        - Đầu ra:
            + Hiển thị danh sách người dùng trong Treeview.
        """
        self._xoa_bieu_do()
        self._hien_label_title("Danh sách người dùng")

        # Tạo Treeview nếu chưa tồn tại
        if not hasattr(self, "treeview"):
            self.treeview = ttk.Treeview(
                self.right_frame,
                columns=("Mã người dùng", "Tên đăng nhập", "Vai trò", "Email", "Ngày đăng ký"),
                show="headings"
            )
            for col in ("Mã người dùng", "Tên đăng nhập", "Vai trò", "Email", "Ngày đăng ký"):
                self.treeview.heading(col, text=col)
                self.treeview.column(col, width=120, anchor="center")
            self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Xóa dữ liệu cũ trong Treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Thêm dữ liệu mới vào Treeview
        for row in data:
            self.treeview.insert("", "end", values=(
                row["mand"], row["ten_dang_nhap"], row["vai_tro"], row["email"], row["ngay_dang_ky"]
            ))

    def _hien_label_title(self, title):
        """Hiển thị tiêu đề phía trên bảng hoặc biểu đồ"""
        tk.Label(self.right_frame, text=title, font=("San Francisco", 14), bg="#ffffff").pack(pady=5)

    def hien_thi_bieu_do_luong(self, data):
        """
        Hiển thị biểu đồ tổng lương theo phòng ban.

        - Đầu vào:
            + data (list): Dữ liệu lương theo phòng ban, mỗi phần tử là một từ điển chứa:
                * Tên phòng ban
                * Tổng lương
        - Đầu ra:
            + Hiển thị biểu đồ tròn về tổng lương trên giao diện.
        """
        self._xoa_bieu_do()
        labels = [row["ten_phong_ban"] for row in data]
        values = [row["tong_luong"] for row in data]

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
        ax.set_title("Tổng lương theo phòng ban")

        self._hien_bieu_do(fig)

    def hien_thi_bieu_do_du_an(self, data):
        """"
        Hiển thị biểu đồ tổng quan dự án.
        - Đầu vào:
            + data (list): Dữ liệu tổng quan dự án, mỗi phần tử là một từ điển chứa:
                * Trạng thái
                * Số lượng dự án
        - Đầu ra:
            + Hiển thị biểu đồ cột về trạng thái dự án trên giao diện.
        """
        self._xoa_bieu_do()
        labels = [row["trang_thai"] for row in data]
        values = [row["so_luong"] for row in data]

        fig, ax = plt.subplots()
        ax.bar(labels, values, color="skyblue")
        ax.set_title("Tổng quan dự án")
        ax.set_ylabel("Số lượng dự án")

        self._hien_bieu_do(fig)

    def hien_thi_tien_do_du_an(self, data):
        """
        Hiển thị tiến độ các dự án.
        - Đầu vào:
            + data (list): Dữ liệu tiến độ dự án, mỗi phần tử là một từ điển chứa:
                * Tên dự án
                * Ngày bắt đầu
                * Ngày kết thúc
        - Đầu ra:
            + Hiển thị biểu đồ đường về tiến độ dự án trên giao diện.
        """
        self._xoa_bieu_do()
        fig, ax = plt.subplots()

        for row in data:
            ax.plot([row["ngay_bat_dau"], row["ngay_ket_thuc"]], [row["ten_du_an"], row["ten_du_an"]], marker="o")

        ax.set_title("Tiến độ các dự án")
        ax.set_xlabel("Thời gian")
        ax.set_ylabel("Tên dự án")

        self._hien_bieu_do(fig)

    def _hien_bieu_do(self, fig):
        """"
        Hiển thị biểu đồ trong khung bên phải.

        - Đầu vào:
            + fig: Đối tượng `Figure` của Matplotlib.
        - Đầu ra:
            + Hiển thị biểu đồ trong giao diện.
        """
        canvas = FigureCanvasTkAgg(fig, self.right_frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        canvas.draw()

    def _xoa_bieu_do(self):
        """
        Xóa nội dung hiển thị trong khung bên phải.

        - Đầu vào: Không có.
        - Đầu ra:
            + Loại bỏ tất cả các widget hiện tại trong khung bên phải.
        """
        for widget in self.right_frame.winfo_children():
            widget.destroy()

    def cap_nhat_danh_sach_nguoi_dung(self, du_lieu):
        """
        Cập nhật danh sách người dùng trên giao diện.

        - Đầu vào:
            + du_lieu (list): Danh sách người dùng, mỗi phần tử là một từ điển chứa:
                * Mã người dùng (`mand`)
                * Tên đăng nhập (`ten_dang_nhap`)
                * Vai trò (`vai_tro`)
                * Email (`email`)
                * Ngày đăng ký (`ngay_dang_ky`)
        - Đầu ra:
            + In danh sách người dùng ra console để kiểm tra (tạm thời sử dụng cho mục đích debug).
            + Hiển thị dữ liệu lên giao diện (phần triển khai cần bổ sung nếu chưa hoàn chỉnh).
        """
        print("Cập nhật danh sách người dùng:", du_lieu)

    def _hien_label_title(self, param):
        """
        Hiển thị tiêu đề cho bảng hoặc biểu đồ trên giao diện.
        - Đầu vào:
            + param (str): Tiêu đề cần hiển thị.
        - Đầu ra:
            + Hiển thị một tiêu đề trên khung bên phải của giao diện (phần triển khai cần bổ sung nếu chưa hoàn chỉnh).
        - Lưu ý:
            + Phương thức hiện tại chưa được triển khai đầy đủ, cần bổ sung logic hiển thị.
        """
        pass

