# Progress and evidence

Artifact creation, learning, and project work are separate. Generated content never proves understanding.
## Artifact states

| State | Meaning |
|---|---|
| Absent | No initialized unit folder |
| Draft | Complete initial pack exists but has not yet met approval evidence |
| Approved | Canonical note and required artifacts were reviewed, source-checked, and validated |
## Learning states

```text
⬜ Not started → 🟠 Learning → 🟡 Practiced → 🔵 Recalled → 🟣 Demonstrated → 🟢 Retained
```

`★ Mastery` is exceptional and requires retained knowledge, teach-back, diagnosis, transfer, and current-version awareness.
## Evidence gates

- **Learning:** engage with the mental model and record a real question, trace, or misconception.
- **Practiced:** attempt required work before solutions, pass relevant learner tests, and explain corrections.
- **Recalled:** reconstruct after at least one day and correct critical gaps.
- **Demonstrated:** solve or adapt a new scenario, trace lifecycle, explain trade-offs, and satisfy the unit evidence profile.
- **Retained:** succeed again after spaced intervals or provide equivalent documented production/project transfer.

A failed review may lower a state. Project completion does not advance unit states automatically.
## Unit tracker

| Unit ID | Title | Priority | Artifact state | Learning state | Last evidence | Next review | Weakest point | Evidence link |
|---|---|:---:|---|---|---|---|---|---|
| `FAPI-FND-010` | Python runtime, uv project, and reproducible environment | `C` | Absent | Not started | — | — | — | — |
| `FAPI-FND-020` | Minimal FastAPI application and first route | `C` | Absent | Not started | — | — | — | — |
| `FAPI-FND-030` | Application entry points, import strings, reload, and server startup | `C` | Absent | Not started | — | — | — | — |
| `FAPI-FND-040` | Interactive documentation, OpenAPI inspection, and simple API clients | `C` | Absent | Not started | — | — | — | — |
| `FAPI-FND-050` | Configuration, environment variables, and application factories | `C` | Absent | Not started | — | — | — | — |
| `FAPI-FND-060` | Startup, import, reload, and configuration failure diagnosis | `C` | Absent | Not started | — | — | — | — |
| `FAPI-HTTP-010` | HTTP message anatomy, methods, status codes, and media types | `C` | Absent | Not started | — | — | — | — |
| `FAPI-HTTP-020` | URLs, path/query semantics, request bodies, encoding, and JSON | `C` | Absent | Not started | — | — | — | — |
| `FAPI-HTTP-030` | Headers, cookies, content negotiation, and representation metadata | `C` | Absent | Not started | — | — | — | — |
| `FAPI-HTTP-040` | REST resources, actions, RPC-style endpoints, and practical constraints | `C` | Absent | Not started | — | — | — | — |
| `FAPI-HTTP-050` | Error contracts, RFC problem details, and API versioning | `C` | Absent | Not started | — | — | — | — |
| `FAPI-HTTP-060` | Pagination, filtering, sorting, and field selection | `C` | Absent | Not started | — | — | — | — |
| `FAPI-HTTP-070` | Partial updates, idempotency keys, and conditional writes | `P` | Absent | Not started | — | — | — | — |
| `FAPI-HTTP-080` | Caching, ETags, conditional requests, redirects, and range responses | `P` | Absent | Not started | — | — | — | — |
| `FAPI-ASGI-010` | WSGI versus ASGI and the protocol boundary | `C` | Absent | Not started | — | — | — | — |
| `FAPI-ASGI-020` | ASGI scope, receive, send, and the HTTP lifecycle | `C` | Absent | Not started | — | — | — | — |
| `FAPI-ASGI-030` | Starlette beneath FastAPI: requests, responses, routing, and exceptions | `C` | Absent | Not started | — | — | — | — |
| `FAPI-ASGI-040` | Lifespan, application state, and resource ownership | `C` | Absent | Not started | — | — | — | — |
| `FAPI-ASGI-050` | ASGI middleware onion, exception flow, and ordering | `C` | Absent | Not started | — | — | — | — |
| `FAPI-ASGI-060` | Client disconnects, cancellation, and streaming lifecycle | `P` | Absent | Not started | — | — | — | — |
| `FAPI-ASGI-070` | ASGI servers, workers, proxy headers, root paths, and mounted applications | `P` | Absent | Not started | — | — | — | — |
| `FAPI-PYD-010` | BaseModel fields: required, optional, nullable, defaults, and factories | `C` | Absent | Not started | — | — | — | — |
| `FAPI-PYD-020` | Coercion, strict validation, constraints, and Annotated | `C` | Absent | Not started | — | — | — | — |
| `FAPI-PYD-030` | Model configuration, extra fields, frozen models, copying, and trusted construction | `C` | Absent | Not started | — | — | — | — |
| `FAPI-PYD-040` | Nested and recursive models, forward annotations, unions, and discriminators | `C` | Absent | Not started | — | — | — | — |
| `FAPI-PYD-050` | Generics, RootModel, TypeAdapter, and Pydantic dataclasses | `P` | Absent | Not started | — | — | — | — |
| `FAPI-PYD-060` | Aliases, validation aliases, serialization aliases, and alias generators | `C` | Absent | Not started | — | — | — | — |
| `FAPI-PYD-070` | Field and model validators: modes, ordering, context, and defaults | `C` | Absent | Not started | — | — | — | — |
| `FAPI-PYD-080` | Serialization, serializers, computed fields, and inclusion or exclusion | `C` | Absent | Not started | — | — | — | — |
| `FAPI-PYD-090` | JSON Schema, OpenAPI interaction, and custom types | `P` | Absent | Not started | — | — | — | — |
| `FAPI-PYD-100` | Pydantic Settings: source precedence, env files, secrets, nesting, and custom sources | `C` | Absent | Not started | — | — | — | — |
| `FAPI-PYD-110` | Object-attribute validation and model boundaries | `C` | Absent | Not started | — | — | — | — |
| `FAPI-PYD-120` | Pydantic performance, validator side effects, v1-to-v2 migration, and common mistakes | `P` | Absent | Not started | — | — | — | — |
| `FAPI-APP-010` | Path operations, router matching, route order, and conflicts | `C` | Absent | Not started | — | — | — | — |
| `FAPI-APP-020` | Path and query parameters, constraints, aliases, and custom parsing | `C` | Absent | Not started | — | — | — | — |
| `FAPI-APP-030` | Headers, cookies, custom parameter types, and direct Request access | `C` | Absent | Not started | — | — | — | — |
| `FAPI-APP-040` | Request bodies, multiple body parameters, embedding, and aliases | `C` | Absent | Not started | — | — | — | — |
| `FAPI-APP-050` | Forms, multipart data, file uploads, and UploadFile | `C` | Absent | Not started | — | — | — | — |
| `FAPI-APP-060` | Response models, output validation, serialization, status, headers, and cookies | `C` | Absent | Not started | — | — | — | — |
| `FAPI-APP-070` | Response classes, redirects, files, and streaming responses | `C` | Absent | Not started | — | — | — | — |
| `FAPI-APP-080` | APIRouter, nested routers, tags, operation IDs, and route organization | `C` | Absent | Not started | — | — | — | — |
| `FAPI-APP-090` | HTTP exceptions, validation errors, custom handlers, and error translation | `C` | Absent | Not started | — | — | — | — |
| `FAPI-APP-100` | OpenAPI metadata, examples, callbacks, webhooks, and schema quality | `P` | Absent | Not started | — | — | — | — |
| `FAPI-DEP-010` | Callable, class-based, and parameterized dependencies | `C` | Absent | Not started | — | — | — | — |
| `FAPI-DEP-020` | Subdependencies and dependency-graph resolution | `C` | Absent | Not started | — | — | — | — |
| `FAPI-DEP-030` | Per-request dependency caching and use_cache | `C` | Absent | Not started | — | — | — | — |
| `FAPI-DEP-040` | Yield dependencies, setup/teardown order, scopes, and resource safety | `C` | Absent | Not started | — | — | — | — |
| `FAPI-DEP-050` | Authentication and authorization dependencies | `C` | Absent | Not started | — | — | — | — |
| `FAPI-DEP-060` | Router/global dependencies and test overrides | `C` | Absent | Not started | — | — | — | — |
| `FAPI-DEP-070` | Request state, composition roots, service location, and dependency boundaries | `P` | Absent | Not started | — | — | — | — |
| `FAPI-MID-010` | Function, class-based, and raw ASGI middleware ordering | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MID-020` | Request IDs, structured logging, context variables, and correlation | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MID-030` | CORS, trusted hosts, HTTPS redirects, compression, and sessions | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MID-040` | Body consumption, exception behavior, and cancellation in middleware | `P` | Absent | Not started | — | — | — | — |
| `FAPI-MID-050` | Rate limiting, observability, and choosing middleware versus dependencies | `P` | Absent | Not started | — | — | — | — |
| `FAPI-DB-010` | Relational modelling and PostgreSQL constraints for APIs | `C` | Absent | Not started | — | — | — | — |
| `FAPI-DB-020` | PostgreSQL drivers, SQLAlchemy engines, URLs, and connection pools | `C` | Absent | Not started | — | — | — | — |
| `FAPI-DB-030` | SQLAlchemy typed declarative mappings, columns, and constraints | `C` | Absent | Not started | — | — | — | — |
| `FAPI-DB-040` | Session per request, identity map, and unit-of-work lifecycle | `C` | Absent | Not started | — | — | — | — |
| `FAPI-DB-050` | Transactions, flush, commit, rollback, refresh, expiration, and savepoints | `C` | Absent | Not started | — | — | — | — |
| `FAPI-DB-060` | Relationships, cascades, eager/lazy loading, and object graphs | `C` | Absent | Not started | — | — | — | — |
| `FAPI-DB-070` | AsyncEngine, AsyncSession, and preventing implicit I/O | `C` | Absent | Not started | — | — | — | — |
| `FAPI-DB-080` | Queries, joins, aggregates, filtering, sorting, and pagination | `C` | Absent | Not started | — | — | — | — |
| `FAPI-DB-090` | N+1 diagnosis, eager loading, query plans, and indexes | `C` | Absent | Not started | — | — | — | — |
| `FAPI-DB-100` | Locking, isolation levels, deadlocks, retries, and optimistic concurrency | `P` | Absent | Not started | — | — | — | — |
| `FAPI-DB-110` | Bulk work, generated values, timestamps, soft deletion, and tenant boundaries | `P` | Absent | Not started | — | — | — | — |
| `FAPI-DB-120` | Database test isolation, mapping boundaries, repositories, and direct SQLAlchemy | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MIG-010` | Alembic environment, configuration, metadata discovery, and revision graph | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MIG-020` | First migration, upgrade, downgrade, current, and history | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MIG-030` | Autogenerate review, naming conventions, constraints, indexes, and defaults | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MIG-040` | Data migrations, backfills, enum changes, and offline SQL | `P` | Absent | Not started | — | — | — | — |
| `FAPI-MIG-050` | Migration branches, multiple heads, merge revisions, and conflicts | `P` | Absent | Not started | — | — | — | — |
| `FAPI-MIG-060` | Async application integration, migration testing, and drift detection | `P` | Absent | Not started | — | — | — | — |
| `FAPI-MIG-070` | Expand-and-contract changes, locks, compatibility windows, and rollback decisions | `P` | Absent | Not started | — | — | — | — |
| `FAPI-ARC-010` | From a single file to routers and feature modules | `C` | Absent | Not started | — | — | — | — |
| `FAPI-ARC-020` | Layered architecture versus vertical slices | `C` | Absent | Not started | — | — | — | — |
| `FAPI-ARC-030` | Service layer, functional core, domain services, DTO mapping, and orchestration | `C` | Absent | Not started | — | — | — | — |
| `FAPI-ARC-040` | Repository and Unit of Work patterns with transaction ownership | `P` | Absent | Not started | — | — | — | — |
| `FAPI-ARC-050` | Composition root, dependency inversion, and error translation | `C` | Absent | Not started | — | — | — | — |
| `FAPI-ARC-060` | Modular monolith boundaries, circular imports, and plugin extension points | `P` | Absent | Not started | — | — | — | — |
| `FAPI-ARC-070` | Multi-tenancy, gateway boundaries, monolith/microservice choices, and stopping rules | `P` | Absent | Not started | — | — | — | — |
| `FAPI-ASY-010` | def versus async def, event-loop execution, and thread-pool dispatch | `C` | Absent | Not started | — | — | — | — |
| `FAPI-ASY-020` | Blocking I/O, CPU-bound work, worker threads, and process offloading | `C` | Absent | Not started | — | — | — | — |
| `FAPI-ASY-030` | Timeouts, cancellation, task groups, and structured concurrency | `C` | Absent | Not started | — | — | — | — |
| `FAPI-ASY-040` | BackgroundTasks versus durable jobs and external workers | `C` | Absent | Not started | — | — | — | — |
| `FAPI-ASY-050` | Message brokers, RabbitMQ, retries, idempotency, and job state | `P` | Absent | Not started | — | — | — | — |
| `FAPI-ASY-060` | Streaming request/response bodies, backpressure, memory, and cleanup | `C` | Absent | Not started | — | — | — | — |
| `FAPI-ASY-070` | Workers, processes, concurrency limits, pool sizing, and shared state | `C` | Absent | Not started | — | — | — | — |
| `FAPI-ASY-080` | Caching, Redis, serialization costs, compression, and response size | `P` | Absent | Not started | — | — | — | — |
| `FAPI-ASY-090` | Profiling, load testing, benchmarking, and evidence-led performance diagnosis | `P` | Absent | Not started | — | — | — | — |
| `FAPI-SEC-010` | Authentication, authorization, and API threat modelling | `C` | Absent | Not started | — | — | — | — |
| `FAPI-SEC-020` | Password hashing, API keys, HTTP Basic, and bearer credentials | `C` | Absent | Not started | — | — | — | — |
| `FAPI-SEC-030` | JWT validation, key rotation, access tokens, refresh rotation, and revocation | `C` | Absent | Not started | — | — | — | — |
| `FAPI-SEC-040` | Secure cookies, sessions, CSRF, and browser credential boundaries | `C` | Absent | Not started | — | — | — | — |
| `FAPI-SEC-050` | OAuth2 flows, OpenID Connect, external identity providers, and scopes | `P` | Absent | Not started | — | — | — | — |
| `FAPI-SEC-060` | RBAC, ABAC, object-level authorization, and tenant isolation | `C` | Absent | Not started | — | — | — | — |
| `FAPI-SEC-070` | CORS, trusted hosts, HTTPS, proxy trust, and security headers | `C` | Absent | Not started | — | — | — | — |
| `FAPI-SEC-080` | Validation boundaries, mass assignment, SQL injection, SSRF, uploads, and path traversal | `C` | Absent | Not started | — | — | — | — |
| `FAPI-SEC-090` | Rate limits, brute-force controls, replay, idempotency, audit, and sensitive logging | `P` | Absent | Not started | — | — | — | — |
| `FAPI-SEC-100` | Secrets, dependency vulnerabilities, authorization tests, and security review | `P` | Absent | Not started | — | — | — | — |
| `FAPI-RT-010` | REST, RPC, streaming, events, GraphQL, and gRPC boundaries | `C` | Absent | Not started | — | — | — | — |
| `FAPI-RT-020` | Streaming HTTP responses, chunking, large files, and disconnects | `C` | Absent | Not started | — | — | — | — |
| `FAPI-RT-030` | Server-Sent Events: framing, reconnects, IDs, buffering, and cleanup | `P` | Absent | Not started | — | — | — | — |
| `FAPI-RT-040` | WebSocket handshake, connection lifetime, receive/send loops, and disconnects | `C` | Absent | Not started | — | — | — | — |
| `FAPI-RT-050` | WebSocket managers, broadcast, heartbeats, auth, backpressure, and scaling | `P` | Absent | Not started | — | — | — | — |
| `FAPI-RT-060` | Webhooks: signing, replay protection, retries, idempotency, and delivery logs | `P` | Absent | Not started | — | — | — | — |
| `FAPI-RT-070` | Polling, long polling, brokers, and event-driven API boundaries | `P` | Absent | Not started | — | — | — | — |
| `FAPI-RT-080` | gRPC foundations: Protocol Buffers, code generation, unary calls, status, and metadata | `P` | Absent | Not started | — | — | — | — |
| `FAPI-RT-090` | gRPC streaming, deadlines, cancellation, interceptors, auth, evolution, and gateways | `A` | Absent | Not started | — | — | — | — |
| `FAPI-TST-010` | Testing strategy, observable contracts, and test boundaries | `C` | Absent | Not started | — | — | — | — |
| `FAPI-TST-020` | TestClient, HTTPX AsyncClient, ASGI transports, and lifespan-aware tests | `C` | Absent | Not started | — | — | — | — |
| `FAPI-TST-030` | Dependency overrides, auth tests, validation errors, and OpenAPI contracts | `C` | Absent | Not started | — | — | — | — |
| `FAPI-TST-040` | Property-based testing for Pydantic models and API contracts | `P` | Absent | Not started | — | — | — | — |
| `FAPI-TST-050` | PostgreSQL integration tests, transaction isolation, fixtures, and factories | `C` | Absent | Not started | — | — | — | — |
| `FAPI-TST-060` | Alembic migration tests and schema-compatibility checks | `P` | Absent | Not started | — | — | — | — |
| `FAPI-TST-070` | WebSocket, SSE, gRPC, webhook, and background-job tests | `P` | Absent | Not started | — | — | — | — |
| `FAPI-TST-080` | Timeout, retry, concurrency, load, performance, and security-focused tests | `P` | Absent | Not started | — | — | — | — |
| `FAPI-OPS-010` | Environment configuration, secret injection, and production settings | `C` | Absent | Not started | — | — | — | — |
| `FAPI-OPS-020` | Uvicorn process model, workers, startup, shutdown, and graceful draining | `C` | Absent | Not started | — | — | — | — |
| `FAPI-OPS-030` | Reverse proxies, forwarded headers, root paths, TLS, and trust | `C` | Absent | Not started | — | — | — | — |
| `FAPI-OPS-040` | Containers, images, Compose profiles, health, and readiness | `C` | Absent | Not started | — | — | — | — |
| `FAPI-OPS-050` | Structured logs, metrics, traces, and request-span propagation | `C` | Absent | Not started | — | — | — | — |
| `FAPI-OPS-060` | Capacity planning, worker/pool limits, load tests, and performance budgets | `P` | Absent | Not started | — | — | — | — |
| `FAPI-OPS-070` | Production debugging, incident response, deployment strategies, and rollback | `P` | Absent | Not started | — | — | — | — |
| `FAPI-SYN-010` | Request-lifecycle and framework-boundary interview synthesis | `C` | Absent | Not started | — | — | — | — |
| `FAPI-SYN-020` | Pydantic, dependency, middleware, and error-handling interview synthesis | `C` | Absent | Not started | — | — | — | — |
| `FAPI-SYN-030` | PostgreSQL, SQLAlchemy, Alembic, and architecture interview synthesis | `C` | Absent | Not started | — | — | — | — |
| `FAPI-SYN-040` | Async, security, real-time, performance, and production design synthesis | `C` | Absent | Not started | — | — | — | — |
| `FAPI-SYN-050` | Senior FastAPI code review, debugging, and architecture capstone | `P` | Absent | Not started | — | — | — | — |

| `FAPI-MSV-010` | Microservice decision, decomposition, ownership, and stopping rules | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-020` | Remote-call reality: partial failure, latency, clocks, concurrency, and partitions | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-030` | Communication selection across HTTP, gRPC, queues, pub/sub, logs, and browser streams | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-040` | Service and message contracts, envelopes, versioning, and ownership | `P` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-050` | RabbitMQ fundamentals: AMQP entities, topology, routing, and local operations | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-060` | RabbitMQ connections, channels, recovery, permissions, and topology compatibility | `P` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-070` | RabbitMQ publisher correctness: confirms, mandatory returns, uncertainty, and backpressure | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-080` | RabbitMQ consumer correctness: acknowledgements, prefetch, crash windows, and draining | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-090` | RabbitMQ retries, dead lettering, delay, redrive, and poison-message operations | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-100` | RabbitMQ queue types, ordering, retention, and broker selection | `P` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-110` | Delivery semantics, duplicate handling, and idempotent operations | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-120` | Transactional outbox, inbox, relay, CDC boundaries, and cleanup | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-130` | Distributed workflows: sagas, compensation, orchestration, and intervention | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-140` | Eventual consistency, read models, CQRS, and event-sourcing boundaries | `P` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-150` | Production gRPC contracts: Protobuf evolution, status details, and metadata | `P` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-160` | Production gRPC execution: deadlines, cancellation, retries, streaming, and flow control | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-170` | gRPC operations: channels, discovery, balancing, health, TLS, tracing, and gateways | `P` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-180` | Resilience budgets: timeouts, retry amplification, breakers, bulkheads, and load shedding | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-190` | Discovery, gateways, proxies, Kubernetes traffic, and service-mesh boundaries | `P` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-200` | Service data ownership, cross-service queries, reporting, and migration from shared storage | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-210` | Distributed observability: context propagation, logs, metrics, traces, SLIs, SLOs, and alerts | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-220` | Microservice security: workload identity, mTLS, delegated authorization, broker permissions, and tenant context | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-230` | Distributed testing: contracts, real dependencies, duplicate delivery, fault injection, and eventual consistency | `C` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-240` | Compatible deployment and evolution: rollout, draining, autoscaling, backlog, and schema windows | `P` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-250` | Reliability operations: runbooks, incidents, postmortems, disaster recovery, and dependency upgrades | `P` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-260` | Governance and ownership: catalogs, ADRs, golden paths, shared libraries, team topology, and cost | `A` | Absent | Not started | — | — | — | — |
| `FAPI-MSV-270` | Evolutionary extraction and senior microservice design synthesis | `C` | Absent | Not started | — | — | — | — |

