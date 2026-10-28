logs = [
    "2026-10-19 10:20:01 SUCCESS login from 10.0.0.5 user=tanaka",
    "2026-10-19 10:21:15 FAILED login from 203.0.113.9 user=root",
    "2026-10-19 10:21:18 FAILED login from 203.0.113.9 user=admin",
    "2026-10-19 10:22:40 SUCCESS login from 10.0.0.8 user=suzuki",
    "2026-10-19 10:23:02 FAILED login from 198.51.100.4 user=test",
]

count = 0
for log in logs:
    if "FAILED" in log:
        parts = log.split()
        ip = parts[5]
        user = parts[6].split('=')[1]
        print(f"{ip} -> {user}")
        count += 1
print(f'失敗回数：{count}')