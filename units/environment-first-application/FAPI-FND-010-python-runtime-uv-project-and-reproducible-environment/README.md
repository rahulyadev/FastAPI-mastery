# FAPI-FND-010 — Python runtime, uv project, and reproducible environment

## Physical Notebook Core

### Problem or pressure

Python source does not carry its interpreter or installed packages inside the file. The same checkout
can therefore use a global Python on one command, a project virtual environment on another, and a
different transitive dependency graph on a teammate's machine. That ambiguity produces misleading
import errors and bugs that cannot be reproduced.

### One-sentence mental model

> A reproducible Python environment is a verified chain from project intent, through a locked
> resolution and isolated installation, to the exact interpreter that executes the command.

### Essential visual

~~~text
SELECTION                 DECLARATION                  RESOLUTION
.python-version           pyproject.toml               uv.lock
"prefer 3.14.7"           "3.11 <= Python < 3.15"      exact package graph
       \                         |                         /
        \                        |                        /
         +-----------------------v-----------------------+
                                 |
                          uv sync --locked
                                 |
                                 v
                    .venv/ interpreter + packages
                                 |
                           uv run --locked ...
                                 |
                                 v
             sys.executable + importlib.metadata.version(...)
                          observable evidence
~~~

#### How to read this visual

Read from the three declarations at the top toward the running process. <code>.python-version</code>
requests a preferred interpreter; <code>requires-python</code> states the project's compatible range;
and <code>uv.lock</code> records uv's exact resolved graph, including environment-specific branches.
Sync materializes the selected graph in <code>.venv</code>. The final arrow matters most: a shell
prompt or activated-environment label is only a hint, while the running process can report
<code>sys.executable</code>, its virtual-environment prefixes, and installed distribution versions.

#### Key insight

The files are promises; runtime inspection is evidence. Reproducibility requires both. A correct
lockfile cannot help a command accidentally launched by a global interpreter, and an isolated
interpreter is not reproducible when its packages were installed without the project lock.

#### Simplification or limitation

The drawing omits operating system, CPU architecture, native libraries, package indexes, credentials,
environment variables, and external services. A universal uv lock can encode platform branches, but
it does not make every machine identical or prove that a dependency is safe. Production images and CI
must also pin and verify the surrounding platform and build process.

### Governing lifecycle rule or invariant

1. Change dependency intent in <code>pyproject.toml</code>, resolve it into
   <code>uv.lock</code>, and review both files together.
2. Run project commands through uv and verify the live interpreter and installed metadata; never infer
   the environment merely from the command name <code>python</code> or a shell prompt.
3. In validation and deployment, use a locked check or sync so the command fails instead of silently
   rewriting dependency evidence.

### Minimal code skeleton

~~~python
from importlib.metadata import version
from pathlib import Path
import platform
import sys

print(f"python={platform.python_version()}")
print(f"executable={Path(sys.executable)}")
print(f"virtual_environment={sys.prefix != sys.base_prefix}")
print(f"fastapi={version('fastapi')}")
~~~

Run it with <code>uv run --locked python probe.py</code>. The code reports Python-owned runtime facts;
uv owns interpreter discovery, dependency resolution, lock management, and project-environment sync.

### Common failure, comparison, and interview cues

- Failure: <code>pytest</code> from the shell and <code>uv run pytest</code> use different
  interpreters, so only one can import the project's packages.
- Compare with: <code>python -m venv</code> plus a separately maintained requirements workflow can
  isolate packages, but this repository uses uv to coordinate selection, locking, syncing, and runs.
- Recall: Which artifact states intent, which records resolution, and which runtime value proves what
  actually executed?

## 1. Learning outcomes and evidence

By the end of this unit, you can:

1. Explain the distinct jobs of <code>.python-version</code>, <code>requires-python</code>,
   <code>pyproject.toml</code>, <code>uv.lock</code>, and <code>.venv</code>.
2. Create or sync an isolated environment with the intended dependency groups without starting any
   database, broker, or web server.
3. Prove interpreter provenance with <code>sys.executable</code>,
   <code>sys.prefix</code>, and <code>sys.base_prefix</code>.
