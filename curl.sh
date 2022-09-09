curl --location --request POST '192.168.10.85:5500/cron' \
--header 'content_type: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
   "username": "validuser",
   "token": "validpass"
}'
