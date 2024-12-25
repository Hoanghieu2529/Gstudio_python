import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="studio"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def execute_query(self, query, values=None):
        """Thực thi truy vấn với hoặc không có tham số"""
        self.cursor.execute(query, values or ())
        self.connection.commit()

    def fetch_one(self, query, values=None):
        """Lấy một hàng dữ liệu từ một truy vấn"""
        self.cursor.execute(query, values or ())
        return self.cursor.fetchone()

    def fetch_all(self, query, values=None):
        """Lấy tất cả dữ liệu từ một truy vấn"""
        self.cursor.execute(query, values or ())
        return self.cursor.fetchall()

    def __del__(self):
        """Đóng kết nối khi không sử dụng"""
        self.connection.close()
