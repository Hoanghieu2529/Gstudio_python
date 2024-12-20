from models import NhanVien, CongViec

class Timesheet:
    def __init__(self, nhanvien: NhanVien, congviec: CongViec, gio_lam: float = 0):
        self.ma_nhanvien = nhanvien.ma_nhanvien
        self.ma_congvienc = congviec.ma_congviec
        self.gio_lam = gio_lam

    def them_gio_lam(self, gio: float):
        if gio < 0:
            raise ValueError('Số giờ làm không thể bé hơn không')
        self.gio_lam += gio

    def print_gio_lam(self):
        pass
