# Agentic Engineering プロンプト一覧（Claude Code CLI）

> `tools/agentic-prompts/generate.py` が `tools/agentic-prompts/config.toml` から生成しました。手で編集せず、設定を変えて再生成してください。
> 構成と状態ファイル: [docs/program-layout.md](../docs/program-layout.md)。ジェネレーターの使い方: [tools/agentic-prompts/README.ja.md](../tools/agentic-prompts/README.ja.md)

## 設定

- CLI: Claude Code CLI
- 横断的な手法（調査のみ。以降のすべての手法に適用）: ① Prompt Engineering、② Context Engineering、③ Memory Engineering、④ Knowledge Engineering
- その他の手法（調査 → 実装計画 → 実装とまとめ）: ⑤ Spec / Plan Engineering、⑥ Verification / Eval Engineering、⑦ Tool Engineering、⑧ Harness / Guardrail Engineering、⑨ Observability Engineering、⑩ Loop Engineering、⑪ Graph Engineering、⑫ Multi-Agent Orchestration、⑬ Production Engineering
- ステップ数: 31

## 使い方

- 上から順に、1 ステップにつき 1 つのプロンプトを、新しいセッションに貼り付けます。前のステップの結果を確認してから次へ進みます。
- 各ステップの後: 差分を確認し、docs/INDEX.md・docs/PROGRESS.md・docs/DIGEST.md の更新を確かめ、コミットします。

## ステップ一覧

1. ①-1 Prompt Engineering: 調査
2. ②-1 Context Engineering: 調査
3. ③-1 Memory Engineering: 調査
4. ④-1 Knowledge Engineering: 調査
5. ⑤-1 Spec / Plan Engineering: 調査
6. ⑤-2 Spec / Plan Engineering: 実装計画
7. ⑤-3 Spec / Plan Engineering: 実装とまとめ
8. ⑥-1 Verification / Eval Engineering: 調査
9. ⑥-2 Verification / Eval Engineering: 実装計画
10. ⑥-3 Verification / Eval Engineering: 実装とまとめ
11. ⑦-1 Tool Engineering: 調査
12. ⑦-2 Tool Engineering: 実装計画
13. ⑦-3 Tool Engineering: 実装とまとめ
14. ⑧-1 Harness / Guardrail Engineering: 調査
15. ⑧-2 Harness / Guardrail Engineering: 実装計画
16. ⑧-3 Harness / Guardrail Engineering: 実装とまとめ
17. ⑨-1 Observability Engineering: 調査
18. ⑨-2 Observability Engineering: 実装計画
19. ⑨-3 Observability Engineering: 実装とまとめ
20. ⑩-1 Loop Engineering: 調査
21. ⑩-2 Loop Engineering: 実装計画
22. ⑩-3 Loop Engineering: 実装とまとめ
23. ⑪-1 Graph Engineering: 調査
24. ⑪-2 Graph Engineering: 実装計画
25. ⑪-3 Graph Engineering: 実装とまとめ
26. ⑫-1 Multi-Agent Orchestration: 調査
27. ⑫-2 Multi-Agent Orchestration: 実装計画
28. ⑫-3 Multi-Agent Orchestration: 実装とまとめ
29. ⑬-1 Production Engineering: 調査
30. ⑬-2 Production Engineering: 実装計画
31. ⑬-3 Production Engineering: 実装とまとめ

## プロンプト

### ① Prompt Engineering（横断的な手法）

#### ①-1 Prompt Engineering: 調査

- 起動: `claude -n ae-01-1-claude-code`
- 書き出し: `docs/prompt-engineering-for-cli-agents.claude-code.md`、`docs/prompt-engineering-for-cli-agents.claude-code.ja.md`

````text
Claude Code CLI 用に Prompt Engineering を調査してまとめてください。ただし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
後続のステップが再調査なしに頼れる調査文書: 定義、原則、Claude Code CLI が現時点で Prompt Engineering をどうサポートしているか、テンプレート、アンチパターン、チェックリスト、出典。

## コンテキスト
- 範囲: 1 ターンと指示ファイルで何を伝えるか: ゴール、コンテキスト、制約、完了条件。検証基準。探索→計画→実装。口調と強調。再利用できるプロンプトのテンプレート。
- これは最初の手法なので、先行する文書はない。
- 調査時点で最新の公式ドキュメントを調べて書く。既存の知識や過去の調査結果に頼らない。二次情報はその旨を明記する。

## 制約
- この手法は横断的な手法であり、後続のすべての手法に適用される。どう適用するかが分かる書き方にする。
- 構成: 定義と隣接する手法との境界。原則。Claude Code CLI がどうサポートしているか（正確なパス・設定・フラグ・コマンド付き）。関係する Claude Code CLI の機能の一覧表。Claude Code CLI 向けの再利用できるテンプレートやプロンプト。アンチパターン。チェックリスト。出典（公式と二次情報を区別）。対象は Claude Code CLI だけにする。
- 文書の冒頭に調査日を書く。公式ドキュメントで確認できなかったものには「未確認」と印を付ける。
- docs/prompt-engineering-for-cli-agents.claude-code.md（英語）と docs/prompt-engineering-for-cli-agents.claude-code.ja.md（見出し構造が同一の忠実な翻訳）を書く。状態ファイル以外のファイルは作らない。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 01-1 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 後続のステップが知るべき原則と制約）を更新する。
- コミットしない。

## 完了条件
- 両ファイルが存在し、## と ### の見出し数が同じであること。すべてのパス・フラグ・コマンドに出典か「未確認」の印があること。
- 最後のメッセージに、書いたファイル、使った公式ソース、未確認の項目、未解決の問いを列挙すること。
````

### ② Context Engineering（横断的な手法）

#### ②-1 Context Engineering: 調査

- 起動: `claude -n ae-02-1-claude-code`
- 書き出し: `docs/context-engineering-for-cli-agents.claude-code.md`、`docs/context-engineering-for-cli-agents.claude-code.ja.md`

````text
Claude Code CLI 用に Context Engineering を調査してまとめてください。ただし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
後続のステップが再調査なしに頼れる調査文書: 定義、原則、Claude Code CLI が現時点で Context Engineering をどうサポートしているか、テンプレート、アンチパターン、チェックリスト、出典。

## コンテキスト
- 範囲: コンテキストウィンドウに何が、いつ、どれだけの間あるか: 読み込みの階層、必要時の取得、サブエージェントでの隔離、コンパクション、ツール出力のフィルタ、プロンプトキャッシュ、使用量の計測。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  それらの上に積み上げる: 内容を繰り返さずに該当セクションへクロスリンクし、同じ構成を保つ。
- 調査時点で最新の公式ドキュメントを調べて書く。既存の知識や過去の調査結果に頼らない。二次情報はその旨を明記する。

## 制約
- この手法は横断的な手法であり、後続のすべての手法に適用される。どう適用するかが分かる書き方にする。
- 構成: 定義と隣接する手法との境界。原則。Claude Code CLI がどうサポートしているか（正確なパス・設定・フラグ・コマンド付き）。関係する Claude Code CLI の機能の一覧表。Claude Code CLI 向けの再利用できるテンプレートやプロンプト。アンチパターン。チェックリスト。出典（公式と二次情報を区別）。対象は Claude Code CLI だけにする。
- 文書の冒頭に調査日を書く。公式ドキュメントで確認できなかったものには「未確認」と印を付ける。
- docs/context-engineering-for-cli-agents.claude-code.md（英語）と docs/context-engineering-for-cli-agents.claude-code.ja.md（見出し構造が同一の忠実な翻訳）を書く。状態ファイル以外のファイルは作らない。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 02-1 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 後続のステップが知るべき原則と制約）を更新する。
- コミットしない。

## 完了条件
- 両ファイルが存在し、## と ### の見出し数が同じであること。すべてのパス・フラグ・コマンドに出典か「未確認」の印があること。
- 最後のメッセージに、書いたファイル、使った公式ソース、未確認の項目、未解決の問いを列挙すること。
````

### ③ Memory Engineering（横断的な手法）

#### ③-1 Memory Engineering: 調査

- 起動: `claude -n ae-03-1-claude-code`
- 書き出し: `docs/memory-engineering-for-cli-agents.claude-code.md`、`docs/memory-engineering-for-cli-agents.claude-code.ja.md`

````text
Claude Code CLI 用に Memory Engineering を調査してまとめてください。ただし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
後続のステップが再調査なしに頼れる調査文書: 定義、原則、Claude Code CLI が現時点で Memory Engineering をどうサポートしているか、テンプレート、アンチパターン、チェックリスト、出典。

## コンテキスト
- 範囲: セッションをまたいで何が残り、どう戻ってくるか: 指示ファイルとエージェントが書くメモリ、索引とトピックファイル、昇格、削除、メモリのセキュリティ、セッションの再開とやり直し、長いタスクの作業記憶ファイル。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  それらの上に積み上げる: 内容を繰り返さずに該当セクションへクロスリンクし、同じ構成を保つ。
- 調査時点で最新の公式ドキュメントを調べて書く。既存の知識や過去の調査結果に頼らない。二次情報はその旨を明記する。

## 制約
- この手法は横断的な手法であり、後続のすべての手法に適用される。どう適用するかが分かる書き方にする。
- 構成: 定義と隣接する手法との境界。原則。Claude Code CLI がどうサポートしているか（正確なパス・設定・フラグ・コマンド付き）。関係する Claude Code CLI の機能の一覧表。Claude Code CLI 向けの再利用できるテンプレートやプロンプト。アンチパターン。チェックリスト。出典（公式と二次情報を区別）。対象は Claude Code CLI だけにする。
- 文書の冒頭に調査日を書く。公式ドキュメントで確認できなかったものには「未確認」と印を付ける。
- docs/memory-engineering-for-cli-agents.claude-code.md（英語）と docs/memory-engineering-for-cli-agents.claude-code.ja.md（見出し構造が同一の忠実な翻訳）を書く。状態ファイル以外のファイルは作らない。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 03-1 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 後続のステップが知るべき原則と制約）を更新する。
- コミットしない。

## 完了条件
- 両ファイルが存在し、## と ### の見出し数が同じであること。すべてのパス・フラグ・コマンドに出典か「未確認」の印があること。
- 最後のメッセージに、書いたファイル、使った公式ソース、未確認の項目、未解決の問いを列挙すること。
````

### ④ Knowledge Engineering（横断的な手法）

#### ④-1 Knowledge Engineering: 調査

- 起動: `claude -n ae-04-1-claude-code`
- 書き出し: `docs/knowledge-engineering-for-cli-agents.claude-code.md`、`docs/knowledge-engineering-for-cli-agents.claude-code.ja.md`

````text
Claude Code CLI 用に Knowledge Engineering を調査してまとめてください。ただし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
後続のステップが再調査なしに頼れる調査文書: 定義、原則、Claude Code CLI が現時点で Knowledge Engineering をどうサポートしているか、テンプレート、アンチパターン、チェックリスト、出典。

## コンテキスト
- 範囲: エージェントが参照できる知識と、その作り方・パッケージ化・検証・共有: 正解の源としてのコード、Agent Skills と段階的な読み込み、ルール、ドキュメント、外部の情報源、プラグイン、評価、担当者とサプライチェーンの安全。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  それらの上に積み上げる: 内容を繰り返さずに該当セクションへクロスリンクし、同じ構成を保つ。
- 調査時点で最新の公式ドキュメントを調べて書く。既存の知識や過去の調査結果に頼らない。二次情報はその旨を明記する。

## 制約
- この手法は横断的な手法であり、後続のすべての手法に適用される。どう適用するかが分かる書き方にする。
- 構成: 定義と隣接する手法との境界。原則。Claude Code CLI がどうサポートしているか（正確なパス・設定・フラグ・コマンド付き）。関係する Claude Code CLI の機能の一覧表。Claude Code CLI 向けの再利用できるテンプレートやプロンプト。アンチパターン。チェックリスト。出典（公式と二次情報を区別）。対象は Claude Code CLI だけにする。
- 文書の冒頭に調査日を書く。公式ドキュメントで確認できなかったものには「未確認」と印を付ける。
- docs/knowledge-engineering-for-cli-agents.claude-code.md（英語）と docs/knowledge-engineering-for-cli-agents.claude-code.ja.md（見出し構造が同一の忠実な翻訳）を書く。状態ファイル以外のファイルは作らない。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 04-1 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 後続のステップが知るべき原則と制約）を更新する。
- コミットしない。

## 完了条件
- 両ファイルが存在し、## と ### の見出し数が同じであること。すべてのパス・フラグ・コマンドに出典か「未確認」の印があること。
- 最後のメッセージに、書いたファイル、使った公式ソース、未確認の項目、未解決の問いを列挙すること。
````

### ⑤ Spec / Plan Engineering（その他の手法）

#### ⑤-1 Spec / Plan Engineering: 調査

- 起動: `claude -n ae-05-1-claude-code`
- 書き出し: `docs/05-spec-plan-engineering/research.claude-code.md`、`docs/05-spec-plan-engineering/research.claude-code.ja.md`

````text
Claude Code CLI 用に Spec / Plan Engineering を調査して、実装の計画にあたって重要なことを含めてまとめてください。ただし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑤-2 が再調査なしに頼れる調査文書: 定義、原則、Claude Code CLI が現時点でこの手法をどうサポートしているか、実装への含意。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。次に、英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
- 範囲: 作る前に決めること。仕様書（何を、なぜ、対象外、検証）と計画（ファイル、ステップ、チェック）を、会話より長生きし、実装中の正となるファイルとして扱う。インタビュー → 仕様 → 計画 → 実装 → 検証の引き継ぎ。計画の同期。ADR。
- 調査の焦点: エージェントがよく従う仕様・計画の形式。CLI ごとのプランモードと、計画がコンパクションをどう乗り切るか。インタビューの技法。タスクの粒度。確認可能な受け入れ基準。JSON の機能リスト。新しいコンテキストでの計画レビュー。計画を省いてよい場合。
- 出発点（ヒントのみ: Claude Code CLI に関する項目を使い、それぞれ最新の公式ドキュメントで確認し、より新しい機能も調べる）: Claude Code のプランモード（Shift+Tab、--permission-mode plan）、Ctrl+G、コンパクション後の計画ファイル再注入、/goal、AskUserQuestion。Codex の /plan、/goal、「計画のマイルストーン 1 を実装して」。Antigravity の /plan、/planning、Ctrl+R や /artifact でレビューする実装計画アーティファクト、artifactReviewPolicy、/grill-me。
- 調査時点で最新の公式ドキュメントを調べて書く。既存の知識や過去の調査結果に頼らない。二次情報は背景として使ってよいが、その旨を明記する。

## 制約
- 文書そのものに 4 つの横断的な手法を適用する（例: 理由を添えた平易な口調、繰り返しではなくセクションへのクロスリンク、1 文 1 事実で時期に依存するものには日付、見出しで振り分けられる構成）。
- 構成は横断的な手法の文書と同じ: 定義と隣接する手法との境界。原則。Claude Code CLI がどうサポートしているか（正確なパス・設定・フラグ・コマンド付き）。関係する Claude Code CLI の機能の一覧表。Claude Code CLI 向けの再利用できるテンプレートやプロンプト。アンチパターン。チェックリスト。出典（公式と二次情報を区別）。対象は Claude Code CLI だけにする。
- 「実装計画への含意」のセクションを追加する: 候補となる成果物と Claude Code CLI での置き場所（今回の調査で確認したもの）。⑤-2 が決めるべき事項。リスク。ドキュメントからは確認できないこと。
- 文書の冒頭に調査日を書く。公式ドキュメントで確認できなかったものには「未確認」と印を付ける。
- docs/05-spec-plan-engineering/research.claude-code.md（英語）と docs/05-spec-plan-engineering/research.claude-code.ja.md（見出し構造が同一の忠実な翻訳）を書く。状態ファイル以外のファイルは作らない。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 05-1 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 実装者が知るべき制約と決定）を更新する。
- コミットしない。

