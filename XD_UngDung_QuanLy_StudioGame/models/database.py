import mysql.connector
"""Ghi log cho truy vấn và lỗi để check lỗi"""
import logging
logging.basicConfig(level=logging.INFO)


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="studio"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def check_connection(self):
        """Kiểm tra kết nối với cơ sở dữ liệu"""
        try:
            self.connection.ping(reconnect=True, attempts=3, delay=5)
            logging.info("Database connection is active")
        except mysql.connector.Error as err:
            logging.error("Database connection failed: %s", err)
            raise

    def execute_query(self, query, values=None):
        """Thực thi truy vấn với hoặc không có tham số"""
        try:
            self.cursor.execute(query, values or ())
            self.connection.commit()
            logging.info("Query executed successfully")
        except mysql.connector.Error as err:
            logging.error("Error executing query: %s", err)
            self.connection.rollback()

    def fetch_one(self, query, values=None):
        """Lấy một hàng dữ liệu từ một truy vấn"""
        try:
            self.cursor.execute(query, values or ())
            logging.info("Query executed: %s", query)
            return self.cursor.fetchone()
        except mysql.connector.Error as err:
            logging.error("Error fetching one: %s", err)
            return None

    def fetch_all(self, query, values=None):
        """Lấy tất cả dữ liệu từ một truy vấn"""
        try:
            self.cursor.execute(query, values or ())
            logging.info("Query executed: %s", query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            logging.error("Error fetching all: %s", err)
            return []

    def fetch_all_phong_ban(self):
        """Lấy tất cả thông tin từ bảng phong_ban."""
        query = "SELECT * FROM phong_ban"
        try:
            result = self.fetch_all(query)
            return result
        except Exception as e:
            print(f"Lỗi khi lấy dữ liệu phòng ban: {e}")
            return []

    def __enter__(self):
        """Bắt đầu sử dụng kết nối trong khối with"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Kết thúc sử dụng kết nối, đóng tài nguyên"""
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            logging.info("Database connection closed")
        except Exception as e:
            logging.error("Error during connection close: %s", e)

#Kiểm thử WITH trong file database
if __name__ == "__main__":
    with Database() as db:
        try:
            db.check_connection()
            result = db.fetch_all("SELECT DATABASE();")
            print("Current Database:", result)
        except Exception as e:
            print("Error:", e)
