# Login Failure Detector

ログファイルからログイン失敗をIPアドレスごとに集計し、失敗回数がしきい値を超えたIPを不審なアクセスとして検出するコマンドラインツールです。

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
 python detector.py sample_logs/auth.log

203.0.113.9 -> root
203.0.113.9 -> admin
198.51.100.4 -> test
失敗回数:3

IPごとの失敗回数
203.0.113.9: 2回
198.51.100.4: 1回

[!]不審なIP（失敗 2回以上）
203.0.113.9: 2回

 python detector.py sample_logs/auth.log --threshold 3

203.0.113.9 -> root
203.0.113.9 -> admin
198.51.100.4 -> test
失敗回数:3

IPごとの失敗回数
203.0.113.9: 2回
198.51.100.4: 1回

[!]不審なIP（失敗 3回以上）

 python detector.py --help
usage: detector.py [-h] [--threshold THRESHOLD]
                   logfile

ログイン失敗ログから不審なIPを検出するツール

positional arguments:
  logfile               解析するログインファイルのパス

options:
  -h, --help            show this help message
                        and exit
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