## 完了条件
- 両ファイルが存在し、## と ### の見出し数が同じであること。すべてのパス・フラグ・コマンドに出典か「未確認」の印があること。
- INDEX、PROGRESS、DIGEST が更新されていること。
- 最後のメッセージに、書いたファイル、使った公式ソース、未確認の項目、⑤-2 で決めるべき事項を列挙すること。
````

#### ⑤-2 Spec / Plan Engineering: 実装計画

- 起動: `claude -n ae-05-2-claude-code --permission-mode plan`
- 書き出し: `docs/05-spec-plan-engineering/plan.claude-code.md`、`docs/05-spec-plan-engineering/plan.claude-code.ja.md`

````text
Claude Code CLI 用の Spec / Plan Engineering の実装計画を立ててください。ただし、フォルダ階層は必須とし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑤-3 が何も決め直さずに実行できる計画: 何を、どこに、どの順で作り、各ステップをどう確認するか。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/05-spec-plan-engineering/research.claude-code.md
- 以前の手法の文書はない。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 範囲: 作る前に決めること。仕様書（何を、なぜ、対象外、検証）と計画（ファイル、ステップ、チェック）を、会話より長生きし、実装中の正となるファイルとして扱う。インタビュー → 仕様 → 計画 → 実装 → 検証の引き継ぎ。計画の同期。ADR。
- 想定する成果物（確定または差し替える既定値）: shared/templates（SPEC.md、PLAN.md、progress.md、feature_list.json、ADR.md）。スキル spec-interview、plan-feature、review-plan。shared/scripts/check_plan.py（ステップ内のすべてのパスがツリーにあり、すべてのステップにチェックがある）。CLI ごとに、いつ計画するかの短い常時ルールと、計画レビュアーのサブエージェント。
- リポジトリ構成は docs/program-layout.md に従う（Claude Code CLI での置き場所は調査文書から取る）。プログラムの骨格（shared/ と CLI ルート）がまだなければ、この計画で定義する（docs の状態ファイル、15 行以内のリポジトリルートの AGENTS.md と CLAUDE.md、shared/、claude-code/ を docs/program-layout.md の §2 と §5 のとおりに）。すでにあれば、それに従い、変更は「移行」の項でのみ提案する。
- Claude Code CLI に関する事実は調査文書から取る。計画が依存するパス・フラグ・コマンドは、頼る前に最新の公式ドキュメントで確認する。

## 制約
- 計画のみ: 2 つの計画ファイルと状態ファイル以外は作成も編集もしない。プランモードのままでいる。
- 書き始める前に、答えによって計画が変わる質問を最大 5 つ私にする。自明な質問は省く。AskUserQuestion を使う。
- フォルダ階層は必須: 作成・変更するすべてのファイルの完全なツリー。各項目に 1 行の目的と、使う Claude Code CLI の仕組み（スキル、ルール、フック、設定、エージェント、テンプレート、スクリプト）。
- 4 つの横断的な手法を適用し、「横断的な手法 → この計画での適用方法」の表を、チェックリスト（各横断的な手法の文書 docs/prompt-engineering-for-cli-agents.claude-code.md、docs/context-engineering-for-cli-agents.claude-code.md、docs/memory-engineering-for-cli-agents.claude-code.md、docs/knowledge-engineering-for-cli-agents.claude-code.md のチェックリストのセクション）を使って含める。特に: 常時読み込むファイルは短く保つ。条件付きの知識はパスや glob のルールにする。手順は shared/skills に標準フロントマターの Agent Skills として置き、説明文はトリガー語から始める。決定論的な手順はスクリプトにする。絶対に起きてはいけないことはフックか権限ルールにする。状態は索引の上限を意識してファイルに置く。
- ステップは小さく、順序付きにする。各ステップに: 触るファイル。うまくいったことを証明するチェック（コマンドまたは目視）。示すべき証拠。私の承認が必要なステップには印を付ける。
- セクション: 範囲と対象外 · 成果物表（パス、種類、Claude Code CLI の仕組み、読み込み階層、担当者） · フォルダ階層 · ステップ · 検証（⑤-3 がどう証明するか） · リスクと未解決の問い · ロールバック · 移行（既存の骨格を変える場合のみ）。
- docs/05-spec-plan-engineering/plan.claude-code.md（英語）と docs/05-spec-plan-engineering/plan.claude-code.ja.md（見出し構造が同一）を書く。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 05-2 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 成果物と決定）を更新する。
- コミットしない。

## 完了条件
- ステップに出てくるすべてのパスがツリーにあり、ツリーのすべての項目がいずれかのステップに出てくること。
- すべてのステップにチェックがあること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 10 行以内の計画の要約、私の承認が必要な決定（質問の形で）、未確認の事項。
````

#### ⑤-3 Spec / Plan Engineering: 実装とまとめ

- 起動: `claude -n ae-05-3-claude-code`
- 書き出し: `docs/05-spec-plan-engineering/implementation.claude-code.md`、`docs/05-spec-plan-engineering/implementation.claude-code.ja.md`

````text
承認済みの計画に従って Claude Code CLI 用の Spec / Plan Engineering の実装を進めて、最後に内容をまとめてください。ただし、md ファイルは英語版を .md、和訳版を .ja.md にしてください。

## ゴール
docs/05-spec-plan-engineering/plan.claude-code.md のすべての成果物が存在し、Claude Code CLI の中で検証され、後続のステップが積み上げられるように文書化されていること。

## コンテキスト
- docs/INDEX.md、docs/DIGEST.md、docs/PROGRESS.md を読み、`git log --oneline -20` を実行する。編集前に作業ツリーがきれいであることを確認する。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
- 以前の手法の文書はない。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 承認済みの計画が正。その「横断的な手法 → 適用方法」の表は拘束力を持つ。

## 制約
- 計画のステップを順に実行する。各ステップの後にそのチェックを実行し、出力を見せる。チェックが 2 回失敗したか、判断が必要なら、止めて質問する。
- 計画のツリー外のファイルには触らない。やむを得ない場合は、理由とともに「逸脱」の項に記録する。
- 作ったものに対して 4 つの横断的な手法のルールを検証する: SKILL.md は 500 行未満で標準フロントマター。説明文は 1,024 文字以内で、用途とトリガー語から始まる。常時読み込む指示ファイルは短い。決定論的な手順はスクリプト。絶対に起きてはいけないことはフックか権限ルール。状態ファイルは索引の上限内。
- Claude Code CLI の中でテストする: `cd claude-code && claude -p "List the skills, rules and hooks available to you" --output-format json` を実行し、計画した項目が現れることを確認する。対話的に /skills, /context, /hooks でも確認する。次に、計画の「検証」セクションにあるエンドツーエンドのシナリオ（受け入れの証拠: 対象の CLI で、スキルがおもちゃの機能に対して SPEC.md と PLAN.md を生成する。check_plan が通る。新しいコンテキストのレビュアーが不足を見つけない。コンパクション後も計画に従っている。）を実行し、証拠（コマンド、出力、ファイル）を残す。
- まとめる前に、新しいコンテキストのサブエージェント、または /code-review に結果と計画を照合させる。正しさや要件に関わる不足は直し、それ以外は「既知の不足」に列挙する。
- docs/05-spec-plan-engineering/implementation.claude-code.md（英語）と docs/05-spec-plan-engineering/implementation.claude-code.ja.md を、次の内容で書く: 作ったもの（最終的なツリー） · 使い方（コマンド、プロンプト） · 検証の証拠 · 4 つの横断的な手法をどう適用したか · 逸脱 · 既知の不足 · 「後続ステップ向けの要約」（15 行以内: 何がどこにあり、どう呼び出し、何を避けるか）。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 05-3 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（15 行以内の要約を追記）を更新する。
- 論理的な単位ごとに、`05-spec-plan-engineering(claude-code):` を接頭辞にしたメッセージでコミットする。

## 完了条件
- 計画のすべてのステップがチェック済みで、証拠が実装文書にあること。
- レビュアーが未解決の正しさの不足を報告していないか、「既知の不足」に列挙されていること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 15 行以内の要約、逸脱、既知の不足、次のステップへの提言。
````

### ⑥ Verification / Eval Engineering（その他の手法）

#### ⑥-1 Verification / Eval Engineering: 調査

- 起動: `claude -n ae-06-1-claude-code`
- 書き出し: `docs/06-verification-eval-engineering/research.claude-code.md`、`docs/06-verification-eval-engineering/research.claude-code.ja.md`

````text
Claude Code CLI 用に Verification / Eval Engineering を調査して、実装の計画にあたって重要なことを含めてまとめてください。ただし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑥-2 が再調査なしに頼れる調査文書: 定義、原則、Claude Code CLI が現時点でこの手法をどうサポートしているか、実装への含意。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。次に、英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
- 範囲: 成果を証明すること: エージェントが実行できるチェック（テスト、ビルド、リント、フィクスチャ差分、スクリーンショット）、主張ではなく証拠、ゲート（ゴール条件、Stop フック）、新しいコンテキストでの独立したレビュー、そしてエージェント層そのもの（スキル、ルール、プロンプト）の評価: あり・なしの基準線、発動テスト、回帰。
- 調査の焦点: 検証の戦略とプロンプトでの表現。/goal の評価器と停滞。Stop フックのゲートと上限。レビューコマンド。機械で確認できる結果のための構造化出力。スキルの評価とベンチマーク。評価ケースの設計と不安定さ。見た目の検証。テスト出力のフィルタ。
- 出発点（ヒントのみ: Claude Code CLI に関する項目を使い、それぞれ最新の公式ドキュメントで確認し、より新しい機能も調べる）: Claude Code の /verify、/goal、Stop フック、検証用サブエージェント、/code-review、claude plugin eval、skill-creator、PreToolUse によるテスト出力フィルタ、--output-format json。Codex の /review、codex exec --output-schema、Stop フック。Antigravity のアーティファクトレビュー、/goal、/browser のスクリーンショット、Stop と PostInvocation フック（terminationBehavior）。
- 調査時点で最新の公式ドキュメントを調べて書く。既存の知識や過去の調査結果に頼らない。二次情報は背景として使ってよいが、その旨を明記する。

## 制約
- 文書そのものに 4 つの横断的な手法を適用する（例: 理由を添えた平易な口調、繰り返しではなくセクションへのクロスリンク、1 文 1 事実で時期に依存するものには日付、見出しで振り分けられる構成）。
- 構成は横断的な手法の文書と同じ: 定義と隣接する手法との境界。原則。Claude Code CLI がどうサポートしているか（正確なパス・設定・フラグ・コマンド付き）。関係する Claude Code CLI の機能の一覧表。Claude Code CLI 向けの再利用できるテンプレートやプロンプト。アンチパターン。チェックリスト。出典（公式と二次情報を区別）。対象は Claude Code CLI だけにする。
- 「実装計画への含意」のセクションを追加する: 候補となる成果物と Claude Code CLI での置き場所（今回の調査で確認したもの）。⑥-2 が決めるべき事項。リスク。ドキュメントからは確認できないこと。
- 文書の冒頭に調査日を書く。公式ドキュメントで確認できなかったものには「未確認」と印を付ける。
- docs/06-verification-eval-engineering/research.claude-code.md（英語）と docs/06-verification-eval-engineering/research.claude-code.ja.md（見出し構造が同一の忠実な翻訳）を書く。状態ファイル以外のファイルは作らない。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 06-1 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 実装者が知るべき制約と決定）を更新する。
- コミットしない。

## 完了条件
- 両ファイルが存在し、## と ### の見出し数が同じであること。すべてのパス・フラグ・コマンドに出典か「未確認」の印があること。
- INDEX、PROGRESS、DIGEST が更新されていること。
- 最後のメッセージに、書いたファイル、使った公式ソース、未確認の項目、⑥-2 で決めるべき事項を列挙すること。
````

#### ⑥-2 Verification / Eval Engineering: 実装計画

- 起動: `claude -n ae-06-2-claude-code --permission-mode plan`
- 書き出し: `docs/06-verification-eval-engineering/plan.claude-code.md`、`docs/06-verification-eval-engineering/plan.claude-code.ja.md`

````text
Claude Code CLI 用の Verification / Eval Engineering の実装計画を立ててください。ただし、フォルダ階層は必須とし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑥-3 が何も決め直さずに実行できる計画: 何を、どこに、どの順で作り、各ステップをどう確認するか。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 範囲: 成果を証明すること: エージェントが実行できるチェック（テスト、ビルド、リント、フィクスチャ差分、スクリーンショット）、主張ではなく証拠、ゲート（ゴール条件、Stop フック）、新しいコンテキストでの独立したレビュー、そしてエージェント層そのもの（スキル、ルール、プロンプト）の評価: あり・なしの基準線、発動テスト、回帰。
- 想定する成果物（確定または差し替える既定値）: shared/evals（スキルごとのケース: プロンプト、期待値、採点器）。shared/scripts/run_evals。スキル verify-change と review-against-plan。CLI ごとのレビュアーエージェント。Stop ゲートのスクリプト。テスト出力フィルタのフック。実装文書用の証拠セクションのテンプレート。
- リポジトリ構成は docs/program-layout.md に従う（Claude Code CLI での置き場所は調査文書から取る）。プログラムの骨格（shared/ と CLI ルート）がまだなければ、この計画で定義する（docs の状態ファイル、15 行以内のリポジトリルートの AGENTS.md と CLAUDE.md、shared/、claude-code/ を docs/program-layout.md の §2 と §5 のとおりに）。すでにあれば、それに従い、変更は「移行」の項でのみ提案する。
- Claude Code CLI に関する事実は調査文書から取る。計画が依存するパス・フラグ・コマンドは、頼る前に最新の公式ドキュメントで確認する。

## 制約
- 計画のみ: 2 つの計画ファイルと状態ファイル以外は作成も編集もしない。プランモードのままでいる。
- 書き始める前に、答えによって計画が変わる質問を最大 5 つ私にする。自明な質問は省く。AskUserQuestion を使う。
- フォルダ階層は必須: 作成・変更するすべてのファイルの完全なツリー。各項目に 1 行の目的と、使う Claude Code CLI の仕組み（スキル、ルール、フック、設定、エージェント、テンプレート、スクリプト）。
- 4 つの横断的な手法を適用し、「横断的な手法 → この計画での適用方法」の表を、チェックリスト（各横断的な手法の文書 docs/prompt-engineering-for-cli-agents.claude-code.md、docs/context-engineering-for-cli-agents.claude-code.md、docs/memory-engineering-for-cli-agents.claude-code.md、docs/knowledge-engineering-for-cli-agents.claude-code.md のチェックリストのセクション）を使って含める。特に: 常時読み込むファイルは短く保つ。条件付きの知識はパスや glob のルールにする。手順は shared/skills に標準フロントマターの Agent Skills として置き、説明文はトリガー語から始める。決定論的な手順はスクリプトにする。絶対に起きてはいけないことはフックか権限ルールにする。状態は索引の上限を意識してファイルに置く。
- ステップは小さく、順序付きにする。各ステップに: 触るファイル。うまくいったことを証明するチェック（コマンドまたは目視）。示すべき証拠。私の承認が必要なステップには印を付ける。
- セクション: 範囲と対象外 · 成果物表（パス、種類、Claude Code CLI の仕組み、読み込み階層、担当者） · フォルダ階層 · ステップ · 検証（⑥-3 がどう証明するか） · リスクと未解決の問い · ロールバック · 移行（既存の骨格を変える場合のみ）。
- docs/06-verification-eval-engineering/plan.claude-code.md（英語）と docs/06-verification-eval-engineering/plan.claude-code.ja.md（見出し構造が同一）を書く。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 06-2 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 成果物と決定）を更新する。
- コミットしない。

