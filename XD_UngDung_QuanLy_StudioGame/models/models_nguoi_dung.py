import bcrypt
from models.database import Database


class model_nguoi_dung:
    @staticmethod
    def hash_password(mat_khau):
        """Hàm mã hóa mật khẩu."""
        return bcrypt.hashpw(mat_khau.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def them_nguoi_dung(ten_dang_nhap, mat_khau, email, vai_tro):
        """Thêm người dùng mới vào cơ sở dữ liệu."""
        query = """
            INSERT INTO nguoi_dung (ten_dang_nhap, mat_khau, email, vai_tro)
            VALUES (%s, %s, %s, %s)
            """
        hashed_password = bcrypt.hashpw(mat_khau.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        db = Database()
        try:
            db.execute_query(query, (ten_dang_nhap, hashed_password, email, vai_tro))
            return True
        except Exception as e:
            print("Lỗi khi thêm người dùng:", e)
            return False

    @staticmethod
    def kiem_tra_dang_nhap(ten_dang_nhap, mat_khau):
        """Xác thực thông tin đăng nhập."""
        query = "SELECT mat_khau FROM nguoi_dung WHERE ten_dang_nhap = %s"
        db = Database()
        user = db.fetch_one(query, (ten_dang_nhap,))
        if user:
            stored_password = user['mat_khau']
            if bcrypt.checkpw(mat_khau.encode('utf-8'), stored_password.encode('utf-8')):
                return True
        return False

    @staticmethod
    def kiem_tra_vai_tro(ten_dang_nhap):
        """Lấy vai trò của người dùng dựa trên tên đăng nhập."""
        db = Database()
        try:
            query = "SELECT vai_tro FROM nguoi_dung WHERE ten_dang_nhap = %s"
            result = db.fetch_all(query, (ten_dang_nhap,))
            return result[0]['vai_tro'] if result else None
        finally:
            db.__del__()  # Đóng kết nối sau khi sử dụng

