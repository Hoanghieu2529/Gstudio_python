import tkinter as tk
from tkinter import PhotoImage, messagebox, font, Toplevel
from controllers.controller_dang_ky import controller_dang_ky
from View.View_dang_ky import View_dang_ky
from models.database import Database


class View_dang_nhap:
    def __init__(self, root, controller_dangnhap, on_login_success=None):
        """Thiết lập giao diện đăng nhập"""
        self.controller = controller_dangnhap
        self.on_login_success = on_login_success
        self.root = root
        self.root.title("HỆ THỐNG QUẢN LÝ DỰ ÁN STUDIO - Đăng Nhập")

        # Đặt kích thước giao diện và căn giữa màn hình
        window_width, window_height = 500, 300
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.root.configure(bg="#f0f0f0")  # màu nền

        try:
            logo = PhotoImage(file="Images/Logo_studio.png")
            self.root.iconphoto(False, logo)
        except Exception as e:
            print(f"Lỗi khi tải logo: {e}")

        # Sử dụng Frame để quản lý
        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)

        # Các thành phần trong giao diện
        tk.Label(frame, text="Tên đăng nhập:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(frame, text="Mật khẩu:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.ten_dang_nhap = tk.Entry(frame, width=30)
        self.mat_khau = tk.Entry(frame, show="*", width=30)
        self.ten_dang_nhap.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.mat_khau.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Checkbox ghi nhớ tài khoản
        self.remember_var = tk.BooleanVar()
        self.chk_remember = tk.Checkbutton(frame, text="Ghi nhớ thông tin", variable=self.remember_var, bg="#f0f0f0")
        self.chk_remember.grid(row=2, column=1, sticky="w", padx=10, pady=5)

        # Khung dành cho Đăng nhập và Quên mật khẩu
        button_frame = tk.Frame(frame, bg="#f0f0f0")
        button_frame.grid(row=3, column=0, columnspan=2, pady=20)

        # Nút Đăng nhập
        btn_dang_nhap = tk.Button(button_frame, text="Đăng nhập", command=self.dang_nhap)
        btn_dang_nhap.grid(row=0, column=0, padx=(0, 5))

        # Quên mật khẩu
        lbl_quen_mat_khau = tk.Label(
            button_frame, text="Quên mật khẩu?", fg="blue", cursor="hand2", bg="#f0f0f0"
        )
        lbl_quen_mat_khau.grid(row=0, column=1, padx=(10, 0))
        lbl_quen_mat_khau.bind("<Button-1>", self.quen_mat_khau)

        # Đăng ký
        underline_font = font.Font(underline=True)
        lbl_dang_ky = tk.Label(
            frame, text="Đăng ký", fg="blue", cursor="hand2", bg="#f0f0f0", font=underline_font
        )
        lbl_dang_ky.grid(row=4, column=0, columnspan=2, pady=20)
        lbl_dang_ky.bind("<Button-1>", self.dang_ky)

        # Tải thông tin tài khoản đã lưu
        self.load_login_info()

    # def dang_nhap(self):
    #     """Hàm xử lý khi nhấn nút Đăng nhập"""
    #     ten_dn = self.ten_dang_nhap.get()
    #     mat_khau = self.mat_khau.get()
    #
    #     if self.controller.xu_ly_dang_nhap(ten_dn, mat_khau):
    #         self.update_remember_account(ten_dn)
    #         if self.on_login_success:
    #             self.on_login_success()  # Gọi callback chuyển sang giao diện chính
    #         self.root.destroy()
    #     else:
    #         messagebox.showerror("Thất bại!", "Tên đăng nhập hoặc mật khẩu không đúng!")
    def dang_nhap(self):
        """Hàm xử lý khi nhấn nút Đăng nhập"""
        ten_dn = self.ten_dang_nhap.get()
        mat_khau = self.mat_khau.get()
        if self.controller.xu_ly_dang_nhap(ten_dn, mat_khau):
            if self.remember_var.get():
                self.save_login_info_to_db(ten_dn, mat_khau)
            else:
                self.clear_login_info_from_db(ten_dn)

            if self.on_login_success:
                self.on_login_success()  # Gọi callback chuyển sang giao diện chính
            self.root.destroy()
        else:
            messagebox.showerror("Thất bại!", "Tên đăng nhập hoặc mật khẩu không đúng!")

    def load_login_info(self):
        """Tải thông tin đăng nhập từ cơ sở dữ liệu"""
        db = Database()
        try:
            query = "SELECT ten_dang_nhap, mat_khau FROM nguoi_dung WHERE ghi_nho = 1 LIMIT 1"
            result = db.fetch_one(query)
            if result:
                self.ten_dang_nhap.insert(0, result['ten_dang_nhap'])
                self.mat_khau.insert(0, result['mat_khau'])
                self.remember_var.set(True)
        except Exception as e:
            print(f"Lỗi khi tải thông tin đăng nhập: {e}")
        finally:
            del db

    def save_login_info_to_db(self, ten_dn, mat_khau):
        """Lưu thông tin đăng nhập vào cơ sở dữ liệu"""
        db = Database()
        try:
            query = "UPDATE nguoi_dung SET ghi_nho = 1 WHERE ten_dang_nhap = %s AND mat_khau = %s"
            db.execute_query(query, (ten_dn, mat_khau))
        except Exception as e:
            print(f"Lỗi khi lưu thông tin đăng nhập: {e}")
        finally:
            del db

    def clear_login_info_from_db(self, ten_dn):
        """Xóa thông tin ghi nhớ đăng nhập trong cơ sở dữ liệu"""
        db = Database()
        try:
            query = "UPDATE nguoi_dung SET ghi_nho = 0 WHERE ten_dang_nhap = %s"
            db.execute_query(query, (ten_dn,))
        except Exception as e:
            print(f"Lỗi khi xóa thông tin ghi nhớ đăng nhập: {e}")
        finally:
            del db

    def dang_ky(self, event=None):
        """Hàm xử lý khi nhấn vào Đăng ký"""
        self.goi_dang_ky()

    def quen_mat_khau(self, event=None):
        """Hàm xử lý khi nhấn vào Quên mật khẩu"""
        messagebox.showinfo("Quên mật khẩu", "Chức năng quên mật khẩu đang được phát triển!")

    def goi_dang_ky(self):
        """Hiển thị cửa sổ đăng ký"""
        toplevel = Toplevel(self.root)  # Tạo cửa sổ mới
        controller = controller_dang_ky()
        View_dang_ky(toplevel, controller)
        toplevel.geometry("400x500")
