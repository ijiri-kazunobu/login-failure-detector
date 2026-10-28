THRESHOLD = 2


def analyze_log(path):
    count = 0
    fail_counts = {}
    with open(path,encoding="utf-8") as f:
        for log in f:
            log = log.strip()
            if "FAILED" in log:
                parts = log.split()
                ip = parts[5]
                user = parts[6].split('=')[1]
                print(f"{ip} -> {user}")
                count += 1

                if ip in fail_counts:
                    fail_counts[ip] += 1
                else:
                    fail_counts[ip] = 1
    return count, fail_counts


def show_report(count, fail_counts):
    print(f"失敗回数:{count}")
    print()
    print("IPごとの失敗回数")
    for ip, num in fail_counts.items():
        print(f"{ip}: {num}回")
    print()
    print(f"[!]不審なIP（失敗 {THRESHOLD}回以上）")
    for ip, num in fail_counts.items():
        if num >= THRESHOLD:
            print(f"{ip}: {num}回")


count, fail_counts = analyze_log("sample_logs/auth.log")
show_report(count, fail_counts)