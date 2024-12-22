from models import DuAn, PhongBan


class Studio:
    def __init__(self, ten_studio: str):
        self.ten_studio = ten_studio
        self.duan = []
        self.phongban = []

    def them_duan(self, duan: DuAn):
        self.duan.append(duan)

    def loaibo_duan(self, ten_duan: str):
        self.duan = [d for d in self.duan if d.ten_duan != ten_duan]

    def lietke_duan(self):
        return [duan.ten_duan for duan in self.duan]

    def them_phongban(self, phongban: PhongBan):
        self.phongban.append(phongban)

    def loaibo_phongban(self, ma_phongban: int):
        self.phongban = [pb for pb in self.phongban if pb.ma_phongban != ma_phongban]

    def lietke_phongban(self):
        return [phongban.ten_phongban for phongban in self.phongban]