## 完了条件
- ステップに出てくるすべてのパスがツリーにあり、ツリーのすべての項目がいずれかのステップに出てくること。
- すべてのステップにチェックがあること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 10 行以内の計画の要約、私の承認が必要な決定（質問の形で）、未確認の事項。
````

#### ⑥-3 Verification / Eval Engineering: 実装とまとめ

- 起動: `claude -n ae-06-3-claude-code`
- 書き出し: `docs/06-verification-eval-engineering/implementation.claude-code.md`、`docs/06-verification-eval-engineering/implementation.claude-code.ja.md`

````text
承認済みの計画に従って Claude Code CLI 用の Verification / Eval Engineering の実装を進めて、最後に内容をまとめてください。ただし、md ファイルは英語版を .md、和訳版を .ja.md にしてください。

## ゴール
docs/06-verification-eval-engineering/plan.claude-code.md のすべての成果物が存在し、Claude Code CLI の中で検証され、後続のステップが積み上げられるように文書化されていること。

## コンテキスト
- docs/INDEX.md、docs/DIGEST.md、docs/PROGRESS.md を読み、`git log --oneline -20` を実行する。編集前に作業ツリーがきれいであることを確認する。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/06-verification-eval-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 承認済みの計画が正。その「横断的な手法 → 適用方法」の表は拘束力を持つ。

## 制約
- 計画のステップを順に実行する。各ステップの後にそのチェックを実行し、出力を見せる。チェックが 2 回失敗したか、判断が必要なら、止めて質問する。
- 計画のツリー外のファイルには触らない。やむを得ない場合は、理由とともに「逸脱」の項に記録する。
- 作ったものに対して 4 つの横断的な手法のルールを検証する: SKILL.md は 500 行未満で標準フロントマター。説明文は 1,024 文字以内で、用途とトリガー語から始まる。常時読み込む指示ファイルは短い。決定論的な手順はスクリプト。絶対に起きてはいけないことはフックか権限ルール。状態ファイルは索引の上限内。
- Claude Code CLI の中でテストする: `cd claude-code && claude -p "List the skills, rules and hooks available to you" --output-format json` を実行し、計画した項目が現れることを確認する。対話的に /skills, /context, /hooks でも確認する。次に、計画の「検証」セクションにあるエンドツーエンドのシナリオ（受け入れの証拠: 以前のスキルのあり・なし評価と結果ファイル。Stop ゲートが仕込んだ失敗状態を止め、修正後に解放する。前の分野の実装に対する review-against-plan の実行。）を実行し、証拠（コマンド、出力、ファイル）を残す。
- まとめる前に、新しいコンテキストのサブエージェント、または /code-review に結果と計画を照合させる。正しさや要件に関わる不足は直し、それ以外は「既知の不足」に列挙する。
- docs/06-verification-eval-engineering/implementation.claude-code.md（英語）と docs/06-verification-eval-engineering/implementation.claude-code.ja.md を、次の内容で書く: 作ったもの（最終的なツリー） · 使い方（コマンド、プロンプト） · 検証の証拠 · 4 つの横断的な手法をどう適用したか · 逸脱 · 既知の不足 · 「後続ステップ向けの要約」（15 行以内: 何がどこにあり、どう呼び出し、何を避けるか）。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 06-3 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（15 行以内の要約を追記）を更新する。
- 論理的な単位ごとに、`06-verification-eval-engineering(claude-code):` を接頭辞にしたメッセージでコミットする。

## 完了条件
- 計画のすべてのステップがチェック済みで、証拠が実装文書にあること。
- レビュアーが未解決の正しさの不足を報告していないか、「既知の不足」に列挙されていること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 15 行以内の要約、逸脱、既知の不足、次のステップへの提言。
````

### ⑦ Tool Engineering（その他の手法）

#### ⑦-1 Tool Engineering: 調査

- 起動: `claude -n ae-07-1-claude-code`
- 書き出し: `docs/07-tool-engineering/research.claude-code.md`、`docs/07-tool-engineering/research.claude-code.ja.md`

````text
Claude Code CLI 用に Tool Engineering を調査して、実装の計画にあたって重要なことを含めてまとめてください。ただし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑦-2 が再調査なしに頼れる調査文書: 定義、原則、Claude Code CLI が現時点でこの手法をどうサポートしているか、実装への含意。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。次に、英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
- 範囲: エージェントができること: 明確で重複のない説明を持つ MCP サーバー、CLI ラッパー、スキルのスクリプト。上限のある、絞られた出力。安全な既定値。許可リスト。発見のコスト。
- 調査の焦点: ツールの設計（自己完結、エラーに強い、用途が明確、重複なし）。CLI ごとの MCP 設定。一覧のコストと遅延読み込み。出力の上限とフィルタ。CLI と MCP のトレードオフ。対処できるエラーメッセージ。冪等性と dry-run フラグ。エージェントごとのツール制限。ツール用の秘密情報。ツール単体のテスト。
- 出発点（ヒントのみ: Claude Code CLI に関する項目を使い、それぞれ最新の公式ドキュメントで確認し、より新しい機能も調べる）: Claude Code の claude mcp add、MCP スキーマの遅延読み込みとツール検索（ENABLE_TOOL_SEARCH）、/mcp、コードインテリジェンスプラグイン、PreToolUse の updatedInput、スキルの allowed-tools。Codex の codex mcp add、mcp_servers.<id>（enabled_tools、tool_timeout_sec、output_token_limit）、tool_output_token_limit、agents/openai.yaml でのスキルの MCP 依存。Antigravity の .agents/mcp_config.json、/mcp、サブエージェントの tools と mcpServers、サイドカー。
- 調査時点で最新の公式ドキュメントを調べて書く。既存の知識や過去の調査結果に頼らない。二次情報は背景として使ってよいが、その旨を明記する。

## 制約
- 文書そのものに 4 つの横断的な手法を適用する（例: 理由を添えた平易な口調、繰り返しではなくセクションへのクロスリンク、1 文 1 事実で時期に依存するものには日付、見出しで振り分けられる構成）。
- 構成は横断的な手法の文書と同じ: 定義と隣接する手法との境界。原則。Claude Code CLI がどうサポートしているか（正確なパス・設定・フラグ・コマンド付き）。関係する Claude Code CLI の機能の一覧表。Claude Code CLI 向けの再利用できるテンプレートやプロンプト。アンチパターン。チェックリスト。出典（公式と二次情報を区別）。対象は Claude Code CLI だけにする。
- 「実装計画への含意」のセクションを追加する: 候補となる成果物と Claude Code CLI での置き場所（今回の調査で確認したもの）。⑦-2 が決めるべき事項。リスク。ドキュメントからは確認できないこと。
- 文書の冒頭に調査日を書く。公式ドキュメントで確認できなかったものには「未確認」と印を付ける。
- docs/07-tool-engineering/research.claude-code.md（英語）と docs/07-tool-engineering/research.claude-code.ja.md（見出し構造が同一の忠実な翻訳）を書く。状態ファイル以外のファイルは作らない。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 07-1 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 実装者が知るべき制約と決定）を更新する。
- コミットしない。

## 完了条件
- 両ファイルが存在し、## と ### の見出し数が同じであること。すべてのパス・フラグ・コマンドに出典か「未確認」の印があること。
- INDEX、PROGRESS、DIGEST が更新されていること。
- 最後のメッセージに、書いたファイル、使った公式ソース、未確認の項目、⑦-2 で決めるべき事項を列挙すること。
````

#### ⑦-2 Tool Engineering: 実装計画

- 起動: `claude -n ae-07-2-claude-code --permission-mode plan`
- 書き出し: `docs/07-tool-engineering/plan.claude-code.md`、`docs/07-tool-engineering/plan.claude-code.ja.md`

````text
Claude Code CLI 用の Tool Engineering の実装計画を立ててください。ただし、フォルダ階層は必須とし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑦-3 が何も決め直さずに実行できる計画: 何を、どこに、どの順で作り、各ステップをどう確認するか。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/07-tool-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/06-verification-eval-engineering/plan.claude-code.md
  - docs/06-verification-eval-engineering/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 範囲: エージェントができること: 明確で重複のない説明を持つ MCP サーバー、CLI ラッパー、スキルのスクリプト。上限のある、絞られた出力。安全な既定値。許可リスト。発見のコスト。
- 想定する成果物（確定または差し替える既定値）: shared/tools/<tool>（README、スキーマ、テスト付きの MCP サーバーまたは CLI ラッパー）。ツール記述のスタイルガイドを持つ author-tool スキル。出力フィルタのスクリプト。CLI ごとの MCP 設定と許可リスト。
- リポジトリ構成は docs/program-layout.md に従う（Claude Code CLI での置き場所は調査文書から取る）。プログラムの骨格（shared/ と CLI ルート）がまだなければ、この計画で定義する（docs の状態ファイル、15 行以内のリポジトリルートの AGENTS.md と CLAUDE.md、shared/、claude-code/ を docs/program-layout.md の §2 と §5 のとおりに）。すでにあれば、それに従い、変更は「移行」の項でのみ提案する。
- Claude Code CLI に関する事実は調査文書から取る。計画が依存するパス・フラグ・コマンドは、頼る前に最新の公式ドキュメントで確認する。

## 制約
- 計画のみ: 2 つの計画ファイルと状態ファイル以外は作成も編集もしない。プランモードのままでいる。
- 書き始める前に、答えによって計画が変わる質問を最大 5 つ私にする。自明な質問は省く。AskUserQuestion を使う。
- フォルダ階層は必須: 作成・変更するすべてのファイルの完全なツリー。各項目に 1 行の目的と、使う Claude Code CLI の仕組み（スキル、ルール、フック、設定、エージェント、テンプレート、スクリプト）。
- 4 つの横断的な手法を適用し、「横断的な手法 → この計画での適用方法」の表を、チェックリスト（各横断的な手法の文書 docs/prompt-engineering-for-cli-agents.claude-code.md、docs/context-engineering-for-cli-agents.claude-code.md、docs/memory-engineering-for-cli-agents.claude-code.md、docs/knowledge-engineering-for-cli-agents.claude-code.md のチェックリストのセクション）を使って含める。特に: 常時読み込むファイルは短く保つ。条件付きの知識はパスや glob のルールにする。手順は shared/skills に標準フロントマターの Agent Skills として置き、説明文はトリガー語から始める。決定論的な手順はスクリプトにする。絶対に起きてはいけないことはフックか権限ルールにする。状態は索引の上限を意識してファイルに置く。
- ステップは小さく、順序付きにする。各ステップに: 触るファイル。うまくいったことを証明するチェック（コマンドまたは目視）。示すべき証拠。私の承認が必要なステップには印を付ける。
- セクション: 範囲と対象外 · 成果物表（パス、種類、Claude Code CLI の仕組み、読み込み階層、担当者） · フォルダ階層 · ステップ · 検証（⑦-3 がどう証明するか） · リスクと未解決の問い · ロールバック · 移行（既存の骨格を変える場合のみ）。
- docs/07-tool-engineering/plan.claude-code.md（英語）と docs/07-tool-engineering/plan.claude-code.ja.md（見出し構造が同一）を書く。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 07-2 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 成果物と決定）を更新する。
- コミットしない。

## 完了条件
- ステップに出てくるすべてのパスがツリーにあり、ツリーのすべての項目がいずれかのステップに出てくること。
- すべてのステップにチェックがあること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 10 行以内の計画の要約、私の承認が必要な決定（質問の形で）、未確認の事項。
````

#### ⑦-3 Tool Engineering: 実装とまとめ

- 起動: `claude -n ae-07-3-claude-code`
- 書き出し: `docs/07-tool-engineering/implementation.claude-code.md`、`docs/07-tool-engineering/implementation.claude-code.ja.md`

````text
承認済みの計画に従って Claude Code CLI 用の Tool Engineering の実装を進めて、最後に内容をまとめてください。ただし、md ファイルは英語版を .md、和訳版を .ja.md にしてください。

## ゴール
docs/07-tool-engineering/plan.claude-code.md のすべての成果物が存在し、Claude Code CLI の中で検証され、後続のステップが積み上げられるように文書化されていること。

## コンテキスト
- docs/INDEX.md、docs/DIGEST.md、docs/PROGRESS.md を読み、`git log --oneline -20` を実行する。編集前に作業ツリーがきれいであることを確認する。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/07-tool-engineering/research.claude-code.md
  - docs/07-tool-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/06-verification-eval-engineering/plan.claude-code.md
  - docs/06-verification-eval-engineering/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 承認済みの計画が正。その「横断的な手法 → 適用方法」の表は拘束力を持つ。

## 制約
- 計画のステップを順に実行する。各ステップの後にそのチェックを実行し、出力を見せる。チェックが 2 回失敗したか、判断が必要なら、止めて質問する。
- 計画のツリー外のファイルには触らない。やむを得ない場合は、理由とともに「逸脱」の項に記録する。
- 作ったものに対して 4 つの横断的な手法のルールを検証する: SKILL.md は 500 行未満で標準フロントマター。説明文は 1,024 文字以内で、用途とトリガー語から始まる。常時読み込む指示ファイルは短い。決定論的な手順はスクリプト。絶対に起きてはいけないことはフックか権限ルール。状態ファイルは索引の上限内。
- Claude Code CLI の中でテストする: `cd claude-code && claude -p "List the skills, rules and hooks available to you" --output-format json` を実行し、計画した項目が現れることを確認する。対話的に /skills, /context, /hooks でも確認する。次に、計画の「検証」セクションにあるエンドツーエンドのシナリオ（受け入れの証拠: ツールが CLI で認識される（/mcp）。シナリオがそれを使う。出力が設定した上限内に収まる。不正な入力に対処可能なエラーが返る。）を実行し、証拠（コマンド、出力、ファイル）を残す。
- まとめる前に、新しいコンテキストのサブエージェント、または /code-review に結果と計画を照合させる。正しさや要件に関わる不足は直し、それ以外は「既知の不足」に列挙する。
- docs/07-tool-engineering/implementation.claude-code.md（英語）と docs/07-tool-engineering/implementation.claude-code.ja.md を、次の内容で書く: 作ったもの（最終的なツリー） · 使い方（コマンド、プロンプト） · 検証の証拠 · 4 つの横断的な手法をどう適用したか · 逸脱 · 既知の不足 · 「後続ステップ向けの要約」（15 行以内: 何がどこにあり、どう呼び出し、何を避けるか）。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 07-3 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（15 行以内の要約を追記）を更新する。
- 論理的な単位ごとに、`07-tool-engineering(claude-code):` を接頭辞にしたメッセージでコミットする。

