# Toolchain and local infrastructure

The versions below were verified against authoritative project/PyPI pages on 2026-08-29. FastAPI owns its compatible Starlette dependency; Starlette is documented but not separately pinned in `pyproject.toml`.

| Package | Verified stable version | Repository role |
|---|---:|---|
| `python` | `3.14.7` | Canonical runtime; examples retain Python 3.11 alternatives where useful. |
| `fastapi` | `0.141.1` | Core framework. |
| `starlette` | `1.6.0` | Verified current release; resolved through FastAPI rather than pinned as a direct dependency. |
| `pydantic` | `2.13.4` | Validation and serialization. |
| `pydantic-settings` | `2.15.0` | Typed settings. |
| `sqlalchemy` | `2.0.52` | Stable SQLAlchemy 2.x; 2.1 prereleases excluded. |
| `alembic` | `1.19.1` | Schema migrations. |
| `psycopg` | `3.3.4` | PostgreSQL driver and pool. |
| `uvicorn` | `0.52.4` | ASGI server. |
| `httpx` | `0.28.1` | Stable HTTP client and ASGI testing; 1.0 development releases excluded. |
| `anyio` | `4.14.2` | Structured async runtime used by Starlette/testing. |
| `pytest` | `9.1.1` | Test runner. |
| `pytest-cov` | `7.1.0` | Coverage integration. |
| `pytest-asyncio` | `1.3.0` | Optional asyncio test compatibility; AnyIO plugin remains primary for many examples. |
| `hypothesis` | `6.165.10` | Property-based testing. |
| `ruff` | `0.16.4` | Formatter and linter. |
| `mypy` | `2.3.1` | Static analysis. |
| `grpcio` | `1.83.1` | gRPC runtime. |
| `grpcio-tools` | `1.83.0` | Protobuf code generation; latest verified tools release at packaging. |
| `protobuf` | `7.36.0` | Protocol Buffers runtime. |
| `redis` | `8.1.0` | Optional cache and pub/sub client. |
| `opentelemetry-sdk` | `1.44.0` | Optional observability SDK. |

## Setup

```bash
uv sync --group dev
```

Optional integrations:

```bash
uv sync --group dev --group postgres
uv sync --group dev --group grpc
uv sync --group dev --group redis
uv sync --group dev --group observability
```

Run structural validation:

```bash
python scripts/validate_repo.py
```

Run extended validator fixtures:

```bash
uv run --group dev python scripts/validate_repo.py --self-test
```

## Compose profiles

Copy `.env.example` to a local `.env` and change values only for local disposable use.

```bash
docker compose --profile postgres up -d
docker compose --profile redis up -d
docker compose --profile mail-testing up -d
docker compose --profile observability up -d
```

Inspect and stop:

```bash
docker compose ps
docker compose logs -f postgres
docker compose stop postgres redis mailpit otel-lgtm
```

Do not use a broad volume-removal command. Follow the service-specific reset procedure, verify the active Docker context and exact Compose labels, and remove only the named disposable learning volume. The RabbitMQ procedure below is the model for this repository.

PostgreSQL is the default relational practice service. Redis, mail testing, and observability are optional and should not run for basic units.

## Lock checks

The canonical check is:

```bash
uv lock --check --python 3.14.7
```

If CPython 3.14.7 is unavailable and uv would download it, record that exact check as **Skipped**. A substituted interpreter check must be named explicitly rather than presented as the canonical check.

## RabbitMQ local profile

RabbitMQ runs only when its explicit profile is selected. Ports bind to loopback, and the credentials in `.env.example` are synthetic local-learning values.

```bash
cp .env.example .env
uv sync --group dev --group rabbitmq
docker compose --profile rabbitmq up -d rabbitmq
docker compose ps rabbitmq
docker compose logs --tail=100 rabbitmq
docker compose exec -T rabbitmq rabbitmq-diagnostics -q ping
```

Resolve the actual loopback-bound management address from Compose instead of assuming that `.env` variables were exported into the host shell:

```bash
docker compose port rabbitmq 15672
```

Open the reported `127.0.0.1:<port>` address and use the synthetic local credentials from `.env`.

### Inspect the running broker

The commands below use RabbitMQ 4.3-supported `rabbitmqctl` fields. Commands needing the vhost or learning queue resolve them **inside the container** from the service environment.

