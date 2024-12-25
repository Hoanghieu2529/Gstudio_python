import logging
import bcrypt
from models.database import Database

# Thêm chức năng ghi log
logging.basicConfig(
    filename="cap_nhat_mat_khau.log",  # Tên file log
    filemode="a",  # Ghi log vào cuối file (append mode)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Định dạng log
    level=logging.INFO,  # Mức log: INFO, DEBUG, WARNING, ERROR
)

def cap_nhat_mat_khau():
    """Hàm cập nhật mật khẩu mã hóa"""
    db = Database()

    query_select = "SELECT mand, mat_khau FROM nguoi_dung"
    query_update = "UPDATE nguoi_dung SET mat_khau = %s WHERE mand = %s"

    try:
        users = db.fetch_all(query_select)  # Lấy tất cả người dùng và mật khẩu
        for user in users:
            try:
                mat_khau = user['mat_khau']
                # Kiểm tra nếu mật khẩu chưa mã hóa
                if not mat_khau.startswith("$2b$"):
                    hashed_password = bcrypt.hashpw(mat_khau.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    db.execute_query(query_update, (hashed_password, user['mand']))
                    logging.info(f"Cập nhật mật khẩu thành công cho người dùng: {user['mand']}")
                else:
                    logging.info(f"Mật khẩu của người dùng {user['mand']} đã được mã hóa, bỏ qua.")
            except Exception as user_error:
                logging.error(f"Lỗi khi cập nhật mật khẩu cho người dùng {user['mand']}: {user_error}")
        logging.info("Cập nhật mật khẩu hoàn tất.")
    except Exception as e:
        logging.error(f"Lỗi khi thực hiện cập nhật mật khẩu: {e}")

