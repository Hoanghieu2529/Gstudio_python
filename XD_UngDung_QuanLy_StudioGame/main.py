import tkinter as tk
from View.View_dang_nhap import View_dang_nhap
from controllers.controller_dang_ky import controller_dang_ky
from controllers.controller_dang_nhap import controller_dang_nhap
from View.View_dang_ky import View_dang_ky


def goi_dang_ky():
    """Hàm gọi giao diện đăng ký"""
    root = tk.Toplevel()  # Tạo cửa sổ mới
    controller = controller_dang_ky()
    View_dang_ky(root, controller)
    root.mainloop()


def ham_chinh():
    """Khởi tạo cửa sổ chính và giao diện đăng nhập"""
    root = tk.Tk()  # Tạo cửa sổ chính
    controller_dangnhap = controller_dang_nhap()
    View_dang_nhap(root, controller_dangnhap)  # Khởi tạo giao diện đăng nhập
    root.mainloop()


if __name__ == "__main__":
    ham_chinh()
