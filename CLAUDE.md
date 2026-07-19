# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

`zoko` is a Python SDK wrapping the [Zoko](https://www.zoko.io/) WhatsApp business API (base URL `https://chat.zoko.io/v2`). Early-stage (v0.0.1). Implemented resources: Account, Message, Customer, Agent, Webhook, Group.

## Commands

```bash
pip install -r requirements.txt   # install test deps (requests, httpretty, python-dotenv)
pip install pre-commit            # dev tooling; kept out of requirements.txt (pre-commit 4.x needs py>=3.9, but CI tests 3.8)
pre-commit install                # activate git hooks (run once after cloning)
python -m unittest -v             # run all tests
python -m unittest -v tests.test_client_message.TestZokoClientMessage.test_send_message_success  # single test
flake8 . --select=E9,F63,F7,F82   # lint (mirrors CI; E9/F-codes fail the build)
pre-commit run -a                 # run all hooks (black + whitespace/eol) across the repo
```

Note: the black hook is pinned to 25.1.0 because it runs under Python 3.9; newer black requires >=3.10.

CI (`.github/workflows/test-package.yml`) runs flake8 + unittest on Python 3.8/3.9/3.10, plus a separate `pre-commit` job, for pushes/PRs to `main`.

## Architecture

- `ZokoClient(api_key)` builds an `apikey` header dict (lowercase - the API rejects other casings) and passes it to each resource, exposed as `client.account`, `.message`, `.customer`, `.agent`, `.webhook`, `.group`.
- All resources subclass `Resource` (`zoko/resources/base.py`), which owns the shared `_request(method, url, *, params, json)`: it sends via `requests`, raises `ZokoError` (`zoko/exceptions.py`) on non-2xx, and returns parsed JSON (or `None` for 204/empty). `Resource._clean(payload)` drops `None` values so optional fields aren't sent as null - every method builds its payload/params dict and passes it through `_clean`.
- All URLs are centralized in `zoko/constants/endpoint.py` as class attributes with `{placeholder}` templates filled via `str.format`. Note the Group resource uses a different base (`/v2/channels/whatsapp/cloud/group`), not `/v2/group`.
- Types: `TypedDict` for request/response payload shapes (defined inline in each resource file), `Literal` enums in `zoko/types/common.py` (`TemplateType`, `Channel`, `CustomerPropertyType`, `AgentRole`, `WebhookEvent`, `JoinRequestAction`).
- `get_template_by_id` / `get_templates_by_type` filter client-side over `get_all_templates()` - there is no dedicated server endpoint for these.
- Group identifiers: `create_group` returns the internal UUID as `_id`; that UUID (not Meta's `group_id`) is what subsequent group calls take.

## Conventions

- Tests use `httpretty` to mock HTTP; `allow_net_connect=False` so tests must register every URI they hit. `httpretty==1.1.4` breaks on `urllib3>=2`, so requirements.txt pins `urllib3<2` - keep it until httpretty is bumped.
- Public methods carry NumPy-style docstrings; match that style when adding methods.
- Adding a resource: add an endpoint class to `endpoint.py`, create `zoko/resources/<name>.py` with a class subclassing `Resource` and calling `self._request(...)`, then wire it into `ZokoClient.__init__`. Don't call `requests` directly - go through `_request` so error handling stays consistent.
