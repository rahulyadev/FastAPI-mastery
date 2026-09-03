# Milestone projects

Projects integrate units but do not automatically advance unit learning states. Initialize one project per dedicated Worktree chat with `Initialize project <PROJECT-ID>.`

## Overview

| Project ID | Project | Main integration |
|---|---|---|
| [`FAPI-PRJ-010`](#fapi-prj-010) | First typed CRUD API | minimal app, request/response validation, error contracts, OpenAPI, route tests |
| [`FAPI-PRJ-020`](#fapi-prj-020) | PostgreSQL catalog and ordering service | PostgreSQL, SQLAlchemy, transactions, Alembic, pagination, N+1 diagnosis |
| [`FAPI-PRJ-030`](#fapi-prj-030) | Authenticated multi-tenant service | authentication, RBAC/ABAC, object authorization, tenant isolation, audit |
| [`FAPI-PRJ-040`](#fapi-prj-040) | Synthetic review and workflow platform | workflow state, nested resources, authorization, transactions, idempotency, notifications |
| [`FAPI-PRJ-050`](#fapi-prj-050) | File-processing and durable-job service | uploads, RabbitMQ, retries, idempotency, backpressure, security |
| [`FAPI-PRJ-060`](#fapi-prj-060) | Real-time operations dashboard | SSE, WebSockets, Redis pub/sub, backpressure, observability |
| [`FAPI-PRJ-070`](#fapi-prj-070) | REST-to-gRPC gateway | REST, gRPC, Protobuf, deadline propagation, gateway translation |
| [`FAPI-PRJ-080`](#fapi-prj-080) | Production modular backend capstone | architecture, security, database, migrations, async, observability, deployment, incident response |
| [`FAPI-PRJ-090`](#fapi-prj-090) | Reliable RabbitMQ workflow service | FastAPI command endpoint, PostgreSQL outbox/inbox, RabbitMQ correctness, worker reliability, observability |
| [`FAPI-PRJ-100`](#fapi-prj-100) | Microservices production capstone | evolutionary extraction, owned data, REST, gRPC, RabbitMQ, saga, security, tracing, rollout, incident response |

<a id="fapi-prj-010"></a>
## FAPI-PRJ-010 — First typed CRUD API

**Purpose:** Build a minimal but complete typed CRUD API, then let concrete change pressure justify routers, dependencies, and explicit error contracts.

**Required prerequisites:** `FAPI-FND-040`, `FAPI-HTTP-050`, `FAPI-PYD-020`, `FAPI-APP-060`, `FAPI-TST-020`

**Recommended prerequisites:** `FAPI-APP-080`, `FAPI-DEP-010`

**Integrated concepts:** minimal app, request/response validation, error contracts, OpenAPI, route tests

### Staged change pressure

1. Implement an in-memory item API in one file with create, read, list, update, and delete operations.
2. Add duplicate-name rejection, partial updates, pagination, and a stable problem-detail error contract.
3. Split routes and application logic only after the one-file change pressure is visible.
4. Add an injected clock and ID generator so tests are deterministic without global monkey patching.
5. Add OpenAPI contract checks and a backward-compatible response evolution.

### Governing invariants

- Every stored item has one stable identifier.
- A successful response always satisfies its declared response model.
- The API never returns an internal exception shape.

### Seeded defects

- A PATCH endpoint replaces omitted fields with null values.
- A route-order conflict causes `/items/search` to be parsed as an item ID.

### Adversarial tests and evidence

- Route tests for success, duplicate creation, not-found, partial update, pagination, and OpenAPI.
- A property-based test for round-tripping valid create payloads through the response model.

### Refactoring checkpoint

Preserve observable contracts while moving only the boundary justified by the next stage. Record the before/after dependency direction, transaction ownership, and failure ownership.

### Rejected alternatives

- A repository interface before any persistence boundary exists.
- A generic base CRUD service that hides item-specific rules.

### Operational exercise

Run under Uvicorn, inspect generated OpenAPI, and demonstrate graceful startup/shutdown with no external infrastructure.

### Required visuals

- one architecture/topology visual;
- one request, transaction, job, stream, or protocol sequence visual;
- each visual includes how to read it, the key insight, and its simplification.

### Definition of done

- [ ] Every staged requirement is implemented and tested.
- [ ] Seeded defects are diagnosed before fixes are shown.
- [ ] Invariants and failure ownership are explained.
- [ ] Security and abuse cases are reviewed.
- [ ] Performance claims record environment, workload, and limitations.
- [ ] The operational exercise is reproducible on disposable synthetic data.
- [ ] Rejected alternatives and one future change are defended.
- [ ] A senior interview walkthrough is completed.
- [ ] No project result silently changes unit learning states.

<a id="fapi-prj-020"></a>
## FAPI-PRJ-020 — PostgreSQL catalog and ordering service

**Purpose:** Build a transactional catalog and order service that makes SQLAlchemy session ownership, migration review, query shape, and concurrency visible.

**Required prerequisites:** `FAPI-DB-090`, `FAPI-MIG-030`, `FAPI-TST-050`, `FAPI-ARC-030`

**Recommended prerequisites:** `FAPI-DB-100`, `FAPI-MIG-040`

**Integrated concepts:** PostgreSQL, SQLAlchemy, transactions, Alembic, pagination, N+1 diagnosis

### Staged change pressure

1. Create products and inventory with reviewed constraints and an initial Alembic migration.
2. Add orders with line items and one explicit transaction boundary that reserves inventory atomically.
3. Add stable keyset pagination, filtering, sorting, and aggregate order totals.
4. Introduce concurrent order placement to expose lost updates and choose locking or optimistic versioning.
5. Add a nullable column, backfill, and later non-null constraint through an expand-and-contract sequence.

### Governing invariants

- Committed inventory never becomes negative.
- An order and its line items commit or roll back together.
- List ordering is stable across pages.

### Seeded defects

- A commit inside a repository breaks atomic order creation.
- Lazy relationship access in async code triggers unexpected I/O or a missing-greenlet failure.

### Adversarial tests and evidence

- PostgreSQL integration tests with transaction isolation and real constraints.
- Migration tests from an empty database and from the previous revision.
- Query-count assertion exposing and then fixing an N+1 path.

### Refactoring checkpoint

Preserve observable contracts while moving only the boundary justified by the next stage. Record the before/after dependency direction, transaction ownership, and failure ownership.

### Rejected alternatives

- Using Pydantic models as SQLAlchemy persistence models.
- Offset pagination for a high-churn ordered feed without acknowledging inconsistency.

### Operational exercise

Inspect EXPLAIN output, pool checkout behavior, deadlock/retry logs, and migration lock duration on disposable local data.

### Required visuals

- one architecture/topology visual;
- one request, transaction, job, stream, or protocol sequence visual;
- each visual includes how to read it, the key insight, and its simplification.

### Definition of done

- [ ] Every staged requirement is implemented and tested.
- [ ] Seeded defects are diagnosed before fixes are shown.
- [ ] Invariants and failure ownership are explained.
- [ ] Security and abuse cases are reviewed.
- [ ] Performance claims record environment, workload, and limitations.
- [ ] The operational exercise is reproducible on disposable synthetic data.
- [ ] Rejected alternatives and one future change are defended.
- [ ] A senior interview walkthrough is completed.
- [ ] No project result silently changes unit learning states.

<a id="fapi-prj-030"></a>
## FAPI-PRJ-030 — Authenticated multi-tenant service

**Purpose:** Build a service where identity, tenant selection, object-level authorization, audit events, and token/session choices are explicit security boundaries.

**Required prerequisites:** `FAPI-SEC-060`, `FAPI-SEC-090`, `FAPI-TST-030`, `FAPI-DB-110`

**Recommended prerequisites:** `FAPI-SEC-050`, `FAPI-OPS-050`

**Integrated concepts:** authentication, RBAC/ABAC, object authorization, tenant isolation, audit

### Staged change pressure

1. Start with one authenticated profile endpoint backed by an external identity claim.
2. Add organizations, memberships, roles, and tenant-scoped resources.
3. Add object-level authorization so resource ownership and role permissions are both checked.
4. Add refresh-token rotation or secure-session handling with revocation and replay analysis.
5. Add immutable audit events and tests proving cross-tenant access cannot occur.

### Governing invariants

- Every tenant-owned query includes a trusted tenant boundary.
- Authentication establishes identity; authorization is evaluated separately for each action.
- Audit records contain no token or sensitive payload data.

### Seeded defects

- A client-supplied tenant ID overrides the trusted tenant claim.
- An admin-list endpoint checks route access but omits object-level filtering.

### Adversarial tests and evidence

- Authentication failure, expired token, wrong audience, revoked refresh, RBAC, ABAC, and cross-tenant denial tests.
- A property-based test that generated users cannot access resources outside their memberships.

### Refactoring checkpoint

Preserve observable contracts while moving only the boundary justified by the next stage. Record the before/after dependency direction, transaction ownership, and failure ownership.

### Rejected alternatives

- Treating a decoded JWT as sufficient authorization.
- Putting all authorization logic in one middleware without resource context.

### Operational exercise

Rotate a signing key in a controlled exercise, inspect redacted audit logs, and document proxy/TLS trust assumptions.

### Required visuals

- one architecture/topology visual;
- one request, transaction, job, stream, or protocol sequence visual;
- each visual includes how to read it, the key insight, and its simplification.

### Definition of done

- [ ] Every staged requirement is implemented and tested.
- [ ] Seeded defects are diagnosed before fixes are shown.
- [ ] Invariants and failure ownership are explained.
- [ ] Security and abuse cases are reviewed.
- [ ] Performance claims record environment, workload, and limitations.
- [ ] The operational exercise is reproducible on disposable synthetic data.
- [ ] Rejected alternatives and one future change are defended.
- [ ] A senior interview walkthrough is completed.
- [ ] No project result silently changes unit learning states.

<a id="fapi-prj-040"></a>
## FAPI-PRJ-040 — Synthetic review and workflow platform

**Purpose:** Build a synthetic enterprise workflow with nested review data, explicit state transitions, transaction ownership, roles, idempotency, audit, and notifications.

**Required prerequisites:** `FAPI-ARC-050`, `FAPI-DB-120`, `FAPI-MIG-070`, `FAPI-SEC-060`, `FAPI-ASY-040`

**Recommended prerequisites:** `FAPI-RT-030`, `FAPI-OPS-050`

**Integrated concepts:** workflow state, nested resources, authorization, transactions, idempotency, notifications

### Staged change pressure

1. Create reviews, sections, criteria, assignments, and role-scoped list/detail endpoints.
2. Add a state machine for draft, submitted, validating, returned, and closed states with explicit transition rules.
3. Add nested partial updates and optimistic concurrency to prevent silent overwrites.
4. Add idempotent submit/close commands and an outbox-backed notification boundary.
5. Add audit history, filters, pagination, SSE status updates, and a zero-downtime schema change.

### Governing invariants

- Only declared state transitions are legal.
- A workflow transition and its audit/outbox records are atomic.
- Authorization is evaluated against both role and review assignment.

### Seeded defects

- Two validators overwrite each other because no version precondition is checked.
- A notification is sent before commit and reports a transition that later rolls back.

### Adversarial tests and evidence

- Transition-table tests, permission matrix tests, idempotency replay tests, transaction rollback tests, and migration compatibility tests.
- A concurrent update test proving stale versions receive a conflict response.

### Refactoring checkpoint

Preserve observable contracts while moving only the boundary justified by the next stage. Record the before/after dependency direction, transaction ownership, and failure ownership.

### Rejected alternatives

- Encoding state transitions as scattered endpoint if/elif blocks.
- Leaking SQLAlchemy models directly as the public API contract.

### Operational exercise

Trace one transition across request ID, database transaction, outbox event, notification worker, and SSE client using only synthetic records.

### Required visuals

- one architecture/topology visual;
- one request, transaction, job, stream, or protocol sequence visual;
- each visual includes how to read it, the key insight, and its simplification.

### Definition of done

- [ ] Every staged requirement is implemented and tested.
- [ ] Seeded defects are diagnosed before fixes are shown.
- [ ] Invariants and failure ownership are explained.
- [ ] Security and abuse cases are reviewed.
- [ ] Performance claims record environment, workload, and limitations.
- [ ] The operational exercise is reproducible on disposable synthetic data.
- [ ] Rejected alternatives and one future change are defended.
- [ ] A senior interview walkthrough is completed.
- [ ] No project result silently changes unit learning states.

<a id="fapi-prj-050"></a>
## FAPI-PRJ-050 — File-processing and durable-job service

**Purpose:** Build a safe upload and processing API that moves work to a durable broker, survives retries, and exposes truthful job state without trusting file names or payloads.

**Required prerequisites:** `FAPI-APP-050`, `FAPI-ASY-050`, `FAPI-SEC-080`, `FAPI-TST-080`

**Recommended prerequisites:** `FAPI-RT-030`, `FAPI-OPS-060`

**Integrated concepts:** uploads, RabbitMQ, retries, idempotency, backpressure, security

### Staged change pressure

1. Accept bounded uploads with streamed storage, content inspection, and safe synthetic metadata.
2. Create a durable job record and publish work through a RabbitMQ boundary after the database commit.
3. Add retry classification, deduplication, idempotency keys, cancellation requests, and a dead-letter path.
4. Expose status polling plus optional SSE progress without holding the upload request open.
5. Inject broker outage, worker crash, duplicate delivery, malformed file, and storage failure.

### Governing invariants

- A job is processed at least once but externally visible effects remain idempotent.
- Untrusted file names never determine storage paths.
- Queue admission and upload limits keep memory and disk use bounded.

### Seeded defects

- The broker message is published before the job transaction commits.
- A retry creates duplicate output because the handler has no idempotency record.

### Adversarial tests and evidence

- Upload-size, content-type, traversal, duplicate delivery, retry, cancellation, timeout, and broker-failure tests.
- A differential test comparing the worker result with a synchronous reference processor on small inputs.

### Refactoring checkpoint

Preserve observable contracts while moving only the boundary justified by the next stage. Record the before/after dependency direction, transaction ownership, and failure ownership.

### Rejected alternatives

- FastAPI BackgroundTasks for durable multi-minute work.
- Loading every upload into memory before validation.

### Operational exercise

Observe queue depth, retry counts, processing latency, disk use, and dead-letter messages under a bounded local load.

### Required visuals

- one architecture/topology visual;
- one request, transaction, job, stream, or protocol sequence visual;
- each visual includes how to read it, the key insight, and its simplification.

### Definition of done

- [ ] Every staged requirement is implemented and tested.
- [ ] Seeded defects are diagnosed before fixes are shown.
- [ ] Invariants and failure ownership are explained.
- [ ] Security and abuse cases are reviewed.
- [ ] Performance claims record environment, workload, and limitations.
- [ ] The operational exercise is reproducible on disposable synthetic data.
- [ ] Rejected alternatives and one future change are defended.
- [ ] A senior interview walkthrough is completed.
- [ ] No project result silently changes unit learning states.

<a id="fapi-prj-060"></a>
## FAPI-PRJ-060 — Real-time operations dashboard

**Purpose:** Build an optional browser-visible operations feed using SSE and WebSockets while making connection lifetime, backpressure, authentication, Redis fan-out, and shutdown observable.

**Required prerequisites:** `FAPI-RT-050`, `FAPI-RT-030`, `FAPI-ASY-080`, `FAPI-TST-070`

**Recommended prerequisites:** `FAPI-MID-020`, `FAPI-OPS-050`

**Integrated concepts:** SSE, WebSockets, Redis pub/sub, backpressure, observability

### Staged change pressure

1. Expose one bounded SSE feed with event IDs, heartbeat comments, and reconnect support.
2. Add a WebSocket command/acknowledgement channel with authentication at connect time and per-message authorization.
3. Add bounded per-client queues and a slow-consumer policy.
4. Use Redis pub/sub for multi-process fan-out while preserving local connection ownership.
5. Add an optional tiny static visual client and perform disconnect, proxy-buffering, and graceful-shutdown drills.

### Governing invariants

- Each connection has one owner and bounded pending output.
- A disconnected client is removed exactly once.
- Cross-process pub/sub never substitutes for per-client authorization.

### Seeded defects

- A slow client grows an unbounded queue.
- A connection manager stored in process memory is incorrectly assumed to broadcast across workers.

### Adversarial tests and evidence

- SSE framing/reconnect tests, WebSocket auth/disconnect tests, slow-consumer tests, and multi-instance fan-out integration tests.
- A cancellation test that proves cleanup runs after the client disconnects.

### Refactoring checkpoint

Preserve observable contracts while moving only the boundary justified by the next stage. Record the before/after dependency direction, transaction ownership, and failure ownership.

### Rejected alternatives

- WebSockets for one-way low-frequency updates that SSE can handle.
- A React application when a static client is enough to expose protocol behavior.

### Operational exercise

Inspect active connections, queue depth, disconnect reasons, Redis health, proxy buffering, and graceful drain during deployment.

### Required visuals

- one architecture/topology visual;
- one request, transaction, job, stream, or protocol sequence visual;
- each visual includes how to read it, the key insight, and its simplification.

### Definition of done

- [ ] Every staged requirement is implemented and tested.
- [ ] Seeded defects are diagnosed before fixes are shown.
- [ ] Invariants and failure ownership are explained.
- [ ] Security and abuse cases are reviewed.
- [ ] Performance claims record environment, workload, and limitations.
- [ ] The operational exercise is reproducible on disposable synthetic data.
- [ ] Rejected alternatives and one future change are defended.
- [ ] A senior interview walkthrough is completed.
- [ ] No project result silently changes unit learning states.

<a id="fapi-prj-070"></a>
## FAPI-PRJ-070 — REST-to-gRPC gateway

**Purpose:** Run FastAPI and gRPC side by side with explicit contract translation, deadlines, cancellation, status mapping, authentication metadata, and schema-evolution tests.

**Required prerequisites:** `FAPI-RT-090`, `FAPI-TST-070`, `FAPI-ARC-050`

**Recommended prerequisites:** `FAPI-OPS-030`, `FAPI-OPS-050`

**Integrated concepts:** REST, gRPC, Protobuf, deadline propagation, gateway translation

### Staged change pressure

1. Define a small versioned Protobuf service and generate synchronous and asynchronous Python stubs.
2. Expose a REST resource that calls one unary gRPC operation and maps status codes deliberately.
3. Add server streaming with an HTTP streaming or SSE gateway.
4. Propagate deadlines, cancellation, request IDs, identity metadata, and trace context.
5. Evolve the schema compatibly and test old/new clients against the service.

### Governing invariants

- The gateway never converts a deadline into an unbounded call.
- Protobuf field numbers are never reused.
- REST and gRPC error contracts preserve meaningful semantics without pretending they are identical.

### Seeded defects

- The REST timeout fires but the downstream gRPC call continues.
- A removed Protobuf field number is reused and corrupts compatibility.

### Adversarial tests and evidence

- Unary, streaming, deadline, cancellation, metadata, status-mapping, and compatibility tests.
- Contract tests comparing gateway JSON with canonical gRPC responses for representative cases.

### Refactoring checkpoint

Preserve observable contracts while moving only the boundary justified by the next stage. Record the before/after dependency direction, transaction ownership, and failure ownership.

### Rejected alternatives

- Using gRPC for a public browser API with no operational need.
- Sharing generated transport messages directly as domain models.

### Operational exercise

Run FastAPI and gRPC as side-by-side processes, inspect reflection, health, deadline metrics, and proxy/load-balancer boundaries.

### Required visuals

- one architecture/topology visual;
- one request, transaction, job, stream, or protocol sequence visual;
- each visual includes how to read it, the key insight, and its simplification.

### Definition of done

- [ ] Every staged requirement is implemented and tested.
- [ ] Seeded defects are diagnosed before fixes are shown.
- [ ] Invariants and failure ownership are explained.
- [ ] Security and abuse cases are reviewed.
- [ ] Performance claims record environment, workload, and limitations.
- [ ] The operational exercise is reproducible on disposable synthetic data.
- [ ] Rejected alternatives and one future change are defended.
- [ ] A senior interview walkthrough is completed.
- [ ] No project result silently changes unit learning states.

<a id="fapi-prj-080"></a>
## FAPI-PRJ-080 — Production modular backend capstone

**Purpose:** Harden a modular FastAPI service through production-like change, security review, capacity constraints, observability, deployment, and incident response.

**Required prerequisites:** `FAPI-SYN-050`

**Recommended prerequisites:** None

**Integrated concepts:** architecture, security, database, migrations, async, observability, deployment, incident response

### Staged change pressure

1. Select one earlier service and establish an observable baseline with architecture and request-lifecycle diagrams.
2. Introduce a second feature slice and resolve transaction, package, and dependency boundaries without pattern ceremony.
3. Add authentication/authorization, a reviewed schema evolution, durable work, and one real-time or streaming boundary.
4. Set worker, connection-pool, queue, request-size, timeout, and retry budgets from a measured workload.
5. Deploy behind a local reverse proxy, inject database/broker/downstream failures, and execute a rollback or recovery drill.
6. Conduct a final code review and senior design interview covering rejected alternatives and future scaling paths.

### Governing invariants

- Every resource has one explicit lifetime and cleanup owner.
- No request can commit partial domain state across the declared transaction boundary.
- Capacity limits compose without allowing workers, pools, or queues to amplify overload.

### Seeded defects

- Worker count exceeds available database connections and causes pool starvation.
- Proxy trust is misconfigured, allowing spoofed client or scheme information.
- A migration and application release are incompatible during rolling deployment.

### Adversarial tests and evidence

- Full contract, migration, authorization, failure-injection, graceful-shutdown, and performance-budget suites.
- A smoke test through the reverse proxy and a restore/recovery verification using disposable synthetic data.

### Refactoring checkpoint

Preserve observable contracts while moving only the boundary justified by the next stage. Record the before/after dependency direction, transaction ownership, and failure ownership.

### Rejected alternatives

- Splitting the service into microservices before independent deployment pressure exists.
- Adding repositories, buses, and adapters that have no alternative implementation or test seam.

### Operational exercise

Produce runbooks, dashboards, alerts, capacity assumptions, an incident timeline, and a reproducible deployment/rollback exercise.

### Required visuals

- one architecture/topology visual;
- one request, transaction, job, stream, or protocol sequence visual;
- each visual includes how to read it, the key insight, and its simplification.

### Definition of done

- [ ] Every staged requirement is implemented and tested.
- [ ] Seeded defects are diagnosed before fixes are shown.
- [ ] Invariants and failure ownership are explained.
- [ ] Security and abuse cases are reviewed.
- [ ] Performance claims record environment, workload, and limitations.
- [ ] The operational exercise is reproducible on disposable synthetic data.
- [ ] Rejected alternatives and one future change are defended.
- [ ] A senior interview walkthrough is completed.
- [ ] No project result silently changes unit learning states.

<a id="fapi-prj-090"></a>
## FAPI-PRJ-090 — Reliable RabbitMQ workflow service

**Purpose:** Build a production-shaped command and worker workflow that makes every database/broker failure window observable and repairable.

**Required prerequisites:** `FAPI-MSV-090`, `FAPI-MSV-110`, `FAPI-MSV-120`, `FAPI-MSV-210`, `FAPI-MSV-230`

**Recommended prerequisites:** `FAPI-MSV-180`, `FAPI-MSV-220`, `FAPI-MSV-240`

**Integrated concepts:** FastAPI command endpoint, PostgreSQL job/order state, transactional outbox, RabbitMQ publisher confirms and mandatory returns, declared topology, separate worker process, manual acknowledgements, prefetch, bounded retries, DLQ, inbox/idempotent consumer, duplicate handling, tracing, metrics, draining, redrive, and incident response.

### Staged change pressure

1. Accept a command and commit the domain record plus outbox row atomically.
2. Add a relay that claims outbox rows, publishes with confirms, records uncertain outcomes, and retries without losing or duplicating domain intent.
3. Add a worker with manual acknowledgements, bounded prefetch, an inbox/deduplication boundary, and observable job state.
4. Introduce transient and permanent failures, bounded retry topology, DLQ parking, operator redrive, and no infinite requeue.
5. Add trace propagation, queue-delay metrics, consumer-capacity/backlog signals, graceful draining, and an incident runbook.

### Governing invariants

- A committed command eventually has either a published outbox record or an explicit operator-visible failure state.
- Publisher confirms prove broker acceptance; they do not prove consumer completion.
- A consumer acknowledgement occurs only after the idempotent business side effect and inbox record are durably committed.
- Redelivery may repeat delivery but must not repeat the externally visible effect.
- Retry count is bounded and poison messages become operable records, not infinite traffic.

### Seeded defects

- Kill the relay after the broker confirms but before the outbox row is marked sent.
- Kill the consumer after the side effect commits but before acknowledgement.
- Publish with an unroutable key while `mandatory` is enabled.
- Create a poison payload that fails deterministically and verify DLQ routing and alerting.
- Exhaust the consumer database pool while backlog rises.

### Adversarial tests and evidence

- Characterization test for command idempotency.
- Real PostgreSQL and RabbitMQ topology/integration tests.
- Duplicate-delivery and crash-window tests using an externally observable effect counter.
- Retry/DLQ tests that inspect broker metadata and bounded attempts.
- A differential oracle comparing accepted commands with terminal job states and unapplied inbox/outbox records.

### Required visuals

- command → transaction → outbox → confirm → worker → inbox → acknowledgement sequence;
- failure window and redelivery trace;
- queue, exchange, routing, retry, and DLQ topology;
- each visual includes how to read it, the key insight, and the simplification.

### Refactoring checkpoint

Move broker-specific code behind a narrow application port only after the failure semantics are understood. Preserve the broker-visible behavior and crash-window tests while reducing framework coupling.

### Rejected alternatives

Reject dual writes, acknowledgement-before-commit, infinite requeue, one connection per message, and a generic event bus that hides confirms and routing.

### Security and observability review

Use a dedicated local vhost and least-privilege user, propagate trace context without leaking sensitive baggage, and expose publisher failures, queue delay, backlog, redelivery, DLQ depth, idempotency conflicts, and terminal workflow state. This observability is part of the failure injection evidence.

### Operational exercise

Start the named RabbitMQ profile, inspect topology and rates, generate backlog, drain safely, park poison messages, redrive one explicitly named local queue, and follow the runbook without broad destructive commands.

### Definition of done

- [ ] Every failure window has a reproducible test and observable state.
- [ ] Confirms, mandatory returns, manual acknowledgements, prefetch, retries, DLQ, outbox, and inbox are demonstrated.
- [ ] Duplicate delivery changes no externally visible result.
- [ ] Metrics expose publish failures, queue delay, backlog, redelivery, DLQ, and terminal failures.
- [ ] Shutdown drains bounded in-flight work and documents leftovers.
- [ ] Redrive and incident procedures are safe and explicit.
- [ ] A senior walkthrough defends RabbitMQ versus database jobs, managed queues, and event logs.
- [ ] Project evidence does not automatically advance unit learning states.


<a id="fapi-prj-100"></a>
## FAPI-PRJ-100 — Microservices production capstone

**Purpose:** Evolve a synthetic modular monolith into only three or four independently useful services and prove that every new boundary earns its operational cost.

**Required prerequisites:** `FAPI-MSV-270`, `FAPI-MSV-230`, `FAPI-MSV-240`, `FAPI-MSV-250`, `FAPI-SEC-100`

**Recommended prerequisites:** `FAPI-PRJ-090`, `FAPI-OPS-070`

**Integrated concepts:** public FastAPI gateway, owned PostgreSQL data, REST, gRPC, RabbitMQ commands/events, outbox/inbox, one saga, identity and authorization, schema evolution, tracing, metrics, logs, contract tests, fault injection, compatible rollout, ADRs, migration from a modular monolith, and incident response.

### Starting point and service limits

Begin with one modular monolith containing synthetic workflow, notification, and reporting capabilities. Extract no more than four services. Every extraction requires a written independent-deployment pressure, owner, data boundary, contract, reliability budget, and rollback plan.

### Staged change pressure

1. Record baseline monolith latency, change coupling, deployment frequency, and incident ownership.
2. Extract one service through a strangler route while preserving a compatibility window.
3. Use REST for one user-facing synchronous interaction, gRPC for one internal strict low-latency query, and RabbitMQ for one durable command/event workflow; justify each.
4. Move owned data without shared-table writes; introduce read models or composition for cross-service views.
5. Add an outbox/inbox boundary and one saga with compensation and manual intervention.
6. Propagate identity, tenant, deadlines, cancellation, trace context, and audit information.
7. Perform compatible event, Protobuf, API, and database evolution during rolling deployment.
8. Inject dependency outage, latency, broker backlog, duplicate delivery, and partial rollout failures; run an incident and postmortem.

### Governing invariants

- No service writes another service's owned tables.
- Every synchronous hop has an end-to-end deadline budget and cancellation behavior.
- Every asynchronous side effect is duplicate-safe and observable.
- Contracts remain backward compatible during the declared rollout window.
- The saga reaches a terminal success, compensated, or operator-intervention state.
- Removing a boundary is allowed when measured value does not exceed its cost.

### Seeded defects

- A gateway retry and gRPC client retry amplify one failing dependency into an incident.
- A service writes another service's table during a compatibility window.
- An old consumer rejects a newly added event field because it is not a tolerant reader.
- A saga compensation fails after two earlier steps succeeded.
- A tenant or user identity is propagated to one transport but lost on another.

### Required visuals

- modular-monolith baseline and extracted topology;
- data ownership map;
- one synchronous REST/gRPC deadline trace;
- one RabbitMQ/outbox/inbox saga failure and compensation trace;
- one rollout compatibility timeline;
- each visual includes how to read it, key insight, and limitation.

### Adversarial tests and evidence

- HTTP and gRPC compatibility tests; message-schema tests; real PostgreSQL/RabbitMQ integration; duplicate and crash-window tests; eventual-consistency assertions; timeout/cancellation tests; latency and outage injection; rollout/backward-compatibility checks; authorization and tenant-isolation tests.

### Refactoring checkpoint

After the first extraction, compare measured deployment coupling, latency, incident load, ownership, and operating cost. Keep, reshape, or remove the boundary based on evidence; preserve contracts and migration safety while refactoring.

### Rejected alternatives

Document why each interaction is REST, gRPC, or RabbitMQ. Reject a service per entity, shared database writes, synchronous chains for durable workflows, retries at every layer, a mesh as a substitute for contracts, and a shared-library distributed monolith.

### Operational exercise

Run a bounded failure injection covering dependency outage, latency, RabbitMQ backlog, duplicate delivery, partial rollout, and one recovery or rollback limit. Use traces, metrics, logs, contract tests, and the runbook to diagnose and recover.

### Optional visual client

A small generated client may show workflow state, retries, failures, trace IDs, and an event timeline through polling, SSE, or WebSocket. It is isolated, prebuilt, optional, and not learner evidence.

### Definition of done

- [ ] Three or four meaningful services have explicit owners, contracts, and data.
- [ ] Communication choices are justified from coupling, latency, durability, replay, browser, and operations needs.
- [ ] One migration can be reversed or stopped safely without force or data loss.
- [ ] Security, observability, resilience, rollout, and incident procedures are executable.
- [ ] Fault injection produces useful alerts, traces, and runbook actions.
- [ ] Postmortem actions modify code, contract, operations, or ownership—not only documentation.
- [ ] A senior interview walkthrough covers requirements, load, boundaries, data, consistency, failures, security, observability, evolution, cost, and rejected complexity.
- [ ] Project evidence remains separate from unit learning-state changes.
