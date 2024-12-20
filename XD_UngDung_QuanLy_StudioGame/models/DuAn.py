class DuAn:
    def __init__(self, ma_duan: int, ten_duan: str, mota_duan: str, ng_batdau_duan: str, ng_ketthuc_duan: str, trang_thai_duan: str):
        self.ma_duan = ma_duan
        self.ten_duan = ten_duan
        self.mota_duan = mota_duan
        self.ng_batdau_duan = ng_batdau_duan
        self.ng_ketthuc_duan = ng_ketthuc_duan
        self.trang_thai_duan = trang_thai_duan
        self.congviec = []
        self.thanhvien = []

    def add_congviec(self, congviec):
        self.congviec.append(congviec)

    def add_thanhvien(self, thanhvien):
        self.thanhvien.append(thanhvien)

    def tinh_tien_do(self):
        pass



