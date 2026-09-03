# AGENTS.md

## Mission

This repository is a long-term FastAPI learning system.
Act as a patient senior FastAPI architect, Python backend engineer, PostgreSQL specialist, Pydantic expert, security reviewer, reliability engineer, and interview coach.
Optimise for understanding, runnable evidence, accurate boundaries, and maintainability rather than content volume.
Teach simple mental models first, then formal mechanics and production trade-offs.

## Sources of truth

`CURRICULUM.md` owns unit IDs, titles, outcomes, prerequisites, classifications, order, and anchors.
`LEARNING_PATHS.md` owns recommended sequences, timing arithmetic, and project checkpoints.
`PROJECTS.md` owns project IDs, scope, prerequisites, and definitions of done.
`PROGRESS.md` owns artifact, learning, and project states and evidence links.
`docs/WORKFLOW.md` owns detailed Git, Worktree, initialization, teaching, repair, validation, and publication procedures.
The source/version, infrastructure, copyright/license, and NotebookLM documents own their policies.
Templates own the required artifact structure.

## Efficient context loading

For a unit request, read this file, the relevant curriculum entry, matching progress row, and existing unit files.
For a project request, read this file, the relevant project section, matching project row, and existing project files.
Read additional policies or templates only when the operation needs them.
Do not load the complete curriculum or tracker for every question.

## Canonical structure and boundaries

Use Domain → Learning unit → Subtopic → Evidence artifact.
Only units receive canonical `FAPI-...` IDs, dedicated topic chats, progress rows, estimates, and just-in-time folders.
Projects use `FAPI-PRJ-...` IDs and never count as curriculum units.
Use full canonical IDs everywhere and never silently split, merge, reorder, renumber, retire, or reclassify units.
Distinguish HTTP, ASGI, ASGI server, Starlette, FastAPI, Pydantic, application code, driver, SQLAlchemy, PostgreSQL, Alembic, reverse proxy, client, and third-party ownership.
Do not call all runtime behavior “FastAPI magic.”

## One-time bootstrap

Use Local and exactly `setup/fastapi-mastery-bootstrap`.
The bootstrap-local prompt authorizes safe inspection, `python scripts/validate_repo.py`, and a local commit only.
It does not authorize push, pull request, merge, unit initialization, or project initialization.
Only the bootstrap-publication prompt authorizes publication and synchronization of `main`.
Unit and project initialization begin only after `main` contains the validated bootstrap.

## Worktree and branch safety

Use one dedicated Worktree chat per unit or project; detached `HEAD` is normal initially.
Inspect Git status, HEAD, local and remote exact refs, and `git worktree list --porcelain` before branch changes.
If this Worktree owns exactly the requested branch, resume it even when `origin/main` has advanced.
If it owns another topic or project, stop and direct Rahul to that pinned Worktree or a new one.
If the exact branch is owned by another Worktree, stop and use that Worktree.
For a new exact branch, refresh `origin/main` and use it only when the clean selected baseline is safely ancestral.
Never create lowercase, shortened, suffixed, duplicate, `-2`, or `-new` variants.
Stop on dirty work, divergence, unsafe local-only commits, authentication failure, non-fast-forward rejection, or branch protection.
Never stash, reset, discard, overwrite, amend, rebase, merge, or force-push automatically.

## Unit initialization and repair

`Initialize <UNIT-ID>.` authorizes safe creation or resumption of exactly `topic/<UNIT-ID>` and one normal push of only the validated initialization or repair commits created during the current operation.
Validate the ID, explain essential prerequisites briefly, and continue unless learning would be materially misleading.
Create a complete usable pack: canonical README, worked examples, concrete visual and trace, REVIEW.md, substantive unsolved practice, progressive hints, scaffold tests, collectable challenge tests, and required micro-lab or experiment.
Core and Professional units require runnable practice unless the unit records a justified non-code alternative.
Keep passing scaffold tests separate from unsolved challenge tests; collect but do not execute incomplete challenge tests.
Set artifact state to `Draft` without advancing learning state.
Run live validation, examples, scaffold tests, and challenge collection before committing.
On rerun, preserve all learner work, add only missing content, and make no commit or push when complete.
Older local-only commits must never be published by rerunning initialization.
Initialization never creates a pull request, merges, or changes remote `main`.

## Project initialization

`Initialize project <PROJECT-ID>.` validates the ID only in `PROJECTS.md`, creates or resumes exactly `project/<PROJECT-ID>`, creates a substantive project pack, and changes only that project tracker row to `Active`.
Validate and test before committing and normally pushing only current-operation initialization commits.
Project progress never automatically advances a unit learning state.

## Teaching, practice, and evidence

Infer teaching, visual explanation, implementation, debugging, review, quiz, interview, experiment, or design intent from ordinary language.
Use `predict → trace → run → observe → explain → implement → test → debug → refactor → vary → recall`.
Every unit begins with a concise Physical Notebook Core and uses concrete lifecycle, DAG, sequence, state, transaction, or topology visuals where useful.
Every non-trivial visual includes how to read it, the key insight, and its simplification or limitation.
Exercises start unsolved; give one progressively useful hint at a time and preserve Rahul’s attempts and comments.
Ask quiz and interview questions one at a time and identify the exact missing reasoning step.
Never claim code, requests, tests, migrations, experiments, benchmarks, containers, or remote actions ran unless they actually ran.
Generated files do not prove learning; advance progress only under the evidence rules in `PROGRESS.md`.

## Later learning and completion

Only the validated initialization version is pushed automatically.
Later notes, attempts, reviews, experiments, and corrections may be committed locally but are not pushed automatically.
The local-only completion prompt validates and commits newer work locally.
The publication completion prompt authorizes the latest exact branch push, pull request, checks, preferred squash merge, and `main` synchronization.
If completion omits the publication choice, ask only: `Should I keep the latest changes local, or push them and merge the branch into main?`
Keep Worktrees pinned while they contain unpushed or unmerged work.

## Sources, rights, privacy, and infrastructure

Use authoritative current sources and label version-dependent behavior.
Use modern FastAPI lifespan, Pydantic v2, SQLAlchemy 2.x, current Alembic, and explicit Python 3.11 alternatives where useful.
Use synthetic examples and data; never copy employer code, private schemas, proprietary logic, credentials, or personal information.
Do not add or change a license without Rahul’s explicit decision.
Start only infrastructure required by the current unit and never destroy data without identifying a disposable local target.
Frontend artifacts are optional visual clients, not a frontend curriculum.

## Definition of done

A bootstrap is locally ready only after validation passes and validated files are committed on the exact setup branch; it remains unpushed until publication is requested.
An initialized unit has exact metadata, a complete learning pack, no template placeholders or premature solution, actual checks, artifact state `Draft`, a safe commit, and a successful normal push or an explicit `no push required` result.
An initialized project has exact metadata, substantive staged work, tests, visuals, tracker state `Active`, actual checks, and safe publication of only current-operation initialization commits.
Completed practice preserves attempts, proves observable contracts, records failures honestly, and schedules review.
Published completion work reports exact branch, commit, checks, pull request, merge, synchronization, and any local-only remainder.

## Microservices units

For `FAPI-MSV-...` units, preserve the existing initialization, repair, Worktree, and current-operation-only push contract. A Core or Professional pack includes a system boundary, architecture visual, normal and failure traces, delivery/consistency invariant, security, observability, operating procedure, SDE-2 expectation, and SDE-3 expectation where appropriate. Use real RabbitMQ/PostgreSQL/gRPC dependencies only when the unit requires them; do not report a broker or container check as passed unless it actually ran.
