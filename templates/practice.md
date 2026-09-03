<!-- Copy to practice/README.md. Tasks begin unsolved. -->
# Practice — {{UNIT_ID}} {{UNIT_TITLE}}

## Learning question

{{PRECISE_QUESTION}}

## Initial state

Describe starter files and what already works. Do not hide a solution in comments, examples, or test names.

## Concrete unsolved tasks

### Task 1 — Predict and trace
- Given state: {{STATE}}
- Write the expected lifecycle or output before running anything.
- Explain the governing rule.

### Task 2 — Implement
- Required observable behavior: {{BEHAVIOR}}
- Constraints: {{CONSTRAINTS}}
- Files allowed to change: {{FILES}}

### Task 3 — Debug and vary
- Diagnose the seeded failure.
- Preserve the external contract.
- Adapt to the changed requirement: {{VARIATION}}

## Acceptance criteria

- [ ] Scaffold examples pass.
- [ ] Learner challenge is implemented without a revealed solution.
- [ ] Edge and failure cases are tested.
- [ ] Lifecycle, security, transaction, and performance reasoning are explained where relevant.

## Commands

```bash
uv run --group dev python -m compileall -q .
uv run --group dev python -m pytest -q practice/test_examples.py
uv run --group dev python -m pytest --collect-only -q practice/test_challenge.py
```

Do not execute intentionally incomplete challenge tests and report them as passing.

## Troubleshooting

## Progressive hints

Add one hint only after a meaningful attempt. Start with the smallest missing reasoning step.

## Reflection questions

## Attempt and review record

Preserve Rahul’s original code and reasoning. Add a comparison solution only after the exercise is explicitly closed.

## Distributed-service practice, when applicable

Use `predict → run → observe → explain → implement → fail deliberately → repair → vary → operate`. Include one bounded failure injection, observable recovery evidence, and safe local operating commands. Do not expose complete solutions.
