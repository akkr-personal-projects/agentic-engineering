#!/usr/bin/env python3
"""Write every Agentic Engineering prompt for one CLI, in order, into one file.

Settings: config.toml (one CLI, the cross-cutting methods, the other methods, language, output,
max_file_kib). If the output is larger than max_file_kib, it is split at heading boundaries into
parts, and the output path becomes a table of contents linking to them (see mdsplit.py).
Scope descriptions for known disciplines: briefs.toml (optional per discipline).

Usage:
  python3 tools/agentic-prompts/generate.py
  python3 tools/agentic-prompts/generate.py --config path/to/config.toml

Standard library only (Python 3.11+).
"""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path

from mdsplit import write_split

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DOCS = "docs"
LAYOUT = "docs/program-layout.md"
CIRCLED = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"

CLIS = {
    "claude-code": {
        "name": "Claude Code CLI", "root": "claude-code",
        "start": "claude -n {session}", "plan_start": "claude -n {session} --permission-mode plan",
        "context": "/context", "checks": "/skills, /context, /hooks",
        "discovery": 'cd claude-code && claude -p "List the skills, rules and hooks available to you" --output-format json',
        "plan_mode": {"en": "Stay in plan mode.", "ja": "プランモードのままでいる。"},
        "interview": {"en": "Use AskUserQuestion.", "ja": "AskUserQuestion を使う。"},
        "reviewer": {"en": "a subagent with a fresh context, or /code-review", "ja": "新しいコンテキストのサブエージェント、または /code-review "},
        "explorer": {"en": "the Explore agent", "ja": "Explore エージェント"},
    },
    "codex": {
        "name": "Codex CLI", "root": "codex",
        "start": "codex", "plan_start": "codex → /plan",
        "start_note": {"en": "record the session id in docs/PROGRESS.md", "ja": "セッション ID を docs/PROGRESS.md に記録する"},
        "context": "/status", "checks": "/skills, /status, /mcp",
        "discovery": 'cd codex && codex exec "Summarize the current instructions and list the available skills"',
        "plan_mode": {"en": "Use /plan.", "ja": "/plan を使う。"},
        "interview": {"en": "Ask in plain text, one question per line.", "ja": "通常のテキストで、1 行に 1 問ずつ質問する。"},
        "reviewer": {"en": "/review, or an explorer subagent", "ja": "/review、または explorer サブエージェント"},
        "explorer": {"en": "an explorer subagent", "ja": "explorer サブエージェント"},
    },
    "antigravity": {
        "name": "Antigravity CLI", "root": "antigravity",
        "start": "agy → /rename {session}", "plan_start": "agy → /rename {session} → /plan",
        "context": "/context", "checks": "/skills, /context, /hooks",
        "discovery": 'cd antigravity && agy -p "List the loaded rules, skills and hooks" --cwd "$(pwd)"',
        "plan_mode": {"en": "Use /plan.", "ja": "/plan を使う。"},
        "interview": {"en": "/grill-me is also fine.", "ja": "/grill-me でもよい。"},
        "reviewer": {"en": "a read-only subagent", "ja": "読み取り専用のサブエージェント"},
        "explorer": {"en": "a subagent with view_file and grep_search only", "ja": "view_file と grep_search のみを持つサブエージェント"},
    },
}


def circ(n: int) -> str:
    return CIRCLED[n - 1] if 1 <= n <= len(CIRCLED) else f"({n})"


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def ja_path(path: str) -> str:
    return path[:-3] + ".ja.md"


def bullets(items: list[str]) -> str:
    return "\n".join(f"  - {x}" for x in items)


@dataclass
class Discipline:
    kind: str  # "cross" | "method"
    name: str
    number: int
    brief: dict

    @property
    def slug(self) -> str:
        return slugify(self.name)

    def field(self, key: str, lang: str = "") -> str:
        if lang:
            return self.brief.get(lang, {}).get(key) or self.brief.get("en", {}).get(key, "")
        return self.brief.get(key, "")


@dataclass
class Step:
    disc: Discipline
    k: int  # 1 research, 2 plan, 3 implement

    @property
    def sid(self) -> str:
        return f"{circ(self.disc.number)}-{self.k}"

    @property
    def row(self) -> str:
        return f"{self.disc.number:02d}-{self.k}"


