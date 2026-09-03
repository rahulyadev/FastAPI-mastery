# Learning paths

Paths are recommended views over the same canonical units. Any unit may be initialized earlier with a precise prerequisite bridge. Short routes may assume only the exact prerequisites listed in their own section.
## Selector

- [Absolute FastAPI beginner path](#absolute-fastapi-beginner)
- [Emergency FastAPI interview revision](#emergency-fastapi-interview)
- [7-day FastAPI refresher](#seven-day-fastapi-refresher)
- [14-day backend interview preparation](#fourteen-day-backend-interview)
- [30-day production foundation](#thirty-day-production-foundation)
- [90-day FastAPI mastery](#ninety-day-fastapi-mastery)
- [Complete FastAPI mastery](#complete-fastapi-mastery)
- [Deep Pydantic path](#deep-pydantic)
- [PostgreSQL, SQLAlchemy, and Alembic path](#postgres-sqlalchemy-alembic)
- [Async, concurrency, and performance path](#async-concurrency-performance)
- [Security and authentication path](#security-authentication)
- [API architecture and production path](#api-architecture-production)
- [WebSockets, SSE, streaming, and gRPC path](#realtime-streaming-grpc)
- [Senior interview and design-practice path](#senior-interview-design-practice)
- [RabbitMQ and reliable asynchronous services](#rabbitmq-reliable-async-services)
- [Microservices and distributed service engineering](#microservices-distributed-service-engineering)
- [Senior microservices design and operations](#senior-microservices-design-operations)

## Study-depth contracts

### Rapid interview pass

Includes Physical Notebook Core, essential visual, minimal example, runtime trace, recognition cues, one comparison, traps, focused questions, and a tiny micro-drill. A complete learner challenge is counted separately under selected practice.

### Full mastery pass

Includes complete notes, examples, implementation, tests, database/runtime experiments, debugging, refactoring, comparisons, delayed recall, and transfer evidence. Project work and later review cycles remain additional.

<a id="absolute-fastapi-beginner"></a>
## Absolute FastAPI beginner path

For rebuilding from first principles with no assumed FastAPI knowledge.

<!-- path-meta: {"slug":"absolute-fastapi-beginner","declared_units":35,"rapid_unit_minutes":[1430,2200],"lab_minutes":[300,420],"recall_minutes":[120,180],"mock_minutes":[0,0],"checkpoint_minutes":[120,180],"rapid_total_minutes":[1970,2980],"full_mastery_hours":[276,492],"assumed_prerequisites":[]} -->
| Component | Count or time |
|---|---:|
| Canonical units | 35 |
| Rapid unit study | 23 h 50 min–36 h 40 min |
| Selected practice/labs | 0 checkpoints; 5 h–7 h |
| Recall and comparison | 2 h–3 h |
| Mock interviews | 0 min–0 min |
| Project checkpoints | 2 h–3 h |
| **Rapid path total** | **32 h 50 min–49 h 40 min** |
| Full mastery of included units | 276–492 h |

### Assumed prior knowledge or prerequisite bridges

None. The path includes its canonical prerequisites.

### Recommended sequence

| # | Unit | Size |
|---:|---|:---:|
| 1 | [FAPI-FND-010 — Python runtime, uv project, and reproducible environment](CURRICULUM.md#fapi-fnd-010) | `M` |
| 2 | [FAPI-FND-020 — Minimal FastAPI application and first route](CURRICULUM.md#fapi-fnd-020) | `S` |
| 3 | [FAPI-FND-030 — Application entry points, import strings, reload, and server startup](CURRICULUM.md#fapi-fnd-030) | `M` |
| 4 | [FAPI-FND-040 — Interactive documentation, OpenAPI inspection, and simple API clients](CURRICULUM.md#fapi-fnd-040) | `S` |
| 5 | [FAPI-FND-050 — Configuration, environment variables, and application factories](CURRICULUM.md#fapi-fnd-050) | `M` |
| 6 | [FAPI-FND-060 — Startup, import, reload, and configuration failure diagnosis](CURRICULUM.md#fapi-fnd-060) | `M` |
| 7 | [FAPI-HTTP-010 — HTTP message anatomy, methods, status codes, and media types](CURRICULUM.md#fapi-http-010) | `L` |
| 8 | [FAPI-HTTP-020 — URLs, path/query semantics, request bodies, encoding, and JSON](CURRICULUM.md#fapi-http-020) | `M` |
| 9 | [FAPI-HTTP-040 — REST resources, actions, RPC-style endpoints, and practical constraints](CURRICULUM.md#fapi-http-040) | `L` |
| 10 | [FAPI-HTTP-050 — Error contracts, RFC problem details, and API versioning](CURRICULUM.md#fapi-http-050) | `L` |
| 11 | [FAPI-HTTP-060 — Pagination, filtering, sorting, and field selection](CURRICULUM.md#fapi-http-060) | `L` |
| 12 | [FAPI-ASGI-010 — WSGI versus ASGI and the protocol boundary](CURRICULUM.md#fapi-asgi-010) | `L` |
| 13 | [FAPI-ASGI-020 — ASGI scope, receive, send, and the HTTP lifecycle](CURRICULUM.md#fapi-asgi-020) | `L` |
| 14 | [FAPI-ASGI-030 — Starlette beneath FastAPI: requests, responses, routing, and exceptions](CURRICULUM.md#fapi-asgi-030) | `L` |
| 15 | [FAPI-ASGI-040 — Lifespan, application state, and resource ownership](CURRICULUM.md#fapi-asgi-040) | `L` |
| 16 | [FAPI-ASGI-050 — ASGI middleware onion, exception flow, and ordering](CURRICULUM.md#fapi-asgi-050) | `L` |
| 17 | [FAPI-PYD-010 — BaseModel fields: required, optional, nullable, defaults, and factories](CURRICULUM.md#fapi-pyd-010) | `M` |
| 18 | [FAPI-PYD-020 — Coercion, strict validation, constraints, and Annotated](CURRICULUM.md#fapi-pyd-020) | `L` |
| 19 | [FAPI-PYD-030 — Model configuration, extra fields, frozen models, copying, and trusted construction](CURRICULUM.md#fapi-pyd-030) | `L` |
| 20 | [FAPI-PYD-060 — Aliases, validation aliases, serialization aliases, and alias generators](CURRICULUM.md#fapi-pyd-060) | `M` |
| 21 | [FAPI-PYD-080 — Serialization, serializers, computed fields, and inclusion or exclusion](CURRICULUM.md#fapi-pyd-080) | `L` |
| 22 | [FAPI-APP-010 — Path operations, router matching, route order, and conflicts](CURRICULUM.md#fapi-app-010) | `M` |
| 23 | [FAPI-APP-020 — Path and query parameters, constraints, aliases, and custom parsing](CURRICULUM.md#fapi-app-020) | `L` |
| 24 | [FAPI-APP-040 — Request bodies, multiple body parameters, embedding, and aliases](CURRICULUM.md#fapi-app-040) | `L` |
| 25 | [FAPI-APP-060 — Response models, output validation, serialization, status, headers, and cookies](CURRICULUM.md#fapi-app-060) | `L` |
| 26 | [FAPI-APP-080 — APIRouter, nested routers, tags, operation IDs, and route organization](CURRICULUM.md#fapi-app-080) | `L` |
| 27 | [FAPI-APP-090 — HTTP exceptions, validation errors, custom handlers, and error translation](CURRICULUM.md#fapi-app-090) | `L` |
| 28 | [FAPI-DEP-010 — Callable, class-based, and parameterized dependencies](CURRICULUM.md#fapi-dep-010) | `L` |
| 29 | [FAPI-DEP-020 — Subdependencies and dependency-graph resolution](CURRICULUM.md#fapi-dep-020) | `L` |
| 30 | [FAPI-DEP-040 — Yield dependencies, setup/teardown order, scopes, and resource safety](CURRICULUM.md#fapi-dep-040) | `XL` |
| 31 | [FAPI-DEP-060 — Router/global dependencies and test overrides](CURRICULUM.md#fapi-dep-060) | `L` |
| 32 | [FAPI-ARC-010 — From a single file to routers and feature modules](CURRICULUM.md#fapi-arc-010) | `L` |
| 33 | [FAPI-TST-010 — Testing strategy, observable contracts, and test boundaries](CURRICULUM.md#fapi-tst-010) | `L` |
| 34 | [FAPI-TST-020 — TestClient, HTTPX AsyncClient, ASGI transports, and lifespan-aware tests](CURRICULUM.md#fapi-tst-020) | `L` |
| 35 | [FAPI-TST-030 — Dependency overrides, auth tests, validation errors, and OpenAPI contracts](CURRICULUM.md#fapi-tst-030) | `L` |

### Project milestones

- [FAPI-PRJ-010 — First typed CRUD API](PROJECTS.md#fapi-prj-010)

<a id="emergency-fastapi-interview"></a>
## Emergency FastAPI interview revision

For prior FastAPI users who need a focused revision pass. Every omitted prerequisite is listed explicitly as assumed prior knowledge or a required bridge; this is not a beginner transformation.

<!-- path-meta: {"slug":"emergency-fastapi-interview","declared_units":31,"rapid_unit_minutes":[1500,2265],"lab_minutes":[240,360],"recall_minutes":[120,180],"mock_minutes":[90,120],"checkpoint_minutes":[60,120],"rapid_total_minutes":[2010,3045],"full_mastery_hours":[309,547],"assumed_prerequisites":["FAPI-FND-010","FAPI-FND-050","FAPI-HTTP-020","FAPI-ASGI-070","FAPI-PYD-030","FAPI-PYD-040","FAPI-PYD-060","FAPI-APP-020","FAPI-APP-040","FAPI-DEP-050","FAPI-DB-020","FAPI-DB-030","FAPI-DB-110","FAPI-ASY-070","FAPI-SEC-020","FAPI-SEC-070","FAPI-TST-010"]} -->
| Component | Count or time |
|---|---:|
| Canonical units | 31 |
| Rapid unit study | 25 h–37 h 45 min |
| Selected practice/labs | 0 checkpoints; 4 h–6 h |
| Recall and comparison | 2 h–3 h |
| Mock interviews | 1 h 30 min–2 h |
| Project checkpoints | 1 h–2 h |
| **Rapid path total** | **33 h 30 min–50 h 45 min** |
| Full mastery of included units | 309–547 h |

**Time assumption:** prior exposure and approximately four to six full-time days. This is a rapid review contract, not full mastery.

### Assumed prior knowledge or prerequisite bridges

These are explicit omissions, not hidden prerequisites. Review each before its dependent unit or ask Codex for the smallest correct bridge.

- [FAPI-FND-010 — Python runtime, uv project, and reproducible environment](CURRICULUM.md#fapi-fnd-010) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-FND-050 — Configuration, environment variables, and application factories](CURRICULUM.md#fapi-fnd-050) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-HTTP-020 — URLs, path/query semantics, request bodies, encoding, and JSON](CURRICULUM.md#fapi-http-020) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-ASGI-070 — ASGI servers, workers, proxy headers, root paths, and mounted applications](CURRICULUM.md#fapi-asgi-070) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-PYD-030 — Model configuration, extra fields, frozen models, copying, and trusted construction](CURRICULUM.md#fapi-pyd-030) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-PYD-040 — Nested and recursive models, forward annotations, unions, and discriminators](CURRICULUM.md#fapi-pyd-040) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-PYD-060 — Aliases, validation aliases, serialization aliases, and alias generators](CURRICULUM.md#fapi-pyd-060) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-APP-020 — Path and query parameters, constraints, aliases, and custom parsing](CURRICULUM.md#fapi-app-020) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-APP-040 — Request bodies, multiple body parameters, embedding, and aliases](CURRICULUM.md#fapi-app-040) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-DEP-050 — Authentication and authorization dependencies](CURRICULUM.md#fapi-dep-050) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-DB-020 — PostgreSQL drivers, SQLAlchemy engines, URLs, and connection pools](CURRICULUM.md#fapi-db-020) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-DB-030 — SQLAlchemy typed declarative mappings, columns, and constraints](CURRICULUM.md#fapi-db-030) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-DB-110 — Bulk work, generated values, timestamps, soft deletion, and tenant boundaries](CURRICULUM.md#fapi-db-110) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-ASY-070 — Workers, processes, concurrency limits, pool sizing, and shared state](CURRICULUM.md#fapi-asy-070) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-SEC-020 — Password hashing, API keys, HTTP Basic, and bearer credentials](CURRICULUM.md#fapi-sec-020) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-SEC-070 — CORS, trusted hosts, HTTPS, proxy trust, and security headers](CURRICULUM.md#fapi-sec-070) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-TST-010 — Testing strategy, observable contracts, and test boundaries](CURRICULUM.md#fapi-tst-010) — assumed prior knowledge or prerequisite bridge required.

### Recommended sequence

| # | Unit | Size |
|---:|---|:---:|
| 1 | [FAPI-FND-020 — Minimal FastAPI application and first route](CURRICULUM.md#fapi-fnd-020) | `S` |
| 2 | [FAPI-FND-030 — Application entry points, import strings, reload, and server startup](CURRICULUM.md#fapi-fnd-030) | `M` |
| 3 | [FAPI-HTTP-010 — HTTP message anatomy, methods, status codes, and media types](CURRICULUM.md#fapi-http-010) | `L` |
| 4 | [FAPI-HTTP-040 — REST resources, actions, RPC-style endpoints, and practical constraints](CURRICULUM.md#fapi-http-040) | `L` |
| 5 | [FAPI-HTTP-050 — Error contracts, RFC problem details, and API versioning](CURRICULUM.md#fapi-http-050) | `L` |
| 6 | [FAPI-ASGI-010 — WSGI versus ASGI and the protocol boundary](CURRICULUM.md#fapi-asgi-010) | `L` |
| 7 | [FAPI-ASGI-020 — ASGI scope, receive, send, and the HTTP lifecycle](CURRICULUM.md#fapi-asgi-020) | `L` |
| 8 | [FAPI-ASGI-030 — Starlette beneath FastAPI: requests, responses, routing, and exceptions](CURRICULUM.md#fapi-asgi-030) | `L` |
| 9 | [FAPI-ASGI-040 — Lifespan, application state, and resource ownership](CURRICULUM.md#fapi-asgi-040) | `L` |
| 10 | [FAPI-ASGI-050 — ASGI middleware onion, exception flow, and ordering](CURRICULUM.md#fapi-asgi-050) | `L` |
| 11 | [FAPI-PYD-010 — BaseModel fields: required, optional, nullable, defaults, and factories](CURRICULUM.md#fapi-pyd-010) | `M` |
| 12 | [FAPI-PYD-020 — Coercion, strict validation, constraints, and Annotated](CURRICULUM.md#fapi-pyd-020) | `L` |
| 13 | [FAPI-PYD-070 — Field and model validators: modes, ordering, context, and defaults](CURRICULUM.md#fapi-pyd-070) | `XL` |
| 14 | [FAPI-PYD-080 — Serialization, serializers, computed fields, and inclusion or exclusion](CURRICULUM.md#fapi-pyd-080) | `L` |
| 15 | [FAPI-APP-010 — Path operations, router matching, route order, and conflicts](CURRICULUM.md#fapi-app-010) | `M` |
| 16 | [FAPI-APP-060 — Response models, output validation, serialization, status, headers, and cookies](CURRICULUM.md#fapi-app-060) | `L` |
| 17 | [FAPI-APP-090 — HTTP exceptions, validation errors, custom handlers, and error translation](CURRICULUM.md#fapi-app-090) | `L` |
| 18 | [FAPI-DEP-010 — Callable, class-based, and parameterized dependencies](CURRICULUM.md#fapi-dep-010) | `L` |
| 19 | [FAPI-DEP-020 — Subdependencies and dependency-graph resolution](CURRICULUM.md#fapi-dep-020) | `L` |
| 20 | [FAPI-DEP-040 — Yield dependencies, setup/teardown order, scopes, and resource safety](CURRICULUM.md#fapi-dep-040) | `XL` |
| 21 | [FAPI-DB-040 — Session per request, identity map, and unit-of-work lifecycle](CURRICULUM.md#fapi-db-040) | `XL` |
| 22 | [FAPI-DB-050 — Transactions, flush, commit, rollback, refresh, expiration, and savepoints](CURRICULUM.md#fapi-db-050) | `XL` |
| 23 | [FAPI-DB-070 — AsyncEngine, AsyncSession, and preventing implicit I/O](CURRICULUM.md#fapi-db-070) | `XL` |
| 24 | [FAPI-ASY-010 — def versus async def, event-loop execution, and thread-pool dispatch](CURRICULUM.md#fapi-asy-010) | `L` |
| 25 | [FAPI-ASY-020 — Blocking I/O, CPU-bound work, worker threads, and process offloading](CURRICULUM.md#fapi-asy-020) | `L` |
| 26 | [FAPI-SEC-010 — Authentication, authorization, and API threat modelling](CURRICULUM.md#fapi-sec-010) | `L` |
| 27 | [FAPI-SEC-030 — JWT validation, key rotation, access tokens, refresh rotation, and revocation](CURRICULUM.md#fapi-sec-030) | `XL` |
| 28 | [FAPI-SEC-060 — RBAC, ABAC, object-level authorization, and tenant isolation](CURRICULUM.md#fapi-sec-060) | `XL` |
| 29 | [FAPI-TST-020 — TestClient, HTTPX AsyncClient, ASGI transports, and lifespan-aware tests](CURRICULUM.md#fapi-tst-020) | `L` |
| 30 | [FAPI-OPS-020 — Uvicorn process model, workers, startup, shutdown, and graceful draining](CURRICULUM.md#fapi-ops-020) | `L` |
| 31 | [FAPI-OPS-030 — Reverse proxies, forwarded headers, root paths, TLS, and trust](CURRICULUM.md#fapi-ops-030) | `L` |

### Project milestones

- [FAPI-PRJ-010 — First typed CRUD API](PROJECTS.md#fapi-prj-010)
- [FAPI-PRJ-020 — PostgreSQL catalog and ordering service](PROJECTS.md#fapi-prj-020)

<a id="seven-day-fastapi-refresher"></a>
## 7-day FastAPI refresher

For prior professional exposure and a full-time week. Every omitted prerequisite is named explicitly; specialist transports, advanced migration cases, and optional integrations are deferred.

<!-- path-meta: {"slug":"seven-day-fastapi-refresher","declared_units":70,"rapid_unit_minutes":[3405,5140],"lab_minutes":[480,660],"recall_minutes":[180,300],"mock_minutes":[120,180],"checkpoint_minutes":[120,180],"rapid_total_minutes":[4305,6460],"full_mastery_hours":[703,1244],"assumed_prerequisites":["FAPI-FND-040","FAPI-ASGI-060","FAPI-ASGI-070","FAPI-PYD-060","FAPI-PYD-110","FAPI-APP-050","FAPI-DEP-070","FAPI-MID-050","FAPI-DB-060","FAPI-DB-080","FAPI-DB-110","FAPI-DB-120","FAPI-SEC-020","FAPI-SEC-040","FAPI-SEC-070"]} -->
| Component | Count or time |
|---|---:|
| Canonical units | 70 |
| Rapid unit study | 56 h 45 min–85 h 40 min |
| Selected practice/labs | 0 checkpoints; 8 h–11 h |
| Recall and comparison | 3 h–5 h |
| Mock interviews | 2 h–3 h |
| Project checkpoints | 2 h–3 h |
| **Rapid path total** | **71 h 45 min–107 h 40 min** |
| Full mastery of included units | 703–1244 h |

**Time assumption:** prior exposure and a full-time seven-day week. The total requires several focused hours every day.

### Assumed prior knowledge or prerequisite bridges

These are explicit omissions, not hidden prerequisites. Review each before its dependent unit or ask Codex for the smallest correct bridge.

- [FAPI-FND-040 — Interactive documentation, OpenAPI inspection, and simple API clients](CURRICULUM.md#fapi-fnd-040) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-ASGI-060 — Client disconnects, cancellation, and streaming lifecycle](CURRICULUM.md#fapi-asgi-060) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-ASGI-070 — ASGI servers, workers, proxy headers, root paths, and mounted applications](CURRICULUM.md#fapi-asgi-070) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-PYD-060 — Aliases, validation aliases, serialization aliases, and alias generators](CURRICULUM.md#fapi-pyd-060) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-PYD-110 — Object-attribute validation and model boundaries](CURRICULUM.md#fapi-pyd-110) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-APP-050 — Forms, multipart data, file uploads, and UploadFile](CURRICULUM.md#fapi-app-050) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-DEP-070 — Request state, composition roots, service location, and dependency boundaries](CURRICULUM.md#fapi-dep-070) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-MID-050 — Rate limiting, observability, and choosing middleware versus dependencies](CURRICULUM.md#fapi-mid-050) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-DB-060 — Relationships, cascades, eager/lazy loading, and object graphs](CURRICULUM.md#fapi-db-060) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-DB-080 — Queries, joins, aggregates, filtering, sorting, and pagination](CURRICULUM.md#fapi-db-080) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-DB-110 — Bulk work, generated values, timestamps, soft deletion, and tenant boundaries](CURRICULUM.md#fapi-db-110) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-DB-120 — Database test isolation, mapping boundaries, repositories, and direct SQLAlchemy](CURRICULUM.md#fapi-db-120) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-SEC-020 — Password hashing, API keys, HTTP Basic, and bearer credentials](CURRICULUM.md#fapi-sec-020) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-SEC-040 — Secure cookies, sessions, CSRF, and browser credential boundaries](CURRICULUM.md#fapi-sec-040) — assumed prior knowledge or prerequisite bridge required.
- [FAPI-SEC-070 — CORS, trusted hosts, HTTPS, proxy trust, and security headers](CURRICULUM.md#fapi-sec-070) — assumed prior knowledge or prerequisite bridge required.

### Recommended sequence

| # | Unit | Size |
|---:|---|:---:|
| 1 | [FAPI-FND-010 — Python runtime, uv project, and reproducible environment](CURRICULUM.md#fapi-fnd-010) | `M` |
| 2 | [FAPI-FND-020 — Minimal FastAPI application and first route](CURRICULUM.md#fapi-fnd-020) | `S` |
| 3 | [FAPI-FND-030 — Application entry points, import strings, reload, and server startup](CURRICULUM.md#fapi-fnd-030) | `M` |
| 4 | [FAPI-FND-050 — Configuration, environment variables, and application factories](CURRICULUM.md#fapi-fnd-050) | `M` |
| 5 | [FAPI-HTTP-010 — HTTP message anatomy, methods, status codes, and media types](CURRICULUM.md#fapi-http-010) | `L` |
| 6 | [FAPI-HTTP-020 — URLs, path/query semantics, request bodies, encoding, and JSON](CURRICULUM.md#fapi-http-020) | `M` |
| 7 | [FAPI-HTTP-030 — Headers, cookies, content negotiation, and representation metadata](CURRICULUM.md#fapi-http-030) | `M` |
| 8 | [FAPI-HTTP-040 — REST resources, actions, RPC-style endpoints, and practical constraints](CURRICULUM.md#fapi-http-040) | `L` |
| 9 | [FAPI-HTTP-050 — Error contracts, RFC problem details, and API versioning](CURRICULUM.md#fapi-http-050) | `L` |
| 10 | [FAPI-HTTP-060 — Pagination, filtering, sorting, and field selection](CURRICULUM.md#fapi-http-060) | `L` |
| 11 | [FAPI-HTTP-070 — Partial updates, idempotency keys, and conditional writes](CURRICULUM.md#fapi-http-070) | `L` |
| 12 | [FAPI-ASGI-010 — WSGI versus ASGI and the protocol boundary](CURRICULUM.md#fapi-asgi-010) | `L` |
| 13 | [FAPI-ASGI-020 — ASGI scope, receive, send, and the HTTP lifecycle](CURRICULUM.md#fapi-asgi-020) | `L` |
| 14 | [FAPI-ASGI-030 — Starlette beneath FastAPI: requests, responses, routing, and exceptions](CURRICULUM.md#fapi-asgi-030) | `L` |
| 15 | [FAPI-ASGI-040 — Lifespan, application state, and resource ownership](CURRICULUM.md#fapi-asgi-040) | `L` |
| 16 | [FAPI-ASGI-050 — ASGI middleware onion, exception flow, and ordering](CURRICULUM.md#fapi-asgi-050) | `L` |
| 17 | [FAPI-PYD-010 — BaseModel fields: required, optional, nullable, defaults, and factories](CURRICULUM.md#fapi-pyd-010) | `M` |
| 18 | [FAPI-PYD-020 — Coercion, strict validation, constraints, and Annotated](CURRICULUM.md#fapi-pyd-020) | `L` |
| 19 | [FAPI-PYD-030 — Model configuration, extra fields, frozen models, copying, and trusted construction](CURRICULUM.md#fapi-pyd-030) | `L` |
| 20 | [FAPI-PYD-040 — Nested and recursive models, forward annotations, unions, and discriminators](CURRICULUM.md#fapi-pyd-040) | `L` |
| 21 | [FAPI-PYD-070 — Field and model validators: modes, ordering, context, and defaults](CURRICULUM.md#fapi-pyd-070) | `XL` |
| 22 | [FAPI-PYD-080 — Serialization, serializers, computed fields, and inclusion or exclusion](CURRICULUM.md#fapi-pyd-080) | `L` |
| 23 | [FAPI-PYD-100 — Pydantic Settings: source precedence, env files, secrets, nesting, and custom sources](CURRICULUM.md#fapi-pyd-100) | `L` |
| 24 | [FAPI-APP-010 — Path operations, router matching, route order, and conflicts](CURRICULUM.md#fapi-app-010) | `M` |
| 25 | [FAPI-APP-020 — Path and query parameters, constraints, aliases, and custom parsing](CURRICULUM.md#fapi-app-020) | `L` |
| 26 | [FAPI-APP-040 — Request bodies, multiple body parameters, embedding, and aliases](CURRICULUM.md#fapi-app-040) | `L` |
| 27 | [FAPI-APP-060 — Response models, output validation, serialization, status, headers, and cookies](CURRICULUM.md#fapi-app-060) | `L` |
| 28 | [FAPI-APP-080 — APIRouter, nested routers, tags, operation IDs, and route organization](CURRICULUM.md#fapi-app-080) | `L` |
| 29 | [FAPI-APP-090 — HTTP exceptions, validation errors, custom handlers, and error translation](CURRICULUM.md#fapi-app-090) | `L` |
| 30 | [FAPI-DEP-010 — Callable, class-based, and parameterized dependencies](CURRICULUM.md#fapi-dep-010) | `L` |
| 31 | [FAPI-DEP-020 — Subdependencies and dependency-graph resolution](CURRICULUM.md#fapi-dep-020) | `L` |
| 32 | [FAPI-DEP-030 — Per-request dependency caching and use_cache](CURRICULUM.md#fapi-dep-030) | `M` |
| 33 | [FAPI-DEP-040 — Yield dependencies, setup/teardown order, scopes, and resource safety](CURRICULUM.md#fapi-dep-040) | `XL` |
| 34 | [FAPI-DEP-050 — Authentication and authorization dependencies](CURRICULUM.md#fapi-dep-050) | `L` |
| 35 | [FAPI-DEP-060 — Router/global dependencies and test overrides](CURRICULUM.md#fapi-dep-060) | `L` |
| 36 | [FAPI-MID-010 — Function, class-based, and raw ASGI middleware ordering](CURRICULUM.md#fapi-mid-010) | `L` |
| 37 | [FAPI-MID-020 — Request IDs, structured logging, context variables, and correlation](CURRICULUM.md#fapi-mid-020) | `L` |
| 38 | [FAPI-MID-030 — CORS, trusted hosts, HTTPS redirects, compression, and sessions](CURRICULUM.md#fapi-mid-030) | `L` |
| 39 | [FAPI-DB-010 — Relational modelling and PostgreSQL constraints for APIs](CURRICULUM.md#fapi-db-010) | `L` |
| 40 | [FAPI-DB-020 — PostgreSQL drivers, SQLAlchemy engines, URLs, and connection pools](CURRICULUM.md#fapi-db-020) | `L` |
| 41 | [FAPI-DB-030 — SQLAlchemy typed declarative mappings, columns, and constraints](CURRICULUM.md#fapi-db-030) | `L` |
| 42 | [FAPI-DB-040 — Session per request, identity map, and unit-of-work lifecycle](CURRICULUM.md#fapi-db-040) | `XL` |
| 43 | [FAPI-DB-050 — Transactions, flush, commit, rollback, refresh, expiration, and savepoints](CURRICULUM.md#fapi-db-050) | `XL` |
| 44 | [FAPI-DB-070 — AsyncEngine, AsyncSession, and preventing implicit I/O](CURRICULUM.md#fapi-db-070) | `XL` |
| 45 | [FAPI-DB-090 — N+1 diagnosis, eager loading, query plans, and indexes](CURRICULUM.md#fapi-db-090) | `XL` |
| 46 | [FAPI-MIG-010 — Alembic environment, configuration, metadata discovery, and revision graph](CURRICULUM.md#fapi-mig-010) | `L` |
| 47 | [FAPI-MIG-020 — First migration, upgrade, downgrade, current, and history](CURRICULUM.md#fapi-mig-020) | `L` |
| 48 | [FAPI-MIG-030 — Autogenerate review, naming conventions, constraints, indexes, and defaults](CURRICULUM.md#fapi-mig-030) | `XL` |
| 49 | [FAPI-ARC-010 — From a single file to routers and feature modules](CURRICULUM.md#fapi-arc-010) | `L` |
| 50 | [FAPI-ARC-020 — Layered architecture versus vertical slices](CURRICULUM.md#fapi-arc-020) | `L` |
| 51 | [FAPI-ARC-030 — Service layer, functional core, domain services, DTO mapping, and orchestration](CURRICULUM.md#fapi-arc-030) | `L` |
| 52 | [FAPI-ARC-050 — Composition root, dependency inversion, and error translation](CURRICULUM.md#fapi-arc-050) | `L` |
| 53 | [FAPI-ASY-010 — def versus async def, event-loop execution, and thread-pool dispatch](CURRICULUM.md#fapi-asy-010) | `L` |
| 54 | [FAPI-ASY-020 — Blocking I/O, CPU-bound work, worker threads, and process offloading](CURRICULUM.md#fapi-asy-020) | `L` |
| 55 | [FAPI-ASY-030 — Timeouts, cancellation, task groups, and structured concurrency](CURRICULUM.md#fapi-asy-030) | `XL` |
| 56 | [FAPI-ASY-040 — BackgroundTasks versus durable jobs and external workers](CURRICULUM.md#fapi-asy-040) | `L` |
| 57 | [FAPI-ASY-070 — Workers, processes, concurrency limits, pool sizing, and shared state](CURRICULUM.md#fapi-asy-070) | `XL` |
| 58 | [FAPI-SEC-010 — Authentication, authorization, and API threat modelling](CURRICULUM.md#fapi-sec-010) | `L` |
| 59 | [FAPI-SEC-030 — JWT validation, key rotation, access tokens, refresh rotation, and revocation](CURRICULUM.md#fapi-sec-030) | `XL` |
| 60 | [FAPI-SEC-050 — OAuth2 flows, OpenID Connect, external identity providers, and scopes](CURRICULUM.md#fapi-sec-050) | `XL` |
| 61 | [FAPI-SEC-060 — RBAC, ABAC, object-level authorization, and tenant isolation](CURRICULUM.md#fapi-sec-060) | `XL` |
| 62 | [FAPI-SEC-080 — Validation boundaries, mass assignment, SQL injection, SSRF, uploads, and path traversal](CURRICULUM.md#fapi-sec-080) | `XL` |
| 63 | [FAPI-SEC-090 — Rate limits, brute-force controls, replay, idempotency, audit, and sensitive logging](CURRICULUM.md#fapi-sec-090) | `XL` |
| 64 | [FAPI-TST-010 — Testing strategy, observable contracts, and test boundaries](CURRICULUM.md#fapi-tst-010) | `L` |
| 65 | [FAPI-TST-020 — TestClient, HTTPX AsyncClient, ASGI transports, and lifespan-aware tests](CURRICULUM.md#fapi-tst-020) | `L` |
| 66 | [FAPI-TST-030 — Dependency overrides, auth tests, validation errors, and OpenAPI contracts](CURRICULUM.md#fapi-tst-030) | `L` |
| 67 | [FAPI-TST-050 — PostgreSQL integration tests, transaction isolation, fixtures, and factories](CURRICULUM.md#fapi-tst-050) | `XL` |
| 68 | [FAPI-OPS-020 — Uvicorn process model, workers, startup, shutdown, and graceful draining](CURRICULUM.md#fapi-ops-020) | `L` |
| 69 | [FAPI-OPS-030 — Reverse proxies, forwarded headers, root paths, TLS, and trust](CURRICULUM.md#fapi-ops-030) | `L` |
| 70 | [FAPI-OPS-050 — Structured logs, metrics, traces, and request-span propagation](CURRICULUM.md#fapi-ops-050) | `XL` |

### Project milestones

- [FAPI-PRJ-020 — PostgreSQL catalog and ordering service](PROJECTS.md#fapi-prj-020)

<a id="fourteen-day-backend-interview"></a>
## 14-day backend interview preparation

For systematic interview preparation with database, security, async, testing, and architecture depth.

<!-- path-meta: {"slug":"fourteen-day-backend-interview","declared_units":81,"rapid_unit_minutes":[3975,5990],"lab_minutes":[780,1080],"recall_minutes":[360,480],"mock_minutes":[240,360],"checkpoint_minutes":[240,360],"rapid_total_minutes":[5595,8270],"full_mastery_hours":[823,1456],"assumed_prerequisites":[]} -->
| Component | Count or time |
|---|---:|
| Canonical units | 81 |
| Rapid unit study | 66 h 15 min–99 h 50 min |
| Selected practice/labs | 0 checkpoints; 13 h–18 h |
| Recall and comparison | 6 h–8 h |
| Mock interviews | 4 h–6 h |
| Project checkpoints | 4 h–6 h |
| **Rapid path total** | **93 h 15 min–137 h 50 min** |
| Full mastery of included units | 823–1456 h |

### Assumed prior knowledge or prerequisite bridges

None. The path includes its canonical prerequisites.

### Recommended sequence

| # | Unit | Size |
|---:|---|:---:|
| 1 | [FAPI-FND-010 — Python runtime, uv project, and reproducible environment](CURRICULUM.md#fapi-fnd-010) | `M` |
| 2 | [FAPI-FND-020 — Minimal FastAPI application and first route](CURRICULUM.md#fapi-fnd-020) | `S` |
| 3 | [FAPI-FND-030 — Application entry points, import strings, reload, and server startup](CURRICULUM.md#fapi-fnd-030) | `M` |
| 4 | [FAPI-FND-040 — Interactive documentation, OpenAPI inspection, and simple API clients](CURRICULUM.md#fapi-fnd-040) | `S` |
| 5 | [FAPI-FND-050 — Configuration, environment variables, and application factories](CURRICULUM.md#fapi-fnd-050) | `M` |
| 6 | [FAPI-HTTP-010 — HTTP message anatomy, methods, status codes, and media types](CURRICULUM.md#fapi-http-010) | `L` |
| 7 | [FAPI-HTTP-020 — URLs, path/query semantics, request bodies, encoding, and JSON](CURRICULUM.md#fapi-http-020) | `M` |
| 8 | [FAPI-HTTP-030 — Headers, cookies, content negotiation, and representation metadata](CURRICULUM.md#fapi-http-030) | `M` |
| 9 | [FAPI-HTTP-040 — REST resources, actions, RPC-style endpoints, and practical constraints](CURRICULUM.md#fapi-http-040) | `L` |
| 10 | [FAPI-HTTP-050 — Error contracts, RFC problem details, and API versioning](CURRICULUM.md#fapi-http-050) | `L` |
| 11 | [FAPI-HTTP-060 — Pagination, filtering, sorting, and field selection](CURRICULUM.md#fapi-http-060) | `L` |
| 12 | [FAPI-HTTP-070 — Partial updates, idempotency keys, and conditional writes](CURRICULUM.md#fapi-http-070) | `L` |
| 13 | [FAPI-ASGI-010 — WSGI versus ASGI and the protocol boundary](CURRICULUM.md#fapi-asgi-010) | `L` |
| 14 | [FAPI-ASGI-020 — ASGI scope, receive, send, and the HTTP lifecycle](CURRICULUM.md#fapi-asgi-020) | `L` |
| 15 | [FAPI-ASGI-030 — Starlette beneath FastAPI: requests, responses, routing, and exceptions](CURRICULUM.md#fapi-asgi-030) | `L` |
| 16 | [FAPI-ASGI-040 — Lifespan, application state, and resource ownership](CURRICULUM.md#fapi-asgi-040) | `L` |
| 17 | [FAPI-ASGI-050 — ASGI middleware onion, exception flow, and ordering](CURRICULUM.md#fapi-asgi-050) | `L` |
| 18 | [FAPI-ASGI-060 — Client disconnects, cancellation, and streaming lifecycle](CURRICULUM.md#fapi-asgi-060) | `L` |
| 19 | [FAPI-ASGI-070 — ASGI servers, workers, proxy headers, root paths, and mounted applications](CURRICULUM.md#fapi-asgi-070) | `L` |
| 20 | [FAPI-PYD-010 — BaseModel fields: required, optional, nullable, defaults, and factories](CURRICULUM.md#fapi-pyd-010) | `M` |
| 21 | [FAPI-PYD-020 — Coercion, strict validation, constraints, and Annotated](CURRICULUM.md#fapi-pyd-020) | `L` |
| 22 | [FAPI-PYD-030 — Model configuration, extra fields, frozen models, copying, and trusted construction](CURRICULUM.md#fapi-pyd-030) | `L` |
| 23 | [FAPI-PYD-040 — Nested and recursive models, forward annotations, unions, and discriminators](CURRICULUM.md#fapi-pyd-040) | `L` |
| 24 | [FAPI-PYD-060 — Aliases, validation aliases, serialization aliases, and alias generators](CURRICULUM.md#fapi-pyd-060) | `M` |
| 25 | [FAPI-PYD-080 — Serialization, serializers, computed fields, and inclusion or exclusion](CURRICULUM.md#fapi-pyd-080) | `L` |
| 26 | [FAPI-PYD-090 — JSON Schema, OpenAPI interaction, and custom types](CURRICULUM.md#fapi-pyd-090) | `XL` |
| 27 | [FAPI-PYD-100 — Pydantic Settings: source precedence, env files, secrets, nesting, and custom sources](CURRICULUM.md#fapi-pyd-100) | `L` |
| 28 | [FAPI-PYD-110 — Object-attribute validation and model boundaries](CURRICULUM.md#fapi-pyd-110) | `L` |
| 29 | [FAPI-APP-010 — Path operations, router matching, route order, and conflicts](CURRICULUM.md#fapi-app-010) | `M` |
| 30 | [FAPI-APP-020 — Path and query parameters, constraints, aliases, and custom parsing](CURRICULUM.md#fapi-app-020) | `L` |
| 31 | [FAPI-APP-040 — Request bodies, multiple body parameters, embedding, and aliases](CURRICULUM.md#fapi-app-040) | `L` |
| 32 | [FAPI-APP-050 — Forms, multipart data, file uploads, and UploadFile](CURRICULUM.md#fapi-app-050) | `L` |
| 33 | [FAPI-APP-060 — Response models, output validation, serialization, status, headers, and cookies](CURRICULUM.md#fapi-app-060) | `L` |
| 34 | [FAPI-APP-080 — APIRouter, nested routers, tags, operation IDs, and route organization](CURRICULUM.md#fapi-app-080) | `L` |
| 35 | [FAPI-APP-090 — HTTP exceptions, validation errors, custom handlers, and error translation](CURRICULUM.md#fapi-app-090) | `L` |
| 36 | [FAPI-DEP-010 — Callable, class-based, and parameterized dependencies](CURRICULUM.md#fapi-dep-010) | `L` |
| 37 | [FAPI-DEP-020 — Subdependencies and dependency-graph resolution](CURRICULUM.md#fapi-dep-020) | `L` |
| 38 | [FAPI-DEP-040 — Yield dependencies, setup/teardown order, scopes, and resource safety](CURRICULUM.md#fapi-dep-040) | `XL` |
| 39 | [FAPI-DEP-050 — Authentication and authorization dependencies](CURRICULUM.md#fapi-dep-050) | `L` |
| 40 | [FAPI-DEP-060 — Router/global dependencies and test overrides](CURRICULUM.md#fapi-dep-060) | `L` |
| 41 | [FAPI-DEP-070 — Request state, composition roots, service location, and dependency boundaries](CURRICULUM.md#fapi-dep-070) | `XL` |
| 42 | [FAPI-MID-010 — Function, class-based, and raw ASGI middleware ordering](CURRICULUM.md#fapi-mid-010) | `L` |
| 43 | [FAPI-MID-020 — Request IDs, structured logging, context variables, and correlation](CURRICULUM.md#fapi-mid-020) | `L` |
| 44 | [FAPI-MID-050 — Rate limiting, observability, and choosing middleware versus dependencies](CURRICULUM.md#fapi-mid-050) | `L` |
| 45 | [FAPI-DB-010 — Relational modelling and PostgreSQL constraints for APIs](CURRICULUM.md#fapi-db-010) | `L` |
| 46 | [FAPI-DB-020 — PostgreSQL drivers, SQLAlchemy engines, URLs, and connection pools](CURRICULUM.md#fapi-db-020) | `L` |
| 47 | [FAPI-DB-030 — SQLAlchemy typed declarative mappings, columns, and constraints](CURRICULUM.md#fapi-db-030) | `L` |
| 48 | [FAPI-DB-040 — Session per request, identity map, and unit-of-work lifecycle](CURRICULUM.md#fapi-db-040) | `XL` |
| 49 | [FAPI-DB-050 — Transactions, flush, commit, rollback, refresh, expiration, and savepoints](CURRICULUM.md#fapi-db-050) | `XL` |
| 50 | [FAPI-DB-060 — Relationships, cascades, eager/lazy loading, and object graphs](CURRICULUM.md#fapi-db-060) | `L` |
| 51 | [FAPI-DB-080 — Queries, joins, aggregates, filtering, sorting, and pagination](CURRICULUM.md#fapi-db-080) | `L` |
| 52 | [FAPI-DB-090 — N+1 diagnosis, eager loading, query plans, and indexes](CURRICULUM.md#fapi-db-090) | `XL` |
| 53 | [FAPI-DB-100 — Locking, isolation levels, deadlocks, retries, and optimistic concurrency](CURRICULUM.md#fapi-db-100) | `XL` |
| 54 | [FAPI-DB-110 — Bulk work, generated values, timestamps, soft deletion, and tenant boundaries](CURRICULUM.md#fapi-db-110) | `L` |
| 55 | [FAPI-MIG-010 — Alembic environment, configuration, metadata discovery, and revision graph](CURRICULUM.md#fapi-mig-010) | `L` |
| 56 | [FAPI-MIG-020 — First migration, upgrade, downgrade, current, and history](CURRICULUM.md#fapi-mig-020) | `L` |
| 57 | [FAPI-MIG-030 — Autogenerate review, naming conventions, constraints, indexes, and defaults](CURRICULUM.md#fapi-mig-030) | `XL` |
| 58 | [FAPI-ARC-010 — From a single file to routers and feature modules](CURRICULUM.md#fapi-arc-010) | `L` |
| 59 | [FAPI-ARC-020 — Layered architecture versus vertical slices](CURRICULUM.md#fapi-arc-020) | `L` |
| 60 | [FAPI-ARC-030 — Service layer, functional core, domain services, DTO mapping, and orchestration](CURRICULUM.md#fapi-arc-030) | `L` |
| 61 | [FAPI-ARC-050 — Composition root, dependency inversion, and error translation](CURRICULUM.md#fapi-arc-050) | `L` |
| 62 | [FAPI-ASY-010 — def versus async def, event-loop execution, and thread-pool dispatch](CURRICULUM.md#fapi-asy-010) | `L` |
| 63 | [FAPI-ASY-030 — Timeouts, cancellation, task groups, and structured concurrency](CURRICULUM.md#fapi-asy-030) | `XL` |
| 64 | [FAPI-ASY-070 — Workers, processes, concurrency limits, pool sizing, and shared state](CURRICULUM.md#fapi-asy-070) | `XL` |
| 65 | [FAPI-ASY-090 — Profiling, load testing, benchmarking, and evidence-led performance diagnosis](CURRICULUM.md#fapi-asy-090) | `XL` |
| 66 | [FAPI-SEC-010 — Authentication, authorization, and API threat modelling](CURRICULUM.md#fapi-sec-010) | `L` |
| 67 | [FAPI-SEC-060 — RBAC, ABAC, object-level authorization, and tenant isolation](CURRICULUM.md#fapi-sec-060) | `XL` |
| 68 | [FAPI-SEC-080 — Validation boundaries, mass assignment, SQL injection, SSRF, uploads, and path traversal](CURRICULUM.md#fapi-sec-080) | `XL` |
| 69 | [FAPI-SEC-090 — Rate limits, brute-force controls, replay, idempotency, audit, and sensitive logging](CURRICULUM.md#fapi-sec-090) | `XL` |
| 70 | [FAPI-SEC-100 — Secrets, dependency vulnerabilities, authorization tests, and security review](CURRICULUM.md#fapi-sec-100) | `L` |
| 71 | [FAPI-RT-010 — REST, RPC, streaming, events, GraphQL, and gRPC boundaries](CURRICULUM.md#fapi-rt-010) | `L` |
| 72 | [FAPI-RT-080 — gRPC foundations: Protocol Buffers, code generation, unary calls, status, and metadata](CURRICULUM.md#fapi-rt-080) | `XL` |
| 73 | [FAPI-RT-090 — gRPC streaming, deadlines, cancellation, interceptors, auth, evolution, and gateways](CURRICULUM.md#fapi-rt-090) | `XL` |
| 74 | [FAPI-TST-010 — Testing strategy, observable contracts, and test boundaries](CURRICULUM.md#fapi-tst-010) | `L` |
| 75 | [FAPI-TST-020 — TestClient, HTTPX AsyncClient, ASGI transports, and lifespan-aware tests](CURRICULUM.md#fapi-tst-020) | `L` |
| 76 | [FAPI-TST-030 — Dependency overrides, auth tests, validation errors, and OpenAPI contracts](CURRICULUM.md#fapi-tst-030) | `L` |
| 77 | [FAPI-TST-080 — Timeout, retry, concurrency, load, performance, and security-focused tests](CURRICULUM.md#fapi-tst-080) | `XL` |
| 78 | [FAPI-OPS-020 — Uvicorn process model, workers, startup, shutdown, and graceful draining](CURRICULUM.md#fapi-ops-020) | `L` |
| 79 | [FAPI-OPS-050 — Structured logs, metrics, traces, and request-span propagation](CURRICULUM.md#fapi-ops-050) | `XL` |
| 80 | [FAPI-OPS-060 — Capacity planning, worker/pool limits, load tests, and performance budgets](CURRICULUM.md#fapi-ops-060) | `XL` |
| 81 | [FAPI-SYN-040 — Async, security, real-time, performance, and production design synthesis](CURRICULUM.md#fapi-syn-040) | `XL` |

### Project milestones

- [FAPI-PRJ-020 — PostgreSQL catalog and ordering service](PROJECTS.md#fapi-prj-020)
- [FAPI-PRJ-030 — Authenticated multi-tenant service](PROJECTS.md#fapi-prj-030)

<a id="thirty-day-production-foundation"></a>
## 30-day production foundation

For building a strong production baseline at roughly three to five focused hours per day.

<!-- path-meta: {"slug":"thirty-day-production-foundation","declared_units":93,"rapid_unit_minutes":[4715,7070],"lab_minutes":[1200,1800],"recall_minutes":[480,720],"mock_minutes":[300,480],"checkpoint_minutes":[360,540],"rapid_total_minutes":[7055,10610],"full_mastery_hours":[987,1744],"assumed_prerequisites":[]} -->
| Component | Count or time |
|---|---:|
| Canonical units | 93 |
| Rapid unit study | 78 h 35 min–117 h 50 min |
| Selected practice/labs | 0 checkpoints; 20 h–30 h |
| Recall and comparison | 8 h–12 h |
| Mock interviews | 5 h–8 h |
| Project checkpoints | 6 h–9 h |
| **Rapid path total** | **117 h 35 min–176 h 50 min** |
| Full mastery of included units | 987–1744 h |

### Assumed prior knowledge or prerequisite bridges

None. The path includes its canonical prerequisites.

### Recommended sequence

| # | Unit | Size |
|---:|---|:---:|
| 1 | [FAPI-FND-010 — Python runtime, uv project, and reproducible environment](CURRICULUM.md#fapi-fnd-010) | `M` |
| 2 | [FAPI-FND-020 — Minimal FastAPI application and first route](CURRICULUM.md#fapi-fnd-020) | `S` |
| 3 | [FAPI-FND-030 — Application entry points, import strings, reload, and server startup](CURRICULUM.md#fapi-fnd-030) | `M` |
| 4 | [FAPI-FND-040 — Interactive documentation, OpenAPI inspection, and simple API clients](CURRICULUM.md#fapi-fnd-040) | `S` |
| 5 | [FAPI-FND-050 — Configuration, environment variables, and application factories](CURRICULUM.md#fapi-fnd-050) | `M` |
| 6 | [FAPI-HTTP-010 — HTTP message anatomy, methods, status codes, and media types](CURRICULUM.md#fapi-http-010) | `L` |
| 7 | [FAPI-HTTP-020 — URLs, path/query semantics, request bodies, encoding, and JSON](CURRICULUM.md#fapi-http-020) | `M` |
| 8 | [FAPI-HTTP-030 — Headers, cookies, content negotiation, and representation metadata](CURRICULUM.md#fapi-http-030) | `M` |
| 9 | [FAPI-HTTP-040 — REST resources, actions, RPC-style endpoints, and practical constraints](CURRICULUM.md#fapi-http-040) | `L` |
| 10 | [FAPI-HTTP-050 — Error contracts, RFC problem details, and API versioning](CURRICULUM.md#fapi-http-050) | `L` |
| 11 | [FAPI-HTTP-060 — Pagination, filtering, sorting, and field selection](CURRICULUM.md#fapi-http-060) | `L` |
| 12 | [FAPI-HTTP-070 — Partial updates, idempotency keys, and conditional writes](CURRICULUM.md#fapi-http-070) | `L` |
| 13 | [FAPI-ASGI-010 — WSGI versus ASGI and the protocol boundary](CURRICULUM.md#fapi-asgi-010) | `L` |
| 14 | [FAPI-ASGI-020 — ASGI scope, receive, send, and the HTTP lifecycle](CURRICULUM.md#fapi-asgi-020) | `L` |
| 15 | [FAPI-ASGI-030 — Starlette beneath FastAPI: requests, responses, routing, and exceptions](CURRICULUM.md#fapi-asgi-030) | `L` |
| 16 | [FAPI-ASGI-040 — Lifespan, application state, and resource ownership](CURRICULUM.md#fapi-asgi-040) | `L` |
| 17 | [FAPI-ASGI-050 — ASGI middleware onion, exception flow, and ordering](CURRICULUM.md#fapi-asgi-050) | `L` |
| 18 | [FAPI-ASGI-060 — Client disconnects, cancellation, and streaming lifecycle](CURRICULUM.md#fapi-asgi-060) | `L` |
| 19 | [FAPI-ASGI-070 — ASGI servers, workers, proxy headers, root paths, and mounted applications](CURRICULUM.md#fapi-asgi-070) | `L` |
| 20 | [FAPI-PYD-010 — BaseModel fields: required, optional, nullable, defaults, and factories](CURRICULUM.md#fapi-pyd-010) | `M` |
| 21 | [FAPI-PYD-020 — Coercion, strict validation, constraints, and Annotated](CURRICULUM.md#fapi-pyd-020) | `L` |
| 22 | [FAPI-PYD-030 — Model configuration, extra fields, frozen models, copying, and trusted construction](CURRICULUM.md#fapi-pyd-030) | `L` |
| 23 | [FAPI-PYD-040 — Nested and recursive models, forward annotations, unions, and discriminators](CURRICULUM.md#fapi-pyd-040) | `L` |
| 24 | [FAPI-PYD-060 — Aliases, validation aliases, serialization aliases, and alias generators](CURRICULUM.md#fapi-pyd-060) | `M` |
| 25 | [FAPI-PYD-080 — Serialization, serializers, computed fields, and inclusion or exclusion](CURRICULUM.md#fapi-pyd-080) | `L` |
| 26 | [FAPI-PYD-090 — JSON Schema, OpenAPI interaction, and custom types](CURRICULUM.md#fapi-pyd-090) | `XL` |
| 27 | [FAPI-PYD-100 — Pydantic Settings: source precedence, env files, secrets, nesting, and custom sources](CURRICULUM.md#fapi-pyd-100) | `L` |
| 28 | [FAPI-PYD-110 — Object-attribute validation and model boundaries](CURRICULUM.md#fapi-pyd-110) | `L` |
| 29 | [FAPI-APP-010 — Path operations, router matching, route order, and conflicts](CURRICULUM.md#fapi-app-010) | `M` |
| 30 | [FAPI-APP-020 — Path and query parameters, constraints, aliases, and custom parsing](CURRICULUM.md#fapi-app-020) | `L` |
| 31 | [FAPI-APP-040 — Request bodies, multiple body parameters, embedding, and aliases](CURRICULUM.md#fapi-app-040) | `L` |
| 32 | [FAPI-APP-050 — Forms, multipart data, file uploads, and UploadFile](CURRICULUM.md#fapi-app-050) | `L` |
| 33 | [FAPI-APP-060 — Response models, output validation, serialization, status, headers, and cookies](CURRICULUM.md#fapi-app-060) | `L` |
| 34 | [FAPI-APP-080 — APIRouter, nested routers, tags, operation IDs, and route organization](CURRICULUM.md#fapi-app-080) | `L` |
| 35 | [FAPI-APP-090 — HTTP exceptions, validation errors, custom handlers, and error translation](CURRICULUM.md#fapi-app-090) | `L` |
| 36 | [FAPI-DEP-010 — Callable, class-based, and parameterized dependencies](CURRICULUM.md#fapi-dep-010) | `L` |
| 37 | [FAPI-DEP-020 — Subdependencies and dependency-graph resolution](CURRICULUM.md#fapi-dep-020) | `L` |
| 38 | [FAPI-DEP-040 — Yield dependencies, setup/teardown order, scopes, and resource safety](CURRICULUM.md#fapi-dep-040) | `XL` |
| 39 | [FAPI-DEP-050 — Authentication and authorization dependencies](CURRICULUM.md#fapi-dep-050) | `L` |
| 40 | [FAPI-DEP-060 — Router/global dependencies and test overrides](CURRICULUM.md#fapi-dep-060) | `L` |
| 41 | [FAPI-DEP-070 — Request state, composition roots, service location, and dependency boundaries](CURRICULUM.md#fapi-dep-070) | `XL` |
| 42 | [FAPI-MID-010 — Function, class-based, and raw ASGI middleware ordering](CURRICULUM.md#fapi-mid-010) | `L` |
| 43 | [FAPI-MID-020 — Request IDs, structured logging, context variables, and correlation](CURRICULUM.md#fapi-mid-020) | `L` |
| 44 | [FAPI-MID-030 — CORS, trusted hosts, HTTPS redirects, compression, and sessions](CURRICULUM.md#fapi-mid-030) | `L` |
| 45 | [FAPI-MID-050 — Rate limiting, observability, and choosing middleware versus dependencies](CURRICULUM.md#fapi-mid-050) | `L` |
| 46 | [FAPI-DB-010 — Relational modelling and PostgreSQL constraints for APIs](CURRICULUM.md#fapi-db-010) | `L` |
| 47 | [FAPI-DB-020 — PostgreSQL drivers, SQLAlchemy engines, URLs, and connection pools](CURRICULUM.md#fapi-db-020) | `L` |
| 48 | [FAPI-DB-030 — SQLAlchemy typed declarative mappings, columns, and constraints](CURRICULUM.md#fapi-db-030) | `L` |
| 49 | [FAPI-DB-040 — Session per request, identity map, and unit-of-work lifecycle](CURRICULUM.md#fapi-db-040) | `XL` |
| 50 | [FAPI-DB-050 — Transactions, flush, commit, rollback, refresh, expiration, and savepoints](CURRICULUM.md#fapi-db-050) | `XL` |
| 51 | [FAPI-DB-060 — Relationships, cascades, eager/lazy loading, and object graphs](CURRICULUM.md#fapi-db-060) | `L` |
| 52 | [FAPI-DB-070 — AsyncEngine, AsyncSession, and preventing implicit I/O](CURRICULUM.md#fapi-db-070) | `XL` |
| 53 | [FAPI-DB-080 — Queries, joins, aggregates, filtering, sorting, and pagination](CURRICULUM.md#fapi-db-080) | `L` |
| 54 | [FAPI-DB-090 — N+1 diagnosis, eager loading, query plans, and indexes](CURRICULUM.md#fapi-db-090) | `XL` |
| 55 | [FAPI-DB-100 — Locking, isolation levels, deadlocks, retries, and optimistic concurrency](CURRICULUM.md#fapi-db-100) | `XL` |
| 56 | [FAPI-DB-110 — Bulk work, generated values, timestamps, soft deletion, and tenant boundaries](CURRICULUM.md#fapi-db-110) | `L` |
| 57 | [FAPI-DB-120 — Database test isolation, mapping boundaries, repositories, and direct SQLAlchemy](CURRICULUM.md#fapi-db-120) | `XL` |
| 58 | [FAPI-MIG-010 — Alembic environment, configuration, metadata discovery, and revision graph](CURRICULUM.md#fapi-mig-010) | `L` |
| 59 | [FAPI-MIG-020 — First migration, upgrade, downgrade, current, and history](CURRICULUM.md#fapi-mig-020) | `L` |
| 60 | [FAPI-MIG-030 — Autogenerate review, naming conventions, constraints, indexes, and defaults](CURRICULUM.md#fapi-mig-030) | `XL` |
| 61 | [FAPI-MIG-040 — Data migrations, backfills, enum changes, and offline SQL](CURRICULUM.md#fapi-mig-040) | `XL` |
| 62 | [FAPI-MIG-060 — Async application integration, migration testing, and drift detection](CURRICULUM.md#fapi-mig-060) | `L` |
| 63 | [FAPI-MIG-070 — Expand-and-contract changes, locks, compatibility windows, and rollback decisions](CURRICULUM.md#fapi-mig-070) | `XL` |
| 64 | [FAPI-ARC-010 — From a single file to routers and feature modules](CURRICULUM.md#fapi-arc-010) | `L` |
| 65 | [FAPI-ARC-020 — Layered architecture versus vertical slices](CURRICULUM.md#fapi-arc-020) | `L` |
| 66 | [FAPI-ARC-030 — Service layer, functional core, domain services, DTO mapping, and orchestration](CURRICULUM.md#fapi-arc-030) | `L` |
| 67 | [FAPI-ARC-040 — Repository and Unit of Work patterns with transaction ownership](CURRICULUM.md#fapi-arc-040) | `XL` |
| 68 | [FAPI-ARC-070 — Multi-tenancy, gateway boundaries, monolith/microservice choices, and stopping rules](CURRICULUM.md#fapi-arc-070) | `XL` |
| 69 | [FAPI-ASY-010 — def versus async def, event-loop execution, and thread-pool dispatch](CURRICULUM.md#fapi-asy-010) | `L` |
| 70 | [FAPI-ASY-030 — Timeouts, cancellation, task groups, and structured concurrency](CURRICULUM.md#fapi-asy-030) | `XL` |
| 71 | [FAPI-ASY-070 — Workers, processes, concurrency limits, pool sizing, and shared state](CURRICULUM.md#fapi-asy-070) | `XL` |
| 72 | [FAPI-ASY-090 — Profiling, load testing, benchmarking, and evidence-led performance diagnosis](CURRICULUM.md#fapi-asy-090) | `XL` |
| 73 | [FAPI-SEC-010 — Authentication, authorization, and API threat modelling](CURRICULUM.md#fapi-sec-010) | `L` |
| 74 | [FAPI-SEC-060 — RBAC, ABAC, object-level authorization, and tenant isolation](CURRICULUM.md#fapi-sec-060) | `XL` |
| 75 | [FAPI-SEC-070 — CORS, trusted hosts, HTTPS, proxy trust, and security headers](CURRICULUM.md#fapi-sec-070) | `L` |
| 76 | [FAPI-SEC-080 — Validation boundaries, mass assignment, SQL injection, SSRF, uploads, and path traversal](CURRICULUM.md#fapi-sec-080) | `XL` |
| 77 | [FAPI-SEC-090 — Rate limits, brute-force controls, replay, idempotency, audit, and sensitive logging](CURRICULUM.md#fapi-sec-090) | `XL` |
| 78 | [FAPI-SEC-100 — Secrets, dependency vulnerabilities, authorization tests, and security review](CURRICULUM.md#fapi-sec-100) | `L` |
| 79 | [FAPI-RT-010 — REST, RPC, streaming, events, GraphQL, and gRPC boundaries](CURRICULUM.md#fapi-rt-010) | `L` |
| 80 | [FAPI-RT-040 — WebSocket handshake, connection lifetime, receive/send loops, and disconnects](CURRICULUM.md#fapi-rt-040) | `L` |
| 81 | [FAPI-RT-050 — WebSocket managers, broadcast, heartbeats, auth, backpressure, and scaling](CURRICULUM.md#fapi-rt-050) | `XL` |
| 82 | [FAPI-RT-080 — gRPC foundations: Protocol Buffers, code generation, unary calls, status, and metadata](CURRICULUM.md#fapi-rt-080) | `XL` |
| 83 | [FAPI-RT-090 — gRPC streaming, deadlines, cancellation, interceptors, auth, evolution, and gateways](CURRICULUM.md#fapi-rt-090) | `XL` |
| 84 | [FAPI-TST-010 — Testing strategy, observable contracts, and test boundaries](CURRICULUM.md#fapi-tst-010) | `L` |
| 85 | [FAPI-TST-020 — TestClient, HTTPX AsyncClient, ASGI transports, and lifespan-aware tests](CURRICULUM.md#fapi-tst-020) | `L` |
| 86 | [FAPI-TST-030 — Dependency overrides, auth tests, validation errors, and OpenAPI contracts](CURRICULUM.md#fapi-tst-030) | `L` |
| 87 | [FAPI-TST-080 — Timeout, retry, concurrency, load, performance, and security-focused tests](CURRICULUM.md#fapi-tst-080) | `XL` |
| 88 | [FAPI-OPS-020 — Uvicorn process model, workers, startup, shutdown, and graceful draining](CURRICULUM.md#fapi-ops-020) | `L` |
| 89 | [FAPI-OPS-030 — Reverse proxies, forwarded headers, root paths, TLS, and trust](CURRICULUM.md#fapi-ops-030) | `L` |
| 90 | [FAPI-OPS-050 — Structured logs, metrics, traces, and request-span propagation](CURRICULUM.md#fapi-ops-050) | `XL` |
| 91 | [FAPI-OPS-060 — Capacity planning, worker/pool limits, load tests, and performance budgets](CURRICULUM.md#fapi-ops-060) | `XL` |
| 92 | [FAPI-OPS-070 — Production debugging, incident response, deployment strategies, and rollback](CURRICULUM.md#fapi-ops-070) | `XL` |
| 93 | [FAPI-SYN-040 — Async, security, real-time, performance, and production design synthesis](CURRICULUM.md#fapi-syn-040) | `XL` |

### Project milestones

- [FAPI-PRJ-030 — Authenticated multi-tenant service](PROJECTS.md#fapi-prj-030)
- [FAPI-PRJ-040 — Synthetic review and workflow platform](PROJECTS.md#fapi-prj-040)
- [FAPI-PRJ-060 — Real-time operations dashboard](PROJECTS.md#fapi-prj-060)

<a id="ninety-day-fastapi-mastery"></a>
## 90-day FastAPI mastery

This route provides rapid-breadth coverage of all 156 canonical units. Complete FastAPI mastery uses the same complete knowledge surface, but demands substantially deeper practice, projects, experiments, delayed recall, and transfer evidence.

<!-- path-meta: {"slug":"ninety-day-fastapi-mastery","declared_units":156,"rapid_unit_minutes":[8355,12425],"lab_minutes":[4200,6300],"recall_minutes":[1200,1800],"mock_minutes":[660,1020],"checkpoint_minutes":[1320,1980],"rapid_total_minutes":[15735,23525],"full_mastery_hours":[1780,3139],"assumed_prerequisites":[]} -->
| Component | Count or time |
|---|---:|
| Canonical units | 156 |
| Rapid unit study | 139 h 15 min–207 h 5 min |
| Selected practice/labs | 70 h–105 h |
| Recall and comparison | 20 h–30 h |
| Mock interviews | 11 h–17 h |
| Project checkpoints | 22 h–33 h |
| **Rapid path total** | **262 h 15 min–392 h 5 min** |
| Full mastery of included units | 1,780–3,139 h |

### Assumed prior knowledge or prerequisite bridges

None. The path includes its canonical prerequisites.

### Recommended sequence

| # | Unit | Size |
|---:|---|:---:|
| 1 | [FAPI-FND-010 — Python runtime, uv project, and reproducible environment](CURRICULUM.md#fapi-fnd-010) | `M` |
| 2 | [FAPI-FND-020 — Minimal FastAPI application and first route](CURRICULUM.md#fapi-fnd-020) | `S` |
| 3 | [FAPI-FND-030 — Application entry points, import strings, reload, and server startup](CURRICULUM.md#fapi-fnd-030) | `M` |
| 4 | [FAPI-FND-040 — Interactive documentation, OpenAPI inspection, and simple API clients](CURRICULUM.md#fapi-fnd-040) | `S` |
| 5 | [FAPI-FND-050 — Configuration, environment variables, and application factories](CURRICULUM.md#fapi-fnd-050) | `M` |
| 6 | [FAPI-FND-060 — Startup, import, reload, and configuration failure diagnosis](CURRICULUM.md#fapi-fnd-060) | `M` |
| 7 | [FAPI-HTTP-010 — HTTP message anatomy, methods, status codes, and media types](CURRICULUM.md#fapi-http-010) | `L` |
| 8 | [FAPI-HTTP-020 — URLs, path/query semantics, request bodies, encoding, and JSON](CURRICULUM.md#fapi-http-020) | `M` |
| 9 | [FAPI-HTTP-030 — Headers, cookies, content negotiation, and representation metadata](CURRICULUM.md#fapi-http-030) | `M` |
| 10 | [FAPI-HTTP-040 — REST resources, actions, RPC-style endpoints, and practical constraints](CURRICULUM.md#fapi-http-040) | `L` |
| 11 | [FAPI-HTTP-050 — Error contracts, RFC problem details, and API versioning](CURRICULUM.md#fapi-http-050) | `L` |
| 12 | [FAPI-HTTP-060 — Pagination, filtering, sorting, and field selection](CURRICULUM.md#fapi-http-060) | `L` |
| 13 | [FAPI-HTTP-070 — Partial updates, idempotency keys, and conditional writes](CURRICULUM.md#fapi-http-070) | `L` |
| 14 | [FAPI-HTTP-080 — Caching, ETags, conditional requests, redirects, and range responses](CURRICULUM.md#fapi-http-080) | `L` |
| 15 | [FAPI-ASGI-010 — WSGI versus ASGI and the protocol boundary](CURRICULUM.md#fapi-asgi-010) | `L` |
| 16 | [FAPI-ASGI-020 — ASGI scope, receive, send, and the HTTP lifecycle](CURRICULUM.md#fapi-asgi-020) | `L` |
| 17 | [FAPI-ASGI-030 — Starlette beneath FastAPI: requests, responses, routing, and exceptions](CURRICULUM.md#fapi-asgi-030) | `L` |
| 18 | [FAPI-ASGI-040 — Lifespan, application state, and resource ownership](CURRICULUM.md#fapi-asgi-040) | `L` |
| 19 | [FAPI-ASGI-050 — ASGI middleware onion, exception flow, and ordering](CURRICULUM.md#fapi-asgi-050) | `L` |
| 20 | [FAPI-ASGI-060 — Client disconnects, cancellation, and streaming lifecycle](CURRICULUM.md#fapi-asgi-060) | `L` |
| 21 | [FAPI-ASGI-070 — ASGI servers, workers, proxy headers, root paths, and mounted applications](CURRICULUM.md#fapi-asgi-070) | `L` |
| 22 | [FAPI-PYD-010 — BaseModel fields: required, optional, nullable, defaults, and factories](CURRICULUM.md#fapi-pyd-010) | `M` |
| 23 | [FAPI-PYD-020 — Coercion, strict validation, constraints, and Annotated](CURRICULUM.md#fapi-pyd-020) | `L` |
| 24 | [FAPI-PYD-030 — Model configuration, extra fields, frozen models, copying, and trusted construction](CURRICULUM.md#fapi-pyd-030) | `L` |
| 25 | [FAPI-PYD-040 — Nested and recursive models, forward annotations, unions, and discriminators](CURRICULUM.md#fapi-pyd-040) | `L` |
| 26 | [FAPI-PYD-050 — Generics, RootModel, TypeAdapter, and Pydantic dataclasses](CURRICULUM.md#fapi-pyd-050) | `L` |
| 27 | [FAPI-PYD-060 — Aliases, validation aliases, serialization aliases, and alias generators](CURRICULUM.md#fapi-pyd-060) | `M` |
| 28 | [FAPI-PYD-070 — Field and model validators: modes, ordering, context, and defaults](CURRICULUM.md#fapi-pyd-070) | `XL` |
| 29 | [FAPI-PYD-080 — Serialization, serializers, computed fields, and inclusion or exclusion](CURRICULUM.md#fapi-pyd-080) | `L` |
| 30 | [FAPI-PYD-090 — JSON Schema, OpenAPI interaction, and custom types](CURRICULUM.md#fapi-pyd-090) | `XL` |
| 31 | [FAPI-PYD-100 — Pydantic Settings: source precedence, env files, secrets, nesting, and custom sources](CURRICULUM.md#fapi-pyd-100) | `L` |
| 32 | [FAPI-PYD-110 — Object-attribute validation and model boundaries](CURRICULUM.md#fapi-pyd-110) | `L` |
| 33 | [FAPI-PYD-120 — Pydantic performance, validator side effects, v1-to-v2 migration, and common mistakes](CURRICULUM.md#fapi-pyd-120) | `XL` |
| 34 | [FAPI-APP-010 — Path operations, router matching, route order, and conflicts](CURRICULUM.md#fapi-app-010) | `M` |
| 35 | [FAPI-APP-020 — Path and query parameters, constraints, aliases, and custom parsing](CURRICULUM.md#fapi-app-020) | `L` |
| 36 | [FAPI-APP-030 — Headers, cookies, custom parameter types, and direct Request access](CURRICULUM.md#fapi-app-030) | `M` |
| 37 | [FAPI-APP-040 — Request bodies, multiple body parameters, embedding, and aliases](CURRICULUM.md#fapi-app-040) | `L` |
| 38 | [FAPI-APP-050 — Forms, multipart data, file uploads, and UploadFile](CURRICULUM.md#fapi-app-050) | `L` |
| 39 | [FAPI-APP-060 — Response models, output validation, serialization, status, headers, and cookies](CURRICULUM.md#fapi-app-060) | `L` |
| 40 | [FAPI-APP-070 — Response classes, redirects, files, and streaming responses](CURRICULUM.md#fapi-app-070) | `L` |
| 41 | [FAPI-APP-080 — APIRouter, nested routers, tags, operation IDs, and route organization](CURRICULUM.md#fapi-app-080) | `L` |
| 42 | [FAPI-APP-090 — HTTP exceptions, validation errors, custom handlers, and error translation](CURRICULUM.md#fapi-app-090) | `L` |
| 43 | [FAPI-APP-100 — OpenAPI metadata, examples, callbacks, webhooks, and schema quality](CURRICULUM.md#fapi-app-100) | `L` |
| 44 | [FAPI-DEP-010 — Callable, class-based, and parameterized dependencies](CURRICULUM.md#fapi-dep-010) | `L` |
| 45 | [FAPI-DEP-020 — Subdependencies and dependency-graph resolution](CURRICULUM.md#fapi-dep-020) | `L` |
| 46 | [FAPI-DEP-030 — Per-request dependency caching and use_cache](CURRICULUM.md#fapi-dep-030) | `M` |
| 47 | [FAPI-DEP-040 — Yield dependencies, setup/teardown order, scopes, and resource safety](CURRICULUM.md#fapi-dep-040) | `XL` |
| 48 | [FAPI-DEP-050 — Authentication and authorization dependencies](CURRICULUM.md#fapi-dep-050) | `L` |
| 49 | [FAPI-DEP-060 — Router/global dependencies and test overrides](CURRICULUM.md#fapi-dep-060) | `L` |
| 50 | [FAPI-DEP-070 — Request state, composition roots, service location, and dependency boundaries](CURRICULUM.md#fapi-dep-070) | `XL` |
| 51 | [FAPI-MID-010 — Function, class-based, and raw ASGI middleware ordering](CURRICULUM.md#fapi-mid-010) | `L` |
| 52 | [FAPI-MID-020 — Request IDs, structured logging, context variables, and correlation](CURRICULUM.md#fapi-mid-020) | `L` |
| 53 | [FAPI-MID-030 — CORS, trusted hosts, HTTPS redirects, compression, and sessions](CURRICULUM.md#fapi-mid-030) | `L` |
| 54 | [FAPI-MID-040 — Body consumption, exception behavior, and cancellation in middleware](CURRICULUM.md#fapi-mid-040) | `XL` |
| 55 | [FAPI-MID-050 — Rate limiting, observability, and choosing middleware versus dependencies](CURRICULUM.md#fapi-mid-050) | `L` |
| 56 | [FAPI-DB-010 — Relational modelling and PostgreSQL constraints for APIs](CURRICULUM.md#fapi-db-010) | `L` |
| 57 | [FAPI-DB-020 — PostgreSQL drivers, SQLAlchemy engines, URLs, and connection pools](CURRICULUM.md#fapi-db-020) | `L` |
| 58 | [FAPI-DB-030 — SQLAlchemy typed declarative mappings, columns, and constraints](CURRICULUM.md#fapi-db-030) | `L` |
| 59 | [FAPI-DB-040 — Session per request, identity map, and unit-of-work lifecycle](CURRICULUM.md#fapi-db-040) | `XL` |
| 60 | [FAPI-DB-050 — Transactions, flush, commit, rollback, refresh, expiration, and savepoints](CURRICULUM.md#fapi-db-050) | `XL` |
| 61 | [FAPI-DB-060 — Relationships, cascades, eager/lazy loading, and object graphs](CURRICULUM.md#fapi-db-060) | `L` |
| 62 | [FAPI-DB-070 — AsyncEngine, AsyncSession, and preventing implicit I/O](CURRICULUM.md#fapi-db-070) | `XL` |
| 63 | [FAPI-DB-080 — Queries, joins, aggregates, filtering, sorting, and pagination](CURRICULUM.md#fapi-db-080) | `L` |
| 64 | [FAPI-DB-090 — N+1 diagnosis, eager loading, query plans, and indexes](CURRICULUM.md#fapi-db-090) | `XL` |
| 65 | [FAPI-DB-100 — Locking, isolation levels, deadlocks, retries, and optimistic concurrency](CURRICULUM.md#fapi-db-100) | `XL` |
| 66 | [FAPI-DB-110 — Bulk work, generated values, timestamps, soft deletion, and tenant boundaries](CURRICULUM.md#fapi-db-110) | `L` |
| 67 | [FAPI-DB-120 — Database test isolation, mapping boundaries, repositories, and direct SQLAlchemy](CURRICULUM.md#fapi-db-120) | `XL` |
| 68 | [FAPI-MIG-010 — Alembic environment, configuration, metadata discovery, and revision graph](CURRICULUM.md#fapi-mig-010) | `L` |
| 69 | [FAPI-MIG-020 — First migration, upgrade, downgrade, current, and history](CURRICULUM.md#fapi-mig-020) | `L` |
| 70 | [FAPI-MIG-030 — Autogenerate review, naming conventions, constraints, indexes, and defaults](CURRICULUM.md#fapi-mig-030) | `XL` |
| 71 | [FAPI-MIG-040 — Data migrations, backfills, enum changes, and offline SQL](CURRICULUM.md#fapi-mig-040) | `XL` |
| 72 | [FAPI-MIG-050 — Migration branches, multiple heads, merge revisions, and conflicts](CURRICULUM.md#fapi-mig-050) | `L` |
| 73 | [FAPI-MIG-060 — Async application integration, migration testing, and drift detection](CURRICULUM.md#fapi-mig-060) | `L` |
| 74 | [FAPI-MIG-070 — Expand-and-contract changes, locks, compatibility windows, and rollback decisions](CURRICULUM.md#fapi-mig-070) | `XL` |
| 75 | [FAPI-ARC-010 — From a single file to routers and feature modules](CURRICULUM.md#fapi-arc-010) | `L` |
| 76 | [FAPI-ARC-020 — Layered architecture versus vertical slices](CURRICULUM.md#fapi-arc-020) | `L` |
| 77 | [FAPI-ARC-030 — Service layer, functional core, domain services, DTO mapping, and orchestration](CURRICULUM.md#fapi-arc-030) | `L` |
| 78 | [FAPI-ARC-040 — Repository and Unit of Work patterns with transaction ownership](CURRICULUM.md#fapi-arc-040) | `XL` |
| 79 | [FAPI-ARC-050 — Composition root, dependency inversion, and error translation](CURRICULUM.md#fapi-arc-050) | `L` |
| 80 | [FAPI-ARC-060 — Modular monolith boundaries, circular imports, and plugin extension points](CURRICULUM.md#fapi-arc-060) | `L` |
| 81 | [FAPI-ARC-070 — Multi-tenancy, gateway boundaries, monolith/microservice choices, and stopping rules](CURRICULUM.md#fapi-arc-070) | `XL` |
| 82 | [FAPI-ASY-010 — def versus async def, event-loop execution, and thread-pool dispatch](CURRICULUM.md#fapi-asy-010) | `L` |
| 83 | [FAPI-ASY-020 — Blocking I/O, CPU-bound work, worker threads, and process offloading](CURRICULUM.md#fapi-asy-020) | `L` |
| 84 | [FAPI-ASY-030 — Timeouts, cancellation, task groups, and structured concurrency](CURRICULUM.md#fapi-asy-030) | `XL` |
| 85 | [FAPI-ASY-040 — BackgroundTasks versus durable jobs and external workers](CURRICULUM.md#fapi-asy-040) | `L` |
| 86 | [FAPI-ASY-050 — Message brokers, RabbitMQ, retries, idempotency, and job state](CURRICULUM.md#fapi-asy-050) | `XL` |
| 87 | [FAPI-ASY-060 — Streaming request/response bodies, backpressure, memory, and cleanup](CURRICULUM.md#fapi-asy-060) | `XL` |
| 88 | [FAPI-ASY-070 — Workers, processes, concurrency limits, pool sizing, and shared state](CURRICULUM.md#fapi-asy-070) | `XL` |
| 89 | [FAPI-ASY-080 — Caching, Redis, serialization costs, compression, and response size](CURRICULUM.md#fapi-asy-080) | `L` |
| 90 | [FAPI-ASY-090 — Profiling, load testing, benchmarking, and evidence-led performance diagnosis](CURRICULUM.md#fapi-asy-090) | `XL` |
| 91 | [FAPI-SEC-010 — Authentication, authorization, and API threat modelling](CURRICULUM.md#fapi-sec-010) | `L` |
| 92 | [FAPI-SEC-020 — Password hashing, API keys, HTTP Basic, and bearer credentials](CURRICULUM.md#fapi-sec-020) | `L` |
| 93 | [FAPI-SEC-030 — JWT validation, key rotation, access tokens, refresh rotation, and revocation](CURRICULUM.md#fapi-sec-030) | `XL` |
| 94 | [FAPI-SEC-040 — Secure cookies, sessions, CSRF, and browser credential boundaries](CURRICULUM.md#fapi-sec-040) | `L` |
| 95 | [FAPI-SEC-050 — OAuth2 flows, OpenID Connect, external identity providers, and scopes](CURRICULUM.md#fapi-sec-050) | `XL` |
| 96 | [FAPI-SEC-060 — RBAC, ABAC, object-level authorization, and tenant isolation](CURRICULUM.md#fapi-sec-060) | `XL` |
| 97 | [FAPI-SEC-070 — CORS, trusted hosts, HTTPS, proxy trust, and security headers](CURRICULUM.md#fapi-sec-070) | `L` |
| 98 | [FAPI-SEC-080 — Validation boundaries, mass assignment, SQL injection, SSRF, uploads, and path traversal](CURRICULUM.md#fapi-sec-080) | `XL` |
| 99 | [FAPI-SEC-090 — Rate limits, brute-force controls, replay, idempotency, audit, and sensitive logging](CURRICULUM.md#fapi-sec-090) | `XL` |
| 100 | [FAPI-SEC-100 — Secrets, dependency vulnerabilities, authorization tests, and security review](CURRICULUM.md#fapi-sec-100) | `L` |
| 101 | [FAPI-RT-010 — REST, RPC, streaming, events, GraphQL, and gRPC boundaries](CURRICULUM.md#fapi-rt-010) | `L` |
| 102 | [FAPI-RT-020 — Streaming HTTP responses, chunking, large files, and disconnects](CURRICULUM.md#fapi-rt-020) | `L` |
| 103 | [FAPI-RT-030 — Server-Sent Events: framing, reconnects, IDs, buffering, and cleanup](CURRICULUM.md#fapi-rt-030) | `L` |
| 104 | [FAPI-RT-040 — WebSocket handshake, connection lifetime, receive/send loops, and disconnects](CURRICULUM.md#fapi-rt-040) | `L` |
| 105 | [FAPI-RT-050 — WebSocket managers, broadcast, heartbeats, auth, backpressure, and scaling](CURRICULUM.md#fapi-rt-050) | `XL` |
| 106 | [FAPI-RT-060 — Webhooks: signing, replay protection, retries, idempotency, and delivery logs](CURRICULUM.md#fapi-rt-060) | `L` |
| 107 | [FAPI-RT-070 — Polling, long polling, brokers, and event-driven API boundaries](CURRICULUM.md#fapi-rt-070) | `L` |
| 108 | [FAPI-RT-080 — gRPC foundations: Protocol Buffers, code generation, unary calls, status, and metadata](CURRICULUM.md#fapi-rt-080) | `XL` |
| 109 | [FAPI-RT-090 — gRPC streaming, deadlines, cancellation, interceptors, auth, evolution, and gateways](CURRICULUM.md#fapi-rt-090) | `XL` |
| 110 | [FAPI-TST-010 — Testing strategy, observable contracts, and test boundaries](CURRICULUM.md#fapi-tst-010) | `L` |
| 111 | [FAPI-TST-020 — TestClient, HTTPX AsyncClient, ASGI transports, and lifespan-aware tests](CURRICULUM.md#fapi-tst-020) | `L` |
| 112 | [FAPI-TST-030 — Dependency overrides, auth tests, validation errors, and OpenAPI contracts](CURRICULUM.md#fapi-tst-030) | `L` |
| 113 | [FAPI-TST-040 — Property-based testing for Pydantic models and API contracts](CURRICULUM.md#fapi-tst-040) | `L` |
| 114 | [FAPI-TST-050 — PostgreSQL integration tests, transaction isolation, fixtures, and factories](CURRICULUM.md#fapi-tst-050) | `XL` |
| 115 | [FAPI-TST-060 — Alembic migration tests and schema-compatibility checks](CURRICULUM.md#fapi-tst-060) | `L` |
| 116 | [FAPI-TST-070 — WebSocket, SSE, gRPC, webhook, and background-job tests](CURRICULUM.md#fapi-tst-070) | `XL` |
| 117 | [FAPI-TST-080 — Timeout, retry, concurrency, load, performance, and security-focused tests](CURRICULUM.md#fapi-tst-080) | `XL` |
| 118 | [FAPI-OPS-010 — Environment configuration, secret injection, and production settings](CURRICULUM.md#fapi-ops-010) | `L` |
| 119 | [FAPI-OPS-020 — Uvicorn process model, workers, startup, shutdown, and graceful draining](CURRICULUM.md#fapi-ops-020) | `L` |
| 120 | [FAPI-OPS-030 — Reverse proxies, forwarded headers, root paths, TLS, and trust](CURRICULUM.md#fapi-ops-030) | `L` |
| 121 | [FAPI-OPS-040 — Containers, images, Compose profiles, health, and readiness](CURRICULUM.md#fapi-ops-040) | `L` |
| 122 | [FAPI-OPS-050 — Structured logs, metrics, traces, and request-span propagation](CURRICULUM.md#fapi-ops-050) | `XL` |
| 123 | [FAPI-OPS-060 — Capacity planning, worker/pool limits, load tests, and performance budgets](CURRICULUM.md#fapi-ops-060) | `XL` |
| 124 | [FAPI-OPS-070 — Production debugging, incident response, deployment strategies, and rollback](CURRICULUM.md#fapi-ops-070) | `XL` |
| 125 | [FAPI-SYN-010 — Request-lifecycle and framework-boundary interview synthesis](CURRICULUM.md#fapi-syn-010) | `L` |
| 126 | [FAPI-SYN-020 — Pydantic, dependency, middleware, and error-handling interview synthesis](CURRICULUM.md#fapi-syn-020) | `L` |
| 127 | [FAPI-SYN-030 — PostgreSQL, SQLAlchemy, Alembic, and architecture interview synthesis](CURRICULUM.md#fapi-syn-030) | `XL` |
| 128 | [FAPI-SYN-040 — Async, security, real-time, performance, and production design synthesis](CURRICULUM.md#fapi-syn-040) | `XL` |
| 129 | [FAPI-MSV-010 — Microservice decision, decomposition, ownership, and stopping rules](CURRICULUM.md#fapi-msv-010) | `XL` |
| 130 | [FAPI-MSV-020 — Remote-call reality: partial failure, latency, clocks, concurrency, and partitions](CURRICULUM.md#fapi-msv-020) | `XL` |
| 131 | [FAPI-MSV-030 — Communication selection across HTTP, gRPC, queues, pub/sub, logs, and browser streams](CURRICULUM.md#fapi-msv-030) | `XL` |
| 132 | [FAPI-MSV-040 — Service and message contracts, envelopes, versioning, and ownership](CURRICULUM.md#fapi-msv-040) | `L` |
| 133 | [FAPI-MSV-050 — RabbitMQ fundamentals: AMQP entities, topology, routing, and local operations](CURRICULUM.md#fapi-msv-050) | `XL` |
| 134 | [FAPI-MSV-060 — RabbitMQ connections, channels, recovery, permissions, and topology compatibility](CURRICULUM.md#fapi-msv-060) | `L` |
| 135 | [FAPI-MSV-070 — RabbitMQ publisher correctness: confirms, mandatory returns, uncertainty, and backpressure](CURRICULUM.md#fapi-msv-070) | `XL` |
| 136 | [FAPI-MSV-080 — RabbitMQ consumer correctness: acknowledgements, prefetch, crash windows, and draining](CURRICULUM.md#fapi-msv-080) | `XL` |
| 137 | [FAPI-MSV-090 — RabbitMQ retries, dead lettering, delay, redrive, and poison-message operations](CURRICULUM.md#fapi-msv-090) | `XL` |
| 138 | [FAPI-MSV-100 — RabbitMQ queue types, ordering, retention, and broker selection](CURRICULUM.md#fapi-msv-100) | `L` |
| 139 | [FAPI-MSV-110 — Delivery semantics, duplicate handling, and idempotent operations](CURRICULUM.md#fapi-msv-110) | `XL` |
| 140 | [FAPI-MSV-120 — Transactional outbox, inbox, relay, CDC boundaries, and cleanup](CURRICULUM.md#fapi-msv-120) | `XL` |
| 141 | [FAPI-MSV-130 — Distributed workflows: sagas, compensation, orchestration, and intervention](CURRICULUM.md#fapi-msv-130) | `XL` |
| 142 | [FAPI-MSV-140 — Eventual consistency, read models, CQRS, and event-sourcing boundaries](CURRICULUM.md#fapi-msv-140) | `XL` |
| 143 | [FAPI-MSV-150 — Production gRPC contracts: Protobuf evolution, status details, and metadata](CURRICULUM.md#fapi-msv-150) | `L` |
| 144 | [FAPI-MSV-160 — Production gRPC execution: deadlines, cancellation, retries, streaming, and flow control](CURRICULUM.md#fapi-msv-160) | `XL` |
| 145 | [FAPI-MSV-170 — gRPC operations: channels, discovery, balancing, health, TLS, tracing, and gateways](CURRICULUM.md#fapi-msv-170) | `XL` |
| 146 | [FAPI-MSV-180 — Resilience budgets: timeouts, retry amplification, breakers, bulkheads, and load shedding](CURRICULUM.md#fapi-msv-180) | `XL` |
| 147 | [FAPI-MSV-190 — Discovery, gateways, proxies, Kubernetes traffic, and service-mesh boundaries](CURRICULUM.md#fapi-msv-190) | `XL` |
| 148 | [FAPI-MSV-200 — Service data ownership, cross-service queries, reporting, and migration from shared storage](CURRICULUM.md#fapi-msv-200) | `XL` |
| 149 | [FAPI-MSV-210 — Distributed observability: context propagation, logs, metrics, traces, SLIs, SLOs, and alerts](CURRICULUM.md#fapi-msv-210) | `XL` |
| 150 | [FAPI-MSV-220 — Microservice security: workload identity, mTLS, delegated authorization, broker permissions, and tenant context](CURRICULUM.md#fapi-msv-220) | `XL` |
| 151 | [FAPI-MSV-230 — Distributed testing: contracts, real dependencies, duplicate delivery, fault injection, and eventual consistency](CURRICULUM.md#fapi-msv-230) | `XL` |
| 152 | [FAPI-MSV-240 — Compatible deployment and evolution: rollout, draining, autoscaling, backlog, and schema windows](CURRICULUM.md#fapi-msv-240) | `XL` |
| 153 | [FAPI-MSV-250 — Reliability operations: runbooks, incidents, postmortems, disaster recovery, and dependency upgrades](CURRICULUM.md#fapi-msv-250) | `XL` |
| 154 | [FAPI-MSV-260 — Governance and ownership: catalogs, ADRs, golden paths, shared libraries, team topology, and cost](CURRICULUM.md#fapi-msv-260) | `XL` |
| 155 | [FAPI-SYN-050 — Senior FastAPI code review, debugging, and architecture capstone](CURRICULUM.md#fapi-syn-050) | `XL` |
| 156 | [FAPI-MSV-270 — Evolutionary extraction and senior microservice design synthesis](CURRICULUM.md#fapi-msv-270) | `XL` |

### Project milestones

- [FAPI-PRJ-010 — First typed CRUD API](PROJECTS.md#fapi-prj-010)
- [FAPI-PRJ-020 — PostgreSQL catalog and ordering service](PROJECTS.md#fapi-prj-020)
- [FAPI-PRJ-030 — Authenticated multi-tenant service](PROJECTS.md#fapi-prj-030)
- [FAPI-PRJ-040 — Synthetic review and workflow platform](PROJECTS.md#fapi-prj-040)
- [FAPI-PRJ-050 — File-processing and durable-job service](PROJECTS.md#fapi-prj-050)
- [FAPI-PRJ-060 — Real-time operations dashboard](PROJECTS.md#fapi-prj-060)
- [FAPI-PRJ-090 — Reliable RabbitMQ workflow service](PROJECTS.md#fapi-prj-090)
- [FAPI-PRJ-100 — Microservices production capstone](PROJECTS.md#fapi-prj-100)

<a id="complete-fastapi-mastery"></a>
## Complete FastAPI mastery

All canonical units, all projects, delayed recall, and transfer evidence; this is a long-term path.

<!-- path-meta: {"slug":"complete-fastapi-mastery","declared_units":156,"rapid_unit_minutes":[8355,12425],"lab_minutes":[5400,8100],"recall_minutes":[1320,1980],"mock_minutes":[840,1260],"checkpoint_minutes":[1800,2550],"rapid_total_minutes":[17715,26315],"full_mastery_hours":[1780,3139],"assumed_prerequisites":[]} -->
| Component | Count or time |
|---|---:|
| Canonical units | 156 |
| Rapid unit study | 139 h 15 min–207 h 5 min |
| Selected practice/labs | 90 h–135 h |
| Recall and comparison | 22 h–33 h |
| Mock interviews | 14 h–21 h |
| Project checkpoints | 30 h–42 h 30 min |
| **Rapid path total** | **295 h 15 min–438 h 35 min** |
| Full mastery of included units | 1780–3139 h |

### Assumed prior knowledge or prerequisite bridges

None. The path includes its canonical prerequisites.

### Recommended sequence

| # | Unit | Size |
|---:|---|:---:|
| 1 | [FAPI-FND-010 — Python runtime, uv project, and reproducible environment](CURRICULUM.md#fapi-fnd-010) | `M` |
| 2 | [FAPI-FND-020 — Minimal FastAPI application and first route](CURRICULUM.md#fapi-fnd-020) | `S` |
| 3 | [FAPI-FND-030 — Application entry points, import strings, reload, and server startup](CURRICULUM.md#fapi-fnd-030) | `M` |
| 4 | [FAPI-FND-040 — Interactive documentation, OpenAPI inspection, and simple API clients](CURRICULUM.md#fapi-fnd-040) | `S` |
| 5 | [FAPI-FND-050 — Configuration, environment variables, and application factories](CURRICULUM.md#fapi-fnd-050) | `M` |
| 6 | [FAPI-FND-060 — Startup, import, reload, and configuration failure diagnosis](CURRICULUM.md#fapi-fnd-060) | `M` |
| 7 | [FAPI-HTTP-010 — HTTP message anatomy, methods, status codes, and media types](CURRICULUM.md#fapi-http-010) | `L` |
| 8 | [FAPI-HTTP-020 — URLs, path/query semantics, request bodies, encoding, and JSON](CURRICULUM.md#fapi-http-020) | `M` |
| 9 | [FAPI-HTTP-030 — Headers, cookies, content negotiation, and representation metadata](CURRICULUM.md#fapi-http-030) | `M` |
| 10 | [FAPI-HTTP-040 — REST resources, actions, RPC-style endpoints, and practical constraints](CURRICULUM.md#fapi-http-040) | `L` |
| 11 | [FAPI-HTTP-050 — Error contracts, RFC problem details, and API versioning](CURRICULUM.md#fapi-http-050) | `L` |
| 12 | [FAPI-HTTP-060 — Pagination, filtering, sorting, and field selection](CURRICULUM.md#fapi-http-060) | `L` |
| 13 | [FAPI-HTTP-070 — Partial updates, idempotency keys, and conditional writes](CURRICULUM.md#fapi-http-070) | `L` |
| 14 | [FAPI-HTTP-080 — Caching, ETags, conditional requests, redirects, and range responses](CURRICULUM.md#fapi-http-080) | `L` |
| 15 | [FAPI-ASGI-010 — WSGI versus ASGI and the protocol boundary](CURRICULUM.md#fapi-asgi-010) | `L` |
| 16 | [FAPI-ASGI-020 — ASGI scope, receive, send, and the HTTP lifecycle](CURRICULUM.md#fapi-asgi-020) | `L` |
| 17 | [FAPI-ASGI-030 — Starlette beneath FastAPI: requests, responses, routing, and exceptions](CURRICULUM.md#fapi-asgi-030) | `L` |
| 18 | [FAPI-ASGI-040 — Lifespan, application state, and resource ownership](CURRICULUM.md#fapi-asgi-040) | `L` |
| 19 | [FAPI-ASGI-050 — ASGI middleware onion, exception flow, and ordering](CURRICULUM.md#fapi-asgi-050) | `L` |
| 20 | [FAPI-ASGI-060 — Client disconnects, cancellation, and streaming lifecycle](CURRICULUM.md#fapi-asgi-060) | `L` |
| 21 | [FAPI-ASGI-070 — ASGI servers, workers, proxy headers, root paths, and mounted applications](CURRICULUM.md#fapi-asgi-070) | `L` |
| 22 | [FAPI-PYD-010 — BaseModel fields: required, optional, nullable, defaults, and factories](CURRICULUM.md#fapi-pyd-010) | `M` |
| 23 | [FAPI-PYD-020 — Coercion, strict validation, constraints, and Annotated](CURRICULUM.md#fapi-pyd-020) | `L` |
| 24 | [FAPI-PYD-030 — Model configuration, extra fields, frozen models, copying, and trusted construction](CURRICULUM.md#fapi-pyd-030) | `L` |
| 25 | [FAPI-PYD-040 — Nested and recursive models, forward annotations, unions, and discriminators](CURRICULUM.md#fapi-pyd-040) | `L` |
| 26 | [FAPI-PYD-050 — Generics, RootModel, TypeAdapter, and Pydantic dataclasses](CURRICULUM.md#fapi-pyd-050) | `L` |
| 27 | [FAPI-PYD-060 — Aliases, validation aliases, serialization aliases, and alias generators](CURRICULUM.md#fapi-pyd-060) | `M` |
| 28 | [FAPI-PYD-070 — Field and model validators: modes, ordering, context, and defaults](CURRICULUM.md#fapi-pyd-070) | `XL` |
| 29 | [FAPI-PYD-080 — Serialization, serializers, computed fields, and inclusion or exclusion](CURRICULUM.md#fapi-pyd-080) | `L` |
| 30 | [FAPI-PYD-090 — JSON Schema, OpenAPI interaction, and custom types](CURRICULUM.md#fapi-pyd-090) | `XL` |
| 31 | [FAPI-PYD-100 — Pydantic Settings: source precedence, env files, secrets, nesting, and custom sources](CURRICULUM.md#fapi-pyd-100) | `L` |
| 32 | [FAPI-PYD-110 — Object-attribute validation and model boundaries](CURRICULUM.md#fapi-pyd-110) | `L` |
| 33 | [FAPI-PYD-120 — Pydantic performance, validator side effects, v1-to-v2 migration, and common mistakes](CURRICULUM.md#fapi-pyd-120) | `XL` |
| 34 | [FAPI-APP-010 — Path operations, router matching, route order, and conflicts](CURRICULUM.md#fapi-app-010) | `M` |
| 35 | [FAPI-APP-020 — Path and query parameters, constraints, aliases, and custom parsing](CURRICULUM.md#fapi-app-020) | `L` |
| 36 | [FAPI-APP-030 — Headers, cookies, custom parameter types, and direct Request access](CURRICULUM.md#fapi-app-030) | `M` |
| 37 | [FAPI-APP-040 — Request bodies, multiple body parameters, embedding, and aliases](CURRICULUM.md#fapi-app-040) | `L` |
| 38 | [FAPI-APP-050 — Forms, multipart data, file uploads, and UploadFile](CURRICULUM.md#fapi-app-050) | `L` |
| 39 | [FAPI-APP-060 — Response models, output validation, serialization, status, headers, and cookies](CURRICULUM.md#fapi-app-060) | `L` |
| 40 | [FAPI-APP-070 — Response classes, redirects, files, and streaming responses](CURRICULUM.md#fapi-app-070) | `L` |
| 41 | [FAPI-APP-080 — APIRouter, nested routers, tags, operation IDs, and route organization](CURRICULUM.md#fapi-app-080) | `L` |
| 42 | [FAPI-APP-090 — HTTP exceptions, validation errors, custom handlers, and error translation](CURRICULUM.md#fapi-app-090) | `L` |
| 43 | [FAPI-APP-100 — OpenAPI metadata, examples, callbacks, webhooks, and schema quality](CURRICULUM.md#fapi-app-100) | `L` |
| 44 | [FAPI-DEP-010 — Callable, class-based, and parameterized dependencies](CURRICULUM.md#fapi-dep-010) | `L` |
| 45 | [FAPI-DEP-020 — Subdependencies and dependency-graph resolution](CURRICULUM.md#fapi-dep-020) | `L` |
| 46 | [FAPI-DEP-030 — Per-request dependency caching and use_cache](CURRICULUM.md#fapi-dep-030) | `M` |
| 47 | [FAPI-DEP-040 — Yield dependencies, setup/teardown order, scopes, and resource safety](CURRICULUM.md#fapi-dep-040) | `XL` |
| 48 | [FAPI-DEP-050 — Authentication and authorization dependencies](CURRICULUM.md#fapi-dep-050) | `L` |
| 49 | [FAPI-DEP-060 — Router/global dependencies and test overrides](CURRICULUM.md#fapi-dep-060) | `L` |
| 50 | [FAPI-DEP-070 — Request state, composition roots, service location, and dependency boundaries](CURRICULUM.md#fapi-dep-070) | `XL` |
| 51 | [FAPI-MID-010 — Function, class-based, and raw ASGI middleware ordering](CURRICULUM.md#fapi-mid-010) | `L` |
| 52 | [FAPI-MID-020 — Request IDs, structured logging, context variables, and correlation](CURRICULUM.md#fapi-mid-020) | `L` |
| 53 | [FAPI-MID-030 — CORS, trusted hosts, HTTPS redirects, compression, and sessions](CURRICULUM.md#fapi-mid-030) | `L` |
| 54 | [FAPI-MID-040 — Body consumption, exception behavior, and cancellation in middleware](CURRICULUM.md#fapi-mid-040) | `XL` |
| 55 | [FAPI-MID-050 — Rate limiting, observability, and choosing middleware versus dependencies](CURRICULUM.md#fapi-mid-050) | `L` |
| 56 | [FAPI-DB-010 — Relational modelling and PostgreSQL constraints for APIs](CURRICULUM.md#fapi-db-010) | `L` |
| 57 | [FAPI-DB-020 — PostgreSQL drivers, SQLAlchemy engines, URLs, and connection pools](CURRICULUM.md#fapi-db-020) | `L` |
| 58 | [FAPI-DB-030 — SQLAlchemy typed declarative mappings, columns, and constraints](CURRICULUM.md#fapi-db-030) | `L` |
| 59 | [FAPI-DB-040 — Session per request, identity map, and unit-of-work lifecycle](CURRICULUM.md#fapi-db-040) | `XL` |
| 60 | [FAPI-DB-050 — Transactions, flush, commit, rollback, refresh, expiration, and savepoints](CURRICULUM.md#fapi-db-050) | `XL` |
| 61 | [FAPI-DB-060 — Relationships, cascades, eager/lazy loading, and object graphs](CURRICULUM.md#fapi-db-060) | `L` |
| 62 | [FAPI-DB-070 — AsyncEngine, AsyncSession, and preventing implicit I/O](CURRICULUM.md#fapi-db-070) | `XL` |
| 63 | [FAPI-DB-080 — Queries, joins, aggregates, filtering, sorting, and pagination](CURRICULUM.md#fapi-db-080) | `L` |
| 64 | [FAPI-DB-090 — N+1 diagnosis, eager loading, query plans, and indexes](CURRICULUM.md#fapi-db-090) | `XL` |
| 65 | [FAPI-DB-100 — Locking, isolation levels, deadlocks, retries, and optimistic concurrency](CURRICULUM.md#fapi-db-100) | `XL` |
| 66 | [FAPI-DB-110 — Bulk work, generated values, timestamps, soft deletion, and tenant boundaries](CURRICULUM.md#fapi-db-110) | `L` |
| 67 | [FAPI-DB-120 — Database test isolation, mapping boundaries, repositories, and direct SQLAlchemy](CURRICULUM.md#fapi-db-120) | `XL` |
| 68 | [FAPI-MIG-010 — Alembic environment, configuration, metadata discovery, and revision graph](CURRICULUM.md#fapi-mig-010) | `L` |
| 69 | [FAPI-MIG-020 — First migration, upgrade, downgrade, current, and history](CURRICULUM.md#fapi-mig-020) | `L` |
| 70 | [FAPI-MIG-030 — Autogenerate review, naming conventions, constraints, indexes, and defaults](CURRICULUM.md#fapi-mig-030) | `XL` |
| 71 | [FAPI-MIG-040 — Data migrations, backfills, enum changes, and offline SQL](CURRICULUM.md#fapi-mig-040) | `XL` |
| 72 | [FAPI-MIG-050 — Migration branches, multiple heads, merge revisions, and conflicts](CURRICULUM.md#fapi-mig-050) | `L` |
| 73 | [FAPI-MIG-060 — Async application integration, migration testing, and drift detection](CURRICULUM.md#fapi-mig-060) | `L` |
| 74 | [FAPI-MIG-070 — Expand-and-contract changes, locks, compatibility windows, and rollback decisions](CURRICULUM.md#fapi-mig-070) | `XL` |
| 75 | [FAPI-ARC-010 — From a single file to routers and feature modules](CURRICULUM.md#fapi-arc-010) | `L` |
| 76 | [FAPI-ARC-020 — Layered architecture versus vertical slices](CURRICULUM.md#fapi-arc-020) | `L` |
| 77 | [FAPI-ARC-030 — Service layer, functional core, domain services, DTO mapping, and orchestration](CURRICULUM.md#fapi-arc-030) | `L` |
| 78 | [FAPI-ARC-040 — Repository and Unit of Work patterns with transaction ownership](CURRICULUM.md#fapi-arc-040) | `XL` |
| 79 | [FAPI-ARC-050 — Composition root, dependency inversion, and error translation](CURRICULUM.md#fapi-arc-050) | `L` |
| 80 | [FAPI-ARC-060 — Modular monolith boundaries, circular imports, and plugin extension points](CURRICULUM.md#fapi-arc-060) | `L` |
| 81 | [FAPI-ARC-070 — Multi-tenancy, gateway boundaries, monolith/microservice choices, and stopping rules](CURRICULUM.md#fapi-arc-070) | `XL` |
| 82 | [FAPI-ASY-010 — def versus async def, event-loop execution, and thread-pool dispatch](CURRICULUM.md#fapi-asy-010) | `L` |
| 83 | [FAPI-ASY-020 — Blocking I/O, CPU-bound work, worker threads, and process offloading](CURRICULUM.md#fapi-asy-020) | `L` |
| 84 | [FAPI-ASY-030 — Timeouts, cancellation, task groups, and structured concurrency](CURRICULUM.md#fapi-asy-030) | `XL` |
| 85 | [FAPI-ASY-040 — BackgroundTasks versus durable jobs and external workers](CURRICULUM.md#fapi-asy-040) | `L` |
| 86 | [FAPI-ASY-050 — Message brokers, RabbitMQ, retries, idempotency, and job state](CURRICULUM.md#fapi-asy-050) | `XL` |
| 87 | [FAPI-ASY-060 — Streaming request/response bodies, backpressure, memory, and cleanup](CURRICULUM.md#fapi-asy-060) | `XL` |
| 88 | [FAPI-ASY-070 — Workers, processes, concurrency limits, pool sizing, and shared state](CURRICULUM.md#fapi-asy-070) | `XL` |
| 89 | [FAPI-ASY-080 — Caching, Redis, serialization costs, compression, and response size](CURRICULUM.md#fapi-asy-080) | `L` |
| 90 | [FAPI-ASY-090 — Profiling, load testing, benchmarking, and evidence-led performance diagnosis](CURRICULUM.md#fapi-asy-090) | `XL` |
| 91 | [FAPI-SEC-010 — Authentication, authorization, and API threat modelling](CURRICULUM.md#fapi-sec-010) | `L` |
| 92 | [FAPI-SEC-020 — Password hashing, API keys, HTTP Basic, and bearer credentials](CURRICULUM.md#fapi-sec-020) | `L` |
| 93 | [FAPI-SEC-030 — JWT validation, key rotation, access tokens, refresh rotation, and revocation](CURRICULUM.md#fapi-sec-030) | `XL` |
| 94 | [FAPI-SEC-040 — Secure cookies, sessions, CSRF, and browser credential boundaries](CURRICULUM.md#fapi-sec-040) | `L` |
| 95 | [FAPI-SEC-050 — OAuth2 flows, OpenID Connect, external identity providers, and scopes](CURRICULUM.md#fapi-sec-050) | `XL` |
| 96 | [FAPI-SEC-060 — RBAC, ABAC, object-level authorization, and tenant isolation](CURRICULUM.md#fapi-sec-060) | `XL` |
| 97 | [FAPI-SEC-070 — CORS, trusted hosts, HTTPS, proxy trust, and security headers](CURRICULUM.md#fapi-sec-070) | `L` |
| 98 | [FAPI-SEC-080 — Validation boundaries, mass assignment, SQL injection, SSRF, uploads, and path traversal](CURRICULUM.md#fapi-sec-080) | `XL` |
| 99 | [FAPI-SEC-090 — Rate limits, brute-force controls, replay, idempotency, audit, and sensitive logging](CURRICULUM.md#fapi-sec-090) | `XL` |
| 100 | [FAPI-SEC-100 — Secrets, dependency vulnerabilities, authorization tests, and security review](CURRICULUM.md#fapi-sec-100) | `L` |
| 101 | [FAPI-RT-010 — REST, RPC, streaming, events, GraphQL, and gRPC boundaries](CURRICULUM.md#fapi-rt-010) | `L` |
| 102 | [FAPI-RT-020 — Streaming HTTP responses, chunking, large files, and disconnects](CURRICULUM.md#fapi-rt-020) | `L` |
| 103 | [FAPI-RT-030 — Server-Sent Events: framing, reconnects, IDs, buffering, and cleanup](CURRICULUM.md#fapi-rt-030) | `L` |
| 104 | [FAPI-RT-040 — WebSocket handshake, connection lifetime, receive/send loops, and disconnects](CURRICULUM.md#fapi-rt-040) | `L` |
| 105 | [FAPI-RT-050 — WebSocket managers, broadcast, heartbeats, auth, backpressure, and scaling](CURRICULUM.md#fapi-rt-050) | `XL` |
| 106 | [FAPI-RT-060 — Webhooks: signing, replay protection, retries, idempotency, and delivery logs](CURRICULUM.md#fapi-rt-060) | `L` |
| 107 | [FAPI-RT-070 — Polling, long polling, brokers, and event-driven API boundaries](CURRICULUM.md#fapi-rt-070) | `L` |
| 108 | [FAPI-RT-080 — gRPC foundations: Protocol Buffers, code generation, unary calls, status, and metadata](CURRICULUM.md#fapi-rt-080) | `XL` |
| 109 | [FAPI-RT-090 — gRPC streaming, deadlines, cancellation, interceptors, auth, evolution, and gateways](CURRICULUM.md#fapi-rt-090) | `XL` |
| 110 | [FAPI-TST-010 — Testing strategy, observable contracts, and test boundaries](CURRICULUM.md#fapi-tst-010) | `L` |
| 111 | [FAPI-TST-020 — TestClient, HTTPX AsyncClient, ASGI transports, and lifespan-aware tests](CURRICULUM.md#fapi-tst-020) | `L` |
| 112 | [FAPI-TST-030 — Dependency overrides, auth tests, validation errors, and OpenAPI contracts](CURRICULUM.md#fapi-tst-030) | `L` |
| 113 | [FAPI-TST-040 — Property-based testing for Pydantic models and API contracts](CURRICULUM.md#fapi-tst-040) | `L` |
| 114 | [FAPI-TST-050 — PostgreSQL integration tests, transaction isolation, fixtures, and factories](CURRICULUM.md#fapi-tst-050) | `XL` |
| 115 | [FAPI-TST-060 — Alembic migration tests and schema-compatibility checks](CURRICULUM.md#fapi-tst-060) | `L` |
| 116 | [FAPI-TST-070 — WebSocket, SSE, gRPC, webhook, and background-job tests](CURRICULUM.md#fapi-tst-070) | `XL` |
| 117 | [FAPI-TST-080 — Timeout, retry, concurrency, load, performance, and security-focused tests](CURRICULUM.md#fapi-tst-080) | `XL` |
| 118 | [FAPI-OPS-010 — Environment configuration, secret injection, and production settings](CURRICULUM.md#fapi-ops-010) | `L` |
| 119 | [FAPI-OPS-020 — Uvicorn process model, workers, startup, shutdown, and graceful draining](CURRICULUM.md#fapi-ops-020) | `L` |
| 120 | [FAPI-OPS-030 — Reverse proxies, forwarded headers, root paths, TLS, and trust](CURRICULUM.md#fapi-ops-030) | `L` |
| 121 | [FAPI-OPS-040 — Containers, images, Compose profiles, health, and readiness](CURRICULUM.md#fapi-ops-040) | `L` |
| 122 | [FAPI-OPS-050 — Structured logs, metrics, traces, and request-span propagation](CURRICULUM.md#fapi-ops-050) | `XL` |
| 123 | [FAPI-OPS-060 — Capacity planning, worker/pool limits, load tests, and performance budgets](CURRICULUM.md#fapi-ops-060) | `XL` |
| 124 | [FAPI-OPS-070 — Production debugging, incident response, deployment strategies, and rollback](CURRICULUM.md#fapi-ops-070) | `XL` |
| 125 | [FAPI-SYN-010 — Request-lifecycle and framework-boundary interview synthesis](CURRICULUM.md#fapi-syn-010) | `L` |
| 126 | [FAPI-SYN-020 — Pydantic, dependency, middleware, and error-handling interview synthesis](CURRICULUM.md#fapi-syn-020) | `L` |
| 127 | [FAPI-SYN-030 — PostgreSQL, SQLAlchemy, Alembic, and architecture interview synthesis](CURRICULUM.md#fapi-syn-030) | `XL` |
| 128 | [FAPI-SYN-040 — Async, security, real-time, performance, and production design synthesis](CURRICULUM.md#fapi-syn-040) | `XL` |
| 129 | [FAPI-SYN-050 — Senior FastAPI code review, debugging, and architecture capstone](CURRICULUM.md#fapi-syn-050) | `XL` |
| 130 | [FAPI-MSV-010 — Microservice decision, decomposition, ownership, and stopping rules](CURRICULUM.md#fapi-msv-010) | `XL` |
| 131 | [FAPI-MSV-020 — Remote-call reality: partial failure, latency, clocks, concurrency, and partitions](CURRICULUM.md#fapi-msv-020) | `XL` |
| 132 | [FAPI-MSV-030 — Communication selection across HTTP, gRPC, queues, pub/sub, logs, and browser streams](CURRICULUM.md#fapi-msv-030) | `XL` |
| 133 | [FAPI-MSV-040 — Service and message contracts, envelopes, versioning, and ownership](CURRICULUM.md#fapi-msv-040) | `L` |
| 134 | [FAPI-MSV-050 — RabbitMQ fundamentals: AMQP entities, topology, routing, and local operations](CURRICULUM.md#fapi-msv-050) | `XL` |
| 135 | [FAPI-MSV-060 — RabbitMQ connections, channels, recovery, permissions, and topology compatibility](CURRICULUM.md#fapi-msv-060) | `L` |
| 136 | [FAPI-MSV-070 — RabbitMQ publisher correctness: confirms, mandatory returns, uncertainty, and backpressure](CURRICULUM.md#fapi-msv-070) | `XL` |
| 137 | [FAPI-MSV-080 — RabbitMQ consumer correctness: acknowledgements, prefetch, crash windows, and draining](CURRICULUM.md#fapi-msv-080) | `XL` |
| 138 | [FAPI-MSV-090 — RabbitMQ retries, dead lettering, delay, redrive, and poison-message operations](CURRICULUM.md#fapi-msv-090) | `XL` |
| 139 | [FAPI-MSV-100 — RabbitMQ queue types, ordering, retention, and broker selection](CURRICULUM.md#fapi-msv-100) | `L` |
| 140 | [FAPI-MSV-110 — Delivery semantics, duplicate handling, and idempotent operations](CURRICULUM.md#fapi-msv-110) | `XL` |
| 141 | [FAPI-MSV-120 — Transactional outbox, inbox, relay, CDC boundaries, and cleanup](CURRICULUM.md#fapi-msv-120) | `XL` |
| 142 | [FAPI-MSV-130 — Distributed workflows: sagas, compensation, orchestration, and intervention](CURRICULUM.md#fapi-msv-130) | `XL` |
| 143 | [FAPI-MSV-140 — Eventual consistency, read models, CQRS, and event-sourcing boundaries](CURRICULUM.md#fapi-msv-140) | `XL` |
| 144 | [FAPI-MSV-150 — Production gRPC contracts: Protobuf evolution, status details, and metadata](CURRICULUM.md#fapi-msv-150) | `L` |
| 145 | [FAPI-MSV-160 — Production gRPC execution: deadlines, cancellation, retries, streaming, and flow control](CURRICULUM.md#fapi-msv-160) | `XL` |
| 146 | [FAPI-MSV-170 — gRPC operations: channels, discovery, balancing, health, TLS, tracing, and gateways](CURRICULUM.md#fapi-msv-170) | `XL` |
| 147 | [FAPI-MSV-180 — Resilience budgets: timeouts, retry amplification, breakers, bulkheads, and load shedding](CURRICULUM.md#fapi-msv-180) | `XL` |
| 148 | [FAPI-MSV-190 — Discovery, gateways, proxies, Kubernetes traffic, and service-mesh boundaries](CURRICULUM.md#fapi-msv-190) | `XL` |
| 149 | [FAPI-MSV-200 — Service data ownership, cross-service queries, reporting, and migration from shared storage](CURRICULUM.md#fapi-msv-200) | `XL` |
| 150 | [FAPI-MSV-210 — Distributed observability: context propagation, logs, metrics, traces, SLIs, SLOs, and alerts](CURRICULUM.md#fapi-msv-210) | `XL` |
| 151 | [FAPI-MSV-220 — Microservice security: workload identity, mTLS, delegated authorization, broker permissions, and tenant context](CURRICULUM.md#fapi-msv-220) | `XL` |
| 152 | [FAPI-MSV-230 — Distributed testing: contracts, real dependencies, duplicate delivery, fault injection, and eventual consistency](CURRICULUM.md#fapi-msv-230) | `XL` |
| 153 | [FAPI-MSV-240 — Compatible deployment and evolution: rollout, draining, autoscaling, backlog, and schema windows](CURRICULUM.md#fapi-msv-240) | `XL` |
| 154 | [FAPI-MSV-250 — Reliability operations: runbooks, incidents, postmortems, disaster recovery, and dependency upgrades](CURRICULUM.md#fapi-msv-250) | `XL` |
| 155 | [FAPI-MSV-260 — Governance and ownership: catalogs, ADRs, golden paths, shared libraries, team topology, and cost](CURRICULUM.md#fapi-msv-260) | `XL` |
| 156 | [FAPI-MSV-270 — Evolutionary extraction and senior microservice design synthesis](CURRICULUM.md#fapi-msv-270) | `XL` |

### Project milestones

- [FAPI-PRJ-010 — First typed CRUD API](PROJECTS.md#fapi-prj-010)
- [FAPI-PRJ-020 — PostgreSQL catalog and ordering service](PROJECTS.md#fapi-prj-020)
- [FAPI-PRJ-030 — Authenticated multi-tenant service](PROJECTS.md#fapi-prj-030)
- [FAPI-PRJ-040 — Synthetic review and workflow platform](PROJECTS.md#fapi-prj-040)
- [FAPI-PRJ-050 — File-processing and durable-job service](PROJECTS.md#fapi-prj-050)
- [FAPI-PRJ-060 — Real-time operations dashboard](PROJECTS.md#fapi-prj-060)
- [FAPI-PRJ-070 — REST-to-gRPC gateway](PROJECTS.md#fapi-prj-070)
- [FAPI-PRJ-080 — Production modular backend capstone](PROJECTS.md#fapi-prj-080)
- [FAPI-PRJ-090 — Reliable RabbitMQ workflow service](PROJECTS.md#fapi-prj-090)
- [FAPI-PRJ-100 — Microservices production capstone](PROJECTS.md#fapi-prj-100)

<a id="deep-pydantic"></a>
## Deep Pydantic path

For model semantics, validation, serialization, settings, schemas, performance, and FastAPI interaction.

<!-- path-meta: {"slug":"deep-pydantic","declared_units":26,"rapid_unit_minutes":[1105,1680],"lab_minutes":[360,540],"recall_minutes":[180,240],"mock_minutes":[60,120],"checkpoint_minutes":[90,150],"rapid_total_minutes":[1795,2730],"full_mastery_hours":[217,386],"assumed_prerequisites":[]} -->
| Component | Count or time |
|---|---:|
| Canonical units | 26 |
| Rapid unit study | 18 h 25 min–28 h |
| Selected practice/labs | 0 checkpoints; 6 h–9 h |
| Recall and comparison | 3 h–4 h |
| Mock interviews | 1 h–2 h |
| Project checkpoints | 1 h 30 min–2 h 30 min |
| **Rapid path total** | **29 h 55 min–45 h 30 min** |
| Full mastery of included units | 217–386 h |

### Assumed prior knowledge or prerequisite bridges

None. The path includes its canonical prerequisites.

### Recommended sequence

| # | Unit | Size |
|---:|---|:---:|
| 1 | [FAPI-FND-010 — Python runtime, uv project, and reproducible environment](CURRICULUM.md#fapi-fnd-010) | `M` |
| 2 | [FAPI-FND-020 — Minimal FastAPI application and first route](CURRICULUM.md#fapi-fnd-020) | `S` |
| 3 | [FAPI-FND-030 — Application entry points, import strings, reload, and server startup](CURRICULUM.md#fapi-fnd-030) | `M` |
| 4 | [FAPI-FND-040 — Interactive documentation, OpenAPI inspection, and simple API clients](CURRICULUM.md#fapi-fnd-040) | `S` |
| 5 | [FAPI-HTTP-010 — HTTP message anatomy, methods, status codes, and media types](CURRICULUM.md#fapi-http-010) | `L` |
| 6 | [FAPI-HTTP-020 — URLs, path/query semantics, request bodies, encoding, and JSON](CURRICULUM.md#fapi-http-020) | `M` |
| 7 | [FAPI-ASGI-010 — WSGI versus ASGI and the protocol boundary](CURRICULUM.md#fapi-asgi-010) | `L` |
| 8 | [FAPI-ASGI-020 — ASGI scope, receive, send, and the HTTP lifecycle](CURRICULUM.md#fapi-asgi-020) | `L` |
| 9 | [FAPI-ASGI-030 — Starlette beneath FastAPI: requests, responses, routing, and exceptions](CURRICULUM.md#fapi-asgi-030) | `L` |
| 10 | [FAPI-PYD-010 — BaseModel fields: required, optional, nullable, defaults, and factories](CURRICULUM.md#fapi-pyd-010) | `M` |
| 11 | [FAPI-PYD-020 — Coercion, strict validation, constraints, and Annotated](CURRICULUM.md#fapi-pyd-020) | `L` |
| 12 | [FAPI-PYD-030 — Model configuration, extra fields, frozen models, copying, and trusted construction](CURRICULUM.md#fapi-pyd-030) | `L` |
| 13 | [FAPI-PYD-040 — Nested and recursive models, forward annotations, unions, and discriminators](CURRICULUM.md#fapi-pyd-040) | `L` |
| 14 | [FAPI-PYD-060 — Aliases, validation aliases, serialization aliases, and alias generators](CURRICULUM.md#fapi-pyd-060) | `M` |
| 15 | [FAPI-PYD-070 — Field and model validators: modes, ordering, context, and defaults](CURRICULUM.md#fapi-pyd-070) | `XL` |
| 16 | [FAPI-PYD-080 — Serialization, serializers, computed fields, and inclusion or exclusion](CURRICULUM.md#fapi-pyd-080) | `L` |
| 17 | [FAPI-PYD-090 — JSON Schema, OpenAPI interaction, and custom types](CURRICULUM.md#fapi-pyd-090) | `XL` |
| 18 | [FAPI-PYD-120 — Pydantic performance, validator side effects, v1-to-v2 migration, and common mistakes](CURRICULUM.md#fapi-pyd-120) | `XL` |
| 19 | [FAPI-APP-010 — Path operations, router matching, route order, and conflicts](CURRICULUM.md#fapi-app-010) | `M` |
| 20 | [FAPI-APP-020 — Path and query parameters, constraints, aliases, and custom parsing](CURRICULUM.md#fapi-app-020) | `L` |
| 21 | [FAPI-APP-040 — Request bodies, multiple body parameters, embedding, and aliases](CURRICULUM.md#fapi-app-040) | `L` |
| 22 | [FAPI-APP-060 — Response models, output validation, serialization, status, headers, and cookies](CURRICULUM.md#fapi-app-060) | `L` |
| 23 | [FAPI-APP-080 — APIRouter, nested routers, tags, operation IDs, and route organization](CURRICULUM.md#fapi-app-080) | `L` |
| 24 | [FAPI-APP-100 — OpenAPI metadata, examples, callbacks, webhooks, and schema quality](CURRICULUM.md#fapi-app-100) | `L` |
| 25 | [FAPI-TST-010 — Testing strategy, observable contracts, and test boundaries](CURRICULUM.md#fapi-tst-010) | `L` |
| 26 | [FAPI-TST-040 — Property-based testing for Pydantic models and API contracts](CURRICULUM.md#fapi-tst-040) | `L` |

### Project milestones

- [FAPI-PRJ-010 — First typed CRUD API](PROJECTS.md#fapi-prj-010)

<a id="postgres-sqlalchemy-alembic"></a>
## PostgreSQL, SQLAlchemy, and Alembic path

For database modelling, transactions, async ORM behavior, migrations, and production schema evolution.

<!-- path-meta: {"slug":"postgres-sqlalchemy-alembic","declared_units":53,"rapid_unit_minutes":[2515,3790],"lab_minutes":[720,1080],"recall_minutes":[240,360],"mock_minutes":[120,180],"checkpoint_minutes":[180,300],"rapid_total_minutes":[3775,5710],"full_mastery_hours":[515,912],"assumed_prerequisites":[]} -->
| Component | Count or time |
|---|---:|
| Canonical units | 53 |
| Rapid unit study | 41 h 55 min–63 h 10 min |
| Selected practice/labs | 0 checkpoints; 12 h–18 h |
| Recall and comparison | 4 h–6 h |
| Mock interviews | 2 h–3 h |
| Project checkpoints | 3 h–5 h |
| **Rapid path total** | **62 h 55 min–95 h 10 min** |
| Full mastery of included units | 515–912 h |

### Assumed prior knowledge or prerequisite bridges

None. The path includes its canonical prerequisites.

### Recommended sequence

| # | Unit | Size |
|---:|---|:---:|
| 1 | [FAPI-FND-010 — Python runtime, uv project, and reproducible environment](CURRICULUM.md#fapi-fnd-010) | `M` |
| 2 | [FAPI-FND-020 — Minimal FastAPI application and first route](CURRICULUM.md#fapi-fnd-020) | `S` |
| 3 | [FAPI-FND-030 — Application entry points, import strings, reload, and server startup](CURRICULUM.md#fapi-fnd-030) | `M` |
| 4 | [FAPI-FND-040 — Interactive documentation, OpenAPI inspection, and simple API clients](CURRICULUM.md#fapi-fnd-040) | `S` |
| 5 | [FAPI-FND-050 — Configuration, environment variables, and application factories](CURRICULUM.md#fapi-fnd-050) | `M` |
| 6 | [FAPI-HTTP-010 — HTTP message anatomy, methods, status codes, and media types](CURRICULUM.md#fapi-http-010) | `L` |
| 7 | [FAPI-HTTP-020 — URLs, path/query semantics, request bodies, encoding, and JSON](CURRICULUM.md#fapi-http-020) | `M` |
| 8 | [FAPI-HTTP-030 — Headers, cookies, content negotiation, and representation metadata](CURRICULUM.md#fapi-http-030) | `M` |
| 9 | [FAPI-HTTP-040 — REST resources, actions, RPC-style endpoints, and practical constraints](CURRICULUM.md#fapi-http-040) | `L` |
| 10 | [FAPI-HTTP-070 — Partial updates, idempotency keys, and conditional writes](CURRICULUM.md#fapi-http-070) | `L` |
| 11 | [FAPI-ASGI-010 — WSGI versus ASGI and the protocol boundary](CURRICULUM.md#fapi-asgi-010) | `L` |
| 12 | [FAPI-ASGI-020 — ASGI scope, receive, send, and the HTTP lifecycle](CURRICULUM.md#fapi-asgi-020) | `L` |
| 13 | [FAPI-ASGI-030 — Starlette beneath FastAPI: requests, responses, routing, and exceptions](CURRICULUM.md#fapi-asgi-030) | `L` |
| 14 | [FAPI-ASGI-040 — Lifespan, application state, and resource ownership](CURRICULUM.md#fapi-asgi-040) | `L` |
| 15 | [FAPI-PYD-010 — BaseModel fields: required, optional, nullable, defaults, and factories](CURRICULUM.md#fapi-pyd-010) | `M` |
| 16 | [FAPI-PYD-020 — Coercion, strict validation, constraints, and Annotated](CURRICULUM.md#fapi-pyd-020) | `L` |
| 17 | [FAPI-PYD-030 — Model configuration, extra fields, frozen models, copying, and trusted construction](CURRICULUM.md#fapi-pyd-030) | `L` |
| 18 | [FAPI-PYD-060 — Aliases, validation aliases, serialization aliases, and alias generators](CURRICULUM.md#fapi-pyd-060) | `M` |
| 19 | [FAPI-PYD-080 — Serialization, serializers, computed fields, and inclusion or exclusion](CURRICULUM.md#fapi-pyd-080) | `L` |
| 20 | [FAPI-PYD-110 — Object-attribute validation and model boundaries](CURRICULUM.md#fapi-pyd-110) | `L` |
| 21 | [FAPI-APP-010 — Path operations, router matching, route order, and conflicts](CURRICULUM.md#fapi-app-010) | `M` |
| 22 | [FAPI-APP-020 — Path and query parameters, constraints, aliases, and custom parsing](CURRICULUM.md#fapi-app-020) | `L` |
| 23 | [FAPI-APP-040 — Request bodies, multiple body parameters, embedding, and aliases](CURRICULUM.md#fapi-app-040) | `L` |
| 24 | [FAPI-APP-060 — Response models, output validation, serialization, status, headers, and cookies](CURRICULUM.md#fapi-app-060) | `L` |
| 25 | [FAPI-APP-080 — APIRouter, nested routers, tags, operation IDs, and route organization](CURRICULUM.md#fapi-app-080) | `L` |
| 26 | [FAPI-DEP-010 — Callable, class-based, and parameterized dependencies](CURRICULUM.md#fapi-dep-010) | `L` |
| 27 | [FAPI-DEP-020 — Subdependencies and dependency-graph resolution](CURRICULUM.md#fapi-dep-020) | `L` |
| 28 | [FAPI-DEP-040 — Yield dependencies, setup/teardown order, scopes, and resource safety](CURRICULUM.md#fapi-dep-040) | `XL` |
| 29 | [FAPI-DEP-060 — Router/global dependencies and test overrides](CURRICULUM.md#fapi-dep-060) | `L` |
| 30 | [FAPI-DEP-070 — Request state, composition roots, service location, and dependency boundaries](CURRICULUM.md#fapi-dep-070) | `XL` |
| 31 | [FAPI-DB-010 — Relational modelling and PostgreSQL constraints for APIs](CURRICULUM.md#fapi-db-010) | `L` |
| 32 | [FAPI-DB-020 — PostgreSQL drivers, SQLAlchemy engines, URLs, and connection pools](CURRICULUM.md#fapi-db-020) | `L` |
| 33 | [FAPI-DB-030 — SQLAlchemy typed declarative mappings, columns, and constraints](CURRICULUM.md#fapi-db-030) | `L` |
| 34 | [FAPI-DB-040 — Session per request, identity map, and unit-of-work lifecycle](CURRICULUM.md#fapi-db-040) | `XL` |
| 35 | [FAPI-DB-050 — Transactions, flush, commit, rollback, refresh, expiration, and savepoints](CURRICULUM.md#fapi-db-050) | `XL` |
| 36 | [FAPI-DB-070 — AsyncEngine, AsyncSession, and preventing implicit I/O](CURRICULUM.md#fapi-db-070) | `XL` |
| 37 | [FAPI-DB-100 — Locking, isolation levels, deadlocks, retries, and optimistic concurrency](CURRICULUM.md#fapi-db-100) | `XL` |
| 38 | [FAPI-DB-120 — Database test isolation, mapping boundaries, repositories, and direct SQLAlchemy](CURRICULUM.md#fapi-db-120) | `XL` |
| 39 | [FAPI-MIG-010 — Alembic environment, configuration, metadata discovery, and revision graph](CURRICULUM.md#fapi-mig-010) | `L` |
| 40 | [FAPI-MIG-020 — First migration, upgrade, downgrade, current, and history](CURRICULUM.md#fapi-mig-020) | `L` |
| 41 | [FAPI-MIG-030 — Autogenerate review, naming conventions, constraints, indexes, and defaults](CURRICULUM.md#fapi-mig-030) | `XL` |
| 42 | [FAPI-MIG-040 — Data migrations, backfills, enum changes, and offline SQL](CURRICULUM.md#fapi-mig-040) | `XL` |
| 43 | [FAPI-MIG-060 — Async application integration, migration testing, and drift detection](CURRICULUM.md#fapi-mig-060) | `L` |
| 44 | [FAPI-MIG-070 — Expand-and-contract changes, locks, compatibility windows, and rollback decisions](CURRICULUM.md#fapi-mig-070) | `XL` |
| 45 | [FAPI-ARC-010 — From a single file to routers and feature modules](CURRICULUM.md#fapi-arc-010) | `L` |
| 46 | [FAPI-ARC-020 — Layered architecture versus vertical slices](CURRICULUM.md#fapi-arc-020) | `L` |
| 47 | [FAPI-ARC-030 — Service layer, functional core, domain services, DTO mapping, and orchestration](CURRICULUM.md#fapi-arc-030) | `L` |
| 48 | [FAPI-ARC-050 — Composition root, dependency inversion, and error translation](CURRICULUM.md#fapi-arc-050) | `L` |
| 49 | [FAPI-TST-010 — Testing strategy, observable contracts, and test boundaries](CURRICULUM.md#fapi-tst-010) | `L` |
| 50 | [FAPI-TST-020 — TestClient, HTTPX AsyncClient, ASGI transports, and lifespan-aware tests](CURRICULUM.md#fapi-tst-020) | `L` |
| 51 | [FAPI-TST-050 — PostgreSQL integration tests, transaction isolation, fixtures, and factories](CURRICULUM.md#fapi-tst-050) | `XL` |
| 52 | [FAPI-TST-060 — Alembic migration tests and schema-compatibility checks](CURRICULUM.md#fapi-tst-060) | `L` |
| 53 | [FAPI-SYN-030 — PostgreSQL, SQLAlchemy, Alembic, and architecture interview synthesis](CURRICULUM.md#fapi-syn-030) | `XL` |

### Project milestones

- [FAPI-PRJ-020 — PostgreSQL catalog and ordering service](PROJECTS.md#fapi-prj-020)
- [FAPI-PRJ-040 — Synthetic review and workflow platform](PROJECTS.md#fapi-prj-040)

<a id="async-concurrency-performance"></a>
## Async, concurrency, and performance path

For event-loop judgment, cancellation, jobs, streaming, pools, workers, caches, and measurement.

<!-- path-meta: {"slug":"async-concurrency-performance","declared_units":67,"rapid_unit_minutes":[3195,4830],"lab_minutes":[600,900],"recall_minutes":[180,300],"mock_minutes":[120,180],"checkpoint_minutes":[180,300],"rapid_total_minutes":[4275,6510],"full_mastery_hours":[655,1160],"assumed_prerequisites":[]} -->
| Component | Count or time |
|---|---:|
| Canonical units | 67 |
| Rapid unit study | 53 h 15 min–80 h 30 min |
| Selected practice/labs | 0 checkpoints; 10 h–15 h |
| Recall and comparison | 3 h–5 h |
| Mock interviews | 2 h–3 h |
| Project checkpoints | 3 h–5 h |
| **Rapid path total** | **71 h 15 min–108 h 30 min** |
| Full mastery of included units | 655–1160 h |

### Assumed prior knowledge or prerequisite bridges

None. The path includes its canonical prerequisites.

### Recommended sequence

| # | Unit | Size |
|---:|---|:---:|
| 1 | [FAPI-FND-010 — Python runtime, uv project, and reproducible environment](CURRICULUM.md#fapi-fnd-010) | `M` |
| 2 | [FAPI-FND-020 — Minimal FastAPI application and first route](CURRICULUM.md#fapi-fnd-020) | `S` |
| 3 | [FAPI-FND-030 — Application entry points, import strings, reload, and server startup](CURRICULUM.md#fapi-fnd-030) | `M` |
| 4 | [FAPI-FND-040 — Interactive documentation, OpenAPI inspection, and simple API clients](CURRICULUM.md#fapi-fnd-040) | `S` |
| 5 | [FAPI-FND-050 — Configuration, environment variables, and application factories](CURRICULUM.md#fapi-fnd-050) | `M` |
| 6 | [FAPI-HTTP-010 — HTTP message anatomy, methods, status codes, and media types](CURRICULUM.md#fapi-http-010) | `L` |
| 7 | [FAPI-HTTP-020 — URLs, path/query semantics, request bodies, encoding, and JSON](CURRICULUM.md#fapi-http-020) | `M` |
| 8 | [FAPI-HTTP-030 — Headers, cookies, content negotiation, and representation metadata](CURRICULUM.md#fapi-http-030) | `M` |
| 9 | [FAPI-HTTP-040 — REST resources, actions, RPC-style endpoints, and practical constraints](CURRICULUM.md#fapi-http-040) | `L` |
| 10 | [FAPI-HTTP-050 — Error contracts, RFC problem details, and API versioning](CURRICULUM.md#fapi-http-050) | `L` |
| 11 | [FAPI-HTTP-060 — Pagination, filtering, sorting, and field selection](CURRICULUM.md#fapi-http-060) | `L` |
| 12 | [FAPI-HTTP-070 — Partial updates, idempotency keys, and conditional writes](CURRICULUM.md#fapi-http-070) | `L` |
| 13 | [FAPI-ASGI-010 — WSGI versus ASGI and the protocol boundary](CURRICULUM.md#fapi-asgi-010) | `L` |
| 14 | [FAPI-ASGI-020 — ASGI scope, receive, send, and the HTTP lifecycle](CURRICULUM.md#fapi-asgi-020) | `L` |
| 15 | [FAPI-ASGI-030 — Starlette beneath FastAPI: requests, responses, routing, and exceptions](CURRICULUM.md#fapi-asgi-030) | `L` |
| 16 | [FAPI-ASGI-040 — Lifespan, application state, and resource ownership](CURRICULUM.md#fapi-asgi-040) | `L` |
| 17 | [FAPI-ASGI-050 — ASGI middleware onion, exception flow, and ordering](CURRICULUM.md#fapi-asgi-050) | `L` |
| 18 | [FAPI-ASGI-060 — Client disconnects, cancellation, and streaming lifecycle](CURRICULUM.md#fapi-asgi-060) | `L` |
| 19 | [FAPI-ASGI-070 — ASGI servers, workers, proxy headers, root paths, and mounted applications](CURRICULUM.md#fapi-asgi-070) | `L` |
| 20 | [FAPI-PYD-010 — BaseModel fields: required, optional, nullable, defaults, and factories](CURRICULUM.md#fapi-pyd-010) | `M` |
| 21 | [FAPI-PYD-020 — Coercion, strict validation, constraints, and Annotated](CURRICULUM.md#fapi-pyd-020) | `L` |
| 22 | [FAPI-PYD-030 — Model configuration, extra fields, frozen models, copying, and trusted construction](CURRICULUM.md#fapi-pyd-030) | `L` |
| 23 | [FAPI-PYD-060 — Aliases, validation aliases, serialization aliases, and alias generators](CURRICULUM.md#fapi-pyd-060) | `M` |
| 24 | [FAPI-PYD-080 — Serialization, serializers, computed fields, and inclusion or exclusion](CURRICULUM.md#fapi-pyd-080) | `L` |
| 25 | [FAPI-PYD-100 — Pydantic Settings: source precedence, env files, secrets, nesting, and custom sources](CURRICULUM.md#fapi-pyd-100) | `L` |
| 26 | [FAPI-PYD-110 — Object-attribute validation and model boundaries](CURRICULUM.md#fapi-pyd-110) | `L` |
| 27 | [FAPI-APP-010 — Path operations, router matching, route order, and conflicts](CURRICULUM.md#fapi-app-010) | `M` |
| 28 | [FAPI-APP-020 — Path and query parameters, constraints, aliases, and custom parsing](CURRICULUM.md#fapi-app-020) | `L` |
| 29 | [FAPI-APP-040 — Request bodies, multiple body parameters, embedding, and aliases](CURRICULUM.md#fapi-app-040) | `L` |
| 30 | [FAPI-APP-050 — Forms, multipart data, file uploads, and UploadFile](CURRICULUM.md#fapi-app-050) | `L` |
| 31 | [FAPI-APP-060 — Response models, output validation, serialization, status, headers, and cookies](CURRICULUM.md#fapi-app-060) | `L` |
| 32 | [FAPI-APP-080 — APIRouter, nested routers, tags, operation IDs, and route organization](CURRICULUM.md#fapi-app-080) | `L` |
| 33 | [FAPI-APP-090 — HTTP exceptions, validation errors, custom handlers, and error translation](CURRICULUM.md#fapi-app-090) | `L` |
| 34 | [FAPI-DEP-010 — Callable, class-based, and parameterized dependencies](CURRICULUM.md#fapi-dep-010) | `L` |
| 35 | [FAPI-DEP-020 — Subdependencies and dependency-graph resolution](CURRICULUM.md#fapi-dep-020) | `L` |
| 36 | [FAPI-DEP-040 — Yield dependencies, setup/teardown order, scopes, and resource safety](CURRICULUM.md#fapi-dep-040) | `XL` |
| 37 | [FAPI-DEP-050 — Authentication and authorization dependencies](CURRICULUM.md#fapi-dep-050) | `L` |
| 38 | [FAPI-DEP-060 — Router/global dependencies and test overrides](CURRICULUM.md#fapi-dep-060) | `L` |
| 39 | [FAPI-DEP-070 — Request state, composition roots, service location, and dependency boundaries](CURRICULUM.md#fapi-dep-070) | `XL` |
| 40 | [FAPI-MID-010 — Function, class-based, and raw ASGI middleware ordering](CURRICULUM.md#fapi-mid-010) | `L` |
| 41 | [FAPI-MID-020 — Request IDs, structured logging, context variables, and correlation](CURRICULUM.md#fapi-mid-020) | `L` |
| 42 | [FAPI-MID-050 — Rate limiting, observability, and choosing middleware versus dependencies](CURRICULUM.md#fapi-mid-050) | `L` |
| 43 | [FAPI-DB-010 — Relational modelling and PostgreSQL constraints for APIs](CURRICULUM.md#fapi-db-010) | `L` |
| 44 | [FAPI-DB-020 — PostgreSQL drivers, SQLAlchemy engines, URLs, and connection pools](CURRICULUM.md#fapi-db-020) | `L` |
| 45 | [FAPI-DB-030 — SQLAlchemy typed declarative mappings, columns, and constraints](CURRICULUM.md#fapi-db-030) | `L` |
| 46 | [FAPI-DB-040 — Session per request, identity map, and unit-of-work lifecycle](CURRICULUM.md#fapi-db-040) | `XL` |
| 47 | [FAPI-DB-050 — Transactions, flush, commit, rollback, refresh, expiration, and savepoints](CURRICULUM.md#fapi-db-050) | `XL` |
| 48 | [FAPI-DB-060 — Relationships, cascades, eager/lazy loading, and object graphs](CURRICULUM.md#fapi-db-060) | `L` |
| 49 | [FAPI-DB-070 — AsyncEngine, AsyncSession, and preventing implicit I/O](CURRICULUM.md#fapi-db-070) | `XL` |
| 50 | [FAPI-DB-080 — Queries, joins, aggregates, filtering, sorting, and pagination](CURRICULUM.md#fapi-db-080) | `L` |
| 51 | [FAPI-DB-090 — N+1 diagnosis, eager loading, query plans, and indexes](CURRICULUM.md#fapi-db-090) | `XL` |
| 52 | [FAPI-DB-110 — Bulk work, generated values, timestamps, soft deletion, and tenant boundaries](CURRICULUM.md#fapi-db-110) | `L` |
| 53 | [FAPI-ASY-010 — def versus async def, event-loop execution, and thread-pool dispatch](CURRICULUM.md#fapi-asy-010) | `L` |
| 54 | [FAPI-ASY-070 — Workers, processes, concurrency limits, pool sizing, and shared state](CURRICULUM.md#fapi-asy-070) | `XL` |
| 55 | [FAPI-ASY-090 — Profiling, load testing, benchmarking, and evidence-led performance diagnosis](CURRICULUM.md#fapi-asy-090) | `XL` |
| 56 | [FAPI-SEC-010 — Authentication, authorization, and API threat modelling](CURRICULUM.md#fapi-sec-010) | `L` |
| 57 | [FAPI-SEC-060 — RBAC, ABAC, object-level authorization, and tenant isolation](CURRICULUM.md#fapi-sec-060) | `XL` |
| 58 | [FAPI-SEC-080 — Validation boundaries, mass assignment, SQL injection, SSRF, uploads, and path traversal](CURRICULUM.md#fapi-sec-080) | `XL` |
| 59 | [FAPI-SEC-090 — Rate limits, brute-force controls, replay, idempotency, audit, and sensitive logging](CURRICULUM.md#fapi-sec-090) | `XL` |
| 60 | [FAPI-SEC-100 — Secrets, dependency vulnerabilities, authorization tests, and security review](CURRICULUM.md#fapi-sec-100) | `L` |
| 61 | [FAPI-TST-010 — Testing strategy, observable contracts, and test boundaries](CURRICULUM.md#fapi-tst-010) | `L` |
| 62 | [FAPI-TST-020 — TestClient, HTTPX AsyncClient, ASGI transports, and lifespan-aware tests](CURRICULUM.md#fapi-tst-020) | `L` |
| 63 | [FAPI-TST-030 — Dependency overrides, auth tests, validation errors, and OpenAPI contracts](CURRICULUM.md#fapi-tst-030) | `L` |
| 64 | [FAPI-TST-080 — Timeout, retry, concurrency, load, performance, and security-focused tests](CURRICULUM.md#fapi-tst-080) | `XL` |
| 65 | [FAPI-OPS-020 — Uvicorn process model, workers, startup, shutdown, and graceful draining](CURRICULUM.md#fapi-ops-020) | `L` |
| 66 | [FAPI-OPS-050 — Structured logs, metrics, traces, and request-span propagation](CURRICULUM.md#fapi-ops-050) | `XL` |
| 67 | [FAPI-OPS-060 — Capacity planning, worker/pool limits, load tests, and performance budgets](CURRICULUM.md#fapi-ops-060) | `XL` |

### Project milestones

- [FAPI-PRJ-050 — File-processing and durable-job service](PROJECTS.md#fapi-prj-050)
- [FAPI-PRJ-060 — Real-time operations dashboard](PROJECTS.md#fapi-prj-060)

<a id="security-authentication"></a>
## Security and authentication path

For practical API threat modelling, credentials, tokens, browser security, authorization, tenancy, and security tests.

<!-- path-meta: {"slug":"security-authentication","declared_units":59,"rapid_unit_minutes":[2660,4060],"lab_minutes":[600,900],"recall_minutes":[180,300],"mock_minutes":[120,180],"checkpoint_minutes":[180,300],"rapid_total_minutes":[3740,5740],"full_mastery_hours":[534,948],"assumed_prerequisites":[]} -->
| Component | Count or time |
|---|---:|
| Canonical units | 59 |
| Rapid unit study | 44 h 20 min–67 h 40 min |
| Selected practice/labs | 0 checkpoints; 10 h–15 h |
| Recall and comparison | 3 h–5 h |
| Mock interviews | 2 h–3 h |
| Project checkpoints | 3 h–5 h |
| **Rapid path total** | **62 h 20 min–95 h 40 min** |
| Full mastery of included units | 534–948 h |

### Assumed prior knowledge or prerequisite bridges

None. The path includes its canonical prerequisites.

### Recommended sequence

| # | Unit | Size |
|---:|---|:---:|
| 1 | [FAPI-FND-010 — Python runtime, uv project, and reproducible environment](CURRICULUM.md#fapi-fnd-010) | `M` |
| 2 | [FAPI-FND-020 — Minimal FastAPI application and first route](CURRICULUM.md#fapi-fnd-020) | `S` |
| 3 | [FAPI-FND-030 — Application entry points, import strings, reload, and server startup](CURRICULUM.md#fapi-fnd-030) | `M` |
| 4 | [FAPI-FND-040 — Interactive documentation, OpenAPI inspection, and simple API clients](CURRICULUM.md#fapi-fnd-040) | `S` |
| 5 | [FAPI-FND-050 — Configuration, environment variables, and application factories](CURRICULUM.md#fapi-fnd-050) | `M` |
| 6 | [FAPI-HTTP-010 — HTTP message anatomy, methods, status codes, and media types](CURRICULUM.md#fapi-http-010) | `L` |
| 7 | [FAPI-HTTP-020 — URLs, path/query semantics, request bodies, encoding, and JSON](CURRICULUM.md#fapi-http-020) | `M` |
| 8 | [FAPI-HTTP-030 — Headers, cookies, content negotiation, and representation metadata](CURRICULUM.md#fapi-http-030) | `M` |
| 9 | [FAPI-HTTP-040 — REST resources, actions, RPC-style endpoints, and practical constraints](CURRICULUM.md#fapi-http-040) | `L` |
| 10 | [FAPI-HTTP-050 — Error contracts, RFC problem details, and API versioning](CURRICULUM.md#fapi-http-050) | `L` |
| 11 | [FAPI-HTTP-060 — Pagination, filtering, sorting, and field selection](CURRICULUM.md#fapi-http-060) | `L` |
| 12 | [FAPI-HTTP-070 — Partial updates, idempotency keys, and conditional writes](CURRICULUM.md#fapi-http-070) | `L` |
| 13 | [FAPI-ASGI-010 — WSGI versus ASGI and the protocol boundary](CURRICULUM.md#fapi-asgi-010) | `L` |
| 14 | [FAPI-ASGI-020 — ASGI scope, receive, send, and the HTTP lifecycle](CURRICULUM.md#fapi-asgi-020) | `L` |
| 15 | [FAPI-ASGI-030 — Starlette beneath FastAPI: requests, responses, routing, and exceptions](CURRICULUM.md#fapi-asgi-030) | `L` |
| 16 | [FAPI-ASGI-040 — Lifespan, application state, and resource ownership](CURRICULUM.md#fapi-asgi-040) | `L` |
| 17 | [FAPI-ASGI-050 — ASGI middleware onion, exception flow, and ordering](CURRICULUM.md#fapi-asgi-050) | `L` |
| 18 | [FAPI-ASGI-070 — ASGI servers, workers, proxy headers, root paths, and mounted applications](CURRICULUM.md#fapi-asgi-070) | `L` |
| 19 | [FAPI-PYD-010 — BaseModel fields: required, optional, nullable, defaults, and factories](CURRICULUM.md#fapi-pyd-010) | `M` |
| 20 | [FAPI-PYD-020 — Coercion, strict validation, constraints, and Annotated](CURRICULUM.md#fapi-pyd-020) | `L` |
| 21 | [FAPI-PYD-030 — Model configuration, extra fields, frozen models, copying, and trusted construction](CURRICULUM.md#fapi-pyd-030) | `L` |
| 22 | [FAPI-PYD-060 — Aliases, validation aliases, serialization aliases, and alias generators](CURRICULUM.md#fapi-pyd-060) | `M` |
| 23 | [FAPI-PYD-080 — Serialization, serializers, computed fields, and inclusion or exclusion](CURRICULUM.md#fapi-pyd-080) | `L` |
| 24 | [FAPI-PYD-100 — Pydantic Settings: source precedence, env files, secrets, nesting, and custom sources](CURRICULUM.md#fapi-pyd-100) | `L` |
| 25 | [FAPI-PYD-110 — Object-attribute validation and model boundaries](CURRICULUM.md#fapi-pyd-110) | `L` |
| 26 | [FAPI-APP-010 — Path operations, router matching, route order, and conflicts](CURRICULUM.md#fapi-app-010) | `M` |
| 27 | [FAPI-APP-020 — Path and query parameters, constraints, aliases, and custom parsing](CURRICULUM.md#fapi-app-020) | `L` |
| 28 | [FAPI-APP-040 — Request bodies, multiple body parameters, embedding, and aliases](CURRICULUM.md#fapi-app-040) | `L` |
| 29 | [FAPI-APP-050 — Forms, multipart data, file uploads, and UploadFile](CURRICULUM.md#fapi-app-050) | `L` |
| 30 | [FAPI-APP-060 — Response models, output validation, serialization, status, headers, and cookies](CURRICULUM.md#fapi-app-060) | `L` |
| 31 | [FAPI-APP-080 — APIRouter, nested routers, tags, operation IDs, and route organization](CURRICULUM.md#fapi-app-080) | `L` |
| 32 | [FAPI-APP-090 — HTTP exceptions, validation errors, custom handlers, and error translation](CURRICULUM.md#fapi-app-090) | `L` |
| 33 | [FAPI-DEP-010 — Callable, class-based, and parameterized dependencies](CURRICULUM.md#fapi-dep-010) | `L` |
| 34 | [FAPI-DEP-020 — Subdependencies and dependency-graph resolution](CURRICULUM.md#fapi-dep-020) | `L` |
| 35 | [FAPI-DEP-040 — Yield dependencies, setup/teardown order, scopes, and resource safety](CURRICULUM.md#fapi-dep-040) | `XL` |
| 36 | [FAPI-DEP-050 — Authentication and authorization dependencies](CURRICULUM.md#fapi-dep-050) | `L` |
| 37 | [FAPI-DEP-060 — Router/global dependencies and test overrides](CURRICULUM.md#fapi-dep-060) | `L` |
| 38 | [FAPI-DEP-070 — Request state, composition roots, service location, and dependency boundaries](CURRICULUM.md#fapi-dep-070) | `XL` |
| 39 | [FAPI-MID-010 — Function, class-based, and raw ASGI middleware ordering](CURRICULUM.md#fapi-mid-010) | `L` |
| 40 | [FAPI-MID-020 — Request IDs, structured logging, context variables, and correlation](CURRICULUM.md#fapi-mid-020) | `L` |
| 41 | [FAPI-MID-030 — CORS, trusted hosts, HTTPS redirects, compression, and sessions](CURRICULUM.md#fapi-mid-030) | `L` |
| 42 | [FAPI-MID-050 — Rate limiting, observability, and choosing middleware versus dependencies](CURRICULUM.md#fapi-mid-050) | `L` |
| 43 | [FAPI-DB-010 — Relational modelling and PostgreSQL constraints for APIs](CURRICULUM.md#fapi-db-010) | `L` |
| 44 | [FAPI-DB-020 — PostgreSQL drivers, SQLAlchemy engines, URLs, and connection pools](CURRICULUM.md#fapi-db-020) | `L` |
| 45 | [FAPI-DB-030 — SQLAlchemy typed declarative mappings, columns, and constraints](CURRICULUM.md#fapi-db-030) | `L` |
| 46 | [FAPI-DB-040 — Session per request, identity map, and unit-of-work lifecycle](CURRICULUM.md#fapi-db-040) | `XL` |
| 47 | [FAPI-DB-050 — Transactions, flush, commit, rollback, refresh, expiration, and savepoints](CURRICULUM.md#fapi-db-050) | `XL` |
| 48 | [FAPI-DB-080 — Queries, joins, aggregates, filtering, sorting, and pagination](CURRICULUM.md#fapi-db-080) | `L` |
| 49 | [FAPI-DB-110 — Bulk work, generated values, timestamps, soft deletion, and tenant boundaries](CURRICULUM.md#fapi-db-110) | `L` |
| 50 | [FAPI-SEC-010 — Authentication, authorization, and API threat modelling](CURRICULUM.md#fapi-sec-010) | `L` |
| 51 | [FAPI-SEC-060 — RBAC, ABAC, object-level authorization, and tenant isolation](CURRICULUM.md#fapi-sec-060) | `XL` |
| 52 | [FAPI-SEC-070 — CORS, trusted hosts, HTTPS, proxy trust, and security headers](CURRICULUM.md#fapi-sec-070) | `L` |
| 53 | [FAPI-SEC-080 — Validation boundaries, mass assignment, SQL injection, SSRF, uploads, and path traversal](CURRICULUM.md#fapi-sec-080) | `XL` |
| 54 | [FAPI-SEC-090 — Rate limits, brute-force controls, replay, idempotency, audit, and sensitive logging](CURRICULUM.md#fapi-sec-090) | `XL` |
| 55 | [FAPI-SEC-100 — Secrets, dependency vulnerabilities, authorization tests, and security review](CURRICULUM.md#fapi-sec-100) | `L` |
| 56 | [FAPI-TST-010 — Testing strategy, observable contracts, and test boundaries](CURRICULUM.md#fapi-tst-010) | `L` |
| 57 | [FAPI-TST-020 — TestClient, HTTPX AsyncClient, ASGI transports, and lifespan-aware tests](CURRICULUM.md#fapi-tst-020) | `L` |
| 58 | [FAPI-TST-030 — Dependency overrides, auth tests, validation errors, and OpenAPI contracts](CURRICULUM.md#fapi-tst-030) | `L` |
| 59 | [FAPI-OPS-030 — Reverse proxies, forwarded headers, root paths, TLS, and trust](CURRICULUM.md#fapi-ops-030) | `L` |

### Project milestones

- [FAPI-PRJ-030 — Authenticated multi-tenant service](PROJECTS.md#fapi-prj-030)

<a id="api-architecture-production"></a>
## API architecture and production path

For modularity, transaction ownership, operations, observability, deployment, and incident reasoning.

<!-- path-meta: {"slug":"api-architecture-production","declared_units":65,"rapid_unit_minutes":[3180,4790],"lab_minutes":[840,1200],"recall_minutes":[240,360],"mock_minutes":[180,240],"checkpoint_minutes":[240,360],"rapid_total_minutes":[4680,6950],"full_mastery_hours":[658,1164],"assumed_prerequisites":[]} -->
| Component | Count or time |
|---|---:|
| Canonical units | 65 |
| Rapid unit study | 53 h–79 h 50 min |
| Selected practice/labs | 0 checkpoints; 14 h–20 h |
| Recall and comparison | 4 h–6 h |
| Mock interviews | 3 h–4 h |
| Project checkpoints | 4 h–6 h |
| **Rapid path total** | **78 h–115 h 50 min** |
| Full mastery of included units | 658–1164 h |

### Assumed prior knowledge or prerequisite bridges

None. The path includes its canonical prerequisites.

### Recommended sequence

| # | Unit | Size |
|---:|---|:---:|
| 1 | [FAPI-FND-010 — Python runtime, uv project, and reproducible environment](CURRICULUM.md#fapi-fnd-010) | `M` |
| 2 | [FAPI-FND-020 — Minimal FastAPI application and first route](CURRICULUM.md#fapi-fnd-020) | `S` |
| 3 | [FAPI-FND-030 — Application entry points, import strings, reload, and server startup](CURRICULUM.md#fapi-fnd-030) | `M` |
| 4 | [FAPI-FND-050 — Configuration, environment variables, and application factories](CURRICULUM.md#fapi-fnd-050) | `M` |
| 5 | [FAPI-HTTP-010 — HTTP message anatomy, methods, status codes, and media types](CURRICULUM.md#fapi-http-010) | `L` |
| 6 | [FAPI-HTTP-020 — URLs, path/query semantics, request bodies, encoding, and JSON](CURRICULUM.md#fapi-http-020) | `M` |
| 7 | [FAPI-HTTP-030 — Headers, cookies, content negotiation, and representation metadata](CURRICULUM.md#fapi-http-030) | `M` |
| 8 | [FAPI-HTTP-040 — REST resources, actions, RPC-style endpoints, and practical constraints](CURRICULUM.md#fapi-http-040) | `L` |
| 9 | [FAPI-HTTP-060 — Pagination, filtering, sorting, and field selection](CURRICULUM.md#fapi-http-060) | `L` |
| 10 | [FAPI-HTTP-070 — Partial updates, idempotency keys, and conditional writes](CURRICULUM.md#fapi-http-070) | `L` |
| 11 | [FAPI-ASGI-010 — WSGI versus ASGI and the protocol boundary](CURRICULUM.md#fapi-asgi-010) | `L` |
| 12 | [FAPI-ASGI-020 — ASGI scope, receive, send, and the HTTP lifecycle](CURRICULUM.md#fapi-asgi-020) | `L` |
| 13 | [FAPI-ASGI-030 — Starlette beneath FastAPI: requests, responses, routing, and exceptions](CURRICULUM.md#fapi-asgi-030) | `L` |
| 14 | [FAPI-ASGI-040 — Lifespan, application state, and resource ownership](CURRICULUM.md#fapi-asgi-040) | `L` |
| 15 | [FAPI-ASGI-050 — ASGI middleware onion, exception flow, and ordering](CURRICULUM.md#fapi-asgi-050) | `L` |
| 16 | [FAPI-ASGI-070 — ASGI servers, workers, proxy headers, root paths, and mounted applications](CURRICULUM.md#fapi-asgi-070) | `L` |
| 17 | [FAPI-PYD-010 — BaseModel fields: required, optional, nullable, defaults, and factories](CURRICULUM.md#fapi-pyd-010) | `M` |
| 18 | [FAPI-PYD-020 — Coercion, strict validation, constraints, and Annotated](CURRICULUM.md#fapi-pyd-020) | `L` |
| 19 | [FAPI-PYD-030 — Model configuration, extra fields, frozen models, copying, and trusted construction](CURRICULUM.md#fapi-pyd-030) | `L` |
| 20 | [FAPI-PYD-060 — Aliases, validation aliases, serialization aliases, and alias generators](CURRICULUM.md#fapi-pyd-060) | `M` |
| 21 | [FAPI-PYD-080 — Serialization, serializers, computed fields, and inclusion or exclusion](CURRICULUM.md#fapi-pyd-080) | `L` |
| 22 | [FAPI-PYD-110 — Object-attribute validation and model boundaries](CURRICULUM.md#fapi-pyd-110) | `L` |
| 23 | [FAPI-APP-010 — Path operations, router matching, route order, and conflicts](CURRICULUM.md#fapi-app-010) | `M` |
| 24 | [FAPI-APP-020 — Path and query parameters, constraints, aliases, and custom parsing](CURRICULUM.md#fapi-app-020) | `L` |
| 25 | [FAPI-APP-040 — Request bodies, multiple body parameters, embedding, and aliases](CURRICULUM.md#fapi-app-040) | `L` |
| 26 | [FAPI-APP-060 — Response models, output validation, serialization, status, headers, and cookies](CURRICULUM.md#fapi-app-060) | `L` |
| 27 | [FAPI-APP-080 — APIRouter, nested routers, tags, operation IDs, and route organization](CURRICULUM.md#fapi-app-080) | `L` |
| 28 | [FAPI-DEP-010 — Callable, class-based, and parameterized dependencies](CURRICULUM.md#fapi-dep-010) | `L` |
| 29 | [FAPI-DEP-020 — Subdependencies and dependency-graph resolution](CURRICULUM.md#fapi-dep-020) | `L` |
| 30 | [FAPI-DEP-040 — Yield dependencies, setup/teardown order, scopes, and resource safety](CURRICULUM.md#fapi-dep-040) | `XL` |
| 31 | [FAPI-DEP-060 — Router/global dependencies and test overrides](CURRICULUM.md#fapi-dep-060) | `L` |
| 32 | [FAPI-DEP-070 — Request state, composition roots, service location, and dependency boundaries](CURRICULUM.md#fapi-dep-070) | `XL` |
| 33 | [FAPI-MID-010 — Function, class-based, and raw ASGI middleware ordering](CURRICULUM.md#fapi-mid-010) | `L` |
| 34 | [FAPI-MID-020 — Request IDs, structured logging, context variables, and correlation](CURRICULUM.md#fapi-mid-020) | `L` |
| 35 | [FAPI-MID-030 — CORS, trusted hosts, HTTPS redirects, compression, and sessions](CURRICULUM.md#fapi-mid-030) | `L` |
| 36 | [FAPI-DB-010 — Relational modelling and PostgreSQL constraints for APIs](CURRICULUM.md#fapi-db-010) | `L` |
| 37 | [FAPI-DB-020 — PostgreSQL drivers, SQLAlchemy engines, URLs, and connection pools](CURRICULUM.md#fapi-db-020) | `L` |
| 38 | [FAPI-DB-030 — SQLAlchemy typed declarative mappings, columns, and constraints](CURRICULUM.md#fapi-db-030) | `L` |
| 39 | [FAPI-DB-040 — Session per request, identity map, and unit-of-work lifecycle](CURRICULUM.md#fapi-db-040) | `XL` |
| 40 | [FAPI-DB-050 — Transactions, flush, commit, rollback, refresh, expiration, and savepoints](CURRICULUM.md#fapi-db-050) | `XL` |
| 41 | [FAPI-DB-070 — AsyncEngine, AsyncSession, and preventing implicit I/O](CURRICULUM.md#fapi-db-070) | `XL` |
| 42 | [FAPI-DB-080 — Queries, joins, aggregates, filtering, sorting, and pagination](CURRICULUM.md#fapi-db-080) | `L` |
| 43 | [FAPI-DB-100 — Locking, isolation levels, deadlocks, retries, and optimistic concurrency](CURRICULUM.md#fapi-db-100) | `XL` |
| 44 | [FAPI-DB-110 — Bulk work, generated values, timestamps, soft deletion, and tenant boundaries](CURRICULUM.md#fapi-db-110) | `L` |
| 45 | [FAPI-DB-120 — Database test isolation, mapping boundaries, repositories, and direct SQLAlchemy](CURRICULUM.md#fapi-db-120) | `XL` |
| 46 | [FAPI-MIG-010 — Alembic environment, configuration, metadata discovery, and revision graph](CURRICULUM.md#fapi-mig-010) | `L` |
| 47 | [FAPI-MIG-020 — First migration, upgrade, downgrade, current, and history](CURRICULUM.md#fapi-mig-020) | `L` |
| 48 | [FAPI-MIG-030 — Autogenerate review, naming conventions, constraints, indexes, and defaults](CURRICULUM.md#fapi-mig-030) | `XL` |
| 49 | [FAPI-MIG-040 — Data migrations, backfills, enum changes, and offline SQL](CURRICULUM.md#fapi-mig-040) | `XL` |
| 50 | [FAPI-MIG-060 — Async application integration, migration testing, and drift detection](CURRICULUM.md#fapi-mig-060) | `L` |
| 51 | [FAPI-MIG-070 — Expand-and-contract changes, locks, compatibility windows, and rollback decisions](CURRICULUM.md#fapi-mig-070) | `XL` |
| 52 | [FAPI-ARC-010 — From a single file to routers and feature modules](CURRICULUM.md#fapi-arc-010) | `L` |
| 53 | [FAPI-ARC-020 — Layered architecture versus vertical slices](CURRICULUM.md#fapi-arc-020) | `L` |
| 54 | [FAPI-ARC-030 — Service layer, functional core, domain services, DTO mapping, and orchestration](CURRICULUM.md#fapi-arc-030) | `L` |
| 55 | [FAPI-ARC-040 — Repository and Unit of Work patterns with transaction ownership](CURRICULUM.md#fapi-arc-040) | `XL` |
| 56 | [FAPI-ARC-050 — Composition root, dependency inversion, and error translation](CURRICULUM.md#fapi-arc-050) | `L` |
| 57 | [FAPI-ARC-070 — Multi-tenancy, gateway boundaries, monolith/microservice choices, and stopping rules](CURRICULUM.md#fapi-arc-070) | `XL` |
| 58 | [FAPI-ASY-010 — def versus async def, event-loop execution, and thread-pool dispatch](CURRICULUM.md#fapi-asy-010) | `L` |
| 59 | [FAPI-ASY-070 — Workers, processes, concurrency limits, pool sizing, and shared state](CURRICULUM.md#fapi-asy-070) | `XL` |
| 60 | [FAPI-SEC-070 — CORS, trusted hosts, HTTPS, proxy trust, and security headers](CURRICULUM.md#fapi-sec-070) | `L` |
| 61 | [FAPI-OPS-020 — Uvicorn process model, workers, startup, shutdown, and graceful draining](CURRICULUM.md#fapi-ops-020) | `L` |
| 62 | [FAPI-OPS-030 — Reverse proxies, forwarded headers, root paths, TLS, and trust](CURRICULUM.md#fapi-ops-030) | `L` |
| 63 | [FAPI-OPS-050 — Structured logs, metrics, traces, and request-span propagation](CURRICULUM.md#fapi-ops-050) | `XL` |
| 64 | [FAPI-OPS-070 — Production debugging, incident response, deployment strategies, and rollback](CURRICULUM.md#fapi-ops-070) | `XL` |
| 65 | [FAPI-SYN-030 — PostgreSQL, SQLAlchemy, Alembic, and architecture interview synthesis](CURRICULUM.md#fapi-syn-030) | `XL` |

### Project milestones

- [FAPI-PRJ-040 — Synthetic review and workflow platform](PROJECTS.md#fapi-prj-040)
- [FAPI-PRJ-080 — Production modular backend capstone](PROJECTS.md#fapi-prj-080)

<a id="realtime-streaming-grpc"></a>
## WebSockets, SSE, streaming, and gRPC path

For long-lived transports, webhooks, streaming, scaling, and adjacent gRPC services.

<!-- path-meta: {"slug":"realtime-streaming-grpc","declared_units":72,"rapid_unit_minutes":[3445,5210],"lab_minutes":[600,900],"recall_minutes":[180,300],"mock_minutes":[120,180],"checkpoint_minutes":[180,300],"rapid_total_minutes":[4525,6890],"full_mastery_hours":[707,1252],"assumed_prerequisites":[]} -->
| Component | Count or time |
|---|---:|
| Canonical units | 72 |
| Rapid unit study | 57 h 25 min–86 h 50 min |
| Selected practice/labs | 0 checkpoints; 10 h–15 h |
| Recall and comparison | 3 h–5 h |
| Mock interviews | 2 h–3 h |
| Project checkpoints | 3 h–5 h |
| **Rapid path total** | **75 h 25 min–114 h 50 min** |
| Full mastery of included units | 707–1252 h |

### Assumed prior knowledge or prerequisite bridges

None. The path includes its canonical prerequisites.

### Recommended sequence

| # | Unit | Size |
|---:|---|:---:|
| 1 | [FAPI-FND-010 — Python runtime, uv project, and reproducible environment](CURRICULUM.md#fapi-fnd-010) | `M` |
| 2 | [FAPI-FND-020 — Minimal FastAPI application and first route](CURRICULUM.md#fapi-fnd-020) | `S` |
| 3 | [FAPI-FND-030 — Application entry points, import strings, reload, and server startup](CURRICULUM.md#fapi-fnd-030) | `M` |
| 4 | [FAPI-FND-040 — Interactive documentation, OpenAPI inspection, and simple API clients](CURRICULUM.md#fapi-fnd-040) | `S` |
| 5 | [FAPI-FND-050 — Configuration, environment variables, and application factories](CURRICULUM.md#fapi-fnd-050) | `M` |
| 6 | [FAPI-HTTP-010 — HTTP message anatomy, methods, status codes, and media types](CURRICULUM.md#fapi-http-010) | `L` |
| 7 | [FAPI-HTTP-020 — URLs, path/query semantics, request bodies, encoding, and JSON](CURRICULUM.md#fapi-http-020) | `M` |
| 8 | [FAPI-HTTP-030 — Headers, cookies, content negotiation, and representation metadata](CURRICULUM.md#fapi-http-030) | `M` |
| 9 | [FAPI-HTTP-040 — REST resources, actions, RPC-style endpoints, and practical constraints](CURRICULUM.md#fapi-http-040) | `L` |
| 10 | [FAPI-HTTP-050 — Error contracts, RFC problem details, and API versioning](CURRICULUM.md#fapi-http-050) | `L` |
| 11 | [FAPI-HTTP-060 — Pagination, filtering, sorting, and field selection](CURRICULUM.md#fapi-http-060) | `L` |
| 12 | [FAPI-HTTP-070 — Partial updates, idempotency keys, and conditional writes](CURRICULUM.md#fapi-http-070) | `L` |
| 13 | [FAPI-ASGI-010 — WSGI versus ASGI and the protocol boundary](CURRICULUM.md#fapi-asgi-010) | `L` |
| 14 | [FAPI-ASGI-020 — ASGI scope, receive, send, and the HTTP lifecycle](CURRICULUM.md#fapi-asgi-020) | `L` |
| 15 | [FAPI-ASGI-030 — Starlette beneath FastAPI: requests, responses, routing, and exceptions](CURRICULUM.md#fapi-asgi-030) | `L` |
| 16 | [FAPI-ASGI-040 — Lifespan, application state, and resource ownership](CURRICULUM.md#fapi-asgi-040) | `L` |
| 17 | [FAPI-ASGI-050 — ASGI middleware onion, exception flow, and ordering](CURRICULUM.md#fapi-asgi-050) | `L` |
| 18 | [FAPI-ASGI-060 — Client disconnects, cancellation, and streaming lifecycle](CURRICULUM.md#fapi-asgi-060) | `L` |
| 19 | [FAPI-ASGI-070 — ASGI servers, workers, proxy headers, root paths, and mounted applications](CURRICULUM.md#fapi-asgi-070) | `L` |
| 20 | [FAPI-PYD-010 — BaseModel fields: required, optional, nullable, defaults, and factories](CURRICULUM.md#fapi-pyd-010) | `M` |
| 21 | [FAPI-PYD-020 — Coercion, strict validation, constraints, and Annotated](CURRICULUM.md#fapi-pyd-020) | `L` |
| 22 | [FAPI-PYD-030 — Model configuration, extra fields, frozen models, copying, and trusted construction](CURRICULUM.md#fapi-pyd-030) | `L` |
| 23 | [FAPI-PYD-040 — Nested and recursive models, forward annotations, unions, and discriminators](CURRICULUM.md#fapi-pyd-040) | `L` |
| 24 | [FAPI-PYD-060 — Aliases, validation aliases, serialization aliases, and alias generators](CURRICULUM.md#fapi-pyd-060) | `M` |
| 25 | [FAPI-PYD-080 — Serialization, serializers, computed fields, and inclusion or exclusion](CURRICULUM.md#fapi-pyd-080) | `L` |
| 26 | [FAPI-PYD-090 — JSON Schema, OpenAPI interaction, and custom types](CURRICULUM.md#fapi-pyd-090) | `XL` |
| 27 | [FAPI-PYD-110 — Object-attribute validation and model boundaries](CURRICULUM.md#fapi-pyd-110) | `L` |
| 28 | [FAPI-APP-010 — Path operations, router matching, route order, and conflicts](CURRICULUM.md#fapi-app-010) | `M` |
| 29 | [FAPI-APP-020 — Path and query parameters, constraints, aliases, and custom parsing](CURRICULUM.md#fapi-app-020) | `L` |
| 30 | [FAPI-APP-040 — Request bodies, multiple body parameters, embedding, and aliases](CURRICULUM.md#fapi-app-040) | `L` |
| 31 | [FAPI-APP-060 — Response models, output validation, serialization, status, headers, and cookies](CURRICULUM.md#fapi-app-060) | `L` |
| 32 | [FAPI-APP-070 — Response classes, redirects, files, and streaming responses](CURRICULUM.md#fapi-app-070) | `L` |
| 33 | [FAPI-APP-080 — APIRouter, nested routers, tags, operation IDs, and route organization](CURRICULUM.md#fapi-app-080) | `L` |
| 34 | [FAPI-APP-090 — HTTP exceptions, validation errors, custom handlers, and error translation](CURRICULUM.md#fapi-app-090) | `L` |
| 35 | [FAPI-DEP-010 — Callable, class-based, and parameterized dependencies](CURRICULUM.md#fapi-dep-010) | `L` |
| 36 | [FAPI-DEP-020 — Subdependencies and dependency-graph resolution](CURRICULUM.md#fapi-dep-020) | `L` |
| 37 | [FAPI-DEP-040 — Yield dependencies, setup/teardown order, scopes, and resource safety](CURRICULUM.md#fapi-dep-040) | `XL` |
| 38 | [FAPI-DEP-050 — Authentication and authorization dependencies](CURRICULUM.md#fapi-dep-050) | `L` |
| 39 | [FAPI-DEP-060 — Router/global dependencies and test overrides](CURRICULUM.md#fapi-dep-060) | `L` |
| 40 | [FAPI-DEP-070 — Request state, composition roots, service location, and dependency boundaries](CURRICULUM.md#fapi-dep-070) | `XL` |
| 41 | [FAPI-MID-010 — Function, class-based, and raw ASGI middleware ordering](CURRICULUM.md#fapi-mid-010) | `L` |
| 42 | [FAPI-MID-020 — Request IDs, structured logging, context variables, and correlation](CURRICULUM.md#fapi-mid-020) | `L` |
| 43 | [FAPI-MID-050 — Rate limiting, observability, and choosing middleware versus dependencies](CURRICULUM.md#fapi-mid-050) | `L` |
| 44 | [FAPI-DB-010 — Relational modelling and PostgreSQL constraints for APIs](CURRICULUM.md#fapi-db-010) | `L` |
| 45 | [FAPI-DB-020 — PostgreSQL drivers, SQLAlchemy engines, URLs, and connection pools](CURRICULUM.md#fapi-db-020) | `L` |
| 46 | [FAPI-DB-030 — SQLAlchemy typed declarative mappings, columns, and constraints](CURRICULUM.md#fapi-db-030) | `L` |
| 47 | [FAPI-DB-040 — Session per request, identity map, and unit-of-work lifecycle](CURRICULUM.md#fapi-db-040) | `XL` |
| 48 | [FAPI-DB-050 — Transactions, flush, commit, rollback, refresh, expiration, and savepoints](CURRICULUM.md#fapi-db-050) | `XL` |
| 49 | [FAPI-DB-080 — Queries, joins, aggregates, filtering, sorting, and pagination](CURRICULUM.md#fapi-db-080) | `L` |
| 50 | [FAPI-DB-110 — Bulk work, generated values, timestamps, soft deletion, and tenant boundaries](CURRICULUM.md#fapi-db-110) | `L` |
| 51 | [FAPI-ASY-010 — def versus async def, event-loop execution, and thread-pool dispatch](CURRICULUM.md#fapi-asy-010) | `L` |
| 52 | [FAPI-ASY-020 — Blocking I/O, CPU-bound work, worker threads, and process offloading](CURRICULUM.md#fapi-asy-020) | `L` |
| 53 | [FAPI-ASY-030 — Timeouts, cancellation, task groups, and structured concurrency](CURRICULUM.md#fapi-asy-030) | `XL` |
| 54 | [FAPI-ASY-040 — BackgroundTasks versus durable jobs and external workers](CURRICULUM.md#fapi-asy-040) | `L` |
| 55 | [FAPI-ASY-060 — Streaming request/response bodies, backpressure, memory, and cleanup](CURRICULUM.md#fapi-asy-060) | `XL` |
| 56 | [FAPI-ASY-070 — Workers, processes, concurrency limits, pool sizing, and shared state](CURRICULUM.md#fapi-asy-070) | `XL` |
| 57 | [FAPI-SEC-010 — Authentication, authorization, and API threat modelling](CURRICULUM.md#fapi-sec-010) | `L` |
| 58 | [FAPI-SEC-060 — RBAC, ABAC, object-level authorization, and tenant isolation](CURRICULUM.md#fapi-sec-060) | `XL` |
| 59 | [FAPI-SEC-090 — Rate limits, brute-force controls, replay, idempotency, audit, and sensitive logging](CURRICULUM.md#fapi-sec-090) | `XL` |
| 60 | [FAPI-RT-010 — REST, RPC, streaming, events, GraphQL, and gRPC boundaries](CURRICULUM.md#fapi-rt-010) | `L` |
| 61 | [FAPI-RT-020 — Streaming HTTP responses, chunking, large files, and disconnects](CURRICULUM.md#fapi-rt-020) | `L` |
| 62 | [FAPI-RT-030 — Server-Sent Events: framing, reconnects, IDs, buffering, and cleanup](CURRICULUM.md#fapi-rt-030) | `L` |
| 63 | [FAPI-RT-040 — WebSocket handshake, connection lifetime, receive/send loops, and disconnects](CURRICULUM.md#fapi-rt-040) | `L` |
| 64 | [FAPI-RT-050 — WebSocket managers, broadcast, heartbeats, auth, backpressure, and scaling](CURRICULUM.md#fapi-rt-050) | `XL` |
| 65 | [FAPI-RT-060 — Webhooks: signing, replay protection, retries, idempotency, and delivery logs](CURRICULUM.md#fapi-rt-060) | `L` |
| 66 | [FAPI-RT-080 — gRPC foundations: Protocol Buffers, code generation, unary calls, status, and metadata](CURRICULUM.md#fapi-rt-080) | `XL` |
| 67 | [FAPI-RT-090 — gRPC streaming, deadlines, cancellation, interceptors, auth, evolution, and gateways](CURRICULUM.md#fapi-rt-090) | `XL` |
| 68 | [FAPI-TST-010 — Testing strategy, observable contracts, and test boundaries](CURRICULUM.md#fapi-tst-010) | `L` |
| 69 | [FAPI-TST-020 — TestClient, HTTPX AsyncClient, ASGI transports, and lifespan-aware tests](CURRICULUM.md#fapi-tst-020) | `L` |
| 70 | [FAPI-TST-070 — WebSocket, SSE, gRPC, webhook, and background-job tests](CURRICULUM.md#fapi-tst-070) | `XL` |
| 71 | [FAPI-OPS-020 — Uvicorn process model, workers, startup, shutdown, and graceful draining](CURRICULUM.md#fapi-ops-020) | `L` |
| 72 | [FAPI-OPS-050 — Structured logs, metrics, traces, and request-span propagation](CURRICULUM.md#fapi-ops-050) | `XL` |

### Project milestones

- [FAPI-PRJ-060 — Real-time operations dashboard](PROJECTS.md#fapi-prj-060)
- [FAPI-PRJ-070 — REST-to-gRPC gateway](PROJECTS.md#fapi-prj-070)

<a id="senior-interview-design-practice"></a>
## Senior interview and design-practice path

For mixed senior questions, code review, changed constraints, and architecture trade-offs.

<!-- path-meta: {"slug":"senior-interview-design-practice","declared_units":96,"rapid_unit_minutes":[4875,7310],"lab_minutes":[720,1080],"recall_minutes":[240,360],"mock_minutes":[240,360],"checkpoint_minutes":[240,360],"rapid_total_minutes":[6315,9470],"full_mastery_hours":[1021,1804],"assumed_prerequisites":[]} -->
| Component | Count or time |
|---|---:|
| Canonical units | 96 |
| Rapid unit study | 81 h 15 min–121 h 50 min |
| Selected practice/labs | 0 checkpoints; 12 h–18 h |
| Recall and comparison | 4 h–6 h |
| Mock interviews | 4 h–6 h |
| Project checkpoints | 4 h–6 h |
| **Rapid path total** | **105 h 15 min–157 h 50 min** |
| Full mastery of included units | 1021–1804 h |

### Assumed prior knowledge or prerequisite bridges

None. The path includes its canonical prerequisites.

### Recommended sequence

| # | Unit | Size |
|---:|---|:---:|
| 1 | [FAPI-FND-010 — Python runtime, uv project, and reproducible environment](CURRICULUM.md#fapi-fnd-010) | `M` |
| 2 | [FAPI-FND-020 — Minimal FastAPI application and first route](CURRICULUM.md#fapi-fnd-020) | `S` |
| 3 | [FAPI-FND-030 — Application entry points, import strings, reload, and server startup](CURRICULUM.md#fapi-fnd-030) | `M` |
| 4 | [FAPI-FND-040 — Interactive documentation, OpenAPI inspection, and simple API clients](CURRICULUM.md#fapi-fnd-040) | `S` |
| 5 | [FAPI-FND-050 — Configuration, environment variables, and application factories](CURRICULUM.md#fapi-fnd-050) | `M` |
| 6 | [FAPI-HTTP-010 — HTTP message anatomy, methods, status codes, and media types](CURRICULUM.md#fapi-http-010) | `L` |
| 7 | [FAPI-HTTP-020 — URLs, path/query semantics, request bodies, encoding, and JSON](CURRICULUM.md#fapi-http-020) | `M` |
| 8 | [FAPI-HTTP-030 — Headers, cookies, content negotiation, and representation metadata](CURRICULUM.md#fapi-http-030) | `M` |
| 9 | [FAPI-HTTP-040 — REST resources, actions, RPC-style endpoints, and practical constraints](CURRICULUM.md#fapi-http-040) | `L` |
| 10 | [FAPI-HTTP-050 — Error contracts, RFC problem details, and API versioning](CURRICULUM.md#fapi-http-050) | `L` |
| 11 | [FAPI-HTTP-060 — Pagination, filtering, sorting, and field selection](CURRICULUM.md#fapi-http-060) | `L` |
| 12 | [FAPI-HTTP-070 — Partial updates, idempotency keys, and conditional writes](CURRICULUM.md#fapi-http-070) | `L` |
| 13 | [FAPI-ASGI-010 — WSGI versus ASGI and the protocol boundary](CURRICULUM.md#fapi-asgi-010) | `L` |
| 14 | [FAPI-ASGI-020 — ASGI scope, receive, send, and the HTTP lifecycle](CURRICULUM.md#fapi-asgi-020) | `L` |
| 15 | [FAPI-ASGI-030 — Starlette beneath FastAPI: requests, responses, routing, and exceptions](CURRICULUM.md#fapi-asgi-030) | `L` |
| 16 | [FAPI-ASGI-040 — Lifespan, application state, and resource ownership](CURRICULUM.md#fapi-asgi-040) | `L` |
| 17 | [FAPI-ASGI-050 — ASGI middleware onion, exception flow, and ordering](CURRICULUM.md#fapi-asgi-050) | `L` |
| 18 | [FAPI-ASGI-060 — Client disconnects, cancellation, and streaming lifecycle](CURRICULUM.md#fapi-asgi-060) | `L` |
| 19 | [FAPI-ASGI-070 — ASGI servers, workers, proxy headers, root paths, and mounted applications](CURRICULUM.md#fapi-asgi-070) | `L` |
| 20 | [FAPI-PYD-010 — BaseModel fields: required, optional, nullable, defaults, and factories](CURRICULUM.md#fapi-pyd-010) | `M` |
| 21 | [FAPI-PYD-020 — Coercion, strict validation, constraints, and Annotated](CURRICULUM.md#fapi-pyd-020) | `L` |
| 22 | [FAPI-PYD-030 — Model configuration, extra fields, frozen models, copying, and trusted construction](CURRICULUM.md#fapi-pyd-030) | `L` |
| 23 | [FAPI-PYD-040 — Nested and recursive models, forward annotations, unions, and discriminators](CURRICULUM.md#fapi-pyd-040) | `L` |
| 24 | [FAPI-PYD-060 — Aliases, validation aliases, serialization aliases, and alias generators](CURRICULUM.md#fapi-pyd-060) | `M` |
| 25 | [FAPI-PYD-070 — Field and model validators: modes, ordering, context, and defaults](CURRICULUM.md#fapi-pyd-070) | `XL` |
| 26 | [FAPI-PYD-080 — Serialization, serializers, computed fields, and inclusion or exclusion](CURRICULUM.md#fapi-pyd-080) | `L` |
| 27 | [FAPI-PYD-090 — JSON Schema, OpenAPI interaction, and custom types](CURRICULUM.md#fapi-pyd-090) | `XL` |
| 28 | [FAPI-PYD-100 — Pydantic Settings: source precedence, env files, secrets, nesting, and custom sources](CURRICULUM.md#fapi-pyd-100) | `L` |
| 29 | [FAPI-PYD-110 — Object-attribute validation and model boundaries](CURRICULUM.md#fapi-pyd-110) | `L` |
| 30 | [FAPI-PYD-120 — Pydantic performance, validator side effects, v1-to-v2 migration, and common mistakes](CURRICULUM.md#fapi-pyd-120) | `XL` |
| 31 | [FAPI-APP-010 — Path operations, router matching, route order, and conflicts](CURRICULUM.md#fapi-app-010) | `M` |
| 32 | [FAPI-APP-020 — Path and query parameters, constraints, aliases, and custom parsing](CURRICULUM.md#fapi-app-020) | `L` |
| 33 | [FAPI-APP-040 — Request bodies, multiple body parameters, embedding, and aliases](CURRICULUM.md#fapi-app-040) | `L` |
| 34 | [FAPI-APP-050 — Forms, multipart data, file uploads, and UploadFile](CURRICULUM.md#fapi-app-050) | `L` |
| 35 | [FAPI-APP-060 — Response models, output validation, serialization, status, headers, and cookies](CURRICULUM.md#fapi-app-060) | `L` |
| 36 | [FAPI-APP-080 — APIRouter, nested routers, tags, operation IDs, and route organization](CURRICULUM.md#fapi-app-080) | `L` |
| 37 | [FAPI-APP-090 — HTTP exceptions, validation errors, custom handlers, and error translation](CURRICULUM.md#fapi-app-090) | `L` |
| 38 | [FAPI-DEP-010 — Callable, class-based, and parameterized dependencies](CURRICULUM.md#fapi-dep-010) | `L` |
| 39 | [FAPI-DEP-020 — Subdependencies and dependency-graph resolution](CURRICULUM.md#fapi-dep-020) | `L` |
| 40 | [FAPI-DEP-040 — Yield dependencies, setup/teardown order, scopes, and resource safety](CURRICULUM.md#fapi-dep-040) | `XL` |
| 41 | [FAPI-DEP-050 — Authentication and authorization dependencies](CURRICULUM.md#fapi-dep-050) | `L` |
| 42 | [FAPI-DEP-060 — Router/global dependencies and test overrides](CURRICULUM.md#fapi-dep-060) | `L` |
| 43 | [FAPI-DEP-070 — Request state, composition roots, service location, and dependency boundaries](CURRICULUM.md#fapi-dep-070) | `XL` |
| 44 | [FAPI-MID-010 — Function, class-based, and raw ASGI middleware ordering](CURRICULUM.md#fapi-mid-010) | `L` |
| 45 | [FAPI-MID-020 — Request IDs, structured logging, context variables, and correlation](CURRICULUM.md#fapi-mid-020) | `L` |
| 46 | [FAPI-MID-030 — CORS, trusted hosts, HTTPS redirects, compression, and sessions](CURRICULUM.md#fapi-mid-030) | `L` |
| 47 | [FAPI-MID-050 — Rate limiting, observability, and choosing middleware versus dependencies](CURRICULUM.md#fapi-mid-050) | `L` |
| 48 | [FAPI-DB-010 — Relational modelling and PostgreSQL constraints for APIs](CURRICULUM.md#fapi-db-010) | `L` |
| 49 | [FAPI-DB-020 — PostgreSQL drivers, SQLAlchemy engines, URLs, and connection pools](CURRICULUM.md#fapi-db-020) | `L` |
| 50 | [FAPI-DB-030 — SQLAlchemy typed declarative mappings, columns, and constraints](CURRICULUM.md#fapi-db-030) | `L` |
| 51 | [FAPI-DB-040 — Session per request, identity map, and unit-of-work lifecycle](CURRICULUM.md#fapi-db-040) | `XL` |
| 52 | [FAPI-DB-050 — Transactions, flush, commit, rollback, refresh, expiration, and savepoints](CURRICULUM.md#fapi-db-050) | `XL` |
| 53 | [FAPI-DB-060 — Relationships, cascades, eager/lazy loading, and object graphs](CURRICULUM.md#fapi-db-060) | `L` |
| 54 | [FAPI-DB-070 — AsyncEngine, AsyncSession, and preventing implicit I/O](CURRICULUM.md#fapi-db-070) | `XL` |
| 55 | [FAPI-DB-080 — Queries, joins, aggregates, filtering, sorting, and pagination](CURRICULUM.md#fapi-db-080) | `L` |
| 56 | [FAPI-DB-090 — N+1 diagnosis, eager loading, query plans, and indexes](CURRICULUM.md#fapi-db-090) | `XL` |
| 57 | [FAPI-DB-100 — Locking, isolation levels, deadlocks, retries, and optimistic concurrency](CURRICULUM.md#fapi-db-100) | `XL` |
| 58 | [FAPI-DB-110 — Bulk work, generated values, timestamps, soft deletion, and tenant boundaries](CURRICULUM.md#fapi-db-110) | `L` |
| 59 | [FAPI-DB-120 — Database test isolation, mapping boundaries, repositories, and direct SQLAlchemy](CURRICULUM.md#fapi-db-120) | `XL` |
| 60 | [FAPI-MIG-010 — Alembic environment, configuration, metadata discovery, and revision graph](CURRICULUM.md#fapi-mig-010) | `L` |
| 61 | [FAPI-MIG-020 — First migration, upgrade, downgrade, current, and history](CURRICULUM.md#fapi-mig-020) | `L` |
| 62 | [FAPI-MIG-030 — Autogenerate review, naming conventions, constraints, indexes, and defaults](CURRICULUM.md#fapi-mig-030) | `XL` |
| 63 | [FAPI-MIG-040 — Data migrations, backfills, enum changes, and offline SQL](CURRICULUM.md#fapi-mig-040) | `XL` |
| 64 | [FAPI-MIG-060 — Async application integration, migration testing, and drift detection](CURRICULUM.md#fapi-mig-060) | `L` |
| 65 | [FAPI-MIG-070 — Expand-and-contract changes, locks, compatibility windows, and rollback decisions](CURRICULUM.md#fapi-mig-070) | `XL` |
| 66 | [FAPI-ARC-010 — From a single file to routers and feature modules](CURRICULUM.md#fapi-arc-010) | `L` |
| 67 | [FAPI-ARC-020 — Layered architecture versus vertical slices](CURRICULUM.md#fapi-arc-020) | `L` |
| 68 | [FAPI-ARC-030 — Service layer, functional core, domain services, DTO mapping, and orchestration](CURRICULUM.md#fapi-arc-030) | `L` |
| 69 | [FAPI-ARC-050 — Composition root, dependency inversion, and error translation](CURRICULUM.md#fapi-arc-050) | `L` |
| 70 | [FAPI-ASY-010 — def versus async def, event-loop execution, and thread-pool dispatch](CURRICULUM.md#fapi-asy-010) | `L` |
| 71 | [FAPI-ASY-030 — Timeouts, cancellation, task groups, and structured concurrency](CURRICULUM.md#fapi-asy-030) | `XL` |
| 72 | [FAPI-ASY-070 — Workers, processes, concurrency limits, pool sizing, and shared state](CURRICULUM.md#fapi-asy-070) | `XL` |
| 73 | [FAPI-ASY-090 — Profiling, load testing, benchmarking, and evidence-led performance diagnosis](CURRICULUM.md#fapi-asy-090) | `XL` |
| 74 | [FAPI-SEC-010 — Authentication, authorization, and API threat modelling](CURRICULUM.md#fapi-sec-010) | `L` |
| 75 | [FAPI-SEC-060 — RBAC, ABAC, object-level authorization, and tenant isolation](CURRICULUM.md#fapi-sec-060) | `XL` |
| 76 | [FAPI-SEC-070 — CORS, trusted hosts, HTTPS, proxy trust, and security headers](CURRICULUM.md#fapi-sec-070) | `L` |
| 77 | [FAPI-SEC-080 — Validation boundaries, mass assignment, SQL injection, SSRF, uploads, and path traversal](CURRICULUM.md#fapi-sec-080) | `XL` |
| 78 | [FAPI-SEC-090 — Rate limits, brute-force controls, replay, idempotency, audit, and sensitive logging](CURRICULUM.md#fapi-sec-090) | `XL` |
| 79 | [FAPI-SEC-100 — Secrets, dependency vulnerabilities, authorization tests, and security review](CURRICULUM.md#fapi-sec-100) | `L` |
| 80 | [FAPI-RT-010 — REST, RPC, streaming, events, GraphQL, and gRPC boundaries](CURRICULUM.md#fapi-rt-010) | `L` |
| 81 | [FAPI-RT-080 — gRPC foundations: Protocol Buffers, code generation, unary calls, status, and metadata](CURRICULUM.md#fapi-rt-080) | `XL` |
| 82 | [FAPI-RT-090 — gRPC streaming, deadlines, cancellation, interceptors, auth, evolution, and gateways](CURRICULUM.md#fapi-rt-090) | `XL` |
| 83 | [FAPI-TST-010 — Testing strategy, observable contracts, and test boundaries](CURRICULUM.md#fapi-tst-010) | `L` |
| 84 | [FAPI-TST-020 — TestClient, HTTPX AsyncClient, ASGI transports, and lifespan-aware tests](CURRICULUM.md#fapi-tst-020) | `L` |
| 85 | [FAPI-TST-030 — Dependency overrides, auth tests, validation errors, and OpenAPI contracts](CURRICULUM.md#fapi-tst-030) | `L` |
| 86 | [FAPI-TST-080 — Timeout, retry, concurrency, load, performance, and security-focused tests](CURRICULUM.md#fapi-tst-080) | `XL` |
| 87 | [FAPI-OPS-020 — Uvicorn process model, workers, startup, shutdown, and graceful draining](CURRICULUM.md#fapi-ops-020) | `L` |
| 88 | [FAPI-OPS-030 — Reverse proxies, forwarded headers, root paths, TLS, and trust](CURRICULUM.md#fapi-ops-030) | `L` |
| 89 | [FAPI-OPS-050 — Structured logs, metrics, traces, and request-span propagation](CURRICULUM.md#fapi-ops-050) | `XL` |
| 90 | [FAPI-OPS-060 — Capacity planning, worker/pool limits, load tests, and performance budgets](CURRICULUM.md#fapi-ops-060) | `XL` |
| 91 | [FAPI-OPS-070 — Production debugging, incident response, deployment strategies, and rollback](CURRICULUM.md#fapi-ops-070) | `XL` |
| 92 | [FAPI-SYN-010 — Request-lifecycle and framework-boundary interview synthesis](CURRICULUM.md#fapi-syn-010) | `L` |
| 93 | [FAPI-SYN-020 — Pydantic, dependency, middleware, and error-handling interview synthesis](CURRICULUM.md#fapi-syn-020) | `L` |
| 94 | [FAPI-SYN-030 — PostgreSQL, SQLAlchemy, Alembic, and architecture interview synthesis](CURRICULUM.md#fapi-syn-030) | `XL` |
| 95 | [FAPI-SYN-040 — Async, security, real-time, performance, and production design synthesis](CURRICULUM.md#fapi-syn-040) | `XL` |
| 96 | [FAPI-SYN-050 — Senior FastAPI code review, debugging, and architecture capstone](CURRICULUM.md#fapi-syn-050) | `XL` |

### Project milestones

- [FAPI-PRJ-020 — PostgreSQL catalog and ordering service](PROJECTS.md#fapi-prj-020)
- [FAPI-PRJ-030 — Authenticated multi-tenant service](PROJECTS.md#fapi-prj-030)
- [FAPI-PRJ-040 — Synthetic review and workflow platform](PROJECTS.md#fapi-prj-040)

<a id="rabbitmq-reliable-async-services"></a>
## RabbitMQ and reliable asynchronous services

A focused broker path for engineers who already have the production FastAPI foundation and need correct asynchronous delivery, PostgreSQL-backed reliability, bounded failure handling, and operable RabbitMQ services.

<!-- path-meta: {"slug":"rabbitmq-reliable-async-services","declared_units":22,"rapid_unit_minutes":[1290,1900],"lab_minutes":[1080,1680],"recall_minutes":[240,360],"mock_minutes":[120,180],"checkpoint_minutes":[480,720],"rapid_total_minutes":[3210,4840],"full_mastery_hours":[282,496],"assumed_prerequisites":[],"assumed_prior_paths":["thirty-day-production-foundation"],"schedule_weeks":[6,9],"hours_per_week":[9,10],"overlap_justifications":{"microservices-distributed-service-engineering":"Intentional focused subset: this path isolates RabbitMQ publisher, consumer, retry, idempotency, outbox, resilience, and observability evidence for learners who do not yet need the complete distributed-service curriculum."}} -->

| Component | Count or time |
|---|---:|
| Canonical units studied or revisited | 22 |
| Rapid unit study | 21 h 30 min–31 h 40 min |
| Selected practice/labs | 18 h–28 h |
| Recall and comparison | 4 h–6 h |
| Mock interviews / incident rounds | 2 h–3 h |
| Project checkpoints | 8 h–12 h |
| **Rapid path total** | **53 h 30 min–80 h 40 min** |
| Full mastery of included units | 282–496 h |

### Entry contract and schedule

**Named prior path:** `30-day production foundation`. This route does not reteach routing, Pydantic, sessions, migrations, authentication, or basic testing. It adds only the FastAPI, async, database, operations, and messaging bridges needed for reliable RabbitMQ work.

Plan approximately **6–9 weeks at 9–10 hours per week**. That provides 54–90 scheduled hours for the calculated 53 h 30 min–80 h 40 min rapid route.

### Assumed prior knowledge or prerequisite bridges

- Complete or diagnose the [30-day production foundation](#thirty-day-production-foundation) first. Its units are treated as named prior-path evidence, not silently repeated here.
- When a prior unit is weak, use its Physical Notebook Core and smallest bridge before continuing; this does not award its learning state.

### Recommended sequence

| Step | Stage | Unit |
|---:|---|---|
| 1 | FastAPI/async bridge | [FAPI-ARC-050 — Composition root, dependency inversion, and error translation](CURRICULUM.md#fapi-arc-050) |
| 2 | FastAPI/async bridge | [FAPI-ARC-060 — Modular monolith boundaries, circular imports, and plugin extension points](CURRICULUM.md#fapi-arc-060) |
| 3 | FastAPI/async bridge | [FAPI-ASY-020 — Blocking I/O, CPU-bound work, worker threads, and process offloading](CURRICULUM.md#fapi-asy-020) |
| 4 | FastAPI/async bridge | [FAPI-ASY-040 — BackgroundTasks versus durable jobs and external workers](CURRICULUM.md#fapi-asy-040) |
| 5 | FastAPI/async bridge | [FAPI-ASY-050 — Message brokers, RabbitMQ, retries, idempotency, and job state](CURRICULUM.md#fapi-asy-050) |
| 6 | FastAPI/async bridge | [FAPI-RT-070 — Polling, long polling, brokers, and event-driven API boundaries](CURRICULUM.md#fapi-rt-070) |
| 7 | FastAPI/async bridge | [FAPI-OPS-010 — Environment configuration, secret injection, and production settings](CURRICULUM.md#fapi-ops-010) |
| 8 | FastAPI/async bridge | [FAPI-OPS-040 — Containers, images, Compose profiles, health, and readiness](CURRICULUM.md#fapi-ops-040) |
| 9 | RabbitMQ reliability | [FAPI-MSV-010 — Microservice decision, decomposition, ownership, and stopping rules](CURRICULUM.md#fapi-msv-010) |
| 10 | RabbitMQ reliability | [FAPI-MSV-020 — Remote-call reality: partial failure, latency, clocks, concurrency, and partitions](CURRICULUM.md#fapi-msv-020) |
| 11 | RabbitMQ reliability | [FAPI-MSV-030 — Communication selection across HTTP, gRPC, queues, pub/sub, logs, and browser streams](CURRICULUM.md#fapi-msv-030) |
| 12 | RabbitMQ reliability | [FAPI-MSV-040 — Service and message contracts, envelopes, versioning, and ownership](CURRICULUM.md#fapi-msv-040) |
| 13 | RabbitMQ reliability | [FAPI-MSV-050 — RabbitMQ fundamentals: AMQP entities, topology, routing, and local operations](CURRICULUM.md#fapi-msv-050) |
| 14 | RabbitMQ reliability | [FAPI-MSV-060 — RabbitMQ connections, channels, recovery, permissions, and topology compatibility](CURRICULUM.md#fapi-msv-060) |
| 15 | RabbitMQ reliability | [FAPI-MSV-070 — RabbitMQ publisher correctness: confirms, mandatory returns, uncertainty, and backpressure](CURRICULUM.md#fapi-msv-070) |
| 16 | RabbitMQ reliability | [FAPI-MSV-080 — RabbitMQ consumer correctness: acknowledgements, prefetch, crash windows, and draining](CURRICULUM.md#fapi-msv-080) |
| 17 | RabbitMQ reliability | [FAPI-MSV-090 — RabbitMQ retries, dead lettering, delay, redrive, and poison-message operations](CURRICULUM.md#fapi-msv-090) |
| 18 | RabbitMQ reliability | [FAPI-MSV-100 — RabbitMQ queue types, ordering, retention, and broker selection](CURRICULUM.md#fapi-msv-100) |
| 19 | RabbitMQ reliability | [FAPI-MSV-110 — Delivery semantics, duplicate handling, and idempotent operations](CURRICULUM.md#fapi-msv-110) |
| 20 | RabbitMQ reliability | [FAPI-MSV-120 — Transactional outbox, inbox, relay, CDC boundaries, and cleanup](CURRICULUM.md#fapi-msv-120) |
| 21 | Cross-cutting reliability | [FAPI-MSV-180 — Resilience budgets: timeouts, retry amplification, breakers, bulkheads, and load shedding](CURRICULUM.md#fapi-msv-180) |
| 22 | Cross-cutting reliability | [FAPI-MSV-210 — Distributed observability: context propagation, logs, metrics, traces, SLIs, SLOs, and alerts](CURRICULUM.md#fapi-msv-210) |

### Project milestones

- [FAPI-PRJ-090 — Reliable RabbitMQ workflow service](PROJECTS.md#fapi-prj-090)

### Required comparison, failure, and interview work

- Reconstruct one architecture or message-flow visual closed book.
- Diagnose at least one partial-failure or incident scenario without receiving the intended pattern first.
- Compare at least two plausible communication or reliability mechanisms and reject one with explicit reasons.
- Complete one mock design interview in which requirements change after the initial design.

### Intentional overlap

- With `microservices-distributed-service-engineering`: Intentional focused subset: this path isolates RabbitMQ publisher, consumer, retry, idempotency, outbox, resilience, and observability evidence for learners who do not yet need the complete distributed-service curriculum.

### Intentionally deferred

gRPC operations, Kubernetes traffic, cross-service database composition, broad governance, and the full microservice capstone are deferred to the complete microservices route.


<a id="microservices-distributed-service-engineering"></a>
## Microservices and distributed service engineering

The complete appended MSV sequence for an engineer who already owns a production FastAPI foundation and now wants end-to-end service decomposition, communication, consistency, reliability, security, testing, evolution, and operations.

<!-- path-meta: {"slug":"microservices-distributed-service-engineering","declared_units":47,"rapid_unit_minutes":[2865,4190],"lab_minutes":[2100,3300],"recall_minutes":[480,720],"mock_minutes":[240,360],"checkpoint_minutes":[960,1440],"rapid_total_minutes":[6645,10010],"full_mastery_hours":[633,1112],"assumed_prerequisites":[],"assumed_prior_paths":["thirty-day-production-foundation"],"schedule_weeks":[12,18],"hours_per_week":[10,10],"overlap_justifications":{"rabbitmq-reliable-async-services":"Intentional superset: RabbitMQ is one complete phase of this broader service-engineering path, so learners who finished the focused path may mark those overlapping units as diagnostic revisits rather than repeat all labs.","senior-microservices-design-operations":"Intentional foundation: the senior route revisits a selected subset after this path and demands deeper design, incident, governance, and migration evidence."}} -->

| Component | Count or time |
|---|---:|
| Canonical units studied or revisited | 47 |
| Rapid unit study | 47 h 45 min–69 h 50 min |
| Selected practice/labs | 35 h–55 h |
| Recall and comparison | 8 h–12 h |
| Mock interviews / incident rounds | 4 h–6 h |
| Project checkpoints | 16 h–24 h |
| **Rapid path total** | **110 h 45 min–166 h 50 min** |
| Full mastery of included units | 633–1112 h |

### Entry contract and schedule

**Named prior path:** `30-day production foundation`. The listed bridge units close the additional Pydantic, architecture, async, transport, test, operations, and synthesis prerequisites that path intentionally omits; then all 27 MSV units are completed in canonical order.

Plan approximately **12–18 weeks at 10 hours per week**. That provides 120–180 scheduled hours for the calculated 110 h 45 min–166 h 50 min rapid route.

### Assumed prior knowledge or prerequisite bridges

- Complete or diagnose the [30-day production foundation](#thirty-day-production-foundation) first. Its units are treated as named prior-path evidence, not silently repeated here.
- When a prior unit is weak, use its Physical Notebook Core and smallest bridge before continuing; this does not award its learning state.

### Recommended sequence

| Step | Stage | Unit |
|---:|---|---|
| 1 | Production FastAPI bridge | [FAPI-PYD-070 — Field and model validators: modes, ordering, context, and defaults](CURRICULUM.md#fapi-pyd-070) |
| 2 | Production FastAPI bridge | [FAPI-PYD-120 — Pydantic performance, validator side effects, v1-to-v2 migration, and common mistakes](CURRICULUM.md#fapi-pyd-120) |
| 3 | Production FastAPI bridge | [FAPI-APP-070 — Response classes, redirects, files, and streaming responses](CURRICULUM.md#fapi-app-070) |
| 4 | Production FastAPI bridge | [FAPI-ARC-050 — Composition root, dependency inversion, and error translation](CURRICULUM.md#fapi-arc-050) |
| 5 | Production FastAPI bridge | [FAPI-ARC-060 — Modular monolith boundaries, circular imports, and plugin extension points](CURRICULUM.md#fapi-arc-060) |
| 6 | Production FastAPI bridge | [FAPI-ASY-020 — Blocking I/O, CPU-bound work, worker threads, and process offloading](CURRICULUM.md#fapi-asy-020) |
| 7 | Production FastAPI bridge | [FAPI-ASY-040 — BackgroundTasks versus durable jobs and external workers](CURRICULUM.md#fapi-asy-040) |
| 8 | Production FastAPI bridge | [FAPI-ASY-050 — Message brokers, RabbitMQ, retries, idempotency, and job state](CURRICULUM.md#fapi-asy-050) |
| 9 | Production FastAPI bridge | [FAPI-ASY-060 — Streaming request/response bodies, backpressure, memory, and cleanup](CURRICULUM.md#fapi-asy-060) |
| 10 | Production FastAPI bridge | [FAPI-RT-020 — Streaming HTTP responses, chunking, large files, and disconnects](CURRICULUM.md#fapi-rt-020) |
| 11 | Production FastAPI bridge | [FAPI-RT-030 — Server-Sent Events: framing, reconnects, IDs, buffering, and cleanup](CURRICULUM.md#fapi-rt-030) |
| 12 | Production FastAPI bridge | [FAPI-RT-060 — Webhooks: signing, replay protection, retries, idempotency, and delivery logs](CURRICULUM.md#fapi-rt-060) |
| 13 | Production FastAPI bridge | [FAPI-RT-070 — Polling, long polling, brokers, and event-driven API boundaries](CURRICULUM.md#fapi-rt-070) |
| 14 | Production FastAPI bridge | [FAPI-TST-070 — WebSocket, SSE, gRPC, webhook, and background-job tests](CURRICULUM.md#fapi-tst-070) |
| 15 | Production FastAPI bridge | [FAPI-OPS-010 — Environment configuration, secret injection, and production settings](CURRICULUM.md#fapi-ops-010) |
| 16 | Production FastAPI bridge | [FAPI-OPS-040 — Containers, images, Compose profiles, health, and readiness](CURRICULUM.md#fapi-ops-040) |
| 17 | Production FastAPI bridge | [FAPI-SYN-010 — Request-lifecycle and framework-boundary interview synthesis](CURRICULUM.md#fapi-syn-010) |
| 18 | Production FastAPI bridge | [FAPI-SYN-020 — Pydantic, dependency, middleware, and error-handling interview synthesis](CURRICULUM.md#fapi-syn-020) |
| 19 | Production FastAPI bridge | [FAPI-SYN-030 — PostgreSQL, SQLAlchemy, Alembic, and architecture interview synthesis](CURRICULUM.md#fapi-syn-030) |
| 20 | Production FastAPI bridge | [FAPI-SYN-050 — Senior FastAPI code review, debugging, and architecture capstone](CURRICULUM.md#fapi-syn-050) |
| 21 | Boundaries and messaging | [FAPI-MSV-010 — Microservice decision, decomposition, ownership, and stopping rules](CURRICULUM.md#fapi-msv-010) |
| 22 | Boundaries and messaging | [FAPI-MSV-020 — Remote-call reality: partial failure, latency, clocks, concurrency, and partitions](CURRICULUM.md#fapi-msv-020) |
| 23 | Boundaries and messaging | [FAPI-MSV-030 — Communication selection across HTTP, gRPC, queues, pub/sub, logs, and browser streams](CURRICULUM.md#fapi-msv-030) |
| 24 | Boundaries and messaging | [FAPI-MSV-040 — Service and message contracts, envelopes, versioning, and ownership](CURRICULUM.md#fapi-msv-040) |
| 25 | Boundaries and messaging | [FAPI-MSV-050 — RabbitMQ fundamentals: AMQP entities, topology, routing, and local operations](CURRICULUM.md#fapi-msv-050) |
| 26 | Boundaries and messaging | [FAPI-MSV-060 — RabbitMQ connections, channels, recovery, permissions, and topology compatibility](CURRICULUM.md#fapi-msv-060) |
| 27 | Boundaries and messaging | [FAPI-MSV-070 — RabbitMQ publisher correctness: confirms, mandatory returns, uncertainty, and backpressure](CURRICULUM.md#fapi-msv-070) |
| 28 | Boundaries and messaging | [FAPI-MSV-080 — RabbitMQ consumer correctness: acknowledgements, prefetch, crash windows, and draining](CURRICULUM.md#fapi-msv-080) |
| 29 | Boundaries and messaging | [FAPI-MSV-090 — RabbitMQ retries, dead lettering, delay, redrive, and poison-message operations](CURRICULUM.md#fapi-msv-090) |
| 30 | Boundaries and messaging | [FAPI-MSV-100 — RabbitMQ queue types, ordering, retention, and broker selection](CURRICULUM.md#fapi-msv-100) |
| 31 | Boundaries and messaging | [FAPI-MSV-110 — Delivery semantics, duplicate handling, and idempotent operations](CURRICULUM.md#fapi-msv-110) |
| 32 | Boundaries and messaging | [FAPI-MSV-120 — Transactional outbox, inbox, relay, CDC boundaries, and cleanup](CURRICULUM.md#fapi-msv-120) |
| 33 | Workflows and gRPC | [FAPI-MSV-130 — Distributed workflows: sagas, compensation, orchestration, and intervention](CURRICULUM.md#fapi-msv-130) |
| 34 | Workflows and gRPC | [FAPI-MSV-140 — Eventual consistency, read models, CQRS, and event-sourcing boundaries](CURRICULUM.md#fapi-msv-140) |
| 35 | Workflows and gRPC | [FAPI-MSV-150 — Production gRPC contracts: Protobuf evolution, status details, and metadata](CURRICULUM.md#fapi-msv-150) |
| 36 | Workflows and gRPC | [FAPI-MSV-160 — Production gRPC execution: deadlines, cancellation, retries, streaming, and flow control](CURRICULUM.md#fapi-msv-160) |
| 37 | Workflows and gRPC | [FAPI-MSV-170 — gRPC operations: channels, discovery, balancing, health, TLS, tracing, and gateways](CURRICULUM.md#fapi-msv-170) |
| 38 | Reliability, operations, and governance | [FAPI-MSV-180 — Resilience budgets: timeouts, retry amplification, breakers, bulkheads, and load shedding](CURRICULUM.md#fapi-msv-180) |
| 39 | Reliability, operations, and governance | [FAPI-MSV-190 — Discovery, gateways, proxies, Kubernetes traffic, and service-mesh boundaries](CURRICULUM.md#fapi-msv-190) |
| 40 | Reliability, operations, and governance | [FAPI-MSV-200 — Service data ownership, cross-service queries, reporting, and migration from shared storage](CURRICULUM.md#fapi-msv-200) |
| 41 | Reliability, operations, and governance | [FAPI-MSV-210 — Distributed observability: context propagation, logs, metrics, traces, SLIs, SLOs, and alerts](CURRICULUM.md#fapi-msv-210) |
| 42 | Reliability, operations, and governance | [FAPI-MSV-220 — Microservice security: workload identity, mTLS, delegated authorization, broker permissions, and tenant context](CURRICULUM.md#fapi-msv-220) |
| 43 | Reliability, operations, and governance | [FAPI-MSV-230 — Distributed testing: contracts, real dependencies, duplicate delivery, fault injection, and eventual consistency](CURRICULUM.md#fapi-msv-230) |
| 44 | Reliability, operations, and governance | [FAPI-MSV-240 — Compatible deployment and evolution: rollout, draining, autoscaling, backlog, and schema windows](CURRICULUM.md#fapi-msv-240) |
| 45 | Reliability, operations, and governance | [FAPI-MSV-250 — Reliability operations: runbooks, incidents, postmortems, disaster recovery, and dependency upgrades](CURRICULUM.md#fapi-msv-250) |
| 46 | Reliability, operations, and governance | [FAPI-MSV-260 — Governance and ownership: catalogs, ADRs, golden paths, shared libraries, team topology, and cost](CURRICULUM.md#fapi-msv-260) |
| 47 | Reliability, operations, and governance | [FAPI-MSV-270 — Evolutionary extraction and senior microservice design synthesis](CURRICULUM.md#fapi-msv-270) |

### Project milestones

- [FAPI-PRJ-090 — Reliable RabbitMQ workflow service](PROJECTS.md#fapi-prj-090)
- [FAPI-PRJ-100 — Microservices production capstone](PROJECTS.md#fapi-prj-100)

### Required comparison, failure, and interview work

- Reconstruct one architecture or message-flow visual closed book.
- Diagnose at least one partial-failure or incident scenario without receiving the intended pattern first.
- Compare at least two plausible communication or reliability mechanisms and reject one with explicit reasons.
- Complete one mock design interview in which requirements change after the initial design.

### Intentional overlap

- With `rabbitmq-reliable-async-services`: Intentional superset: RabbitMQ is one complete phase of this broader service-engineering path, so learners who finished the focused path may mark those overlapping units as diagnostic revisits rather than repeat all labs.
- With `senior-microservices-design-operations`: Intentional foundation: the senior route revisits a selected subset after this path and demands deeper design, incident, governance, and migration evidence.

### Intentionally deferred

Full Kubernetes administration, production Kafka operations, service-mesh administration, and cloud-provider certification material remain separate specialist curricula.


<a id="senior-microservices-design-operations"></a>
## Senior microservices design and operations

A design, evolution, reliability, incident, and organizational-ownership route for engineers who have already completed the full microservices path. It deliberately revisits only the units that carry SDE-3 system-boundary and operational judgment.

<!-- path-meta: {"slug":"senior-microservices-design-operations","declared_units":20,"rapid_unit_minutes":[1350,1940],"lab_minutes":[840,1320],"recall_minutes":[360,540],"mock_minutes":[360,480],"checkpoint_minutes":[480,720],"rapid_total_minutes":[3390,5000],"full_mastery_hours":[306,536],"assumed_prerequisites":[],"assumed_prior_paths":["microservices-distributed-service-engineering"],"schedule_weeks":[7,10],"hours_per_week":[9,9],"overlap_justifications":{"microservices-distributed-service-engineering":"Intentional advanced revisit: every selected unit was previously studied, but this route raises evidence to cross-team contract ownership, migration strategy, reliability budgets, incident leadership, governance, and cost decisions."}} -->

| Component | Count or time |
|---|---:|
| Canonical units studied or revisited | 20 |
| Rapid unit study | 22 h 30 min–32 h 20 min |
| Selected practice/labs | 14 h–22 h |
| Recall and comparison | 6 h–9 h |
| Mock interviews / incident rounds | 6 h–8 h |
| Project checkpoints | 8 h–12 h |
| **Rapid path total** | **56 h 30 min–83 h 20 min** |
| Full mastery of included units | 306–536 h |

### Entry contract and schedule

**Named prior path:** `Microservices and distributed service engineering`. This is not a from-scratch route. Unit links below are selected retrieval and transfer rounds; introductory RabbitMQ topology and elementary FastAPI mechanics are assumed and are not restarted.

Plan approximately **7–10 weeks at 9 hours per week**. That provides 63–90 scheduled hours for the calculated 56 h 30 min–83 h 20 min rapid route.

### Assumed prior knowledge or prerequisite bridges

- Complete or diagnose the [Microservices and distributed service engineering](#microservices-distributed-service-engineering) first. Its units are treated as named prior-path evidence, not silently repeated here.
- When a prior unit is weak, use its Physical Notebook Core and smallest bridge before continuing; this does not award its learning state.

### Recommended sequence

| Step | Stage | Unit |
|---:|---|---|
| 1 | Boundary and contract judgment | [FAPI-MSV-010 — Microservice decision, decomposition, ownership, and stopping rules](CURRICULUM.md#fapi-msv-010) |
| 2 | Boundary and contract judgment | [FAPI-MSV-020 — Remote-call reality: partial failure, latency, clocks, concurrency, and partitions](CURRICULUM.md#fapi-msv-020) |
| 3 | Boundary and contract judgment | [FAPI-MSV-030 — Communication selection across HTTP, gRPC, queues, pub/sub, logs, and browser streams](CURRICULUM.md#fapi-msv-030) |
| 4 | Boundary and contract judgment | [FAPI-MSV-040 — Service and message contracts, envelopes, versioning, and ownership](CURRICULUM.md#fapi-msv-040) |
| 5 | Boundary and contract judgment | [FAPI-MSV-110 — Delivery semantics, duplicate handling, and idempotent operations](CURRICULUM.md#fapi-msv-110) |
| 6 | Boundary and contract judgment | [FAPI-MSV-120 — Transactional outbox, inbox, relay, CDC boundaries, and cleanup](CURRICULUM.md#fapi-msv-120) |
| 7 | Boundary and contract judgment | [FAPI-MSV-130 — Distributed workflows: sagas, compensation, orchestration, and intervention](CURRICULUM.md#fapi-msv-130) |
| 8 | Boundary and contract judgment | [FAPI-MSV-140 — Eventual consistency, read models, CQRS, and event-sourcing boundaries](CURRICULUM.md#fapi-msv-140) |
| 9 | Runtime and resilience | [FAPI-MSV-150 — Production gRPC contracts: Protobuf evolution, status details, and metadata](CURRICULUM.md#fapi-msv-150) |
| 10 | Runtime and resilience | [FAPI-MSV-160 — Production gRPC execution: deadlines, cancellation, retries, streaming, and flow control](CURRICULUM.md#fapi-msv-160) |
| 11 | Runtime and resilience | [FAPI-MSV-170 — gRPC operations: channels, discovery, balancing, health, TLS, tracing, and gateways](CURRICULUM.md#fapi-msv-170) |
| 12 | Runtime and resilience | [FAPI-MSV-180 — Resilience budgets: timeouts, retry amplification, breakers, bulkheads, and load shedding](CURRICULUM.md#fapi-msv-180) |
| 13 | Ownership, operations, and evolution | [FAPI-MSV-190 — Discovery, gateways, proxies, Kubernetes traffic, and service-mesh boundaries](CURRICULUM.md#fapi-msv-190) |
| 14 | Ownership, operations, and evolution | [FAPI-MSV-200 — Service data ownership, cross-service queries, reporting, and migration from shared storage](CURRICULUM.md#fapi-msv-200) |
| 15 | Ownership, operations, and evolution | [FAPI-MSV-210 — Distributed observability: context propagation, logs, metrics, traces, SLIs, SLOs, and alerts](CURRICULUM.md#fapi-msv-210) |
| 16 | Ownership, operations, and evolution | [FAPI-MSV-220 — Microservice security: workload identity, mTLS, delegated authorization, broker permissions, and tenant context](CURRICULUM.md#fapi-msv-220) |
| 17 | Ownership, operations, and evolution | [FAPI-MSV-240 — Compatible deployment and evolution: rollout, draining, autoscaling, backlog, and schema windows](CURRICULUM.md#fapi-msv-240) |
| 18 | Ownership, operations, and evolution | [FAPI-MSV-250 — Reliability operations: runbooks, incidents, postmortems, disaster recovery, and dependency upgrades](CURRICULUM.md#fapi-msv-250) |
| 19 | Ownership, operations, and evolution | [FAPI-MSV-260 — Governance and ownership: catalogs, ADRs, golden paths, shared libraries, team topology, and cost](CURRICULUM.md#fapi-msv-260) |
| 20 | Ownership, operations, and evolution | [FAPI-MSV-270 — Evolutionary extraction and senior microservice design synthesis](CURRICULUM.md#fapi-msv-270) |

### Project milestones

- [FAPI-PRJ-100 — Microservices production capstone](PROJECTS.md#fapi-prj-100)

### Required comparison, failure, and interview work

- Reconstruct one architecture or message-flow visual closed book.
- Diagnose at least one partial-failure or incident scenario without receiving the intended pattern first.
- Compare at least two plausible communication or reliability mechanisms and reject one with explicit reasons.
- Complete one mock design interview in which requirements change after the initial design.

### Intentional overlap

- With `microservices-distributed-service-engineering`: Intentional advanced revisit: every selected unit was previously studied, but this route raises evidence to cross-team contract ownership, migration strategy, reliability budgets, incident leadership, governance, and cost decisions.

### Intentionally deferred

Elementary route construction, introductory Pydantic, basic CRUD, introductory AMQP topology, and first-pass gRPC syntax are assumed prior evidence rather than repeated study.
