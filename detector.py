import argparse
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


def show_report(count, fail_counts, threshold):
    print(f"失敗回数:{count}")
    print()
    print("IPごとの失敗回数")
    for ip, num in fail_counts.items():
        print(f"{ip}: {num}回")
    print()
    print(f"[!]不審なIP（失敗 {threshold}回以上）")
    for ip, num in fail_counts.items():
        if num >= threshold:
            print(f"{ip}: {num}回")


parser = argparse.ArgumentParser(description="ログイン失敗ログから不審なIPを検出するツール")
parser.add_argument("logfile", help = "解析するログファイルのパス")
parser.add_argument("--threshold", type=int, default=THRESHOLD, help="不審と判断する失敗回数のしきい値")
args = parser.parse_args()


count, fail_counts = analyze_log(args.logfile)
show_report(count, fail_counts, args.threshold)