class Generator:
    def __init__(self, cfg: dict, briefs: dict):
        self.cli = cfg.get("cli", "claude-code")
        if self.cli not in CLIS:
            sys.exit(f"error: cli must be one of {', '.join(CLIS)} (got '{self.cli}')")
        self.lang = cfg.get("language", "ja")
        if self.lang not in ("ja", "en"):
            sys.exit(f"error: language must be 'ja' or 'en' (got '{self.lang}')")
        self.prof = CLIS[self.cli]
        self.cli_name = self.prof["name"]
        n = 0
        self.cross: list[Discipline] = []
        self.methods: list[Discipline] = []
        for kind, names, target in (("cross", cfg.get("cross_cutting", []), self.cross),
                                    ("method", cfg.get("methods", []), self.methods)):
            for name in names:
                n += 1
                b = briefs.get(slugify(name), {})
                if not b:
                    print(f"warning: no brief for '{name}' in briefs.toml; its prompts ask the agent to define the scope",
                          file=sys.stderr)
                target.append(Discipline(kind, name, n, b))
        self.steps = [Step(d, 1) for d in self.cross]
        for m in self.methods:
            self.steps += [Step(m, 1), Step(m, 2), Step(m, 3)]

    # -- helpers -------------------------------------------------------------
    def t(self, en: str, ja: str) -> str:
        return ja if self.lang == "ja" else en

    def tr(self, value) -> str:
        return value.get(self.lang, value.get("en", "")) if isinstance(value, dict) else value

    def research(self, d: Discipline) -> str:
        if d.kind == "cross":
            return f"{DOCS}/{d.slug}-for-cli-agents.{self.cli}.md"
        return f"{DOCS}/{d.number:02d}-{d.slug}/research.{self.cli}.md"

    def plan_doc(self, d: Discipline) -> str:
        return f"{DOCS}/{d.number:02d}-{d.slug}/plan.{self.cli}.md"

    def impl_doc(self, d: Discipline) -> str:
        return f"{DOCS}/{d.number:02d}-{d.slug}/implementation.{self.cli}.md"

    def output_of(self, s: Step) -> str:
        return [self.research, self.plan_doc, self.impl_doc][s.k - 1](s.disc)

    def layout_ref(self, d: Discipline) -> str:
        """Layout, naming and state-file rules. It holds no CLI facts; those come from this run's research."""
        return self.t(f"{LAYOUT} (repository layout, naming and state files)",
                      f"{LAYOUT}（リポジトリ構成、命名、状態ファイル）")

    def cross_docs(self) -> list[str]:
        return [self.research(c) for c in self.cross]

    def prior_docs(self, d: Discipline) -> list[str]:
        out = []
        for m in self.methods:
            if m.number < d.number:
                out += [self.research(m), self.plan_doc(m), self.impl_doc(m)]
        return out

    def checklists(self) -> str:
        docs = (", " if self.lang == "en" else "、").join(self.cross_docs())
        if not docs:
            return self.t("(no cross-cutting methods configured)", "（横断的な手法の設定なし）")
        return self.t(f"in the checklist section of each cross-cutting document ({docs})",
                      f"（各横断的な手法の文書 {docs} のチェックリストのセクション）")

    def brief_lines(self, d: Discipline, keys: list[str]) -> str:
        labels = {
            "scope": ("Scope", "範囲"),
            "research_focus": ("Research focus", "調査の焦点"),
            "starting_points": (f"Starting points (hints only: use the {self.cli_name} items, verify each against current official docs, and look for newer features)",
                                f"出発点（ヒントのみ: {self.cli_name} に関する項目を使い、それぞれ最新の公式ドキュメントで確認し、より新しい機能も調べる）"),
            "expected_artifacts": ("Expected artifacts (defaults to confirm or replace)", "想定する成果物（確定または差し替える既定値）"),
        }
        lines = [f"- {self.t(*labels[k])}: {d.field(k, self.lang)}" for k in keys if d.field(k, self.lang)]
        if not d.brief:
            lines.append(self.t("- Scope: not specified. Define it from the method's name and state your definition at the top of the document.",
                                "- 範囲: 指定なし。手法の名前から範囲を定義し、文書の冒頭にその定義を書く。"))
        return "\n".join(lines)

    def structure(self, prefix_en: str, prefix_ja: str) -> str:
        c = self.cli_name
        return self.t(
            f"- {prefix_en}: definition and boundaries with neighboring methods; principles; how {c} supports it, with exact paths, settings, flags and commands; a summary table of the {c} features involved; reusable templates or prompts for {c}; anti-patterns; checklist; sources (official vs secondary). Cover only {c}.",
            f"- {prefix_ja}: 定義と隣接する手法との境界。原則。{c} がどうサポートしているか（正確なパス・設定・フラグ・コマンド付き）。関係する {c} の機能の一覧表。{c} 向けの再利用できるテンプレートやプロンプト。アンチパターン。チェックリスト。出典（公式と二次情報を区別）。対象は {c} だけにする。")

    def state_update(self, s: Step, digest_en: str, digest_ja: str) -> str:
        return self.t(
            f"- Create docs/INDEX.md, docs/PROGRESS.md and docs/DIGEST.md from §4 of {LAYOUT} if they do not exist. Update docs/INDEX.md (one line per new file), docs/PROGRESS.md (row {s.row} {self.cli}: done, date, open questions) and docs/DIGEST.md ({digest_en}).",
            f"- docs/INDEX.md、docs/PROGRESS.md、docs/DIGEST.md がなければ {LAYOUT} の §4 から作成する。docs/INDEX.md（新しいファイルごとに 1 行）、docs/PROGRESS.md（行 {s.row} {self.cli}: 完了、日付、未解決の問い）、docs/DIGEST.md（{digest_ja}）を更新する。")

    def reading_block(self, s: Step) -> str:
        d = s.disc
        full = self.cross_docs() + [self.layout_ref(d), self.research(d)]
        if s.k == 3:
            full.append(self.plan_doc(d))
        prior = self.prior_docs(d)
        lines = [self.t("- Read in full, English versions only, never the .ja.md files:",
                        "- 英語版のみを全文読む（.ja.md は読まない）:") + "\n" + bullets(full + prior)]
        if not prior:
            lines.append(self.t("- There are no earlier method documents.", "- 以前の手法の文書はない。"))
        else:
            lines.append(self.t(
                f"- If reading all of this in full would use more than about 40% of your context window, read the earlier methods through docs/DIGEST.md and the \"Summary for later steps\" section of each implementation document instead, open a full document only where this step depends on it, and list what you opened. You can delegate the reading to {self.tr(self.prof['explorer'])} and have it return a ≤ 40-line digest.",
                f"- これらを全文読むとコンテキストウィンドウの約 40% を超える場合は、以前の手法を docs/DIGEST.md と各実装文書の「後続ステップ向けの要約」セクションで読み、このステップが依存する場合にだけ全文を開き、開いた文書を列挙する。読み込みは {self.tr(self.prof['explorer'])} に任せ、40 行以内のダイジェストを返させてもよい。"))
        lines.append(self.t(f"- After reading, check usage with {self.prof['context']} and report it.",
                            f"- 読み込みの後に {self.prof['context']} で使用量を確認して報告する。"))
        lines.append(self.t(
            "- If docs/DIGEST.md shows this method was already implemented for another CLI, reuse shared/ and add adapters for this CLI; do not fork shared skills.",
            "- docs/DIGEST.md から、この手法が別の CLI 向けに実装済みだと分かる場合は、shared/ を再利用してこの CLI 用のアダプターを追加し、共有スキルをフォークしない。"))
        return "\n".join(lines)

    # -- prompts -------------------------------------------------------------
    def cross_research(self, s: Step) -> str:
        d, c = s.disc, self.cli_name
        out = self.research(d)
        prev = [self.research(x) for x in self.cross if x.number < d.number]
        if prev:
            read = self.t("- Read in full, English versions only, never the .ja.md files:",
                          "- 英語版のみを全文読む（.ja.md は読まない）:") + "\n" + bullets(prev) + "\n" + self.t(
                "  Build on them: cross-link to their sections instead of repeating them, and keep the same structure.",
                "  それらの上に積み上げる: 内容を繰り返さずに該当セクションへクロスリンクし、同じ構成を保つ。")
        else:
            read = self.t("- This is the first method, so there are no earlier documents.", "- これは最初の手法なので、先行する文書はない。")
        if self.lang == "ja":
            return f"""{c} 用に {d.name} を調査してまとめてください。ただし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
後続のステップが再調査なしに頼れる調査文書: 定義、原則、{c} が現時点で {d.name} をどうサポートしているか、テンプレート、アンチパターン、チェックリスト、出典。

## コンテキスト
{self.brief_lines(d, ["scope", "research_focus", "starting_points"])}
{read}
- 調査時点で最新の公式ドキュメントを調べて書く。既存の知識や過去の調査結果に頼らない。二次情報はその旨を明記する。

## 制約
- この手法は横断的な手法であり、後続のすべての手法に適用される。どう適用するかが分かる書き方にする。
{self.structure("Structure", "構成")}
- 文書の冒頭に調査日を書く。公式ドキュメントで確認できなかったものには「未確認」と印を付ける。
- {out}（英語）と {ja_path(out)}（見出し構造が同一の忠実な翻訳）を書く。状態ファイル以外のファイルは作らない。
{self.state_update(s, "", "8 行以内: 後続のステップが知るべき原則と制約")}
- コミットしない。

## 完了条件
- 両ファイルが存在し、## と ### の見出し数が同じであること。すべてのパス・フラグ・コマンドに出典か「未確認」の印があること。
- 最後のメッセージに、書いたファイル、使った公式ソース、未確認の項目、未解決の問いを列挙すること。"""
        return f"""Research {d.name} for {c} and write it up, in English as .md and a Japanese translation as .ja.md.

## Goal
A research document that later steps can rely on without re-researching: definitions, principles, how {c} supports {d.name} today, templates, anti-patterns, a checklist and sources.

## Context
{self.brief_lines(d, ["scope", "research_focus", "starting_points"])}
{read}
- Research the current official documentation at the time of writing; do not rely on prior knowledge or earlier research. Label secondary sources as such.

## Constraints
- This is a cross-cutting method: every later method applies it. Write it so that how to apply it is clear.
{self.structure("Structure", "構成")}
- Put the research date at the top of the document. Mark anything not verified against official docs as "unverified".
- Write {out} (English) and {ja_path(out)} (faithful translation, identical heading structure). Create no other files except the state files.
{self.state_update(s, "≤ 8 lines: principles and constraints later steps must know", "")}
- Do not commit.

## Done when
- Both files exist with the same number of ## and ### headings; every path, flag or command has a source or an "unverified" mark.
- Your final message lists files written, official sources used, unverified items and open questions."""

    def method_research(self, s: Step) -> str:
        d, c = s.disc, self.cli_name
        out = self.research(d)
        reads = bullets(self.cross_docs() + [self.layout_ref(d)])
        nxt = f"{circ(d.number)}-2"
        n = len(self.cross)
        if self.lang == "ja":
            return f"""{c} 用に {d.name} を調査して、実装の計画にあたって重要なことを含めてまとめてください。ただし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ {nxt} が再調査なしに頼れる調査文書: 定義、原則、{c} が現時点でこの手法をどうサポートしているか、実装への含意。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。次に、英語版のみを全文読む（.ja.md は読まない）:
{reads}
{self.brief_lines(d, ["scope", "research_focus", "starting_points"])}
- 調査時点で最新の公式ドキュメントを調べて書く。既存の知識や過去の調査結果に頼らない。二次情報は背景として使ってよいが、その旨を明記する。

## 制約
- 文書そのものに {n} つの横断的な手法を適用する（例: 理由を添えた平易な口調、繰り返しではなくセクションへのクロスリンク、1 文 1 事実で時期に依存するものには日付、見出しで振り分けられる構成）。
{self.structure("Structure, as in the cross-cutting documents", "構成は横断的な手法の文書と同じ")}
- 「実装計画への含意」のセクションを追加する: 候補となる成果物と {c} での置き場所（今回の調査で確認したもの）。{nxt} が決めるべき事項。リスク。ドキュメントからは確認できないこと。
- 文書の冒頭に調査日を書く。公式ドキュメントで確認できなかったものには「未確認」と印を付ける。
- {out}（英語）と {ja_path(out)}（見出し構造が同一の忠実な翻訳）を書く。状態ファイル以外のファイルは作らない。
{self.state_update(s, "", "8 行以内: 実装者が知るべき制約と決定")}
- コミットしない。

## 完了条件
- 両ファイルが存在し、## と ### の見出し数が同じであること。すべてのパス・フラグ・コマンドに出典か「未確認」の印があること。
- INDEX、PROGRESS、DIGEST が更新されていること。
- 最後のメッセージに、書いたファイル、使った公式ソース、未確認の項目、{nxt} で決めるべき事項を列挙すること。"""
        return f"""Research {d.name} for {c} and write it up, including what matters for implementation planning, in English as .md and a Japanese translation as .ja.md.

## Goal
A research document that step {nxt} can rely on without re-researching: definitions, principles, how {c} supports this method today, and the implications for implementation.

## Context
- Read docs/INDEX.md and docs/DIGEST.md first. Then read in full, English versions only, never the .ja.md files:
{reads}
{self.brief_lines(d, ["scope", "research_focus", "starting_points"])}
- Research the current official documentation at the time of writing; do not rely on prior knowledge or earlier research. Secondary sources are allowed for context and must be labeled.

## Constraints
- Apply the {n} cross-cutting methods to the document itself (for example: plain tone with reasons; cross-links instead of repetition; one fact per statement, dated when time-sensitive; headings a later agent can route by).
{self.structure("Structure, as in the cross-cutting documents", "構成は横断的な手法の文書と同じ")}
- Add a section "Implications for implementation planning": candidate artifacts and where each lives in {c} (as verified in this research); decisions {nxt} must make; risks; what cannot be verified from documentation.
- Put the research date at the top of the document. Mark anything not verified against official docs as "unverified".
- Write {out} (English) and {ja_path(out)} (faithful translation, identical heading structure). Create no other files except the state files.
{self.state_update(s, "≤ 8 lines: constraints and decisions an implementer must know", "")}
- Do not commit.

## Done when
- Both files exist with the same number of ## and ### headings; every path, flag or command has a source or an "unverified" mark.
- INDEX, PROGRESS and DIGEST are updated.
- Your final message lists: files written, official sources used, unverified items, and the open decisions for {nxt}."""

    def plan(self, s: Step) -> str:
        d, c, p = s.disc, self.cli_name, self.prof
        out = self.plan_doc(d)
        nxt = f"{circ(d.number)}-3"
        n = len(self.cross)
        root = p["root"]
        if self.lang == "ja":
            return f"""{c} 用の {d.name} の実装計画を立ててください。ただし、フォルダ階層は必須とし、英語で .md、和訳版を .ja.md にまとめてください。

## ゴール
ステップ {nxt} が何も決め直さずに実行できる計画: 何を、どこに、どの順で作り、各ステップをどう確認するか。

## コンテキスト
- まず docs/INDEX.md と docs/DIGEST.md を読む。
{self.reading_block(s)}
{self.brief_lines(d, ["scope", "expected_artifacts"])}
- リポジトリ構成は {LAYOUT} に従う（{c} での置き場所は調査文書から取る）。プログラムの骨格（shared/ と CLI ルート）がまだなければ、この計画で定義する（docs の状態ファイル、15 行以内のリポジトリルートの AGENTS.md と CLAUDE.md、shared/、{root}/ を {LAYOUT} の §2 と §5 のとおりに）。すでにあれば、それに従い、変更は「移行」の項でのみ提案する。
- {c} に関する事実は調査文書から取る。計画が依存するパス・フラグ・コマンドは、頼る前に最新の公式ドキュメントで確認する。

## 制約
- 計画のみ: 2 つの計画ファイルと状態ファイル以外は作成も編集もしない。{self.tr(p['plan_mode'])}
- 書き始める前に、答えによって計画が変わる質問を最大 5 つ私にする。自明な質問は省く。{self.tr(p['interview'])}
- フォルダ階層は必須: 作成・変更するすべてのファイルの完全なツリー。各項目に 1 行の目的と、使う {c} の仕組み（スキル、ルール、フック、設定、エージェント、テンプレート、スクリプト）。
- {n} つの横断的な手法を適用し、「横断的な手法 → この計画での適用方法」の表を、チェックリスト{self.checklists()}を使って含める。特に: 常時読み込むファイルは短く保つ。条件付きの知識はパスや glob のルールにする。手順は shared/skills に標準フロントマターの Agent Skills として置き、説明文はトリガー語から始める。決定論的な手順はスクリプトにする。絶対に起きてはいけないことはフックか権限ルールにする。状態は索引の上限を意識してファイルに置く。
- ステップは小さく、順序付きにする。各ステップに: 触るファイル。うまくいったことを証明するチェック（コマンドまたは目視）。示すべき証拠。私の承認が必要なステップには印を付ける。
- セクション: 範囲と対象外 · 成果物表（パス、種類、{c} の仕組み、読み込み階層、担当者） · フォルダ階層 · ステップ · 検証（{nxt} がどう証明するか） · リスクと未解決の問い · ロールバック · 移行（既存の骨格を変える場合のみ）。
- {out}（英語）と {ja_path(out)}（見出し構造が同一）を書く。
{self.state_update(s, "", "8 行以内: 成果物と決定")}
- コミットしない。

## 完了条件
- ステップに出てくるすべてのパスがツリーにあり、ツリーのすべての項目がいずれかのステップに出てくること。
- すべてのステップにチェックがあること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 10 行以内の計画の要約、私の承認が必要な決定（質問の形で）、未確認の事項。"""
        return f"""Create the implementation plan for {d.name} in {c}. The folder hierarchy is mandatory. Write it in English as .md and a Japanese translation as .ja.md.

## Goal
A plan that step {nxt} can execute without re-deciding anything: what to build, where, in which order, and how each step is checked.

## Context
- Read docs/INDEX.md and docs/DIGEST.md first.
{self.reading_block(s)}
{self.brief_lines(d, ["scope", "expected_artifacts"])}
- Follow the repository layout in {LAYOUT} (take where things live in {c} from the research document). If the program skeleton (shared/ and the CLI roots) does not exist yet, this plan defines it (docs state files, repo-root AGENTS.md and CLAUDE.md under 15 lines, shared/, {root}/ as in §2 and §5 of {LAYOUT}). If it exists, it is binding; propose changes only under "Migration".
- Facts about {c} come from the research document. Verify any path, flag or command the plan depends on against the current official docs before relying on it.

## Constraints
- Plan only: create or edit no files except the two plan files and the state files. {self.tr(p['plan_mode'])}
- Before writing, ask me up to five questions whose answers would change the plan; skip obvious ones. {self.tr(p['interview'])}
- Folder hierarchy is mandatory: a complete tree of every file to create or change, one line of purpose per entry, and the {c} mechanism it uses (skill, rule, hook, settings, agent, template, script).
- Apply the {n} cross-cutting methods and include a table "Cross-cutting method → how this plan applies it" using the checklists {self.checklists()}. In particular: always-on files stay short; conditional knowledge uses path or glob rules; procedures are Agent Skills in shared/skills with standard frontmatter and descriptions that lead with trigger words; deterministic steps are scripts; must-never-happen rules are hooks or permission rules; state lives in files written with index limits in mind.
- Steps are small and ordered. Each has: files touched; a check (command or inspection) that proves it worked; the evidence to show. Mark steps that need my approval.
- Sections: Scope and non-goals · Artifacts table (path, type, {c} mechanism, loading tier, owner) · Folder hierarchy · Steps · Verification (how {nxt} proves it) · Risks and open questions · Rollback · Migration (only if an existing skeleton changes).
- Write {out} (English) and {ja_path(out)} (identical heading structure).
{self.state_update(s, "≤ 8 lines: artifacts and decisions", "")}
- Do not commit.

## Done when
- Every path in the steps appears in the tree, and every tree entry appears in a step.
- Every step has a check.
- Both language files have the same heading structure; state files updated.
- Your final message: a ≤ 10-line plan summary, the decisions that need my approval (as questions), and anything unverified."""

    def implement(self, s: Step) -> str:
        d, c, p = s.disc, self.cli_name, self.prof
        out = self.impl_doc(d)
        plan = self.plan_doc(d)
        n = len(self.cross)
        accept = d.field("acceptance", self.lang)
        prefix = f"{d.number:02d}-{d.slug}({self.cli}):"
        if self.lang == "ja":
            scen = (f"計画の「検証」セクションにあるエンドツーエンドのシナリオ（受け入れの証拠: {accept}）" if accept
                    else "計画の「検証」セクションにある現実的なエンドツーエンドのシナリオ")
            return f"""承認済みの計画に従って {c} 用の {d.name} の実装を進めて、最後に内容をまとめてください。ただし、md ファイルは英語版を .md、和訳版を .ja.md にしてください。

## ゴール
{plan} のすべての成果物が存在し、{c} の中で検証され、後続のステップが積み上げられるように文書化されていること。

## コンテキスト
- docs/INDEX.md、docs/DIGEST.md、docs/PROGRESS.md を読み、`git log --oneline -20` を実行する。編集前に作業ツリーがきれいであることを確認する。
{self.reading_block(s)}
- 承認済みの計画が正。その「横断的な手法 → 適用方法」の表は拘束力を持つ。

## 制約
- 計画のステップを順に実行する。各ステップの後にそのチェックを実行し、出力を見せる。チェックが 2 回失敗したか、判断が必要なら、止めて質問する。
- 計画のツリー外のファイルには触らない。やむを得ない場合は、理由とともに「逸脱」の項に記録する。
- 作ったものに対して {n} つの横断的な手法のルールを検証する: SKILL.md は 500 行未満で標準フロントマター。説明文は 1,024 文字以内で、用途とトリガー語から始まる。常時読み込む指示ファイルは短い。決定論的な手順はスクリプト。絶対に起きてはいけないことはフックか権限ルール。状態ファイルは索引の上限内。
- {c} の中でテストする: `{p['discovery']}` を実行し、計画した項目が現れることを確認する。対話的に {p['checks']} でも確認する。次に、{scen}を実行し、証拠（コマンド、出力、ファイル）を残す。
- まとめる前に、{self.tr(p['reviewer'])}に結果と計画を照合させる。正しさや要件に関わる不足は直し、それ以外は「既知の不足」に列挙する。
- {out}（英語）と {ja_path(out)} を、次の内容で書く: 作ったもの（最終的なツリー） · 使い方（コマンド、プロンプト） · 検証の証拠 · {n} つの横断的な手法をどう適用したか · 逸脱 · 既知の不足 · 「後続ステップ向けの要約」（15 行以内: 何がどこにあり、どう呼び出し、何を避けるか）。
{self.state_update(s, "", "15 行以内の要約を追記")}
- 論理的な単位ごとに、`{prefix}` を接頭辞にしたメッセージでコミットする。

## 完了条件
- 計画のすべてのステップがチェック済みで、証拠が実装文書にあること。
- レビュアーが未解決の正しさの不足を報告していないか、「既知の不足」に列挙されていること。
- 両言語のファイルの見出し構造が同じで、状態ファイルが更新されていること。
- 最後のメッセージ: 15 行以内の要約、逸脱、既知の不足、次のステップへの提言。"""
        scen = (f"the end-to-end scenario from the plan's Verification section (acceptance evidence: {accept})" if accept
                else "one realistic end-to-end scenario from the plan's Verification section")
        return f"""Implement {d.name} for {c} following the approved plan, then summarize. Write md files in English as .md and a Japanese translation as .ja.md.

## Goal
Every artifact in {plan} exists, is verified inside {c}, and is documented so later steps can build on it.

## Context
- Read docs/INDEX.md, docs/DIGEST.md and docs/PROGRESS.md, then run `git log --oneline -20`. Confirm the working tree is clean before editing.
{self.reading_block(s)}
- The approved plan is the source of truth; its "Cross-cutting method → how applied" table is binding.

## Constraints
- Execute the plan's steps in order. After each step, run its check and show the output. If a check fails twice, or a decision is needed, stop and ask.
- Touch no files outside the plan's tree. If you must, record each under "Deviations" with the reason.
- Verify the {n} cross-cutting methods' rules on what you produce: SKILL.md under 500 lines with standard frontmatter; descriptions ≤ 1,024 characters leading with the use case and trigger words; always-on instruction files short; scripts for deterministic steps; hooks or permission rules for must-never-happen behavior; state files within index limits.
- Test inside {c}: run `{p['discovery']}` and confirm the planned items appear; confirm interactively with {p['checks']}; then run {scen} and capture the evidence (commands, outputs, files).
- Before summarizing, have {self.tr(p['reviewer'])} compare the result with the plan. Fix gaps that affect correctness or requirements; list the rest under "Known gaps".
- Write {out} (English) and {ja_path(out)} with: what was built (final tree) · how to use it (commands, prompts) · verification evidence · how the {n} cross-cutting methods were applied · deviations · known gaps · "Summary for later steps" (≤ 15 lines: what exists, where, how to invoke it, what to avoid).
{self.state_update(s, "append the ≤ 15-line summary", "")}
- Commit in logical units with messages prefixed `{prefix}`.

## Done when
- All plan steps are checked, with evidence in the implementation document.
- The reviewer reported no open correctness gaps, or they are listed under "Known gaps".
- Both language files have the same heading structure; state files updated.
- Your final message: the ≤ 15-line summary, deviations, known gaps, and recommendations for the next step."""

    def prompt(self, s: Step) -> str:
        if s.disc.kind == "cross":
            return self.cross_research(s)
        return {1: self.method_research, 2: self.plan, 3: self.implement}[s.k](s)

    # -- document ------------------------------------------------------------
    def title(self, s: Step) -> str:
        phase = self.t(["Research", "Plan", "Implement and summarize"][s.k - 1],
                       ["調査", "実装計画", "実装とまとめ"][s.k - 1])
        return f"{s.sid} {s.disc.name}: {phase}"

    def start(self, s: Step) -> str:
        session = f"ae-{s.disc.number:02d}-{s.k}-{self.cli}"
        cmd = (self.prof["plan_start"] if s.k == 2 else self.prof["start"]).replace("{session}", session)
        text = " → ".join(f"`{x.strip()}`" for x in cmd.split("→"))
        note = self.tr(self.prof.get("start_note", ""))
        return text + (self.t(f" ({note})", f"（{note}）") if note else "")

    def document(self) -> str:
        c = self.cli_name
        sep = "、" if self.lang == "ja" else ", "
        cross = sep.join(f"{circ(d.number)} {d.name}" for d in self.cross) or self.t("none", "なし")
        meth = sep.join(f"{circ(d.number)} {d.name}" for d in self.methods) or self.t("none", "なし")
        L: list[str] = []
        if self.lang == "ja":
            L += [f"# Agentic Engineering プロンプト一覧（{c}）", "",
                  "> `tools/agentic-prompts/generate.py` が `tools/agentic-prompts/config.toml` から生成しました。手で編集せず、設定を変えて再生成してください。",
                  f"> 構成と状態ファイル: [{LAYOUT}](../{LAYOUT})。ジェネレーターの使い方: [tools/agentic-prompts/README.ja.md](../tools/agentic-prompts/README.ja.md)", "",
                  "## 設定", "", f"- CLI: {c}",
                  f"- 横断的な手法（調査のみ。以降のすべての手法に適用）: {cross}",
                  f"- その他の手法（調査 → 実装計画 → 実装とまとめ）: {meth}",
                  f"- ステップ数: {len(self.steps)}", "",
                  "## 使い方", "",
                  "- 上から順に、1 ステップにつき 1 つのプロンプトを、新しいセッションに貼り付けます。前のステップの結果を確認してから次へ進みます。",
                  "- 各ステップの後: 差分を確認し、docs/INDEX.md・docs/PROGRESS.md・docs/DIGEST.md の更新を確かめ、コミットします。", "",
                  "## ステップ一覧", ""]
        else:
            L += [f"# Agentic Engineering prompt list ({c})", "",
                  "> Generated by `tools/agentic-prompts/generate.py` from `tools/agentic-prompts/config.toml`. Do not edit by hand: change the config and regenerate.",
                  f"> Layout and state files: [{LAYOUT}](../{LAYOUT}). Generator usage: [tools/agentic-prompts/README.md](../tools/agentic-prompts/README.md)", "",
                  "## Settings", "", f"- CLI: {c}",
                  f"- Cross-cutting methods (research only; applied to every later method): {cross}",
                  f"- Other methods (research → plan → implement and summarize): {meth}",
                  f"- Steps: {len(self.steps)}", "",
                  "## How to use", "",
                  "- Go top to bottom: one prompt per step, each pasted into a fresh session. Check the result before moving on.",
                  "- After each step: review the diff, confirm docs/INDEX.md, docs/PROGRESS.md and docs/DIGEST.md were updated, and commit.", "",
                  "## Steps", ""]
        L += [f"{i}. {self.title(s)}" for i, s in enumerate(self.steps, start=1)]
        L += ["", self.t("## Prompts", "## プロンプト"), ""]
        current = None
        for s in self.steps:
            if s.disc is not current:
                current = s.disc
                kind = self.t("cross-cutting", "横断的な手法") if s.disc.kind == "cross" else self.t("method", "その他の手法")
                L += [f"### {circ(s.disc.number)} {s.disc.name}（{kind}）" if self.lang == "ja"
                      else f"### {circ(s.disc.number)} {s.disc.name} ({kind})", ""]
            out = self.output_of(s)
            L += [f"#### {self.title(s)}", "",
                  f"- {self.t('Start', '起動')}: {self.start(s)}",
                  f"- {self.t('Writes', '書き出し')}: `{out}`{sep}`{ja_path(out)}`", "",
                  "````text", self.prompt(s), "````", ""]
        return "\n".join(L).rstrip() + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", type=Path, default=HERE / "config.toml", help="settings file (default: %(default)s)")
    ap.add_argument("--briefs", type=Path, default=HERE / "briefs.toml", help="scope descriptions (default: %(default)s)")
    args = ap.parse_args()
    cfg = tomllib.loads(args.config.read_text(encoding="utf-8"))
    briefs = tomllib.loads(args.briefs.read_text(encoding="utf-8")) if args.briefs.exists() else {}
    gen = Generator(cfg, briefs)
    out = Path(cfg.get("output", f"prompts/agentic-engineering-prompts.{gen.cli}.md"))
    out = out if out.is_absolute() else ROOT / out
    max_kib = float(cfg.get("max_file_kib", 400))
    written = write_split(gen.document(), out, max_kib, gen.lang, clean=True)
    for p in written:
        shown = p.relative_to(ROOT) if p.is_relative_to(ROOT) else p
        print(f"wrote {shown} ({p.stat().st_size / 1024:.1f} KiB)")
    print(f"{len(gen.steps)} steps; {'not split' if len(written) == 1 else f'split into {len(written) - 1} parts'} "
          f"(limit {max_kib:g} KiB per file)")


if __name__ == "__main__":
    main()
