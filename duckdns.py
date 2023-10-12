
# Edit crontab
# crontab -e 

# Thêm dòng sau (chạy script cập nhật mỗi 10 phút)
# */10 * * * * /usr/bin/python /home/pi/duckdns.py >/dev/null 2>&1


#Để sử dụng lệnh service mà không cần quyền root, bạn có thể thêm 2 thư mục /sbin và /usr/sbin vào biến PATH:
#export PATH=$PATH:/sbin:/usr/sbin

# kiểm tra service nếu Active: active (running) là đã hoạt động
# service cron status

import requests
import os
DOMAIN = "vipi"
TOKEN = "e428b8da-5316-49f4-88e0-209f41259cfa" 

def update_ip():
  url = f"https://www.duckdns.org/update?domains={DOMAIN}&token={TOKEN}&ip="
  
  current_ip = get_current_ip()
  url += current_ip

  response = requests.get(url)
  if response.text.startswith("OK"):
    print(f"Update IP thành công:  {current_ip}") 
    return True
  else:
    print(f"Không Update được IP: {response.text}")
    return False

def get_current_ip():
    response = requests.get("https://api.ipify.org")
    return response.text

def main():
    # Đọc địa chỉ IP hiện tại được lưu trữ từ tệp txt
    with open("current_ip.txt", "r") as f:
        current_ip = f.read().strip()

    # Lấy địa chỉ IP hiện tại
    new_ip = get_current_ip()

    # Nếu địa chỉ IP khác nhau, cập nhật DuckDNS
    if new_ip != current_ip:
        # Cập nhật địa chỉ IP mới vào tệp txt
        with open("current_ip.txt", "w") as f:
            f.write(new_ip)

        # Thực hiện cập nhật địa chỉ IP mới lên DuckDNS
        update_ip()
    else:
        print(f"Không có thay đổi IP, không cập nhật lại IP: {new_ip}")

if __name__ == "__main__":
    main()