## 完了条件
- 計画のすべてのステップがチェック済みで、証拠が実装文書にあること。
- レビュアーが未解決の正しさの不足を報告していないか、「既知の不足」に列挙されていること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 15 行以内の要約、逸脱、既知の不足、次のステップへの提言。
````

### ⑧ Harness / Guardrail Engineering（その他の手法）

#### ⑧-1 Harness / Guardrail Engineering: 調査

- 起動: `claude -n ae-08-1-claude-code`
- 書き出し: `docs/08-harness-guardrail-engineering/research.claude-code.md`、`docs/08-harness-guardrail-engineering/research.claude-code.ja.md`

````text
Claude Code CLI 用に Harness / Guardrail Engineering を調査して、実装の計画にあたって重要なことを含めてまとめてください。ただし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑧-2 が再調査なしに頼れる調査文書: 定義、原則、Claude Code CLI が現時点でこの手法をどうサポートしているか、実装への含意。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。次に、英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
- 範囲: 決定論的な境界: フック、権限モード、サンドボックス、deny ルール、承認ポリシー。プロンプトインジェクションへの対策。秘密情報の保護。長時間実行のハーネス（初期化スクリプト、機能リスト、進捗、セッション開始時の手順）。
- 調査の焦点: CLI ごとのフックのイベントと能力。権限とサンドボックスのモデルと既定値。影響範囲に合わせたモード選択。PreToolUse の拒否・許可・書き換え。Stop ゲート。信頼できない内容の扱い。管理による強制。長時間実行のハーネスパターン。禁止操作を試みてガードレールをテストすること。
- 出発点（ヒントのみ: Claude Code CLI に関する項目を使い、それぞれ最新の公式ドキュメントで確認し、より新しい機能も調べる）: Claude Code のフック（PreToolUse、PostToolUse、Stop、SessionStart、SessionEnd、InstructionsLoaded）、権限モード、/permissions、/sandbox、permissions.deny の Read(...) ルール、管理設定、disableSkillShellExecution。Codex の --sandbox、approval_policy、PermissionRequest を含むフック、requirements.toml、memories.disable_on_external_context。Antigravity の toolPermission、enableTerminalSandbox、/permissions、artifactReviewPolicy、フック（PreToolUse、PostToolUse、PreInvocation、PostInvocation、Stop）、commandExecutionPolicy。
- 調査時点で最新の公式ドキュメントを調べて書く。既存の知識や過去の調査結果に頼らない。二次情報は背景として使ってよいが、その旨を明記する。

## 制約
- 文書そのものに 4 つの横断的な手法を適用する（例: 理由を添えた平易な口調、繰り返しではなくセクションへのクロスリンク、1 文 1 事実で時期に依存するものには日付、見出しで振り分けられる構成）。
- 構成は横断的な手法の文書と同じ: 定義と隣接する手法との境界。原則。Claude Code CLI がどうサポートしているか（正確なパス・設定・フラグ・コマンド付き）。関係する Claude Code CLI の機能の一覧表。Claude Code CLI 向けの再利用できるテンプレートやプロンプト。アンチパターン。チェックリスト。出典（公式と二次情報を区別）。対象は Claude Code CLI だけにする。
- 「実装計画への含意」のセクションを追加する: 候補となる成果物と Claude Code CLI での置き場所（今回の調査で確認したもの）。⑧-2 が決めるべき事項。リスク。ドキュメントからは確認できないこと。
- 文書の冒頭に調査日を書く。公式ドキュメントで確認できなかったものには「未確認」と印を付ける。
- docs/08-harness-guardrail-engineering/research.claude-code.md（英語）と docs/08-harness-guardrail-engineering/research.claude-code.ja.md（見出し構造が同一の忠実な翻訳）を書く。状態ファイル以外のファイルは作らない。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 08-1 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 実装者が知るべき制約と決定）を更新する。
- コミットしない。

## 完了条件
- 両ファイルが存在し、## と ### の見出し数が同じであること。すべてのパス・フラグ・コマンドに出典か「未確認」の印があること。
- INDEX、PROGRESS、DIGEST が更新されていること。
- 最後のメッセージに、書いたファイル、使った公式ソース、未確認の項目、⑧-2 で決めるべき事項を列挙すること。
````

#### ⑧-2 Harness / Guardrail Engineering: 実装計画

- 起動: `claude -n ae-08-2-claude-code --permission-mode plan`
- 書き出し: `docs/08-harness-guardrail-engineering/plan.claude-code.md`、`docs/08-harness-guardrail-engineering/plan.claude-code.ja.md`

````text
Claude Code CLI 用の Harness / Guardrail Engineering の実装計画を立ててください。ただし、フォルダ階層は必須とし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑧-3 が何も決め直さずに実行できる計画: 何を、どこに、どの順で作り、各ステップをどう確認するか。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/08-harness-guardrail-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/06-verification-eval-engineering/plan.claude-code.md
  - docs/06-verification-eval-engineering/implementation.claude-code.md
  - docs/07-tool-engineering/research.claude-code.md
  - docs/07-tool-engineering/plan.claude-code.md
  - docs/07-tool-engineering/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 範囲: 決定論的な境界: フック、権限モード、サンドボックス、deny ルール、承認ポリシー。プロンプトインジェクションへの対策。秘密情報の保護。長時間実行のハーネス（初期化スクリプト、機能リスト、進捗、セッション開始時の手順）。
- 想定する成果物（確定または差し替える既定値）: shared/hooks のスクリプトを使う CLI ごとのフック設定。権限プリセット（開発、CI、無人）。init.sh。shared/evals/guardrails のガードレールテスト。短い常時のインジェクション対策ルール。秘密情報スキャンのフック。
- リポジトリ構成は docs/program-layout.md に従う（Claude Code CLI での置き場所は調査文書から取る）。プログラムの骨格（shared/ と CLI ルート）がまだなければ、この計画で定義する（docs の状態ファイル、15 行以内のリポジトリルートの AGENTS.md と CLAUDE.md、shared/、claude-code/ を docs/program-layout.md の §2 と §5 のとおりに）。すでにあれば、それに従い、変更は「移行」の項でのみ提案する。
- Claude Code CLI に関する事実は調査文書から取る。計画が依存するパス・フラグ・コマンドは、頼る前に最新の公式ドキュメントで確認する。

## 制約
- 計画のみ: 2 つの計画ファイルと状態ファイル以外は作成も編集もしない。プランモードのままでいる。
- 書き始める前に、答えによって計画が変わる質問を最大 5 つ私にする。自明な質問は省く。AskUserQuestion を使う。
- フォルダ階層は必須: 作成・変更するすべてのファイルの完全なツリー。各項目に 1 行の目的と、使う Claude Code CLI の仕組み（スキル、ルール、フック、設定、エージェント、テンプレート、スクリプト）。
- 4 つの横断的な手法を適用し、「横断的な手法 → この計画での適用方法」の表を、チェックリスト（各横断的な手法の文書 docs/prompt-engineering-for-cli-agents.claude-code.md、docs/context-engineering-for-cli-agents.claude-code.md、docs/memory-engineering-for-cli-agents.claude-code.md、docs/knowledge-engineering-for-cli-agents.claude-code.md のチェックリストのセクション）を使って含める。特に: 常時読み込むファイルは短く保つ。条件付きの知識はパスや glob のルールにする。手順は shared/skills に標準フロントマターの Agent Skills として置き、説明文はトリガー語から始める。決定論的な手順はスクリプトにする。絶対に起きてはいけないことはフックか権限ルールにする。状態は索引の上限を意識してファイルに置く。
- ステップは小さく、順序付きにする。各ステップに: 触るファイル。うまくいったことを証明するチェック（コマンドまたは目視）。示すべき証拠。私の承認が必要なステップには印を付ける。
- セクション: 範囲と対象外 · 成果物表（パス、種類、Claude Code CLI の仕組み、読み込み階層、担当者） · フォルダ階層 · ステップ · 検証（⑧-3 がどう証明するか） · リスクと未解決の問い · ロールバック · 移行（既存の骨格を変える場合のみ）。
- docs/08-harness-guardrail-engineering/plan.claude-code.md（英語）と docs/08-harness-guardrail-engineering/plan.claude-code.ja.md（見出し構造が同一）を書く。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 08-2 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 成果物と決定）を更新する。
- コミットしない。

## 完了条件
- ステップに出てくるすべてのパスがツリーにあり、ツリーのすべての項目がいずれかのステップに出てくること。
- すべてのステップにチェックがあること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 10 行以内の計画の要約、私の承認が必要な決定（質問の形で）、未確認の事項。
````

#### ⑧-3 Harness / Guardrail Engineering: 実装とまとめ

- 起動: `claude -n ae-08-3-claude-code`
- 書き出し: `docs/08-harness-guardrail-engineering/implementation.claude-code.md`、`docs/08-harness-guardrail-engineering/implementation.claude-code.ja.md`

````text
承認済みの計画に従って Claude Code CLI 用の Harness / Guardrail Engineering の実装を進めて、最後に内容をまとめてください。ただし、md ファイルは英語版を .md、和訳版を .ja.md にしてください。

## ゴール
docs/08-harness-guardrail-engineering/plan.claude-code.md のすべての成果物が存在し、Claude Code CLI の中で検証され、後続のステップが積み上げられるように文書化されていること。

## コンテキスト
- docs/INDEX.md、docs/DIGEST.md、docs/PROGRESS.md を読み、`git log --oneline -20` を実行する。編集前に作業ツリーがきれいであることを確認する。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/08-harness-guardrail-engineering/research.claude-code.md
  - docs/08-harness-guardrail-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/06-verification-eval-engineering/plan.claude-code.md
  - docs/06-verification-eval-engineering/implementation.claude-code.md
  - docs/07-tool-engineering/research.claude-code.md
  - docs/07-tool-engineering/plan.claude-code.md
  - docs/07-tool-engineering/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 承認済みの計画が正。その「横断的な手法 → 適用方法」の表は拘束力を持つ。

## 制約
- 計画のステップを順に実行する。各ステップの後にそのチェックを実行し、出力を見せる。チェックが 2 回失敗したか、判断が必要なら、止めて質問する。
- 計画のツリー外のファイルには触らない。やむを得ない場合は、理由とともに「逸脱」の項に記録する。
- 作ったものに対して 4 つの横断的な手法のルールを検証する: SKILL.md は 500 行未満で標準フロントマター。説明文は 1,024 文字以内で、用途とトリガー語から始まる。常時読み込む指示ファイルは短い。決定論的な手順はスクリプト。絶対に起きてはいけないことはフックか権限ルール。状態ファイルは索引の上限内。
- Claude Code CLI の中でテストする: `cd claude-code && claude -p "List the skills, rules and hooks available to you" --output-format json` を実行し、計画した項目が現れることを確認する。対話的に /skills, /context, /hooks でも確認する。次に、計画の「検証」セクションにあるエンドツーエンドのシナリオ（受け入れの証拠: 禁止操作（保護されたパスへの書き込み、main への push、秘密ファイルの読み取り）が証拠付きで止められる。許可された作業はそのまま通る。無人プリセットがプロンプトなしでシナリオを完了する。）を実行し、証拠（コマンド、出力、ファイル）を残す。
- まとめる前に、新しいコンテキストのサブエージェント、または /code-review に結果と計画を照合させる。正しさや要件に関わる不足は直し、それ以外は「既知の不足」に列挙する。
- docs/08-harness-guardrail-engineering/implementation.claude-code.md（英語）と docs/08-harness-guardrail-engineering/implementation.claude-code.ja.md を、次の内容で書く: 作ったもの（最終的なツリー） · 使い方（コマンド、プロンプト） · 検証の証拠 · 4 つの横断的な手法をどう適用したか · 逸脱 · 既知の不足 · 「後続ステップ向けの要約」（15 行以内: 何がどこにあり、どう呼び出し、何を避けるか）。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 08-3 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（15 行以内の要約を追記）を更新する。
- 論理的な単位ごとに、`08-harness-guardrail-engineering(claude-code):` を接頭辞にしたメッセージでコミットする。

## 完了条件
- 計画のすべてのステップがチェック済みで、証拠が実装文書にあること。
- レビュアーが未解決の正しさの不足を報告していないか、「既知の不足」に列挙されていること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 15 行以内の要約、逸脱、既知の不足、次のステップへの提言。
````

### ⑨ Observability Engineering（その他の手法）

#### ⑨-1 Observability Engineering: 調査

- 起動: `claude -n ae-09-1-claude-code`
- 書き出し: `docs/09-observability-engineering/research.claude-code.md`、`docs/09-observability-engineering/research.claude-code.ja.md`

````text
Claude Code CLI 用に Observability Engineering を調査して、実装の計画にあたって重要なことを含めてまとめてください。ただし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑨-2 が再調査なしに頼れる調査文書: 定義、原則、Claude Code CLI が現時点でこの手法をどうサポートしているか、実装への含意。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。次に、英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
- 範囲: エージェントの動きとコストを見ること: コンテキスト使用量、トークンとコスト、ツール呼び出し、スキルの発動、フックの発火、セッション。ログとメトリクスのエクスポート。レポート。
- 調査の焦点: CLI ごとの組み込みビュー。メトリクスとログのエクスポートとその属性。ログ発生源としてのフック。トランスクリプトの形式とその不安定さ。コストの帰属。デバッグログ。プライバシーと秘匿化。ダッシュボードと定期レポート。
- 出発点（ヒントのみ: Claude Code CLI に関する項目を使い、それぞれ最新の公式ドキュメントで確認し、より新しい機能も調べる）: Claude Code の /context、/usage、/insights、ステータスライン、OpenTelemetry（skill_activated、OTEL_LOG_TOOL_DETAILS=1）、フックの transcript_path、/export、--debug-file。Codex の /status、TUI のコンテキスト使用率、history.jsonl（history.persistence、history.max_bytes）、log_dir、フック。Antigravity の /context、/usage、/statusline、/tasks、Ctrl+O、enableTelemetry、フック。
- 調査時点で最新の公式ドキュメントを調べて書く。既存の知識や過去の調査結果に頼らない。二次情報は背景として使ってよいが、その旨を明記する。

## 制約
- 文書そのものに 4 つの横断的な手法を適用する（例: 理由を添えた平易な口調、繰り返しではなくセクションへのクロスリンク、1 文 1 事実で時期に依存するものには日付、見出しで振り分けられる構成）。
- 構成は横断的な手法の文書と同じ: 定義と隣接する手法との境界。原則。Claude Code CLI がどうサポートしているか（正確なパス・設定・フラグ・コマンド付き）。関係する Claude Code CLI の機能の一覧表。Claude Code CLI 向けの再利用できるテンプレートやプロンプト。アンチパターン。チェックリスト。出典（公式と二次情報を区別）。対象は Claude Code CLI だけにする。
- 「実装計画への含意」のセクションを追加する: 候補となる成果物と Claude Code CLI での置き場所（今回の調査で確認したもの）。⑨-2 が決めるべき事項。リスク。ドキュメントからは確認できないこと。
- 文書の冒頭に調査日を書く。公式ドキュメントで確認できなかったものには「未確認」と印を付ける。
- docs/09-observability-engineering/research.claude-code.md（英語）と docs/09-observability-engineering/research.claude-code.ja.md（見出し構造が同一の忠実な翻訳）を書く。状態ファイル以外のファイルは作らない。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 09-1 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 実装者が知るべき制約と決定）を更新する。
- コミットしない。

