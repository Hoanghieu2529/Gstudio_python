import tkinter as tk

class Sidebar(tk.Frame):
    def __init__(self, master, show_form_callback):
        super().__init__(master, bg="#2C2C2E", width=200, height=600)
        self.pack(side=tk.LEFT, fill=tk.Y, padx=0)

        self.buttons = {}  # Lưu trữ các nút để dễ dàng thay đổi màu sắc
        self.submenu_frames = {}  # Lưu trữ frame cho từng submenu
        self.selected_button = None  # Theo dõi nút được chọn hiện tại

        # Cấu trúc các menu chính và phụ
        menu_structure = {
            "Điều hành": ["Quản trị", "Studio - Báo cáo", "Phòng ban"],
            "Nhân sự": ["Nhân viên", "Bảng công", "Tính lương", "BHXH"],
            "Công việc": ["Dự án", "Báo cáo tiến độ"],
            "Tài chính": ["Chi phí", "Doanh thu", "Báo cáo tổng hợp"]
        }

        for main_menu, sub_menus in menu_structure.items():
            # Thêm menu chính
            main_btn = tk.Button(
                self,
                text=main_menu,
                bg="#1C1C1E",  # Màu nền tối
                fg="white",  # Màu chữ sáng
                bd=0,
                pady=12,
                padx=10,
                anchor="w",  # Căn text sát lề trái
                font=("San Francisco", 14, "bold"),  # Font in đậm cho menu chính
                activebackground="#007AFF",  # Màu khi nhấn
                activeforeground="white",
                highlightthickness=0,  # Tắt đường viền khi chọn
                relief="flat",  # Tạo cảm giác mượt mà
                command=lambda opt=main_menu: self.toggle_submenu(opt)
            )
            main_btn.pack(fill=tk.X, padx=0, pady=5)
            self.buttons[main_menu] = main_btn

            # Frame chứa các menu con
            submenu_frame = tk.Frame(self, bg="#2C2C2E")
            submenu_frame.pack(fill=tk.X, padx=0, pady=0)
            submenu_frame.pack_forget()  # Ẩn submenu ban đầu
            self.submenu_frames[main_menu] = submenu_frame

            for sub_menu in sub_menus:
                sub_btn = tk.Button(
                    submenu_frame,
                    text=f"  {sub_menu}",  # Thụt lề để phân biệt
                    bg="#333333",  # Màu nhạt hơn cho submenu
                    fg="white",
                    bd=0,
                    pady=8,
                    padx=10,
                    anchor="w",  # Căn text sát lề trái
                    font=("San Francisco", 12),
                    activebackground="#007AFF",
                    activeforeground="white",
                    highlightthickness=0,
                    relief="flat",
                    command=lambda opt=sub_menu: self.select_option(opt, show_form_callback)
                )
                sub_btn.pack(fill=tk.X, padx=0, pady=2)
                self.buttons[sub_menu] = sub_btn

    def toggle_submenu(self, main_menu):
        """Hiển thị hoặc ẩn submenu khi bấm vào menu chính"""
        submenu_frame = self.submenu_frames[main_menu]
        if submenu_frame.winfo_ismapped():
            submenu_frame.pack_forget()  # Ẩn submenu
        else:
            # Tìm vị trí để hiển thị submenu ngay dưới nút chính
            for frame in self.submenu_frames.values():
                frame.pack_forget()
            submenu_frame.pack(after=self.buttons[main_menu])  # Hiển thị submenu ngay dưới nút chính

    def select_option(self, option, show_form_callback):
        """Thay đổi màu nút khi được chọn"""
        # Reset màu tất cả các nút
        for btn, original_color in self.buttons.items():
            if btn in self.submenu_frames:
                self.buttons[btn].config(bg="#1C1C1E", fg="white")
            else:
                self.buttons[btn].config(bg="#333333", fg="white")

        # Đổi màu nút được chọn
        selected_btn = self.buttons[option]
        selected_btn.config(bg="#007AFF", fg="white")  # Màu xanh iOS

        # Lưu trạng thái nút được chọn
        self.selected_button = selected_btn

        # Gọi callback để hiển thị form tương ứng
        show_form_callback(option)

# Test Sidebar Implementation
if __name__ == "__main__":
    def mock_callback(option):
        print(f"Selected: {option}")

    root = tk.Tk()
    root.geometry("200x600")
    sidebar = Sidebar(root, mock_callback)
    root.mainloop()

