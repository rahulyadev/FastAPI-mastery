# Workflow

## One-time bootstrap

Use Local and the exact branch `setup/fastapi-mastery-bootstrap`. The bootstrap-local and publication prompts are in [START_HERE.md](../START_HERE.md). Local setup never pushes automatically.

## Permanent helper chat

Use one helper chat to locate the canonical unit. It returns ID, title, reason, prerequisites, related units, Python references, infrastructure needs, folder existence, and `Initialize <UNIT-ID>.` It does not claim to know whether another chat exists.

## Worktree routing

A Codex chat retains its associated Worktree. Initial detached `HEAD` is normal, and one branch can be checked out in only one Worktree.

Before branch work, inspect:

```bash
git status --porcelain=v1 --untracked-files=all
git rev-parse --verify HEAD
git worktree list --porcelain
git branch --list
git branch --remotes --list
```

Refresh only local remote-tracking observations:

```bash
git fetch --no-tags origin \
  +refs/heads/main:refs/remotes/origin/main
```

For a topic:

```bash
git ls-remote --exit-code --heads origin refs/heads/topic/<UNIT-ID>
git fetch --no-tags origin \
  +refs/heads/topic/<UNIT-ID>:refs/remotes/origin/topic/<UNIT-ID>
```

For a project:

```bash
git ls-remote --exit-code --heads origin refs/heads/project/<PROJECT-ID>
git fetch --no-tags origin \
  +refs/heads/project/<PROJECT-ID>:refs/remotes/origin/project/<PROJECT-ID>
```

The leading `+` refreshes only the named local remote-tracking ref. It does not push or rewrite a local or remote branch.

### Decision matrix

| State | Safe action |
|---|---|
| This Worktree owns the exact requested branch | Resume it even when `origin/main` has advanced |
| Worktree owns another topic/project | Stop and use that pinned chat/Worktree or create a new Worktree |
| Exact branch owned by another Worktree | Stop and use the owning Worktree |
| Neither local nor remote exact branch exists | On a completely clean initial Worktree, create the exact branch from refreshed `origin/main` when the selected commit is safely ancestral |
| Remote only | Fetch exact ref and attach or track it without losing work |
| Local only | Resume only in its owning Worktree; enumerate local-only commits before any push |
| Identical | Resume; if initialization is complete remotely, report `no push required` |
| Local ahead | Enumerate commits; automatic push only if all were created during this initialization/repair |
| Remote ahead with no local-only work | Fast-forward the exact local branch safely |
| Diverged | Stop for explicit reconciliation |
| Dirty Worktree | Stop before `INIT_START` |

Never create alternate branch spellings. Never stash, reset, discard, rebase, merge, amend, or force automatically.

## Clean gate and push boundary

The clean-status command must return no output before recording:

```bash
git rev-parse HEAD
```

as `INIT_START`.

Enumerate local-only and current-operation commits. Automatic publication is allowed only when those lists are identical. Older local-only learning commits cause a stop. If the initialized version is already remote, do not push again.

## Unit initialization

`Initialize <UNIT-ID>.` validates the ID, checks prerequisites, creates/resumes exactly `topic/<UNIT-ID>`, and creates or repairs a complete unit pack. A typical pack is:

```text
units/<domain-slug>/<UNIT-ID>-<slug>/
├── README.md
├── REVIEW.md
├── examples/
│   ├── 01_minimal.py
│   ├── 02_traced.py
│   ├── 03_realistic.py
│   └── 04_failure_case.py
└── practice/
    ├── README.md
    ├── starter.py or app/
    ├── requests.http
    ├── test_examples.py
    └── test_challenge.py
```

Add experiments, migrations, proto, visual clients, Compose files, fixtures, or load tests only when required.

Initialization creates complete teaching content, concrete visuals, real unsolved tasks, scaffold tests, collectable challenge tests, and REVIEW.md. Core and Professional units require a runnable micro-lab unless a justified trace/design alternative is recorded. Challenge tests are collected but not run before learner implementation.

Run:

```bash
python scripts/validate_repo.py --profile live
uv run --group dev python -m compileall -q <unit-directory>
uv run --group dev python -m pytest -q <unit-directory>/practice/test_examples.py
uv run --group dev python -m pytest --collect-only -q <unit-directory>/practice/test_challenge.py
```

Then commit and normally push only current-operation initialization commits. No pull request or merge occurs.

## Idempotent repair

Rerunning initialization on the exact owning branch audits completeness, preserves notes, code, attempts, experiments, and review evidence, and adds only missing content. A complete pack produces no commit or push. Repair publication obeys the same current-operation-only commit boundary.

## Later learning and completion

Later changes remain local. Use the exact completion prompts from START_HERE. Run live validation and relevant tests before local completion or publication. Prefer squash merge and never bypass checks or protections.

## Extended validator setup

Ordinary validation is standard-library-only. Install the locked dev group for self-tests and full report verification:

```bash
uv sync --group dev
uv run --group dev python scripts/validate_repo.py --self-test
```

A content/hash/statistics-only renamed archive check may use the validator’s explicit skip-self-test-comparison option; canonical final report verification compares the self-test summary.

## Microservices unit-pack profile

A Core or Professional MSV initialization creates complete normal-flow and failure-flow material, an architecture or sequence visual, delivery/consistency invariant, security and observability sections, operating commands, incident questions, and SDE-2/SDE-3 expectations. Relevant packs may add `services/`, `worker/`, `contracts/`, `proto/`, `infra/`, `fixtures/`, or an optional generated `visual-client/`. The visual client is never frontend-learning evidence.

RabbitMQ exercises must keep publisher confirms separate from consumer acknowledgements, use bounded retries, avoid unqualified exactly-once claims, and expose outbox/inbox and crash windows where relevant.
