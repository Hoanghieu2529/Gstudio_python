from models.models_nguoi_dung import model_nguoi_dung

class controller_dang_nhap:
    def __init__(self):
        pass

    def xu_ly_dang_nhap(self, ten_dang_nhap, mat_khau):
        return model_nguoi_dung.kiem_tra_dang_nhap(ten_dang_nhap, mat_khau) is not None