```bash
docker compose exec -T rabbitmq rabbitmqctl \
  list_connections name user peer_host state channels

docker compose exec -T rabbitmq rabbitmqctl \
  list_channels number user vhost confirm consumer_count \
  messages_unacknowledged messages_unconfirmed prefetch_count

docker compose exec -T rabbitmq sh -lc '  rabbitmqctl list_exchanges -p "$RABBITMQ_DEFAULT_VHOST"   name type durable auto_delete internal'

docker compose exec -T rabbitmq sh -lc '  rabbitmqctl list_queues -p "$RABBITMQ_DEFAULT_VHOST"   name type durable messages_ready messages_unacknowledged   consumers consumer_utilisation'

docker compose exec -T rabbitmq sh -lc '  rabbitmqctl list_bindings -p "$RABBITMQ_DEFAULT_VHOST"   source_name source_kind destination_name destination_kind routing_key'

docker compose exec -T rabbitmq sh -lc '  rabbitmqctl list_consumers -p "$RABBITMQ_DEFAULT_VHOST"'
```

`list_consumers` has a fixed supported output format, so no unsupported column arguments are passed. `consumer_utilisation` is the documented queue field used here.

### Publish and consume a sample message

The bootstrap intentionally contains no generated unit files, so there are no root-level `examples/rabbitmq/...` scripts. Initialize the owning unit first:

```text
Initialize FAPI-MSV-050.
```

That command creates this exact unit directory:

```text
units/microservices-distributed-services/FAPI-MSV-050-rabbitmq-fundamentals-amqp-entities-topology-routing-and-local-operations/
```

Use the publisher and consumer commands written into that generated unit's `practice/README.md`. To display the authoritative unit-local commands after initialization:

```bash
unit_dir=units/microservices-distributed-services/FAPI-MSV-050-rabbitmq-fundamentals-amqp-entities-topology-routing-and-local-operations
sed -n '/^## Commands$/,/^## Troubleshooting$/p' "$unit_dir/practice/README.md"
```

Run those commands from the owning Worktree. The generated unit pack—not the bootstrap root—owns the concrete sample filenames.

### Safely inspect, purge, or delete only the named learning queue

First print and verify the values resolved inside the RabbitMQ container:

```bash
docker compose exec -T rabbitmq sh -lc '  set -eu
  vhost="$RABBITMQ_DEFAULT_VHOST"
  queue="$RABBITMQ_LEARNING_QUEUE"
  printf "vhost=%s queue=%s\n" "$vhost" "$queue"
  rabbitmqctl list_queues -p "$vhost" name | grep -Fqx -- "$queue"'
```

Purge only that verified local queue:

```bash
docker compose exec -T rabbitmq sh -lc '  set -eu
  vhost="$RABBITMQ_DEFAULT_VHOST"
  queue="$RABBITMQ_LEARNING_QUEUE"
  rabbitmqctl list_queues -p "$vhost" name | grep -Fqx -- "$queue"
  rabbitmqctl purge_queue -p "$vhost" "$queue"'
```

Delete only that verified queue, and only when unused and empty:

```bash
docker compose exec -T rabbitmq sh -lc '  set -eu
  vhost="$RABBITMQ_DEFAULT_VHOST"
  queue="$RABBITMQ_LEARNING_QUEUE"
  rabbitmqctl list_queues -p "$vhost" name | grep -Fqx -- "$queue"
  rabbitmqctl delete_queue -p "$vhost" "$queue" --if-empty --if-unused'
```

### Stop or reset only RabbitMQ

Stopping RabbitMQ must not stop PostgreSQL, Redis, Mailpit, or observability services:

```bash
docker compose --profile rabbitmq stop rabbitmq
docker compose --profile rabbitmq rm -f rabbitmq
```

A deliberate local volume reset requires inspecting the active Docker context and exact Compose-labelled volume first:

```bash
docker context show
docker volume inspect fastapi-mastery_fastapi_rabbitmq_data
docker volume inspect --format   '{{ index .Labels "com.docker.compose.project" }} {{ index .Labels "com.docker.compose.volume" }}'   fastapi-mastery_fastapi_rabbitmq_data
```

Proceed only when the label output is exactly:

```text
fastapi-mastery fastapi_rabbitmq_data
```

Then remove only that disposable learning volume:

```bash
docker volume rm fastapi-mastery_fastapi_rabbitmq_data
```

Never use a broad Compose volume deletion or system-wide Docker cleanup for a RabbitMQ learning reset.

## Optional profiles

```text
postgres
rabbitmq
redis
mail-testing
observability
```

Start only what the current unit or project requires.
