from models.PhongBan import PhongBan
from models.CongViec import CongViec

class NhanVien:
    def __init__(self, nhanvien_id: int, nhanvien_name: str, vaitro: str, phongban: PhongBan, nhanvien_email: str):
        #Xác thực tham số
        if not isinstance(phongban, PhongBan):
            raise TypeError('phongban must be of type PhongBan')

        self.nhanvien_id = nhanvien_id
        self.nhanvien_name = nhanvien_name
        self.vaitro = vaitro
        self.phongban_id = phongban.phongban_id
        self.nhanvien_email = nhanvien_email
        self.congviec = []

    def assign_cong_viec(self, congviec):
        if not isinstance(congviec, CongViec):
            raise TypeError('congviec must be of type CongViec')
        self.congviec.append(congviec)

    def print_nhanvien(self):
        #In nhân viên và công việc được giao
        print(f"Mã nhân viên: {self.nhanvien_id}")
        print(f"Tên: {self.nhanvien_name}")
        print(f"Vai trò: {self.vaitro}")
        print(f"Phòng ban ID: {self.phongban_id}")
        print(f"Email: {self.nhanvien_email}")
        print("Danh sách công việc được giao:")
        if self.congviec:
            for idx, cv in enumerate(self.congviec, start=1):
                print(f"  {idx}. Công việc ID: {cv.congviec_ID}, Tên công việc: {cv.name}")
        else:
            print("  Chưa có công việc nào được giao.")