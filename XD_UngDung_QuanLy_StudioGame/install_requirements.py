import subprocess
import sys
import os

def install_requirements():
    """Tự động cài đặt các thư viện từ file requirements.txt"""
    requirements_file = "requirements.txt"

    # Đảm bảo  chạy lệnh này trong terminal trước khi cài bất cứ thư viện nào: python.exe -m pip install --upgrade pip
    # Kiểm tra file requirements có tồn tại không ?
    if not os.path.exists(requirements_file):
        print(f"File {requirements_file} không tồn tại! Vui lòng kiểm tra lại.")
        sys.exit(1)

    print("Đang kiểm tra và cài đặt các thư viện cần thiết...")
    try:
        # Lệnh cài đặt các thư viện từ file requirements
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
        print("Cài đặt thư viện thành công!")
    except subprocess.CalledProcessError:
        print("Có lỗi xảy ra trong quá trình cài đặt các thư viện!")
        sys.exit(1)


if __name__ == "__main__":
    install_requirements()
