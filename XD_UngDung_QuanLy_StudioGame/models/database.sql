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
    luong_cb INT,
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
    email VARCHAR(250),
    vai_tro ENUM('quan_tri_vien', 'lap_trinh_vien', 'kiem_thu', 'nguoi_dung', 'vang_lai') NOT NULL,
    ngay_dang_ky DATE NOT NULL
);
--- dữ liệu phòng ban
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('001', 'Ban Điều Hành', 'Điều hành mọi hoạt động công ty');
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('002', 'IT', 'Quản lý hệ thống IT');
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('003', 'Nhân sự', 'Chính sách và phúc lợi, lương thưởng');
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('004', 'Tài chính', 'Quản lý tài chính công ty');
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('005', 'Marketing', 'Thực hiện các hành động marketing và quản lý thương hiệu');
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('006', 'Bán hàng', 'Tìm kiếm khách hàng và bán hàng');
--- dữ liệu nhân viên
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (101, 'Nguyễn Duy Hiếu', 'hieund1@ms.uit.edu.vn', 'Quản lý', '001', 22000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (102, 'Hồ Trí Quang', 'hồ.quang@ms.uit.edu.vn', 'Quản lý', '001', 79000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (103, 'Đoàn Minh Trí', 'đoàn.trí@ms.uit.edu.vn', 'Quản lý', '003', 55000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (104, 'Hồ Bảo Lâm', 'hồ.lâm@ms.uit.edu.vn', 'Trưởng phòng', '003', 40000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (105, 'Trần Thanh Trúc', 'trần.trúc@ms.uit.edu.vn', 'Trưởng phòng', '005', 52000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (106, 'Nguyễn Quang Bình', 'nguyễn.bình@ms.uit.edu.vn', 'Lập trình viên', '005', 30000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (107, 'Dương Quốc Duy', 'dương.duy@ms.uit.edu.vn', 'Quản lý', '002', 66000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (108, 'Dương Thiên Bình', 'dương.bình@ms.uit.edu.vn', 'Trưởng phòng', '004', 49000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (109, 'Đinh Minh Quang', 'đinh.quang@ms.uit.edu.vn', 'Nhân viên', '005', 10000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (110, 'Bùi Thiên Phát', 'bùi.phát@ms.uit.edu.vn', 'Trưởng phòng', '001', 46000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (111, 'Phan Minh Thảo', 'phan.thảo@ms.uit.edu.vn', 'Nhân viên', '005', 28000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (112, 'Phan Quang Huy', 'phan.huy@ms.uit.edu.vn', 'Nhân viên', '005', 23000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (113, 'Lê Minh Hùng', 'lê.hùng@ms.uit.edu.vn', 'Lập trình viên', '002', 21000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (114, 'Lê Quang Tâm', 'lê.tâm@ms.uit.edu.vn', 'Quản lý', '006', 46000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (115, 'Lê Thị Ánh', 'lê.ánh@ms.uit.edu.vn', 'Trưởng phòng', '003', 41000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (116, 'Bùi Thanh Tuyền', 'bùi.tuyền@ms.uit.edu.vn', 'Quản lý', '003', 60000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (117, 'Nguyễn Minh Cường', 'nguyễn.cường@ms.uit.edu.vn', 'Trưởng phòng', '004', 36000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (118, 'Đoàn Quốc Tường', 'đoàn.tường@ms.uit.edu.vn', 'Nhân viên', '003', 28000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (119, 'Bùi Thị Lan Anh', 'bùi.anh@ms.uit.edu.vn', 'Lập trình viên', '003', 14000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (120, 'Lê Đức Tuấn', 'lê.tuấn@ms.uit.edu.vn', 'Lập trình viên', '005', 18000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (121, 'Trần Kim Tiến', 'trần.tiến@ms.uit.edu.vn', 'Nhân viên', '002', 27000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (122, 'Trương Thị Mai', 'trương.mai@ms.uit.edu.vn', 'Lập trình viên', '005', 60000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (123, 'Đinh Thiên Phúc', 'đinh.phúc@ms.uit.edu.vn', 'Nhân viên', '006', 28000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (124, 'Trần Thiên Phúc', 'trần.phúc@ms.uit.edu.vn', 'Quản lý', '001', 75000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (125, 'Lê Thiết Phúc', 'lê.phúc@ms.uit.edu.vn', 'Quản lý', '005', 49000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (126, 'Trần Minh Nhật', 'trần.nhật@ms.uit.edu.vn', 'Nhân viên', '004', 16000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (127, 'Trương Thị Lan', 'trương.lan@ms.uit.edu.vn', 'Quản lý', '003', 76000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (128, 'Trần Thanh Hằng', 'trần.hằng@ms.uit.edu.vn', 'Quản lý', '006', 78000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (129, 'Lê Thanh Bình', 'lê.bình@ms.uit.edu.vn', 'Quản lý', '005', 62000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (130, 'Vũ Minh Tuấn', 'vũ.tuấn@ms.uit.edu.vn', 'Lập trình viên', '001', 73000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (131, 'Vũ Thi Thiên', 'vũ.thiên@ms.uit.edu.vn', 'Quản lý', '003', 78000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (132, 'Trương Kim Ngọc', 'trương.ngọc@ms.uit.edu.vn', 'Quản lý', '005', 67000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (133, 'Dương Thiên Phát', 'dương.phát@ms.uit.edu.vn', 'Quản lý', '005', 44000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (134, 'Nguyễn Quang Đại', 'nguyễn.đại@ms.uit.edu.vn', 'Lập trình viên', '005', 79000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (135, 'Vũ Thị Bảo Ngọc', 'vũ.ngọc@ms.uit.edu.vn', 'Trưởng phòng', '006', 44000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (136, 'Lê Minh Hoàng', 'lê.hoàng@ms.uit.edu.vn', 'Nhân viên', '002', 9000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (138, 'Dương Thị Thanh Hằng', 'dương.hằng@ms.uit.edu.vn', 'Quản lý', '006', 48000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (139, 'Nguyễn Tiến An', 'nguyễn.an@ms.uit.edu.vn', 'Nhân viên', '004', 29000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (140, 'Lê Quang Lâm', 'lê.lâm@ms.uit.edu.vn', 'Lập trình viên', '001', 37000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (141, 'Nguyễn Thái Hòa', 'nguyễn.hòa@ms.uit.edu.vn', 'Lập trình viên', '005', 27000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (143, 'Lê Thị Thu Trang', 'lê.trang@ms.uit.edu.vn', 'Trưởng phòng', '005', 40000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (144, 'Lê Hoàng Thiên', 'lê.thiên@ms.uit.edu.vn', 'Quản lý', '002', 63000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (145, 'Trần Quang Minh', 'trần.minh@ms.uit.edu.vn', 'Trưởng phòng', '003', 22000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (146, 'Nguyễn Tất Hùng', 'nguyễn.hùng@ms.uit.edu.vn', 'Quản lý', '005', 53000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (147, 'Trần Ngọc Hòa', 'trần.hòa@ms.uit.edu.vn', 'Nhân viên', '006', 22000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (148, 'Nguyễn Thành Tân', 'nguyễn.tân@ms.uit.edu.vn', 'Quản lý', '006', 75000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (149, 'Nguyễn Hùng Quân', 'nguyễn.quân@ms.uit.edu.vn', 'Trưởng phòng', '004', 27000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (150, 'Vũ Thị Kim Lan', 'vũ.lan@ms.uit.edu.vn', 'Nhân viên', '005', 28000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (151, 'Lê Minh Tiến', 'lê.tiến@ms.uit.edu.vn', 'Trưởng phòng', '004', 39000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (152, 'Dương Minh Tài', 'dương.tài@ms.uit.edu.vn', 'Lập trình viên', '003', 68000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (153, 'Lâm Hữu Tín', 'lâm.tín@ms.uit.edu.vn', 'Lập trình viên', '006', 66000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (154, 'Vũ Tiến Khánh', 'vũ.khánh@ms.uit.edu.vn', 'Nhân viên', '004', 30000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (155, 'Nguyễn Thiệt Duy', 'nguyễn.duy@ms.uit.edu.vn', 'Quản lý', '005', 51000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (156, 'Trần Quang Đoàn', 'trần.đoàn@ms.uit.edu.vn', 'Quản lý', '006', 68000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (157, 'Dương Thiên Tuấn', 'dương.tuấn@ms.uit.edu.vn', 'Lập trình viên', '001', 38000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (158, 'Trương Quốc Thiện', 'trương.thiện@ms.uit.edu.vn', 'Lập trình viên', '006', 20000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (159, 'Phạm Thiên Hoàng', 'phạm.hoàng@ms.uit.edu.vn', 'Quản lý', '005', 74000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (160, 'Phạm Duy Khoa', 'phạm.khoa@ms.uit.edu.vn', 'Trưởng phòng', '005', 45000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (161, 'Đinh Quang Linh', 'đinh.linh@ms.uit.edu.vn', 'Lập trình viên', '005', 16000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (162, 'Lê Quang Minh', 'lê.minh@ms.uit.edu.vn', 'Lập trình viên', '001', 57000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (163, 'Trương Quốc Duy', 'trương.duy@ms.uit.edu.vn', 'Trưởng phòng', '004', 43000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (164, 'Trần Tấn Phát', 'trần.phát@ms.uit.edu.vn', 'Nhân viên', '003', 17000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (165, 'Nguyễn Duy Hiếu', 'nguyễn.hiếu@ms.uit.edu.vn', 'Trưởng phòng', '003', 28000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (167, 'Bùi Anh Đức', 'bùi.đức@ms.uit.edu.vn', 'Lập trình viên', '002', 51000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (169, 'Nguyễn Văn Lộc', 'nguyễn.lộc@ms.uit.edu.vn', 'Quản lý', '004', 41000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (170, 'Phan Minh Khoa', 'phan.khoa@ms.uit.edu.vn', 'Quản lý', '006', 71000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (171, 'Trần Thị Kim Hạnh', 'trần.hạnh@ms.uit.edu.vn', 'Quản lý', '005', 51000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (172, 'Nguyễn Minh Bảo', 'nguyễn.bảo@ms.uit.edu.vn', 'Quản lý', '002', 74000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (173, 'Trần Minh Tín', 'trần.tín@ms.uit.edu.vn', 'Lập trình viên', '006', 44000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (174, 'Nguyễn Thị Thanh Lan', 'nguyễn.lan@ms.uit.edu.vn', 'Lập trình viên', '006', 17000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (175, 'Nguyễn Anh Khoa', 'nguyễn.khoa@ms.uit.edu.vn', 'Nhân viên', '001', 23000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (177, 'Trương Hoàng Sơn', 'trương.sơn@ms.uit.edu.vn', 'Trưởng phòng', '006', 38000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (178, 'Bùi Thiết Hòa', 'bùi.hòa@ms.uit.edu.vn', 'Quản lý', '006', 67000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (179, 'Phạm Minh Quang', 'phạm.quang@ms.uit.edu.vn', 'Lập trình viên', '003', 74000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (180, 'Trần Minh Lộc', 'trần.lộc@ms.uit.edu.vn', 'Quản lý', '004', 77000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (182, 'Nguyễn Minh Khang', 'nguyễn.khang@ms.uit.edu.vn', 'Quản lý', '005', 46000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (183, 'Nguyễn Thị Quỳnh', 'nguyễn.quỳnh@ms.uit.edu.vn', 'Nhân viên', '002', 14000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (184, 'Nguyễn Hoàng Nam', 'nguyễn.nam@ms.uit.edu.vn', 'Trưởng phòng', '002', 24000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (185, 'Lê Hoàng Long', 'lê.long@ms.uit.edu.vn', 'Nhân viên', '006', 25000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (186, 'Võ Thị Bích Ngọc', 'võ.ngọc@ms.uit.edu.vn', 'Quản lý', '002', 72000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (187, 'Lê Thanh Hương', 'lê.hương@ms.uit.edu.vn', 'Trưởng phòng', '006', 42000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (188, 'Đinh Minh Thanh', 'đinh.thanh@ms.uit.edu.vn', 'Quản lý', '004', 59000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (189, 'Bùi Thị Bảo Ngọc', 'bùi.ngọc@ms.uit.edu.vn', 'Lập trình viên', '003', 25000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (190, 'Hồ Thị Kim Anh', 'hồ.anh@ms.uit.edu.vn', 'Lập trình viên', '002', 53000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (191, 'Vũ Minh Phú', 'vũ.phú@ms.uit.edu.vn', 'Trưởng phòng', '002', 23000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (192, 'Nguyễn Anh Đức', 'nguyễn.đức@ms.uit.edu.vn', 'Trưởng phòng', '001', 46000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (193, 'Trương Minh Hoàng', 'trương.hoàng@ms.uit.edu.vn', 'Lập trình viên', '006', 40000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (194, 'Đoàn Đình Ngọc', 'đoàn.ngọc@ms.uit.edu.vn', 'Lập trình viên', '001', 27000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (195, 'Vũ Tiến Hoàng', 'vũ.hoàng@ms.uit.edu.vn', 'Quản lý', '005', 50000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (196, 'Nguyễn Ngọc Tâm', 'nguyễn.tâm@ms.uit.edu.vn', 'Quản lý', '001', 72000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (197, 'Hồ Thanh Sơn', 'hồ.sơn@ms.uit.edu.vn', 'Lập trình viên', '002', 28000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (198, 'Phan Thị Minh', 'phan.minh@ms.uit.edu.vn', 'Trưởng phòng', '005', 29000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (199, 'Trần Minh Châu', 'trần.châu@ms.uit.edu.vn', 'Lập trình viên', '005', 56000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (200, 'Phạm Duy Linh', 'phạm.linh@ms.uit.edu.vn', 'Lập trình viên', '004', 59000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (201, 'Đoàn Thiết Sơn', 'đoàn.sơn@ms.uit.edu.vn', 'Lập trình viên', '002', 73000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (202, 'Nguyễn Minh Tiến', 'nguyễn.tiến@ms.uit.edu.vn', 'Lập trình viên', '006', 22000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (204, 'Bùi Thị Quỳnh Như', 'bùi.như@ms.uit.edu.vn', 'Lập trình viên', '003', 75000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (205, 'Nguyễn Thanh Vũ', 'nguyễn.vũ@ms.uit.edu.vn', 'Lập trình viên', '005', 24000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (207, 'Lê Hoàng Nhật', 'lê.nhật@ms.uit.edu.vn', 'Trưởng phòng', '004', 59000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (209, 'Lê Anh Tín', 'lê.tín@ms.uit.edu.vn', 'Trưởng phòng', '001', 56000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (211, 'Nguyễn Thanh Trúc', 'nguyễn.trúc@ms.uit.edu.vn', 'Trưởng phòng', '001', 48000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (212, 'Hồ Minh Kỳ', 'hồ.kỳ@ms.uit.edu.vn', 'Nhân viên', '004', 29000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (213, 'Nguyễn Thị Khánh', 'nguyễn.khánh@ms.uit.edu.vn', 'Lập trình viên', '002', 49000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (214, 'Nguyễn Quang Huy', 'nguyễn.huy@ms.uit.edu.vn', 'Lập trình viên', '005', 31000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (215, 'Phan Hữu Khánh', 'phan.khánh@ms.uit.edu.vn', 'Trưởng phòng', '006', 42000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (216, 'Trương Quốc Lâm', 'trương.lâm@ms.uit.edu.vn', 'Lập trình viên', '001', 22000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (217, 'Dương Minh Tân', 'dương.tân@ms.uit.edu.vn', 'Lập trình viên', '004', 79000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (218, 'Lê Minh Hải', 'lê.hải@ms.uit.edu.vn', 'Trưởng phòng', '006', 58000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (219, 'Trần Hoàng Đức', 'trần.đức@ms.uit.edu.vn', 'Lập trình viên', '004', 60000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (220, 'Lê Hoàng Sơn', 'lê.sơn@ms.uit.edu.vn', 'Nhân viên', '004', 9000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (221, 'Trần Thiên Hải', 'trần.hải@ms.uit.edu.vn', 'Trưởng phòng', '004', 20000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (222, 'Lâm Anh Tuấn', 'lâm.tuấn@ms.uit.edu.vn', 'Trưởng phòng', '001', 38000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (224, 'Lê Thanh Duy', 'lê.duy@ms.uit.edu.vn', 'Nhân viên', '003', 13000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (225, 'Đoàn Quốc Duy', 'đoàn.duy@ms.uit.edu.vn', 'Quản lý', '001', 73000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (226, 'Lê Quốc Đạt', 'lê.đạt@ms.uit.edu.vn', 'Trưởng phòng', '003', 30000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (227, 'Nguyễn Anh Minh', 'nguyễn.minh@ms.uit.edu.vn', 'Trưởng phòng', '001', 46000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (228, 'Phan Minh Quang', 'phan.quang@ms.uit.edu.vn', 'Lập trình viên', '002', 46000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (229, 'Vũ Hải Dương', 'vũ.dương@ms.uit.edu.vn', 'Lập trình viên', '003', 26000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (230, 'Vũ Minh Nhật', 'vũ.nhật@ms.uit.edu.vn', 'Trưởng phòng', '002', 48000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (231, 'Đinh Tuấn Kiệt', 'đinh.kiệt@ms.uit.edu.vn', 'Quản lý', '003', 49000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (232, 'Trương Minh Huy', 'trương.huy@ms.uit.edu.vn', 'Trưởng phòng', '004', 44000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (233, 'Đoàn Thị Phương', 'đoàn.phương@ms.uit.edu.vn', 'Trưởng phòng', '004', 57000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (234, 'Hồ Thị Ngọc Định', 'hồ.định@ms.uit.edu.vn', 'Quản lý', '003', 65000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (235, 'Phan Thành Nhân', 'phan.nhân@ms.uit.edu.vn', 'Nhân viên', '002', 26000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (237, 'Dương Hữu Khoa', 'dương.khoa@ms.uit.edu.vn', 'Nhân viên', '006', 27000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (238, 'Vũ Thiện Quang', 'vũ.quang@ms.uit.edu.vn', 'Trưởng phòng', '003', 44000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (239, 'Phan Ngọc Tú', 'phan.tú@ms.uit.edu.vn', 'Nhân viên', '001', 29000000);

select * from nhan_vien

---dữ liệu nguời dùng
INSERT INTO nguoi_dung (mand, ten_dang_nhap, mat_khau, email, vai_tro, ngay_dang_ky) VALUES
(241201, 'hieund', '123', 'hieund@studio', 'quan_tri_vien', '2023-12-10'),
(241202, 'ducna', '123', 'duc@studio', 'lap_trinh_vien', '2023-12-12'),
(241203, 'dinhhtn', '123', 'dinh@studio', 'kiem_thu', '2023-12-15'),
(241204, 'nguyenvan', '123', 'nguoidung@gmail', 'nguoi_dung', '2023-12-20'),
(241205, 'vuhieu9a', '123', 'vuhieu9a@gmail.com', 'lap_trinh_vien', '2023-07-15'),
(241206, 'pzro5bp6', '123', 'pzro5bp6@gmail.com', 'lap_trinh_vien', '2023-10-25'),
(241207, 'lz7au9zx', '123', 'lz7au9zx@gmail.com', 'lap_trinh_vien', '2023-08-14'),
(241208, 'p2nk7uq5', '123', 'p2nk7uq5@gmail.com', 'lap_trinh_vien', '2023-03-11'),
(241209, 'fzp6hl2b', '123', 'fzp6hl2b@gmail.com', 'nguoi_dung', '2023-09-05'),
(241210, 'n1vqhwla', '123', 'n1vqhwla@gmail.com', 'nguoi_dung', '2023-02-18'),
(241211, 'twos7cf8', '123', 'twos7cf8@gmail.com', 'nguoi_dung', '2023-05-25');

--- dữ liệu khách hàng
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Mai Khánh Toàn', 'mai.khánh.toàn@example.com', '0923456789', 'Đà Nẵng, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Ngô Minh Tuấn', 'ngô.minh.tuấn@example.com', '0934567890', 'Bình Dương, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Nguyễn Hoàng Lộc', 'nguyễn.hoàng.lộc@example.com', '0967890123', 'Hà Nội, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Trần Hải Minh', 'trần.hải.minh@example.com', '0978901234', 'Vũng Tàu, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Bùi Anh Dũng', 'bùi.anh.dũng@example.com', '0990123456', 'Hải Phòng, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Lý Thị Lan', 'lý.thị.lan@example.com', '0990123456', 'Hà Nội, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Đoàn Hữu Đức', 'đoàn.hữu.đức@example.com', '0901234567', 'Hải Phòng, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Vũ Lan Anh', 'vũ.lan.anh@example.com', '0945678901', 'Đà Nẵng, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Phạm Hoàng Duy', 'phạm.hoàng.duy@example.com', '0945678901', 'Cần Thơ, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Bùi Lan Anh', 'bùi.lan.anh@example.com', '0967890123', 'Hồ Chí Minh, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Trần Hữu Tâm', 'trần.hữu.tâm@example.com', '0978901234', 'Hải Phòng, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Nguyễn Văn An', 'nguyễn.văn.an@example.com', '0990123456', 'Vũng Tàu, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Hồ Thị Hoa', 'hồ.thị.hoa@example.com', '0934567890', 'Lào Cai, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Trần Thị Bình', 'trần.thị.bình@example.com', '0989012345', 'Cần Thơ, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Nguyễn Hoàng Hải', 'nguyễn.hoàng.hải@example.com', '0990123456', 'Nha Trang, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Mai Khánh Hòa', 'mai.khánh.hòa@example.com', '0923456789', 'Hà Nội, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Lê Quang Sơn', 'lê.quang.sơn@example.com', '0912345678', 'Hà Nội, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Ngô Minh Quân', 'ngô.minh.quân@example.com', '0990123456', 'Đà Nẵng, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Lê Minh Cường', 'lê.minh.cường@example.com', '0945678901', 'Cần Thơ, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Nguyễn Thị Lan', 'nguyễn.thị.lan@example.com', '0989012345', 'Cần Thơ, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Phạm Bình Lộc', 'phạm.bình.lộc@example.com', '0967890123', 'Đà Nẵng, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Đoàn Hữu Tiến', 'đoàn.hữu.tiến@example.com', '0934567890', 'Vũng Tàu, Việt Nam');
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES ('Lê Tuấn Kiệt', 'lê.tuấn.kiệt@example.com', '0934567890', 'Vũng Tàu, Việt Nam');


select * from khach_hang

--- dữ liệu dự án
INSERT INTO du_an (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh) VALUES ('Baldur''s Gate 3', 'Một tựa game nhập vai nổi bật với thế giới mở phong phú và lối chơi đỉnh cao.', '2024-01-15', '2024-06-30', 1);
INSERT INTO du_an (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh) VALUES ('The Legend of Zelda: Tears of the Kingdom', 'Một cuộc phiêu lưu kỳ thú với lối chơi sáng tạo và đồ họa tuyệt đẹp.', '2024-03-01', '2024-09-15', 2);
INSERT INTO du_an (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh) VALUES ('Starfield', 'Trò chơi phiêu lưu không gian với hàng nghìn hành tinh để khám phá.', '2024-04-20', '2024-10-10', 3);
INSERT INTO du_an (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh) VALUES ('Diablo IV', 'Hành trình chống lại quỷ dữ trong một thế giới tối tăm và đầy nguy hiểm.', '2024-02-25', '2024-07-20', 4);
INSERT INTO du_an (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh) VALUES ('Final Fantasy XVI', 'Một câu chuyện sử thi kết hợp với lối chơi hành động độc đáo.', '2024-03-15', '2024-08-30', 6);
INSERT INTO du_an (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh) VALUES ('Resident Evil 4 Remake', 'Phiên bản làm lại của tựa game kinh dị nổi tiếng, với đồ họa và cơ chế cải tiến.', '2024-02-01', '2024-07-15', 7);
INSERT INTO du_an (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh) VALUES ('Cyberpunk 2077: Phantom Liberty', 'Bản mở rộng đầy hứa hẹn của tựa game Cyberpunk 2077.', '2024-05-10', '2024-10-20', 8);
INSERT INTO du_an (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh) VALUES ('Armored Core VI: Fires of Rubicon', 'Trải nghiệm lái robot chiến đấu trong những trận chiến khốc liệt.', '2024-06-01', '2024-11-15', 9);
INSERT INTO du_an (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh) VALUES ('Assassin''s Creed Mirage', 'Quay trở lại với cốt truyện sát thủ truyền thống trong thế giới Trung Đông.', '2024-07-05', '2024-12-01', 10);

--- dữ liệu công việc
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUES(1, 1, 'Thiết kế nhân vật', 'Thiết kế các nhân vật trong game Baldur''s Gate 3', 106, '2024-02-15', 'dang_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (2, 1, 'Lập trình gameplay', 'Phát triển cơ chế gameplay cho Baldur''s Gate 3', 107, '2024-03-01', 'chua_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (3, 1, 'Kiểm tra chất lượng', 'Kiểm tra chất lượng cho Baldur''s Gate 3', 124, '2024-02-20', 'chua_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (4, 1, 'Tạo trailer', 'Tạo trailer cho Baldur''s Gate 3', 125, '2024-03-10', 'dang_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (5, 2, 'Thiết kế giao diện', 'Thiết kế giao diện người dùng cho The Legend of Zelda: Tears of the Kingdom', 126, '2024-05-15', 'chua_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (6, 2, 'Phát triển âm thanh', 'Phát triển âm thanh cho The Legend of Zelda: Tears of the Kingdom', 127, '2024-04-25', 'dang_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (7, 2, 'Viết kịch bản', 'Viết kịch bản cho The Legend of Zelda: Tears of the Kingdom', 128, '2024-04-10', 'chua_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (8, 2, 'Thiết kế nhân vật', 'Thiết kế nhân vật cho The Legend of Zelda: Tears of the Kingdom', 129, '2024-05-20', 'chua_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (9, 3, 'Lập trình mạng', 'Phát triển tính năng mạng cho Starfield', 111, '2024-06-15', 'chua_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (10, 3, 'Thiết kế nhân vật phụ', 'Thiết kế nhân vật phụ cho Starfield', 153, '2024-07-10', 'dang_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (11, 3, 'Tạo nội dung', 'Tạo nội dung cho Starfield', 169, '2024-06-30', 'chua_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (12, 3, 'Kiểm tra bug', 'Kiểm tra bug cho Starfield', 134, '2024-07-20', 'dang_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (13, 4, 'Tạo nội dung', 'Tạo nội dung cho Diablo IV', 184, '2024-03-30', 'chua_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (14, 4, 'Kiểm tra bug', 'Kiểm tra bug cho Diablo IV', 200, '2024-05-25', 'dang_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (15, 4, 'Thiết kế âm thanh', 'Thiết kế âm thanh cho Diablo IV', 185, '2024-04-15', 'chua_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (16, 4, 'Lập trình gameplay', 'Phát triển gameplay cho Diablo IV', 143, '2024-05-10', 'dang_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (17, 6, 'Thiết kế môi trường', 'Thiết kế môi trường cho Final Fantasy XVI', 138, '2024-04-15', 'chua_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (18, 6, 'Lập trình hệ thống', 'Phát triển hệ thống cho Final Fantasy XVI', 139, '2024-06-20', 'dang_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (19, 6, 'Viết kịch bản', 'Viết kịch bản cho Final Fantasy XVI', 140, '2024-05-30', 'chua_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (20, 6, 'Thiết kế nhân vật', 'Thiết kế nhân vật cho Final Fantasy XVI', 141, '2024-06-10', 'dang_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (21, 7, 'Phát triển AI', 'Phát triển AI cho Resident Evil 4 Remake', 144, '2024-03-15', 'chua_thuc_hien');
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai) VALUE (22, 7, 'Thiết kế nhân vật', 'Thiết kế nhân vật cho Resident Evil 4 Remake', 143, '2024-04-05', 'dang_thuc_hien');

--- dữ liệu bảng thời gian
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (1, 106, 1, 8, '2024-01-10');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (2, 107, 2, 6, '2024-01-11');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (3, 108, 3, 7, '2024-01-12');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (4, 109, 4, 5, '2024-01-13');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (5, 106, 5, 8, '2024-01-14');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (6, 107, 6, 6, '2024-01-15');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (7, 108, 7, 7, '2024-01-16');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (8, 109, 8, 5, '2024-01-17');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (9, 106, 9, 8, '2024-01-18');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (10, 107, 10, 6, '2024-01-19');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (11, 108, 11, 7, '2024-01-20');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (12, 109, 12, 5, '2024-01-21');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (13, 106, 13, 8, '2024-01-22');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (14, 107, 14, 6, '2024-01-23');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (15, 108, 15, 7, '2024-01-24');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (16, 109, 16, 5, '2024-01-25');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (17, 106, 17, 8, '2024-01-26');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (18, 107, 18, 6, '2024-01-27');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (19, 108, 19, 7, '2024-01-28');
INSERT INTO bang_thoi_gian (matg, manv, macv, so_gio, ngay_lam) VALUES (20, 109, 20, 5, '2024-01-29');