## 完了条件
- 両ファイルが存在し、## と ### の見出し数が同じであること。すべてのパス・フラグ・コマンドに出典か「未確認」の印があること。
- INDEX、PROGRESS、DIGEST が更新されていること。
- 最後のメッセージに、書いたファイル、使った公式ソース、未確認の項目、⑨-2 で決めるべき事項を列挙すること。
````

#### ⑨-2 Observability Engineering: 実装計画

- 起動: `claude -n ae-09-2-claude-code --permission-mode plan`
- 書き出し: `docs/09-observability-engineering/plan.claude-code.md`、`docs/09-observability-engineering/plan.claude-code.ja.md`

````text
Claude Code CLI 用の Observability Engineering の実装計画を立ててください。ただし、フォルダ階層は必須とし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑨-3 が何も決め直さずに実行できる計画: 何を、どこに、どの順で作り、各ステップをどう確認するか。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/09-observability-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/06-verification-eval-engineering/plan.claude-code.md
  - docs/06-verification-eval-engineering/implementation.claude-code.md
  - docs/07-tool-engineering/research.claude-code.md
  - docs/07-tool-engineering/plan.claude-code.md
  - docs/07-tool-engineering/implementation.claude-code.md
  - docs/08-harness-guardrail-engineering/research.claude-code.md
  - docs/08-harness-guardrail-engineering/plan.claude-code.md
  - docs/08-harness-guardrail-engineering/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 範囲: エージェントの動きとコストを見ること: コンテキスト使用量、トークンとコスト、ツール呼び出し、スキルの発動、フックの発火、セッション。ログとメトリクスのエクスポート。レポート。
- 想定する成果物（確定または差し替える既定値）: .ae/logs に JSONL イベントを書くログ用フック。ステータスラインの設定。テレメトリ設定の断片。shared/scripts/report_usage（スキル別、ツール別、セッション別）。レポートのテンプレート。秘匿化のルール。
- リポジトリ構成は docs/program-layout.md に従う（Claude Code CLI での置き場所は調査文書から取る）。プログラムの骨格（shared/ と CLI ルート）がまだなければ、この計画で定義する（docs の状態ファイル、15 行以内のリポジトリルートの AGENTS.md と CLAUDE.md、shared/、claude-code/ を docs/program-layout.md の §2 と §5 のとおりに）。すでにあれば、それに従い、変更は「移行」の項でのみ提案する。
- Claude Code CLI に関する事実は調査文書から取る。計画が依存するパス・フラグ・コマンドは、頼る前に最新の公式ドキュメントで確認する。

## 制約
- 計画のみ: 2 つの計画ファイルと状態ファイル以外は作成も編集もしない。プランモードのままでいる。
- 書き始める前に、答えによって計画が変わる質問を最大 5 つ私にする。自明な質問は省く。AskUserQuestion を使う。
- フォルダ階層は必須: 作成・変更するすべてのファイルの完全なツリー。各項目に 1 行の目的と、使う Claude Code CLI の仕組み（スキル、ルール、フック、設定、エージェント、テンプレート、スクリプト）。
- 4 つの横断的な手法を適用し、「横断的な手法 → この計画での適用方法」の表を、チェックリスト（各横断的な手法の文書 docs/prompt-engineering-for-cli-agents.claude-code.md、docs/context-engineering-for-cli-agents.claude-code.md、docs/memory-engineering-for-cli-agents.claude-code.md、docs/knowledge-engineering-for-cli-agents.claude-code.md のチェックリストのセクション）を使って含める。特に: 常時読み込むファイルは短く保つ。条件付きの知識はパスや glob のルールにする。手順は shared/skills に標準フロントマターの Agent Skills として置き、説明文はトリガー語から始める。決定論的な手順はスクリプトにする。絶対に起きてはいけないことはフックか権限ルールにする。状態は索引の上限を意識してファイルに置く。
- ステップは小さく、順序付きにする。各ステップに: 触るファイル。うまくいったことを証明するチェック（コマンドまたは目視）。示すべき証拠。私の承認が必要なステップには印を付ける。
- セクション: 範囲と対象外 · 成果物表（パス、種類、Claude Code CLI の仕組み、読み込み階層、担当者） · フォルダ階層 · ステップ · 検証（⑨-3 がどう証明するか） · リスクと未解決の問い · ロールバック · 移行（既存の骨格を変える場合のみ）。
- docs/09-observability-engineering/plan.claude-code.md（英語）と docs/09-observability-engineering/plan.claude-code.ja.md（見出し構造が同一）を書く。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 09-2 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 成果物と決定）を更新する。
- コミットしない。

## 完了条件
- ステップに出てくるすべてのパスがツリーにあり、ツリーのすべての項目がいずれかのステップに出てくること。
- すべてのステップにチェックがあること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 10 行以内の計画の要約、私の承認が必要な決定（質問の形で）、未確認の事項。
````

#### ⑨-3 Observability Engineering: 実装とまとめ

- 起動: `claude -n ae-09-3-claude-code`
- 書き出し: `docs/09-observability-engineering/implementation.claude-code.md`、`docs/09-observability-engineering/implementation.claude-code.ja.md`

````text
承認済みの計画に従って Claude Code CLI 用の Observability Engineering の実装を進めて、最後に内容をまとめてください。ただし、md ファイルは英語版を .md、和訳版を .ja.md にしてください。

## ゴール
docs/09-observability-engineering/plan.claude-code.md のすべての成果物が存在し、Claude Code CLI の中で検証され、後続のステップが積み上げられるように文書化されていること。

## コンテキスト
- docs/INDEX.md、docs/DIGEST.md、docs/PROGRESS.md を読み、`git log --oneline -20` を実行する。編集前に作業ツリーがきれいであることを確認する。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/09-observability-engineering/research.claude-code.md
  - docs/09-observability-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/06-verification-eval-engineering/plan.claude-code.md
  - docs/06-verification-eval-engineering/implementation.claude-code.md
  - docs/07-tool-engineering/research.claude-code.md
  - docs/07-tool-engineering/plan.claude-code.md
  - docs/07-tool-engineering/implementation.claude-code.md
  - docs/08-harness-guardrail-engineering/research.claude-code.md
  - docs/08-harness-guardrail-engineering/plan.claude-code.md
  - docs/08-harness-guardrail-engineering/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 承認済みの計画が正。その「横断的な手法 → 適用方法」の表は拘束力を持つ。

## 制約
- 計画のステップを順に実行する。各ステップの後にそのチェックを実行し、出力を見せる。チェックが 2 回失敗したか、判断が必要なら、止めて質問する。
- 計画のツリー外のファイルには触らない。やむを得ない場合は、理由とともに「逸脱」の項に記録する。
- 作ったものに対して 4 つの横断的な手法のルールを検証する: SKILL.md は 500 行未満で標準フロントマター。説明文は 1,024 文字以内で、用途とトリガー語から始まる。常時読み込む指示ファイルは短い。決定論的な手順はスクリプト。絶対に起きてはいけないことはフックか権限ルール。状態ファイルは索引の上限内。
- Claude Code CLI の中でテストする: `cd claude-code && claude -p "List the skills, rules and hooks available to you" --output-format json` を実行し、計画した項目が現れることを確認する。対話的に /skills, /context, /hooks でも確認する。次に、計画の「検証」セクションにあるエンドツーエンドのシナリオ（受け入れの証拠: シナリオがイベントログを生成する。レポートに発動したスキル、呼ばれたツール、トークンが表示される。ステータスラインにコンテキスト使用量が出る。）を実行し、証拠（コマンド、出力、ファイル）を残す。
- まとめる前に、新しいコンテキストのサブエージェント、または /code-review に結果と計画を照合させる。正しさや要件に関わる不足は直し、それ以外は「既知の不足」に列挙する。
- docs/09-observability-engineering/implementation.claude-code.md（英語）と docs/09-observability-engineering/implementation.claude-code.ja.md を、次の内容で書く: 作ったもの（最終的なツリー） · 使い方（コマンド、プロンプト） · 検証の証拠 · 4 つの横断的な手法をどう適用したか · 逸脱 · 既知の不足 · 「後続ステップ向けの要約」（15 行以内: 何がどこにあり、どう呼び出し、何を避けるか）。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 09-3 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（15 行以内の要約を追記）を更新する。
- 論理的な単位ごとに、`09-observability-engineering(claude-code):` を接頭辞にしたメッセージでコミットする。

## 完了条件
- 計画のすべてのステップがチェック済みで、証拠が実装文書にあること。
- レビュアーが未解決の正しさの不足を報告していないか、「既知の不足」に列挙されていること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 15 行以内の要約、逸脱、既知の不足、次のステップへの提言。
````

### ⑩ Loop Engineering（その他の手法）

#### ⑩-1 Loop Engineering: 調査

- 起動: `claude -n ae-10-1-claude-code`
- 書き出し: `docs/10-loop-engineering/research.claude-code.md`、`docs/10-loop-engineering/research.claude-code.ja.md`

````text
Claude Code CLI 用に Loop Engineering を調査して、実装の計画にあたって重要なことを含めてまとめてください。ただし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑩-2 が再調査なしに頼れる調査文書: 定義、原則、Claude Code CLI が現時点でこの手法をどうサポートしているか、実装への含意。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。次に、英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
- 範囲: 反復と無人実行: チェックが通るまで回すループ、ゴール条件、スケジュールされた定期実行、ヘッドレスのバッチ、停滞の検出、ターンと予算の上限、冪等な再実行と再開。
- 調査の焦点: /goal の意味論と停滞。Stop ゲートの上限。スケジュール済みタスクと /loop。/schedule とサイドカーのスケジュール。Codex の Automations。上限付きのヘッドレスループ。失敗後の再開。冪等性。ループのテレメトリ。バックグラウンドのターンのコスト。
- 出発点（ヒントのみ: Claude Code CLI に関する項目を使い、それぞれ最新の公式ドキュメントで確認し、より新しい機能も調べる）: Claude Code の /goal、Stop フック、/loop、スケジュール済みタスク、--permission-mode dontAsk と --allowedTools を付けた claude -p、--max-turns、--max-budget-usd、/batch。Codex の /goal、codex exec（resume --last、--json、--output-schema）、Stop フック、Automations。Antigravity の /goal、/schedule、サイドカー（builtin schedule、agentapi new-conversation）、agy -p --cwd。
- 調査時点で最新の公式ドキュメントを調べて書く。既存の知識や過去の調査結果に頼らない。二次情報は背景として使ってよいが、その旨を明記する。

## 制約
- 文書そのものに 4 つの横断的な手法を適用する（例: 理由を添えた平易な口調、繰り返しではなくセクションへのクロスリンク、1 文 1 事実で時期に依存するものには日付、見出しで振り分けられる構成）。
- 構成は横断的な手法の文書と同じ: 定義と隣接する手法との境界。原則。Claude Code CLI がどうサポートしているか（正確なパス・設定・フラグ・コマンド付き）。関係する Claude Code CLI の機能の一覧表。Claude Code CLI 向けの再利用できるテンプレートやプロンプト。アンチパターン。チェックリスト。出典（公式と二次情報を区別）。対象は Claude Code CLI だけにする。
- 「実装計画への含意」のセクションを追加する: 候補となる成果物と Claude Code CLI での置き場所（今回の調査で確認したもの）。⑩-2 が決めるべき事項。リスク。ドキュメントからは確認できないこと。
- 文書の冒頭に調査日を書く。公式ドキュメントで確認できなかったものには「未確認」と印を付ける。
- docs/10-loop-engineering/research.claude-code.md（英語）と docs/10-loop-engineering/research.claude-code.ja.md（見出し構造が同一の忠実な翻訳）を書く。状態ファイル以外のファイルは作らない。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 10-1 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 実装者が知るべき制約と決定）を更新する。
- コミットしない。

## 完了条件
- 両ファイルが存在し、## と ### の見出し数が同じであること。すべてのパス・フラグ・コマンドに出典か「未確認」の印があること。
- INDEX、PROGRESS、DIGEST が更新されていること。
- 最後のメッセージに、書いたファイル、使った公式ソース、未確認の項目、⑩-2 で決めるべき事項を列挙すること。
````

#### ⑩-2 Loop Engineering: 実装計画

- 起動: `claude -n ae-10-2-claude-code --permission-mode plan`
- 書き出し: `docs/10-loop-engineering/plan.claude-code.md`、`docs/10-loop-engineering/plan.claude-code.ja.md`

````text
Claude Code CLI 用の Loop Engineering の実装計画を立ててください。ただし、フォルダ階層は必須とし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑩-3 が何も決め直さずに実行できる計画: 何を、どこに、どの順で作り、各ステップをどう確認するか。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/10-loop-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/06-verification-eval-engineering/plan.claude-code.md
  - docs/06-verification-eval-engineering/implementation.claude-code.md
  - docs/07-tool-engineering/research.claude-code.md
  - docs/07-tool-engineering/plan.claude-code.md
  - docs/07-tool-engineering/implementation.claude-code.md
  - docs/08-harness-guardrail-engineering/research.claude-code.md
  - docs/08-harness-guardrail-engineering/plan.claude-code.md
  - docs/08-harness-guardrail-engineering/implementation.claude-code.md
  - docs/09-observability-engineering/research.claude-code.md
  - docs/09-observability-engineering/plan.claude-code.md
  - docs/09-observability-engineering/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 範囲: 反復と無人実行: チェックが通るまで回すループ、ゴール条件、スケジュールされた定期実行、ヘッドレスのバッチ、停滞の検出、ターンと予算の上限、冪等な再実行と再開。
- 想定する成果物（確定または差し替える既定値）: shared/loops（上限付きの実行器: チェック → 修正 → 再チェック）。ゴールのテンプレート。スケジュールの例。停滞と予算のガード。run-until-green スキル。
- リポジトリ構成は docs/program-layout.md に従う（Claude Code CLI での置き場所は調査文書から取る）。プログラムの骨格（shared/ と CLI ルート）がまだなければ、この計画で定義する（docs の状態ファイル、15 行以内のリポジトリルートの AGENTS.md と CLAUDE.md、shared/、claude-code/ を docs/program-layout.md の §2 と §5 のとおりに）。すでにあれば、それに従い、変更は「移行」の項でのみ提案する。
- Claude Code CLI に関する事実は調査文書から取る。計画が依存するパス・フラグ・コマンドは、頼る前に最新の公式ドキュメントで確認する。

