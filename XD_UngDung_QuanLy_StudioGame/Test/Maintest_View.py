from View import Sidebar, NguoiDungForm, StudioForm, DuAnForm, Nhan_vien_form, PhongBanForm, CongViecForm

import tkinter as tk


# Import các form khác

class AdminDashboard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Admin Dashboard")
        self.geometry("800x600")
        self.configure(bg="#f8f9fa")

        self.sidebar = Sidebar(self, self.show_form)
        self.main_content = tk.Frame(self, bg="#f8f9fa", width=600, height=600)
        self.main_content.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        self.label = tk.Label(self.main_content, text="Chào bạn", bg="#f8f9fa", font=("SF Pro Display", 24))
        self.label.pack(pady=20)

    def show_form(self, option):
        for widget in self.main_content.winfo_children():
            widget.destroy()

        self.label = tk.Label(self.main_content, text=option, bg="#f8f9fa", font=("SF Pro Display", 24))
        self.label.pack(pady=20)

        if option == "Người dùng":
            NguoiDungForm(self.main_content)
        elif option == "Studio":
            StudioForm(self.main_content)
        elif option == "Phòng ban":
            PhongBanForm(self.main_content)
        elif option == "Dự án":
            DuAnForm(self.main_content)
        elif option == "Nhân viên":
            Nhan_vien_form(self.main_content)
        elif option == "Công việc":
            CongViecForm(self.main_content)
        # Thêm các form khác tương tự

if __name__ == "__main__":
    app = AdminDashboard()
    app.mainloop()
