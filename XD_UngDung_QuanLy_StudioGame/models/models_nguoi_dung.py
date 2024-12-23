import bcrypt
from models.database import Database


class model_nguoi_dung:
    @staticmethod
    def hash_password(mat_khau):
        """Hàm mã hóa mật khẩu."""
        return bcrypt.hashpw(mat_khau.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def them_nguoi_dung(ten_dang_nhap, mat_khau, vai_tro):
        """Thêm người dùng mới vào cơ sở dữ liệu với mật khẩu mã hóa."""
        db = Database()
        try:
            hashed_password = model_nguoi_dung.hash_password(mat_khau)
            query = "INSERT INTO nguoi_dung (ten_dang_nhap, mat_khau, vai_tro) VALUES (%s, %s, %s)"
            db.execute_query(query, (ten_dang_nhap, hashed_password, vai_tro))
            print(f"Người dùng {ten_dang_nhap} đã được thêm thành công.")
        except Exception as e:
            print(f"Lỗi khi thêm người dùng: {e}")
        finally:
            db.__del__()  # Đóng kết nối DB

    @staticmethod
    def kiem_tra_dang_nhap(ten_dang_nhap, mat_khau):
        """Kiểm tra đăng nhập với mật khẩu mã hóa."""
        db = Database()
        try:
            # Truy vấn người dùng theo tên đăng nhập
            query = "SELECT * FROM nguoi_dung WHERE ten_dang_nhap = %s"
            result = db.fetch_all(query, (ten_dang_nhap,))

            # Nếu tìm thấy người dùng, kiểm tra mật khẩu
            if result:
                user = result[0]
                stored_password = user['mat_khau']  # Lấy mật khẩu đã mã hóa từ DB
                if bcrypt.checkpw(mat_khau.encode('utf-8'), stored_password.encode('utf-8')):
                    return user  # Đăng nhập thành công, trả về thông tin người dùng
            return None  # Sai mật khẩu hoặc không tìm thấy người dùng
        finally:
            db.__del__()  # Đóng kết nối DB

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


