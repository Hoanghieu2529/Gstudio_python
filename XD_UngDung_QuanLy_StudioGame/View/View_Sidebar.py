import tkinter as tk


class Sidebar(tk.Frame):
    def __init__(self, master, show_form_callback):
        super().__init__(master, bg="#2C2C2E", width=200, height=600)
        self.pack(side=tk.LEFT, fill=tk.Y)

        options = [
            "Dashboard", "Người dùng", "Studio", "Phòng ban",
            "Nhân viên", "Dự án", "Công việc", "Bảng thời gian"]

        # Tạo các nút với style giống Apple
        for option in options:
            btn = tk.Button(
                self,
                text=option,
                bg="#1C1C1E",  # Màu nền tối
                fg="white",  # Màu chữ sáng
                bd=0,
                pady=12,
                padx=10,
                font=("San Francisco", 14),  # Phông chữ giống Apple
                activebackground="#007AFF",  # Màu khi nhấn (blue như iOS)
                activeforeground="white",
                highlightthickness=0,  # Tắt đường viền khi chọn
                relief="flat",  # Tạo cảm giác mượt mà
                command=lambda opt=option: show_form_callback(opt))

            # Tạo hiệu ứng hover (khi rê chuột qua)
            btn.bind("<Enter>", lambda event, button=btn: button.config(bg="#3A3A3C"))
            btn.bind("<Leave>", lambda event, button=btn: button.config(bg="#1C1C1E"))

            btn.pack(fill=tk.X, padx=5, pady=5)