## 制約
- 計画のみ: 2 つの計画ファイルと状態ファイル以外は作成も編集もしない。プランモードのままでいる。
- 書き始める前に、答えによって計画が変わる質問を最大 5 つ私にする。自明な質問は省く。AskUserQuestion を使う。
- フォルダ階層は必須: 作成・変更するすべてのファイルの完全なツリー。各項目に 1 行の目的と、使う Claude Code CLI の仕組み（スキル、ルール、フック、設定、エージェント、テンプレート、スクリプト）。
- 4 つの横断的な手法を適用し、「横断的な手法 → この計画での適用方法」の表を、チェックリスト（各横断的な手法の文書 docs/prompt-engineering-for-cli-agents.claude-code.md、docs/context-engineering-for-cli-agents.claude-code.md、docs/memory-engineering-for-cli-agents.claude-code.md、docs/knowledge-engineering-for-cli-agents.claude-code.md のチェックリストのセクション）を使って含める。特に: 常時読み込むファイルは短く保つ。条件付きの知識はパスや glob のルールにする。手順は shared/skills に標準フロントマターの Agent Skills として置き、説明文はトリガー語から始める。決定論的な手順はスクリプトにする。絶対に起きてはいけないことはフックか権限ルールにする。状態は索引の上限を意識してファイルに置く。
- ステップは小さく、順序付きにする。各ステップに: 触るファイル。うまくいったことを証明するチェック（コマンドまたは目視）。示すべき証拠。私の承認が必要なステップには印を付ける。
- セクション: 範囲と対象外 · 成果物表（パス、種類、Claude Code CLI の仕組み、読み込み階層、担当者） · フォルダ階層 · ステップ · 検証（⑩-3 がどう証明するか） · リスクと未解決の問い · ロールバック · 移行（既存の骨格を変える場合のみ）。
- docs/10-loop-engineering/plan.claude-code.md（英語）と docs/10-loop-engineering/plan.claude-code.ja.md（見出し構造が同一）を書く。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 10-2 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 成果物と決定）を更新する。
- コミットしない。

## 完了条件
- ステップに出てくるすべてのパスがツリーにあり、ツリーのすべての項目がいずれかのステップに出てくること。
- すべてのステップにチェックがあること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 10 行以内の計画の要約、私の承認が必要な決定（質問の形で）、未確認の事項。
````

#### ⑩-3 Loop Engineering: 実装とまとめ

- 起動: `claude -n ae-10-3-claude-code`
- 書き出し: `docs/10-loop-engineering/implementation.claude-code.md`、`docs/10-loop-engineering/implementation.claude-code.ja.md`

````text
承認済みの計画に従って Claude Code CLI 用の Loop Engineering の実装を進めて、最後に内容をまとめてください。ただし、md ファイルは英語版を .md、和訳版を .ja.md にしてください。

## ゴール
docs/10-loop-engineering/plan.claude-code.md のすべての成果物が存在し、Claude Code CLI の中で検証され、後続のステップが積み上げられるように文書化されていること。

## コンテキスト
- docs/INDEX.md、docs/DIGEST.md、docs/PROGRESS.md を読み、`git log --oneline -20` を実行する。編集前に作業ツリーがきれいであることを確認する。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/10-loop-engineering/research.claude-code.md
  - docs/10-loop-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/06-verification-eval-engineering/plan.claude-code.md
  - docs/06-verification-eval-engineering/implementation.claude-code.md
  - docs/07-tool-engineering/research.claude-code.md
  - docs/07-tool-engineering/plan.claude-code.md
  - docs/07-tool-engineering/implementation.claude-code.md
  - docs/08-harness-guardrail-engineering/research.claude-code.md
  - docs/08-harness-guardrail-engineering/plan.claude-code.md
  - docs/08-harness-guardrail-engineering/implementation.claude-code.md
  - docs/09-observability-engineering/research.claude-code.md
  - docs/09-observability-engineering/plan.claude-code.md
  - docs/09-observability-engineering/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 承認済みの計画が正。その「横断的な手法 → 適用方法」の表は拘束力を持つ。

## 制約
- 計画のステップを順に実行する。各ステップの後にそのチェックを実行し、出力を見せる。チェックが 2 回失敗したか、判断が必要なら、止めて質問する。
- 計画のツリー外のファイルには触らない。やむを得ない場合は、理由とともに「逸脱」の項に記録する。
- 作ったものに対して 4 つの横断的な手法のルールを検証する: SKILL.md は 500 行未満で標準フロントマター。説明文は 1,024 文字以内で、用途とトリガー語から始まる。常時読み込む指示ファイルは短い。決定論的な手順はスクリプト。絶対に起きてはいけないことはフックか権限ルール。状態ファイルは索引の上限内。
- Claude Code CLI の中でテストする: `cd claude-code && claude -p "List the skills, rules and hooks available to you" --output-format json` を実行し、計画した項目が現れることを確認する。対話的に /skills, /context, /hooks でも確認する。次に、計画の「検証」セクションにあるエンドツーエンドのシナリオ（受け入れの証拠: 仕込んだ失敗テストをループが無人で上限内に直して止まる。成功できないループが上限で止まりレポートを出す。スケジュール実行が 1 回動いてログを残す。）を実行し、証拠（コマンド、出力、ファイル）を残す。
- まとめる前に、新しいコンテキストのサブエージェント、または /code-review に結果と計画を照合させる。正しさや要件に関わる不足は直し、それ以外は「既知の不足」に列挙する。
- docs/10-loop-engineering/implementation.claude-code.md（英語）と docs/10-loop-engineering/implementation.claude-code.ja.md を、次の内容で書く: 作ったもの（最終的なツリー） · 使い方（コマンド、プロンプト） · 検証の証拠 · 4 つの横断的な手法をどう適用したか · 逸脱 · 既知の不足 · 「後続ステップ向けの要約」（15 行以内: 何がどこにあり、どう呼び出し、何を避けるか）。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 10-3 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（15 行以内の要約を追記）を更新する。
- 論理的な単位ごとに、`10-loop-engineering(claude-code):` を接頭辞にしたメッセージでコミットする。

## 完了条件
- 計画のすべてのステップがチェック済みで、証拠が実装文書にあること。
- レビュアーが未解決の正しさの不足を報告していないか、「既知の不足」に列挙されていること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 15 行以内の要約、逸脱、既知の不足、次のステップへの提言。
````

### ⑪ Graph Engineering（その他の手法）

#### ⑪-1 Graph Engineering: 調査

- 起動: `claude -n ae-11-1-claude-code`
- 書き出し: `docs/11-graph-engineering/research.claude-code.md`、`docs/11-graph-engineering/research.claude-code.ja.md`

````text
Claude Code CLI 用に Graph Engineering を調査して、実装の計画にあたって重要なことを含めてまとめてください。ただし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑪-2 が再調査なしに頼れる調査文書: 定義、原則、Claude Code CLI が現時点でこの手法をどうサポートしているか、実装への含意。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。次に、英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
- 範囲: 構造を明示すること: 依存関係とゲートを持つタスク DAG。ノードがエージェントのステップで、チェックポイントで再開できるワークフローグラフ。分割、影響分析、振り分けに使うコードベースの構造グラフ（依存、呼び出し、所有）。
- 調査の焦点: CLI ごとの DAG・ワークフローのプリミティブ。データとしての DAG。部分的に完了したグラフのチェックポイントと再開。条件分岐と判断ゲート。言語サーバーや依存抽出によるコードグラフ。グラフから導くパスによる分割。描画（Mermaid）。ネストと同時実行数の上限。
- 出発点（ヒントのみ: Claude Code CLI に関する項目を使い、それぞれ最新の公式ドキュメントで確認し、より新しい機能も調べる）: Claude Code のダイナミックワークフロー（pipeline、parallel、フェーズ）、/batch、サブエージェント、worktree、コードインテリジェンスプラグイン。Codex のサブエージェント（agents.max_concurrent_threads_per_session）、/agent。Antigravity の invoke_subagent（深さ上限 10）、/agents、SDK のサブエージェントとライフサイクルフック、サイドカー。
- 調査時点で最新の公式ドキュメントを調べて書く。既存の知識や過去の調査結果に頼らない。二次情報は背景として使ってよいが、その旨を明記する。

## 制約
- 文書そのものに 4 つの横断的な手法を適用する（例: 理由を添えた平易な口調、繰り返しではなくセクションへのクロスリンク、1 文 1 事実で時期に依存するものには日付、見出しで振り分けられる構成）。
- 構成は横断的な手法の文書と同じ: 定義と隣接する手法との境界。原則。Claude Code CLI がどうサポートしているか（正確なパス・設定・フラグ・コマンド付き）。関係する Claude Code CLI の機能の一覧表。Claude Code CLI 向けの再利用できるテンプレートやプロンプト。アンチパターン。チェックリスト。出典（公式と二次情報を区別）。対象は Claude Code CLI だけにする。
- 「実装計画への含意」のセクションを追加する: 候補となる成果物と Claude Code CLI での置き場所（今回の調査で確認したもの）。⑪-2 が決めるべき事項。リスク。ドキュメントからは確認できないこと。
- 文書の冒頭に調査日を書く。公式ドキュメントで確認できなかったものには「未確認」と印を付ける。
- docs/11-graph-engineering/research.claude-code.md（英語）と docs/11-graph-engineering/research.claude-code.ja.md（見出し構造が同一の忠実な翻訳）を書く。状態ファイル以外のファイルは作らない。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 11-1 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 実装者が知るべき制約と決定）を更新する。
- コミットしない。

## 完了条件
- 両ファイルが存在し、## と ### の見出し数が同じであること。すべてのパス・フラグ・コマンドに出典か「未確認」の印があること。
- INDEX、PROGRESS、DIGEST が更新されていること。
- 最後のメッセージに、書いたファイル、使った公式ソース、未確認の項目、⑪-2 で決めるべき事項を列挙すること。
````

#### ⑪-2 Graph Engineering: 実装計画

- 起動: `claude -n ae-11-2-claude-code --permission-mode plan`
- 書き出し: `docs/11-graph-engineering/plan.claude-code.md`、`docs/11-graph-engineering/plan.claude-code.ja.md`

````text
Claude Code CLI 用の Graph Engineering の実装計画を立ててください。ただし、フォルダ階層は必須とし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑪-3 が何も決め直さずに実行できる計画: 何を、どこに、どの順で作り、各ステップをどう確認するか。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/11-graph-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/06-verification-eval-engineering/plan.claude-code.md
  - docs/06-verification-eval-engineering/implementation.claude-code.md
  - docs/07-tool-engineering/research.claude-code.md
  - docs/07-tool-engineering/plan.claude-code.md
  - docs/07-tool-engineering/implementation.claude-code.md
  - docs/08-harness-guardrail-engineering/research.claude-code.md
  - docs/08-harness-guardrail-engineering/plan.claude-code.md
  - docs/08-harness-guardrail-engineering/implementation.claude-code.md
  - docs/09-observability-engineering/research.claude-code.md
  - docs/09-observability-engineering/plan.claude-code.md
  - docs/09-observability-engineering/implementation.claude-code.md
  - docs/10-loop-engineering/research.claude-code.md
  - docs/10-loop-engineering/plan.claude-code.md
  - docs/10-loop-engineering/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 範囲: 構造を明示すること: 依存関係とゲートを持つタスク DAG。ノードがエージェントのステップで、チェックポイントで再開できるワークフローグラフ。分割、影響分析、振り分けに使うコードベースの構造グラフ（依存、呼び出し、所有）。
- 想定する成果物（確定または差し替える既定値）: shared/graphs（DAG のスキーマと例）。CLI のヘッドレスモードを通じて DAG をチェックポイント付きで実行する実行器。shared/scripts/code_graph（依存グラフ → 分割の提案）。plan-to-dag スキル。Mermaid による描画。
- リポジトリ構成は docs/program-layout.md に従う（Claude Code CLI での置き場所は調査文書から取る）。プログラムの骨格（shared/ と CLI ルート）がまだなければ、この計画で定義する（docs の状態ファイル、15 行以内のリポジトリルートの AGENTS.md と CLAUDE.md、shared/、claude-code/ を docs/program-layout.md の §2 と §5 のとおりに）。すでにあれば、それに従い、変更は「移行」の項でのみ提案する。
- Claude Code CLI に関する事実は調査文書から取る。計画が依存するパス・フラグ・コマンドは、頼る前に最新の公式ドキュメントで確認する。

## 制約
- 計画のみ: 2 つの計画ファイルと状態ファイル以外は作成も編集もしない。プランモードのままでいる。
- 書き始める前に、答えによって計画が変わる質問を最大 5 つ私にする。自明な質問は省く。AskUserQuestion を使う。
- フォルダ階層は必須: 作成・変更するすべてのファイルの完全なツリー。各項目に 1 行の目的と、使う Claude Code CLI の仕組み（スキル、ルール、フック、設定、エージェント、テンプレート、スクリプト）。
- 4 つの横断的な手法を適用し、「横断的な手法 → この計画での適用方法」の表を、チェックリスト（各横断的な手法の文書 docs/prompt-engineering-for-cli-agents.claude-code.md、docs/context-engineering-for-cli-agents.claude-code.md、docs/memory-engineering-for-cli-agents.claude-code.md、docs/knowledge-engineering-for-cli-agents.claude-code.md のチェックリストのセクション）を使って含める。特に: 常時読み込むファイルは短く保つ。条件付きの知識はパスや glob のルールにする。手順は shared/skills に標準フロントマターの Agent Skills として置き、説明文はトリガー語から始める。決定論的な手順はスクリプトにする。絶対に起きてはいけないことはフックか権限ルールにする。状態は索引の上限を意識してファイルに置く。
- ステップは小さく、順序付きにする。各ステップに: 触るファイル。うまくいったことを証明するチェック（コマンドまたは目視）。示すべき証拠。私の承認が必要なステップには印を付ける。
- セクション: 範囲と対象外 · 成果物表（パス、種類、Claude Code CLI の仕組み、読み込み階層、担当者） · フォルダ階層 · ステップ · 検証（⑪-3 がどう証明するか） · リスクと未解決の問い · ロールバック · 移行（既存の骨格を変える場合のみ）。
- docs/11-graph-engineering/plan.claude-code.md（英語）と docs/11-graph-engineering/plan.claude-code.ja.md（見出し構造が同一）を書く。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 11-2 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 成果物と決定）を更新する。
- コミットしない。

## 完了条件
- ステップに出てくるすべてのパスがツリーにあり、ツリーのすべての項目がいずれかのステップに出てくること。
- すべてのステップにチェックがあること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 10 行以内の計画の要約、私の承認が必要な決定（質問の形で）、未確認の事項。
````

#### ⑪-3 Graph Engineering: 実装とまとめ

- 起動: `claude -n ae-11-3-claude-code`
- 書き出し: `docs/11-graph-engineering/implementation.claude-code.md`、`docs/11-graph-engineering/implementation.claude-code.ja.md`

````text
承認済みの計画に従って Claude Code CLI 用の Graph Engineering の実装を進めて、最後に内容をまとめてください。ただし、md ファイルは英語版を .md、和訳版を .ja.md にしてください。

## ゴール
docs/11-graph-engineering/plan.claude-code.md のすべての成果物が存在し、Claude Code CLI の中で検証され、後続のステップが積み上げられるように文書化されていること。

## コンテキスト
- docs/INDEX.md、docs/DIGEST.md、docs/PROGRESS.md を読み、`git log --oneline -20` を実行する。編集前に作業ツリーがきれいであることを確認する。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/11-graph-engineering/research.claude-code.md
  - docs/11-graph-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/06-verification-eval-engineering/plan.claude-code.md
  - docs/06-verification-eval-engineering/implementation.claude-code.md
  - docs/07-tool-engineering/research.claude-code.md
  - docs/07-tool-engineering/plan.claude-code.md
  - docs/07-tool-engineering/implementation.claude-code.md
  - docs/08-harness-guardrail-engineering/research.claude-code.md
  - docs/08-harness-guardrail-engineering/plan.claude-code.md
  - docs/08-harness-guardrail-engineering/implementation.claude-code.md
  - docs/09-observability-engineering/research.claude-code.md
  - docs/09-observability-engineering/plan.claude-code.md
  - docs/09-observability-engineering/implementation.claude-code.md
  - docs/10-loop-engineering/research.claude-code.md
  - docs/10-loop-engineering/plan.claude-code.md
  - docs/10-loop-engineering/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 承認済みの計画が正。その「横断的な手法 → 適用方法」の表は拘束力を持つ。

