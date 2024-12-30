from models.models_nguoi_dung import model_nguoi_dung
from models.database import Database

class controller_dang_nhap:
    def __init__(self):
        self.db = Database()

    def xu_ly_dang_nhap(self, ten_dang_nhap, mat_khau):
        return model_nguoi_dung.kiem_tra_dang_nhap(ten_dang_nhap, mat_khau) is not None

    def xac_dinh_vai_tro(self, ten_dang_nhap, mat_khau):
        query = "SELECT vai_tro FROM nguoi_dung WHERE ten_dang_nhap = %s AND mat_khau = %s"
        result = self.db.fetch_one(query, (ten_dang_nhap, mat_khau))
        return result['vai_tro'] if result else None

