from models.database import Database

class ModelDuAn:
    def __init__(self):
        self.db = Database()

    def lay_danh_sach_du_an(self):
        """Lấy danh sách dự án từ cơ sở dữ liệu"""
        db = Database()
        try:
            query = "SELECT mada, ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, trang_thai FROM du_an"
            result = db.fetch_all(query)
            return result
        except Exception as e:
            print(f"Lỗi khi truy vấn dữ liệu dự án: {e}")
            return []
        finally:
            del db

    def them_du_an(self, ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh, trang_thai):
        """Thêm mới một dự án."""
        query = """
            INSERT INTO du_an (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh, trang_thai)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.db.execute_query(query, (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh, trang_thai))

    def cap_nhat_du_an(self, mada, ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh, trang_thai):
        """Cập nhật thông tin một dự án."""
        query = """
            UPDATE du_an
            SET ten_du_an = %s, mo_ta = %s, ngay_bat_dau = %s, ngay_ket_thuc = %s, makh = %s, trang_thai = %s
            WHERE mada = %s
        """
        self.db.execute_query(query, (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh, trang_thai, mada))

    def xoa_du_an(self, mada):
        """Xóa một dự án."""
        query = "DELETE FROM du_an WHERE mada = %s"
        self.db.execute_query(query, (mada,))
