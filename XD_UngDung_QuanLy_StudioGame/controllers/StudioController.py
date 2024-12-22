from models import *

class HeThongController:
    def __init__(self):
        self.duan_list = []
        self.phongban_list = []

    # Quản lý Dự Án
    def tao_duan(self, ma_duan, ten_duan, mota_duan, ng_batdau_duan, ng_ketthuc_duan, trang_thai_duan):
        duan = DuAn(ma_duan, ten_duan, mota_duan, ng_batdau_duan, ng_ketthuc_duan, trang_thai_duan)
        self.duan_list.append(duan)
        return duan

    def lietke_duan(self):
        return [str(duan) for duan in self.duan_list]

    # Quản lý Phòng Ban
    def tao_phongban(self, ma_phongban, ten_phongban, quanly_phongban):
        phongban = PhongBan(ma_phongban, ten_phongban, quanly_phongban)
        self.phongban_list.append(phongban)
        return phongban

    def lietke_phongban(self):
        return [str(pb) for pb in self.phongban_list]

    # Quản lý Nhân Viên
    def them_nhanvien(self, phongban_id, ma_nhanvien, ten_nhanvien, vaitro, email_nhanvien):
        phongban = next((pb for pb in self.phongban_list if pb.ma_phongban == phongban_id), None)
        if phongban:
            nhanvien = NhanVien(ma_nhanvien, ten_nhanvien, vaitro, phongban, email_nhanvien)
            phongban.them_nhanvien(nhanvien)
            return nhanvien
        raise ValueError("Phòng ban không tồn tại.")
