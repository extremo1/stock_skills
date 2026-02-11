# stock-skills

割安株スクリーニングシステム。Yahoo Finance APIを使って日本株・米国株・ASEAN株の割安銘柄を発見する。

## スキル一覧

- `/screen-stocks` : 割安株スクリーニング
- `/stock-report` : 個別銘柄レポート
- `/watchlist` : ウォッチリスト管理

## 開発ルール

- Python 3.10+
- データ取得は src/data/yahoo_client.py 経由
- テストは tests/ に配置
