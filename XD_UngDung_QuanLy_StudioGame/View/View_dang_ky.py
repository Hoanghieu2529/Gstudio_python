import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import font
from controllers.controller_dang_ky import controller_dang_ky

class View_dang_ky:
    def __init__(self, root, controller):
        """Giao diện đăng ký"""
        self.controller = controller
        self.root = root
        self.root.title("Đăng Ký Tài Khoản")
        self.root.configure(bg="#f0f0f0")

        # Đặt kích thước giao diện và căn giữa màn hình
        window_width = 400
        window_height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        logo = PhotoImage(file="Images/Logo_studio.png")  # Đường dẫn tới logo
        self.root.iconphoto(False, logo)

        # Các thành phần giao diện
        tk.Label(root, text="Tên đăng nhập:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(root, text="Mật khẩu:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        tk.Label(root, text="Xác nhận mật khẩu:", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        tk.Label(root, text="Email:", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.ten_dang_nhap = tk.Entry(root, width=25)
        self.mat_khau = tk.Entry(root, show="*", width=25)
        self.xac_nhan_mat_khau = tk.Entry(root, show="*", width=25)
        self.email = tk.Entry(root, width=25)

        self.ten_dang_nhap.grid(row=0, column=1, padx=10, pady=10)
        self.mat_khau.grid(row=1, column=1, padx=10, pady=10)
        self.xac_nhan_mat_khau.grid(row=2, column=1, padx=10, pady=10)
        self.email.grid(row=3, column=1, padx=10, pady=10)

        self.otp_label = tk.Label(root, text="Nhập mã OTP:", bg="#f0f0f0")
        self.otp_entry = tk.Entry(root, width=25)

        tk.Button(root, text="Gửi OTP", command=self.gui_otp).grid(row=4, column=1, pady=10)
        tk.Button(root, text="Hoàn tất Đăng Ký", command=self.dang_ky).grid(row=6, column=1, pady=10)

    def gui_otp(self):
        """Xử lý gửi OTP"""
        email = self.email.get()
        if not email:
            messagebox.showerror("Lỗi", "Vui lòng nhập email trước khi gửi OTP!")
            return

        self.otp = self.controller.gui_otp_gui(email)  # Gửi OTP thông qua controller
        if self.otp:
            messagebox.showinfo("Thành công", "OTP đã được gửi đến email của bạn.")
            self.otp_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")
            self.otp_entry.grid(row=5, column=1, padx=10, pady=10)
        else:
            messagebox.showerror("Lỗi", "Không thể gửi OTP. Vui lòng thử lại sau.")

    def dang_ky(self):
        """Xử lý sau khi nhấn nút đăng ký"""
        ten_dang_nhap = self.ten_dang_nhap.get()
        mat_khau = self.mat_khau.get()
        xac_nhan_mat_khau = self.xac_nhan_mat_khau.get()
        email = self.email.get()
        otp_nhap = self.otp_entry.get()

        if not ten_dang_nhap or not mat_khau or not xac_nhan_mat_khau or not email or not otp_nhap:
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
            return

        if mat_khau != xac_nhan_mat_khau:
            messagebox.showerror("Lỗi", "Mật khẩu xác nhận không khớp!")
            return

        if otp_nhap != self.otp:
            messagebox.showerror("Lỗi", "Mã OTP không chính xác!")
            return

        if self.controller.xu_ly_dang_ky(ten_dang_nhap, mat_khau, email):
            messagebox.showinfo("Thành công", "Đăng ký thành công!")
            self.root.destroy()  # Đóng cửa sổ đăng ký
        else:
            messagebox.showerror("Lỗi", "Đăng ký thất bại! Tên đăng nhập hoặc email đã tồn tại.")
