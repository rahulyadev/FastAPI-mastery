# Practice — FAPI-FND-010 Python runtime, uv project, and reproducible environment

## Learning question

Can you prove that a command is using the intended Python and applicable locked packages, then locate
the first broken link without changing the environment until the evidence identifies a cause?

## Initial state

The unit already contains four runnable worked examples and <code>micro_lab.py</code>. The micro-lab
is read-only: it reports project declarations, the lock header, interpreter provenance, virtual
environment prefixes, declared group names, and installed distribution versions.

<code>starter.py</code> defines the public data structures and three unsolved functions:

- <code>load_project_contract</code> reads and validates project declarations.
- <code>evaluate_environment</code> compares a selected slice of the contract with runtime evidence.
- <code>render_report</code> creates a stable terminal or CI report.

<code>broken_probe.py</code> contains a separate seeded defect. Scaffold tests exercise only completed
examples and the micro-lab. Challenge tests import the starter safely, collect successfully, and must
remain unexecuted until Rahul has made a meaningful implementation attempt.

Files allowed to change during the challenge:

- <code>practice/starter.py</code>
- <code>practice/broken_probe.py</code>
- this README's Attempt and review record

Do not change challenge assertions merely to make an incorrect implementation pass.

## Concrete unsolved tasks

### Task 1 — Predict and trace

Before running anything, write a prediction for:

1. the Python version requested by the project;
2. the Python version and executable path the uv command will actually use;
3. whether <code>sys.prefix</code> will equal <code>sys.base_prefix</code>;
4. which dependency groups are declared and which group the test command needs;
5. the installed FastAPI and pytest versions;
6. the exact lifecycle step at which a stale lock should stop a locked run.

Then run:

~~~bash
uv run --locked --group dev python units/environment-first-application/FAPI-FND-010-python-runtime-uv-project-and-reproducible-environment/practice/micro_lab.py
~~~

Record differences between prediction and observation. Explain which values are project declarations,
which are uv observations, and which come from the running Python process. Do not treat a matching
prediction as sufficient; state what the observation still cannot prove.

### Task 2 — Implement the contract inspector

Implement the three functions in <code>starter.py</code>.

#### Expected behavior

<code>load_project_contract(project_root)</code> must:

1. Require readable <code>.python-version</code>, <code>pyproject.toml</code>, and
   <code>uv.lock</code>.
2. Read the requested Python and <code>project.requires-python</code>.
3. return dependency-group names in deterministic sorted order;
4. extract simple exact <code>==</code> pins from runtime dependencies and every dependency group,
   while leaving ranges and environment-marker interpretation out of this D1 exercise;
5. normalize distribution names by treating runs of hyphens, underscores, and periods equivalently;
6. record <code>None</code> as the group for runtime dependencies and the group name for group pins;
7. return pins in deterministic order;
8. read the integer lock schema version;
9. raise <code>EnvironmentContractError</code> with the relevant filename in the message when a
   required file or field is missing or malformed.

<code>evaluate_environment(contract, evidence, selected_groups)</code> must:

1. emit a <code>python-selection</code> check comparing the running version with the exact project
   request;
2. emit a <code>virtual-environment</code> check using prefix/base-prefix inequality and executable
   containment within the environment prefix;
3. emit a failing <code>group-selection</code> check for each requested group absent from the
   declaration;
4. check all exact runtime pins and only the exact pins belonging to selected, declared groups;
5. emit package codes in the form <code>package:normalized-name</code>;
6. report missing distributions as <code>not-installed</code>;
7. produce deterministic check order without mutating the supplied contract or evidence.

<code>render_report(report)</code> must return one plain-text line per check:

~~~text
[PASS] check-code: useful detail
[FAIL] another-code: useful detail
~~~

The rendered string must end with exactly one newline when at least one check exists, contain no ANSI
escape sequences, and be empty for an empty report.

Constraints:

- Use Python 3.11-compatible syntax and the standard library.
- Do not run uv, pip, or a shell command from the inspector.
- Do not edit, create, delete, or sync an environment.
- Do not hard-code this repository's absolute path or current package versions.
- Keep declaration loading separate from runtime comparison.
- Preserve the supplied public dataclasses and function signatures.

### Task 3 — Debug and vary

First, diagnose why <code>broken_probe.current_executable()</code> can return a plausible-looking
value that is not evidence of the executing interpreter. Write the failed invariant before editing
the function, then repair it without spawning another process or searching <code>PATH</code>.

Next vary the scenario:

1. Evaluate runtime-only plus <code>dev</code> pins.
2. Evaluate runtime-only plus <code>postgres</code> pins.
3. Explain why a missing PostgreSQL package is irrelevant in the first report but relevant in the
   second.
4. Add one synthetic wrong-Python case and one missing-distribution case to your notes.
5. Preserve the external report format while explaining which requirements would force a D2
   extension, such as full PEP 440 specifier evaluation or environment-marker handling.

