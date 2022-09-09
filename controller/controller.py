import subprocess


def call():
    out = subprocess.run(['docker exec shopbackend /usr/bin/php7.4  /var/www/html/bin/magento cron:run'], text=True,shell=True ,capture_output=True)
    print(out)

