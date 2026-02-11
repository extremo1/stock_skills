---
name: stock-report
description: 個別銘柄の詳細レポート。ティッカーシンボルを指定して財務分析レポートを生成する。
argument-hint: "[ticker]  例: 7203.T, AAPL, D05.SI"
allowed-tools: Bash(python3 *)
---

# 個別銘柄レポートスキル

$ARGUMENTS からティッカーシンボルを取り出し、以下のコマンドを実行してください。

```bash
python3 /Users/kikuchihiroyuki/stock-skills/.claude/skills/stock-report/scripts/generate_report.py $ARGUMENTS
```

結果をそのまま表示してください。
