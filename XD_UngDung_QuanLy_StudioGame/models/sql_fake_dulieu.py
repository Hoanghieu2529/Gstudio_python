from faker import Faker
import random
from datetime import datetime, timedelta

# Khởi tạo Faker với tiếng Việt
faker = Faker("vi_VN")


def generate_fake_data():
    """Tự động thêm dữ liêu cho các bảng database studio_game"""
    phong_ban_statements = []
    nhan_vien_statements = []
    khach_hang_statements = []
    du_an_statements = []
    cong_viec_statements = []
    bang_thoi_gian_statements = []

    # Tạo ánh xạ mapb -> id
    phong_ban_mapping = {}

    # Dữ liệu cho bảng phong_ban
    phong_ban_names = ["Ban Điều Hành","IT", "Nhân sự", "Tài chính", "Marketing", "Bán hàng"]
    for idx, name in enumerate(phong_ban_names, start=1):
        mapb = f"PB{str(idx).zfill(3)}"  # Tạo mã phòng ban dạng PB001, PB002, ...
        phong_ban_mapping[mapb] = idx
        phong_ban_statements.append(
            f"INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('{mapb}', '{name}', '{faker.text()}');"
        )

    # Dữ liệu cho bảng nhan_vien
    for i in range(1, 101):
        manv = 100 + i
        ho_ten = faker.name()  # Sửa tên tiếng Việt đầy đủ
        email = f"{faker.first_name().lower()}.{faker.last_name().lower()}@ms.uit.edu.vn"
        chuc_vu = random.choice(["Lập trình viên", "Quản lý", "Trưởng phòng", "Nhân viên"])

        # Chọn ngẫu nhiên một mapb từ phong_ban_mapping
        mapb = random.choice(list(phong_ban_mapping.keys()))

        if chuc_vu == "Lập trình viên":
            luong_cb = round(random.randint(12_000_000, 80_000_000), -6)
        elif chuc_vu == "Quản lý":
            luong_cb = round(random.randint(40_000_000, 80_000_000), -6)
        elif chuc_vu == "Trưởng phòng":
            luong_cb = round(random.randint(20_000_000, 60_000_000), -6)
        else:
            luong_cb = round(random.randint(8_000_000, 30_000_000), -6)

        nhan_vien_statements.append(
            f"INSERT INTO nhan_vien (manv,ho_ten, email, chuc_vu, mapb, luong_cb) "
            f"VALUES ('{manv}''{ho_ten}', '{email}', '{chuc_vu}', '{mapb}', {luong_cb});"
        )

    # Dữ liệu cho bảng khach_hang
    for i in range(1, 101):
        makh = 500 + i
        ten_khach_hang = faker.company()
        email = f"{faker.first_name().lower()}.{faker.last_name().lower()}@client.com"
        so_dien_thoai = f"+84 {random.randint(10000000, 99999999)}"  # Số điện thoại Việt Nam với đầu số +84
        dia_chi = f"{faker.street_address()}, Thành phố Hồ Chí Minh, Việt Nam"  # Địa chỉ tại TP.HCM
        khach_hang_statements.append(
            f"INSERT INTO khach_hang (makh,ten_khach_hang, email, so_dien_thoai, dia_chi) "
            f"VALUES ('{makh}','{ten_khach_hang}', '{email}', '{so_dien_thoai}', '{dia_chi}');"
        )

    # Dữ liệu cho bảng du_an
    for i in range(1, 101):
        ten_du_an = f"Dự án {i}"
        mo_ta = faker.text()
        ngay_bat_dau = faker.date_this_year().isoformat()
        ngay_ket_thuc = (datetime.strptime(ngay_bat_dau, "%Y-%m-%d") + timedelta(days=random.randint(30, 180))).date()
        khach_hang_id = random.randint(1, 100)
        du_an_statements.append(
            f"INSERT INTO du_an (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, khach_hang_id) VALUES ('{ten_du_an}', '{mo_ta}', '{ngay_bat_dau}', '{ngay_ket_thuc}', {khach_hang_id});"
        )

    # Dữ liệu cho bảng cong_viec
    for i in range(1, 101):
        ten_cong_viec = f"Công việc {i}"
        mo_ta = faker.text()
        du_an_id = random.randint(1, 100)
        giao_cho = random.randint(1, 100)
        han_chot = faker.date_between(start_date="today", end_date="+60d")
        trang_thai = random.choice(['chưa thực hiện', 'đang thực hiện', 'hoàn thành'])
        cong_viec_statements.append(
            f"INSERT INTO cong_viec (du_an_id, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUES ({du_an_id}, '{ten_cong_viec}', '{mo_ta}', {giao_cho}, '{han_chot}', '{trang_thai}');"
        )

    # Dữ liệu cho bảng bang_thoi_gian
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
file_path = "./fake_data.sql"
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

print("Dữ liệu đã được tạo và lưu vào file:", file_path)
