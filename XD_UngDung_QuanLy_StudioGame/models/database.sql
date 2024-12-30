CREATE TABLE nguoi_dung (
    mand INT PRIMARY KEY,
    ten_dang_nhap VARCHAR(50) NOT NULL UNIQUE,
    mat_khau VARCHAR(255) NOT NULL,
    email VARCHAR(250),
    vai_tro ENUM('quan tri vien', 'lap trinh vien', 'kiem thu','nguoi dung') NOT NULL,
    ngay_dang_ky DATE,
    ghi_nho TINYINT(1) DEFAULT 0
);

INSERT INTO nguoi_dung (mand, ten_dang_nhap,mat_khau,email,vai_tro,ngay_dang_ky) VALUES (241201,'hieund',123, '23210111@ms.uit.edu.vn','quan tri vien','2024-09-01');
INSERT INTO nguoi_dung (mand, ten_dang_nhap,mat_khau,email,vai_tro,ngay_dang_ky) VALUES (241202,'ducna',123,'23210102@ms.uit.edu.vn','lap trinh vien','2024-10-02');
INSERT INTO nguoi_dung (mand, ten_dang_nhap,mat_khau,email,vai_tro,ngay_dang_ky) VALUES (241203,'dinhhtn',123,'23210099@ms.uit.edu.vn','kiem thu','2024-11-03');
INSERT INTO nguoi_dung (mand, ten_dang_nhap,mat_khau,email,vai_tro,ngay_dang_ky) VALUES (241204,'nhanvien',123,'tknhanvien@ms.uit.edu.vn','nguoi dung','2024-12-01');

select * from nguoi_dung;




CREATE TABLE phong_ban (
                           mapb INT PRIMARY KEY,
                           ten_phong_ban VARCHAR(100) NOT NULL,
                           mo_ta TEXT
);
-- Dữ liệu bảng phong_ban
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('001', 'Ban Điều Hành', 'Điều hành mọi hoạt động công ty');
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('002', 'IT', 'Quản lý hệ thống IT');
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('003', 'Nhân sự', 'Chính sách và phúc lợi, lương thưởng');
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('004', 'Tài chính', 'Quản lý tài chính công ty');
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('005', 'Marketing', 'Thực hiện các hành động marketing và quản lý thương hiệu');
INSERT INTO phong_ban (mapb, ten_phong_ban, mo_ta) VALUES ('006', 'Bán hàng', 'Tìm kiếm khách hàng và bán hàng');

CREATE TABLE nhan_vien (
   manv INT PRIMARY KEY,
   ho_ten VARCHAR(100) NOT NULL,
   email VARCHAR(100) UNIQUE NOT NULL,
   chuc_vu VARCHAR(50),
   mapb INT,
   luong_cb INT
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
               trang_thai VARCHAR(50)
);

CREATE TABLE cong_viec (
                           macv INT PRIMARY KEY,
                           mada INT,
                           ten_cong_viec VARCHAR(100) NOT NULL,
                           mo_ta TEXT,
                           giao_cho INT,
                           han_chot DATE NOT NULL,
                           trang_thai ENUM('chua_thuc_hien', 'dang_thuc_hien', 'hoan_thanh') DEFAULT 'chua_thuc_hien'
);

CREATE TABLE bang_cong (
                           mabc INT PRIMARY KEY,
                           manv INT,
                           macv INT,
                           so_gio INT NOT NULL,
                           ngay_lam DATE NOT NULL,
                           so_luong_san_pham INT
);

-- Thêm khóa ngoại cho bảng nhan_vien liên kết với bảng phong_ban
ALTER TABLE nhan_vien
    ADD CONSTRAINT fk_nhan_vien_phong_ban
        FOREIGN KEY (mapb) REFERENCES phong_ban(mapb);

-- Thêm khóa ngoại cho bảng du_an liên kết với bảng khach_hang
ALTER TABLE du_an
    ADD CONSTRAINT fk_du_an_khach_hang
        FOREIGN KEY (makh) REFERENCES khach_hang(makh);

-- Thêm khóa ngoại cho bảng cong_viec liên kết với bảng du_an
ALTER TABLE cong_viec
    ADD CONSTRAINT fk_cong_viec_du_an
        FOREIGN KEY (mada) REFERENCES du_an(mada);

