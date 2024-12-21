class PhongBan:
    def __init__(self, ma_phongban: int, ten_phongban: str, quanly_phongban: str):
        self.ma_phongban = ma_phongban
        self.ten_phongban = ten_phongban
        self.quanly_phongban = quanly_phongban
        self.nhanvien = []

    def them_nhanvien(self, nhanvien: str):
        self.nhanvien.append(nhanvien)

    def loaibo_nhanvien(self, ten_nhanvien: str):
        self.nhanvien = [nv for nv in self.nhanvien if nv != ten_nhanvien]

    def lietke_nhanvien(self):
        return self.nhanvien

    def __str__(self):
        return f"Phòng ban: {self.ten_phongban} (Mã: {self.ma_phongban})"
