from models.database import Database

class ModelTinhLuong:
    def __init__(self):
        self.db = Database()

    def lay_danh_sach_luong(self):
        """Lấy danh sách thông tin lương của nhân viên từ cơ sở dữ liệu."""
        query = """
        SELECT bc.mabc, bc.manv, nv.ho_ten, nv.chuc_vu, nv.luong_cb, bc.ngay_cong, bc.so_luong_san_pham
        FROM bang_cong AS bc
        JOIN nhan_vien AS nv ON bc.manv = nv.manv
        ORDER BY nv.manv ASC;
        """
        return self.db.fetch_all(query)

    def cap_nhat_ngay_cong(self, manv, ngay_cong_moi):
        """Cập nhật số ngày công cho nhân viên."""
        query = """
        UPDATE nhan_vien
        SET ngay_cong = %s
        WHERE manv = %s
        """
        self.db.execute(query, (ngay_cong_moi, manv))
