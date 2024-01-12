# zoko

A Python library for interacting with the [Zoko](https://www.zoko.io/) APIs.
> :construction: This project is work in progress. The library still has a lot of methods to implement.

[![Tests](https://github.com/rocktimsaikia/zoko-python/actions/workflows/test-package.yml/badge.svg)](https://github.com/rocktimsaikia/zoko-python/actions/workflows/test-package.yml)
<!-- [![PyPI - Version](https://img.shields.io/pypi/v/zoko.svg)](https://pypi.org/project/zoko) -->
<!-- [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zoko.svg)](https://pypi.org/project/zoko) -->

---

**Table of Contents**

- [Installation](#installation)
- [Quickstart](#quickstart)
- [Documentation](#documentation)
- [License](#license)

## Installation

```console
pip install zoko
```


## Quickstart

```python
from zoko import ZokoClient

# Initialize the client with your Zoko API key
zoko = ZokoClient(api_key='YOUR_API_KEY')

# Get all all templates
templates = zoko.account.get_all_templates()

print(templates)
```

Expected output:

```python
[
  {
    "active": True,
    "channel": "whatsapp",
    "isRichTemplate": True,
    "templateDesc": "Good morning {{1}}. How may I help you today?",
    "templateId": "greeting_01",
    "templateLanguage": "en",
    "templateType": "buttonTemplate",
    "templateVariableCount": 1
  }
]
```

## Documentation
You can find the documentation for the all the available resource and method examples [here](./examples).

## License

`zoko` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
