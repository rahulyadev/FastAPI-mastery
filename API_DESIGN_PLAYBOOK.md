# API design playbook

Use this playbook while designing or reviewing HTTP and alternative API contracts. It is a decision aid, not a replacement for the owning curriculum units.

## Start with the contract

1. Identify actors, resources, actions, trust boundaries, and consistency needs.
2. Decide whether the interaction is resource-oriented HTTP, an explicit command, streaming, callback, broker event, GraphQL, or gRPC.
3. Define success, error, retry, idempotency, authorization, and observability behavior before implementation details.
4. Keep transport validation, business rules, database constraints, and authorization distinct.

## Resource and action checklist

- Stable resource identity and ownership.
- Method safety and idempotency are intentional.
- Status codes reflect transport outcome rather than business marketing language.
- Path identifies a resource or stable action boundary; query modifies retrieval.
- Partial update semantics are explicit.
- Retry behavior and idempotency keys are documented for commands.
- Pagination order is deterministic.
- Filtering and sorting fields are bounded and indexed where needed.
- Error responses are stable, machine-readable, and do not expose private internals.

## Boundary comparisons

| Choice | Prefer when | Avoid when |
|---|---|---|
| Dependency | Request-scoped input/resource composition | Cross-cutting response wrapping or proxy concerns |
| Middleware | Every request needs transport-level behavior | Business logic or route-specific authorization |
| Exception handler | Translating known failures into HTTP contracts | Recovering from arbitrary corruption |
| Service layer | Orchestration and transactions outgrow path operations | A tiny CRUD endpoint has no meaningful orchestration |
| Repository | Domain/test boundaries need a stable collection contract | It only renames SQLAlchemy methods |
| WebSocket | Bidirectional, low-latency, long-lived interaction | One-way updates or simple polling suffice |
| SSE | One-way browser updates with reconnect semantics | Bidirectional protocol is required |
| gRPC | Typed service-to-service contracts and streaming justify codegen | Browser-first, public, simple HTTP APIs are enough |

## Review questions

- Which layer owns this behavior?
- What happens on duplicate delivery, retry, timeout, cancellation, or disconnect?
- Where is transaction ownership?
- Which data is untrusted, and when is authorization checked?
- What is the maximum body, response, queue, pool, and concurrency size?
- Can the contract evolve without breaking clients?
- What evidence would falsify the performance assumption?

## Distributed communication selection

Do not call REST, gRPC, RabbitMQ, WebSockets, SSE, and Kafka interchangeable request types. Record whether the mechanism is an architectural style, RPC framework, broker model, event log, persistent transport, callback pattern, or polling strategy. Compare temporal coupling, contract strictness, browser compatibility, latency, fan-out, ordering, delivery, replay, backpressure, failure visibility, ownership, and operational cost before selecting it.
