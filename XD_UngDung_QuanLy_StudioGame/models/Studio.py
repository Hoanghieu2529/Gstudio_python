class Studio:
    def __init__(self, ten_studio: str):
        self.ten_studio = ten_studio
        self.phongban = []
        self.duan = []
        self.nhanvien = []

    def them_phong_ban(self, phongban):
        self.phongban.append(phongban)

    def them_duan(self, duan):
        self.duan.append(duan)

    def them_nhanvien(self, nhanvien):
        self.nhanvien.append(nhanvien)