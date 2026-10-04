# Agentic Engineering prompt list generator

Writes every prompt for **one CLI**, in order, into **one file**. Japanese version: [README.ja.md](./README.ja.md)

```bash
python3 tools/agentic-prompts/generate.py
```

Requires Python 3.11+ (standard library only). Every prompt has the agent read [docs/program-layout.md](../../docs/program-layout.md) for the repository layout, naming and state files.

## Settings: `config.toml`

```toml
cli = "claude-code"        # claude-code | codex | antigravity
language = "ja"            # ja | en (language of the prompts)
output = "prompts/agentic-engineering-prompts.claude-code.ja.md"
max_file_kib = 400         # maximum size of one output file in KiB

cross_cutting = [          # cross-cutting methods: research only, applied to every later method
  "Prompt Engineering",
  "Context Engineering",
  "Memory Engineering",
  "Knowledge Engineering",
]

methods = [                # other methods: research → plan → implement and summarize
  "Spec / Plan Engineering",
  "Verification / Eval Engineering",
  # ...
]
```

- The order of the lists is the order of the prompts. Numbers (①, ②, …) run through `cross_cutting` first, then `methods`.
- To make a list for another CLI, change `cli` and `output` (or keep one config file per CLI and pass it with `--config`).

## Output

1. Settings and the numbered step list.
2. One section per step, in order: the start command (session name, plan mode for plan steps), the files the step writes, and the prompt in a `text` block, ready to paste.

| Step | What the prompt asks for |
| --- | --- |
| Cross-cutting `-1` | Research the method for the CLI, building on the earlier cross-cutting documents → `docs/{slug}-for-cli-agents.{cli}.md` (+ `.ja.md`) |
| Method `-1` | Research the method for the CLI, including what matters for implementation planning → `docs/{NN}-{slug}/research.{cli}.md` |
| Method `-2` | Implementation plan with a mandatory folder hierarchy, reading every document created so far → `plan.{cli}.md` |
| Method `-3` | Implement following the plan, test inside the CLI, review, summarize → `implementation.{cli}.md` |

Every prompt also covers: reading English files only, updating `docs/INDEX.md`, `docs/PROGRESS.md` and `docs/DIGEST.md`, and writing English `.md` with a Japanese `.ja.md`. Prompts for later steps tell the agent to switch to the digest files when the reading would pass about 40% of its context window.

Run one prompt per fresh session, in order, and review each result before the next.

## Splitting large output

If the output is larger than `max_file_kib`, it is split into parts so that every file stays within the limit (for example, under an editor's 512 KiB cap):

- `output` becomes a contents page: the title and intro, then a Markdown link to each part with the headings it contains.
- Parts sit next to it: `<name>.part-01.ja.md`, `<name>.part-02.ja.md`, … Each starts and ends with links to the contents page and the previous and next parts.
- Splits happen only at heading boundaries: first between methods (`###`), then between steps (`####`) if one method is too large. Never inside a heading, a code block or a table. Nothing is dropped or reordered.
- A section with no subheadings that is larger than the limit by itself is kept whole, with a warning.
- When the output fits again, the parts from earlier runs are removed and a single file is written.

To split any other Markdown file the same way:

```bash
python3 tools/agentic-prompts/mdsplit.py docs/some-large-file.md            # limit from max_file_kib
python3 tools/agentic-prompts/mdsplit.py docs/some-large-file.md --max-kib 300
```

The file is replaced by its contents page. The tool refuses to run again on a file that is already split, so parts are never lost.

## Scope descriptions: `briefs.toml`

The prompts embed each method's scope, research focus, starting points, expected artifacts and acceptance evidence from `briefs.toml`. Entries are keyed by slug: the name in lower case with non-alphanumerics replaced by `-` (`"Spec / Plan Engineering"` → `spec-plan-engineering`).

- All 13 default methods have entries.
- Prompts never include earlier research results; every step researches the current official docs. Starting points are marked as hints to verify, and research documents carry their research date.
- A method without an entry still works: its prompts ask the agent to define the scope (the generator prints a warning).
- To add one, append a block:

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

## Files

| File | Purpose |
| --- | --- |
| `config.toml` | One CLI, the cross-cutting methods, the other methods, language, output, size limit |
| `briefs.toml` | Scope descriptions per method |
| `generate.py` | The generator. CLI-specific commands (start, plan mode, checks, reviewer) are built in |
| `mdsplit.py` | Splits Markdown at heading boundaries and writes the contents page (used by the generator; also a standalone tool) |
