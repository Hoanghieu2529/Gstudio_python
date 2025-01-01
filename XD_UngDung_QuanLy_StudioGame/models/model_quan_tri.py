from models.database import Database
import os
print(f"Đang làm việc tại: {os.getcwd()}")


class ModelQuanTri:
    def __init__(self):
        self.__db = Database()

    @property
    def db(self):
        return self.__db

    def lay_danh_sach_nguoi_dung(self):
        query = "SELECT * FROM nguoi_dung;"
        return self.db.fetch_all(query)

    def lay_tong_luong_theo_phong_ban(self):
        query = """
        SELECT phong_ban.ten_phong_ban, SUM(nhan_vien.luong_cb) AS tong_luong
        FROM nhan_vien
        JOIN phong_ban ON nhan_vien.mapb = phong_ban.mapb
        GROUP BY phong_ban.ten_phong_ban;
        """
        return self.db.fetch_all(query)

    def lay_tong_quan_du_an(self):
        query = """
        SELECT du_an.trang_thai, COUNT(*) AS so_luong
        FROM du_an
        GROUP BY du_an.trang_thai;
        """
        return self.__db.fetch_all(query)

    def lay_tien_do_du_an(self):
        query = """
        SELECT ten_du_an, ngay_bat_dau, ngay_ket_thuc
        FROM du_an
        WHERE trang_thai = 'dang_thuc_hien' Or trang_thai = 'hoàn thành';
        """
        return self.__db.fetch_all(query)
