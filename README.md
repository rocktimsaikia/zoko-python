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
from zoko import ZokoClient, ZokoError

zoko = ZokoClient(api_key="YOUR_API_KEY")

templates = zoko.account.get_all_templates()

try:
    zoko.message.send_message(recipient="919998880000", template_type="text", message="Hi")
except ZokoError as err:
    print(err.status_code, err.response)
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

See [examples](./examples) for usage.

## License

`zoko` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