4. Inspect installed distributions with <code>importlib.metadata</code> and compare them with project
   declarations and the lock.
5. Diagnose wrong-interpreter, missing-group, stale-lock, unsupported-Python, and wrong-working-directory
   failures without deleting an environment reflexively.
6. Explain what a lockfile does and does not make reproducible.

The canonical evidence profile is <code>E+T+I+D+R+M</code>:

- Explain the environment chain and ownership boundaries.
- Trace one command from uv discovery to the executing interpreter.
- Implement and test the unsolved environment inspector.
- Debug the seeded executable-provenance defect.
- Reconstruct the model after spaced delay.
- Transfer the checks to a CI or deployment command.

Artifact generation leaves learning state at <code>Not started</code>. Evidence is earned only from
Rahul's predictions, attempts, observations, explanations, and later recall.

## 2. Prerequisites and smallest bridge

There are no canonical FastAPI prerequisites. This is the first foundation unit.

The smallest Python bridge is knowing that a program is executed by a particular interpreter and that
imports are resolved from that interpreter's configured paths. If virtual environments or TOML are
new, use the worked examples first; no FastAPI route knowledge is required.

Optional prior recall:

- <code>PY-MOD-050</code> for Python versions, virtual environments, and executable provenance.
- <code>PY-MOD-060</code> for project metadata, dependency declarations, and locking.

## 3. Simple explanation and owning layer

Think of the environment as five related but non-interchangeable things:

| Artifact or observation | Question it answers | Owner |
|---|---|---|
| <code>.python-version</code> | Which Python should uv prefer for this project? | uv project configuration |
| <code>project.requires-python</code> | Which Python versions does this project claim to support? | Python packaging metadata |
| Dependencies and groups in <code>pyproject.toml</code> | What direct capabilities does the project request? | Python packaging plus project policy |
| <code>uv.lock</code> | Which complete version graph did uv resolve across supported environments? | uv |
| <code>.venv</code> | Which interpreter and packages are installed here now? | Python virtual environment, materialized by uv |
| <code>sys.executable</code> and distribution metadata | What is this process actually using? | Running Python process |

The repository currently requests Python <code>3.14.7</code>, advertises compatibility from
<code>3.11</code> up to but excluding <code>3.15</code>, keeps application packages under
<code>project.dependencies</code>, and keeps development and integration tooling in dependency
groups. Those facts are repository policy, not FastAPI behavior.

FastAPI does not select Python, create a virtual environment, or resolve packages. It is one installed
distribution in the environment. Uvicorn is a separate ASGI server distribution. Pydantic is a
separate validation library. uv may install all three according to project metadata, but installation
does not transfer ownership of their runtime behavior to uv.

## 4. Runtime or request-lifecycle trace

This unit has an execution lifecycle, not an HTTP request lifecycle:

~~~text
1. Shell starts: uv run --locked --group dev python examples/01_minimal.py
2. uv walks to the project root and reads configuration.
3. uv evaluates .python-version and project.requires-python.
4. uv verifies that uv.lock agrees with project metadata because --locked was requested.
5. uv ensures the selected dependency groups are installed in the project environment.
6. uv starts the environment's Python executable.
7. Python initializes sys.path and imports the script's modules.
8. importlib.metadata reads installed distribution metadata from that environment.
9. The process prints evidence: version, executable, prefixes, and package versions.
10. The process exits; no FastAPI application or ASGI server was started.
~~~

Two important branches:

- If metadata and the lock disagree, a locked run fails before user code rather than changing the
  lock.
- If a dependency is absent from the selected groups, Python reaches the import and raises
  <code>ModuleNotFoundError</code>; that is different from selecting an unsupported interpreter.

## 5. Detailed visual model

### Declaration-to-process evidence DAG

~~~text
                    .python-version
                          |
                          v
system Pythons ---> uv interpreter discovery <--- requires-python
                          |
                          v
pyproject direct intent -> resolver -> uv.lock
       |                              |
       +---------- group choice ------+
                          |
                          v
                      uv sync
                          |
              +-----------+-----------+
              |                       |
         .venv/bin/python       .venv site-packages
              |                       |
              +-----------+-----------+
                          |
                       process
                    /      |       \
          sys.executable sys.prefix metadata.version
