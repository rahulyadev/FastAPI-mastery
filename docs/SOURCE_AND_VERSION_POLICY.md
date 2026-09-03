# Source and version policy

## Authority order

1. FastAPI, Starlette, Pydantic, SQLAlchemy, Alembic, Psycopg, Uvicorn, AnyIO, HTTPX, gRPC, and PostgreSQL official documentation.
2. HTTP, ASGI, OpenAPI, OAuth/OIDC, SSE, WebSocket, gRPC, and relevant RFC/specification text.
3. Official project release notes and source for implementation-sensitive behavior.
4. Strong secondary explanations only when primary material is insufficient.

Cite only sources actually read. Place citations near subtle claims involving versions, protocol semantics, security, concurrency, transactions, migrations, or performance. Do not mechanically cite every ordinary teaching sentence.

## Canonical runtime

- Python 3.14.7 is the canonical runtime at packaging.
- Examples remain Python 3.11 compatible where practical.
- Mark the first supported version for newer syntax or behavior.
- FastAPI owns its compatible Starlette dependency; do not pin Starlette independently unless a reviewed constraint requires it.
- Pydantic v2, SQLAlchemy 2.x, Alembic current APIs, and FastAPI lifespan are canonical.

## Boundary labels

Classify important behavior as Python, HTTP/specification, ASGI, server, Starlette, FastAPI, Pydantic, SQLAlchemy, Alembic, PostgreSQL, proxy, third-party, or application architecture.

## Experiments and benchmarks

Record exact environment, command, actual output, interpretation, and limitations. Never claim an experiment, migration, container, query, or benchmark ran when it did not. Separate asymptotic or protocol reasoning from measured performance.

## Release audit

When changing a pinned baseline, verify authoritative compatibility, regenerate the lock, run the full test and validation suite, audit version-sensitive units, and preserve older correct behavior through explicit version notes rather than rewriting history.

## Distributed-service sources

Prefer official RabbitMQ guides and AMQP references, official aio-pika/aiormq documentation for client behavior, gRPC and Protocol Buffers documentation, PostgreSQL, Kubernetes, OpenTelemetry specifications, W3C Trace Context, IETF RFCs, and CNCF specifications such as CloudEvents.

Label every claim as standardized protocol behavior, RabbitMQ behavior, client-library behavior, Kubernetes behavior, framework behavior, or professional design judgment. Publisher confirms and consumer acknowledgements are related but distinct mechanisms. At-least-once delivery is expected; any “exactly once” claim must name the bounded layer, storage, deduplication mechanism, and failure assumptions.
