# update_ip_duckdns
Mở terminal trên Linux.

'''
sudo apt-get install git -y && git clone https://github.com/longhd2/update_ip_duckdns
'''

Cài đặt trong file: duckdns.py


    domain = 'vipi'# domain = "yourdomain"
    token = 'e428b8da-5316-49f4-88e0-209f41xx'# token = "yourtoken"


chạy thủ công:
chmod +x duckdns.py
cd /home/pi/update_ip_duckdns
python duckdns.py



Chạy tự động, 10p kiểm tra sau 10 phút
crontab -e
*/10 * * * * /usr/bin/python /home/pi/duckdns.py >/dev/null 2>&1
xem log: 
sudo grep CRON /var/log/syslog
Nếu hiện dạng như sau scrip đã hoạt động
Apr 27 10:00:01 host CRON[1234]: (root) CMD (/usr/bin/python3 /home/pi/update_ip_duckdns/duckdns.py >> /home/pi/cron.log 2>&1)

