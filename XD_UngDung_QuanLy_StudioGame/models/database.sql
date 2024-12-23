CREATE TABLE phong_ban (
    mapb INT PRIMARY KEY,
    ten_phong_ban VARCHAR(100) NOT NULL,
    mo_ta TEXT
);

CREATE TABLE nhan_vien (
    manv INT PRIMARY KEY,
    ho_ten VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    chuc_vu VARCHAR(50),
    mapb INT,
    luong_cb int,
    FOREIGN KEY (mapb) REFERENCES phong_ban(mapb)
);

CREATE TABLE khach_hang (
    makh INT AUTO_INCREMENT PRIMARY KEY,
    ten_khach_hang VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    so_dien_thoai VARCHAR(15),
    dia_chi TEXT
);

CREATE TABLE du_an (
    mada INT AUTO_INCREMENT PRIMARY KEY,
    ten_du_an VARCHAR(100) NOT NULL,
    mo_ta TEXT,
    ngay_bat_dau DATE NOT NULL,
    ngay_ket_thuc DATE NOT NULL,
    makh INT,
    FOREIGN KEY (makh) REFERENCES khach_hang(makh)
);

CREATE TABLE cong_viec (
    macv INT PRIMARY KEY,
    mada INT,
    ten_cong_viec VARCHAR(100) NOT NULL,
    mo_ta TEXT,
    giao_cho INT,
    han_chot DATE NOT NULL,
    trang_thai ENUM('chua_thuc_hien', 'dang_thuc_hien', 'hoan_thanh') DEFAULT 'chua_thuc_hien',
    FOREIGN KEY (mada) REFERENCES du_an(mada),
    FOREIGN KEY (giao_cho) REFERENCES nhan_vien(manv)
);

CREATE TABLE bang_thoi_gian (
    matg INT PRIMARY KEY,
    manv INT,
    macv INT,
    so_gio INT NOT NULL,
    ngay_lam DATE NOT NULL,
    FOREIGN KEY (manv) REFERENCES nhan_vien(manv),
    FOREIGN KEY (macv) REFERENCES cong_viec(macv)
);
CREATE TABLE nguoi_dung (
    mand INT PRIMARY KEY,
    ten_dang_nhap VARCHAR(50) NOT NULL UNIQUE,
    mat_khau VARCHAR(255) NOT NULL,
    vai_tro ENUM('quan tri vien', 'lap trinh vien', 'kiem thu','nguoi dung') NOT NULL
);

-- Dữ liệu bảng phong_ban
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('001', 'Ban Điều Hành', 'Điều hành mọi hoạt động công ty');
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('002', 'IT', 'Quản lý hệ thống IT');
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('003', 'Nhân sự', 'Chính sách và phúc lợi, lương thưởng');
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('004', 'Tài chính', 'Quản lý tài chính công ty');
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('005', 'Marketing', 'Thực hiện các hành động marketing và quản lý thương hiệu');
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('006', 'Bán hàng', 'Tìm kiếm khách hàng và bán hàng');

-- Du liệu bảng nhân vien
INSERT INTO nhan_vien (manv, email, chuc_vu, mapb) VALUES (100,'Nguyễn Duy Hiếu', '23210111@ms.uit.edu.vn', 'Chủ tịch', 001);
INSERT INTO nhan_vien (manv, email, chuc_vu, mapb) VALUES (101,'Nguyễn Anh Đức', '23210102@ms.uit.edu.vn', 'Giám đốc', 001);
INSERT INTO nhan_vien (manv, email, chuc_vu, mapb) VALUES (102,'Hồ Thị Ngọc Định', '23210099@ms.uit.edu.vn', 'Phó giám đốc', 001);

-- Dữ liệu bảng người dùng
INSERT INTO nguoi_dung (mand, ten_dang_nhap,mat_khau,vai_tro) VALUES (241201,'hieund',123,'quan tri vien');
INSERT INTO nguoi_dung (mand, ten_dang_nhap,mat_khau,vai_tro) VALUES (241202,'ducna',123,'lap trinh vien');
INSERT INTO nguoi_dung (mand, ten_dang_nhap,mat_khau,vai_tro) VALUES (241203,'dinhhtn',123,'kiem thu');
INSERT INTO nguoi_dung (mand, ten_dang_nhap,mat_khau,vai_tro) VALUES (241204, 'nguyenvan', 123, 'nguoi dung');
-- Dữ liệu bảng dự án # manv tự động thêm từ 1 đén 100
INSERT INTO du_an (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh) VALUES
('Baldur\'s Gate 3', 'Một tựa game nhập vai nổi bật với thế giới mở phong phú và lối chơi đỉnh cao.', '2024-01-15', '2024-06-30', 1),
('The Legend of Zelda: Tears of the Kingdom', 'Một cuộc phiêu lưu kỳ thú với lối chơi sáng tạo và đồ họa tuyệt đẹp.', '2024-03-01', '2024-09-15', 2),
('Starfield', 'Trò chơi phiêu lưu không gian với hàng nghìn hành tinh để khám phá.', '2024-04-20', '2024-10-10', 3),
('Diablo IV', 'Hành trình chống lại quỷ dữ trong một thế giới tối tăm và đầy nguy hiểm.', '2024-02-25', '2024-07-20', 4),
('Hogwarts Legacy', 'Trải nghiệm thế giới phù thủy tại trường Hogwarts với nhiều điều kỳ diệu.', '2024-01-10', '2024-06-05', 5),
('Final Fantasy XVI', 'Một câu chuyện sử thi kết hợp với lối chơi hành động độc đáo.', '2024-03-15', '2024-08-30', 6),
('Resident Evil 4 Remake', 'Phiên bản làm lại của tựa game kinh dị nổi tiếng, với đồ họa và cơ chế cải tiến.', '2024-02-01', '2024-07-15', 7),
('Cyberpunk 2077: Phantom Liberty', 'Bản mở rộng đầy hứa hẹn của tựa game Cyberpunk 2077.', '2024-05-10', '2024-10-20', 8),
('Armored Core VI: Fires of Rubicon', 'Trải nghiệm lái robot chiến đấu trong những trận chiến khốc liệt.', '2024-06-01', '2024-11-15', 9),
('Assassin\'s Creed Mirage', 'Quay trở lại với cốt truyện sát thủ truyền thống trong thế giới Trung Đông.', '2024-07-05', '2024-12-01', 10);
