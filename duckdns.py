# crontab -e
# */10 * * * * /usr/bin/python /home/pi/duckdns.py >/dev/null 2>&1
# xem log: sudo grep CRON /var/log/syslog
# Apr 27 10:00:01 host CRON[1234]: (root) CMD (/usr/bin/python3 /home/pi/update_ip_duckdns/duckdns.py >> /home/pi/cron.log 2>&1)
# Mở terminal trên Linux.
# cd /home/pi/update_ip_duckdns
# chmod +x duckdns.py

import requests
import os

def update_dns():
    domain = 'vipi'# domain = "yourdomain"
    token = 'e428b8da-5316-49f4-88e0-209f41xx'# token = "yourtoken"
    #url = "https://www.duckdns.org/update?domains=vipi&token=e428b8da-5316-49f4-88e0-209f41259cxx"
    url = f"https://www.duckdns.org/update?domains={domain}&token={token}"
    response = requests.get(url)
    print(response.content)

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
        update_dns()

if __name__ == "__main__":
    main()
