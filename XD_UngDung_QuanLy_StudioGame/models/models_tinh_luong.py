from models.database import Database

class ModelTinhLuong:
    def __init__(self):
        self.db = Database()

    def lay_danh_sach_luong(self):
        """Lấy danh sách thông tin lương của nhân viên từ cơ sở dữ liệu."""
        query = """
        SELECT nv.manv, nv.ho_ten, pb.ten_phong_ban, 3000000 AS luong_co_ban, 22 AS ngay_cong
        FROM nhan_vien nv
        JOIN phong_ban pb ON nv.mapb = pb.mapb;
        """
        return self.db.fetch_all(query)

    def cap_nhat_ngay_cong(self, manv, ngay_cong_moi):
        """Cập nhật số ngày công cho nhân viên."""
        # Ở đây thêm logic cập nhật thông tin vào cơ sở dữ liệu nếu cần.
        pass
