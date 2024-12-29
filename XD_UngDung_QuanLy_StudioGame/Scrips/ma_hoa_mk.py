from bcrypt import gensalt, hashpw
import mysql.connector

#Chạy file này sau khi chạy bang _nguoi dung lần đầu trong _ CSDL
# Kết nối tới cơ sở dữ liệu

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="studio"
)

cursor = connection.cursor()

# Lấy danh sách người dùng từ cơ sở dữ liệu
cursor.execute("SELECT mand, mat_khau FROM nguoi_dung")
nguoi_dung = cursor.fetchall()

# Mã hóa mật khẩu và cập nhật lại cơ sở dữ liệu
for mand, mat_khau in nguoi_dung:
    hashed_password = hashpw(str(mat_khau).encode(), gensalt()).decode()
    query = "UPDATE nguoi_dung SET mat_khau = %s WHERE mand = %s"
    cursor.execute(query, (hashed_password, mand))

# Lưu thay đổi vào cơ sở dữ liệu
connection.commit()
print("Cập nhật mật khẩu mã hóa thành công!")

# Đóng kết nối
cursor.close()
connection.close()
