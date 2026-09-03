#!/usr/bin/env python3
"""Validate the FastAPI Mastery bootstrap using only the Python standard library."""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
import zipfile
from collections import Counter, defaultdict, deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

UNIT_ID_RE = re.compile(r"FAPI-[A-Z]{2,4}-\d{3}")
PROJECT_ID_RE = re.compile(r"FAPI-PRJ-\d{3}")
SDP_ID_RE = re.compile(r"SDP-[A-Z]{3}-\d{3}")
PYTHON_ID_RE = re.compile(r"PY-[A-Z]{3}-\d{3}")
BASELINE_UNIT_COUNT = 129
EXPECTED_UNIT_COUNT = 156
EXPECTED_PROJECT_COUNT = 10
EXPECTED_PATH_COUNT = 17
EXPECTED_BASELINE_ZIP_SHA256 = "1adc52162b1abb2d0e4de375b82ac3ce4c8eab2599bd7f2f24197f14f4441085"
EXPECTED_BASELINE_UNIT_ROWS_SHA256 = "5abab783bd6eee0527f2efd968aba31c03bbf7979530d0c63b4834a418684509"
EXPECTED_MSV_IDS = tuple(f"FAPI-MSV-{number:03d}" for number in range(10, 280, 10))
EXPECTED_DOMAINS = {
    "FND": 6, "HTTP": 8, "ASGI": 7, "PYD": 12, "APP": 10, "DEP": 7,
    "MID": 5, "DB": 12, "MIG": 7, "ARC": 7, "ASY": 9, "SEC": 10,
    "RT": 9, "TST": 8, "OPS": 7, "SYN": 5, "MSV": 27,
}
DOMAIN_SLUGS = {
    "FND":"environment-first-application", "HTTP":"http-api-semantics",
    "ASGI":"asgi-starlette-server", "PYD":"pydantic-settings",
    "APP":"fastapi-routing", "DEP":"dependencies-lifecycle",
    "MID":"middleware-cross-cutting", "DB":"postgresql-sqlalchemy",
    "MIG":"alembic-schema-evolution", "ARC":"application-architecture",
    "ASY":"async-concurrency-performance", "SEC":"security",
    "RT":"realtime-transports", "TST":"testing-debugging",
    "OPS":"production-operations", "SYN":"interview-synthesis",
    "MSV":"microservices-distributed-services",
}
EXPECTED_PROJECT_IDS = [f"FAPI-PRJ-{number:03d}" for number in range(10, 110, 10)]
EXPECTED_PATHS = [
    ("absolute-fastapi-beginner", "Absolute FastAPI beginner path"),
    ("emergency-fastapi-interview", "Emergency FastAPI interview revision"),
    ("seven-day-fastapi-refresher", "7-day FastAPI refresher"),
    ("fourteen-day-backend-interview", "14-day backend interview preparation"),
    ("thirty-day-production-foundation", "30-day production foundation"),
    ("ninety-day-fastapi-mastery", "90-day FastAPI mastery"),
    ("complete-fastapi-mastery", "Complete FastAPI mastery"),
    ("deep-pydantic", "Deep Pydantic path"),
    ("postgres-sqlalchemy-alembic", "PostgreSQL, SQLAlchemy, and Alembic path"),
    ("async-concurrency-performance", "Async, concurrency, and performance path"),
    ("security-authentication", "Security and authentication path"),
    ("api-architecture-production", "API architecture and production path"),
    ("realtime-streaming-grpc", "WebSockets, SSE, streaming, and gRPC path"),
    ("senior-interview-design-practice", "Senior interview and design-practice path"),
    ("rabbitmq-reliable-async-services", "RabbitMQ and reliable asynchronous services"),
    ("microservices-distributed-service-engineering", "Microservices and distributed service engineering"),
    ("senior-microservices-design-operations", "Senior microservices design and operations"),
]

MSV_PATH_SLUGS = {
    "rabbitmq-reliable-async-services",
    "microservices-distributed-service-engineering",
    "senior-microservices-design-operations",
}
REQUIRED_FILES = [
    ".gitignore", ".python-version", ".env.example", "AGENTS.md",
    "API_DESIGN_PLAYBOOK.md", "BUNDLE_MANIFEST.md", "CURRICULUM.md",
    "INTERVIEW_PLAYBOOK.md", "LEARNING_PATHS.md", "NOTEBOOKLM.md",
    "PROGRESS.md", "PROJECTS.md", "PYTHON_REFERENCES.md", "README.md",
    "SOLID_DESIGN_REFERENCES.md", "START_HERE.md", "compose.yaml", "pyproject.toml", "uv.lock",
    "data/toolchain.json", "data/msv_extension.json", "docs/COPYRIGHT_AND_LICENSE.md", "docs/NOTEBOOKLM.md",
    "docs/SOURCE_AND_VERSION_POLICY.md", "docs/TOOLCHAIN_AND_INFRASTRUCTURE.md",
    "docs/WORKFLOW.md", "templates/experiment.md", "templates/mock_interview.md",
    "templates/practice.md", "templates/project.md", "templates/review.md",
    "templates/unit.md", "scripts/validate_repo.py",
]
VALIDATION_PROFILES = {"auto", "bootstrap", "live", "archive"}
WORKING_PROFILES = {"bootstrap", "live"}
WORKING_IGNORED_ROOT_DIRECTORIES = {".venv", "venv", "env", "ENV"}
WORKING_IGNORED_DIRECTORY_NAMES = {
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".hypothesis", "htmlcov",
}
WORKING_IGNORED_FILE_NAMES = {".coverage", "coverage.xml", "coverage.json", "lcov.info"}
WORKING_IGNORED_SUFFIXES = {".pyc", ".pyo"}
WORKING_FORBIDDEN_COMPONENTS = {
    "private", "tokens", "secrets", "credentials", "transcripts", "chat-exports",
}
ARCHIVE_FORBIDDEN_COMPONENTS = (
    WORKING_FORBIDDEN_COMPONENTS | WORKING_IGNORED_ROOT_DIRECTORIES | WORKING_IGNORED_DIRECTORY_NAMES
)
WORKING_BOOTSTRAP_FORBIDDEN_ROOTS = {"units", "projects", "attempts", "solutions"}
LIVE_FORBIDDEN_ROOTS = {"attempts", "solutions"}
ARCHIVE_FORBIDDEN_ROOTS = {".git", "units", "projects", "attempts", "solutions"}
FORBIDDEN_LICENSE_NAMES = {"LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING"}
SENSITIVE_SUFFIXES = {".pem", ".key", ".p12", ".pfx", ".kdbx"}
ALLOWED_PRIORITIES = {"C", "P", "A", "R"}
ALLOWED_FREQUENCIES = {"H", "M", "L"}
ALLOWED_DEPTHS = {"D1", "D2", "D3", "D4"}
ALLOWED_DIFFICULTIES = {1,2,3,4,5}
ALLOWED_SIZES = {"S", "M", "L", "XL"}
ALLOWED_EVIDENCE = {"E", "T", "I", "D", "X", "(X)", "R", "M"}
ALLOWED_ARTIFACT_STATES = {"Absent", "Draft", "Approved"}
ALLOWED_LEARNING_STATES = {"Not started", "Learning", "Practiced", "Recalled", "Demonstrated", "Retained"}
ALLOWED_PROJECT_STATES = {"Planned", "Active", "Complete"}
SIZE_HOURS = {
    "S": ((1,2),(1,2)), "M": ((2,4),(3,5)), "L": ((4,7),(5,9)), "XL": ((7,12),(9,16)),
}
RAPID_MINUTES = {"S":(20,30), "M":(30,45), "L":(45,70), "XL":(70,100)}
REQUIRED_DEV_TOOLS = {"pytest", "pytest-cov", "pytest-asyncio", "hypothesis", "ruff", "mypy"}
REQUIRED_GROUPS = {"dev", "postgres", "rabbitmq", "grpc", "redis", "observability"}
APPROVED_PYTHON_IDS = {
    "PY-BLT-030", "PY-CON-010", "PY-CON-020", "PY-CON-030", "PY-CON-050",
    "PY-CON-060", "PY-CON-070", "PY-CON-080", "PY-ERR-010", "PY-ERR-020",
    "PY-ERR-030", "PY-FIT-010", "PY-FIT-020", "PY-FIT-050", "PY-FIT-080",
    "PY-FIT-090", "PY-FND-020", "PY-IOP-080", "PY-IOP-090", "PY-MOD-010",
    "PY-MOD-020", "PY-MOD-030", "PY-MOD-050", "PY-MOD-060", "PY-MPR-010",
    "PY-MPR-060", "PY-MPR-080", "PY-MPR-090", "PY-MPR-100", "PY-SEC-010",
    "PY-SEC-030", "PY-SEC-040", "PY-SEC-050", "PY-SEC-060", "PY-SEC-070",
    "PY-TST-020", "PY-TST-030", "PY-TST-040", "PY-TST-050", "PY-TST-060",
    "PY-TYP-010", "PY-TYP-020", "PY-TYP-030", "PY-TYP-050", "PY-TYP-060",
}
REQUIRED_SEMANTICS = {
    "FAPI-ASGI-020": ({"scope", "receive", "send"}, {"request", "messages", "lifetime"}),
    "FAPI-PYD-070": ({"validators", "ordering", "context"}, {"before", "after", "plain", "wrap"}),
    "FAPI-DEP-040": ({"yield", "teardown", "resource"}, {"cleanup", "exception", "cancellation", "yield"}),
    "FAPI-DB-050": ({"transactions", "flush", "commit", "rollback"}, {"flush", "commit", "rollback", "savepoint"}),
    "FAPI-MIG-030": ({"autogenerate", "review"}, {"review", "constraints", "indexes", "defaults"}),
    "FAPI-ASY-010": ({"def", "async def", "event-loop"}, {"choose", "dispatches", "work"}),
    "FAPI-SEC-030": ({"jwt", "refresh", "revocation"}, {"validate", "rotation", "revocation"}),
    "FAPI-RT-080": ({"grpc", "protocol buffers"}, {"generate", "unary", "metadata"}),
    "FAPI-SYN-010": ({"request-lifecycle", "framework-boundary"}, {"http", "asgi", "starlette", "fastapi", "pydantic"}),
}
REQUIRED_COVERAGE_PHRASES = [
    "client → reverse proxy → asgi server", "validation failure", "dependency failure",
    "streaming response", "websocket", "background work", "idempotent commands",
    "rfc problem details", "conditional requests", "wsgi versus asgi", "scope, receive, and send",
    "discriminated unions", "typeadapter", "validation aliases", "model validators",
    "dependency-graph", "use_cache", "yield dependencies", "middleware onion",
    "identity map", "unit-of-work", "implicit i/o", "n+1", "deadlocks",
    "autogenerate review", "multiple heads", "expand-and-contract", "vertical slices",
    "functional core", "blocking i/o", "structured concurrency", "backpressure",
    "refresh rotation", "object-level authorization", "ssrf", "server-sent events",
    "webhook", "long polling", "protocol buffers", "testclient", "migration tests",
    "reverse proxies", "metrics", "traces", "incident response",
]
MANUAL_ITEMS = [
    "Pedagogical quality and accuracy of future generated unit explanations",
    "Correctness and idiomatic quality of future learner and AI-generated code",
    "Production realism of future project implementations and interview simulations",
    "Copyright originality and source interpretation of future generated content",
]
IMPORTANT_REPORT_STATISTICS = (
    "domains", "domain_unit_counts", "curriculum_units", "unique_unit_ids", "prerequisite_edges",
    "learning_paths", "learning_path_topic_links", "learning_path_project_callouts", "projects",
    "python_mastery_references", "markdown_files", "markdown_tables", "markdown_links",
    "code_fence_blocks", "development_dependencies", "dependency_groups", "locked_packages",
    "required_files", "required_files_present", "compose_profiles", "msv_units",
    "solid_design_references", "baseline_prefix_preserved",
)
EXPECTED_SOLID_REFERENCES = {
    "SDP-FND-020": "Change pressure, responsibilities, and boundaries",
    "SDP-FND-030": "Cohesion, coupling, and dependency direction",
    "SDP-FND-040": "Abstraction, encapsulation, information hiding, and contracts",
    "SDP-FND-080": "Dependency management, test seams, and test doubles",
    "SDP-FND-100": "Modules, package boundaries, and circular dependencies",
    "SDP-FND-110": "Simplicity heuristics and collaboration laws",
    "SDP-SOL-010": "Single Responsibility Principle",
    "SDP-SOL-040": "Interface Segregation Principle",
    "SDP-SOL-050": "Dependency Inversion Principle",
    "SDP-SOL-080": "SOLID critiques, overapplication, and legacy refactoring",
    "SDP-STR-010": "Adapter", "SDP-STR-020": "Facade", "SDP-STR-040": "Proxy",
    "SDP-BEH-020": "State", "SDP-BEH-030": "Observer", "SDP-BEH-040": "Command",
    "SDP-BEH-050": "Chain of Responsibility",
    "SDP-APP-010": "Dependency Injection and the composition root",
    "SDP-APP-040": "Repository", "SDP-APP-050": "Unit of Work",
    "SDP-APP-060": "Service Layer", "SDP-APP-070": "Domain Events",
    "SDP-ARC-020": "Ports and Adapters / Hexagonal Architecture",
    "SDP-ARC-050": "Event-driven application boundaries",
    "SDP-ARC-060": "CQRS at application scale", "SDP-ARC-070": "Event Sourcing",
    "SDP-ARC-080": "Architectural boundaries and evolutionary design",
    "SDP-RAR-070": "Saga as a distributed workflow pattern",
    "SDP-RAR-080": "Circuit Breaker as a resilience pattern",
    "SDP-REF-070": "Circular dependencies and temporal coupling",
    "SDP-REF-080": "Mock-heavy tests and meaningless interfaces",
    "SDP-REF-090": "Unnecessary factories, abstraction layers, and pattern soup",
    "SDP-INT-060": "Observer versus publish/subscribe versus Mediator versus Domain Events",
    "SDP-INT-090": "Repository versus DAO and Unit of Work; object versus architectural boundaries",
}
MSV_REQUIRED_MARKERS = {
    "FAPI-MSV-010": ("modular monolith", "conway", "data ownership", "when not to use microservices"),
    "FAPI-MSV-020": ("partial failure", "network latency", "eventual consistency", "retry amplification"),
    "FAPI-MSV-030": ("rest", "grpc", "rabbitmq", "kafka-style", "temporal coupling", "backpressure"),
    "FAPI-MSV-040": ("command", "event", "correlation", "causation", "schema version"),
    "FAPI-MSV-050": ("direct exchange", "topic exchange", "fanout exchange", "headers exchange", "bindings"),
    "FAPI-MSV-060": ("connections", "channels", "virtual hosts", "topology recovery"),
    "FAPI-MSV-070": ("publisher confirms", "mandatory", "unroutable", "publish timeout"),
    "FAPI-MSV-080": ("manual acknowledgements", "prefetch", "crash", "duplicate"),
    "FAPI-MSV-090": ("bounded immediate", "dead-letter", "jitter", "poison"),
    "FAPI-MSV-100": ("classic queues", "quorum queues", "streams", "kafka"),
    "FAPI-MSV-110": ("at-most-once", "at-least-once", "exactly-once", "idempotency"),
    "FAPI-MSV-120": ("transactional outbox", "inbox", "dual writes", "cdc"),
    "FAPI-MSV-130": ("saga", "compensation", "orchestration", "manual intervention"),
    "FAPI-MSV-140": ("eventual consistency", "read models", "cqrs", "event-sourcing"),
    "FAPI-MSV-150": ("field-number", "reserved fields", "status details", "metadata"),
    "FAPI-MSV-160": ("deadline", "cancellation", "retry eligibility", "flow control"),
    "FAPI-MSV-170": ("channel reuse", "health checking", "load balancing", "mtls", "opentelemetry"),
    "FAPI-MSV-180": ("retry amplification", "circuit breaker", "bulkhead", "load shedding"),
    "FAPI-MSV-190": ("dns", "kubernetes services", "api gateway", "service-mesh"),
    "FAPI-MSV-200": ("database per service", "shared-database", "cross-service queries", "backup"),
    "FAPI-MSV-210": ("trace context", "span links", "sli", "slo", "burn-rate"),
    "FAPI-MSV-220": ("workload identity", "mtls", "token audience", "rabbitmq vhosts"),
    "FAPI-MSV-230": ("contract tests", "duplicate-delivery", "fault injection", "eventual-consistency"),
    "FAPI-MSV-240": ("backward-compatible", "rolling", "consumer draining", "queue backlog"),
    "FAPI-MSV-250": ("runbooks", "incident", "postmortem", "disaster recovery"),
    "FAPI-MSV-260": ("service ownership", "adrs", "golden paths", "team topology", "cost"),
    "FAPI-MSV-270": ("strangler", "migration", "sde-2", "sde-3"),
}
UNIT_README_HEADINGS = (
    "## Physical Notebook Core", "## 1. Learning outcomes and evidence",
    "## 3. Simple explanation and owning layer", "## 4. Runtime or request-lifecycle trace",
    "## 5. Detailed visual model", "## 6. Worked examples", "## 7. Formal mechanics and boundaries",
    "## 8. Failure modes and edge cases", "## 9. Performance, resource, transaction, or security costs",
    "## 10. Production relevance and anti-signals", "## 11. Testing and debugging strategy",
    "## 12. Practice ladder", "## 13. Interview questions, traps, and follow-ups",
    "## 14. Explanation exercises", "## 15. Experiment decision",
    "## 16. Python Mastery references", "## 17. Authoritative sources and version notes",
)
REVIEW_HEADINGS = (
    "## Closed-book reconstruction", "## Request or execution-lifecycle explanation",
    "## Debugging questions", "## Design and trade-off questions", "## Delayed-recall prompts",
    "## Interview explanation practice", "## Evidence", "## State decision",
)
PREMATURE_SOLUTION_MARKERS = (
    "## complete solution", "### complete solution", "here is the complete solution",
    "final solution code", "<!-- solution revealed -->",
)
PLACEHOLDER_RE = re.compile(r"\{\{[A-Z0-9_:-]+\}\}")

@dataclass(frozen=True)
class Unit:
    unit_id: str
    title: str
    outcome: str
    prerequisites: tuple[str,...]
    priority: str
    interview: str
    production: str
    backend: str
    depth: str
    difficulty: int
    scopes: tuple[str,...]
    size: str
    evidence: tuple[str,...]
    anchor: str

@dataclass(frozen=True)
class ProgressEntry:
    unit_id: str
    title: str
    priority: str
    artifact_state: str
    learning_state: str

