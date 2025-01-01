from models.database import Database
from mysql.connector import Error

class ModelNhanVien:
    def __init__(self):
        self.db = Database()

    def lay_danh_sach_nhan_vien(self):
        """Lấy danh sách tất cả nhân viên từ cơ sở dữ liệu."""
        query = """
        SELECT 
            nv.manv, nv.ho_ten, nv.chuc_vu, nv.email, pb.ten_phong_ban
        FROM 
            nhan_vien nv
        JOIN 
            phong_ban pb 
        ON 
            nv.mapb = pb.mapb;
        """
        result = self.db.fetch_all(query)
        return result

    def them_nhan_vien(self, ho_ten, chuc_vu, mapb, email):
        """Thêm một nhân viên mới vào cơ sở dữ liệu."""
        query = """
        INSERT INTO nhan_vien (ho_ten, chuc_vu, mapb, email)
        VALUES (%s, %s, %s, %s);
        """
        values = (ho_ten, chuc_vu, mapb, email)
        self.db.execute_query(query, values)

    def cap_nhat_nhan_vien(self, manv, ho_ten=None, chuc_vu=None, mapb=None, email=None):
        """Cập nhật thông tin của một nhân viên."""
        try:
            query = "UPDATE nhan_vien SET"
            fields: list[str] = []  # Chú thích kiểu dữ liệu
            values: list = []

            if ho_ten:
                fields.append("ho_ten = %s")
                values.append(ho_ten)
            if chuc_vu:
                fields.append("chuc_vu = %s")
                values.append(chuc_vu)
            if mapb:
                fields.append("mapb = %s")
                values.append(mapb)
            if email:
                fields.append("email = %s")
                values.append(email)

            if fields:
                query += " " + ", ".join(fields) + " WHERE manv = %s;"
                values.append(manv)
                self.db.execute_query(query, values)
        except Error as e:
            print(f"Lỗi cập nhật nhân viên: {e}")

    def xoa_nhan_vien(self, manv):
        """Xóa một nhân viên khỏi cơ sở dữ liệu."""
        query = "DELETE FROM nhan_vien WHERE manv = %s;"
        self.db.execute_query(query, (manv,))

    def lay_thong_tin_nhan_vien(self, manv):
        """Lấy thông tin chi tiết của một nhân viên."""
        query = """
        SELECT nv.manv, nv.ho_ten, nv.chuc_vu, nv.email, pb.ten_phong_ban
        FROM nhan_vien nv
        JOIN phong_ban pb ON nv.mapb = pb.mapb
        WHERE nv.manv = %s;
        """
        result = self.db.fetch_all(query, (manv,))
        return result[0] if result else None

    def lay_danh_sach_phong_ban(self):
        """Lấy danh sách các phòng ban để sử dụng trong giao diện thêm/cập nhật nhân viên."""
        query = "SELECT mapb, ten_phong_ban FROM phong_ban;"
        return self.db.fetch_all(query)

    def lay_mapb_tu_ten_phong_ban(self, ten_phong_ban):
        """Lấy mapb (mã phòng ban) dựa trên tên phòng ban."""
        query = "SELECT mapb FROM phong_ban WHERE ten_phong_ban = %s;"
        result = self.db.fetch_all(query, (ten_phong_ban,))
        return result[0]["mapb"] if result else None
