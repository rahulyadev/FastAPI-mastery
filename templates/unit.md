<!-- Copy to units/{{DOMAIN_SLUG}}/{{UNIT_ID}}-{{UNIT_SLUG}}/README.md. Remove non-applicable sections; never leave filler. -->
# {{UNIT_ID}} — {{UNIT_TITLE}}

## Physical Notebook Core

### Problem or pressure
{{CONCISE_PROBLEM}}

### One-sentence mental model
> {{MENTAL_MODEL}}

### Essential visual
```text
{{VISUAL}}
```

#### How to read this visual
{{READING_GUIDE}}

#### Key insight
{{KEY_INSIGHT}}

#### Simplification or limitation
{{LIMITATION}}

### Governing lifecycle rule or invariant
1. {{RULE_1}}
2. {{RULE_2}}

### Minimal code skeleton
```python
{{MINIMAL_SKELETON}}
```

### Common failure, comparison, and interview cues
- Failure: {{FAILURE}}
- Compare with: {{COMPARISON}}
- Recall: {{RECALL_QUESTION}}

## 1. Learning outcomes and evidence

## 2. Prerequisites and smallest bridge

## 3. Simple explanation and owning layer

## 4. Runtime or request-lifecycle trace

## 5. Detailed visual model

Every non-trivial visual includes `How to read this visual`, `Key insight`, and `Simplification or limitation`.

## 6. Worked examples

### 6.1 Minimal example
### 6.2 Traced runtime example
### 6.3 Realistic backend example
### 6.4 Failure or debugging example
### 6.5 Comparison with an alternative

Worked examples must not solve the separate learner challenge.

## 7. Formal mechanics and boundaries

Distinguish Python, HTTP/specification, ASGI, server, Starlette, FastAPI, Pydantic, SQLAlchemy, Alembic, PostgreSQL, proxy, third-party, and application behavior.

## 8. Failure modes and edge cases

## 9. Performance, resource, transaction, or security costs

## 10. Production relevance and anti-signals

## 11. Testing and debugging strategy

## 12. Practice ladder

Link to `practice/README.md`; keep the learner challenge unsolved.

## 13. Interview questions, traps, and follow-ups

Include definition, runtime trace, implementation, failure, alternatives, performance, security, testing, changed requirements, and production critique.

## 14. Explanation exercises

## 15. Experiment decision

State `Required`, `Recommended`, or `Not required`, with reason.

## 16. Python Mastery references

## 17. Authoritative sources and version notes

## 18. Open uncertainties

## 19. Distributed-service contract, when applicable

For an MSV unit include: system and data boundary; normal flow; failure flow; delivery/ordering/idempotency/consistency/deadline invariant; capacity and backpressure; security; observability signals; operating and recovery procedure; SDE-2 expectation; SDE-3 expectation; and `## Recall from SOLID and Design Patterns` using verified canonical IDs without invented remote links. Remove this section for units where it does not apply.