@dataclass
class Report:
    root: Path
    profile: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    checks: dict[str,str] = field(default_factory=dict)
    statistics: dict[str,object] = field(default_factory=dict)
    archive: dict[str,object] | None = None
    skipped_external_checks: list[str] = field(default_factory=list)
    self_tests: dict[str,object] | None = None
    def error(self, message: str) -> None: self.errors.append(message)
    def warning(self, message: str) -> None: self.warnings.append(message)
    def mark(self, name: str, value: bool | str) -> None:
        if isinstance(value, str): self.checks[name] = value
        else: self.checks[name] = "passed" if value else "failed"
    def as_dict(self) -> dict[str,object]:
        return {
            "schema_version": 1,
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "status": "passed" if not self.errors else "failed",
            "repository_root": ".",
            "validation_profile": self.profile,
            "validation_scope": {
                "automated": "completed",
                "manual_inspection": {"status":"not_performed", "items":MANUAL_ITEMS},
            },
            "checks": self.checks,
            "statistics": self.statistics,
            "archive": self.archive,
            "skipped_external_checks": self.skipped_external_checks,
            "self_tests": self.self_tests,
            "errors": self.errors,
            "warnings": self.warnings,
        }

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()

def split_table_row(line: str) -> list[str]:
    stripped=line.strip()
    if not (stripped.startswith("|") and stripped.endswith("|")): return []
    body=stripped[1:-1]; cells=[]; current=[]; escaped=False
    for char in body:
        if escaped: current.append(char); escaped=False
        elif char=="\\": current.append(char); escaped=True
        elif char=="|": cells.append("".join(current).strip()); current=[]
        else: current.append(char)
    cells.append("".join(current).strip())
    return cells

def resolve_profile(root: Path, profile: str) -> str:
    if profile not in VALIDATION_PROFILES: raise ValueError(profile)
    if profile != "auto": return profile
    return "live" if (root/"units").exists() or (root/"projects").exists() else "bootstrap"

def is_sensitive_env(path: Path | PurePosixPath) -> bool:
    return path.name == ".env" or path.name.startswith(".env.") and path.name != ".env.example"

def working_ignored_dir(root: Path, path: Path, profile: str) -> bool:
    if profile not in WORKING_PROFILES: return False
    try: rel=path.relative_to(root)
    except ValueError: return False
    if not rel.parts: return False
    if rel.parts[0]==".git": return True
    if len(rel.parts)==1 and rel.name in WORKING_IGNORED_ROOT_DIRECTORIES: return True
    return any(part in WORKING_IGNORED_DIRECTORY_NAMES for part in rel.parts)

def working_ignored_file(root: Path, path: Path, profile: str) -> bool:
    if profile not in WORKING_PROFILES: return False
    try: rel=path.relative_to(root)
    except ValueError: return False
    if not rel.parts: return False
    if rel.parts[0]==".git": return True
    if len(rel.parts)>1 and (rel.parts[0] in WORKING_IGNORED_ROOT_DIRECTORIES or any(p in WORKING_IGNORED_DIRECTORY_NAMES for p in rel.parts[:-1])): return True
    return rel.name in WORKING_IGNORED_FILE_NAMES or rel.name.startswith(".coverage.") or path.suffix.lower() in WORKING_IGNORED_SUFFIXES

def archive_working_artifact(parts: tuple[str,...]) -> bool:
    if not parts: return False
    name=parts[-1]
    return (any(p in WORKING_IGNORED_ROOT_DIRECTORIES for p in parts)
            or any(p in WORKING_IGNORED_DIRECTORY_NAMES for p in parts)
            or name in WORKING_IGNORED_FILE_NAMES or name.startswith(".coverage.")
            or PurePosixPath(name).suffix.lower() in WORKING_IGNORED_SUFFIXES)

def iter_repo_files(root: Path, profile: str) -> list[Path]:
    result=[]
    for current, dirs, files in os.walk(root):
        current_path=Path(current)
        if working_ignored_dir(root,current_path,profile): dirs[:]=[]; continue
        dirs[:]=[d for d in dirs if not working_ignored_dir(root,current_path/d,profile)]
        for name in files:
            path=current_path/name
            if not working_ignored_file(root,path,profile): result.append(path)
    return sorted(result)

def validate_hygiene(report: Report) -> None:
    missing=[name for name in REQUIRED_FILES if not (report.root/name).is_file()]
    if missing: report.error(f"[REQUIRED_FILES_MISSING] Missing required files: {missing}")
    for name in FORBIDDEN_LICENSE_NAMES:
        if (report.root/name).exists(): report.error(f"[LICENSE_FORBIDDEN] License file present without approval: {name}")
    gitignore=(report.root/".gitignore").read_text(encoding="utf-8") if (report.root/".gitignore").is_file() else ""
    for entry in (".venv/", "__pycache__/", "private/", "tokens/", ".env"):
        if entry not in gitignore: report.error(f"[GITIGNORE_ENTRY_MISSING] .gitignore must include {entry}")
    forbidden_roots = WORKING_BOOTSTRAP_FORBIDDEN_ROOTS if report.profile=="bootstrap" else LIVE_FORBIDDEN_ROOTS if report.profile=="live" else ARCHIVE_FORBIDDEN_ROOTS
    for current, dirs, files in os.walk(report.root):
        base=Path(current)
        if working_ignored_dir(report.root,base,report.profile): dirs[:]=[]; continue
        dirs[:]=[d for d in dirs if not working_ignored_dir(report.root,base/d,report.profile)]
        for directory in list(dirs):
            rel=(base/directory).relative_to(report.root)
            if rel.parts and rel.parts[0] in forbidden_roots:
                report.error(f"[PROFILE_FORBIDDEN_ROOT_PATH] {report.profile} profile forbids: {rel}")
                dirs.remove(directory); continue
            if any(part in WORKING_FORBIDDEN_COMPONENTS for part in rel.parts):
                report.error(f"[PROFILE_FORBIDDEN_PRIVATE_PATH] {report.profile} profile forbids: {rel}")
                dirs.remove(directory)
        for name in files:
            path=base/name; rel=path.relative_to(report.root)
            if working_ignored_file(report.root,path,report.profile): continue
            if rel.parts and rel.parts[0] in forbidden_roots:
                report.error(f"[PROFILE_FORBIDDEN_ROOT_PATH] {report.profile} profile forbids: {rel}")
            if any(part in WORKING_FORBIDDEN_COMPONENTS for part in rel.parts) or is_sensitive_env(rel):
                report.error(f"[PROFILE_FORBIDDEN_PRIVATE_PATH] {report.profile} profile forbids: {rel}")
            if path.suffix.lower() in SENSITIVE_SUFFIXES:
                report.error(f"[PROFILE_FORBIDDEN_PRIVATE_PATH] Sensitive key material forbidden: {rel}")
    report.statistics["required_files"]=len(REQUIRED_FILES)
    report.statistics["required_files_present"]=len(REQUIRED_FILES)-len(missing)
    report.mark("required_files_and_hygiene", not any("FORBIDDEN" in e or "MISSING" in e for e in report.errors))

def parse_units(report: Report) -> tuple[list[Unit],dict[str,Unit]]:
    path=report.root/"CURRICULUM.md"
    if not path.is_file(): return [],{}
    text=path.read_text(encoding="utf-8")
    rows=[]
    for line in text.splitlines():
        cells=split_table_row(line)
        if len(cells)!=12 or "<a id=" not in cells[0] or "FAPI-" not in cells[0]: continue
        match=re.search(r'<a id="([a-z0-9-]+)"></a>`(FAPI-[A-Z]{2,4}-\d{3})` — \*\*(.+?)\*\*',cells[0])
        if not match:
            report.error(f"[CURRICULUM_ROW_MALFORMED] Cannot parse unit row: {cells[0]}"); continue
        anchor,uid,title=match.groups()
        prereqs=tuple(UNIT_ID_RE.findall(cells[2]))
        evidence=tuple(re.findall(r"\(X\)|[ETIDRXM]",cells[11]))
        scopes=tuple(item.strip() for item in cells[9].split(",") if item.strip())
        try: difficulty=int(cells[8].strip("`"))
        except ValueError:
            report.error(f"[CLASSIFICATION_INVALID] Invalid difficulty for {uid}: {cells[8]}"); difficulty=0
        rows.append(Unit(uid,title,cells[1],prereqs,cells[3].strip("`"),cells[4].strip("`"),cells[5].strip("`"),cells[6].strip("`"),cells[7].strip("`"),difficulty,scopes,cells[10].strip("`"),evidence,anchor))
    by_id={}
    for unit in rows:
        if unit.unit_id in by_id: report.error(f"[DUPLICATE_UNIT_ID] Duplicate canonical unit ID: {unit.unit_id}")
        by_id[unit.unit_id]=unit
        expected_anchor=unit.unit_id.lower()
        if unit.anchor!=expected_anchor: report.error(f"[UNIT_ANCHOR_MISMATCH] {unit.unit_id}: {unit.anchor} != {expected_anchor}")
        code=unit.unit_id.split("-")[1]
        if code not in EXPECTED_DOMAINS: report.error(f"[UNKNOWN_DOMAIN] {unit.unit_id} uses unknown domain {code}")
        if unit.priority not in ALLOWED_PRIORITIES: report.error(f"[CLASSIFICATION_INVALID] {unit.unit_id} priority {unit.priority}")
        for label,value in (("interview",unit.interview),("production",unit.production),("backend",unit.backend)):
            if value not in ALLOWED_FREQUENCIES: report.error(f"[CLASSIFICATION_INVALID] {unit.unit_id} {label} {value}")
        if unit.depth not in ALLOWED_DEPTHS or unit.difficulty not in ALLOWED_DIFFICULTIES or unit.size not in ALLOWED_SIZES:
            report.error(f"[CLASSIFICATION_INVALID] Invalid depth/difficulty/size for {unit.unit_id}")
        if not unit.scopes: report.error(f"[CLASSIFICATION_INVALID] Empty scope for {unit.unit_id}")
        invalid=set(unit.evidence)-ALLOWED_EVIDENCE
        if invalid or not unit.evidence: report.error(f"[CLASSIFICATION_INVALID] Invalid evidence for {unit.unit_id}: {invalid}")
    if len(rows)!=EXPECTED_UNIT_COUNT or len(by_id)!=EXPECTED_UNIT_COUNT:
        report.error(f"[UNIT_COUNT_MISMATCH] Expected {EXPECTED_UNIT_COUNT}, found {len(rows)} rows/{len(by_id)} unique")
    counts=Counter(u.unit_id.split("-")[1] for u in rows)
    if dict(counts)!=EXPECTED_DOMAINS: report.error(f"[DOMAIN_COUNT_MISMATCH] Expected {EXPECTED_DOMAINS}, found {dict(counts)}")
    index={u.unit_id:i for i,u in enumerate(rows)}
    edges=0
    for unit in rows:
        for prerequisite in unit.prerequisites:
            edges+=1
            if prerequisite not in by_id: report.error(f"[MISSING_PREREQUISITE] {unit.unit_id} references {prerequisite}")
            elif index[prerequisite]>=index[unit.unit_id]: report.error(f"[CURRICULUM_PREREQUISITE_ORDER] {prerequisite} must precede {unit.unit_id}")
    indegree={uid:0 for uid in by_id}; graph=defaultdict(list)
    for unit in rows:
        for pre in unit.prerequisites:
            if pre in by_id: graph[pre].append(unit.unit_id); indegree[unit.unit_id]+=1
    queue=deque(uid for uid,degree in indegree.items() if degree==0); visited=0
    while queue:
        uid=queue.popleft(); visited+=1
        for nxt in graph[uid]:
            indegree[nxt]-=1
            if indegree[nxt]==0: queue.append(nxt)
    if visited!=len(by_id): report.error("[PREREQUISITE_CYCLE] Curriculum prerequisite graph contains a cycle")
    extension_path=report.root/"data/msv_extension.json"
    try:
        extension=json.loads(extension_path.read_text(encoding="utf-8"))
        if extension.get("baseline_zip_sha256")!=EXPECTED_BASELINE_ZIP_SHA256:
            report.error("[MSV_BASELINE_ZIP_IDENTITY_MISMATCH] data/msv_extension.json")
        if extension.get("baseline_unit_count")!=BASELINE_UNIT_COUNT or extension.get("added_unit_count")!=27 or extension.get("final_unit_count")!=EXPECTED_UNIT_COUNT:
            report.error("[MSV_EXTENSION_COUNT_MISMATCH] data/msv_extension.json")
        curriculum_rows=[line for line in text.splitlines() if "<a id=\"fapi-" in line and "`FAPI-" in line]
        actual_prefix_hash=hashlib.sha256(("\n".join(curriculum_rows[:BASELINE_UNIT_COUNT])+"\n").encode()).hexdigest()
        if actual_prefix_hash!=EXPECTED_BASELINE_UNIT_ROWS_SHA256 or extension.get("baseline_unit_rows_sha256")!=EXPECTED_BASELINE_UNIT_ROWS_SHA256:
            report.error(f"[MSV_BASELINE_PREFIX_CHANGED] {actual_prefix_hash}")
        actual_msv=tuple(unit.unit_id for unit in rows[BASELINE_UNIT_COUNT:])
        if actual_msv!=EXPECTED_MSV_IDS or tuple(extension.get("msv_ids",[]))!=EXPECTED_MSV_IDS:
            report.error(f"[MSV_ID_SEQUENCE_MISMATCH] {actual_msv}")
        report.statistics["baseline_prefix_preserved"] = actual_prefix_hash==EXPECTED_BASELINE_UNIT_ROWS_SHA256
        report.statistics["msv_units"] = len(actual_msv)
    except Exception as exc:
        report.error(f"[MSV_EXTENSION_METADATA_INVALID] {exc}")
    report.statistics["domains"]=len(counts)
    report.statistics["domain_unit_counts"]=dict(counts)
    report.statistics["curriculum_units"]=len(rows)
    report.statistics["unique_unit_ids"]=len(by_id)
    report.statistics["prerequisite_edges"]=edges
    report.mark("curriculum", not any(code in "\n".join(report.errors) for code in ("UNIT_","DOMAIN_","PREREQUISITE","CLASSIFICATION")))
    return rows,by_id

def validate_coverage(report: Report, units: dict[str,Unit]) -> None:
    for uid,(title_words,outcome_words) in REQUIRED_SEMANTICS.items():
        unit=units.get(uid)
        if not unit:
            report.error(f"[REQUIRED_SEMANTIC_UNIT_MISSING] {uid}"); continue
        title=unit.title.lower(); outcome=unit.outcome.lower()
        missing_title=sorted(word for word in title_words if word not in title)
        missing_outcome=sorted(word for word in outcome_words if word not in outcome)
        if missing_title or missing_outcome:
            report.error(f"[REQUIRED_SEMANTIC_MISMATCH] {uid}: title {missing_title}; outcome {missing_outcome}")
    combined=(report.root/"CURRICULUM.md").read_text(encoding="utf-8").lower()
    for phrase in REQUIRED_COVERAGE_PHRASES:
        if phrase not in combined: report.error(f"[COVERAGE_PHRASE_MISSING] {phrase}")
    report.mark("coverage_matrix", not any("COVERAGE" in e or "SEMANTIC" in e for e in report.errors))

def parse_progress(report: Report, units: dict[str,Unit]) -> dict[str,ProgressEntry]:
    path=report.root/"PROGRESS.md"; result={}
    for line in path.read_text(encoding="utf-8").splitlines():
        cells=split_table_row(line)
        if len(cells)!=9 or not UNIT_ID_RE.fullmatch(cells[0].strip("`")): continue
        uid=cells[0].strip("`")
        entry=ProgressEntry(uid,cells[1],cells[2].strip("`"),cells[3],cells[4])
        if uid in result: report.error(f"[PROGRESS_DUPLICATE] Duplicate progress row: {uid}")
        result[uid]=entry
        unit=units.get(uid)
        if not unit: report.error(f"[PROGRESS_UNKNOWN_UNIT] {uid}"); continue
        if entry.title!=unit.title: report.error(f"[PROGRESS_TITLE_MISMATCH] {uid}: {entry.title!r} != {unit.title!r}")
        if entry.priority!=unit.priority: report.error(f"[PROGRESS_PRIORITY_MISMATCH] {uid}")
        if entry.artifact_state not in ALLOWED_ARTIFACT_STATES or entry.learning_state not in ALLOWED_LEARNING_STATES:
            report.error(f"[PROGRESS_STATE_INVALID] {uid}")
    if set(result)!=set(units): report.error(f"[PROGRESS_PARITY_MISMATCH] Missing={sorted(set(units)-set(result))}; extra={sorted(set(result)-set(units))}")
    report.mark("progress_parity", not any("PROGRESS_" in e for e in report.errors))
    return result

def parse_projects(report: Report, units: dict[str,Unit]) -> dict[str,str]:
    text=(report.root/"PROJECTS.md").read_text(encoding="utf-8")
    matches=re.findall(r'<a id="(fapi-prj-\d{3})"></a>\n## (FAPI-PRJ-\d{3}) — (.+)',text)
    projects={uid:title.strip() for _anchor,uid,title in matches}
    if list(projects)!=EXPECTED_PROJECT_IDS:
        report.error(f"[PROJECT_ID_ORDER_MISMATCH] Expected {EXPECTED_PROJECT_IDS}, found {list(projects)}")
    for anchor,uid,title in matches:
        if anchor!=uid.lower(): report.error(f"[PROJECT_ANCHOR_MISMATCH] {uid}")
        section=text.split(f'<a id="{anchor}"></a>',1)[1].split('<a id="fapi-prj-',1)[0]
        for required_heading in ("### Staged change pressure","### Governing invariants","### Seeded defects","### Adversarial tests and evidence","### Refactoring checkpoint","### Rejected alternatives","### Operational exercise","### Required visuals","### Definition of done"):
            if required_heading not in section: report.error(f"[PROJECT_SECTION_MISSING] {uid}: {required_heading}")
        for referenced in UNIT_ID_RE.findall(section):
            if PROJECT_ID_RE.fullmatch(referenced):
                continue
            if referenced not in units: report.error(f"[PROJECT_UNKNOWN_PREREQUISITE] {uid}: {referenced}")
    normalized=[]
    for anchor,uid,title in matches:
        section=text.split(f'<a id="{anchor}"></a>',1)[1].split('<a id="fapi-prj-',1)[0].lower()
        section=re.sub(r'fapi-prj-\d{3}|\*\*.+?\*\*','',section)
        normalized.append((uid,re.sub(r'\s+',' ',section)))
    for i,(left_id,left) in enumerate(normalized):
        for right_id,right in normalized[i+1:]:
            # Exact boilerplate is forbidden; qualitative similarity remains manual.
            if left==right: report.error(f"[PROJECT_IDENTICAL_CONTENT] {left_id} and {right_id}")
    tracker={}
    progress=(report.root/"PROGRESS.md").read_text(encoding="utf-8")
    for line in progress.splitlines():
        cells=split_table_row(line)
        if len(cells)==7 and PROJECT_ID_RE.fullmatch(cells[0].strip("`")):
            uid=cells[0].strip("`"); tracker[uid]=(cells[1],cells[2],cells[3].strip("`"))
            if cells[2] not in ALLOWED_PROJECT_STATES: report.error(f"[PROJECT_STATE_INVALID] {uid}: {cells[2]}")
            if cells[3].strip("`")!=f"project/{uid}": report.error(f"[PROJECT_BRANCH_MISMATCH] {uid}")
    if set(tracker)!=set(projects): report.error(f"[PROJECT_TRACKER_PARITY] Missing={sorted(set(projects)-set(tracker))}; extra={sorted(set(tracker)-set(projects))}")
    for uid,title in projects.items():
        if uid in tracker and tracker[uid][0]!=title: report.error(f"[PROJECT_TRACKER_TITLE_MISMATCH] {uid}")
    report.statistics["projects"]=len(projects)
    report.mark("projects", not any("PROJECT_" in e for e in report.errors))
    return projects