-- Thêm khóa ngoại cho bảng cong_viec liên kết với bảng nhan_vien
ALTER TABLE cong_viec
    ADD CONSTRAINT fk_cong_viec_nhan_vien
        FOREIGN KEY (giao_cho) REFERENCES nhan_vien(manv);

-- Thêm khóa ngoại cho bảng bang_cong liên kết với bảng nhan_vien
ALTER TABLE bang_cong
    ADD CONSTRAINT fk_bang_cong_nhan_vien
        FOREIGN KEY (manv) REFERENCES nhan_vien(manv);

-- Thêm khóa ngoại cho bảng bang_cong liên kết với bảng cong_viec
ALTER TABLE bang_cong
    ADD CONSTRAINT fk_bang_cong_cong_viec
        FOREIGN KEY (macv) REFERENCES cong_viec(macv);



-- Du liệu bảng nhân vien
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
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (137, 'Lê Thị Lan Anh', 'anhltl@ms.uit.edu.vn', 'Lập trình viên', '004', 28000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (138, 'Dương Thị Thanh Hằng', 'dương.hằng@ms.uit.edu.vn', 'Quản lý', '006', 48000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (139, 'Nguyễn Tiến An', 'nguyễn.an@ms.uit.edu.vn', 'Nhân viên', '004', 29000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (140, 'Lê Quang Lâm', 'lê.lâm@ms.uit.edu.vn', 'Lập trình viên', '001', 37000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (141, 'Nguyễn Thái Hòa', 'nguyễn.hòa@ms.uit.edu.vn', 'Lập trình viên', '005', 27000000);
INSERT INTO nhan_vien (manv, ho_ten, email, chuc_vu, mapb, luong_cb) VALUES (142, 'Lê Tấn Hoàng', 'hoangletan@ms.uit.edu.vn', 'Trưởng phòng', '001', 53000000);
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

-- them du lieu du an
INSERT INTO du_an (ten_du_an, mo_ta, ngay_bat_dau, ngay_ket_thuc, makh, trang_thai)
VALUES
('Dự án Alpha', 'Hoàn thành đúng thời hạn.', '2023-01-01', '2023-06-30', 1, 'hoàn thành'),
('Dự án Beta', 'Phát triển hệ thống quản lý.', '2022-05-01', '2022-11-15', 2, 'hoàn thành'),
('Dự án Gamma', 'Nâng cấp ứng dụng hiện có.', '2021-09-01', '2021-12-31', 3, 'hoàn thành'),
('Dự án Delta', 'Hoàn thiện website công ty.', '2020-01-15', '2020-07-30', 4, 'hoàn thành'),
('Dự án Epsilon', 'Tối ưu hóa cơ sở dữ liệu.', '2023-03-01', '2023-08-15', 5, 'hoàn thành'),
('Dự án Zeta', 'Phát triển hệ thống ERP.', '2022-02-10', '2022-09-20', 6, 'hoàn thành'),
('Dự án Eta', 'Triển khai mô hình AI.', '2022-08-01', '2023-01-15', 7, 'hoàn thành'),
('Dự án Theta', 'Xây dựng phần mềm kế toán.', '2021-04-10', '2021-10-30', 8, 'hoàn thành'),
('Dự án Iota', 'Đào tạo nhân sự.', '2020-11-15', '2021-02-28', 9, 'hoàn thành'),
('Dự án Kappa', 'Phát triển ứng dụng di động.', '2023-07-01', '2023-12-15', 10, 'hoàn thành'),
('Dự án Lambda', 'Triển khai giải pháp CRM.', '2021-03-01', '2021-08-31', 11, 'hoàn thành'),
('Dự án Mu', 'Tích hợp API mới.', '2020-06-01', '2020-12-01', 12, 'hoàn thành'),
('Dự án Nu', 'Phân tích dữ liệu khách hàng.', '2023-04-01', '2023-09-30', 13, 'hoàn thành'),
('Dự án Xi', 'Nghiên cứu thị trường.', '2022-11-01', '2023-03-30', 14, 'hoàn thành'),
('Dự án Omicron', 'Thiết kế lại giao diện.', '2021-01-15', '2021-06-30', 15, 'hoàn thành'),
('Dự án Pi', 'Phát triển ứng dụng tài chính.', '2020-03-01', '2020-10-15', 16, 'hoàn thành'),
('Dự án Rho', 'Xây dựng phần mềm nhân sự.', '2022-04-01', '2022-12-01', 17, 'hoàn thành'),
('Dự án Sigma', 'Tối ưu hóa hiệu suất hệ thống.', '2023-02-01', '2023-07-01', 18, 'hoàn thành'),
('Dự án Tau', 'Phát triển website bán hàng.', '2022-06-01', '2022-12-01', 19, 'hoàn thành'),
('Dự án Upsilon', 'Cải tiến quy trình làm việc.', '2021-08-01', '2022-01-01', 20, 'hoàn thành'),
('Dự án Phi', 'Xây dựng hệ thống quản lý dữ liệu.', '2023-08-01', '2024-02-01', 21, 'đang thực hiện'),
('Dự án Chi', 'Phát triển ứng dụng giao hàng.', '2023-09-01', '2024-04-01', 22, 'đang thực hiện'),
('Dự án Psi', 'Nâng cấp hệ thống bảo mật.', '2023-10-01', '2024-03-01', 23, 'đang thực hiện'),
('Dự án Omega', 'Tích hợp chatbot hỗ trợ khách hàng.', '2023-11-01', '2024-05-01', 24, 'đang thực hiện'),
('Dự án Alpha2', 'Phát triển công cụ tìm kiếm nội bộ.', '2023-12-01', '2024-06-01', 25, 'đang thực hiện'),
('Dự án Beta2', 'Tối ưu hóa lưu trữ dữ liệu.', '2023-06-01', '2024-01-01', 26, 'đang thực hiện'),
('Dự án Gamma2', 'Xây dựng ứng dụng học trực tuyến.', '2023-05-01', '2024-02-01', 27, 'đang thực hiện'),
('Dự án Delta2', 'Phát triển hệ thống hỗ trợ khách hàng.', '2023-07-01', '2024-03-01', 28, 'đang thực hiện'),
('Dự án Epsilon2', 'Xây dựng nền tảng thương mại điện tử.', '2023-04-01', '2024-02-01', 29, 'đang thực hiện'),
('Dự án Zeta2', 'Cải tiến quy trình sản xuất.', '2023-02-01', '2024-01-01', 30, 'đang thực hiện'),
('Dự án Eta2', 'Phân tích dữ liệu kinh doanh.', '2023-03-01', '2024-01-01', 31, 'đang thực hiện'),
('Dự án Theta2', 'Xây dựng ứng dụng theo dõi sức khỏe.', '2023-01-01', '2023-12-01', 32, 'đang thực hiện'),
('Dự án Iota2', 'Phát triển hệ thống quản lý bán hàng.', '2023-09-01', '2024-03-01', 33, 'đang thực hiện'),
('Dự án Kappa2', 'Nâng cấp giao diện người dùng.', '2023-11-01', '2024-05-01', 34, 'đang thực hiện'),
('Dự án Lambda2', 'Triển khai công cụ tự động hóa.', '2023-08-01', '2024-02-01', 35, 'đang thực hiện'),

('Dự án Mu2', 'Phát triển hệ thống kiểm thử tự động.', '2023-06-01', '2024-01-01', 36, 'chưa hoàn thành'),
('Dự án Nu2', 'Nâng cấp hạ tầng IT.', '2023-05-01', '2024-02-01', 37, 'chưa hoàn thành'),
('Dự án Xi2', 'Xây dựng hệ thống xử lý dữ liệu lớn.', '2023-07-01', '2024-03-01', 38, 'chưa hoàn thành'),
('Dự án Omicron2', 'Phân tích dữ liệu tài chính.', '2023-04-01', '2024-01-01', 39, 'chưa hoàn thành'),
('Dự án Pi2', 'Phát triển nền tảng học tập.', '2023-01-01', '2023-12-01', 40, 'chưa hoàn thành'),
('Dự án Rho2', 'Tích hợp hệ thống quản lý khách hàng.', '2023-08-01', '2024-02-01', 41, 'chưa hoàn thành'),
('Dự án Sigma2', 'Phát triển hệ thống phân phối.', '2023-02-01', '2024-01-01', 42, 'chưa hoàn thành'),
('Dự án Tau2', 'Tối ưu hóa hiệu năng hệ thống.', '2023-03-01', '2024-01-01', 43, 'chưa hoàn thành'),
('Dự án Upsilon2', 'Nâng cấp dịch vụ hỗ trợ khách hàng.', '2023-09-01', '2024-03-01', 44, 'chưa hoàn thành'),
('Dự án Phi2', 'Xây dựng ứng dụng quản lý dự án.', '2023-11-01', '2024-05-01', 45, 'chưa hoàn thành'),

('Dự án Chi2', 'Phát triển hệ thống theo dõi GPS.', '2023-10-01', '2024-03-01', 46, 'hủy bỏ'),
('Dự án Psi2', 'Nâng cấp cơ sở dữ liệu cũ.', '2023-05-01', '2024-02-01', 47, 'hủy bỏ'),
('Dự án Omega2', 'Phát triển ứng dụng truyền thông xã hội.', '2023-08-01', '2024-02-01', 48, 'hủy bỏ'),
('Dự án Alpha3', 'Tích hợp hệ thống thanh toán.', '2023-04-01', '2024-01-01', 49, 'hủy bỏ'),
('Dự án Beta3', 'Nâng cấp phần mềm kế toán.', '2023-06-01', '2024-01-01', 50, 'hủy bỏ');

-- them du lieu khach hang
INSERT INTO khach_hang (ten_khach_hang, email, so_dien_thoai, dia_chi) VALUES
('Mai Khánh Toàn', 'mai.khánh.toàn@example.com', '0923456789', 'Đà Nẵng, Việt Nam'),
('Ngô Minh Tuấn', 'ngô.minh.tuấn@example.com', '0934567890', 'Bình Dương, Việt Nam'),
('Nguyễn Hoàng Lộc', 'nguyễn.hoàng.lộc@example.com', '0967890123', 'Hà Nội, Việt Nam'),
('Trần Hải Minh', 'trần.hải.minh@example.com', '0978901234', 'Vũng Tàu, Việt Nam'),
('Bùi Anh Dũng', 'bùi.anh.dũng@example.com', '0990123456', 'Hải Phòng, Việt Nam'),
('Lý Thị Lan', 'lý.thị.lan@example.com', '0990123456', 'Hà Nội, Việt Nam'),
('Đoàn Hữu Đức', 'đoàn.hữu.đức@example.com', '0901234567', 'Hải Phòng, Việt Nam'),
('Vũ Lan Anh', 'vũ.lan.anh@example.com', '0945678901', 'Đà Nẵng, Việt Nam'),
('Phạm Hoàng Duy', 'phạm.hoàng.duy@example.com', '0945678901', 'Cần Thơ, Việt Nam'),
('Bùi Lan Anh', 'bùi.lan.anh@example.com', '0967890123', 'Hồ Chí Minh, Việt Nam'),
('Trần Hữu Tâm', 'trần.hữu.tâm@example.com', '0978901234', 'Hải Phòng, Việt Nam'),
('Nguyễn Văn An', 'nguyễn.văn.an@example.com', '0990123456', 'Vũng Tàu, Việt Nam'),
('Hồ Thị Hoa', 'hồ.thị.hoa@example.com', '0934567890', 'Lào Cai, Việt Nam'),
('Trần Thị Bình', 'trần.thị.bình@example.com', '0989012345', 'Cần Thơ, Việt Nam'),
('Nguyễn Hoàng Hải', 'nguyễn.hoàng.hải@example.com', '0990123456', 'Nha Trang, Việt Nam'),
('Mai Khánh Hòa', 'mai.khánh.hòa@example.com', '0923456789', 'Hà Nội, Việt Nam'),
('Lê Quang Sơn', 'lê.quang.sơn@example.com', '0912345678', 'Hà Nội, Việt Nam'),
('Ngô Minh Quân', 'ngô.minh.quân@example.com', '0990123456', 'Đà Nẵng, Việt Nam'),
('Lê Minh Cường', 'lê.minh.cường@example.com', '0945678901', 'Cần Thơ, Việt Nam'),
('Nguyễn Thị Lan', 'nguyễn.thị.lan@example.com', '0989012345', 'Cần Thơ, Việt Nam'),
('Phạm Bình Lộc', 'phạm.bình.lộc@example.com', '0967890123', 'Đà Nẵng, Việt Nam'),
('Đoàn Hữu Tiến', 'đoàn.hữu.tiến@example.com', '0934567890', 'Vũng Tàu, Việt Nam'),
('Lê Tuấn Kiệt', 'lê.tuấn.kiệt@example.com', '0934567890', 'Vũng Tàu, Việt Nam'),
('Phạm Tuấn Tài', 'phạm.tuấn.tài@example.com', '0967890123', 'Hải Phòng, Việt Nam'),
('Hồ Thị Lan', 'hồ.thị.lan@example.com', '0989012345', 'Hồ Chí Minh, Việt Nam');
INSERT INTO khach_hang (makh, ten_khach_hang, email, so_dien_thoai, dia_chi)
VALUES
    (26, 'Khách Hàng 26', 'kh26@example.com', '0900123456', 'Hà Nội, Việt Nam'),
    (27, 'Khách Hàng 27', 'kh27@example.com', '0912345678', 'Đà Nẵng, Việt Nam'),
    (28, 'Khách Hàng 28', 'kh28@example.com', '0923456789', 'Hồ Chí Minh, Việt Nam'),
    (29, 'Khách Hàng 29', 'kh29@example.com', '0934567890', 'Cần Thơ, Việt Nam'),
    (30, 'Khách Hàng 30', 'kh30@example.com', '0945678901', 'Hải Phòng, Việt Nam'),
    (31, 'Khách Hàng 31', 'kh31@example.com', '0956789012', 'Nha Trang, Việt Nam'),
    (32, 'Khách Hàng 32', 'kh32@example.com', '0967890123', 'Vũng Tàu, Việt Nam'),
    (33, 'Khách Hàng 33', 'kh33@example.com', '0978901234', 'Bình Dương, Việt Nam'),
    (34, 'Khách Hàng 34', 'kh34@example.com', '0989012345', 'Lào Cai, Việt Nam'),
    (35, 'Khách Hàng 35', 'kh35@example.com', '0990123456', 'Đồng Nai, Việt Nam'),
    (36, 'Khách Hàng 36', 'kh36@example.com', '0901234567', 'Thanh Hóa, Việt Nam'),
    (37, 'Khách Hàng 37', 'kh37@example.com', '0912345678', 'Hà Nội, Việt Nam'),
    (38, 'Khách Hàng 38', 'kh38@example.com', '0923456789', 'Đà Nẵng, Việt Nam'),
    (39, 'Khách Hàng 39', 'kh39@example.com', '0934567890', 'Hồ Chí Minh, Việt Nam'),
    (40, 'Khách Hàng 40', 'kh40@example.com', '0945678901', 'Cần Thơ, Việt Nam'),
    (41, 'Khách Hàng 41', 'kh41@example.com', '0956789012', 'Hải Phòng, Việt Nam'),
    (42, 'Khách Hàng 42', 'kh42@example.com', '0967890123', 'Nha Trang, Việt Nam'),
    (43, 'Khách Hàng 43', 'kh43@example.com', '0978901234', 'Vũng Tàu, Việt Nam'),
    (44, 'Khách Hàng 44', 'kh44@example.com', '0989012345', 'Bình Dương, Việt Nam'),
    (45, 'Khách Hàng 45', 'kh45@example.com', '0990123456', 'Lào Cai, Việt Nam'),
    (46, 'Khách Hàng 46', 'kh46@example.com', '0901234567', 'Đồng Nai, Việt Nam'),
    (47, 'Khách Hàng 47', 'kh47@example.com', '0912345678', 'Thanh Hóa, Việt Nam'),
    (48, 'Khách Hàng 48', 'kh48@example.com', '0923456789', 'Hà Nội, Việt Nam'),
    (49, 'Khách Hàng 49', 'kh49@example.com', '0934567890', 'Đà Nẵng, Việt Nam'),
    (50, 'Khách Hàng 50', 'kh50@example.com', '0945678901', 'Hồ Chí Minh, Việt Nam');

-- cong viec
INSERT INTO cong_viec (macv, mada, ten_cong_viec, mo_ta, giao_cho, han_chot, trang_thai)
VALUES
    (01, 1, 'Thiết kế đồ họa nhân vật', 'Tạo mô hình 3D cho nhân vật chính', 101, '2024-02-15', 'dang_thuc_hien'),
    (02, 1, 'Lập trình AI', 'Phát triển trí tuệ nhân tạo cho NPC', 102, '2024-03-10', 'chua_thuc_hien'),
    (03, 2, 'Thiết kế cảnh quan', 'Xây dựng bản đồ thế giới mở', 103, '2024-03-25', 'dang_thuc_hien'),
    (04, 2, 'Phát triển cơ chế chiến đấu', 'Lập trình cơ chế chiến đấu cận chiến và tầm xa', 104, '2024-04-05', 'chua_thuc_hien'),
    (05, 3, 'Lập trình UI', 'Tạo giao diện người dùng', 105, '2024-05-01', 'chua_thuc_hien'),
    (06, 3, 'Kiểm thử game', 'Thực hiện kiểm tra lỗi và hiệu năng', 106, '2024-05-20', 'chua_thuc_hien'),
    (07, 4, 'Viết cốt truyện', 'Xây dựng cốt truyện chính và nhiệm vụ phụ', 107, '2024-06-15', 'dang_thuc_hien'),
    (08, 5, 'Phát triển hệ thống nhiệm vụ', 'Tạo hệ thống nhiệm vụ tự động', 108, '2024-07-10', 'chua_thuc_hien'),
    (09, 6, 'Lập trình mạng', 'Phát triển hệ thống chơi đa người', 109, '2024-08-20', 'chua_thuc_hien'),
    (10, 7, 'Tối ưu hóa hiệu năng', 'Cải thiện hiệu năng cho các thiết bị cấu hình thấp', 110, '2024-09-15', 'dang_thuc_hien');


-- Thêm dữ liệu cho phòng Bán hàng
INSERT INTO bang_cong (mabc, manv, macv, so_gio, ngay_lam, so_luong_san_pham)
VALUES
    (1, 109, 101, 8, '2024-01-10', 50),
    (2, 111, 102, 6, '2024-01-11', 55),
    (3, 112, 103, 7, '2024-01-12', 48);

-- Thêm dữ liệu cho phòng Marketing
INSERT INTO bang_cong (mabc, manv, macv, so_gio, ngay_lam, so_luong_san_pham)
VALUES
    (4, 105, 201, 8, '2024-01-13', 30),
    (5, 106, 202, 7, '2024-01-14', 32),
    (6, 120, 203, 6, '2024-01-15', 28);

-- Thêm dữ liệu cho phòng IT
INSERT INTO bang_cong (mabc, manv, macv, so_gio, ngay_lam, so_luong_san_pham)
VALUES
    (7, 113, 301, 8, '2024-01-16', 20),
    (8, 167, 302, 9, '2024-01-17', 22),
    (9, 121, 303, 7, '2024-01-18', 18);

-- Thêm dữ liệu cho phòng Quản lý
INSERT INTO bang_cong (mabc, manv, macv, so_gio, ngay_lam, so_luong_san_pham)
VALUES
    (10, 101, 401, 8, '2024-01-19', 10),
    (11, 102, 402, 7, '2024-01-20', 12),
    (12, 110, 403, 6, '2024-01-21', 8);

-- Thêm dữ liệu cho phòng Nhân sự
INSERT INTO bang_cong (mabc, manv, macv, so_gio, ngay_lam, so_luong_san_pham)
VALUES
    (13, 103, 501, 8, '2024-01-22', 15),
    (14, 104, 502, 7, '2024-01-23', 18),
    (15, 118, 503, 6, '2024-01-24', 12);

-- Thêm dữ liệu cho phòng Tài chính
INSERT INTO bang_cong (mabc, manv, macv, so_gio, ngay_lam, so_luong_san_pham)
VALUES
    (16, 108, 601, 8, '2024-01-25', 25),
    (17, 126, 602, 7, '2024-01-26', 28),
    (18, 140, 603, 6, '2024-01-27', 22);

select * from bang_cong;
select * from cong_viec;
select * from du_an;
select * from khach_hang;
select * from nguoi_dung;
select * from nhan_vien;
select * from phong_ban;