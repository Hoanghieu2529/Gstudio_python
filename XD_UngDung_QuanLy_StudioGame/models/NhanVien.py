from models import PhongBan, CongViec

class NhanVien:
    def __init__(self, ma_nhanvien: int, ten_nhanvien: str, vaitro: str, phongban: PhongBan, email_nhanvien: str):
        if not isinstance(phongban, PhongBan):
            raise TypeError('phongban phải là kiểu PhongBan')

        self.__ma_nhanvien = ma_nhanvien
        self._ten_nhanvien = ten_nhanvien
        self._vaitro = vaitro
        self._phongban = phongban
        self._email_nhanvien = email_nhanvien
        self._congviec = []

    def them_nhanvien(self):
        pass

    def giao_congviec(self, congviec: CongViec):
        if not isinstance(congviec, CongViec):
            raise TypeError('congviec phải là kiểu CongViec')
        self._congviec.append(congviec)

    def lietke_congviec(self):
        return [cv.ten_congviec for cv in self._congviec]

    def __str__(self):
        return (f"Nhân viên: {self._ten_nhanvien}, Vai trò: {self._vaitro}, "
                f"Email: {self._email_nhanvien}, Công việc: {', '.join(self.lietke_congviec())}")
