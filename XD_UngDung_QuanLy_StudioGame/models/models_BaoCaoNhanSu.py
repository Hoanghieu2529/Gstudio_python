from models.database import Database


class ModelBaoCaoNhanSu:
    def __init__(self):
        self.db = Database()

    def lay_so_luong_nhan_vien(self):
        """Truy vấn số lượng nhân viên theo phòng ban."""
        query = """
        SELECT pb.ten_phong_ban AS phong_ban, COUNT(nv.manv) AS so_luong
        FROM nhan_vien nv
        JOIN phong_ban pb ON nv.mapb = pb.mapb
        GROUP BY pb.ten_phong_ban;
        """
        return self.db.fetch_all(query)

    def lay_thong_ke_luong(self):
        """Truy vấn thống kê lương cơ bản."""
        query = """
        SELECT 
            MAX(nv.luong_cb) AS max, 
            MIN(nv.luong_cb) AS min, 
            AVG(nv.luong_cb) AS avg
        FROM nhan_vien nv;
        """
        result = self.db.fetch_one(query)
        if result:
            return {
                "max": result["max"],
                "min": result["min"],
                "avg": result["avg"]
            }
        else:
            return {
                "max": 0,
                "min": 0,
                "avg": 0
            }

