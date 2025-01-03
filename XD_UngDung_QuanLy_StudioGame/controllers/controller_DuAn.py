from models.models_du_an import ModelDuAn

class DuAnFormController:
    """
    Lớp điều khiển quản lý dự án, chịu trách nhiệm tương tác giữa View (giao diện) và Model (dữ liệu).
    Bao gồm các chức năng: tải dữ liệu, thêm, cập nhật và xóa dự án.
    """
    def __init__(self, view):
        """
        Khởi tạo lớp điều khiển dự án.

        - Đầu vào:
            + view: Đối tượng giao diện (View) để hiển thị dữ liệu dự án.
        - Đầu ra:
            + Tạo đối tượng `ModelDuAn` để xử lý dữ liệu dự án.
            + Tự động tải dữ liệu dự án và hiển thị lên giao diện khi khởi tạo.
        """
        self.view = view
        self.model = ModelDuAn()
        self.tai_du_lieu()

    def tai_du_lieu(self):
        """Tải dữ liệu danh sách dự án từ Model và hiển thị lên giao diện.
        - Đầu vào: Không có.
        - Đầu ra:
            + Lấy danh sách dự án từ `ModelDuAn`.
            + Hiển thị danh sách dự án lên View thông qua phương thức `hien_thi_du_lieu`."""
        du_lieu = self.model.lay_danh_sach_du_an()
        self.view.hien_thi_du_lieu(du_lieu)

    def them_du_an(self, data):
        """
        Thêm mới một dự án.
        - Đầu vào:
            + data: Dữ liệu của dự án mới cần thêm (dạng từ điển hoặc đối tượng tùy thuộc vào thiết kế Model).
        - Đầu ra:
            + Thêm dự án vào cơ sở dữ liệu thông qua `ModelDuAn`.
            + Cập nhật danh sách dự án hiển thị trên giao diện.
            + In thông báo "Dự án được thêm thành công!" nếu thêm thành công.
            + In thông báo lỗi nếu có ngoại lệ xảy ra.
        """
        try:
            self.model.them_du_an(data)
            self.view.hien_thi_du_lieu(self.model.lay_tat_ca_du_an())
            print("Dự án được thêm thành công!")
        except Exception as e:
            print(f"Lỗi khi thêm dự án: {e}")

    def cap_nhat_du_an(self, data):
        """
        Cập nhật thông tin dự án.
        - Đầu vào:
            + data: Dữ liệu cập nhật của dự án (dạng từ điển hoặc đối tượng tùy thuộc vào thiết kế Model).
        - Đầu ra:
            + Cập nhật thông tin dự án trong cơ sở dữ liệu thông qua `ModelDuAn`.
            + Cập nhật danh sách dự án hiển thị trên giao diện.
            + In thông báo "Cập nhật dự án thành công!" nếu cập nhật thành công.
            + In thông báo lỗi nếu có ngoại lệ xảy ra.
        """
        try:
            self.model.cap_nhat_du_an(data)
            self.view.hien_thi_du_lieu(self.model.lay_tat_ca_du_an())
            print("Cập nhật dự án thành công!")
        except Exception as e:
            print(f"Lỗi khi cập nhật dự án: {e}")

    def xoa_du_an(self, mada):
        """
        Xóa một dự án.
        - Đầu vào:
            + mada: Mã dự án cần xóa.
        - Đầu ra:
            + Xóa dự án khỏi cơ sở dữ liệu thông qua `ModelDuAn`.
            + Cập nhật danh sách dự án hiển thị trên giao diện.
            + In thông báo "Xóa dự án thành công!" nếu xóa thành công.
            + In thông báo lỗi nếu có ngoại lệ xảy ra.
        """
        try:
            self.model.xoa_du_an(mada)
            self.view.hien_thi_du_lieu(self.model.lay_tat_ca_du_an())
            print("Xóa dự án thành công!")
        except Exception as e:
            print(f"Lỗi khi xóa dự án: {e}")