# プログラムの構成と状態ファイル

> Agentic Engineering のプロンプト一覧（`tools/agentic-prompts` で生成）の全ステップが読む文書です。リポジトリの構成、命名の決まり、状態ファイルの雛形だけを載せています。CLI に関する事実は含みません。各ステップが、その時点の調査から取ります。
>
> 英語版: [program-layout.md](./program-layout.md)

## 1. ドキュメントのツリー

```text
docs/
├── program-layout.md (+ .ja.md)                  # この文書
├── INDEX.md                                      # 状態: 文書ごとに 1 行（§4）
├── PROGRESS.md                                   # 状態: ステップごとに 1 行（§4）
├── DIGEST.md                                     # 状態: 追記のみの要約（§4）
├── {slug}-for-cli-agents.{cli}.md (+ .ja.md)     # 横断的な手法の調査。CLI ごとに 1 本
└── {NN}-{slug}/                                  # その他の手法ごとに 1 ディレクトリ
    ├── research.{cli}.md (+ .ja.md)              # ステップ NN-1
    ├── plan.{cli}.md (+ .ja.md)                  # ステップ NN-2
    └── implementation.{cli}.md (+ .ja.md)        # ステップ NN-3
```

命名:

| プレースホルダー | 意味 | 例 |
| --- | --- | --- |
| `{NN}` | プロンプト一覧での手法の番号（2 桁） | `05` |
| `{slug}` | 手法の名前を小文字にし、英数字以外を `-` に置き換えたもの | `spec-plan-engineering` |
| `{cli}` | `claude-code`、`codex`、`antigravity` のいずれか | `claude-code` |

文書の決まり:

- 英語の `.md` が正です。`.ja.md` は、`##` と `###` の見出しが同じ忠実な翻訳です。
- エージェントが読むのは英語の `.md` だけです。
- 調査文書の冒頭には調査日を書きます。公式ドキュメントで確認できなかったものには「未確認」と印を付けます。
- 実装文書の最後には、15 行以内の「後続ステップ向けの要約」セクションを置きます: 何がどこにあり、どう呼び出し、何を避けるか。

## 2. 実装のツリー

最初の実装計画がこの骨格を定義します。以降の計画はそれを維持し、変更は「移行」の項で提案します。

```text
repo/
├── AGENTS.md            # 常時読み込み、15 行以内（雛形は §5）
├── CLAUDE.md            # 「@AGENTS.md」のみ
├── docs/                # §1
├── shared/              # 正本。CLI 非依存の成果物
│   ├── skills/          # Agent Skills（標準フロントマターの SKILL.md と references/、scripts/、assets/）
│   ├── templates/       # 文書のテンプレート（仕様書、計画、進捗メモなど）
│   ├── scripts/         # 決定論的なチェックと補助スクリプト
│   ├── hooks/           # CLI 間で共有するフックのスクリプト
│   └── evals/           # 評価ケースと採点器
├── claude-code/         # Claude Code CLI のインストールルート
├── codex/               # Codex CLI のインストールルート
└── antigravity/         # Antigravity CLI のインストールルート
```

実装の決まり:

- `shared/` には各成果物の正本を 1 つだけ置きます。CLI ルートには、その CLI が共有の成果物を見つけて使うために必要なもの（設定、ルール、リンクや同期コピー、アダプター）だけを置きます。
- CLI ルートは、その CLI の最初の計画が作ります。その中のどこに何を置くか、CLI がどう認識するかは、その CLI の調査から取り、最新の公式ドキュメントで確認します。
- ある手法がすでに別の CLI 向けに実装済みなら、`shared/` を再利用してアダプターを追加します。共有の成果物を CLI ごとにフォークしてはいけません。
- 各 CLI ルートは、その中で CLI を起動すればテストできます。

## 3. 作業の決まり

- 1 つのプロンプトで 1 ステップ。それぞれ新しいセッションで、プロンプト一覧の順に実行します。次のステップへ進む前に結果をレビューします。
- 調査ステップ（`-1`）が調査します。計画（`-2`）と実装（`-3`）のステップは既存のものを読み、依存する事実を確かめるときだけ調べます。
- 各ステップの後に状態ファイル（§4）を更新し、コミットします。コミットメッセージの接頭辞は `{NN}-{slug}({cli}):` です。
- プログラムの状態は、エージェント個人のメモリではなく、状態ファイルと git に置きます。

## 4. 状態ファイル

次のファイルがなければ、以下の内容で作成します。各ステップがこれらを更新します（ファイルの中身はエージェントが読むので英語のままにしています）。

`docs/INDEX.md`:

```markdown
# Index

One line per document. English files only; each has a .ja.md translation.

| Step | CLI | Document | Path | One line |
| --- | --- | --- | --- | --- |
```

`docs/PROGRESS.md`:

```markdown
# Progress

One row per step, in the order of the prompt list.

| Step | CLI | Status | Date | Session | Files | Open questions / approvals |
| --- | --- | --- | --- | --- | --- | --- |
```

`docs/DIGEST.md`:

```markdown
# Digest

Append-only. At most 8 lines per research or plan step, at most 15 lines per implementation step. Newest at the bottom.
Write facts a later step needs (paths, commands, decisions, constraints), not narrative.
```

記入例:

```markdown
| 05-1 | claude-code | Spec / Plan Engineering research | docs/05-spec-plan-engineering/research.claude-code.md | Plan modes, spec and plan formats, implications |
| 05-1 | claude-code | done | 2026-10-05 | ae-05-1-claude-code | docs/05-spec-plan-engineering/research.claude-code.md | — |

## 05-1 claude-code
- ...
```

## 5. リポジトリルートの AGENTS.md の雛形

```markdown
# agentic-engineering
Reference implementation of Agentic Engineering methods for Claude Code CLI, Codex CLI and Antigravity CLI.
- Layout and state: docs/program-layout.md; docs/INDEX.md, docs/PROGRESS.md, docs/DIGEST.md
- shared/ is canonical; claude-code/, codex/, antigravity/ are install roots. Fix shared problems in shared/, not in a CLI root.
- Docs: English .md is the source; .ja.md mirrors its headings. Read only .md files.
- Prompts for each step: tools/agentic-prompts (generated list in prompts/).
```

リポジトリルートの `CLAUDE.md` には `@AGENTS.md` だけを書きます。
