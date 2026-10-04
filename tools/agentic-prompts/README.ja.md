# Agentic Engineering プロンプト一覧ジェネレーター

**1 つの CLI** 向けのすべてのプロンプトを、順番どおりに **1 つのファイル** に書き出します。英語版: [README.md](./README.md)

```bash
python3 tools/agentic-prompts/generate.py
```

Python 3.11 以上が必要です（標準ライブラリのみ）。どのプロンプトも、リポジトリ構成・命名・状態ファイルについて [docs/program-layout.md](../../docs/program-layout.ja.md) をエージェントに読ませます。

## 設定: `config.toml`

```toml
cli = "claude-code"        # claude-code | codex | antigravity
language = "ja"            # ja | en（プロンプトの言語）
output = "prompts/agentic-engineering-prompts.claude-code.ja.md"
max_file_kib = 400         # 1 ファイルの上限サイズ（KiB）

cross_cutting = [          # 横断的な手法: 調査のみ。以降のすべての手法に適用
  "Prompt Engineering",
  "Context Engineering",
  "Memory Engineering",
  "Knowledge Engineering",
]

methods = [                # その他の手法: 調査 → 実装計画 → 実装とまとめ
  "Spec / Plan Engineering",
  "Verification / Eval Engineering",
  # ...
]
```

- リストの順序が、そのままプロンプトの順序になります。番号（①、②、…）は `cross_cutting`、`methods` の順に通しで振られます。
- 別の CLI 向けの一覧を作るときは、`cli` と `output` を変えます（CLI ごとに設定ファイルを用意し、`--config` で渡してもかまいません）。

## 出力

1. 設定と、番号付きのステップ一覧。
2. ステップごとに 1 セクション（順番どおり）: 起動コマンド（セッション名、計画ステップではプランモード）、そのステップが書き出すファイル、貼り付けてそのまま使える `text` ブロックのプロンプト。

| ステップ | プロンプトが依頼すること |
| --- | --- |
| 横断的な手法の `-1` | その CLI 向けに手法を調査する。先行する横断的な手法の文書を踏まえる → `docs/{slug}-for-cli-agents.{cli}.md`（+ `.ja.md`） |
| その他の手法の `-1` | その CLI 向けに手法を調査する。実装の計画にあたって重要なことを含める → `docs/{NN}-{slug}/research.{cli}.md` |
| その他の手法の `-2` | フォルダ階層必須の実装計画。それまでに作成したすべての文書を読む → `plan.{cli}.md` |
| その他の手法の `-3` | 計画に沿って実装し、CLI 内でテストし、レビューし、まとめる → `implementation.{cli}.md` |

どのプロンプトにも、英語ファイルだけを読むこと、`docs/INDEX.md`・`docs/PROGRESS.md`・`docs/DIGEST.md` の更新、英語の `.md` と和訳の `.ja.md` を書くことが含まれます。後半のステップのプロンプトは、読み込みがコンテキストウィンドウの約 40% を超えそうな場合にダイジェストのファイルへ切り替えるよう指示します。

1 つのプロンプトを 1 つの新しいセッションで、順番に実行し、次へ進む前に結果をレビューしてください。

## 大きな出力の分割

出力が `max_file_kib` より大きい場合は、すべてのファイルが上限内に収まるように分割します（例: エディタの 512 KiB 上限への対策）。

- `output` は目次ページになります。タイトルと前書きの後に、各パートへの Markdown リンクと、そのパートに含まれる見出しを並べます。
- パートは同じ場所に `<名前>.part-01.ja.md`、`<名前>.part-02.ja.md`、… として置かれます。各パートの先頭と末尾には、目次・前のパート・次のパートへのリンクがあります。
- 分割は見出しの区切りでのみ行います。まず手法の間（`###`）、1 つの手法が大きすぎる場合はステップの間（`####`）です。見出し・コードブロック・表の途中では分割せず、内容の欠落や並べ替えもありません。
- 小見出しを持たず、それ単体で上限を超えるセクションは、警告を出したうえで分割せずにそのまま残します。
- 出力が再び上限内に収まった場合は、以前の実行で作られたパートを削除し、1 つのファイルとして書き出します。

他の Markdown ファイルも同じ方法で分割できます:

```bash
python3 tools/agentic-prompts/mdsplit.py docs/some-large-file.md            # 上限は max_file_kib から
python3 tools/agentic-prompts/mdsplit.py docs/some-large-file.md --max-kib 300
```

元のファイルは目次ページに置き換わります。すでに分割済みのファイルに対しては実行を拒否するので、パートが失われることはありません。

## 範囲の説明: `briefs.toml`

プロンプトには、各手法の範囲、調査の焦点、出発点、想定する成果物、受け入れの証拠が `briefs.toml` から埋め込まれます。キーはスラッグです。名前を小文字にし、英数字以外を `-` に置き換えたものです（`"Spec / Plan Engineering"` → `spec-plan-engineering`）。

- 既定の 13 の手法はすべて登録済みです。
- プロンプトには、以前の調査結果を含めません。各ステップはその時点で最新の公式ドキュメントを調べます。出発点は確認すべきヒントとして示し、調査文書には調査日を書かせます。
- 登録のない手法も使えます。その場合、プロンプトはエージェントに範囲を定義させます（ジェネレーターは警告を表示します）。
- 追加するには、ブロックを足します:

  ```toml
  [security-engineering]
  [security-engineering.en]
  scope = "..."
  research_focus = "..."
  starting_points = "..."
  expected_artifacts = "..."
  acceptance = "..."
  [security-engineering.ja]
  scope = "..."
  ```

## ファイル

| ファイル | 目的 |
| --- | --- |
| `config.toml` | 1 つの CLI、横断的な手法、その他の手法、言語、出力先、上限サイズ |
| `briefs.toml` | 手法ごとの範囲の説明 |
| `generate.py` | ジェネレーター本体。CLI 固有のコマンド（起動、プランモード、確認、レビュアー）は組み込み |
| `mdsplit.py` | Markdown を見出しの区切りで分割し、目次ページを書き出す（ジェネレーターが使用。単体のツールとしても使える） |
