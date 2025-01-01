from models.models_BaoCaoNhanSu import ModelBaoCaoNhanSu
from View.View_BaoCaoNhanSu import BaoCaoNhanSuForm


class ControllerBaoCaoNhanSu:
    def __init__(self, root):
        self.model = ModelBaoCaoNhanSu()
        self.view = BaoCaoNhanSuForm(root, self)

    def tai_lai_bao_cao(self):
        """Tải lại dữ liệu báo cáo"""
        so_luong_data = self.model.lay_so_luong_nhan_vien()
        self.view.hien_thi_bieu_do_treemap(so_luong_data)

        thong_ke_luong = self.model.lay_thong_ke_luong()
        self.view.hien_thi_bieu_do_luong(thong_ke_luong)
