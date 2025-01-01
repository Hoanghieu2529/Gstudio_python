
from tkinter import ttk, messagebox
from models.models_phong_ban import PhongBanModel

class PhongBanFormController:
    def __init__(self, view):
        self.view = view
        self.model = PhongBanModel()  # Kết nối với model PhongBan

    def tao_pb_moi(self):
        """Thêm một phòng ban mới"""
        messagebox.showinfo("Thông báo", "Chức năng thêm phòng ban đang được phát triển.")

    def doc_pb(self):
        """Xem chi tiết một phòng ban"""
        selected_item = self.view.tree_phongban.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một phòng ban để xem chi tiết")
            return
        item = self.view.tree_phongban.item(selected_item)
        values = item["values"]
        messagebox.showinfo("Thông tin phòng ban",
                            f"Mã phòng ban: {values[1]}\n"
                            f"Tên phòng ban: {values[2]}\n"
                            f"Mô tả: {values[3]}")

    def cap_nhat_pb(self):
        """Cập nhật thông tin một phòng ban"""
        messagebox.showinfo("Thông báo", "Chức năng cập nhật phòng ban đang được phát triển.")

    def xoa_pb(self):
        """Xóa một phòng ban"""
        selected_item = self.view.tree_phongban.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một phòng ban để xóa")
            return
        confirm = messagebox.askyesno("Xác nhận", "Bạn thật sự muốn xóa phòng ban này không?")
        if confirm:
            self.view.tree_phongban.delete(selected_item)

    def tai_dl(self):
        """Tải dữ liệu từ CSDL và hiển thị trong Treeview"""
        self.view.tree_phongban.delete(*self.view.tree_phongban.get_children())  # Xóa dữ liệu cũ
        danh_sach_phong_ban = self.model.lay_danh_sach_phong_ban()  # Lấy dữ liệu từ model
        for idx, phong_ban in enumerate(danh_sach_phong_ban, start=1):
            self.view.tree_phongban.insert("", "end", values=(idx, phong_ban['mapb'], phong_ban['ten_phong_ban'], phong_ban['mo_ta']))
