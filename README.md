# Login Failure Detector

ログインしたIPアドレスの回数の確認。および、不審なアクセスの検知

## 背景

将来、セキュリティエンジニアを目指す中でブルートフォース攻撃の検知をできるようにしたいと考えた。ブルートフォース攻撃とはパスワードを総当たりで試してログインを狙う攻撃のことである。

## 使い方

```
python detector.py sample_logs/auth.log
python detector.py sample_logs/auth.log --threshold 3
```

| 引数 | 説明 |
|---|---|
| `logfile` | （説明） |
| `--threshold` | （説明。省略時の値も） |

## 実行例

```
(.venv) PS C:\Users\ijiri\projects\login-failure-detector> 
(.venv) PS C:\Users\ijiri\projects\login-failure-detector> python detector.py sample_logs/auth.log
203.0.113.9 -> root
203.0.113.9 -> admin
198.51.100.4 -> test
Traceback (most recent call last):
  File "C:\Users\ijiri\projects\login-failure-detector\detector.py", line 45, in <module>
    show_report(count, fail_counts)
TypeError: show_report() missing 1 required positional argument: 'threshold'
(.venv) PS C:\Users\ijiri\projects\login-failure-detector> python detector.py sample_logs/auth.log --threshold 3
203.0.113.9 -> root
203.0.113.9 -> admin
198.51.100.4 -> test
Traceback (most recent call last):
  File "C:\Users\ijiri\projects\login-failure-detector\detector.py", line 45, in <module>
    show_report(count, fail_counts)
TypeError: show_report() missing 1 required positional argument: 'threshold'
(.venv) PS C:\Users\ijiri\projects\login-failure-detector> python detector.py --help
usage: detector.py [-h] [--threshold THRESHOLD] logfile

ログイン失敗ログから不審なIPを検出するツール

positional arguments:
  logfile               解析するログインファイルのパス

options:
  -h, --help            show this help message and exit
  --threshold THRESHOLD
                        不審と判断する失敗回数のしきい値
```

## 工夫した点

- （例：処理を関数に分けた理由）
- （例：しきい値をコマンドラインで変えられるようにした理由）
- （その他、自分が考えたこと）

## 注意事項

テスト用の架空データを使っていること、自分の管理する環境でのみ使うこと

## 使用技術

- Python 3.12
- 標準ライブラリのみ（argparse）