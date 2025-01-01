import pytest
from models.database import Database

@pytest.fixture
def db_connection():
    """Khởi tạo kết nối Database cho mỗi bài kiểm thử."""
    db = Database()
    yield db  # Kết nối này sẽ được sử dụng trong các bài kiểm thử
    del db  # Đóng kết nối sau khi kiểm thử

def test_connection(db_connection):
    """Kiểm tra kết nối cơ sở dữ liệu."""
    assert db_connection.kiem_tra_ket_noi() is None  # Không có lỗi khi kết nối

def test_fetch_all(db_connection):
    """Kiểm tra truy vấn SELECT."""
    data = db_connection.fetch_all("SELECT 1")
    assert data == [{"1": 1}]  # Trả về kết quả mong đợi
