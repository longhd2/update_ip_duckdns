# update_ip_duckdns
git
# crontab -e
# */10 * * * * /usr/bin/python /home/pi/duckdns.py >/dev/null 2>&1
# xem log: sudo grep CRON /var/log/syslog
# Apr 27 10:00:01 host CRON[1234]: (root) CMD (/usr/bin/python3 /home/pi/update_ip_duckdns/duckdns.py >> /home/pi/cron.log 2>&1)
# Mở terminal trên Linux.
# cd /home/pi/update_ip_duckdns
# chmod +x duckdns.py
