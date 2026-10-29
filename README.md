# Login Failure Detector

ログファイルからログイン失敗をIPアドレスごとに集計し、失敗回数がしきい値を超えたIPを不審なアクセスとして検出するコマンドラインツールです。

## 背景

将来、セキュリティエンジニアを目指す中でブルートフォース攻撃の検知をできるようにしたいと考えました。ブルートフォース攻撃とはパスワードを総当たりで試してログインを狙う攻撃のことです。

## 使い方

```
python detector.py sample_logs/auth.log
python detector.py sample_logs/auth.log --threshold 3
```

| 引数 | 説明 |
|---|---|
| `logfile` | 解析するログファイルのパス（必須） |
| `--threshold` | 不審と判定する失敗回数のしきい値（省略時は2） |

## 実行例

```
$ python detector.py sample_logs/auth.log

203.0.113.9 -> root
203.0.113.9 -> admin
198.51.100.4 -> test
失敗回数:3

IPごとの失敗回数
203.0.113.9: 2回
198.51.100.4: 1回

[!]不審なIP（失敗 2回以上）
203.0.113.9: 2回

$ python detector.py sample_logs/auth.log --threshold 3

203.0.113.9 -> root
203.0.113.9 -> admin
198.51.100.4 -> test
失敗回数:3

IPごとの失敗回数
203.0.113.9: 2回
198.51.100.4: 1回

[!]不審なIP（失敗 3回以上）

$ python detector.py --help
usage: detector.py [-h] [--threshold THRESHOLD]
                   logfile

ログイン失敗ログから不審なIPを検出するツール

positional arguments:
  logfile               解析するログファイルのパス

options:
  -h, --help            show this help message
                        and exit
  --threshold THRESHOLD
                        不審と判断する失敗回数のしきい値

```

## 工夫した点

- **しきい値を定数で管理**：判定に使うしきい値を `THRESHOLD` という定数にまとめました。判定処理と表示の見出しで同じ値を使うため、1か所を変えるだけで両方に反映され、直し忘れによる不具合を防げます。
- **処理を関数に分割**：ログを読み込んで集計する `analyze_log` と、結果を表示する `show_report` に役割を分けました。コマンドライン引数に対応させた際も、集計処理を変更せずに機能を追加できました。
- **コマンドライン引数に対応**：`argparse` を使い、ログファイルとしきい値を実行時に指定できるようにしました。コードを書き換えずに使えるうえ、`--help` で使い方を確認できます。

## 注意事項

テスト用の架空データを使っていること、自分の管理する環境でのみ使うこと

## 使用技術

- Python 3.12
- 標準ライブラリのみ（argparse）