~~~

#### How to read this visual

Follow arrows into the process. Interpreter discovery and dependency resolution are separate
decisions. The group choice filters what is installed from the resolved graph. Runtime evidence then
comes from two places: Python's own process state and the installed distribution metadata.

#### Key insight

There is no single “environment version.” A useful report is a tuple containing at least the Python
version, executable path, isolation state, selected groups, lock state, and relevant package versions.

#### Simplification or limitation

uv can resolve all declared groups together even when only some groups are installed. The diagram
does not show source-versus-wheel selection, environment markers, indexes, build backends, or editable
project installation. Those become important when debugging platform-specific builds.

### Mismatch decision path

~~~text
Import or version surprise
        |
        +-- Is sys.executable the expected .venv interpreter?
        |        no -> command provenance problem
        |        yes
        |
        +-- Does running Python satisfy requires-python and the requested pin?
        |        no -> interpreter selection problem
        |        yes
        |
        +-- Does uv lock --check succeed?
        |        no -> declaration/resolution mismatch
        |        yes
        |
        +-- Was the needed group synced?
        |        no -> installation-selection problem
        |        yes
        |
        +-- Does importlib.metadata show the expected distribution?
                 no -> installed-state or package-name/import-name problem
                 yes -> investigate application/import behavior in its owning unit
~~~

#### How to read this visual

Start with the live process, then move backward toward declarations. Stop at the first failed
invariant and preserve its exact output before changing files or installing anything.

#### Key insight

“Recreate the virtual environment” is a last-resort repair, not a diagnosis. The path identifies the
layer that disagrees and produces reusable evidence.

#### Simplification or limitation

The path assumes project metadata is trustworthy and that the failure is local. Index outages,
compromised artifacts, native-library loader errors, and editable-install mistakes need additional
evidence.

## 6. Worked examples

### 6.1 Minimal example

[<code>examples/01_minimal.py</code>](examples/01_minimal.py) prints the running Python version,
absolute executable, virtual-environment status, and key distribution versions. It is deliberately
read-only.

Run:

~~~bash
uv run --locked --group dev python units/environment-first-application/FAPI-FND-010-python-runtime-uv-project-and-reproducible-environment/examples/01_minimal.py
~~~

### 6.2 Traced runtime example

[<code>examples/02_traced.py</code>](examples/02_traced.py) walks the five layers in order and names
the owner of every observation. Run it once with uv and, only as a prediction exercise, compare what
would change under a global <code>python</code>.

### 6.3 Realistic backend example

[<code>examples/03_realistic.py</code>](examples/03_realistic.py) performs a small preflight like one
a backend repository could use: it compares the requested and running Python, checks isolation and
lock presence, and verifies exact direct package pins against installed metadata. It returns a
non-zero status when an invariant fails, making it suitable for automation.

### 6.4 Failure or debugging example

[<code>examples/04_failure_case.py</code>](examples/04_failure_case.py) diagnoses a synthetic incident
without mutating the real environment. Its snapshot combines a wrong executable, wrong Python patch,
missing development group, and package drift so each symptom can be assigned to the correct layer.

### 6.5 Comparison with an alternative

The standard library can create isolation with <code>python -m venv .venv</code>. Activation modifies
the shell's <code>PATH</code>, but activation is not required when invoking the environment's
interpreter by absolute path. A separate tool or reviewed requirements files must then own dependency
resolution and repeatable installation.

uv's project workflow combines Python discovery, a universal lock, group-aware sync, and
environment-aware execution. This is a coordination advantage, not a different kind of Python
interpreter. The observable proof remains inside the Python process.

## 7. Formal mechanics and boundaries

### Python selection

<code>.python-version</code> is a uv-readable version request. It does not change the language
compatibility declared by <code>requires-python</code>. In this repository, exact selection
<code>3.14.7</code> lies within <code>>=3.11,<3.15</code>. A contributor may test another supported
version explicitly, but must label that as a compatibility run rather than the canonical lock check.

### Virtual-environment identity

