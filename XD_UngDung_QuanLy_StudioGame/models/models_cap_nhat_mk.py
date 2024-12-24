import bcrypt
from models.database import Database

def cap_nhat_mat_khau():
    db = Database()

    query_select = "SELECT mand, mat_khau FROM nguoi_dung"
    query_update = "UPDATE nguoi_dung SET mat_khau = %s WHERE mand = %s"

    try:
        users = db.fetch_all(query_select)  # Lấy tất cả người dùng và mật khẩu
        for user in users:
            hashed_password = bcrypt.hashpw(user['mat_khau'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            db.execute_query(query_update, (hashed_password, user['mand']))
        print("Cập nhật mật khẩu thành công.")
    except Exception as e:
        print("Lỗi khi cập nhật mật khẩu:", e)
