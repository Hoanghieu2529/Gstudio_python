import bcrypt
from models.database import Database
from datetime import datetime


class model_nguoi_dung:
    @staticmethod
    def hash_password(mat_khau):
        """Hàm mã hóa mật khẩu."""
        return bcrypt.hashpw(mat_khau.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def tao_mand():
        """Tạo mã người dùng với định dạng: năm + tháng + số thứ tự."""
        db = Database()
        try:
            # Lấy năm và tháng hiện tại
            now = datetime.now()
            nam = now.strftime("%y")  # Lấy 2 chữ số cuối của năm
            thang = now.strftime("%m")  # Lấy tháng hiện tại

            # Lấy số thứ tự lớn nhất từ cơ sở dữ liệu
            query = "SELECT MAX(mand) AS max_mand FROM nguoi_dung"
            result = db.fetch_one(query)

            if result and result['max_mand']:
                max_mand = int(result['max_mand'])
                stt = int(str(max_mand)[-3:]) + 1  # Tăng số thứ tự
            else:
                stt = 1  # Nếu chưa có người dùng nào, bắt đầu từ 1

            # Tạo mã người dùng
            mand = f"{nam}{thang}{stt:03d}"
            return mand
        except Exception as e:
            print("Lỗi khi tạo mã người dùng:", e)
            return None
        finally:
            db.__del__()

    @staticmethod
    def them_nguoi_dung(ten_dang_nhap, mat_khau, email, vai_tro="nguoi dung"):
        """Thêm người dùng mới vào cơ sở dữ liệu."""
        try:
            mand = model_nguoi_dung.tao_mand()  # Gọi hàm tạo mã người dùng
            hashed_password = bcrypt.hashpw(mat_khau.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            query = """
                INSERT INTO nguoi_dung (mand, ten_dang_nhap, mat_khau, email, vai_tro, ngay_dang_ky)
                VALUES (%s, %s, %s, %s, %s, NOW())
            """
            db = Database()
            db.execute_query(query, (mand, ten_dang_nhap, hashed_password, email, vai_tro))
            return True
        except Exception as e:
            print("Lỗi khi thêm người dùng:", e)
            return False

    @staticmethod
    def kiem_tra_dang_nhap(ten_dang_nhap, mat_khau):
        """Xác thực thông tin đăng nhập."""
        query = "SELECT mat_khau FROM nguoi_dung WHERE ten_dang_nhap = %s"
        db = Database()
        try:
            user = db.fetch_one(query, (ten_dang_nhap,))
            if not user:
                print("Không tìm thấy người dùng.")
                return False

            stored_password = user['mat_khau']
            print(f"Kiểm tra mật khẩu cho người dùng {ten_dang_nhap}.")
            if bcrypt.checkpw(mat_khau.encode('utf-8'), stored_password.encode('utf-8')):
                return True
            print("Mật khẩu không đúng.")
            return False
        except Exception as e:
            print(f"Lỗi khi kiểm tra đăng nhập: {e}")
            return False
        finally:
            del db   # Đảm bảo đóng kết nối

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
