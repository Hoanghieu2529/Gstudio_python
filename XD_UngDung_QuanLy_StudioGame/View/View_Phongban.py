import tkinter as tk
from tkinter import ttk, messagebox

from View.View_BaseForm import KhungCoSo
from controllers.controller_PhongBan import PhongBanFormController

class PhongBanForm(KhungCoSo):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.frame = tk.Frame(master, bg="#f8f9fa")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Tiêu đề
        tk.Label(self.frame, text="Quản lý Phòng Ban", font=("Arial", 16), bg="#f8f9fa").pack(pady=10)

        # Bảng hiển thị danh sách phòng ban
        self.tree_phongban = ttk.Treeview(
            self.frame,
            columns=("stt", "ma_phong_ban", "ten_phong_ban", "mo_ta"),
            show="headings",
        )
        self.tree_phongban.heading("stt", text="STT")
        self.tree_phongban.heading("ma_phong_ban", text="Mã Phòng Ban")
        self.tree_phongban.heading("ten_phong_ban", text="Tên Phòng Ban")
        self.tree_phongban.heading("mo_ta", text="Mô Tả")
        self.tree_phongban.column("stt", width=50, anchor="center")
        self.tree_phongban.column("ma_phong_ban", width=100, anchor="center")
        self.tree_phongban.column("ten_phong_ban", width=200)
        self.tree_phongban.column("mo_ta", width=300)
        self.tree_phongban.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Thanh cuộn
        v_scroll = ttk.Scrollbar(self.frame, orient="vertical", command=self.tree_phongban.yview)
        self.tree_phongban.configure(yscrollcommand=v_scroll.set)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Tạo controller
        self.controller = PhongBanFormController(self)

        # Các nút chức năng
        self.tao_thanh_cong_cu()

        # Tải dữ liệu ban đầu
        self.controller.tai_dl()

    def tao_thanh_cong_cu(self):
        """Tạo thanh công cụ các nút chức năng"""
        toolbar = tk.Frame(self.frame, bg="#f8f9fa")
        toolbar.pack(fill=tk.X, pady=10)

        # Các nút chức năng
        btn_create = tk.Button(
            toolbar, text="Thêm mới", command=self.controller.tao_pb_moi, bg="#007bff", fg="white"
        )
        btn_read = tk.Button(
            toolbar, text="Đọc", command=self.controller.doc_pb, bg="#007bff", fg="white"
        )
        btn_update = tk.Button(
            toolbar, text="Cập nhật", command=self.controller.cap_nhat_pb, bg="#007bff", fg="white"
        )
        btn_delete = tk.Button(
            toolbar, text="Xóa", command=self.controller.xoa_pb, bg="#dc3545", fg="white"
        )
        btn_reload = tk.Button(
            toolbar, text="Tải lại", command=self.controller.tai_dl, bg="#28a745", fg="white"
        )

        # Sắp xếp các nút
        btn_create.pack(side=tk.LEFT, padx=5, pady=5)
        btn_read.pack(side=tk.LEFT, padx=5, pady=5)
        btn_update.pack(side=tk.LEFT, padx=5, pady=5)
        btn_delete.pack(side=tk.LEFT, padx=5, pady=5)
        btn_reload.pack(side=tk.LEFT, padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Phòng Ban")
    root.geometry("800x600")
    app = PhongBanForm(root)
    root.mainloop()
