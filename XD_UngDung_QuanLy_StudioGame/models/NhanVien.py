from models import PhongBan, CongViec

class NhanVien:
    def __init__(self, ma_nhanvien: int, ten_nhanvien: str, vaitro: str, phongban: PhongBan, email_nhanvien: str):
        #Xác thực tham số
        if not isinstance(phongban, PhongBan):
            raise TypeError('phongban must be of type PhongBan')

        self.ma_nhanvien = ma_nhanvien
        self.ten_nhanvien = ten_nhanvien
        self.vaitro = vaitro
        self.ma_phongban = phongban.ma_phongban
        self.email_nhanvien = email_nhanvien
        self.congviec = []

    def giao_cong_viec(self, congviec):
        if not isinstance(congviec, CongViec):
            raise TypeError('congviec must be of type CongViec')
        self.congviec.append(congviec)

    def in_nhanvien(self):
        #In nhân viên và công việc được giao
        print(f"Mã nhân viên: {self.ma_nhanvien}")
        print(f"Tên: {self.ten_nhanvien}")
        print(f"Vai trò: {self.vaitro}")
        print(f"Phòng ban ID: {self.ma_phongban}")
        print(f"Email: {self.email_nhanvien}")
        print("Danh sách công việc được giao:")
        if self.congviec:
            for idx, cv in enumerate(self.congviec, start=1):
                print(f"  {idx}. Công việc ID: {cv.ma_congviec}, Tên công việc: {cv.ten_congviec}")
        else:
            print("  Chưa có công việc nào được giao.")