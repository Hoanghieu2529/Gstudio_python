
from tkinter import ttk, messagebox
from models.models_phong_ban import PhongBanModel

class PhongBanFormController:
    """
    Lớp điều khiển quản lý phòng ban, chịu trách nhiệm:
    - Tương tác với model `PhongBanModel` để xử lý dữ liệu.
    - Tương tác với view để hiển thị thông tin phòng ban.
    """
    def __init__(self, view):
        """
        Khởi tạo lớp điều khiển phòng ban.

        - Đầu vào:
            + view: Đối tượng giao diện (View) để hiển thị dữ liệu phòng ban.
        - Đầu ra:
            + Tạo kết nối với model `PhongBanModel`.
        """
        self.view = view
        self.model = PhongBanModel()  # Kết nối với model PhongBan

    def tao_pb_moi(self):
        """
        Thêm một phòng ban mới.
        - Đầu ra:
            + Hiển thị thông báo về trạng thái phát triển của chức năng này.
        """
        messagebox.showinfo("Thông báo", "Chức năng thêm phòng ban đang được phát triển.")

    def doc_pb(self):
        """
        Xem chi tiết thông tin một phòng ban.
        - Đầu ra:
            + Hiển thị hộp thoại thông tin chi tiết của phòng ban được chọn.
            + Nếu không có phòng ban nào được chọn, hiển thị cảnh báo.
        """
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
        """
        Cập nhật thông tin một phòng ban.
        - Đầu ra:
            + Hiển thị thông báo về trạng thái phát triển của chức năng này.
        """
        messagebox.showinfo("Thông báo", "Chức năng cập nhật phòng ban đang được phát triển.")

    def xoa_pb(self):
        """
        Xóa một phòng ban.
        - Đầu ra:
            + Xóa phòng ban được chọn khỏi giao diện `Treeview`.
            + Hiển thị cảnh báo nếu không có phòng ban nào được chọn.
            + Yêu cầu xác nhận từ người dùng trước khi xóa.
        """
        selected_item = self.view.tree_phongban.selection()
        if not selected_item:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một phòng ban để xóa")
            return
        confirm = messagebox.askyesno("Xác nhận", "Bạn thật sự muốn xóa phòng ban này không?")
        if confirm:
            self.view.tree_phongban.delete(selected_item)

    def tai_dl(self):
        """
        Tải dữ liệu phòng ban từ cơ sở dữ liệu và hiển thị trong giao diện `Treeview`.
        - Đầu ra:
            + Xóa dữ liệu cũ trong `Treeview`.
            + Lấy danh sách phòng ban từ model và hiển thị từng phòng ban vào `Treeview`.
            + Mỗi phòng ban bao gồm:
                * Số thứ tự
                * Mã phòng ban
                * Tên phòng ban
                * Mô tả
        """
        self.view.tree_phongban.delete(*self.view.tree_phongban.get_children())  # Xóa dữ liệu cũ
        danh_sach_phong_ban = self.model.lay_danh_sach_phong_ban()  # Lấy dữ liệu từ model
        for idx, phong_ban in enumerate(danh_sach_phong_ban, start=1):
            self.view.tree_phongban.insert("", "end", values=(idx, phong_ban['mapb'], phong_ban['ten_phong_ban'], phong_ban['mo_ta']))
