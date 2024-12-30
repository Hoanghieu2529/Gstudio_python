from models.database import Database

class PhongBanModel:
    def __init__(self):
        self.db = Database()

    def lay_danh_sach_phong_ban(self):
        """Lấy danh sách tất cả các phòng ban từ CSDL"""
        query = "SELECT mapb, ten_phong_ban, mo_ta FROM phong_ban"
        try:
            return self.db.fetch_all(query)
        except Exception as e:
            print(f"Lỗi khi truy vấn danh sách phòng ban: {e}")
            return []
