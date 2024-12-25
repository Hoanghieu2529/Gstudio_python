import tkinter as tk

class Sidebar(tk.Frame):
    def __init__(self, master, show_form_callback):
        super().__init__(master, bg="Gray", width=200, height=600)
        self.pack(side=tk.LEFT, fill=tk.Y)

        options = ["Dashboard", "Người dùng", "Studio", "Phòng ban", "Nhân viên", "Dự án", "Công việc", "Bảng thời gian"]
        for option in options:
            btn = tk.Button(self, text=option, bg="Gray", fg="white", bd=0, pady=10, font=("SF Pro Display", 13),
                            command=lambda opt=option: show_form_callback(opt))
            btn.pack(fill=tk.X)