def validate_readme_counts(report: Report) -> None:
    text=(report.root/"README.md").read_text(encoding="utf-8")
    expected={
        "units": rf"\b{EXPECTED_UNIT_COUNT} canonical learning units\b",
        "paths": rf"\b{EXPECTED_PATH_COUNT} prerequisite-safe learning paths\b",
        "projects": rf"\b{EXPECTED_PROJECT_COUNT} milestone projects\b",
    }
    for label,pattern in expected.items():
        if not re.search(pattern,text):
            report.error(f"[README_COUNT_MISMATCH] README does not report {label}={ {'units':EXPECTED_UNIT_COUNT,'paths':EXPECTED_PATH_COUNT,'projects':EXPECTED_PROJECT_COUNT}[label] }")
    report.mark("readme_counts",not any("README_COUNT" in error for error in report.errors))


def human_minutes(value: int) -> str:
    hours,minutes=divmod(value,60)
    if hours and minutes: return f"{hours} h {minutes} min"
    if hours: return f"{hours} h"
    return f"{minutes} min"


def clean_summary_cell(value: str) -> str:
    return re.sub(r"[`*]", "", value).strip()


def parse_displayed_count(value: str) -> int | None:
    match=re.fullmatch(r"([0-9][0-9,]*)",clean_summary_cell(value))
    return int(match.group(1).replace(",","")) if match else None


def parse_displayed_minutes(value: str) -> list[int] | None:
    text=clean_summary_cell(value)
    parts=re.split(r"\s*[–—-]\s*",text)
    if len(parts)!=2: return None
    parsed=[]
    for part in parts:
        match=re.fullmatch(r"(?:(\d[\d,]*)\s*h)?(?:\s*(\d[\d,]*)\s*min)?",part.strip())
        if not match or (match.group(1) is None and match.group(2) is None): return None
        hours=int(match.group(1).replace(",","")) if match.group(1) else 0
        minutes=int(match.group(2).replace(",","")) if match.group(2) else 0
        if minutes>=60: return None
        parsed.append(hours*60+minutes)
    return parsed


def parse_displayed_hours(value: str) -> list[int] | None:
    text=clean_summary_cell(value)
    match=re.fullmatch(r"([0-9][0-9,]*)\s*[–—-]\s*([0-9][0-9,]*)\s*h",text)
    if not match: return None
    return [int(match.group(1).replace(",","")),int(match.group(2).replace(",",""))]


def visible_path_summary(body: str) -> dict[str,str]:
    summary={}
    for line in body.splitlines():
        cells=split_table_row(line)
        if len(cells)!=2: continue
        label=clean_summary_cell(cells[0]).lower()
        value=clean_summary_cell(cells[1])
        if label.startswith("canonical units"):
            summary["declared_units"]=value
        elif label=="rapid unit study":
            summary["rapid_unit_minutes"]=value
        elif label=="rapid path total":
            summary["rapid_total_minutes"]=value
        elif label=="full mastery of included units":
            summary["full_mastery_hours"]=value
    return summary


def path_unit_links(body: str) -> list[tuple[str,str,str]]:
    sequence_body=body.split("### Recommended sequence",1)[1].split("### Project milestones",1)[0] if "### Recommended sequence" in body else ""
    return re.findall(r'\[(FAPI-[A-Z]{2,4}-\d{3}) — ([^\]]+)\]\(CURRICULUM\.md#(fapi-[a-z0-9-]+)\)',sequence_body)


def validate_reference_quality(report: Report) -> None:
    banned=(
        "Use a five-minute model of the Python behavior",
        "provides the Python mechanism needed to reason about",
        "Use the owning unit’s five-minute bridge",
        "Across a process, the contract gains latency, compatibility, security, observability, ownership, and failure semantics",
        "Do not convert a useful local abstraction into a remote service or shared library without measurable change pressure",
    )
    guidance_rows=[]
    for filename in ("PYTHON_REFERENCES.md","SOLID_DESIGN_REFERENCES.md"):
        text=(report.root/filename).read_text(encoding="utf-8")
        for phrase in banned:
            if phrase in text:
                report.error(f"[REFERENCE_GENERIC_MAPPING] {filename} contains generic boilerplate: {phrase}")
        for line in text.splitlines():
            cells=split_table_row(line)
            if len(cells)==7 and cells[0].startswith("`") and (PYTHON_ID_RE.search(cells[1]) or SDP_ID_RE.search(cells[1])):
                if any(len(re.sub(r'[`*_]','',cell).strip())<24 for cell in cells[3:]):
                    report.error(f"[REFERENCE_MAPPING_SHALLOW] {filename}: {cells[0]} -> {cells[1]}")
                normalized=" | ".join(re.sub(r'\s+',' ',cell.strip().lower()) for cell in cells[3:])
                guidance_rows.append((filename,cells[0],cells[1],normalized))
    repeated=Counter(row[3] for row in guidance_rows)
    for guidance,count in repeated.items():
        if count>=5:
            report.error(f"[REFERENCE_GENERIC_MAPPING] identical guidance repeated {count} times: {guidance[:120]}")
    report.mark("reference_quality",not any("REFERENCE_GENERIC" in error or "REFERENCE_MAPPING_SHALLOW" in error for error in report.errors))


def validate_rabbitmq_operational_docs(report: Report) -> None:
    compose=(report.root/"compose.yaml").read_text(encoding="utf-8")
    docs=(report.root/"docs/TOOLCHAIN_AND_INFRASTRUCTURE.md").read_text(encoding="utf-8")
    if '127.0.0.1:${RABBITMQ_AMQP_PORT:-5672}:5672' not in compose or '127.0.0.1:${RABBITMQ_MANAGEMENT_PORT:-15672}:15672' not in compose:
        report.error("[RABBITMQ_PORT_NOT_LOOPBACK] RabbitMQ AMQP and management ports must bind explicitly to 127.0.0.1")
    if "RABBITMQ_LEARNING_QUEUE:" not in compose:
        report.error("[RABBITMQ_ENV_PARITY] RabbitMQ service must receive RABBITMQ_LEARNING_QUEUE")
    if "$RABBITMQ_VHOST" in docs or "${RABBITMQ_MANAGEMENT_PORT" in docs:
        report.error("[RABBITMQ_HOST_ENV_RELIANCE] Commands must resolve RabbitMQ configuration inside the container or through `docker compose port`")
    if "consumer_capacity" in docs:
        report.error("[RABBITMQCTL_UNSUPPORTED_FIELD] Use the RabbitMQ 4.3-supported queue field consumer_utilisation")
    for match in re.finditer(r'rabbitmqctl\s+list_consumers[^\n\']*',docs):
        command=match.group(0)
        if any(field in command for field in ("queue_name","channel_pid","consumer_tag","ack_required","prefetch_count","active")):
            report.error(f"[RABBITMQCTL_UNSUPPORTED_ARGUMENT] list_consumers uses unsupported selectable columns: {command}")
    if 'rabbitmqctl list_consumers -p "$RABBITMQ_DEFAULT_VHOST"' not in docs:
        report.error("[RABBITMQCTL_INSPECTION_COMMAND_MISSING] Missing supported list_consumers command")
    required_fields=("consumer_utilisation","messages_ready","messages_unacknowledged","messages_unconfirmed","prefetch_count")
    for field in required_fields:
        if field not in docs:
            report.error(f"[RABBITMQCTL_INSPECTION_COMMAND_MISSING] Missing documented inspection field: {field}")
    lowered=docs.lower()
    if "docker compose down --volumes" in lowered or "docker compose down -v" in lowered or "docker system prune" in lowered or "docker compose --profile rabbitmq down" in lowered:
        report.error("[RABBITMQ_BROAD_VOLUME_DELETE] RabbitMQ reset must not stop unrelated services or delete broad Compose volumes")
    for command in ("docker compose --profile rabbitmq stop rabbitmq","docker compose --profile rabbitmq rm -f rabbitmq","docker volume inspect fastapi-mastery_fastapi_rabbitmq_data","docker volume rm fastapi-mastery_fastapi_rabbitmq_data"):
        if command not in docs:
            report.error(f"[RABBITMQ_SAFE_RESET_COMMAND_MISSING] {command}")
    if 'printf "vhost=%s queue=%s\\n"' not in docs:
        report.error("[RABBITMQ_PRINTF_MALFORMED] Expected a single escaped newline in the queue verification command")
    report.mark("rabbitmq_operations",not any(error.startswith("[RABBITMQ") for error in report.errors))


def parse_path_sections(text: str) -> list[tuple[str,str,dict[str,object],str]]:
    anchors=list(re.finditer(r'<a id="([a-z0-9-]+)"></a>\n## ([^\n]+)',text))
    sections=[]
    for index,match in enumerate(anchors):
        start=match.end(); end=anchors[index+1].start() if index+1<len(anchors) else len(text)
        body=text[start:end]
        meta_match=re.search(r'<!-- path-meta: (\{.*?\}) -->',body)
        if meta_match:
            sections.append((match.group(1),match.group(2).strip(),json.loads(meta_match.group(1)),body))
    return sections

def validate_learning_paths(report: Report, units: dict[str,Unit], projects: dict[str,str]) -> None:
    text=(report.root/"LEARNING_PATHS.md").read_text(encoding="utf-8")
    sections=parse_path_sections(text)
    found=[(anchor,title) for anchor,title,_meta,_body in sections]
    if found!=EXPECTED_PATHS: report.error(f"[PATH_SELECTOR_OR_ORDER_MISMATCH] Expected {EXPECTED_PATHS}, found {found}")
    all_links=0; all_projects=0
    effective_units: dict[str,set[str]]={}
    own_units: dict[str,set[str]]={}
    metas: dict[str,dict[str,object]]={}
    bodies: dict[str,str]={}
    previous_slugs=[]
    for anchor,title,meta,body in sections:
        metas[anchor]=meta; bodies[anchor]=body
        if meta.get("slug")!=anchor: report.error(f"[PATH_META_SLUG_MISMATCH] {anchor}")
        links=path_unit_links(body)
        ids=[uid for uid,_title,_anchor in links]
        own_units[anchor]=set(ids)
        all_links+=len(ids)
        if len(ids)!=len(set(ids)): report.error(f"[PATH_DUPLICATE_UNIT] {anchor}")
        if meta.get("declared_units")!=len(ids): report.error(f"[PATH_COUNT_MISMATCH] {anchor}: declared {meta.get('declared_units')}, actual {len(ids)}")
        assumed_raw=meta.get("assumed_prerequisites",[])
        assumed=set(assumed_raw) if isinstance(assumed_raw,list) else set()
        if not isinstance(assumed_raw,list) or any(uid not in units for uid in assumed):
            report.error(f"[PATH_ASSUMPTION_INVALID] {anchor}: {assumed_raw}")
        prior_raw=meta.get("assumed_prior_paths",[])
        prior_paths=prior_raw if isinstance(prior_raw,list) else []
        if not isinstance(prior_raw,list): report.error(f"[PATH_PRIOR_PATH_INVALID] {anchor}: {prior_raw}")
        inherited=set()
        for prior in prior_paths:
            if prior not in previous_slugs:
                report.error(f"[PATH_PRIOR_PATH_INVALID] {anchor}: {prior} must name an earlier path")
                continue
            inherited.update(effective_units.get(prior,set()))
            if f'](#{prior})' not in body:
                report.error(f"[PATH_PRIOR_PATH_UNDOCUMENTED] {anchor}: {prior}")
        assumption_body=body.split("### Assumed prior knowledge or prerequisite bridges",1)[1].split("### Recommended sequence",1)[0] if "### Assumed prior knowledge or prerequisite bridges" in body else ""
        for uid in assumed:
            if uid not in assumption_body:
                report.error(f"[PATH_ASSUMPTION_UNDOCUMENTED] {anchor}: {uid}")
        seen=set(inherited)|assumed
        for uid,linked_title,linked_anchor in links:
            unit=units.get(uid)
            if not unit: report.error(f"[PATH_UNKNOWN_UNIT] {anchor}: {uid}"); continue
            if linked_title!=unit.title: report.error(f"[PATH_TITLE_MISMATCH] {anchor}: {uid}")
            if linked_anchor!=uid.lower(): report.error(f"[PATH_ANCHOR_MISMATCH] {anchor}: {uid}")
            missing=[pre for pre in unit.prerequisites if pre not in seen]
            if missing: report.error(f"[PATH_PREREQUISITE_ORDER] {anchor}: {uid} before {missing}")
            seen.add(uid)
        effective_units[anchor]=seen
        previous_slugs.append(anchor)
        rapid=(0,0); full=(0,0)
        for uid in ids:
            if uid not in units: continue
            size=units[uid].size
            rapid=(rapid[0]+RAPID_MINUTES[size][0],rapid[1]+RAPID_MINUTES[size][1])
            first,practice=SIZE_HOURS[size]
            full=(full[0]+first[0]+practice[0],full[1]+first[1]+practice[1])
        if list(rapid)!=meta.get("rapid_unit_minutes"): report.error(f"[PATH_RAPID_UNIT_TIME_MISMATCH] {anchor}: expected {rapid}, declared {meta.get('rapid_unit_minutes')}")
        if list(full)!=meta.get("full_mastery_hours"): report.error(f"[PATH_FULL_TIME_MISMATCH] {anchor}: expected {full}, declared {meta.get('full_mastery_hours')}")
        total=[0,0]
        for key in ("rapid_unit_minutes","lab_minutes","recall_minutes","mock_minutes","checkpoint_minutes"):
            value=meta.get(key)
            if not isinstance(value,list) or len(value)!=2 or any(not isinstance(item,int) or item<0 for item in value):
                report.error(f"[PATH_TIME_COMPONENT_INVALID] {anchor}: {key}={value}"); value=[0,0]
            total[0]+=value[0]; total[1]+=value[1]
        if total!=meta.get("rapid_total_minutes"): report.error(f"[PATH_TOTAL_TIME_MISMATCH] {anchor}: expected {total}, declared {meta.get('rapid_total_minutes')}")
        visible=visible_path_summary(body)
        displayed_count=parse_displayed_count(visible.get("declared_units",""))
        if displayed_count!=meta.get("declared_units"):
            report.error(f"[PATH_VISIBLE_COUNT_MISMATCH] {anchor}: displayed {displayed_count!r}, metadata {meta.get('declared_units')!r}")
        displayed_rapid=parse_displayed_minutes(visible.get("rapid_unit_minutes",""))
        if displayed_rapid!=meta.get("rapid_unit_minutes"):
            report.error(f"[PATH_VISIBLE_RAPID_UNIT_TIME_MISMATCH] {anchor}: displayed {displayed_rapid!r}, metadata {meta.get('rapid_unit_minutes')!r}")
        displayed_total=parse_displayed_minutes(visible.get("rapid_total_minutes",""))
        if displayed_total!=meta.get("rapid_total_minutes"):
            report.error(f"[PATH_VISIBLE_RAPID_TOTAL_TIME_MISMATCH] {anchor}: displayed {displayed_total!r}, metadata {meta.get('rapid_total_minutes')!r}")
        displayed_full=parse_displayed_hours(visible.get("full_mastery_hours",""))
        if displayed_full!=meta.get("full_mastery_hours"):
            report.error(f"[PATH_VISIBLE_FULL_MASTERY_MISMATCH] {anchor}: displayed {displayed_full!r}, metadata {meta.get('full_mastery_hours')!r}")
        if anchor in MSV_PATH_SLUGS:
            weeks=meta.get("schedule_weeks"); hours=meta.get("hours_per_week")
            if not (isinstance(weeks,list) and len(weeks)==2 and all(isinstance(x,int) and x>0 for x in weeks) and weeks[0]<=weeks[1] and isinstance(hours,list) and len(hours)==2 and all(isinstance(x,int) and x>0 for x in hours) and hours[0]<=hours[1]):
                report.error(f"[PATH_SCHEDULE_METADATA_INVALID] {anchor}: weeks={weeks}, hours={hours}")
            else:
                min_capacity=weeks[0]*hours[0]*60; max_capacity=weeks[1]*hours[1]*60
                if min_capacity<total[0] or max_capacity<total[1]:
                    report.error(f"[PATH_SCHEDULE_CAPACITY_MISMATCH] {anchor}: schedule capacity [{min_capacity},{max_capacity}] cannot contain [{total[0]},{total[1]}]")
                hours_phrase=(f"{hours[0]} hours per week" if hours[0]==hours[1] else f"{hours[0]}–{hours[1]} hours per week")
                schedule_phrase=f"{weeks[0]}–{weeks[1]} weeks at {hours_phrase}"
                total_phrase=f"{human_minutes(total[0])}–{human_minutes(total[1])}"
                if schedule_phrase not in body or total_phrase not in body:
                    report.error(f"[PATH_SCHEDULE_PROSE_MISMATCH] {anchor}: expected `{schedule_phrase}` and `{total_phrase}`")
        project_links=re.findall(r'\[(FAPI-PRJ-\d{3}) — ([^\]]+)\]\(PROJECTS\.md#(fapi-prj-\d{3})\)',body)
        all_projects+=len(project_links)
        for uid,linked_title,linked_anchor in project_links:
            if projects.get(uid)!=linked_title: report.error(f"[PATH_PROJECT_TITLE_MISMATCH] {anchor}: {uid}")
            if linked_anchor!=uid.lower(): report.error(f"[PATH_PROJECT_ANCHOR_MISMATCH] {anchor}: {uid}")
    overlap_stats={}
    msv_slugs=[slug for slug,_title in EXPECTED_PATHS if slug in MSV_PATH_SLUGS and slug in own_units]
    for index,left in enumerate(msv_slugs):
        for right in msv_slugs[index+1:]:
            denominator=min(len(own_units[left]),len(own_units[right])) or 1
            ratio=len(own_units[left]&own_units[right])/denominator
            overlap_stats[f"{left}::{right}"]=round(ratio,4)
            if ratio>0.90:
                left_map=metas[left].get("overlap_justifications",{})
                right_map=metas[right].get("overlap_justifications",{})
                left_reason=left_map.get(right) if isinstance(left_map,dict) else None
                right_reason=right_map.get(left) if isinstance(right_map,dict) else None
                if not ((isinstance(left_reason,str) and len(left_reason)>=80) or (isinstance(right_reason,str) and len(right_reason)>=80)):
                    report.error(f"[PATH_OVERLAP_UNJUSTIFIED] {left} and {right} overlap {ratio:.1%}")
    report.statistics["learning_path_overlap_ratios"]=overlap_stats
    report.statistics["learning_paths"]=len(sections)
    report.statistics["learning_path_topic_links"]=all_links
    report.statistics["learning_path_project_callouts"]=all_projects
    report.mark("learning_paths", not any("PATH_" in e for e in report.errors))

