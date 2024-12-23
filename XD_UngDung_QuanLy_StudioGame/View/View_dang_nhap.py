import tkinter as tk
from tkinter import messagebox
from tkinter import font

class View_dang_nhap:
    def __init__(self, root, controller):
        """Thiết lập giao diện đăng nhập"""
        self.controller = controller
        self.root = root
        self.root.title("HỆ THỐNG QUẢN LÝ DỰ ÁN STUDIO - Đăng Nhập")

        # Đặt kích thước giao diện và căn giữa màn hình
        window_width = 500
        window_height = 300
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.root.configure(bg="#f0f0f0")  # màu nền

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

        # Khung dành Đăng nhập
        button_frame = tk.Frame(frame, bg="#f0f0f0")
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)

        # Nút Đăng nhập
        btn_dang_nhap = tk.Button(button_frame, text="Đăng nhập", command=self.dang_nhap)
        btn_dang_nhap.grid(row=2, column=0, pady=10, padx=(0, 5), sticky="e")


        # Quên mật khẩu
        lbl_quen_mat_khau = tk.Label(frame, text="Quên mật khẩu?", fg="blue", cursor="hand2", bg="#f0f0f0")
        lbl_quen_mat_khau.grid(row=2, column=1, padx=(70, 0))
        lbl_quen_mat_khau.bind("<Button-1>", self.quen_mat_khau)

        # Đăng ký
        underline_font = font.Font(underline=True)
        lbl_dang_ky = tk.Label(frame, text="Đăng ký", fg="blue", cursor="hand2", bg="#f0f0f0", font=underline_font)
        lbl_dang_ky.grid(row=3, column=3, columnspan=2, pady=70,padx=(50, 0))
        lbl_dang_ky.bind("<Button-1>", self.dang_ky)

    def dang_nhap(self):
        """Hàm xử lý khi nhấn nút Đăng nhập"""
        ten_dn = self.ten_dang_nhap.get()
        mat_khau = self.mat_khau.get()
        if self.controller.xu_ly_dang_nhap(ten_dn, mat_khau):
            messagebox.showinfo("Thành công", "Đăng nhập thành công!")
        else:
            messagebox.showerror("Thất bại", "Tên đăng nhập hoặc mật khẩu không đúng!")

    def dang_ky(self, event=None):
        """Hàm xử lý khi nhấn vào Đăng ký"""
        messagebox.showinfo("Đăng ký", "Chức năng đăng ký đang được phát triển!")

    def quen_mat_khau(self, event=None):
        """Hàm xử lý khi nhấn vào Quên mật khẩu"""
        messagebox.showinfo("Quên mật khẩu", "Chức năng quên mật khẩu đang được phát triển!")
