import tkinter as tk

class Sidebar(tk.Frame):
    def __init__(self, master, show_form_callback):
        super().__init__(master, bg="Gray", width=200, height=600)
        self.pack(side=tk.LEFT, fill=tk.Y)

        self.show_form_callback = show_form_callback
        self.selected_button = None  # Nút hiện tại đang được chọn

        options = ["Dashboard", "Người dùng", "Studio", "Phòng ban", "Nhân viên", "Dự án", "Công việc", "Bảng thời gian"]
        self.buttons = {}  # Lưu trữ các nút để thay đổi màu sắc

        for option in options:
            btn = tk.Button(self, text=option, bg="Gray", fg="white", bd=0, pady=10, font=("SF Pro Display", 13),
                            command=lambda opt=option: self.select_option(opt))
            btn.pack(fill=tk.X)
            self.buttons[option] = btn  # Thêm nút vào dictionary

    def select_option(self, option):
        """Thay đổi màu nút khi được chọn"""
        # Reset màu tất cả các nút
        for btn in self.buttons.values():
            btn.config(bg="Gray", fg="white")

        # Đổi màu nút được chọn
        selected_btn = self.buttons[option]
        selected_btn.config(bg="#007bff", fg="white")  # Màu xanh dương nổi bật

        # Lưu trạng thái nút được chọn
        self.selected_button = selected_btn

        # Gọi callback để hiển thị form tương ứng
        self.show_form_callback(option)
