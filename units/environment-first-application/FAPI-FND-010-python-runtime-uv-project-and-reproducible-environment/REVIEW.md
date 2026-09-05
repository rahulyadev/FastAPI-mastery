# Review — FAPI-FND-010 Python runtime, uv project, and reproducible environment

## Closed-book reconstruction

Without opening the README:

1. Recreate the five-layer chain: interpreter request, compatibility declaration, dependency intent,
   locked resolution, installed environment, and runtime evidence.
2. Draw the declaration-to-process DAG and label every uv-owned and Python-owned transition.
3. State the invariant that makes a locked environment observable rather than assumed.
4. Name one limitation of a Python lockfile and one reason not to commit a virtual environment.

Stop after five minutes. Compare the reconstruction with the Physical Notebook Core, mark the first
missing arrow, and explain why that arrow matters.

## Request or execution-lifecycle explanation

There is no HTTP request in this unit. Explain this execution lifecycle in order:

~~~text
shell -> uv project discovery -> Python selection -> lock check -> group sync
      -> environment interpreter -> Python import/metadata lookup -> exit
~~~

Then answer:

1. At which steps can user code not yet have run?
2. Which failure indicates stale resolution rather than a missing installed group?
3. Which live values prove the interpreter and virtual-environment identity?
4. What changes if plain <code>python</code> is used instead of <code>uv run --locked python</code>?

## Debugging questions

1. <code>uv run pytest</code> imports FastAPI, but <code>pytest</code> does not. Capture the first three
   facts you need before proposing a repair.
2. <code>uv lock --check</code> fails after a dependency edit. Why is deleting
   <code>.venv</code> not the first diagnosis?
3. Python is correct and the lock is fresh, but <code>pytest</code> is missing. Which boundary is most
   likely wrong?
4. A package imports but reports an unexpected version. How do module origin and distribution
   metadata complement each other?
5. The environment worked before the repository directory was moved. Which virtual-environment
   property should you suspect?
6. CI passes on Linux and fails building a native dependency on macOS. What does the universal lock
   guarantee, and what does it not guarantee?

For every answer, name the exact command or Python value that would make the claim observable.

## Design and trade-off questions

1. When should a dependency be a runtime project dependency, a development group member, or an
   integration-specific group member?
2. What are the audit and reliability trade-offs between automatic lock updates and
   <code>--locked</code> CI runs?
3. Compare uv's project workflow with standard-library <code>venv</code> plus a separate resolver.
4. Which platform and build facts must be pinned outside <code>uv.lock</code> for a production image?
5. Would you run a package inventory on every service startup? Discuss latency, leakage, and more
   appropriate build-time evidence.
6. How would you support Python 3.11 compatibility testing while retaining 3.14.7 as the canonical
   environment?

## Delayed-recall prompts

- **1 day:** Draw the essential visual and define isolation, locking, syncing, and runtime provenance.
- **3 days:** Diagnose a wrong-interpreter transcript without opening the decision path.
- **7 days:** Rebuild the minimal probe from memory and explain each printed field.
- **14 days:** Design a locked CI preflight with separate runtime and development dependency sets.
- **30 days:** Transfer the invariant to a migration worker or container build and critique its blind
  spots.

Shorten the next interval after any hint, confused lifecycle order, claim that activation proves the
interpreter, claim that locking proves dependency safety, or failure to separate uv from Python and
FastAPI ownership.

## Interview explanation practice

Ask only one question at a time. Start with:

> What is the difference between a virtual environment, a dependency lockfile, and a reproducible
> execution?

Record the exact missing reasoning step rather than “needs more detail.” Follow with one targeted
question from definition, trace, implementation, failure, alternative, performance, security,
testing, changed requirements, or production critique. A strong answer names the artifact, owner,
runtime evidence, and limitation.

## Evidence

Link evidence only after it exists:

- Prediction made before the micro-lab:
- Actual micro-lab output and explanation:
- Learner implementation commit or diff:
- Challenge-test result after implementation:
- Seeded failure diagnosis and correction:
- Closed-book reconstruction:
- Transfer to CI, worker, migration, or deployment:
- Reviewer note identifying the first missing reasoning step:

Generated files, passing scaffold tests, or challenge collection alone are not learning evidence.

## State decision

- Keep <code>Not started</code> after initialization alone.
- Move to <code>Learning</code> only after a real question, prediction, trace, or misconception is
  recorded.
- Move to <code>Practiced</code> only after an original attempt, relevant challenge tests, and an
  explanation of corrections.
- Move to <code>Recalled</code> only after delayed closed-book reconstruction.
- Move to <code>Demonstrated</code> only after a changed scenario and production trade-off explanation.
- Move to <code>Retained</code> only after later successful recall or documented production transfer.

Record the evidence link and weakest point in <code>PROGRESS.md</code>; do not advance a state because
the unit pack exists.