In a virtual environment, Python exposes the environment prefix through <code>sys.prefix</code> and
the base installation through <code>sys.base_prefix</code>. Their inequality is a stronger portable
test than looking for a directory name or trusting <code>VIRTUAL_ENV</code>. On systems where it can
be determined, <code>sys.executable</code> gives the interpreter's absolute executable path. Preserve
that reported path when checking provenance: resolving a POSIX virtual-environment symlink can lead
to the base interpreter target and erase the useful <code>.venv/bin</code> launcher identity.

### Dependency intent and groups

<code>project.dependencies</code> describes runtime dependencies of the project. The standardized
<code>dependency-groups</code> table is appropriate for internal development sets such as tests and
linters; groups are not published as project dependency metadata. This repository also uses groups
for optional learning integrations such as PostgreSQL, RabbitMQ, gRPC, Redis, and observability.
Installing a group is a local capability choice; all declared groups still participate in uv's
project resolution unless explicitly configured as conflicts.

### Locking and syncing

Locking resolves declared requirements into <code>uv.lock</code>. Syncing installs the applicable
subset into the project environment. <code>uv lock --check</code> verifies freshness without
upgrading merely because newer packages exist. <code>uv sync</code> is exact by default, so packages
outside the selected project set can be removed. <code>uv run</code> automatically checks and syncs
unless flags change that behavior; <code>--locked</code> is valuable for evidence because it prevents
an unnoticed lock update.

### Package and import names

Distribution names used by <code>importlib.metadata.version()</code> are not always identical to
Python import names. For example, project metadata is the authority for the distribution name.
An import succeeding proves that some module was found, while installed metadata tells which
distribution record is present; neither alone proves the whole environment matches the lock.

### Layer boundary

| Concern | Owning layer |
|---|---|
| Executable, prefixes, import machinery | Python runtime |
| Compatible Python range and dependency fields | Python packaging metadata plus project policy |
| Python discovery, resolution, uv lock schema, group sync | uv |
| Route registration and dependency injection | FastAPI, outside this unit |
| Socket listening and worker processes | ASGI server such as Uvicorn, outside this unit |
| Validation semantics | Pydantic, outside this unit |
| Database availability | Driver/database/infrastructure, outside this unit |

## 8. Failure modes and edge cases

| Symptom | Likely boundary | First evidence to capture | Safe next move |
|---|---|---|---|
| Package imports under <code>uv run</code> but not plain <code>python</code> | Command provenance | Both values of <code>sys.executable</code> | Standardize the command; do not install globally |
| uv reports no compatible Python | Selection/compatibility | Pin, <code>requires-python</code>, installed candidates | Install or explicitly select a supported interpreter |
| Locked run says lock is stale | Declaration/resolution | Git diff for TOML and lock plus exact error | Resolve deliberately and review the lock change |
| Pytest is absent | Group selection | Selected groups and package metadata | Sync the <code>dev</code> group |
| A package version differs | Installed state or wrong process | Executable plus distribution version | Verify lock, then perform a locked exact sync |
| uv discovers the wrong project | Working-directory discovery | Current directory and located TOML path | Run from the intended project or pass explicit project context |
| Environment breaks after moving its directory | venv portability | Prefix/executable paths | Recreate only that environment from committed declarations |
| Resolved executable appears outside <code>.venv</code> while prefixes prove isolation | Symlink interpretation | Raw <code>sys.executable</code>, resolved target, and prefixes | Preserve the raw launcher path; explain the symlink target separately |
| One operating system selects a different artifact | Platform branch/native build | OS, architecture, Python, wheel/source details | Compare applicable lock branch and native prerequisites |
| Import name and package name differ | Packaging/import boundary | Module origin and distribution metadata | Inspect both names; do not guess from one |
| Lock works but application still differs | External configuration | Environment variables and external service versions | Move to the owning configuration/infrastructure unit |

Do not “repair” these by deleting broad directories, changing global packages, or using an insecure
index option. Preserve the command, error, executable, and project diff first.

## 9. Performance, resource, transaction, or security costs

