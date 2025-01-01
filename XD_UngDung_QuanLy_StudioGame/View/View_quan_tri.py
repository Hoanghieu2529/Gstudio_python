import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class ViewQuanTri(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pack(fill=tk.BOTH, expand=True)
        self.tao_giao_dien()

    def tao_giao_dien(self):
        """Tạo giao diện chính gồm các nút điều hướng và khung hiển thị"""
        self.left_frame = tk.Frame(self, bg="#f8f9fa", width=300)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.right_frame = tk.Frame(self, bg="#ffffff")
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Các nút điều hướng
        buttons = [
            ("Danh sách người dùng", self._goi_ham_controller("hien_thi_danh_sach_nguoi_dung")),
            ("Lương theo phòng ban", self._goi_ham_controller("hien_thi_tong_luong_theo_phong_ban")),
            ("Tổng quan dự án", self._goi_ham_controller("hien_thi_tong_quan_du_an")),
            ("Tiến độ dự án", self._goi_ham_controller("hien_thi_tien_do_du_an")),
        ]

        for text, command in buttons:
            tk.Button(self.left_frame, text=text, command=command).pack(fill=tk.X, pady=5)

    def _goi_ham_controller(self, ten_ham):
        """Trả về hàm gọi từ controller nếu tồn tại, nếu không thì trả về hàm rỗng"""
        def _wrapper():
            if self.controller and hasattr(self.controller, ten_ham):
                try:
                    getattr(self.controller, ten_ham)()
                except Exception as e:
                    print(f"Lỗi khi gọi {ten_ham}: {e}")
            else:
                print(f"Hàm {ten_ham} không tồn tại trong controller")
        return _wrapper

    def hien_thi_danh_sach_nguoi_dung(self):
        """Hiển thị danh sách người dùng trong bảng từ CSDL"""
        self._hien_label_title("Danh sách người dùng")  # Thêm tiêu đề

        # Truy vấn dữ liệu từ CSDL
        try:
            query = "SELECT mand, ten_dang_nhap, vai_tro, email, ngay_dang_ky FROM nguoi_dung"
            data = self.controller.database.fetch_all(
                query)  # Giả sử controller có thuộc tính `database` để thao tác với CSDL
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi tải dữ liệu: {e}")
            return

        # Tạo Treeview
        tree = ttk.Treeview(self.right_frame, columns=("mand", "ten_dang_nhap", "vai_tro", "email", "ngay_dang_ky"),
                            show="headings")
        tree.heading("mand", text="ID")
        tree.heading("ten_dang_nhap", text="Tên đăng nhập")
        tree.heading("vai_tro", text="Vai trò")
        tree.heading("email", text="Email")
        tree.heading("ngay_dang_ky", text="Ngày đăng ký")
        tree.column("mand", width=50, anchor="center")
        tree.column("ten_dang_nhap", width=150, anchor="w")
        tree.column("vai_tro", width=120, anchor="w")
        tree.column("email", width=200, anchor="w")
        tree.column("ngay_dang_ky", width=100, anchor="center")
        tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Thêm dữ liệu vào Treeview
        for row in data:
            tree.insert("", "end",
                        values=(row["mand"], row["ten_dang_nhap"], row["vai_tro"], row["email"], row["ngay_dang_ky"]))

    def hien_thi_bieu_do_luong(self, data):
        """Hiển thị biểu đồ tổng lương theo phòng ban"""
        self._xoa_bieu_do()
        labels = [row["ten_phong_ban"] for row in data]
        values = [row["tong_luong"] for row in data]

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
        ax.set_title("Tổng lương theo phòng ban")

        self._hien_bieu_do(fig)

    def hien_thi_bieu_do_du_an(self, data):
        """Hiển thị biểu đồ tổng quan dự án"""
        self._xoa_bieu_do()
        labels = [row["trang_thai"] for row in data]
        values = [row["so_luong"] for row in data]

        fig, ax = plt.subplots()
        ax.bar(labels, values, color="skyblue")
        ax.set_title("Tổng quan dự án")
        ax.set_ylabel("Số lượng dự án")

        self._hien_bieu_do(fig)

    def hien_thi_tien_do_du_an(self, data):
        """Hiển thị tiến độ các dự án"""
        self._xoa_bieu_do()
        fig, ax = plt.subplots()

        for row in data:
            ax.plot([row["ngay_bat_dau"], row["ngay_ket_thuc"]], [row["ten_du_an"], row["ten_du_an"]], marker="o")

        ax.set_title("Tiến độ các dự án")
        ax.set_xlabel("Thời gian")
        ax.set_ylabel("Tên dự án")

        self._hien_bieu_do(fig)

    def _hien_bieu_do(self, fig):
        """Hiển thị biểu đồ trong khung bên phải"""
        canvas = FigureCanvasTkAgg(fig, self.right_frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        canvas.draw()

    def _xoa_bieu_do(self):
        """Xóa nội dung hiển thị trong khung bên phải"""
        for widget in self.right_frame.winfo_children():
            widget.destroy()

    def cap_nhat_danh_sach_nguoi_dung(self, du_lieu):
        """Cập nhật danh sách người dùng trên giao diện."""
        print("Cập nhật danh sách người dùng:", du_lieu)
