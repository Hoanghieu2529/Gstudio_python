# import mysql.connector
# """Ghi log cho truy vấn và lỗi để check lỗi"""
# import logging
# logging.basicConfig(level=logging.INFO)
#
#
# class Database:
#     def __init__(self):
#         try:
#             self.connection = mysql.connector.connect(
#                 host="localhost",
#                 user="root",
#                 password="1234",
#                 database="studio",
#                 connection_timeout=10
#             )
#             logging.info("Kết nối cơ sở dữ liệu thành công.")
#         except mysql.connector.Error as err:
#             logging.error(f"Lỗi khi kết nối cơ sở dữ liệu: {err}")
#             raise
#         # self.connection = mysql.connector.connect(
#         #     host="localhost",
#         #     user="root",
#         #     password="1234",
#         #     database="studio",
#         #     connection_timeout=10
#         # )
#         # self.cursor = self.connection.cursor(dictionary=True)
#
#
#
#     def execute_query(self, query, values=None):
#         """Thực thi truy vấn với hoặc không có tham số"""
#         try:
#             self.cursor.execute(query, values or ())
#             self.connection.commit()
#             logging.info("Query executed successfully")
#         except mysql.connector.Error as err:
#             logging.error("Error executing query: %s", err)
#             self.connection.rollback()
#
#     def fetch_one(self, query, values=None):
#         """Lấy một hàng dữ liệu từ một truy vấn"""
#         try:
#             self.cursor.execute(query, values or ())
#             logging.info("Query executed: %s", query)
#             return self.cursor.fetchone()
#         except mysql.connector.Error as err:
#             logging.error("Error fetching one: %s", err)
#             return None
#
#     def fetch_all(self, query, values=None):
#         """Lấy tất cả dữ liệu từ một truy vấn"""
#         try:
#             self.cursor.execute(query, values or ())
#             logging.info("Query executed: %s", query)
#             return self.cursor.fetchall()
#         except mysql.connector.Error as err:
#             logging.error("Error fetching all: %s", err)
#             return []
#
#     def fetch_all_phong_ban(self):
#         """Lấy tất cả thông tin từ bảng phong_ban."""
#         query = "SELECT * FROM phong_ban"
#         try:
#             result = self.fetch_all(query)
#             return result
#         except Exception as e:
#             print(f"Lỗi khi lấy dữ liệu phòng ban: {e}")
#             return []
#     def kiem_tra_ket_noi(self):
#         """Kiểm tra kết nối với cơ sở dữ liệu."""
#         try:
#             self.connection.ping(reconnect=True, attempts=3, delay=5)
#             logging.info("Kết nối cơ sở dữ liệu vẫn hoạt động.")
#         except mysql.connector.Error as err:
#             logging.error(f"Kết nối cơ sở dữ liệu bị lỗi: {err}")
#             raise
#
#     def __enter__(self):
#         """Bắt đầu sử dụng kết nối trong khối with"""
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """Kết thúc sử dụng kết nối, đóng tài nguyên"""
#         try:
#             if self.cursor:
#                 self.cursor.close()
#             if self.connection:
#                 self.connection.close()
#             logging.info("Database connection closed")
#         except Exception as e:
#             logging.error("Error during connection close: %s", e)
#
# #Kiểm thử WITH trong file database
# if __name__ == "__main__":
#     with Database() as db:
#         try:
#             db.kiem_tra_ket_noi()
#             print("Kết nối cơ sở dữ liệu thành công.")
#
#             # Kiểm tra fetch_all
#             phong_ban = db.fetch_all("SELECT * FROM phong_ban;")
#             print("Dữ liệu phòng ban:", phong_ban)
#
#             # Kiểm tra fetch_one
#             phong_ban_dau_tien = db.fetch_one("SELECT * FROM phong_ban LIMIT 1;")
#             print("Phòng ban đầu tiên:", phong_ban_dau_tien)
#         except Exception as e:
#             print(f"Lỗi khi thao tác cơ sở dữ liệu: {e}")
#
import mysql.connector
import logging

logging.basicConfig(level=logging.INFO)

class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="studio",
                connection_timeout=10
            )
            logging.info("Kết nối cơ sở dữ liệu thành công.")
        except mysql.connector.Error as err:
            logging.error(f"Lỗi khi kết nối cơ sở dữ liệu: {err}")
            raise

    def execute_query(self, query, values=None):
        """Thực thi truy vấn với hoặc không có tham số."""
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, values or ())
                self.connection.commit()
                logging.info(f"Query executed: {query}")
        except mysql.connector.Error as err:
            logging.error(f"Error executing query: {err}")
            self.connection.rollback()
            raise

    def fetch_one(self, query, values=None):
        """Lấy một hàng dữ liệu từ một truy vấn."""
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, values or ())
                logging.info(f"Query executed: {query}")
                return cursor.fetchone()
        except mysql.connector.Error as err:
            logging.error(f"Error fetching one: {err}")
            return None

    def fetch_all(self, query, values=None):
        """Lấy tất cả dữ liệu từ một truy vấn."""
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute(query, values or ())
                logging.info(f"Query executed: {query}")
                return cursor.fetchall()
        except mysql.connector.Error as err:
            logging.error(f"Error fetching all: {err}")
            return []

    def fetch_all_phong_ban(self):
        """Lấy tất cả thông tin từ bảng phong_ban."""
        query = "SELECT * FROM phong_ban"
        try:
            return self.fetch_all(query)
        except Exception as e:
            logging.error(f"Lỗi khi lấy dữ liệu phòng ban: {e}")
            return []

    def kiem_tra_ket_noi(self):
        """Kiểm tra kết nối với cơ sở dữ liệu."""
        try:
            self.connection.ping(reconnect=True, attempts=3, delay=5)
            logging.info("Kết nối cơ sở dữ liệu vẫn hoạt động.")
        except mysql.connector.Error as err:
            logging.error(f"Kết nối cơ sở dữ liệu bị lỗi: {err}")
            raise

    def __enter__(self):
        """Bắt đầu sử dụng kết nối trong khối with."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Kết thúc sử dụng kết nối, đóng tài nguyên."""
        try:
            if self.connection:
                self.connection.close()
            logging.info("Đã đóng kết nối cơ sở dữ liệu.")
        except Exception as e:
            logging.error(f"Lỗi khi đóng kết nối: {e}")