def validate_python_references(report: Report) -> None:
    text=(report.root/"PYTHON_REFERENCES.md").read_text(encoding="utf-8")
    ids=set(PYTHON_ID_RE.findall(text))
    unknown=ids-APPROVED_PYTHON_IDS
    if unknown: report.error(f"[PYTHON_REFERENCE_UNKNOWN] {sorted(unknown)}")
    for uid in ids:
        expected=f"https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#{uid.lower()}"
        if expected not in text: report.error(f"[PYTHON_REFERENCE_LINK_MISMATCH] {uid}")
    if re.search(r'(?<!PY-)(?<![A-Z])(?:FND|TST|CON|SEC|MPR|MOD|ERR|FIT|TYP|IOP)-\d{3}',text):
        report.error("[SHORTENED_PYTHON_ID] Shortened Python Mastery ID found")
    report.statistics["python_mastery_references"]=len(ids)
    report.mark("python_references", not any("PYTHON_REFERENCE" in e or "SHORTENED_PYTHON" in e for e in report.errors))

def validate_solid_references(report: Report) -> None:
    path=report.root/"SOLID_DESIGN_REFERENCES.md"
    if not path.is_file():
        report.error("[SOLID_REFERENCE_FILE_MISSING]"); return
    text=path.read_text(encoding="utf-8")
    ids=set(SDP_ID_RE.findall(text))
    unknown=ids-set(EXPECTED_SOLID_REFERENCES)
    missing=set(EXPECTED_SOLID_REFERENCES)-ids
    if unknown: report.error(f"[SOLID_REFERENCE_UNKNOWN] {sorted(unknown)}")
    if missing: report.error(f"[SOLID_REFERENCE_MISSING] {sorted(missing)}")
    for uid,title in EXPECTED_SOLID_REFERENCES.items():
        if uid in ids and f"`{uid}` — **{title}**" not in text:
            report.error(f"[SOLID_REFERENCE_TITLE_MISMATCH] {uid}")
    if "not assumed to be published on GitHub `main`" not in text:
        report.error("[SOLID_REFERENCE_PUBLICATION_STATUS_MISSING]")
    if re.search(r'https://github\.com/rahulyadev/solid-and-design-pattern/blob/main/CURRICULUM\.md#',text):
        report.error("[SOLID_REFERENCE_INVENTED_REMOTE_LINK]")
    report.statistics["solid_design_references"]=len(ids)
    report.mark("solid_design_references",not any("SOLID_REFERENCE" in e for e in report.errors))

def validate_msv_extension(report: Report, rows: list[Unit], units: dict[str,Unit], projects: dict[str,str]) -> None:
    combined="\n".join((report.root/name).read_text(encoding="utf-8",errors="replace").lower() for name in (
        "CURRICULUM.md","PROJECTS.md","LEARNING_PATHS.md","API_DESIGN_PLAYBOOK.md",
        "INTERVIEW_PLAYBOOK.md","docs/TOOLCHAIN_AND_INFRASTRUCTURE.md","docs/SOURCE_AND_VERSION_POLICY.md",
        "templates/unit.md","templates/practice.md","templates/experiment.md","templates/review.md","templates/project.md",
    ))
    for uid,markers in MSV_REQUIRED_MARKERS.items():
        unit=units.get(uid)
        if not unit:
            report.error(f"[MSV_REQUIRED_UNIT_MISSING] {uid}"); continue
        searchable=f"{unit.title} {unit.outcome}".lower()
        missing=[marker for marker in markers if marker not in searchable]
        if missing: report.error(f"[MSV_REQUIRED_CONCEPT_MISSING] {uid}: {missing}")
    curriculum=(report.root/"CURRICULUM.md").read_text(encoding="utf-8").lower()
    if "publisher confirms are not consumer acknowledgements" not in curriculum:
        report.error("[MSV_CONFIRM_ACK_CONFLATION] Publisher confirms and consumer acknowledgements are not explicitly distinguished")
    if "manual acknowledgements" not in curriculum:
        report.error("[MSV_MANUAL_ACK_MISSING]")
    retry_unit=units.get("FAPI-MSV-090")
    retry_text=f"{retry_unit.title} {retry_unit.outcome}".lower() if retry_unit else ""
    if "bounded" not in retry_text or "dead-letter" not in retry_text:
        report.error("[MSV_RETRY_DLQ_MISSING]")
    outbox_unit=units.get("FAPI-MSV-120")
    outbox_text=f"{outbox_unit.title} {outbox_unit.outcome}".lower() if outbox_unit else ""
    if "outbox" not in outbox_text or "inbox" not in outbox_text:
        report.error("[MSV_OUTBOX_INBOX_MISSING]")
    if "exactly-once claims must be qualified" not in combined and "qualify exactly-once claims" not in combined:
        report.error("[MSV_EXACTLY_ONCE_UNQUALIFIED]")
    if "exactly once is guaranteed everywhere" in combined:
        report.error("[MSV_EXACTLY_ONCE_UNQUALIFIED]")
    ownership_text=" ".join(f"{units[uid].title} {units[uid].outcome}" for uid in ("FAPI-MSV-010","FAPI-MSV-200") if uid in units).lower()
    if "data ownership" not in ownership_text:
        report.error("[MSV_DATA_OWNERSHIP_MISSING]")
    grpc_execution=f"{units.get('FAPI-MSV-160').title} {units.get('FAPI-MSV-160').outcome}".lower() if units.get("FAPI-MSV-160") else ""
    if "deadline" not in grpc_execution: report.error("[MSV_GRPC_DEADLINE_MISSING]")
    if "cancellation" not in grpc_execution: report.error("[MSV_GRPC_CANCELLATION_MISSING]")
    for phrase,code in (
        ("circuit breaker","[MSV_RESILIENCE_MISSING]"),
        ("trace context","[MSV_OBSERVABILITY_MISSING]"),
        ("workload identity","[MSV_SECURITY_MISSING]"),
        ("sde-2 expectation","[MSV_SENIORITY_EXPECTATION_MISSING]"),
        ("sde-3 expectation","[MSV_SENIORITY_EXPECTATION_MISSING]"),
    ):
        if phrase not in combined: report.error(code+f" {phrase}")
    for project_id in ("FAPI-PRJ-090","FAPI-PRJ-100"):
        if project_id not in projects: report.error(f"[MSV_PROJECT_MISSING] {project_id}")
        section=(report.root/"PROJECTS.md").read_text(encoding="utf-8").lower().split(project_id.lower().replace("fapi-","fapi-"),1)
    project_text=(report.root/"PROJECTS.md").read_text(encoding="utf-8").lower()
    for project_id in ("fapi-prj-090","fapi-prj-100"):
        anchor=f'<a id="{project_id}"></a>'
        if anchor not in project_text: continue
        section=project_text.split(anchor,1)[1].split('<a id="fapi-prj-',1)[0]
        for phrase in ("failure injection","incident","observability","security"):
            if phrase not in section: report.error(f"[MSV_PROJECT_FAILURE_EVIDENCE_MISSING] {project_id.upper()}: {phrase}")
    for template_name,phrases in {
        "templates/unit.md":("system and data boundary","failure flow","sde-2 expectation","sde-3 expectation","recall from solid and design patterns"),
        "templates/practice.md":("fail deliberately","repair","operate"),
        "templates/experiment.md":("delivery count","trace ids","queue delay"),
        "templates/review.md":("runbook action","sde-2 answer","sde-3"),
        "templates/project.md":("service/data ownership","failure injection","incident walkthrough"),
    }.items():
        content=(report.root/template_name).read_text(encoding="utf-8").lower()
        for phrase in phrases:
            if phrase not in content: report.error(f"[MSV_TEMPLATE_CONTRACT_MISSING] {template_name}: {phrase}")
    report.mark("microservices_extension",not any("MSV_" in e for e in report.errors))

def github_heading_anchor(heading: str) -> str:
    value=re.sub(r'[*_`~]','',heading.strip()).lower()
    value=re.sub(r'[^a-z0-9\s-]','',value)
    return re.sub(r'-+','-',re.sub(r'\s+','-',value)).strip('-')

def extract_anchors(text: str) -> set[str]:
    anchors=set(re.findall(r'<a id="([^"]+)"></a>',text))
    counts=Counter()
    for line in text.splitlines():
        match=re.match(r'^(#{1,6})\s+(.+?)\s*$',line)
        if not match: continue
        base=github_heading_anchor(match.group(2)); count=counts[base]; counts[base]+=1
        anchors.add(base if count==0 else f"{base}-{count}")
    return anchors