## Project tracker

| Project ID | Project | Project state | Branch | Last evidence date | Evidence link | Remaining weakness or unfinished requirement |
|---|---|---|---|---|---|---|
| `FAPI-PRJ-010` | First typed CRUD API | Planned | `project/FAPI-PRJ-010` | — | — | Not started |
| `FAPI-PRJ-020` | PostgreSQL catalog and ordering service | Planned | `project/FAPI-PRJ-020` | — | — | Not started |
| `FAPI-PRJ-030` | Authenticated multi-tenant service | Planned | `project/FAPI-PRJ-030` | — | — | Not started |
| `FAPI-PRJ-040` | Synthetic review and workflow platform | Planned | `project/FAPI-PRJ-040` | — | — | Not started |
| `FAPI-PRJ-050` | File-processing and durable-job service | Planned | `project/FAPI-PRJ-050` | — | — | Not started |
| `FAPI-PRJ-060` | Real-time operations dashboard | Planned | `project/FAPI-PRJ-060` | — | — | Not started |
| `FAPI-PRJ-070` | REST-to-gRPC gateway | Planned | `project/FAPI-PRJ-070` | — | — | Not started |
| `FAPI-PRJ-080` | Production modular backend capstone | Planned | `project/FAPI-PRJ-080` | — | — | Not started |
| `FAPI-PRJ-090` | Reliable RabbitMQ workflow service | Planned | `project/FAPI-PRJ-090` | — | — | Outbox, confirms, crash windows, DLQ, and runbook not started |
| `FAPI-PRJ-100` | Microservices production capstone | Planned | `project/FAPI-PRJ-100` | — | — | Evolutionary extraction and distributed operations not started |