Do not start PostgreSQL or any other service. This unit verifies installation metadata, not service
availability.

## Acceptance criteria

- [ ] A prediction exists from before the micro-lab run.
- [ ] Observed output is recorded separately from the prediction.
- [ ] Every observation is assigned to Python, packaging metadata, uv, or project policy.
- [ ] <code>load_project_contract</code> handles valid input and clear missing/malformed metadata
  failures.
- [ ] Runtime pins and selected-group pins are checked; unselected group pins are ignored.
- [ ] Interpreter and virtual-environment checks use live evidence rather than shell labels.
- [ ] The executable-provenance defect is diagnosed before it is repaired.
- [ ] The report is deterministic, plain text, and useful on failure.
- [ ] Scaffold examples still pass.
- [ ] Learner challenge tests pass only after the learner implementation.
- [ ] No environment, lock, or dependency declaration is mutated by the inspector.
- [ ] Reflection explains lockfile limitations, security boundaries, and production transfer.

## Commands

Run from the repository root.

Inspect before implementation:

~~~bash
uv run --locked --group dev python units/environment-first-application/FAPI-FND-010-python-runtime-uv-project-and-reproducible-environment/practice/micro_lab.py
uv run --locked --group dev python units/environment-first-application/FAPI-FND-010-python-runtime-uv-project-and-reproducible-environment/practice/micro_lab.py --json
~~~

Validate completed examples:

~~~bash
uv run --group dev python -m compileall -q units/environment-first-application/FAPI-FND-010-python-runtime-uv-project-and-reproducible-environment
uv run --group dev python -m pytest -q units/environment-first-application/FAPI-FND-010-python-runtime-uv-project-and-reproducible-environment/practice/test_examples.py
~~~

Before implementation, collect but do not execute the incomplete challenge:

~~~bash
uv run --group dev python -m pytest --collect-only -q units/environment-first-application/FAPI-FND-010-python-runtime-uv-project-and-reproducible-environment/practice/test_challenge.py
~~~

Only after recording an original attempt:

~~~bash
uv run --group dev python -m pytest -q units/environment-first-application/FAPI-FND-010-python-runtime-uv-project-and-reproducible-environment/practice/test_challenge.py
~~~

Repository contract check:

~~~bash
python scripts/validate_repo.py --profile live
uv lock --check --python 3.14.7
~~~

Do not execute intentionally incomplete challenge tests during initialization and report them as
passing.

## Troubleshooting

### uv cannot select Python

Capture <code>.python-version</code>, <code>requires-python</code>, <code>uv --version</code>, and
the output of <code>uv python find</code>. If the canonical interpreter is absent and installation
would require network access, label the canonical check skipped rather than substituting another
interpreter without saying so.

### The micro-lab says virtual environment is false

Print <code>sys.executable</code> in the same command. Confirm that the command began with
<code>uv run</code> and that uv found this repository's project root. Do not solve the symptom with a
global installation.

### A distribution is not installed

Separate runtime packages from group packages. Confirm the requested group, inspect
<code>pyproject.toml</code> and <code>uv.lock</code>, then use a locked sync. A package missing from an
unselected integration group is not a failure for a runtime-plus-dev check.

### Lock checking fails

Preserve the exact error and inspect the dependency-declaration and lock diff. A release appearing on
the package index does not itself make the lock stale. Resolve changes deliberately; do not hand-edit
<code>uv.lock</code>.

### Imports fail only from one command

Compare executable paths and module origins from both commands. The shell prompt and command spelling
are insufficient evidence.

## Progressive hints

No hint has been issued at initialization. Make and preserve a meaningful attempt first. Then request
one hint at a time; the instructor should identify the smallest missing reasoning step and avoid
revealing later steps or a completed implementation. If a hint is used, record it and shorten the next
recall interval.

## Reflection questions

1. Which values in your report are intent, resolved state, installed state, and live process state?
2. Why is <code>sys.executable</code> stronger evidence than <code>VIRTUAL_ENV</code> or a prompt
   prefix?
3. Why can a universal lock yield different installed artifacts on two platforms without being
   inconsistent?
4. What does exact sync remove, and why can that be both helpful and surprising?
5. Why is a locked dependency graph not a security verdict?
6. Which facts would a production container need beyond this Python-level report?
7. How would you keep a Python 3.11 compatibility run distinct from the canonical 3.14.7 check?
8. Why is a database package being installed different from PostgreSQL being reachable?
9. What did the seeded failure make you assume, and what observation corrected the assumption?

## Attempt and review record

Preserve Rahul's original code, comments, prediction, command output, failing assertions, and reasoning.
Do not replace an attempt with a polished comparison. Add a comparison implementation only after the
exercise is explicitly closed.

- Prediction recorded:
- First command and observed output:
- First failed invariant:
- First implementation attempt:
- Hint used, if any:
- Correction and explanation:
- Challenge result after implementation:
- Changed-scenario result:
- Weakest reasoning point:
- Next review date:
