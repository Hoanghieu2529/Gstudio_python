# import logging
# from tkinter import messagebox
# from models.model_quan_tri import ModelQuanTri
#
# class ControllerQuanTri:
#     def __init__(self, view, database):
#         """ view: Giao diện liên kết (ViewQuanTri).
#             database: Đối tượng kết nối cơ sở dữ liệu.
#         """
#         self.view = view
#         self.model = ModelQuanTri(database)
#         self.database = database  # Inject database để linh hoạt hơn trong xử lý dữ liệu
#         logging.basicConfig(level=logging.INFO)
#
#     def hien_thi_danh_sach_nguoi_dung(self):
#         """Hiển thị danh sách người dùng từ cơ sở dữ liệu trên giao diện"""
#         try:
#             data = self.model.lay_danh_sach_nguoi_dung()
#             if data:
#                 self.view.hien_thi_danh_sach_nguoi_dung(data)
#                 logging.info("Hiển thị danh sách người dùng thành công.")
#             else:
#                 messagebox.showinfo("Thông báo", "Không có dữ liệu người dùng để hiển thị.")
#         except Exception as e:
#             logging.error(f"Lỗi khi lấy dữ liệu người dùng: {e}")
#             messagebox.showerror("Lỗi", "Không thể hiển thị danh sách người dùng! Vui lòng thử lại sau.")
#
#     def hien_thi_tong_luong_theo_phong_ban(self):
#         """Hiển thị biểu đồ tổng lương theo từng phòng ban"""
#         try:
#             data = self.model.lay_tong_luong_theo_phong_ban()
#             if data:
#                 self.view.hien_thi_bieu_do_luong(data)
#                 logging.info("Hiển thị biểu đồ tổng lương theo phòng ban thành công.")
#             else:
#                 messagebox.showinfo("Thông báo", "Không có dữ liệu lương để hiển thị.")
#         except Exception as e:
#             logging.error(f"Lỗi khi lấy dữ liệu lương: {e}")
#             messagebox.showerror("Lỗi", "Không thể hiển thị tổng lương theo phòng ban! Vui lòng thử lại sau.")
#
#     def hien_thi_tong_quan_du_an(self):
#         """Hiển thị biểu đồ tổng quan các dự án"""
#         try:
#             data = self.model.lay_tong_quan_du_an()
#             if data:
#                 self.view.hien_thi_bieu_do_du_an(data)
#                 logging.info("Hiển thị tổng quan dự án thành công.")
#             else:
#                 messagebox.showinfo("Thông báo", "Không có dữ liệu dự án để hiển thị.")
#         except Exception as e:
#             logging.error(f"Lỗi khi lấy dữ liệu dự án: {e}")
#             messagebox.showerror("Lỗi", "Không thể hiển thị tổng quan dự án! Vui lòng thử lại sau.")
#
#     def hien_thi_tien_do_du_an(self):
#         """Hiển thị biểu đồ tiến độ các dự án"""
#         try:
#             data = self.model.lay_tien_do_du_an()
#             if data:
#                 self.view.hien_thi_tien_do_du_an(data)
#                 logging.info("Hiển thị tiến độ dự án thành công.")
#             else:
#                 messagebox.showinfo("Thông báo", "Không có dữ liệu tiến độ dự án để hiển thị.")
#         except Exception as e:
#             logging.error(f"Lỗi khi lấy tiến độ dự án: {e}")
#             messagebox.showerror("Lỗi", "Không thể hiển thị tiến độ dự án! Vui lòng thử lại sau.")

# from models.model_quan_tri import ModelQuanTri
#
# class ControllerQuanTri:
#     def __init__(self, view, database):
#         self.view = view
#         self.model = ModelQuanTri(database)
#
#     def hien_thi_danh_sach_nguoi_dung(self):
#         data = self.model.lay_danh_sach_nguoi_dung()
#         self.view.hien_thi_danh_sach_nguoi_dung(data)
#
#     def hien_thi_tong_luong_theo_phong_ban(self):
#         data = self.model.lay_tong_luong_theo_phong_ban()
#         self.view.hien_thi_bieu_do_luong(data)
#
#     # def hien_thi_tong_quan_du_an(self):
#     #     data = self.model.lay_tong_quan_du_an()
#     #     self.view.hien_thi_bieu_do_du_an(data)
#
#     def hien_thi_bieu_do_du_an(self):
#         data = self.model.lay_tong_quan_du_an()
#         self.view.hien_thi_bieu_do_du_an(data)
#
#     def hien_thi_tien_do_du_an(self):
#         data = self.model.lay_tien_do_du_an()
#         self.view.hien_thi_tien_do_du_an(data)
#
#     def hien_thi_bieu_do_luong(self):
#         """Hiển thị biểu đồ tổng lương theo phòng ban"""
#         data = self.model.lay_tong_luong_theo_phong_ban()
#         self.view.hien_thi_bieu_do_luong(data)


from models.model_quan_tri import ModelQuanTri


class ControllerQuanTri:
    def __init__(self, view, database):
        """
        Hàm khởi tạo lớp ControllerQuanTri.

        Parameters:
        - view: Giao diện liên kết với controller.
        - database: Đối tượng cơ sở dữ liệu dùng để truy vấn và xử lý dữ liệu.
        """
        self.view = view
        self.model = ModelQuanTri(database)

    def hien_thi_danh_sach_nguoi_dung(self):
        """
        Hiển thị danh sách người dùng.
        Lấy dữ liệu từ model và hiển thị trên giao diện thông qua view.
        """
        data = self.model.lay_danh_sach_nguoi_dung()
        self.view.hien_thi_danh_sach_nguoi_dung(data)

    def hien_thi_tong_luong_theo_phong_ban(self):
        """
        Hiển thị tổng lương theo phòng ban.
        Lấy dữ liệu từ model và hiển thị biểu đồ trên giao diện.
        """
        data = self.model.lay_tong_luong_theo_phong_ban()
        self.view.hien_thi_bieu_do_luong(data)

    def hien_thi_bieu_do_du_an(self):
        """
        Hiển thị biểu đồ tổng quan dự án.
        Lấy dữ liệu từ model và hiển thị biểu đồ trên giao diện thông qua view.
        """
        data = self.model.lay_tong_quan_du_an()
        self.view.hien_thi_bieu_do_du_an(data)

    def hien_thi_tien_do_du_an(self):
        """
        Hiển thị tiến độ các dự án.
        Lấy dữ liệu từ model và hiển thị biểu đồ tiến độ trên giao diện thông qua view.
        """
        data = self.model.lay_tien_do_du_an()
        self.view.hien_thi_tien_do_du_an(data)

    def hien_thi_bieu_do_luong(self):
        """Hiển thị biểu đồ tổng lương theo phòng ban.
        Lấy dữ liệu từ model và hiển thị biểu đồ trên giao diện thông qua view."""
        data = self.model.lay_tong_luong_theo_phong_ban()
        self.view.hien_thi_bieu_do_luong(data)
