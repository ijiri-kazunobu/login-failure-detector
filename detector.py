
count = 0
with open("sample_logs/auth.log",encoding="utf-8") as f:
    for log in f:
        log = log.strip()
        if "FAILED" in log:
            parts = log.split()
            ip = parts[5]
            user = parts[6].split('=')[1]
            print(f"{ip} -> {user}")
            count += 1
print(f'失敗回数：{count}')