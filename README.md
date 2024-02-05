# Hướng dẫn Triển khai Module lên Server

## Mục đích
Hướng dẫn này sẽ giúp bạn triển khai module của dự án lên server một cách dễ dàng và hiệu quả.

## Yêu cầu
Trước khi bắt đầu, đảm bảo rằng server của bạn đáp ứng các yêu cầu sau:
- [ ] **Hệ điều hành:** Server đang chạy hệ điều hành Linux
- [ ] **Phần mềm cài đặt:** Cài đặt các phần mềm cần thiết cho module hoạt động caanf cos python 3.11.5, pip lastest version

## Bước 1: Sao chép mã nguồn từ Repository
```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

## Bước 2: Tạo môi trường ảo python và cài đặt các package cần thiết
```bash
python -m venv env
pip install -r requirements.txt
```

## Bước 3: Chạy ứng dụng và truy cập
```bash
python app.py
```

## Note: Nếu bị lỗi hiển thị có thể dùng lệch sau để khắc phục
```bash
sudo apt install libgl1-mesa-glx
```