Environment creation and exact sync consume network, disk, resolver, decompression, and build time.
Caching can reduce that cost, but a warm cache is not correctness evidence. Dependency groups reduce
unnecessary local and production installations; production images generally should not carry test,
broker, or database tooling they do not execute.

There is no database transaction in this unit. The closest invariant is change atomicity in version
control: review <code>pyproject.toml</code> and <code>uv.lock</code> as one dependency change.

Security considerations:

- A lock reduces unintended version drift but can faithfully reproduce a vulnerable or malicious
  version. It is not a vulnerability scanner, signature policy, or trust decision.
- Commit the lock and project metadata, not <code>.venv</code>, credentials, private-index tokens, or
  machine-local configuration.
- Do not bypass TLS verification with insecure-host options to make installation “work.”
- Review dependency source and lock diffs. Separate deliberate upgrades from ordinary sync.
- Treat install-time build code as code execution. Prefer reviewed sources and controlled CI/network
  policy.

## 10. Production relevance and anti-signals

A production service should make the selected interpreter and dependency graph reviewable, use a
failing locked install in CI/builds, and expose build identity through deployment metadata rather than
silently updating itself at startup. A container adds an operating-system boundary; it complements
the Python lock rather than replacing it.

Useful production signals include Python version, application revision, lock/build digest, and
sanitized package inventory. Avoid logging credentials, index URLs containing tokens, or the whole
environment variable set.

Anti-signals:

- “It works in my activated shell” without an executable path.
- Running <code>pip install</code> manually until imports pass, with no metadata or lock review.
- Committing <code>.venv</code>.
- Installing every integration group into every runtime image.
- Allowing CI to rewrite <code>uv.lock</code>.
- Calling all startup and import failures “FastAPI issues.”
- Claiming bit-for-bit reproducibility from a Python lock while ignoring the base image and native
  libraries.

## 11. Testing and debugging strategy

Use a narrow evidence ladder:

~~~bash
uv --version
uv python find
uv run --locked python -c "import platform, sys; print(platform.python_version()); print(sys.executable); print(sys.prefix != sys.base_prefix)"
uv lock --check --python 3.14.7
uv run --locked python -c "from importlib.metadata import version; print(version('fastapi'))"
uv tree --locked
~~~

Interpret each command separately. <code>uv --version</code> describes the tool, not Python.
<code>uv python find</code> describes selection, not the running process. The Python probe gives live
provenance. The lock check verifies declaration consistency. The metadata probe verifies one installed
distribution. The tree explains dependency relationships but does not prove application behavior.

Tests in this pack:

- <code>practice/test_examples.py</code> runs every worked example and the micro-lab.
- <code>practice/test_challenge.py</code> is collected during initialization but remains unexecuted
  until Rahul implements the challenge.
- Repository validation checks artifact structure and syntax; it does not prove learning.

## 12. Practice ladder

Use [<code>practice/README.md</code>](practice/README.md) and follow:

~~~text
predict -> trace -> run -> observe -> explain -> implement -> test -> debug -> vary -> recall
~~~

The micro-lab is runnable now. The starter inspector and challenge tests are intentionally unsolved.
Do not read or generate a completed implementation before recording a prediction and first attempt.

## 13. Interview questions, traps, and follow-ups

Ask one at a time:

1. **Definition:** What makes a Python project environment reproducible rather than merely isolated?
2. **Runtime trace:** Trace <code>uv run --locked pytest</code> from project discovery to the Python
   process that collects tests.
3. **Implementation:** Which minimal fields would you include in an environment preflight report?
4. **Failure:** Why can <code>python -c "import fastapi"</code> fail while
   <code>uv run python -c "import fastapi"</code> succeeds?
5. **Alternative:** Compare uv project management with <code>python -m venv</code> plus pinned
   requirements. Which responsibilities remain in both approaches?
6. **Performance:** How would you reduce dependency-install time without weakening the locked-build
   invariant?
7. **Security:** What supply-chain risk remains after every package is locked to an exact version?
8. **Testing:** How do you prove that a test runner used the intended interpreter and dependency set?
9. **Changed requirement:** CI must test Python 3.11 while the canonical developer pin is 3.14.7.
   How do you label and execute that without pretending it was the canonical check?
