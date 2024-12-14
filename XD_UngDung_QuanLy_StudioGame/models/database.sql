CREATE TABLE phong_ban (
    mapb INT AUTO_INCREMENT PRIMARY KEY,
    ten_phong_ban VARCHAR(100) NOT NULL,
    mo_ta TEXT
);

CREATE TABLE nhan_vien (
    manv INT AUTO_INCREMENT PRIMARY KEY,
    ho_ten VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    chuc_vu VARCHAR(50),
    phong_ban_id INT,
    luong_cb int,
    FOREIGN KEY (phong_ban_id) REFERENCES phong_ban(mapb)
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
    khach_hang_id INT,
    FOREIGN KEY (khach_hang_id) REFERENCES khach_hang(makh)
);

CREATE TABLE cong_viec (
    macv INT AUTO_INCREMENT PRIMARY KEY,
    du_an_id INT,
    ten_cong_viec VARCHAR(100) NOT NULL,
    mo_ta TEXT,
    giao_cho INT,
    han_chot DATE NOT NULL,
    trang_thai ENUM('chua_thuc_hien', 'dang_thuc_hien', 'hoan_thanh') DEFAULT 'chua_thuc_hien',
    FOREIGN KEY (du_an_id) REFERENCES du_an(mada),
    FOREIGN KEY (giao_cho) REFERENCES nhan_vien(manv)
);

CREATE TABLE bang_thoi_gian (
    mathgian INT AUTO_INCREMENT PRIMARY KEY,
    nhan_vien_id INT,
    cong_viec_id INT,
    so_gio INT NOT NULL,
    ngay_lam DATE NOT NULL,
    FOREIGN KEY (nhan_vien_id) REFERENCES nhan_vien(manv),
    FOREIGN KEY (cong_viec_id) REFERENCES cong_viec(macv)
);
