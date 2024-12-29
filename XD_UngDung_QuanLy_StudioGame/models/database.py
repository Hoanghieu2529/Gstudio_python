import mysql.connector
"""Ghi log cho truy vấn và lỗi để check lỗi"""
import logging
logging.basicConfig(level=logging.INFO)

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Csharpython@95",
            database="studio"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def execute_query(self, query, values=None):
        """Thực thi truy vấn với hoặc không có tham số"""
        try:
            self.cursor.execute(query, values or ())
            self.connection.commit()
            logging.info("Query executed successfully")
        except mysql.connector.Error as err:
            print("Error: %s" % err)
            self.connection.rollback()

    def fetch_one(self, query, values=None):
        """Lấy một hàng dữ liệu từ một truy vấn"""
        self.cursor.execute(query, values or ())
        return self.cursor.fetchone()

    def fetch_all(self, query, values=None):
        """Lấy tất cả dữ liệu từ một truy vấn"""
        self.cursor.execute(query, values or ())
        return self.cursor.fetchall()

    """Chạy khi sử dụng with trong python"""
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def __del__(self):
        """Đóng kết nối khi không sử dụng"""
        self.connection.close()
