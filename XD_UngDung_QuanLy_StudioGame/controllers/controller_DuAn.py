from models.models_du_an import ModelDuAn

class DuAnFormController:
    def __init__(self, view):
        self.view = view
        self.model = ModelDuAn()
        self.tai_du_lieu()

    def tai_du_lieu(self):
        """Tải dữ liệu dự án và hiển thị lên View"""
        du_lieu = self.model.lay_danh_sach_du_an()
        self.view.hien_thi_du_lieu(du_lieu)

    def them_du_an(self, data):
        """Thêm mới dự án"""
        try:
            self.model.them_du_an(data)
            self.view.hien_thi_du_lieu(self.model.lay_tat_ca_du_an())
            print("Dự án được thêm thành công!")
        except Exception as e:
            print(f"Lỗi khi thêm dự án: {e}")

    def cap_nhat_du_an(self, data):
        """Cập nhật dự án"""
        try:
            self.model.cap_nhat_du_an(data)
            self.view.hien_thi_du_lieu(self.model.lay_tat_ca_du_an())
            print("Cập nhật dự án thành công!")
        except Exception as e:
            print(f"Lỗi khi cập nhật dự án: {e}")

    def xoa_du_an(self, mada):
        """Xóa dự án"""
        try:
            self.model.xoa_du_an(mada)
            self.view.hien_thi_du_lieu(self.model.lay_tat_ca_du_an())
            print("Xóa dự án thành công!")
        except Exception as e:
            print(f"Lỗi khi xóa dự án: {e}")