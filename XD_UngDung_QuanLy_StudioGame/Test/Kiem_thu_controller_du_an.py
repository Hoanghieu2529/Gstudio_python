import pytest
from unittest.mock import MagicMock
from controllers.controller_DuAn import DuAnFormController

@pytest.fixture
def controller():
    """Khởi tạo controller với mock view."""
    mock_view = MagicMock()  # Tạo một mock object cho view
    return DuAnFormController(view=mock_view)

def test_lay_danh_sach_du_an(controller):
    """Kiểm tra lấy danh sách dự án."""
    du_an_list = controller.Lay_danh_sach_du_an()
    assert isinstance(du_an_list, list)
    assert len(du_an_list) >= 0