## 制約
- 計画のステップを順に実行する。各ステップの後にそのチェックを実行し、出力を見せる。チェックが 2 回失敗したか、判断が必要なら、止めて質問する。
- 計画のツリー外のファイルには触らない。やむを得ない場合は、理由とともに「逸脱」の項に記録する。
- 作ったものに対して 4 つの横断的な手法のルールを検証する: SKILL.md は 500 行未満で標準フロントマター。説明文は 1,024 文字以内で、用途とトリガー語から始まる。常時読み込む指示ファイルは短い。決定論的な手順はスクリプト。絶対に起きてはいけないことはフックか権限ルール。状態ファイルは索引の上限内。
- Claude Code CLI の中でテストする: `cd claude-code && claude -p "List the skills, rules and hooks available to you" --output-format json` を実行し、計画した項目が現れることを確認する。対話的に /skills, /context, /hooks でも確認する。次に、計画の「検証」セクションにあるエンドツーエンドのシナリオ（受け入れの証拠: ゲートを 1 つ持つ 4〜6 ノードの DAG がエンドツーエンドで動き、中断と再開ができ、描画される。コードグラフがサンプルの変更に対して重ならない分割を提案する。）を実行し、証拠（コマンド、出力、ファイル）を残す。
- まとめる前に、新しいコンテキストのサブエージェント、または /code-review に結果と計画を照合させる。正しさや要件に関わる不足は直し、それ以外は「既知の不足」に列挙する。
- docs/11-graph-engineering/implementation.claude-code.md（英語）と docs/11-graph-engineering/implementation.claude-code.ja.md を、次の内容で書く: 作ったもの（最終的なツリー） · 使い方（コマンド、プロンプト） · 検証の証拠 · 4 つの横断的な手法をどう適用したか · 逸脱 · 既知の不足 · 「後続ステップ向けの要約」（15 行以内: 何がどこにあり、どう呼び出し、何を避けるか）。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 11-3 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（15 行以内の要約を追記）を更新する。
- 論理的な単位ごとに、`11-graph-engineering(claude-code):` を接頭辞にしたメッセージでコミットする。

## 完了条件
- 計画のすべてのステップがチェック済みで、証拠が実装文書にあること。
- レビュアーが未解決の正しさの不足を報告していないか、「既知の不足」に列挙されていること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 15 行以内の要約、逸脱、既知の不足、次のステップへの提言。
````

### ⑫ Multi-Agent Orchestration（その他の手法）

#### ⑫-1 Multi-Agent Orchestration: 調査

- 起動: `claude -n ae-12-1-claude-code`
- 書き出し: `docs/12-multi-agent-orchestration/research.claude-code.md`、`docs/12-multi-agent-orchestration/research.claude-code.ja.md`

