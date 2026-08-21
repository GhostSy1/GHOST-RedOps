# GHOST-RedOps Architecture Review

## Purpose of this document

This document records the repository structure observed during the portfolio review. It is intentionally factual: it describes paths that exist in the checkout and does not imply capabilities that are not implemented.

## Implementation inventory

| Property | Observed value |
|---|---|
| Repository | `GHOST-RedOps` |
| Languages | C++, Python |
| Source-file count | 16 |
| Execution policy | Must be confirmed from the source before use |
| Release boundary | Authorized systems and operator-supplied data only |

## Source map

- `core/__init__.py`
- `core/advanced_evasion.cpp`
- `core/container_escape.cpp`
- `core/generator.py`
- `core/hollowing.cpp`
- `core/injector.cpp`
- `core/obfuscator.py`
- `core/orchestrator.py`
- `core/post_exploitation.py`
- `core/stealth.py`
- `main.py`
- `payloads/__init__.py`
- `payloads/generator.py`
- `tests/test_redops.py`
- `tests/test_repository_contract.py`
- `utils/__init__.py`

## Review expectations

The command-line entry point, if present, should validate operator input, fail closed on invalid paths, and report observations with their source. Network access, external service calls, and privileged actions should be explicit in the README and should never be hidden behind a default command. A detection result must remain traceable to evidence rather than a hardcoded example.

## Change boundary

A change should update the relevant source module, tests, CLI reference, and changelog entry. A public release must not contain credentials, private keys, customer data, raw engagement artifacts, or undocumented access mechanisms.
