# zoko

A Python library for interacting with the [Zoko](https://www.zoko.io/) APIs.

[![Tests](https://github.com/rocktimsaikia/zoko-python/actions/workflows/test-package.yml/badge.svg)](https://github.com/rocktimsaikia/zoko-python/actions/workflows/test-package.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/zoko.svg)](https://pypi.org/project/zoko)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zoko.svg)](https://pypi.org/project/zoko)

## Installation

```console
pip install zoko
```

## Quickstart

```python
from zoko import ZokoClient, MessageType

zoko = ZokoClient(api_key="YOUR_API_KEY")

zoko.message.send_message(
    recipient="919998880000",
    template_type=MessageType.TEXT,
    message="Hi there! Thanks for reaching out. How can we help you today?",
)
```

## Resources

```python
zoko.account   # templates
zoko.message   # send, get, delete, history
zoko.customer  # customers, properties, tags, assign
zoko.agent     # agents, teams
zoko.webhook   # webhooks
zoko.group     # WhatsApp groups
```

## Retries

Transient failures (connection errors, `429`, `5xx`) can be retried automatically:

```python
zoko = ZokoClient(api_key="YOUR_API_KEY", max_retries=3, backoff_factor=0.5)
```

Disabled by default (`max_retries=0`). Applies to every request, POST included.

## Usage

Runnable examples covering every method, one file per resource:

| Resource | Examples |
|----------|----------|
| account  | [examples/account.py](./examples/account.py)   |
| message  | [examples/message.py](./examples/message.py)   |
| customer | [examples/customer.py](./examples/customer.py) |
| agent    | [examples/agent.py](./examples/agent.py)       |
| webhook  | [examples/webhook.py](./examples/webhook.py)   |
| group    | [examples/group.py](./examples/group.py)       |

## License

`zoko` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
