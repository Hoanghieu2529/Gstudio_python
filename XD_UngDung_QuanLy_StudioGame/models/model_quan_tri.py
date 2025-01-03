# from models.database import Database
# import os
# print(f"Đang làm việc tại: {os.getcwd()}")
#
#
# class ModelQuanTri:
#     def __init__(self):
#         self.__db = Database()
#
#     @property
#     def db(self):
#         return self.__db
#
#     def lay_danh_sach_nguoi_dung(self):
#         """Lấy danh sách người dùng từ cơ sở dữ liệu"""
#         query = """
#                 SELECT mand, ten_dang_nhap, email, vai_tro, ngay_dang_ky
#                 FROM nguoi_dung;
#                 ORDER BY mand;
#                 """
#         return self.db.fetch_all(query)
#
#
#     def lay_tong_luong_theo_phong_ban(self):
#         """Lấy tổng lương của nhân viên theo phòng ban"""
#         query = """
#         SELECT phong_ban.ten_phong_ban, SUM(nhan_vien.luong_cb) AS tong_luong
#         FROM nhan_vien
#         JOIN phong_ban ON nhan_vien.mapb = phong_ban.mapb
#         GROUP BY phong_ban.ten_phong_ban;
#         """
#         return self.db.fetch_all(query)
#
#     # def lay_tong_quan_du_an(self):
#     #     """Lấy cột trạng thái của bảng du_an"""
#     #     query = """
#     #     SELECT du_an.trang_thai, COUNT(*) AS so_luong
#     #     FROM du_an
#     #     GROUP BY du_an.trang_thai;
#     #     """
#     #     return self.__db.fetch_all(query)
#     def lay_du_an_dang_thuc_hien(self):
#         """Lấy danh sách dự án đang thực hiện"""
#         query = """
#         SELECT ten_du_an, ngay_bat_dau, ngay_ket_thuc
#         FROM du_an
#         WHERE trang_thai IN ('dang_thuc_hien');
#         """
#         return self.db.fetch_all(query)
#
#     def lay_tien_do_du_an(self):
#         """Truy vấn tiến độ của dự án"""
#         query = """
#         SELECT ten_du_an, ngay_bat_dau, ngay_ket_thuc
#         FROM du_an
#         WHERE trang_thai = 'dang_thuc_hien' Or trang_thai = 'hoàn thành';
#         """
#         return self.__db.fetch_all(query)
from models.database import Database
import os
print(f"Đang làm việc tại: {os.getcwd()}")


class ModelQuanTri:
    """
    Lớp đại diện cho các thao tác quản trị trên cơ sở dữ liệu.

    Bao gồm các chức năng:
    - Lấy danh sách người dùng.
    - Tính tổng lương theo phòng ban.
    - Tổng quan trạng thái dự án.
    - Truy vấn tiến độ của dự án.
    """
    def __init__(self,database):
        """
        Khởi tạo lớp `ModelQuanTri`.
        - Đầu vào:
            + database: Đối tượng kết nối cơ sở dữ liệu (`Database`).
        - Đầu ra:
            + Khởi tạo kết nối cơ sở dữ liệu để thực hiện các truy vấn.
        """
        self.db = Database()
        self.db = database

    def lay_danh_sach_nguoi_dung(self):
        """
        Lấy danh sách người dùng từ cơ sở dữ liệu.
            + Danh sách người dùng, bao gồm các thông tin:
              * Mã người dùng (`mand`)
              * Tên đăng nhập (`ten_dang_nhap`)
              * Vai trò (`vai_tro`)
              * Email (`email`)
              * Ngày đăng ký (`ngay_dang_ky`)
        """
        query = "SELECT mand, ten_dang_nhap, vai_tro, email, ngay_dang_ky FROM nguoi_dung;"
        return self.db.fetch_all(query)

    def lay_tong_luong_theo_phong_ban(self):
        """
        Lấy tổng lương của nhân viên theo từng phòng ban.

        - Đầu vào: Không có.
        - Đầu ra:
            + Danh sách tổng lương theo phòng ban, bao gồm:
              * Tên phòng ban (`ten_phong_ban`)
              * Tổng lương (`tong_luong`)
        """
        query = """
        SELECT phong_ban.ten_phong_ban, SUM(nhan_vien.luong_cb) AS tong_luong
        FROM nhan_vien
        JOIN phong_ban ON nhan_vien.mapb = phong_ban.mapb
        GROUP BY phong_ban.ten_phong_ban;
        """
        return self.db.fetch_all(query)

    def lay_tong_quan_du_an(self):
        """
        Lấy thông tin tổng quan về trạng thái các dự án.
        - Đầu ra:
            + Danh sách trạng thái dự án, bao gồm:
              * Trạng thái (`trang_thai`)
              * Số lượng dự án ở trạng thái đó (`so_luong`)
        """
        query = """
                SELECT du_an.trang_thai, COUNT(*) AS so_luong
                FROM du_an
                GROUP BY du_an.trang_thai;
                """
        query = """
        SELECT du_an.trang_thai, COUNT(*) AS so_luong
        FROM du_an
        GROUP BY du_an.trang_thai;
        """
        return self.db.fetch_all(query)

    def lay_tien_do_du_an(self):
        """
        Lấy tiến độ của các dự án đang thực hiện hoặc đã hoàn thành.

        - Đầu vào: Không có.
        - Đầu ra:
            + Danh sách dự án, bao gồm:
              * Tên dự án (`ten_du_an`)
              * Ngày bắt đầu (`ngay_bat_dau`)
              * Ngày kết thúc (`ngay_ket_thuc`)
        """
        query = """
        SELECT ten_du_an, ngay_bat_dau, ngay_ket_thuc
        FROM du_an
        WHERE trang_thai IN ('dang_thuc_hien', 'hoàn thành');
        """
        return self.db.fetch_all(query)


