# Bootstrap bundle manifest

Files are placed directly at archive root. `units/` and `projects/` are intentionally absent until initialized. No license is selected.

| Path | Purpose |
|---|---|
| `.gitignore` | Excludes local environments, caches, secrets, and generated output. |
| `.python-version` | Pins the canonical Python runtime. |
| `.env.example` | Synthetic local infrastructure variables. |
| `AGENTS.md` | Lean repository-wide Codex contract. |
| `API_DESIGN_PLAYBOOK.md` | Reusable API design comparisons and review questions. |
| `BUNDLE_MANIFEST.md` | Bootstrap inventory and purpose. |
| `CURRICULUM.md` | Canonical unit catalog. |
| `INTERVIEW_PLAYBOOK.md` | Senior explanation and mock protocol. |
| `LEARNING_PATHS.md` | Prerequisite-safe paths and timing. |
| `NOTEBOOKLM.md` | Root handoff pointer. |
| `PROGRESS.md` | Unit/project states and evidence. |
| `PROJECTS.md` | Milestone project catalog. |
| `PYTHON_REFERENCES.md` | Exact cross-repository Python links. |
| `README.md` | Repository overview. |
| `SOLID_DESIGN_REFERENCES.md` | Verified canonical SOLID/design recall map for distributed-service units. |
| `START_HERE.md` | Simple bootstrap and daily workflow. |
| `compose.yaml` | Profile-based local infrastructure. |
| `pyproject.toml` | Dependencies and tool configuration. |
| `uv.lock` | Resolved package record. |
| `data/toolchain.json` | Machine-readable verified versions. |
| `data/msv_extension.json` | Machine-readable append-only baseline and MSV extension identity. |
| `docs/COPYRIGHT_AND_LICENSE.md` | Public-repository rights policy. |
| `docs/NOTEBOOKLM.md` | NotebookLM workflow. |
| `docs/SOURCE_AND_VERSION_POLICY.md` | Sources and version rules. |
| `docs/TOOLCHAIN_AND_INFRASTRUCTURE.md` | Package and Compose setup. |
| `docs/WORKFLOW.md` | Detailed Git/Worktree/learning procedures. |
| `templates/experiment.md` | Runtime experiment structure. |
| `templates/mock_interview.md` | Mock interview record. |
| `templates/practice.md` | Protected unsolved practice structure. |
| `templates/project.md` | Milestone project structure. |
| `templates/review.md` | Closed-book and delayed review. |
| `templates/unit.md` | Canonical unit-note structure. |
| `scripts/validate_repo.py` | Standard-library repository, live, archive, and report validator. |


## Extension summary

- Original prefix: 129 canonical units, preserved byte-for-byte at the unit-row level.
- Appended: 27 `FAPI-MSV-...` units, 3 distinct prerequisite-safe learning paths, 2 projects, RabbitMQ group/profile, and topic-specific Python/SOLID reference guidance.
- Just-in-time rule: no generated `units/` or `projects/` directory is included.

## Baseline-versus-final changed-file manifest

Compared with the verified `1adc52162b1a...` baseline archive:

- Added paths: **2**
- Modified paths: **26**
- Removed paths: **0**

### Added

- `SOLID_DESIGN_REFERENCES.md`
- `data/msv_extension.json`

### Modified

- `.env.example`
- `AGENTS.md`
- `API_DESIGN_PLAYBOOK.md`
- `BUNDLE_MANIFEST.md`
- `CURRICULUM.md`
- `INTERVIEW_PLAYBOOK.md`
- `LEARNING_PATHS.md`
- `PROGRESS.md`
- `PROJECTS.md`
- `PYTHON_REFERENCES.md`
- `README.md`
- `START_HERE.md`
- `compose.yaml`
- `data/toolchain.json`
- `docs/SOURCE_AND_VERSION_POLICY.md`
- `docs/TOOLCHAIN_AND_INFRASTRUCTURE.md`
- `docs/WORKFLOW.md`
- `pyproject.toml`
- `scripts/validate_repo.py`
- `templates/experiment.md`
- `templates/mock_interview.md`
- `templates/practice.md`
- `templates/project.md`
- `templates/review.md`
- `templates/unit.md`
- `uv.lock`

### Removed

- None
