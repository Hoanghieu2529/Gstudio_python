from faker import Faker
import random
from datetime import datetime, timedelta

# Khởi tạo Faker
faker = Faker()

# Hàm sinh dữ liệu giả cho các bảng
def generate_fake_data():
    phong_ban_statements = []
    nhan_vien_statements = []
    khach_hang_statements = []
    du_an_statements = []
    cong_viec_statements = []
    bang_thoi_gian_statements = []

    # Dữ liệu giả cho bảng phong_ban
    phong_ban_names = ["Kỹ thuật", "Nhân sự", "Tài chính", "Marketing", "Bán hàng"]
    for name in phong_ban_names:
        phong_ban_statements.append(
            f"INSERT INTO phong_ban (ten_phong_ban, mo_ta) VALUES ('{name}', '{faker.text()}');"
        )

    # Dữ liệu giả cho bảng nhan_vien
    for i in range(1, 101):
        ho_ten = faker.name()
        email = faker.unique.email()
        chuc_vu = random.choice(["Kỹ sư", "Quản lý", "Trưởng phòng", "Nhân viên"])
        phong_ban_id = random.randint(1, len(phong_ban_names))
        nhan_vien_statements.append(
            f"INSERT INTO nhan_vien (ho_ten, email, chuc_vu, phong_ban_id) VALUES ('{ho_ten}', '{email}', '{chuc_vu}', {phong_ban_id});"
        )

    # Dữ liệu giả cho bảng khach_hang
    for i in range(1, 101):
        ten_khach_hang = faker.company()
        email = faker.unique.email()
        so_dien_thoai = faker.phone_number()
        dia_chi = faker.address().replace("\n", ", ")
        khach_hang_statements.append(
            f"INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('{ten_khach_hang}', '{email}', '{so_dien_thoai}', '{dia_chi}');"
        )

    # Dữ liệu giả cho bảng du_an
    for i in range(1, 101):
        ten_du_an = f"Dự án {i}"
        mo_ta = faker.text()
        ngay_bat_dau = faker.date_this_year().isoformat()
        ngay_ket_thuc = (datetime.strptime(ngay_bat_dau, "%Y-%m-%d") + timedelta(days=random.randint(30, 180))).date()
        khach_hang_id = random.randint(1, 100)
        du_an_statements.append(
            f"INSERT INTO du_an (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, khach_hang_id) VALUES ('{ten_du_an}', '{mo_ta}', '{ngay_bat_dau}', '{ngay_ket_thuc}', {khach_hang_id});"
        )

    # Dữ liệu giả cho bảng cong_viec
    for i in range(1, 101):
        ten_cong_viec = f"Công việc {i}"
        mo_ta = faker.text()
        du_an_id = random.randint(1, 100)
        giao_cho = random.randint(1, 100)
        han_chot = faker.date_between(start_date="today", end_date="+60d")
        trang_thai = random.choice(['chua_thuc_hien', 'dang_thuc_hien', 'hoan_thanh'])
        cong_viec_statements.append(
            f"INSERT INTO cong_viec (du_an_id, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUES ({du_an_id}, '{ten_cong_viec}', '{mo_ta}', {giao_cho}, '{han_chot}', '{trang_thai}');"
        )

    # Dữ liệu giả cho bảng bang_thoi_gian
    for i in range(1, 101):
        nhan_vien_id = random.randint(1, 100)
        cong_viec_id = random.randint(1, 100)
        so_gio = random.randint(1, 8)
        ngay_lam = faker.date_between(start_date="-30d", end_date="today")
        bang_thoi_gian_statements.append(
            f"INSERT INTO bang_thoi_gian (nhan_vien_id, cong_viec_id, so_gio, ngay_lam) VALUES ({nhan_vien_id}, {cong_viec_id}, {so_gio}, '{ngay_lam}');"
        )

    return (
        phong_ban_statements,
        nhan_vien_statements,
        khach_hang_statements,
        du_an_statements,
        cong_viec_statements,
        bang_thoi_gian_statements,
    )

# Gọi hàm sinh dữ liệu
phong_ban, nhan_vien, khach_hang, du_an, cong_viec, bang_thoi_gian = generate_fake_data()

# Ghi dữ liệu vào file SQL
file_path = "//fake_data.sql"
with open(file_path, "w", encoding="utf-8") as f:
    f.write("-- Dữ liệu bảng phong_ban\n")
    f.writelines([stmt + "\n" for stmt in phong_ban])
    f.write("\n-- Dữ liệu bảng nhan_vien\n")
    f.writelines([stmt + "\n" for stmt in nhan_vien])
    f.write("\n-- Dữ liệu bảng khach_hang\n")
    f.writelines([stmt + "\n" for stmt in khach_hang])
    f.write("\n-- Dữ liệu bảng du_an\n")
    f.writelines([stmt + "\n" for stmt in du_an])
    f.write("\n-- Dữ liệu bảng cong_viec\n")
    f.writelines([stmt + "\n" for stmt in cong_viec])
    f.write("\n-- Dữ liệu bảng bang_thoi_gian\n")
    f.writelines([stmt + "\n" for stmt in bang_thoi_gian])

file_path

