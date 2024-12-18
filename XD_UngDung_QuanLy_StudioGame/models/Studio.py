class Studio:
    def __init__(self, studio_Name: str):
        self.studio_Name = studio_Name
        self.phongban = []
        self.duan = []
        self.nhanvien = []

    def them_phong_ban(self, phongban):
        self.phongban.append(phongban)

    def them_duan(self, duan):
        self.duan.append(duan)

    def them_nhanvien(self, nhanvien):
        self.nhanvien.append(nhanvien)