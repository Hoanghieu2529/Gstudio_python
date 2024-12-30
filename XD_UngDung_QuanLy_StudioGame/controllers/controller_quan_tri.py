from models.model_quan_tri import ModelQuanTri

class ControllerQuanTri:
    def __init__(self, view):
        self.model = ModelQuanTri()
        self.view = view

    def hien_thi_danh_sach_nguoi_dung(self):
        data = self.model.lay_danh_sach_nguoi_dung()
        if hasattr(self.view, 'cap_nhat_danh_sach_nguoi_dung'):
            self.view.cap_nhat_danh_sach_nguoi_dung(data)

    def hien_thi_tong_luong_theo_phong_ban(self):
        data = self.model.lay_tong_luong_theo_phong_ban()
        self.view.hien_thi_bieu_do_luong(data)

    def hien_thi_tong_quan_du_an(self):
        data = self.model.lay_tong_quan_du_an()
        self.view.hien_thi_bieu_do_du_an(data)

    def hien_thi_tien_do_du_an(self):
        data = self.model.lay_tien_do_du_an()
        self.view.hien_thi_tien_do_du_an(data)
