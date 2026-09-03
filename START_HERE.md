# Start here

This repository has a one-time setup workflow, then a simple daily FastAPI workflow.

## 1. One-time local bootstrap

Extract the ZIP into the root of the cloned `FastAPI-mastery` repository. Open Codex with **Local** and paste:

```text
Initialize the FastAPI Mastery repository bootstrap locally.

Read AGENTS.md and START_HERE.md. Inspect Git status and verify that the extracted curriculum, learning paths, progress tracker, projects, templates, configuration, infrastructure, links, and Git workflow are valid.

Create or resume the local branch setup/fastapi-mastery-bootstrap, run python scripts/validate_repo.py, commit only the validated bootstrap files, and report the validation results and commit.

Do not push, open a pull request, merge, initialize a unit, or initialize a project. Give me the exact publication prompt when the local bootstrap is ready.
```

The setup branch remains local until you review it. Publish it only with:

```text
Publish the validated FastAPI Mastery bootstrap.

Push setup/fastapi-mastery-bootstrap, create a pull request into main, run validation, merge after checks pass, preferably using a squash merge, and synchronize local main.

Never force-push or bypass failed checks. Stop if authentication, conflicts, branch protection, or unrelated changes require my action.
```

Do not initialize units until the bootstrap is merged and `main` contains the validated baseline.

## 2. Choose a path or ask the helper chat

Use [LEARNING_PATHS.md](LEARNING_PATHS.md), or keep one permanent helper chat and ask naturally:

```text
Which unit teaches FastAPI dependencies deeply?
```

The helper returns the canonical ID, exact title, prerequisites, related units, Python references, infrastructure needs, folder existence, and exact initialization prompt. It cannot know whether another Codex chat exists.

## 3. Open one Worktree chat per unit

Create a new Codex **Worktree** chat for the unit and say only:

```text
Initialize <UNIT-ID>.
```

A new Worktree may begin in detached `HEAD`; this is normal. Initialization creates or safely resumes exactly `topic/<UNIT-ID>`, creates the complete learning pack, validates it, commits it, and normally pushes only that initialization commit. It never creates a pull request or merges.

## 4. Continue naturally

In the same pinned chat, ask:

```text
Explain the request lifecycle visually.
Let me type this from scratch.
Give me one unsolved task.
Review my dependency graph.
Show me the SQL being generated.
Give me the smallest hint.
Quiz me.
```

Later changes may be committed locally but are not pushed automatically.

## 5. Complete the unit

Keep newer work local:

```text
I completed <UNIT-ID>. Keep any new changes local and do not push or merge.
```

Publish and merge the latest work:

```text
I completed <UNIT-ID>. Finalize it, push the latest changes, and merge the topic branch into main.
```

If you state completion without a choice, Codex asks only:

```text
Should I keep the latest changes local, or push them and merge the branch into main?
```

The remote branch already contains the initialized version even when newer learning changes remain local.

## 6. Projects

```text
Initialize project <PROJECT-ID>.
```

```text
I completed project <PROJECT-ID>. Keep any new changes local and do not push or merge.
```

```text
I completed project <PROJECT-ID>. Finalize it, push the latest changes, and merge the project branch into main.
```

## 7. Validation and tools

Ordinary structural validation uses only the Python standard library:

```bash
python scripts/validate_repo.py
```

Install extended tools and run self-tests with:

```bash
uv sync --group dev
uv run --group dev python scripts/validate_repo.py --self-test
```

Infrastructure commands are in [docs/TOOLCHAIN_AND_INFRASTRUCTURE.md](docs/TOOLCHAIN_AND_INFRASTRUCTURE.md).

## Distributed-service routes

Use the helper chat to choose one `FAPI-MSV-...` unit. Start RabbitMQ or other optional infrastructure only when that unit says it is required. The everyday initialization and completion prompts do not change.