10. **Production critique:** A container build runs an unlocked sync and commits no lockfile. What
    failure modes and audit gaps follow?

Common traps:

- Equating a compatibility range with an exact Python selection.
- Equating activation with isolation; activation changes command lookup, while the interpreter and
  prefixes provide evidence.
- Assuming the lock contains one unconditional package list for every platform.
- Treating installed import success as proof that project metadata and the lock agree.
- Saying FastAPI creates or activates the environment.

## 14. Explanation exercises

1. Explain the five environment layers to a developer who only knows <code>pip install</code>.
2. Draw the execution trace from memory and label each uv-owned and Python-owned step.
3. Given two executable paths and package inventories, identify the first divergence and the evidence
   still missing.
4. Explain why exact package pins do not freeze the operating system, environment variables, database,
   or package-index availability.
5. Give a 60-second interview answer, then expand it into a production build review.
6. Transfer the invariant to a worker or migration command: state what remains the same before any
   FastAPI application is imported.

## 15. Experiment decision

**Not required.** The unit is D1 and its claims are observable through the required micro-lab and
scaffold tests; a separate experiment would duplicate that evidence. The micro-lab records live
interpreter, prefix, project declaration, lock presence, and installed package metadata without
changing the environment.

## 16. Python Mastery references

- [PY-MOD-050 — Python versions and virtual environments](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-mod-050)
  is the hard conceptual prerequisite: interpreter selection, isolation, and executable provenance.
- [PY-MOD-060 — Pyproject, dependencies, locking, and reproducibility](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-mod-060)
  is the soft prerequisite for dependency intent, groups, and lock review.
- [PY-MOD-010 — Modules, packages, and executable modules](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-mod-010)
  is optional recall for understanding why the selected interpreter determines import behavior.

Smallest bridge for this unit: print <code>sys.executable</code>, compare
<code>sys.prefix</code> with <code>sys.base_prefix</code>, read one group in
<code>pyproject.toml</code>, and find one installed version in <code>uv.lock</code>.

## 17. Authoritative sources and version notes

Primary sources read for this unit:

- [uv: Python versions](https://docs.astral.sh/uv/concepts/python-versions/) — interpreter discovery,
  version requests, <code>.python-version</code>, and <code>requires-python</code>.
- [uv: Locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/) — lock freshness,
  automatic lock/sync behavior, exact sync, and group selection.
- [uv: Managing dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/) — project
  dependency fields and dependency-group behavior.
- [Python Packaging User Guide: Dependency Groups](https://packaging.python.org/en/latest/specifications/dependency-groups/)
  — standardized group purpose and structure.
- [Python 3.14: <code>venv</code>](https://docs.python.org/3/library/venv.html) and
  [Python 3.14: <code>sys.executable</code>](https://docs.python.org/3/library/sys.html#sys.executable)
  — virtual-environment prefixes, activation, and executable provenance.
- [FastAPI: Virtual Environments](https://fastapi.tiangolo.com/virtual-environments/) — current
  FastAPI guidance to manage projects and run commands with uv.

Repository baseline at initialization:

- Canonical Python: <code>3.14.7</code>; examples use only Python 3.11-compatible syntax.
- Supported Python metadata: <code>>=3.11,<3.15</code>.
- FastAPI <code>0.141.1</code>, Pydantic <code>2.13.4</code>, Uvicorn
  <code>0.52.4</code>, and uv lock schema as committed in the repository.
- Source review date: 2026-09-05.

uv behavior is version-dependent. A newer uv can change CLI details or lock schema support; use the
repository lock and re-read current uv documentation before changing the pinned baseline.

## 18. Open uncertainties

- A universal resolution still has platform-conditional artifacts; this unit does not prove every
  locked branch installs on every supported architecture.
- The repository does not yet define a production image digest or organization-wide artifact
  attestation policy.
- Private-index authentication, offline builds, SBOM generation, and vulnerability-response policy
  belong to later security and operations units.
- Exact compatibility across the full <code>>=3.11,<3.15</code> range requires a test matrix; the
  canonical 3.14.7 run alone cannot prove it.
