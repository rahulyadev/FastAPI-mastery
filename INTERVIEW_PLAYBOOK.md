# FastAPI interview playbook

Do not memorize scripts. Use a repeatable reasoning flow.

## Answer flow

1. Define the concept in plain language.
2. Name the owning layer: HTTP, ASGI, server, Starlette, FastAPI, Pydantic, SQLAlchemy, PostgreSQL, Alembic, proxy, or application.
3. Trace one concrete request or lifecycle.
4. Show the smallest implementation.
5. State failure modes and cleanup.
6. Compare plausible alternatives.
7. Discuss testing, security, and performance.
8. Adapt to a changed requirement.

## High-value explanations

- What FastAPI adds above Starlette and Pydantic.
- Complete request lifecycle and failure branches.
- Why input validation commonly returns 422 and how error customization changes the contract.
- `def` versus `async def` and blocking work inside async endpoints.
- Dependency DAG resolution, per-request caching, and yield teardown.
- Middleware order and why body consumption is dangerous.
- Session-per-request and transaction ownership.
- `flush` versus `commit`, identity maps, expiration, and rollback.
- Async SQLAlchemy implicit I/O and N+1 behavior.
- Pydantic coercion versus strict validation and response-model validation.
- JWT demonstrations versus production authentication systems.
- Scaling WebSockets and handling slow clients.
- BackgroundTasks versus durable jobs.
- Alembic autogenerate limitations and zero-downtime changes.
- Worker, process, and database-pool sizing.
- REST versus SSE, WebSockets, webhooks, brokers, and gRPC.

## Mock protocol

Codex asks one question at a time, waits, identifies the exact missing reasoning step, gives the smallest hint, and lets Rahul recover. Score separately:

| Dimension | Evidence |
|---|---|
| Concept | Accurate boundary and mental model |
| Lifecycle | Correct order, state, failure, and cleanup |
| Implementation | Simple, idiomatic, testable Python |
| Database | Transaction and query ownership |
| Security | Trust and authorization boundaries |
| Reliability | Timeout, retry, idempotency, cancellation |
| Performance | Measurement-led reasoning |
| Communication | Clear assumptions, alternatives, and trade-offs |

## Microservices and distributed-systems round

Explain designs in this order: clarify functional/non-functional requirements; estimate load; choose monolith or service boundary; assign data ownership; select synchronous/asynchronous interactions; define contracts; state consistency; enumerate failure modes; add deadlines, retries, idempotency, and backpressure; cover security and observability; explain deployment/evolution; assign operational ownership; reject unnecessary complexity; adapt to changed requirements.

Score requirement discovery, boundary quality, protocol selection, data ownership, consistency, failure handling, security, observability, scalability, operability, migration strategy, and communication independently. Ask one question at a time and reveal only the smallest useful hint.