def validate_markdown(report: Report) -> None:
    files=[p for p in iter_repo_files(report.root,report.profile) if p.suffix.lower()==".md"]
    table_count=0; link_count=0; fence_lines=0
    anchors_cache={path:extract_anchors(path.read_text(encoding="utf-8")) for path in files}
    for path in files:
        text=path.read_text(encoding="utf-8")
        fence_lines+=sum(1 for line in text.splitlines() if re.match(r'^\s*(```|~~~)',line))
        stack=[]
        for lineno,line in enumerate(text.splitlines(),1):
            fm=re.match(r'^\s*(```+|~~~+)',line)
            if fm:
                token=fm.group(1)[0]
                if stack and stack[-1]==token: stack.pop()
                else: stack.append(token)
        if stack: report.error(f"[MARKDOWN_FENCE_UNBALANCED] {path.relative_to(report.root)}")
        lines=text.splitlines(); i=0
        while i<len(lines):
            if lines[i].strip().startswith("|") and i+1<len(lines) and re.match(r'^\s*\|?\s*:?-{3,}',lines[i+1]):
                header=split_table_row(lines[i]); sep=split_table_row(lines[i+1]); table_count+=1
                if not header or len(header)!=len(sep): report.error(f"[MARKDOWN_TABLE_COLUMNS] {path.relative_to(report.root)}:{i+1}")
                j=i+2
                while j<len(lines) and lines[j].strip().startswith("|"):
                    row=split_table_row(lines[j])
                    if len(row)!=len(header): report.error(f"[MARKDOWN_TABLE_COLUMNS] {path.relative_to(report.root)}:{j+1}: expected {len(header)}, got {len(row)}")
                    j+=1
                i=j; continue
            i+=1
        for match in re.finditer(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',text):
            target=match.group(1).strip(); link_count+=1
            if not target or target.startswith(("http://","https://","mailto:","{{")): continue
            if " " in target and not target.startswith("<"): target=target.split(" ",1)[0]
            target=target.strip("<>")
            file_part,sep,anchor=target.partition("#")
            destination=path if not file_part else (path.parent/unquote(file_part)).resolve()
            try: destination.relative_to(report.root.resolve())
            except ValueError:
                report.error(f"[MARKDOWN_LINK_OUTSIDE_ROOT] {path.relative_to(report.root)} -> {target}"); continue
            if not destination.exists(): report.error(f"[MARKDOWN_LINK_MISSING] {path.relative_to(report.root)} -> {target}"); continue
            if anchor and destination.suffix.lower()==".md":
                available=anchors_cache.get(destination)
                if available is None:
                    try: available=extract_anchors(destination.read_text(encoding="utf-8"))
                    except Exception: available=set()
                if anchor not in available: report.error(f"[MARKDOWN_ANCHOR_MISSING] {path.relative_to(report.root)} -> {target}")
    report.statistics["markdown_files"]=len(files)
    report.statistics["markdown_tables"]=table_count
    report.statistics["markdown_links"]=link_count
    report.statistics["code_fence_blocks"]=fence_lines//2
    report.mark("markdown", not any("MARKDOWN_" in e for e in report.errors))

def compose_service_section(compose: str, service: str) -> str:
    match=re.search(rf'(?ms)^  {re.escape(service)}:\n(.*?)(?=^  [A-Za-z0-9_-]+:\n|^volumes:\n|\Z)',compose)
    return match.group(1) if match else ""

def compose_port_bindings(compose: str) -> list[tuple[str,str]]:
    bindings=[]; service=None; in_ports=False
    for line in compose.splitlines():
        service_match=re.match(r'^  ([A-Za-z0-9_-]+):\s*$',line)
        if service_match:
            service=service_match.group(1); in_ports=False; continue
        if service is None:
            continue
        if re.match(r'^    ports:\s*$',line):
            in_ports=True; continue
        if in_ports:
            item=re.match(r'^      -\s*["\']?(.+?)["\']?\s*$',line)
            if item:
                bindings.append((service,item.group(1))); continue
            if line.strip() and not line.startswith('      '):
                in_ports=False
    return bindings

def validate_toml_tools_and_compose(report: Report, run_external: bool) -> None:
    try: pyproject=tomllib.loads((report.root/"pyproject.toml").read_text(encoding="utf-8"))
    except Exception as exc:
        report.error(f"[PYPROJECT_TOML_INVALID] {exc}"); pyproject={}
    try: lock=tomllib.loads((report.root/"uv.lock").read_text(encoding="utf-8"))
    except Exception as exc:
        report.error(f"[UV_LOCK_TOML_INVALID] {exc}"); lock={}
    groups=pyproject.get("dependency-groups",{}) if isinstance(pyproject,dict) else {}
    if not isinstance(groups,dict) or not REQUIRED_GROUPS.issubset(groups): report.error(f"[DEPENDENCY_GROUP_MISSING] Required groups: {sorted(REQUIRED_GROUPS)}")
    dev_names=set()
    for item in groups.get("dev",[]) if isinstance(groups,dict) else []:
        if isinstance(item,str): dev_names.add(re.split(r'[<>=!~\[; ]',item,maxsplit=1)[0].lower())
    missing_tools=REQUIRED_DEV_TOOLS-dev_names
    if missing_tools: report.error(f"[DEVELOPMENT_TOOL_MISSING] {sorted(missing_tools)}")
    packages=lock.get("package",[]) if isinstance(lock,dict) else []
    locked={item.get("name") for item in packages if isinstance(item,dict) and isinstance(item.get("name"),str)}
    expected_locked={"fastapi","starlette","pydantic","pydantic-settings","uvicorn","httpx","sqlalchemy","alembic","psycopg","pytest","pytest-cov","hypothesis","ruff","mypy","grpcio","grpcio-tools","protobuf","redis","opentelemetry-sdk","aio-pika","aiormq","pamqp","yarl","multidict","propcache"}
    missing_locked=expected_locked-locked
    if missing_locked: report.error(f"[UV_LOCK_PACKAGE_MISSING] {sorted(missing_locked)}")
    try:
        toolchain=json.loads((report.root/"data/toolchain.json").read_text(encoding="utf-8"))
        if toolchain.get("canonical_python")!=(report.root/".python-version").read_text().strip(): report.error("[TOOLCHAIN_PYTHON_MISMATCH] .python-version and toolchain differ")
        packages_meta=toolchain.get("packages",{})
        for key in ("fastapi","starlette","pydantic","pydantic-settings","sqlalchemy","alembic","psycopg","uvicorn","httpx","pytest","grpcio","protobuf","aio-pika","aiormq"):
            if key not in packages_meta: report.error(f"[TOOLCHAIN_PACKAGE_MISSING] {key}")
    except Exception as exc: report.error(f"[TOOLCHAIN_JSON_INVALID] {exc}")
    compose=(report.root/"compose.yaml").read_text(encoding="utf-8")
    profiles=set(re.findall(r'profiles:\s*\[\"([^\"]+)\"\]',compose))
    if profiles!={"postgres","rabbitmq","redis","mail-testing","observability"}: report.error(f"[COMPOSE_PROFILE_MISMATCH] {sorted(profiles)}")
    if 'rabbitmq:' not in compose or 'rabbitmq:4.3.5-management' not in compose or 'rabbitmq-diagnostics' not in compose or 'fastapi_rabbitmq_data' not in compose:
        report.error('[RABBITMQ_COMPOSE_CONTRACT_MISSING]')
    env_text=(report.root/'.env.example').read_text(encoding='utf-8')
    for name in ('RABBITMQ_AMQP_PORT','RABBITMQ_MANAGEMENT_PORT','RABBITMQ_VHOST','RABBITMQ_USER','RABBITMQ_PASSWORD'):
        if name not in env_text or name not in compose: report.error(f'[RABBITMQ_ENV_PARITY_MISSING] {name}')
    if 'RABBITMQ_LEARNING_QUEUE' not in env_text: report.error('[RABBITMQ_ENV_PARITY_MISSING] RABBITMQ_LEARNING_QUEUE')
    rabbit_names=set()
    for item in groups.get('rabbitmq',[]) if isinstance(groups,dict) else []:
        if isinstance(item,str): rabbit_names.add(re.split(r'[<>=!~\[; ]',item,maxsplit=1)[0].lower())
    if 'aio-pika' not in rabbit_names: report.error('[RABBITMQ_DEPENDENCY_GROUP_MISSING] aio-pika')
    for service,binding in compose_port_bindings(compose):
        if not binding.startswith("127.0.0.1:"):
            report.error(f"[COMPOSE_PORT_NOT_LOOPBACK] {service}: {binding}")
            if service=="rabbitmq": report.error(f"[RABBITMQ_PORT_NOT_LOOPBACK] {binding}")
    rabbit_section=compose_service_section(compose,"rabbitmq")
    if not rabbit_section or "healthcheck:" not in rabbit_section or "rabbitmq-diagnostics" not in rabbit_section or '"ping"' not in rabbit_section:
        report.error("[RABBITMQ_HEALTHCHECK_MISSING] rabbitmq must use rabbitmq-diagnostics -q ping")
    if "fastapi_rabbitmq_data:/var/lib/rabbitmq" not in rabbit_section or not re.search(r'(?m)^  fastapi_rabbitmq_data:\s*$',compose):
        report.error("[RABBITMQ_NAMED_VOLUME_MISSING] fastapi_rabbitmq_data")
    validator_source=(report.root/"scripts/validate_repo.py").read_text(encoding="utf-8")
    try:
        fixture_source=validator_source.split("script=r'''",1)[1].split("'''\n        fixture=subprocess.run",1)[0]
    except IndexError:
        fixture_source=""
    bad_transient=[]
    for declaration in re.findall(r'declare_queue\((.*?)\)',fixture_source,re.S):
        if "durable=False" not in declaration:
            continue
        first_argument=declaration.strip().split(",",1)[0].strip()
        if first_argument not in {'""',"''"} or "exclusive=True" not in declaration:
            bad_transient.append(declaration.strip())
    if not fixture_source or bad_transient or fixture_source.count('declare_queue("", durable=False, exclusive=True, auto_delete=True')<2:
        report.error("[RABBITMQ43_TRANSIENT_QUEUE_INCOMPATIBLE] transient queues must be server-named and exclusive, or durable with explicit cleanup")
    report.statistics["development_dependencies"]=len(dev_names)
    report.statistics["dependency_groups"]=len(groups) if isinstance(groups,dict) else 0
    report.statistics["locked_packages"]=len(locked)
    report.statistics["compose_profiles"]=len(profiles)
    if run_external:
        uv=shutil.which("uv")
        pinned=(report.root/".python-version").read_text().strip()
        if not uv:
            message="uv lock --check skipped: uv executable unavailable"
            report.skipped_external_checks.append(message); report.checks["uv_lock_check_pinned"]="skipped"
        elif shutil.which(f"python{'.'.join(pinned.split('.')[:2])}") is None and not Path.home().joinpath('.local/share/uv/python').exists():
            message=f"`uv lock --check --python {pinned}` skipped: pinned interpreter is unavailable and implicit download is disabled"
            report.skipped_external_checks.append(message); report.checks["uv_lock_check_pinned"]="skipped"
        else:
            env=os.environ.copy(); env["UV_NO_MANAGED_PYTHON"]="1"
            proc=subprocess.run([uv,"lock","--check","--python",pinned],cwd=report.root,text=True,capture_output=True,env=env)
            if proc.returncode==0: report.mark("uv_lock_check_pinned",True)
            else:
                report.skipped_external_checks.append(f"Pinned uv lock check did not complete: {(proc.stderr or proc.stdout).strip()}")
                report.checks["uv_lock_check_pinned"]="skipped"
        substituted_command=[uv,"lock","--check","--offline","--python",sys.executable]
        substituted=subprocess.run(substituted_command,cwd=report.root,text=True,capture_output=True)
        if substituted.returncode==0:
            report.mark("uv_lock_check_substituted",True)
        else:
            report.skipped_external_checks.append(
                "Substituted lock check skipped/failed: `uv lock --check --offline --python "
                f"{sys.executable}` returned {substituted.returncode}: "
                f"{(substituted.stderr or substituted.stdout).strip()}"
            )
            report.checks["uv_lock_check_substituted"]="skipped"
        report.statistics["uv_lock_substituted_command"]=(
            f"uv lock --check --offline --python {sys.executable}"
        )
    report.mark("toml_and_tooling", not any(prefix in "\n".join(report.errors) for prefix in ("PYPROJECT_","UV_LOCK_","DEPENDENCY_","DEVELOPMENT_","TOOLCHAIN_","COMPOSE_","RABBITMQ_")))

def validate_optional_docker_and_rabbitmq(report: Report, run_external: bool) -> None:
    if not run_external:
        return
    docker=shutil.which("docker")
    if not docker:
        reason="docker executable is unavailable in the packaging environment"
        report.checks["docker_compose_config"]="skipped"
        report.checks["rabbitmq_integration"]="skipped"
        report.skipped_external_checks.append(f"docker compose config skipped: {reason}")
        report.skipped_external_checks.append(f"RabbitMQ integration fixture skipped: {reason}")
        return
    config=subprocess.run([docker,"compose","config"],cwd=report.root,text=True,capture_output=True)
    if config.returncode!=0:
        report.error(f"[DOCKER_COMPOSE_CONFIG_FAILED] {(config.stderr or config.stdout).strip()}")
        report.mark("docker_compose_config",False)
        report.checks["rabbitmq_integration"]="skipped"
        report.skipped_external_checks.append("RabbitMQ integration fixture skipped because docker compose config failed")
        return
    report.mark("docker_compose_config",True)
    if importlib.util.find_spec("aio_pika") is None:
        reason="aio-pika from the rabbitmq dependency group is unavailable in the active environment; run `uv sync --group dev --group rabbitmq`"
        report.checks["rabbitmq_integration"]="skipped"
        report.skipped_external_checks.append(f"RabbitMQ integration fixture skipped: {reason}")
        return
    project=f"fastapi-mastery-validator-{os.getpid()}"
    env=os.environ.copy()
    env.update({
        "RABBITMQ_AMQP_PORT":"5678", "RABBITMQ_MANAGEMENT_PORT":"15678",
        "RABBITMQ_VHOST":"fastapi_mastery_validator", "RABBITMQ_USER":"validator",
        "RABBITMQ_PASSWORD":"local_validator_only", "RABBITMQ_LEARNING_QUEUE":"fapi.validator.main",
    })
    compose=[docker,"compose","-p",project,"--profile","rabbitmq"]
    try:
        up=subprocess.run(compose+["up","-d","rabbitmq"],cwd=report.root,text=True,capture_output=True,env=env,timeout=120)
        if up.returncode!=0:
            report.error(f"[RABBITMQ_INTEGRATION_START_FAILED] {(up.stderr or up.stdout).strip()}")
            report.mark("rabbitmq_integration",False); return
        healthy=False
        for _ in range(30):
            ping=subprocess.run(compose+["exec","-T","rabbitmq","rabbitmq-diagnostics","-q","ping"],cwd=report.root,text=True,capture_output=True,env=env,timeout=15)
            if ping.returncode==0:
                healthy=True; break
            import time; time.sleep(2)
        if not healthy:
            report.error("[RABBITMQ_INTEGRATION_HEALTH_FAILED] broker did not become healthy")
            report.mark("rabbitmq_integration",False); return
        inspection_commands=[
            ["exec","-T","rabbitmq","rabbitmqctl","list_connections","name","user","peer_host","state","channels"],
            ["exec","-T","rabbitmq","rabbitmqctl","list_channels","number","user","vhost","confirm","consumer_count","messages_unacknowledged","messages_unconfirmed","prefetch_count"],
            ["exec","-T","rabbitmq","sh","-lc",'rabbitmqctl list_exchanges -p "$RABBITMQ_DEFAULT_VHOST" name type durable auto_delete internal'],
            ["exec","-T","rabbitmq","sh","-lc",'rabbitmqctl list_queues -p "$RABBITMQ_DEFAULT_VHOST" name type durable messages_ready messages_unacknowledged consumers consumer_utilisation'],
            ["exec","-T","rabbitmq","sh","-lc",'rabbitmqctl list_bindings -p "$RABBITMQ_DEFAULT_VHOST" source_name source_kind destination_name destination_kind routing_key'],
            ["exec","-T","rabbitmq","sh","-lc",'rabbitmqctl list_consumers -p "$RABBITMQ_DEFAULT_VHOST"'],
        ]
        for command in inspection_commands:
            inspected=subprocess.run(compose+command,cwd=report.root,text=True,capture_output=True,env=env,timeout=30)
            if inspected.returncode!=0:
                report.error(f"[RABBITMQ_INSPECTION_COMMAND_FAILED] {' '.join(command)}: {(inspected.stderr or inspected.stdout).strip()}")
                report.mark("rabbitmq_inspection_commands",False); return
        report.mark("rabbitmq_inspection_commands",True)
        script=r'''import asyncio, json, os, uuid
import aio_pika
from aio_pika import DeliveryMode, ExchangeType, Message
from aio_pika.exceptions import DeliveryError

async def main():
    url=f"amqp://{os.environ['RABBITMQ_USER']}:{os.environ['RABBITMQ_PASSWORD']}@127.0.0.1:{os.environ['RABBITMQ_AMQP_PORT']}/{os.environ['RABBITMQ_VHOST']}"
    connection=await aio_pika.connect_robust(url, timeout=10)
    channel=await connection.channel(publisher_confirms=True, on_return_raises=True)
    await channel.set_qos(prefetch_count=1)
    run_id=uuid.uuid4().hex
    exchange_name=f"fapi.validator.{run_id}"
    dlx_name=f"{exchange_name}.dlx"
    exchange=await channel.declare_exchange(exchange_name, ExchangeType.DIRECT, durable=False, auto_delete=True)
    dlx=await channel.declare_exchange(dlx_name, ExchangeType.DIRECT, durable=False, auto_delete=True)
    queue=await channel.declare_queue("", durable=False, exclusive=True, auto_delete=True, arguments={"x-dead-letter-exchange":dlx_name,"x-dead-letter-routing-key":"failed"})
    dlq=await channel.declare_queue("", durable=False, exclusive=True, auto_delete=True)
    await queue.bind(exchange, routing_key="ok")
    await dlq.bind(dlx, routing_key="failed")
    event_id=str(uuid.uuid4())
    confirmed=await exchange.publish(Message(json.dumps({"event_id":event_id}).encode(),delivery_mode=DeliveryMode.PERSISTENT,message_id=event_id),routing_key="ok",mandatory=True,timeout=10)
    unroutable=False
    try:
        await exchange.publish(Message(b"unroutable"),routing_key="missing",mandatory=True,timeout=10)
    except DeliveryError:
        unroutable=True
    message=await queue.get(timeout=10, fail=True)
    await message.ack()
    await exchange.publish(Message(b"dead-letter-me"),routing_key="ok",mandatory=True,timeout=10)
    poison=await queue.get(timeout=10,fail=True)
    await poison.reject(requeue=False)
    parked=await dlq.get(timeout=10,fail=True)
    await parked.ack()
    seen=set(); applied=0
    for _ in range(2):
        await exchange.publish(Message(json.dumps({"event_id":event_id}).encode(),message_id=event_id),routing_key="ok",mandatory=True,timeout=10)
    for _ in range(2):
        duplicate=await queue.get(timeout=10,fail=True)
        key=duplicate.message_id
        if key not in seen:
            seen.add(key); applied+=1
        await duplicate.ack()
    print(json.dumps({"healthy":True,"publisher_confirm":bool(confirmed),"unroutable_detected":unroutable,"manual_ack":True,"dead_lettered":True,"idempotent_applied_count":applied},sort_keys=True))
    await connection.close()

asyncio.run(main())
'''
        fixture=subprocess.run([sys.executable,"-c",script],cwd=report.root,text=True,capture_output=True,env=env,timeout=90)
        if fixture.returncode!=0:
            report.error(f"[RABBITMQ_INTEGRATION_FAILED] {(fixture.stderr or fixture.stdout).strip()}")
            report.mark("rabbitmq_integration",False); return
        try: observed=json.loads(fixture.stdout.strip().splitlines()[-1])
        except Exception as exc:
            report.error(f"[RABBITMQ_INTEGRATION_OUTPUT_INVALID] {exc}: {fixture.stdout!r}")
            report.mark("rabbitmq_integration",False); return
        expected={"healthy":True,"publisher_confirm":True,"unroutable_detected":True,"manual_ack":True,"dead_lettered":True,"idempotent_applied_count":1}
        if observed!=expected:
            report.error(f"[RABBITMQ_INTEGRATION_ASSERTION_FAILED] expected {expected}, observed {observed}")
            report.mark("rabbitmq_integration",False); return
        report.mark("rabbitmq_integration",True)
    except subprocess.TimeoutExpired as exc:
        report.error(f"[RABBITMQ_INTEGRATION_TIMEOUT] {exc}")
        report.mark("rabbitmq_integration",False)
    finally:
        subprocess.run(compose+["stop","rabbitmq"],cwd=report.root,text=True,capture_output=True,env=env,timeout=120)
        subprocess.run(compose+["rm","-f","rabbitmq"],cwd=report.root,text=True,capture_output=True,env=env,timeout=120)
        volume=f"{project}_fastapi_rabbitmq_data"
        inspected=subprocess.run([docker,"volume","inspect","--format",'{{ index .Labels "com.docker.compose.project" }} {{ index .Labels "com.docker.compose.volume" }}',volume],cwd=report.root,text=True,capture_output=True,timeout=30)
        if inspected.returncode==0 and inspected.stdout.strip()==f"{project} fastapi_rabbitmq_data":
            subprocess.run([docker,"volume","rm",volume],cwd=report.root,text=True,capture_output=True,timeout=60)

def slugify(value: str) -> str:
    value=value.lower().replace("pydantic v1-to-v2","pydantic-v1-to-v2")
    value=re.sub(r'[^a-z0-9]+','-',value).strip('-')
    return re.sub(r'-+','-',value)

def unit_directory(root: Path, unit: Unit) -> Path:
    code=unit.unit_id.split("-")[1]
    return root/"units"/DOMAIN_SLUGS[code]/f"{unit.unit_id}-{slugify(unit.title)}"

def extract_section(text: str, heading: str) -> str:
    start=text.find(heading)
    if start<0: return ""
    tail=text[start+len(heading):]
    match=re.search(r'\n##\s+',tail)
    return tail[:match.start()] if match else tail

def validate_python_file(report: Report, path: Path) -> None:
    try: ast.parse(path.read_text(encoding="utf-8"),filename=str(path))
    except Exception as exc: report.error(f"[UNIT_PYTHON_SYNTAX] {path.relative_to(report.root)}: {exc}")

def substantive(text: str, minimum: int=80) -> bool:
    clean=re.sub(r'[`#*|>\-\[\]()]',' ',text)
    return len(re.findall(r'[A-Za-z0-9_]+',clean))>=minimum

def validate_unit_pack(report: Report, unit: Unit, entry: ProgressEntry, directory: Path) -> None:
    readme=directory/"README.md"; practice=directory/"practice"/"README.md"; review=directory/"REVIEW.md"
    if not readme.is_file(): report.error(f"[UNIT_MISSING_README] {unit.unit_id}"); return
    text=readme.read_text(encoding="utf-8")
    if not text.startswith(f"# {unit.unit_id} — {unit.title}"):
        report.error(f"[UNIT_TITLE_MISMATCH] {unit.unit_id}")
    for heading in UNIT_README_HEADINGS:
        if heading not in text: report.error(f"[UNIT_README_SECTION_MISSING] {unit.unit_id}: {heading}")
    notebook=extract_section(text,"## Physical Notebook Core")
    if not substantive(notebook,100): report.error(f"[UNIT_NOTEBOOK_CORE_SHALLOW] {unit.unit_id}")
    for phrase in ("How to read this visual","Key insight","Simplification or limitation"):
        if phrase not in notebook and phrase not in text: report.error(f"[UNIT_VISUAL_CONTRACT_MISSING] {unit.unit_id}: {phrase}")
    interview=extract_section(text,"## 13. Interview questions, traps, and follow-ups")
    for keyword in ("definition","trace","failure","alternative","performance","security","testing","changed"):
        if keyword not in interview.lower(): report.error(f"[UNIT_INTERVIEW_COVERAGE_MISSING] {unit.unit_id}: {keyword}")
    if PLACEHOLDER_RE.search(text): report.error(f"[UNIT_TEMPLATE_PLACEHOLDER] {unit.unit_id}: README.md")
    if any(marker in text.lower() for marker in PREMATURE_SOLUTION_MARKERS): report.error(f"[UNIT_PREMATURE_SOLUTION] {unit.unit_id}: README.md")
    if not practice.is_file(): report.error(f"[UNIT_MISSING_PRACTICE] {unit.unit_id}")
    else:
        ptext=practice.read_text(encoding="utf-8")
        if "## Concrete unsolved tasks" not in ptext or ptext.count("### Task")<2 or not substantive(ptext,120):
            report.error(f"[UNIT_PRACTICE_TASK_SHALLOW] {unit.unit_id}")
        for phrase in ("Expected behavior","Acceptance criteria","Progressive hints","Reflection questions"):
            if phrase.lower() not in ptext.lower(): report.error(f"[UNIT_PRACTICE_SECTION_MISSING] {unit.unit_id}: {phrase}")
        if PLACEHOLDER_RE.search(ptext): report.error(f"[UNIT_TEMPLATE_PLACEHOLDER] {unit.unit_id}: practice/README.md")
        if any(marker in ptext.lower() for marker in PREMATURE_SOLUTION_MARKERS): report.error(f"[UNIT_PREMATURE_SOLUTION] {unit.unit_id}: practice/README.md")
    if not review.is_file(): report.error(f"[UNIT_MISSING_REVIEW] {unit.unit_id}")
    else:
        rtext=review.read_text(encoding="utf-8")
        for heading in REVIEW_HEADINGS:
            if heading not in rtext: report.error(f"[UNIT_REVIEW_SECTION_MISSING] {unit.unit_id}: {heading}")
        if PLACEHOLDER_RE.search(rtext): report.error(f"[UNIT_TEMPLATE_PLACEHOLDER] {unit.unit_id}: REVIEW.md")
    if unit.priority in {"C","P"}:
        example_dir=directory/"examples"
        expected=[example_dir/name for name in ("01_minimal.py","02_traced.py","03_realistic.py","04_failure_case.py")]
        missing=[p.name for p in expected if not p.is_file()]
        if missing: report.error(f"[UNIT_EXAMPLES_MISSING] {unit.unit_id}: {missing}")
        practice_dir=directory/"practice"
        runnable=[]
        if practice_dir.exists():
            runnable.extend(path for path in practice_dir.rglob("*.py") if path.name in {"micro_lab.py","trace_lab.py","lab.py"})
            app_dir=practice_dir/"app"
            if app_dir.is_dir() and any(app_dir.rglob("*.py")):
                runnable.append(app_dir)
        if not runnable and "justified non-code alternative" not in (practice.read_text(encoding="utf-8").lower() if practice.is_file() else ""):
            report.error(f"[UNIT_MISSING_MICRO_LAB] {unit.unit_id}")
    if "I" in unit.evidence:
        for name in ("test_examples.py","test_challenge.py"):
            if not (directory/"practice"/name).is_file(): report.error(f"[UNIT_TEST_FILE_MISSING] {unit.unit_id}: {name}")
    if "X" in unit.evidence:
        experiments=directory/"experiments"
        if not experiments.exists() or not any(path.name=="README.md" for path in experiments.rglob("README.md")):
            report.error(f"[UNIT_MISSING_EXPERIMENT] {unit.unit_id}")
    for path in directory.rglob("*"):
        if not path.is_file() or any(part in WORKING_IGNORED_DIRECTORY_NAMES for part in path.parts): continue
        if path.suffix==".py": validate_python_file(report,path)
        if path.suffix in {".md",".py",".http",".toml",".yaml",".yml",".proto",".html",".js"}:
            try: content=path.read_text(encoding="utf-8")
            except UnicodeDecodeError: continue
            if PLACEHOLDER_RE.search(content): report.error(f"[UNIT_TEMPLATE_PLACEHOLDER] {unit.unit_id}: {path.relative_to(directory)}")
            if any(marker in content.lower() for marker in PREMATURE_SOLUTION_MARKERS): report.error(f"[UNIT_PREMATURE_SOLUTION] {unit.unit_id}: {path.relative_to(directory)}")

def validate_live(report: Report, units: dict[str,Unit], progress: dict[str,ProgressEntry], projects: dict[str,str]) -> None:
    units_root=report.root/"units"
    expected_dirs=set()
    for uid,entry in progress.items():
        if entry.artifact_state not in {"Draft","Approved"}: continue
        unit=units[uid]; directory=unit_directory(report.root,unit); expected_dirs.add(directory.resolve())
        if not directory.is_dir(): report.error(f"[UNIT_DIRECTORY_MISSING] {uid}: expected {directory.relative_to(report.root)}")
        else: validate_unit_pack(report,unit,entry,directory)
    if units_root.exists():
        for readme in units_root.glob("*/*/README.md"):
            directory=readme.parent.resolve()
            if directory not in expected_dirs: report.error(f"[UNIT_TRACKER_DIRECTORY_PARITY] Untracked initialized directory: {directory.relative_to(report.root)}")
    tracker={}
    for line in (report.root/"PROGRESS.md").read_text(encoding="utf-8").splitlines():
        cells=split_table_row(line)
        if len(cells)==7 and PROJECT_ID_RE.fullmatch(cells[0].strip("`")): tracker[cells[0].strip("`")]=cells[2]
    projects_root=report.root/"projects"
    for uid,state in tracker.items():
        if state in {"Active","Complete"}:
            candidates=list(projects_root.glob(f"{uid}-*/README.md")) if projects_root.exists() else []
            if len(candidates)!=1: report.error(f"[PROJECT_DIRECTORY_PARITY] {uid}: expected one project directory, found {len(candidates)}")
            elif PLACEHOLDER_RE.search(candidates[0].read_text(encoding="utf-8")): report.error(f"[PROJECT_TEMPLATE_PLACEHOLDER] {uid}")
    report.mark("live_content", not any(e.startswith("[UNIT_") or e.startswith("[PROJECT_DIRECTORY") for e in report.errors))

def validate_workflow(report: Report) -> None:
    text="\n".join((report.root/name).read_text(encoding="utf-8") for name in ("AGENTS.md","START_HERE.md","docs/WORKFLOW.md"))
    required=[
        "setup/fastapi-mastery-bootstrap", "topic/<UNIT-ID>", "project/<PROJECT-ID>",
        "git status --porcelain=v1 --untracked-files=all", "git worktree list --porcelain",
        "+refs/heads/main:refs/remotes/origin/main", "+refs/heads/topic/<UNIT-ID>:refs/remotes/origin/topic/<UNIT-ID>",
        "+refs/heads/project/<PROJECT-ID>:refs/remotes/origin/project/<PROJECT-ID>",
        "INIT_START", "no push required", "older local-only", "detached `HEAD`",
        "resume it even when", "another Worktree", "never create", "current-operation-only commit boundary",
        "collect", "challenge", "repair", "preserve", "do not execute",
    ]
    for phrase in required:
        if phrase.lower() not in text.lower(): report.error(f"[WORKFLOW_CONTRACT_MISSING] {phrase}")
    if "Initialize <UNIT-ID>." not in text or "Initialize project <PROJECT-ID>." not in text:
        report.error("[WORKFLOW_PROMPT_MISSING] Initialization prompt missing")
    report.mark("workflow_contract", not any("WORKFLOW_" in e for e in report.errors))

def validate_repository(root: Path, *, profile: str="auto", run_external: bool=True) -> Report:
    root=root.resolve(); resolved=resolve_profile(root,profile); report=Report(root, resolved)
    validate_hygiene(report)
    _rows,units=parse_units(report)
    validate_coverage(report,units)
    progress=parse_progress(report,units)
    projects=parse_projects(report,units)
    validate_readme_counts(report)
    validate_learning_paths(report,units,projects)
    validate_python_references(report)
    validate_solid_references(report)
    validate_reference_quality(report)
    validate_rabbitmq_operational_docs(report)
    validate_msv_extension(report,_rows,units,projects)
    validate_workflow(report)
    if resolved=="live": validate_live(report,units,progress,projects)
    validate_markdown(report)
    validate_toml_tools_and_compose(report,run_external)
    validate_optional_docker_and_rabbitmq(report,run_external)
    report.mark("overall_repository",not report.errors)
    return report

def validate_archive(base_report: Report, archive: Path, *, run_external: bool=False) -> None:
    archive=archive.resolve()
    info={"path":archive.name}
    if not archive.is_file(): base_report.error(f"[ARCHIVE_MISSING] {archive}"); base_report.archive=info; return
    info.update({"sha256":sha256_file(archive),"size_bytes":archive.stat().st_size})
    try:
        with zipfile.ZipFile(archive) as zf:
            names=zf.namelist(); info["entry_count"]=len(names); bad=zf.testzip(); info["corrupt_entry"]=bad
            if bad: base_report.error(f"[ARCHIVE_CORRUPT] {bad}")
            if any(name.startswith("/") or ".." in PurePosixPath(name).parts for name in names): base_report.error("[ARCHIVE_UNSAFE_PATH] Absolute or parent path")
            for name in names:
                parts=PurePosixPath(name).parts
                if ".git" in parts: base_report.error(f"[ARCHIVE_FORBIDDEN_GIT_METADATA] {name}")
                elif parts and parts[0] in ARCHIVE_FORBIDDEN_ROOTS: base_report.error(f"[ARCHIVE_FORBIDDEN_GENERATED_PATH] {name}")
                if archive_working_artifact(parts): base_report.error(f"[ARCHIVE_FORBIDDEN_WORKING_ARTIFACT] {name}")
                if any(part in WORKING_FORBIDDEN_COMPONENTS for part in parts) or is_sensitive_env(PurePosixPath(name)):
                    base_report.error(f"[ARCHIVE_FORBIDDEN_PRIVATE_PATH] {name}")
                if PurePosixPath(name).name in FORBIDDEN_LICENSE_NAMES: base_report.error(f"[ARCHIVE_FORBIDDEN_LICENSE] {name}")
            if not set(REQUIRED_FILES).issubset(names): base_report.error("[ARCHIVE_REQUIRED_FILES_MISSING]")
            if "README.md" not in names or "CURRICULUM.md" not in names: base_report.error("[ARCHIVE_WRAPPER_DIRECTORY]")
            with tempfile.TemporaryDirectory(prefix="fastapi-archive-") as temp:
                extracted=Path(temp); zf.extractall(extracted)
                fresh=validate_repository(extracted,profile="archive",run_external=run_external)
                info["extracted_validation"]="passed" if not fresh.errors else "failed"
                info["extracted_profile"]=fresh.profile
                info["extracted_errors"]=fresh.errors
                info["extracted_warnings"]=fresh.warnings
                if fresh.errors: base_report.errors.extend(f"Extracted archive: {error}" for error in fresh.errors)
    except zipfile.BadZipFile as exc: base_report.error(f"[ARCHIVE_INVALID_ZIP] {exc}")
    base_report.archive=info
    base_report.mark("archive_integrity",not any(error.startswith("[ARCHIVE_") or error.startswith("Extracted archive") for error in base_report.errors))

def extended_prerequisite_error(operation: str) -> str | None:
    if shutil.which("uv") is None:
        return f"[EXTENDED_TEST_PREREQUISITE_MISSING] {operation} requires uv. Run `uv sync --group dev`, then use `uv run --group dev python scripts/validate_repo.py ...`."
    if importlib.util.find_spec("pytest") is None:
        return f"[EXTENDED_TEST_PREREQUISITE_MISSING] {operation} requires pytest from the dev group. Run `uv sync --group dev`."
    return None

def compare_self_test_evidence(recorded: dict[str,object], fresh: dict[str,object]) -> list[str]:
    errors=[]
    for key in ("status","count","passed"):
        if recorded.get(key)!=fresh.get(key):
            errors.append(f"REPORT_SELF_TEST_SUMMARY_MISMATCH: {key}: recorded {recorded.get(key)!r}, fresh {fresh.get(key)!r}")
    recorded_cases={item.get("name"):item for item in recorded.get("cases",[]) if isinstance(item,dict) and isinstance(item.get("name"),str)}
    fresh_cases={item.get("name"):item for item in fresh.get("cases",[]) if isinstance(item,dict) and isinstance(item.get("name"),str)}
    if set(recorded_cases)!=set(fresh_cases):
        errors.append(f"REPORT_SELF_TEST_CASES_MISMATCH: recorded {sorted(recorded_cases)}, fresh {sorted(fresh_cases)}")
    else:
        for name in sorted(fresh_cases):
            for key in ("status","expected_error","observed_matching_error","observed_error_count"):
                if recorded_cases[name].get(key)!=fresh_cases[name].get(key):
                    errors.append(f"REPORT_SELF_TEST_CASE_EVIDENCE_MISMATCH: {name}: {key}: recorded {recorded_cases[name].get(key)!r}, fresh {fresh_cases[name].get(key)!r}")
    recorded_fixtures=recorded.get("fixtures") if isinstance(recorded.get("fixtures"),dict) else {}
    fresh_fixtures=fresh.get("fixtures") if isinstance(fresh.get("fixtures"),dict) else {}
    for key in ("status","count","passed"):
        if recorded_fixtures.get(key)!=fresh_fixtures.get(key):
            errors.append(f"REPORT_FIXTURE_SUMMARY_MISMATCH: {key}: recorded {recorded_fixtures.get(key)!r}, fresh {fresh_fixtures.get(key)!r}")
    recorded_fixture_cases={item.get("name"):item for item in recorded_fixtures.get("cases",[]) if isinstance(item,dict) and isinstance(item.get("name"),str)}
    fresh_fixture_cases={item.get("name"):item for item in fresh_fixtures.get("cases",[]) if isinstance(item,dict) and isinstance(item.get("name"),str)}
    if set(recorded_fixture_cases)!=set(fresh_fixture_cases):
        errors.append(f"REPORT_FIXTURE_CASES_MISMATCH: recorded {sorted(recorded_fixture_cases)}, fresh {sorted(fresh_fixture_cases)}")
    else:
        for name in sorted(fresh_fixture_cases):
            for key in ("status","detail"):
                if recorded_fixture_cases[name].get(key)!=fresh_fixture_cases[name].get(key):
                    errors.append(f"REPORT_FIXTURE_EVIDENCE_MISMATCH: {name}: {key}: recorded {recorded_fixture_cases[name].get(key)!r}, fresh {fresh_fixture_cases[name].get(key)!r}")
    return errors

def verify_report(report_path: Path, archive_path: Path, *, compare_self_tests: bool=True, allow_renamed: bool=False) -> dict[str,object]:
    errors=[]
    def fail(code: str,detail: str) -> None: errors.append(f"{code}: {detail}")
    if compare_self_tests:
        missing=extended_prerequisite_error("Full report verification")
        if missing:
            fail("REPORT_EXTENDED_TEST_PREREQUISITE_MISSING",missing)
            return {"schema_version":1,"status":"failed","errors":errors,"warnings":[]}
    if not report_path.is_file(): fail("REPORT_FILE_MISSING",str(report_path)); return {"schema_version":1,"status":"failed","errors":errors,"warnings":[]}
    if not archive_path.is_file(): fail("REPORT_ARCHIVE_MISSING",str(archive_path)); return {"schema_version":1,"status":"failed","errors":errors,"warnings":[]}
    try: saved=json.loads(report_path.read_text(encoding="utf-8"))
    except Exception as exc: fail("REPORT_JSON_PARSE_ERROR",str(exc)); return {"schema_version":1,"status":"failed","errors":errors,"warnings":[]}
    actual={"path":archive_path.name,"sha256":sha256_file(archive_path),"size_bytes":archive_path.stat().st_size}
    fresh=None; fresh_self=None
    try:
        with zipfile.ZipFile(archive_path) as zf:
            actual["entry_count"]=len(zf.namelist()); actual["corrupt_entry"]=zf.testzip()
            with tempfile.TemporaryDirectory(prefix="fastapi-report-") as temp:
                root=Path(temp); zf.extractall(root)
                fresh=validate_repository(root,profile="archive",run_external=False)
                if compare_self_tests: fresh_self=run_self_tests(root)
    except Exception as exc: fail("REPORT_ARCHIVE_INVALID",str(exc))
    recorded=saved.get("archive") if isinstance(saved,dict) else None
    if not isinstance(recorded,dict): fail("REPORT_ARCHIVE_METADATA_MISSING","archive object missing"); recorded={}
    if not allow_renamed and recorded.get("path")!=actual.get("path"): fail("REPORT_ARCHIVE_FILENAME_MISMATCH",f"recorded {recorded.get('path')}, actual {actual.get('path')}")
    for field,code in (("sha256","REPORT_ARCHIVE_SHA256_MISMATCH"),("size_bytes","REPORT_ARCHIVE_SIZE_MISMATCH"),("entry_count","REPORT_ARCHIVE_ENTRY_COUNT_MISMATCH")):
        if recorded.get(field)!=actual.get(field): fail(code,f"recorded {recorded.get(field)!r}, actual {actual.get(field)!r}")
    if saved.get("repository_root")!=".": fail("REPORT_ROOT_MISMATCH",repr(saved.get("repository_root")))
    manual=saved.get("validation_scope",{}).get("manual_inspection",{}) if isinstance(saved.get("validation_scope"),dict) else {}
    if manual.get("status")!="not_performed": fail("REPORT_MANUAL_SCOPE_MISMATCH",repr(manual))
    if fresh is not None:
        expected="passed" if not fresh.errors else "failed"
        if saved.get("status")!=expected: fail("REPORT_STATUS_MISMATCH",f"recorded {saved.get('status')}, fresh {expected}")
        saved_stats=saved.get("statistics",{})
        for key in IMPORTANT_REPORT_STATISTICS:
            if saved_stats.get(key)!=fresh.statistics.get(key): fail("REPORT_STATISTIC_MISMATCH",f"{key}: recorded {saved_stats.get(key)!r}, fresh {fresh.statistics.get(key)!r}")
        if saved.get("errors")!=fresh.errors: fail("REPORT_ERRORS_MISMATCH",f"recorded {saved.get('errors')!r}, fresh {fresh.errors!r}")
        if saved.get("warnings")!=fresh.warnings: fail("REPORT_WARNINGS_MISMATCH",f"recorded {saved.get('warnings')!r}, fresh {fresh.warnings!r}")
    if compare_self_tests:
        recorded_tests=saved.get("self_tests")
        if not isinstance(recorded_tests,dict): fail("REPORT_SELF_TESTS_MISSING","self_tests missing")
        elif fresh_self:
            errors.extend(compare_self_test_evidence(recorded_tests,fresh_self))
    return {
        "schema_version":1,"status":"passed" if not errors else "failed","report_path":report_path.name,
        "archive":actual,"filename_verification":"content_identity_only" if allow_renamed else "canonical_filename_and_content",
        "statistics_compared":list(IMPORTANT_REPORT_STATISTICS),"self_tests_compared":compare_self_tests,
        "errors":errors,"warnings":[],
    }

def copy_repo(root: Path) -> tempfile.TemporaryDirectory[str]:
    holder=tempfile.TemporaryDirectory(prefix="fastapi-validator-")
    target=Path(holder.name)
    for path in iter_repo_files(root,"bootstrap"):
        rel=path.relative_to(root)
        if rel.parts and rel.parts[0] in {"units","projects"}: continue
        destination=target/rel; destination.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(path,destination)
    return holder

def set_progress_state(root: Path, uid: str, state: str) -> None:
    path=root/"PROGRESS.md"; lines=[]
    for line in path.read_text(encoding="utf-8").splitlines():
        cells=split_table_row(line)
        if len(cells)==9 and cells[0].strip("`")==uid:
            cells[3]=state; line="| "+" | ".join(cells)+" |"
        lines.append(line)
    path.write_text("\n".join(lines)+"\n",encoding="utf-8")

def fixture_readme(unit: Unit) -> str:
    return f'''# {unit.unit_id} — {unit.title}

## Physical Notebook Core

### Problem or pressure
A minimal endpoint should expose one observable contract while keeping framework and application responsibilities distinguishable.

### One-sentence mental model
> FastAPI registers a Starlette route and uses typed declarations to extract, validate, call, and serialize.

### Essential visual

```text
client -> ASGI server -> router -> endpoint -> response validation -> client
```

#### How to read this visual
Follow the arrows once for a successful request and name the owner of each step.

#### Key insight
The route function is application code; serving, routing, validation, and serialization belong to distinct layers.

#### Simplification or limitation
This conceptual trace omits middleware, dependencies, and failure branches introduced in later units.

### Governing lifecycle rule or invariant
1. Route registration occurs before a request arrives.
2. A successful response must satisfy the declared public contract.

### Minimal code skeleton

```python
from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health() -> dict[str, str]:
    return {{"status": "ok"}}
```

### Common failure, comparison, and interview cues
- Failure: using the wrong import string prevents the server from locating the application.
- Compare with: a plain ASGI callable without FastAPI routing and validation.
- Recall: what happens at import time and what happens per request?

## 1. Learning outcomes and evidence
Explain route registration, type a minimal endpoint, trace one request, run scaffold checks, and answer changed-requirement questions.

## 2. Prerequisites and smallest bridge
The environment unit is the hard prerequisite. A bridge is knowing how to run one Python module in the selected uv environment.

## 3. Simple explanation and owning layer
FastAPI supplies declaration and integration mechanics; Starlette owns core routing; Uvicorn drives ASGI messages; the endpoint owns business behavior.

## 4. Runtime or request-lifecycle trace
At import time Python creates the application and registers the route. At request time the server emits ASGI messages, routing selects the endpoint, the endpoint returns data, and FastAPI serializes the response.

## 5. Detailed visual model

```text
import: Python -> FastAPI() -> decorator registers route
time:   t0        t1             t2
request: client -> Uvicorn -> Starlette route -> endpoint -> JSON response
```

### How to read this visual
Read the import line once, then read the request line for every call.

### Key insight
Import-time registration and request-time execution are different lifecycles.

### Simplification or limitation
Dependency resolution and middleware are intentionally excluded.

## 6. Worked examples

### 6.1 Minimal example
`examples/01_minimal.py` exposes `/health`.

### 6.2 Traced runtime example
`examples/02_traced.py` records import and call events without hiding the sequence.

### 6.3 Realistic backend example
`examples/03_realistic.py` returns a typed service-status representation.

### 6.4 Failure or debugging example
`examples/04_failure_case.py` contains a safe diagnostic for an incorrect module path.

### 6.5 Comparison with an alternative
A raw ASGI callable reveals the protocol but is less convenient for typed API work.

## 7. Formal mechanics and boundaries
Python executes decorators at import time. FastAPI stores route metadata through Starlette. Uvicorn is a server, not the application. Pydantic participates when typed validation or serialization requires it.

## 8. Failure modes and edge cases
Wrong module path, wrong object name, route collision, invalid return contract, and assuming reload is a production worker strategy.

## 9. Performance, resource, transaction, or security costs
This endpoint has no database transaction. Import side effects should remain bounded; response serialization and middleware still add measurable cost.

## 10. Production relevance and anti-signals
The one-file shape is appropriate while the service is small. Do not add layers before change pressure exists.

## 11. Testing and debugging strategy
Test the ASGI contract through HTTPX or TestClient, keep a tiny pure function where useful, and inspect OpenAPI separately from runtime responses.

## 12. Practice ladder
Use `practice/README.md`: predict registration, run the micro-lab, implement the missing status route, diagnose a route failure, and vary the response contract.

## 13. Interview questions, traps, and follow-ups
- Definition: what does FastAPI add above Starlette and Pydantic?
- Trace: explain import-time registration and request-time execution.
- Failure: why can a correct application still fail to start?
- Alternative: when is a raw ASGI callable or Starlette alone sufficient?
- Performance: what work occurs on every request?
- Security: what validation is not authorization?
- Testing: what observable contract should a route test prove?
- Changed requirement: how would you add a database resource without a global session?

## 14. Explanation exercises
Explain the application, server, and route as three separate objects. Then explain why returning a dictionary is not the same as sending bytes to the client.

## 15. Experiment decision
Not required for this unit; the micro-lab makes import-time and call-time behavior observable.

## 16. Python Mastery references
Review function calls, decorators, modules, typing, and testing only as needed.

## 17. Authoritative sources and version notes
Use current FastAPI first-steps, application, and testing documentation. Label Python 3.12+ syntax and show a Python 3.11-compatible form.

## 18. Open uncertainties
None after the package versions and server command are verified locally.
'''

def fixture_practice(unit: Unit) -> str:
    return f'''# Practice — {unit.unit_id} {unit.title}

## Learning question
Can you separate import-time route registration from request-time behavior and implement a typed endpoint without copying the worked example?

## Initial state
`starter.py` contains an application and a deliberately incomplete `/status` route. The micro-lab already demonstrates event ordering; examples are separate from the learner challenge.

## Concrete unsolved tasks

### Task 1 — Predict and trace
Before running the micro-lab, write the expected event order and identify which layer owns every event.

### Task 2 — Implement
Implement `/status` so it returns the documented typed contract. Preserve the route path and do not add global mutable state.

### Task 3 — Debug and vary
Diagnose a wrong import string, then change the route to include an optional detail field without breaking the original success contract.

## Expected behavior
A request to `/status` returns HTTP 200 with a valid status payload; invalid output is rejected by the response contract.

## Constraints
Keep the learner implementation in `starter.py`, use no database, and do not copy code from `examples/`.

## Acceptance criteria
- [ ] The predicted trace names import and request phases.
- [ ] Scaffold examples pass.
- [ ] Challenge tests are discoverable and remain unsolved until Rahul implements the route.
- [ ] The changed contract remains backward-compatible.

## Edge cases
Wrong object name, duplicate route, absent optional field, and output that violates the response model.

## Commands

```bash
uv run --group dev python -m compileall -q .
uv run --group dev python practice/micro_lab.py
uv run --group dev python -m pytest -q practice/test_examples.py
uv run --group dev python -m pytest --collect-only -q practice/test_challenge.py
```

## Troubleshooting
Confirm the current directory, import string, selected interpreter, and application object before changing code.

## Progressive hints
Hint 1 should identify the missing lifecycle assumption. Hint 2 may name the contract boundary. Reveal no implementation before a meaningful attempt.

## Reflection questions
Why does route registration happen at import time? Which failure would occur before the endpoint body runs? What changes if the endpoint becomes async?

## Attempt and review record
Preserve Rahul's code, predictions, observed output, failed tests, and reasoning. Do not add a complete solution until the challenge is explicitly closed.
'''

def fixture_review(unit: Unit) -> str:
    return f'''# Review — {unit.unit_id} {unit.title}

## Closed-book reconstruction
Recreate the Physical Notebook Core, the import/request split, and the minimal application from memory.

## Request or execution-lifecycle explanation
Explain client, server, application, router, endpoint, validation, serialization, and response ownership in order.

## Debugging questions
Why would an import string fail? What happens when the returned object violates the response model?

## Design and trade-off questions
When should the one-file application be split? Which layer should own configuration and resource creation?

## Delayed-recall prompts
Review after 1, 3, 7, 14, and 30 days; shorten after a lifecycle or import mistake.

## Interview explanation practice
Answer one question at a time, including a changed requirement that adds a database dependency.

## Evidence
Link the typed implementation, scaffold result, challenge result after completion, trace, and explanation.

## State decision
Generation alone leaves the unit in Learning at most; use the progress evidence gates.
'''

def create_unit_fixture(root: Path, unit: Unit) -> Path:
    directory=unit_directory(root,unit); (directory/"examples").mkdir(parents=True,exist_ok=True); (directory/"practice").mkdir(parents=True,exist_ok=True)
    (directory/"README.md").write_text(fixture_readme(unit),encoding="utf-8")
    (directory/"REVIEW.md").write_text(fixture_review(unit),encoding="utf-8")
    (directory/"practice"/"README.md").write_text(fixture_practice(unit),encoding="utf-8")
    examples={
        "01_minimal.py":"def health() -> dict[str, str]:\n    return {'status': 'ok'}\n",
        "02_traced.py":"events = ['import', 'route-registered']\ndef call() -> list[str]:\n    return [*events, 'endpoint-called', 'serialized']\n",
        "03_realistic.py":"from dataclasses import dataclass\n@dataclass(frozen=True)\nclass ServiceStatus:\n    status: str\n    version: str\n",
        "04_failure_case.py":"def import_diagnostic(module: str, object_name: str) -> str:\n    return f'check {module}:{object_name}'\n",
    }
    for name,code in examples.items(): (directory/"examples"/name).write_text(code,encoding="utf-8")
    (directory/"practice"/"micro_lab.py").write_text("events=['import','registered']\nevents.append('called')\nprint(' -> '.join(events))\n",encoding="utf-8")
    (directory/"practice"/"starter.py").write_text("def status() -> dict[str, str]:\n    raise NotImplementedError('learner task')\n",encoding="utf-8")
    (directory/"practice"/"test_examples.py").write_text("from pathlib import Path\n\ndef test_example_files_exist():\n    assert (Path(__file__).parents[1] / 'examples' / '01_minimal.py').is_file()\n",encoding="utf-8")
    (directory/"practice"/"test_challenge.py").write_text("from practice.starter import status\n\ndef test_status_contract():\n    assert status() == {'status': 'ok'}\n\ndef test_status_is_fresh_mapping():\n    assert status() is not status()\n",encoding="utf-8")
    set_progress_state(root,unit.unit_id,"Draft")
    return directory

def run_fixture_suite(root: Path) -> dict[str,object]:
    cases=[]
    def record(name: str, passed: bool, detail: object) -> None:
        cases.append({"name":name,"status":"passed" if passed else "failed","detail":detail})
    # Fresh bootstrap.
    fresh=validate_repository(root,profile="bootstrap",run_external=False)
    record("fresh_bootstrap",not fresh.errors,{"errors":fresh.errors})
    # Normal clone .git directory and linked-worktree .git file are ignored.
    for name,kind in (("normal_git_directory","directory"),("linked_worktree_git_file","file")):
        holder=copy_repo(root); test_root=Path(holder.name)
        if kind=="directory":
            (test_root/".git").mkdir(); (test_root/".git"/"HEAD").write_text("ref: refs/heads/main\n"); (test_root/".git"/"internal.md").write_text("[secret](missing.md)\n`````\n")
        else: (test_root/".git").write_text("gitdir: /synthetic/worktrees/example\n")
        candidate=validate_repository(test_root,profile="bootstrap",run_external=False)
        record(name,not candidate.errors and candidate.statistics==fresh.statistics,{"errors":candidate.errors,"statistics_unchanged":candidate.statistics==fresh.statistics})
        holder.cleanup()
    # Working environment/caches are pruned.
    holder=copy_repo(root); test_root=Path(holder.name)
    (test_root/".venv"/"bin").mkdir(parents=True); (test_root/".venv"/"pyvenv.cfg").write_text("home = /synthetic\n")
    (test_root/"nested"/"__pycache__").mkdir(parents=True); (test_root/"nested"/"__pycache__"/"x.pyc").write_bytes(b"synthetic")
    (test_root/".pytest_cache").mkdir(); (test_root/".pytest_cache"/"README.md").write_text("[bad](missing.md)\n")
    candidate=validate_repository(test_root,profile="bootstrap",run_external=False)
    record("working_artifacts_ignored",not candidate.errors and candidate.statistics==fresh.statistics,{"errors":candidate.errors,"statistics_unchanged":candidate.statistics==fresh.statistics})
    holder.cleanup()
    # Realistic live unit.
    holder=copy_repo(root); test_root=Path(holder.name); _,units=parse_units(Report(test_root,"bootstrap")); unit=units["FAPI-FND-020"]
    directory=create_unit_fixture(test_root,unit)
    compile_proc=subprocess.run([sys.executable,"-m","compileall","-q",str(directory)],cwd=test_root,text=True,capture_output=True)
    lab_proc=subprocess.run([sys.executable,str(directory/"practice"/"micro_lab.py")],cwd=directory,text=True,capture_output=True)
    example_proc=subprocess.run([sys.executable,"-m","pytest","-q","practice/test_examples.py"],cwd=directory,text=True,capture_output=True)
    collect_proc=subprocess.run([sys.executable,"-m","pytest","--collect-only","-q","practice/test_challenge.py"],cwd=directory,text=True,capture_output=True)
    live=validate_repository(test_root,profile="live",run_external=False)
    collected=len(re.findall(r'test_[A-Za-z0-9_]+',collect_proc.stdout))
    record("realistic_initialized_core_unit",not live.errors and compile_proc.returncode==lab_proc.returncode==example_proc.returncode==collect_proc.returncode==0 and collected>=2,
           {"errors":live.errors,"compile_returncode":compile_proc.returncode,"micro_lab_returncode":lab_proc.returncode,"scaffold_returncode":example_proc.returncode,"challenge_collection_returncode":collect_proc.returncode,"challenge_tests_collected":collected,"challenge_tests_executed":False})
    # Completeness audit/no-op preservation proof by hashes.
    before={str(path.relative_to(directory)):sha256_file(path) for path in directory.rglob("*") if path.is_file()}
    live_again=validate_repository(test_root,profile="live",run_external=False)
    after={str(path.relative_to(directory)):sha256_file(path) for path in directory.rglob("*") if path.is_file()}
    record("complete_pack_rerun_preserves_learner_work",not live_again.errors and before==after,{"errors":live_again.errors,"hashes_unchanged":before==after})
    holder.cleanup()
    passed=sum(case["status"]=="passed" for case in cases)
    return {"status":"passed" if passed==len(cases) else "failed","count":len(cases),"passed":passed,"cases":cases}

def make_zip_from_root(root: Path, archive: Path, extras: dict[str,bytes]|None=None) -> None:
    extras=extras or {}
    with zipfile.ZipFile(archive,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as zf:
        for path in iter_repo_files(root,"bootstrap"):
            rel=path.relative_to(root).as_posix()
            if rel.startswith(("units/","projects/")): continue
            zf.write(path,rel)
        for name,data in extras.items(): zf.writestr(name,data)

def run_self_tests(root: Path) -> dict[str,object]:
    results=[]
    def run_mutation(name: str, expected: str, mutate, *, profile: str="bootstrap") -> None:
        holder=copy_repo(root); test_root=Path(holder.name)
        try:
            mutate(test_root)
            candidate=validate_repository(test_root,profile=profile,run_external=False)
            observed=next((error for error in candidate.errors if expected in error),None)
            results.append({"name":name,"status":"passed" if observed else "failed","expected_error":expected,"observed_matching_error":observed,"observed_error_count":len(candidate.errors)})
        except Exception as exc:
            results.append({"name":name,"status":"failed","expected_error":expected,"observed_matching_error":None,"detail":str(exc)})
        finally: holder.cleanup()
    def replace_once(path: Path, old: str, new: str) -> None:
        text=path.read_text(encoding="utf-8")
        if old not in text: raise AssertionError(f"missing mutation source {old[:50]!r}")
        path.write_text(text.replace(old,new,1),encoding="utf-8")
    def mutate_unit_row(root_path: Path, uid: str, replacements: tuple[tuple[str,str],...]) -> None:
        curriculum=root_path/"CURRICULUM.md"
        lines=curriculum.read_text(encoding="utf-8").splitlines()
        changed=False
        for index,line in enumerate(lines):
            if f"`{uid}`" not in line: continue
            for old,new in replacements:
                line=line.replace(old,new)
            lines[index]=line; changed=True; break
        if not changed: raise AssertionError(f"missing unit row {uid}")
        curriculum.write_text("\n".join(lines)+"\n",encoding="utf-8")
    run_mutation("duplicate_unit_id","[DUPLICATE_UNIT_ID]",lambda r:(r/"CURRICULUM.md").write_text((r/"CURRICULUM.md").read_text()+next(line for line in (r/"CURRICULUM.md").read_text().splitlines() if "`FAPI-FND-010`" in line)+"\n"))
    run_mutation("missing_prerequisite","[MISSING_PREREQUISITE]",lambda r:replace_once(r/"CURRICULUM.md","`FAPI-FND-010` | `C` |","`FAPI-ZZZ-999` | `C` |"))
    run_mutation("prerequisite_cycle","[CURRICULUM_PREREQUISITE_ORDER]",lambda r:replace_once(r/"CURRICULUM.md","| None | `C` | `M` | `H` | `H` | `D1` | `1` | Python, Tooling | `M` |","| `FAPI-FND-020` | `C` | `M` | `H` | `H` | `D1` | `1` | Python, Tooling | `M` |"))
    run_mutation("wrong_path_count","[PATH_COUNT_MISMATCH]",lambda r:replace_once(r/"LEARNING_PATHS.md",'"declared_units":35','"declared_units":34'))
    run_mutation("incorrect_path_timing","[PATH_TOTAL_TIME_MISMATCH]",lambda r:replace_once(r/"LEARNING_PATHS.md",'"rapid_total_minutes":[1970,2980]','"rapid_total_minutes":[1971,2980]'))
    run_mutation("stale_displayed_path_count","[PATH_VISIBLE_COUNT_MISMATCH]",lambda r:replace_once(r/"LEARNING_PATHS.md","| Canonical units | 35 |","| Canonical units | 34 |"))
    run_mutation("stale_displayed_path_timing","[PATH_VISIBLE_RAPID_UNIT_TIME_MISMATCH]",lambda r:replace_once(r/"LEARNING_PATHS.md","| Rapid unit study | 23 h 50 min–36 h 40 min |","| Rapid unit study | 23 h 51 min–36 h 40 min |"))
    run_mutation("missing_progress_row","[PROGRESS_PARITY_MISMATCH]",lambda r:replace_once(r/"PROGRESS.md",next(line for line in (r/"PROGRESS.md").read_text().splitlines() if "`FAPI-FND-010`" in line)+"\n",""))
    run_mutation("missing_project_tracker","[PROJECT_TRACKER_PARITY]",lambda r:replace_once(r/"PROGRESS.md",next(line for line in (r/"PROGRESS.md").read_text().splitlines() if "`FAPI-PRJ-010`" in line)+"\n",""))
    run_mutation("broken_markdown_fence","[MARKDOWN_FENCE_UNBALANCED]",lambda r:(r/"README.md").write_text((r/"README.md").read_text()+"\n```python\n"))
    run_mutation("broken_internal_link","[MARKDOWN_LINK_MISSING]",lambda r:(r/"README.md").write_text((r/"README.md").read_text()+"\n[broken](missing.md)\n"))
    run_mutation("missing_dev_tool","[DEVELOPMENT_TOOL_MISSING]",lambda r:replace_once(r/"pyproject.toml",'  "hypothesis==6.165.10",\n',''))
    run_mutation("workflow_loses_current_operation_guard","[WORKFLOW_CONTRACT_MISSING]",lambda r:replace_once(r/"docs/WORKFLOW.md","current-operation-only commit boundary","same operation"))
    run_mutation("private_working_path","[PROFILE_FORBIDDEN_PRIVATE_PATH]",lambda r:((r/"private").mkdir(),(r/"private"/"notes.txt").write_text("synthetic")))
    run_mutation("tokens_working_path","[PROFILE_FORBIDDEN_PRIVATE_PATH]",lambda r:((r/"tokens").mkdir(),(r/"tokens"/"example.txt").write_text("synthetic")))
    # MSV and RabbitMQ extension mutations. Each must match its intended error.
    run_mutation("missing_rabbitmq_profile","[COMPOSE_PROFILE_MISMATCH]",lambda r:replace_once(r/"compose.yaml",'    profiles: ["rabbitmq"]','    profiles: ["redis"]'))
    run_mutation("missing_publisher_confirms","[MSV_REQUIRED_CONCEPT_MISSING]",lambda r:mutate_unit_row(r,"FAPI-MSV-070",(("publisher confirms","publish receipts"),("Publisher confirms","Publish receipts"))))
    run_mutation("confirm_ack_conflation","[MSV_CONFIRM_ACK_CONFLATION]",lambda r:replace_once(r/"CURRICULUM.md","Publisher confirms are not consumer acknowledgements;","Publisher confirms are consumer acknowledgements;"))
    run_mutation("missing_manual_ack","[MSV_MANUAL_ACK_MISSING]",lambda r:replace_once(r/"CURRICULUM.md","manual acknowledgements","consumer completion signals"))
    run_mutation("unbounded_retry_guidance","[MSV_RETRY_DLQ_MISSING]",lambda r:replace_once(r/"CURRICULUM.md","Design bounded immediate and delayed retries","Design unlimited immediate and delayed retries"))
    run_mutation("unqualified_exactly_once","[MSV_EXACTLY_ONCE_UNQUALIFIED]",lambda r:(r/"CURRICULUM.md").write_text((r/"CURRICULUM.md").read_text()+"\nExactly once is guaranteed everywhere.\n"))
    run_mutation("missing_outbox_inbox","[MSV_OUTBOX_INBOX_MISSING]",lambda r:mutate_unit_row(r,"FAPI-MSV-120",(("outbox","dispatch"),("Outbox","Dispatch"),("inbox","receipt"),("Inbox","Receipt"))))
    run_mutation("missing_data_ownership","[MSV_DATA_OWNERSHIP_MISSING]",lambda r:(mutate_unit_row(r,"FAPI-MSV-010",(("data ownership","data placement"),("Data Ownership","Data Placement"))),mutate_unit_row(r,"FAPI-MSV-200",(("data ownership","data placement"),("Data Ownership","Data Placement")))))
    run_mutation("grpc_missing_deadline","[MSV_GRPC_DEADLINE_MISSING]",lambda r:mutate_unit_row(r,"FAPI-MSV-160",(("deadlines","time budgets"),("Deadlines","Time Budgets"),("deadline","time budget"),("Deadline","Time Budget"))))
    run_mutation("invalid_python_reference","[PYTHON_REFERENCE_UNKNOWN]",lambda r:(r/"PYTHON_REFERENCES.md").write_text((r/"PYTHON_REFERENCES.md").read_text()+"\n`PY-ZZZ-999`\n"))
    run_mutation("invalid_solid_reference","[SOLID_REFERENCE_UNKNOWN]",lambda r:(r/"SOLID_DESIGN_REFERENCES.md").write_text((r/"SOLID_DESIGN_REFERENCES.md").read_text()+"\n`SDP-ZZZ-999`\n"))
    run_mutation("new_path_missing_prerequisite","[PATH_PREREQUISITE_ORDER]",lambda r:replace_once(r/"LEARNING_PATHS.md","| 1 | [FAPI-FND-010", "| 1 | [FAPI-MSV-270"))
    run_mutation("duplicate_microservice_unit","[DUPLICATE_UNIT_ID]",lambda r:(r/"CURRICULUM.md").write_text((r/"CURRICULUM.md").read_text()+next(line for line in (r/"CURRICULUM.md").read_text().splitlines() if "`FAPI-MSV-010`" in line)+"\n"))
    run_mutation("stale_readme_path_count","[README_COUNT_MISMATCH]",lambda r:replace_once(r/"README.md","17 prerequisite-safe learning paths","14 prerequisite-safe learning paths"))
    run_mutation("stale_readme_project_count","[README_COUNT_MISMATCH]",lambda r:replace_once(r/"README.md","10 milestone projects","8 milestone projects"))
    run_mutation("impossible_path_schedule","[PATH_SCHEDULE_CAPACITY_MISMATCH]",lambda r:replace_once(r/"LEARNING_PATHS.md",'"hours_per_week":[9,10]','"hours_per_week":[1,1]'))
    def remove_overlap_justifications(root_path: Path) -> None:
        path=root_path/"LEARNING_PATHS.md"
        text=path.read_text(encoding="utf-8")
        text=text.replace('"overlap_justifications":{"microservices-distributed-service-engineering":"Intentional focused subset: this path isolates RabbitMQ publisher, consumer, retry, idempotency, outbox, resilience, and observability evidence for learners who do not yet need the complete distributed-service curriculum."}','"overlap_justifications":{}',1)
        text=text.replace('"overlap_justifications":{"rabbitmq-reliable-async-services":"Intentional superset: RabbitMQ is one complete phase of this broader service-engineering path, so learners who finished the focused path may mark those overlapping units as diagnostic revisits rather than repeat all labs.","senior-microservices-design-operations":"Intentional foundation: the senior route revisits a selected subset after this path and demands deeper design, incident, governance, and migration evidence."}','"overlap_justifications":{}',1)
        path.write_text(text,encoding="utf-8")
    run_mutation("unjustified_path_overlap","[PATH_OVERLAP_UNJUSTIFIED]",remove_overlap_justifications)
    run_mutation("rabbitmq_host_shell_variable","[RABBITMQ_HOST_ENV_RELIANCE]",lambda r:(r/"docs/TOOLCHAIN_AND_INFRASTRUCTURE.md").write_text((r/"docs/TOOLCHAIN_AND_INFRASTRUCTURE.md").read_text()+"\nrabbitmqctl list_queues -p \"$RABBITMQ_VHOST\"\n"))
    run_mutation("rabbitmq_unsupported_field","[RABBITMQCTL_UNSUPPORTED_FIELD]",lambda r:replace_once(r/"docs/TOOLCHAIN_AND_INFRASTRUCTURE.md","consumer_utilisation","consumer_capacity"))
    run_mutation("rabbitmq_list_consumers_arguments","[RABBITMQCTL_UNSUPPORTED_ARGUMENT]",lambda r:replace_once(r/"docs/TOOLCHAIN_AND_INFRASTRUCTURE.md",'rabbitmqctl list_consumers -p "$RABBITMQ_DEFAULT_VHOST"','rabbitmqctl list_consumers -p "$RABBITMQ_DEFAULT_VHOST" queue_name channel_pid'))
    run_mutation("rabbitmq_port_not_loopback","[RABBITMQ_PORT_NOT_LOOPBACK]",lambda r:replace_once(r/"compose.yaml",'127.0.0.1:${RABBITMQ_AMQP_PORT:-5672}:5672','${RABBITMQ_AMQP_PORT:-5672}:5672'))
    for mutation_name,old_binding,new_binding in (
        ("postgres_port_not_loopback",'127.0.0.1:${POSTGRES_PORT:-55432}:5432','${POSTGRES_PORT:-55432}:5432'),
        ("redis_port_not_loopback",'127.0.0.1:${REDIS_PORT:-56379}:6379','${REDIS_PORT:-56379}:6379'),
        ("mailpit_smtp_port_not_loopback",'127.0.0.1:${MAILPIT_SMTP_PORT:-51025}:1025','${MAILPIT_SMTP_PORT:-51025}:1025'),
        ("mailpit_ui_port_not_loopback",'127.0.0.1:${MAILPIT_UI_PORT:-58025}:8025','${MAILPIT_UI_PORT:-58025}:8025'),
        ("observability_ui_port_not_loopback",'127.0.0.1:${OTEL_LGTM_PORT:-53000}:3000','${OTEL_LGTM_PORT:-53000}:3000'),
        ("otlp_grpc_port_not_loopback",'127.0.0.1:4317:4317','4317:4317'),
        ("otlp_http_port_not_loopback",'127.0.0.1:4318:4318','4318:4318'),
    ):
        run_mutation(mutation_name,"[COMPOSE_PORT_NOT_LOOPBACK]",lambda r,old=old_binding,new=new_binding:replace_once(r/"compose.yaml",old,new))
    run_mutation("rabbitmq_healthcheck_missing","[RABBITMQ_HEALTHCHECK_MISSING]",lambda r:replace_once(r/"compose.yaml","    healthcheck:\n      test: [\"CMD\", \"rabbitmq-diagnostics\", \"-q\", \"ping\"]","    x-healthcheck-removed:\n      test: [\"CMD\", \"rabbitmq-diagnostics\", \"-q\", \"ping\"]"))
    run_mutation("rabbitmq43_transient_nonexclusive_queue","[RABBITMQ43_TRANSIENT_QUEUE_INCOMPATIBLE]",lambda r:replace_once(r/"scripts/validate_repo.py",'declare_queue("", durable=False, exclusive=True, auto_delete=True, arguments=','declare_queue("fapi.validator.main", durable=False, exclusive=False, auto_delete=True, arguments='))
    run_mutation("rabbitmq_broad_volume_delete","[RABBITMQ_BROAD_VOLUME_DELETE]",lambda r:(r/"docs/TOOLCHAIN_AND_INFRASTRUCTURE.md").write_text((r/"docs/TOOLCHAIN_AND_INFRASTRUCTURE.md").read_text()+"\ndocker compose down --volumes\n"))
    def inject_generic_references(root_path: Path) -> None:
        path=root_path/"PYTHON_REFERENCES.md"
        text=path.read_text(encoding="utf-8")
        generic='| `MSV` | [PY-CON-060 — Asyncio event loop, coroutines, tasks, and context](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-con-060) | Soft prerequisite | Recall generic behavior for all topics without detail. | Apply the same generic sentence everywhere without a concrete implementation site. | Every boundary changes in the same generic way; avoid generic misuse. | Use the same generic bridge for every mapping. |\n'
        path.write_text(text+generic*6,encoding="utf-8")
    run_mutation("repeated_generic_reference_mapping","[REFERENCE_GENERIC_MAPPING]",inject_generic_references)
    run_mutation("project_missing_failure_injection","[MSV_PROJECT_FAILURE_EVIDENCE_MISSING]",lambda r:replace_once(r/"PROJECTS.md","failure injection","failure simulation"))
    # Live pack mutations.
    for name,expected,action in (
        ("missing_practice","[UNIT_MISSING_PRACTICE]",lambda d:shutil.rmtree(d/"practice")),
        ("shallow_practice","[UNIT_PRACTICE_TASK_SHALLOW]",lambda d:(d/"practice"/"README.md").write_text("# Practice\n\n### Task 1 — Name only\n")),
        ("missing_review","[UNIT_MISSING_REVIEW]",lambda d:(d/"REVIEW.md").unlink()),
        ("missing_interview_questions","[UNIT_INTERVIEW_COVERAGE_MISSING]",lambda d:replace_once(d/"README.md","- Definition: what does FastAPI add above Starlette and Pydantic?","- General question.")),
        ("missing_micro_lab","[UNIT_MISSING_MICRO_LAB]",lambda d:(d/"practice"/"micro_lab.py").unlink()),
        ("unresolved_placeholder","[UNIT_TEMPLATE_PLACEHOLDER]",lambda d:(d/"README.md").write_text((d/"README.md").read_text()+"\n{{UNRESOLVED}}\n")),
        ("premature_solution","[UNIT_PREMATURE_SOLUTION]",lambda d:(d/"practice"/"README.md").write_text((d/"practice"/"README.md").read_text()+"\n## Complete solution\n")),
    ):
        holder=copy_repo(root); test_root=Path(holder.name); temp_report=Report(test_root,"bootstrap"); _,units=parse_units(temp_report); directory=create_unit_fixture(test_root,units["FAPI-FND-020"])
        try:
            action(directory); candidate=validate_repository(test_root,profile="live",run_external=False); observed=next((e for e in candidate.errors if expected in e),None)
            results.append({"name":name,"status":"passed" if observed else "failed","expected_error":expected,"observed_matching_error":observed,"observed_error_count":len(candidate.errors)})
        except Exception as exc: results.append({"name":name,"status":"failed","expected_error":expected,"observed_matching_error":None,"detail":str(exc)})
        holder.cleanup()
    # Required experiment mutation uses an X unit.
    holder=copy_repo(root); test_root=Path(holder.name); temp_report=Report(test_root,"bootstrap"); _,units=parse_units(temp_report); unit=units["FAPI-HTTP-070"]; directory=create_unit_fixture(test_root,unit)
    candidate=validate_repository(test_root,profile="live",run_external=False); expected="[UNIT_MISSING_EXPERIMENT]"; observed=next((e for e in candidate.errors if expected in e),None)
    results.append({"name":"missing_required_experiment","status":"passed" if observed else "failed","expected_error":expected,"observed_matching_error":observed,"observed_error_count":len(candidate.errors)}); holder.cleanup()
    # Archive mutations.
    for name,entry,expected in (
        ("archive_git",".git/HEAD","[ARCHIVE_FORBIDDEN_GIT_METADATA]"),
        ("archive_generated_unit","units/demo/README.md","[ARCHIVE_FORBIDDEN_GENERATED_PATH]"),
        ("archive_virtual_environment",".venv/pyvenv.cfg","[ARCHIVE_FORBIDDEN_WORKING_ARTIFACT]"),
        ("archive_cache","nested/__pycache__/x.pyc","[ARCHIVE_FORBIDDEN_WORKING_ARTIFACT]"),
        ("archive_private","private/notes.txt","[ARCHIVE_FORBIDDEN_PRIVATE_PATH]"),
        ("archive_tokens","tokens/example.txt","[ARCHIVE_FORBIDDEN_PRIVATE_PATH]"),
    ):
        with tempfile.TemporaryDirectory(prefix="fastapi-archive-mutation-") as temp:
            archive=Path(temp)/"mutated.zip"; make_zip_from_root(root,archive,{entry:b"synthetic"})
            candidate=validate_repository(root,profile="bootstrap",run_external=False); validate_archive(candidate,archive)
            observed=next((e for e in candidate.errors if expected in e),None)
            results.append({"name":name,"status":"passed" if observed else "failed","expected_error":expected,"observed_matching_error":observed,"observed_error_count":len(candidate.errors)})
    # Genuine stale report mutation.
    with tempfile.TemporaryDirectory(prefix="fastapi-stale-report-") as temp:
        archive=Path(temp)/"dsa-no-fastapi.zip"; make_zip_from_root(root,archive)
        candidate=validate_repository(root,profile="bootstrap",run_external=False); validate_archive(candidate,archive)
        report_path=Path(temp)/"report.json"; payload=candidate.as_dict(); payload["archive"]["entry_count"]=-1; report_path.write_text(json.dumps(payload))
        verified=verify_report(report_path,archive,compare_self_tests=False,allow_renamed=False)
        expected="REPORT_ARCHIVE_ENTRY_COUNT_MISMATCH"; observed=next((e for e in verified["errors"] if expected in e),None)
        results.append({"name":"stale_report_metadata","status":"passed" if observed else "failed","expected_error":expected,"observed_matching_error":observed,"observed_error_count":len(verified["errors"])})
    evidence_reference={
        "status":"passed","count":1,"passed":1,
        "cases":[{"name":"sample_mutation","status":"passed","expected_error":"[SAMPLE]","observed_matching_error":"[SAMPLE] matched","observed_error_count":1}],
        "fixtures":{"status":"passed","count":1,"passed":1,"cases":[{"name":"sample_fixture","status":"passed","detail":{"errors":[],"evidence":"stable"}}]},
    }
    tampered_case=copy.deepcopy(evidence_reference); tampered_case["cases"][0]["observed_matching_error"]="[SAMPLE] tampered"
    case_errors=compare_self_test_evidence(tampered_case,evidence_reference)
    expected="REPORT_SELF_TEST_CASE_EVIDENCE_MISMATCH"; observed=next((item for item in case_errors if expected in item),None)
    results.append({"name":"tampered_mutation_evidence","status":"passed" if observed else "failed","expected_error":expected,"observed_matching_error":observed,"observed_error_count":len(case_errors)})
    tampered_fixture=copy.deepcopy(evidence_reference); tampered_fixture["fixtures"]["cases"][0]["detail"]["evidence"]="tampered"
    fixture_errors=compare_self_test_evidence(tampered_fixture,evidence_reference)
    expected="REPORT_FIXTURE_EVIDENCE_MISMATCH"; observed=next((item for item in fixture_errors if expected in item),None)
    results.append({"name":"tampered_fixture_evidence","status":"passed" if observed else "failed","expected_error":expected,"observed_matching_error":observed,"observed_error_count":len(fixture_errors)})
    fixtures=run_fixture_suite(root)
    passed=sum(item["status"]=="passed" for item in results)
    overall=passed==len(results) and fixtures["status"]=="passed"
    return {"status":"passed" if overall else "failed","count":len(results),"passed":passed,"cases":results,"fixtures":fixtures}

def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",type=Path,default=Path.cwd())
    parser.add_argument("--profile",choices=sorted(VALIDATION_PROFILES),default="auto")
    parser.add_argument("--archive",type=Path)
    parser.add_argument("--json",type=Path,dest="json_path")
    parser.add_argument("--verify-report",type=Path,dest="verify_report")
    parser.add_argument("--allow-renamed-archive",action="store_true")
    parser.add_argument("--skip-self-test-comparison",action="store_true")
    parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args()
    if args.verify_report:
        if not args.archive: parser.error("--verify-report requires --archive")
        result=verify_report(args.verify_report,args.archive,compare_self_tests=not args.skip_self_test_comparison,allow_renamed=args.allow_renamed_archive)
        print(json.dumps(result,indent=2,sort_keys=True)); return 0 if result["status"]=="passed" else 1
    report=validate_repository(args.root,profile=args.profile)
    if args.self_test:
        missing=extended_prerequisite_error("Validator --self-test")
        if missing:
            report.error(missing); report.mark("validator_self_tests","skipped")
            report.self_tests={"status":"skipped","reason":missing,"setup_command":"uv sync --group dev","run_command":"uv run --group dev python scripts/validate_repo.py --self-test","count":0,"passed":0,"cases":[],"fixtures":{"status":"skipped","count":0,"passed":0,"cases":[]}}
        else:
            report.self_tests=run_self_tests(args.root.resolve()); report.mark("validator_self_tests",report.self_tests["status"]=="passed")
            if report.self_tests["status"]!="passed": report.error("[VALIDATOR_SELF_TEST_FAILURE] Mutation or fixture tests failed")
    if args.archive: validate_archive(report,args.archive,run_external=False)
    payload=report.as_dict()
    if args.json_path:
        args.json_path.parent.mkdir(parents=True,exist_ok=True); args.json_path.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2,sort_keys=True)); return 0 if payload["status"]=="passed" else 1

if __name__=="__main__": raise SystemExit(main())