````text
Claude Code CLI 用に Multi-Agent Orchestration を調査して、実装の計画にあたって重要なことを含めてまとめてください。ただし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑫-2 が再調査なしに頼れる調査文書: 定義、原則、Claude Code CLI が現時点でこの手法をどうサポートしているか、実装への含意。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。次に、英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
- 範囲: コーディネーターとワーカーの構造: エージェントの役割と定義、構造化された返り値を伴う委任プロンプト、パスによる分割、worktree による隔離、Writer/Reviewer、ファンアウトとファンイン、セッション間のメッセージ、同時実行数とコストの制御。
- 調査の焦点: CLI ごとのサブエージェントのモデル（何を引き継ぎ、何が返るか）。同時実行数の上限。worktree による隔離。エージェントチームとチームワークのプレビュー。セッション間メッセージ。失敗モード（編集の衝突、再帰、コストの暴走）。逐次が並列に勝る場面。
- 出発点（ヒントのみ: Claude Code CLI に関する項目を使い、それぞれ最新の公式ドキュメントで確認し、より新しい機能も調べる）: Claude Code の .claude/agents（tools、model、memory）、/batch、worktree（worktree.sparsePaths）、セッション間メッセージ、エージェントチーム（実験的）、claude agents、Writer/Reviewer。Codex の default、worker、explorer、.codex/agents/*.toml、agents.max_concurrent_threads_per_session、/agent。Antigravity の .agents/agents/*.md、invoke_subagent、/agents、/teamwork-preview。
- 調査時点で最新の公式ドキュメントを調べて書く。既存の知識や過去の調査結果に頼らない。二次情報は背景として使ってよいが、その旨を明記する。

## 制約
- 文書そのものに 4 つの横断的な手法を適用する（例: 理由を添えた平易な口調、繰り返しではなくセクションへのクロスリンク、1 文 1 事実で時期に依存するものには日付、見出しで振り分けられる構成）。
- 構成は横断的な手法の文書と同じ: 定義と隣接する手法との境界。原則。Claude Code CLI がどうサポートしているか（正確なパス・設定・フラグ・コマンド付き）。関係する Claude Code CLI の機能の一覧表。Claude Code CLI 向けの再利用できるテンプレートやプロンプト。アンチパターン。チェックリスト。出典（公式と二次情報を区別）。対象は Claude Code CLI だけにする。
- 「実装計画への含意」のセクションを追加する: 候補となる成果物と Claude Code CLI での置き場所（今回の調査で確認したもの）。⑫-2 が決めるべき事項。リスク。ドキュメントからは確認できないこと。
- 文書の冒頭に調査日を書く。公式ドキュメントで確認できなかったものには「未確認」と印を付ける。
- docs/12-multi-agent-orchestration/research.claude-code.md（英語）と docs/12-multi-agent-orchestration/research.claude-code.ja.md（見出し構造が同一の忠実な翻訳）を書く。状態ファイル以外のファイルは作らない。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 12-1 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 実装者が知るべき制約と決定）を更新する。
- コミットしない。

## 完了条件
- 両ファイルが存在し、## と ### の見出し数が同じであること。すべてのパス・フラグ・コマンドに出典か「未確認」の印があること。
- INDEX、PROGRESS、DIGEST が更新されていること。
- 最後のメッセージに、書いたファイル、使った公式ソース、未確認の項目、⑫-2 で決めるべき事項を列挙すること。
````

#### ⑫-2 Multi-Agent Orchestration: 実装計画

- 起動: `claude -n ae-12-2-claude-code --permission-mode plan`
- 書き出し: `docs/12-multi-agent-orchestration/plan.claude-code.md`、`docs/12-multi-agent-orchestration/plan.claude-code.ja.md`

````text
Claude Code CLI 用の Multi-Agent Orchestration の実装計画を立ててください。ただし、フォルダ階層は必須とし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑫-3 が何も決め直さずに実行できる計画: 何を、どこに、どの順で作り、各ステップをどう確認するか。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/12-multi-agent-orchestration/research.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/06-verification-eval-engineering/plan.claude-code.md
  - docs/06-verification-eval-engineering/implementation.claude-code.md
  - docs/07-tool-engineering/research.claude-code.md
  - docs/07-tool-engineering/plan.claude-code.md
  - docs/07-tool-engineering/implementation.claude-code.md
  - docs/08-harness-guardrail-engineering/research.claude-code.md
  - docs/08-harness-guardrail-engineering/plan.claude-code.md
  - docs/08-harness-guardrail-engineering/implementation.claude-code.md
  - docs/09-observability-engineering/research.claude-code.md
  - docs/09-observability-engineering/plan.claude-code.md
  - docs/09-observability-engineering/implementation.claude-code.md
  - docs/10-loop-engineering/research.claude-code.md
  - docs/10-loop-engineering/plan.claude-code.md
  - docs/10-loop-engineering/implementation.claude-code.md
  - docs/11-graph-engineering/research.claude-code.md
  - docs/11-graph-engineering/plan.claude-code.md
  - docs/11-graph-engineering/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 範囲: コーディネーターとワーカーの構造: エージェントの役割と定義、構造化された返り値を伴う委任プロンプト、パスによる分割、worktree による隔離、Writer/Reviewer、ファンアウトとファンイン、セッション間のメッセージ、同時実行数とコストの制御。
- 想定する成果物（確定または差し替える既定値）: CLI ごとのエージェント定義（調査役、実装役、レビュアー、検証役）。orchestrate スキル（分解 → パスで分割 → 配分 → 回収 → 統合）。返り値形式のスキーマ。worktree の設定。コストガード（最大エージェント数、役割ごとのモデル）。
- リポジトリ構成は docs/program-layout.md に従う（Claude Code CLI での置き場所は調査文書から取る）。プログラムの骨格（shared/ と CLI ルート）がまだなければ、この計画で定義する（docs の状態ファイル、15 行以内のリポジトリルートの AGENTS.md と CLAUDE.md、shared/、claude-code/ を docs/program-layout.md の §2 と §5 のとおりに）。すでにあれば、それに従い、変更は「移行」の項でのみ提案する。
- Claude Code CLI に関する事実は調査文書から取る。計画が依存するパス・フラグ・コマンドは、頼る前に最新の公式ドキュメントで確認する。

## 制約
- 計画のみ: 2 つの計画ファイルと状態ファイル以外は作成も編集もしない。プランモードのままでいる。
- 書き始める前に、答えによって計画が変わる質問を最大 5 つ私にする。自明な質問は省く。AskUserQuestion を使う。
- フォルダ階層は必須: 作成・変更するすべてのファイルの完全なツリー。各項目に 1 行の目的と、使う Claude Code CLI の仕組み（スキル、ルール、フック、設定、エージェント、テンプレート、スクリプト）。
- 4 つの横断的な手法を適用し、「横断的な手法 → この計画での適用方法」の表を、チェックリスト（各横断的な手法の文書 docs/prompt-engineering-for-cli-agents.claude-code.md、docs/context-engineering-for-cli-agents.claude-code.md、docs/memory-engineering-for-cli-agents.claude-code.md、docs/knowledge-engineering-for-cli-agents.claude-code.md のチェックリストのセクション）を使って含める。特に: 常時読み込むファイルは短く保つ。条件付きの知識はパスや glob のルールにする。手順は shared/skills に標準フロントマターの Agent Skills として置き、説明文はトリガー語から始める。決定論的な手順はスクリプトにする。絶対に起きてはいけないことはフックか権限ルールにする。状態は索引の上限を意識してファイルに置く。
- ステップは小さく、順序付きにする。各ステップに: 触るファイル。うまくいったことを証明するチェック（コマンドまたは目視）。示すべき証拠。私の承認が必要なステップには印を付ける。
- セクション: 範囲と対象外 · 成果物表（パス、種類、Claude Code CLI の仕組み、読み込み階層、担当者） · フォルダ階層 · ステップ · 検証（⑫-3 がどう証明するか） · リスクと未解決の問い · ロールバック · 移行（既存の骨格を変える場合のみ）。
- docs/12-multi-agent-orchestration/plan.claude-code.md（英語）と docs/12-multi-agent-orchestration/plan.claude-code.ja.md（見出し構造が同一）を書く。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 12-2 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 成果物と決定）を更新する。
- コミットしない。

## 完了条件
- ステップに出てくるすべてのパスがツリーにあり、ツリーのすべての項目がいずれかのステップに出てくること。
- すべてのステップにチェックがあること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 10 行以内の計画の要約、私の承認が必要な決定（質問の形で）、未確認の事項。
````

#### ⑫-3 Multi-Agent Orchestration: 実装とまとめ

- 起動: `claude -n ae-12-3-claude-code`
- 書き出し: `docs/12-multi-agent-orchestration/implementation.claude-code.md`、`docs/12-multi-agent-orchestration/implementation.claude-code.ja.md`

````text
承認済みの計画に従って Claude Code CLI 用の Multi-Agent Orchestration の実装を進めて、最後に内容をまとめてください。ただし、md ファイルは英語版を .md、和訳版を .ja.md にしてください。

## ゴール
docs/12-multi-agent-orchestration/plan.claude-code.md のすべての成果物が存在し、Claude Code CLI の中で検証され、後続のステップが積み上げられるように文書化されていること。

## コンテキスト
- docs/INDEX.md、docs/DIGEST.md、docs/PROGRESS.md を読み、`git log --oneline -20` を実行する。編集前に作業ツリーがきれいであることを確認する。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/12-multi-agent-orchestration/research.claude-code.md
  - docs/12-multi-agent-orchestration/plan.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/06-verification-eval-engineering/plan.claude-code.md
  - docs/06-verification-eval-engineering/implementation.claude-code.md
  - docs/07-tool-engineering/research.claude-code.md
  - docs/07-tool-engineering/plan.claude-code.md
  - docs/07-tool-engineering/implementation.claude-code.md
  - docs/08-harness-guardrail-engineering/research.claude-code.md
  - docs/08-harness-guardrail-engineering/plan.claude-code.md
  - docs/08-harness-guardrail-engineering/implementation.claude-code.md
  - docs/09-observability-engineering/research.claude-code.md
  - docs/09-observability-engineering/plan.claude-code.md
  - docs/09-observability-engineering/implementation.claude-code.md
  - docs/10-loop-engineering/research.claude-code.md
  - docs/10-loop-engineering/plan.claude-code.md
  - docs/10-loop-engineering/implementation.claude-code.md
  - docs/11-graph-engineering/research.claude-code.md
  - docs/11-graph-engineering/plan.claude-code.md
  - docs/11-graph-engineering/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 承認済みの計画が正。その「横断的な手法 → 適用方法」の表は拘束力を持つ。

## 制約
- 計画のステップを順に実行する。各ステップの後にそのチェックを実行し、出力を見せる。チェックが 2 回失敗したか、判断が必要なら、止めて質問する。
- 計画のツリー外のファイルには触らない。やむを得ない場合は、理由とともに「逸脱」の項に記録する。
- 作ったものに対して 4 つの横断的な手法のルールを検証する: SKILL.md は 500 行未満で標準フロントマター。説明文は 1,024 文字以内で、用途とトリガー語から始まる。常時読み込む指示ファイルは短い。決定論的な手順はスクリプト。絶対に起きてはいけないことはフックか権限ルール。状態ファイルは索引の上限内。
- Claude Code CLI の中でテストする: `cd claude-code && claude -p "List the skills, rules and hooks available to you" --output-format json` を実行し、計画した項目が現れることを確認する。対話的に /skills, /context, /hooks でも確認する。次に、計画の「検証」セクションにあるエンドツーエンドのシナリオ（受け入れの証拠: 重ならない 2 つのパスにまたがる変更が、2 つのワーカーと 1 つのレビュアーで、編集の衝突なしに完了する。エージェントごとのトークンレポートが出る。）を実行し、証拠（コマンド、出力、ファイル）を残す。
- まとめる前に、新しいコンテキストのサブエージェント、または /code-review に結果と計画を照合させる。正しさや要件に関わる不足は直し、それ以外は「既知の不足」に列挙する。
- docs/12-multi-agent-orchestration/implementation.claude-code.md（英語）と docs/12-multi-agent-orchestration/implementation.claude-code.ja.md を、次の内容で書く: 作ったもの（最終的なツリー） · 使い方（コマンド、プロンプト） · 検証の証拠 · 4 つの横断的な手法をどう適用したか · 逸脱 · 既知の不足 · 「後続ステップ向けの要約」（15 行以内: 何がどこにあり、どう呼び出し、何を避けるか）。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 12-3 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（15 行以内の要約を追記）を更新する。
- 論理的な単位ごとに、`12-multi-agent-orchestration(claude-code):` を接頭辞にしたメッセージでコミットする。

## 完了条件
- 計画のすべてのステップがチェック済みで、証拠が実装文書にあること。
- レビュアーが未解決の正しさの不足を報告していないか、「既知の不足」に列挙されていること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 15 行以内の要約、逸脱、既知の不足、次のステップへの提言。
````

### ⑬ Production Engineering（その他の手法）

#### ⑬-1 Production Engineering: 調査

- 起動: `claude -n ae-13-1-claude-code`
- 書き出し: `docs/13-production-engineering/research.claude-code.md`、`docs/13-production-engineering/research.claude-code.ja.md`

````text
Claude Code CLI 用に Production Engineering を調査して、実装の計画にあたって重要なことを含めてまとめてください。ただし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑬-2 が再調査なしに頼れる調査文書: 定義、原則、Claude Code CLI が現時点でこの手法をどうサポートしているか、実装への含意。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。次に、英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
- 範囲: 他者が依存する場所でエージェントのワークフローを動かすこと: CI 連携、秘密情報と環境、バージョン管理と配布（プラグイン、マーケットプレイス、管理設定）、コストの統制、信頼性、監査証跡、セキュリティレビュー、モデル更新時の変更管理、手順書と担当者、対象リポジトリへのツールキットの導入。
- 調査の焦点: CLI ごとのヘッドレス・CI モードと出力形式。GitHub Actions との連携。秘密情報の扱い。クラウド環境。管理設定とプラグインのポリシー。レート制限と予算。帰属のためのテレメトリ。スキルとプラグインのバージョン付きリリース。モデル更新後の再監査。導入のレイアウト。
- 出発点（ヒントのみ: Claude Code CLI に関する項目を使い、それぞれ最新の公式ドキュメントで確認し、より新しい機能も調べる）: Claude Code の claude -p（--output-format json|stream-json、--permission-mode dontAsk|auto、--allowedTools、--no-session-persistence、--max-budget-usd）、管理設定、プラグインとマーケットプレイス（enabledPlugins）、OpenTelemetry。Codex の codex exec（--json、--output-last-message、--ephemeral、--sandbox）、Codex GitHub Action、信頼できないコードが動くジョブでジョブレベルの OPENAI_API_KEY を使わないこと、requirements.toml。Antigravity のヘッドレスモード（agy -p）、プラグインの同期、Remote Control、エンタープライズのドキュメント。
- 調査時点で最新の公式ドキュメントを調べて書く。既存の知識や過去の調査結果に頼らない。二次情報は背景として使ってよいが、その旨を明記する。

## 制約
- 文書そのものに 4 つの横断的な手法を適用する（例: 理由を添えた平易な口調、繰り返しではなくセクションへのクロスリンク、1 文 1 事実で時期に依存するものには日付、見出しで振り分けられる構成）。
- 構成は横断的な手法の文書と同じ: 定義と隣接する手法との境界。原則。Claude Code CLI がどうサポートしているか（正確なパス・設定・フラグ・コマンド付き）。関係する Claude Code CLI の機能の一覧表。Claude Code CLI 向けの再利用できるテンプレートやプロンプト。アンチパターン。チェックリスト。出典（公式と二次情報を区別）。対象は Claude Code CLI だけにする。
- 「実装計画への含意」のセクションを追加する: 候補となる成果物と Claude Code CLI での置き場所（今回の調査で確認したもの）。⑬-2 が決めるべき事項。リスク。ドキュメントからは確認できないこと。
- 文書の冒頭に調査日を書く。公式ドキュメントで確認できなかったものには「未確認」と印を付ける。
- docs/13-production-engineering/research.claude-code.md（英語）と docs/13-production-engineering/research.claude-code.ja.md（見出し構造が同一の忠実な翻訳）を書く。状態ファイル以外のファイルは作らない。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 13-1 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 実装者が知るべき制約と決定）を更新する。
- コミットしない。

## 完了条件
- 両ファイルが存在し、## と ### の見出し数が同じであること。すべてのパス・フラグ・コマンドに出典か「未確認」の印があること。
- INDEX、PROGRESS、DIGEST が更新されていること。
- 最後のメッセージに、書いたファイル、使った公式ソース、未確認の項目、⑬-2 で決めるべき事項を列挙すること。
````

#### ⑬-2 Production Engineering: 実装計画

- 起動: `claude -n ae-13-2-claude-code --permission-mode plan`
- 書き出し: `docs/13-production-engineering/plan.claude-code.md`、`docs/13-production-engineering/plan.claude-code.ja.md`

````text
Claude Code CLI 用の Production Engineering の実装計画を立ててください。ただし、フォルダ階層は必須とし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ ⑬-3 が何も決め直さずに実行できる計画: 何を、どこに、どの順で作り、各ステップをどう確認するか。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/13-production-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/06-verification-eval-engineering/plan.claude-code.md
  - docs/06-verification-eval-engineering/implementation.claude-code.md
  - docs/07-tool-engineering/research.claude-code.md
  - docs/07-tool-engineering/plan.claude-code.md
  - docs/07-tool-engineering/implementation.claude-code.md
  - docs/08-harness-guardrail-engineering/research.claude-code.md
  - docs/08-harness-guardrail-engineering/plan.claude-code.md
  - docs/08-harness-guardrail-engineering/implementation.claude-code.md
  - docs/09-observability-engineering/research.claude-code.md
  - docs/09-observability-engineering/plan.claude-code.md
  - docs/09-observability-engineering/implementation.claude-code.md
  - docs/10-loop-engineering/research.claude-code.md
  - docs/10-loop-engineering/plan.claude-code.md
  - docs/10-loop-engineering/implementation.claude-code.md
  - docs/11-graph-engineering/research.claude-code.md
  - docs/11-graph-engineering/plan.claude-code.md
  - docs/11-graph-engineering/implementation.claude-code.md
  - docs/12-multi-agent-orchestration/research.claude-code.md
  - docs/12-multi-agent-orchestration/plan.claude-code.md
  - docs/12-multi-agent-orchestration/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 範囲: 他者が依存する場所でエージェントのワークフローを動かすこと: CI 連携、秘密情報と環境、バージョン管理と配布（プラグイン、マーケットプレイス、管理設定）、コストの統制、信頼性、監査証跡、セキュリティレビュー、モデル更新時の変更管理、手順書と担当者、対象リポジトリへのツールキットの導入。
- 想定する成果物（確定または差し替える既定値）: CLI ごとの CI ワークフローの例。環境と秘密情報のガイド。shared/ をプラグインとしてパッケージ化するリリース手順。本番用の権限プリセット。予算の設定。手順書。本番準備チェックリスト。対象リポジトリへの導入スクリプト。
- リポジトリ構成は docs/program-layout.md に従う（Claude Code CLI での置き場所は調査文書から取る）。プログラムの骨格（shared/ と CLI ルート）がまだなければ、この計画で定義する（docs の状態ファイル、15 行以内のリポジトリルートの AGENTS.md と CLAUDE.md、shared/、claude-code/ を docs/program-layout.md の §2 と §5 のとおりに）。すでにあれば、それに従い、変更は「移行」の項でのみ提案する。
- Claude Code CLI に関する事実は調査文書から取る。計画が依存するパス・フラグ・コマンドは、頼る前に最新の公式ドキュメントで確認する。

## 制約
- 計画のみ: 2 つの計画ファイルと状態ファイル以外は作成も編集もしない。プランモードのままでいる。
- 書き始める前に、答えによって計画が変わる質問を最大 5 つ私にする。自明な質問は省く。AskUserQuestion を使う。
- フォルダ階層は必須: 作成・変更するすべてのファイルの完全なツリー。各項目に 1 行の目的と、使う Claude Code CLI の仕組み（スキル、ルール、フック、設定、エージェント、テンプレート、スクリプト）。
- 4 つの横断的な手法を適用し、「横断的な手法 → この計画での適用方法」の表を、チェックリスト（各横断的な手法の文書 docs/prompt-engineering-for-cli-agents.claude-code.md、docs/context-engineering-for-cli-agents.claude-code.md、docs/memory-engineering-for-cli-agents.claude-code.md、docs/knowledge-engineering-for-cli-agents.claude-code.md のチェックリストのセクション）を使って含める。特に: 常時読み込むファイルは短く保つ。条件付きの知識はパスや glob のルールにする。手順は shared/skills に標準フロントマターの Agent Skills として置き、説明文はトリガー語から始める。決定論的な手順はスクリプトにする。絶対に起きてはいけないことはフックか権限ルールにする。状態は索引の上限を意識してファイルに置く。
- ステップは小さく、順序付きにする。各ステップに: 触るファイル。うまくいったことを証明するチェック（コマンドまたは目視）。示すべき証拠。私の承認が必要なステップには印を付ける。
- セクション: 範囲と対象外 · 成果物表（パス、種類、Claude Code CLI の仕組み、読み込み階層、担当者） · フォルダ階層 · ステップ · 検証（⑬-3 がどう証明するか） · リスクと未解決の問い · ロールバック · 移行（既存の骨格を変える場合のみ）。
- docs/13-production-engineering/plan.claude-code.md（英語）と docs/13-production-engineering/plan.claude-code.ja.md（見出し構造が同一）を書く。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 13-2 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（8 行以内: 成果物と決定）を更新する。
- コミットしない。

## 完了条件
- ステップに出てくるすべてのパスがツリーにあり、ツリーのすべての項目がいずれかのステップに出てくること。
- すべてのステップにチェックがあること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 10 行以内の計画の要約、私の承認が必要な決定（質問の形で）、未確認の事項。
````

#### ⑬-3 Production Engineering: 実装とまとめ

- 起動: `claude -n ae-13-3-claude-code`
- 書き出し: `docs/13-production-engineering/implementation.claude-code.md`、`docs/13-production-engineering/implementation.claude-code.ja.md`

````text
承認済みの計画に従って Claude Code CLI 用の Production Engineering の実装を進めて、最後に内容をまとめてください。ただし、md ファイルは英語版を .md、和訳版を .ja.md にしてください。

## ゴール
docs/13-production-engineering/plan.claude-code.md のすべての成果物が存在し、Claude Code CLI の中で検証され、後続のステップが積み上げられるように文書化されていること。

## コンテキスト
- docs/INDEX.md、docs/DIGEST.md、docs/PROGRESS.md を読み、`git log --oneline -20` を実行する。編集前に作業ツリーがきれいであることを確認する。
- 英語版のみを全文読む（.ja.md は読まない）:
  - docs/prompt-engineering-for-cli-agents.claude-code.md
  - docs/context-engineering-for-cli-agents.claude-code.md
  - docs/memory-engineering-for-cli-agents.claude-code.md
  - docs/knowledge-engineering-for-cli-agents.claude-code.md
  - docs/program-layout.md（リポジトリ構成、命名、状態ファイル）
  - docs/13-production-engineering/research.claude-code.md
  - docs/13-production-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/research.claude-code.md
  - docs/05-spec-plan-engineering/plan.claude-code.md
  - docs/05-spec-plan-engineering/implementation.claude-code.md
  - docs/06-verification-eval-engineering/research.claude-code.md
  - docs/06-verification-eval-engineering/plan.claude-code.md
  - docs/06-verification-eval-engineering/implementation.claude-code.md
  - docs/07-tool-engineering/research.claude-code.md
  - docs/07-tool-engineering/plan.claude-code.md
  - docs/07-tool-engineering/implementation.claude-code.md
  - docs/08-harness-guardrail-engineering/research.claude-code.md
  - docs/08-harness-guardrail-engineering/plan.claude-code.md
  - docs/08-harness-guardrail-engineering/implementation.claude-code.md
  - docs/09-observability-engineering/research.claude-code.md
  - docs/09-observability-engineering/plan.claude-code.md
  - docs/09-observability-engineering/implementation.claude-code.md
  - docs/10-loop-engineering/research.claude-code.md
  - docs/10-loop-engineering/plan.claude-code.md
  - docs/10-loop-engineering/implementation.claude-code.md
  - docs/11-graph-engineering/research.claude-code.md
  - docs/11-graph-engineering/plan.claude-code.md
  - docs/11-graph-engineering/implementation.claude-code.md
  - docs/12-multi-agent-orchestration/research.claude-code.md
  - docs/12-multi-agent-orchestration/plan.claude-code.md
  - docs/12-multi-agent-orchestration/implementation.claude-code.md
- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは Explore エージェント に任せ、40 行以内のダイジェストを返させてもよい。
- 読み込みの後に /context で使用量を確認して報告する。
- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。
- 承認済みの計画が正。その「横断的な手法 → 適用方法」の表は拘束力を持つ。

## 制約
- 計画のステップを順に実行する。各ステップの後にそのチェックを実行し、出力を見せる。チェックが 2 回失敗したか、判断が必要なら、止めて質問する。
- 計画のツリー外のファイルには触らない。やむを得ない場合は、理由とともに「逸脱」の項に記録する。
- 作ったものに対して 4 つの横断的な手法のルールを検証する: SKILL.md は 500 行未満で標準フロントマター。説明文は 1,024 文字以内で、用途とトリガー語から始まる。常時読み込む指示ファイルは短い。決定論的な手順はスクリプト。絶対に起きてはいけないことはフックか権限ルール。状態ファイルは索引の上限内。
- Claude Code CLI の中でテストする: `cd claude-code && claude -p "List the skills, rules and hooks available to you" --output-format json` を実行し、計画した項目が現れることを確認する。対話的に /skills, /context, /hooks でも確認する。次に、計画の「検証」セクションにあるエンドツーエンドのシナリオ（受け入れの証拠: CI ジョブがヘッドレスの検証を構造化出力で実行し、仕込んだ欠陥で失敗する。プラグインが新しいクローンにインストールできる。準備チェックリストが証拠付きで完了する。）を実行し、証拠（コマンド、出力、ファイル）を残す。
- まとめる前に、新しいコンテキストのサブエージェント、または /code-review に結果と計画を照合させる。正しさや要件に関わる不足は直し、それ以外は「既知の不足」に列挙する。
- docs/13-production-engineering/implementation.claude-code.md（英語）と docs/13-production-engineering/implementation.claude-code.ja.md を、次の内容で書く: 作ったもの（最終的なツリー） · 使い方（コマンド、プロンプト） · 検証の証拠 · 4 つの横断的な手法をどう適用したか · 逸脱 · 既知の不足 · 「後続ステップ向けの要約」（15 行以内: 何がどこにあり、どう呼び出し、何を避けるか）。
- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ docs/program-layout.md の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 13-3 claude-code: 完了、日付、未解決の問い）、docs/DIGEST.md（15 行以内の要約を追記）を更新する。
- 論理的な単位ごとに、`13-production-engineering(claude-code):` を接頭辞にしたメッセージでコミットする。

## 完了条件
- 計画のすべてのステップがチェック済みで、証拠が実装文書にあること。
- レビュアーが未解決の正しさの不足を報告していないか、「既知の不足」に列挙されていること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 15 行以内の要約、逸脱、既知の不足、次のステップへの提言。
````
