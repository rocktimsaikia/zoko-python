# zoko

A Python library for interacting with the [Zoko](https://www.zoko.io/) APIs.
> :construction: This project is work in progress. Account, Message, Customer, Agent, Webhook and Group resources are implemented.

[![Tests](https://github.com/rocktimsaikia/zoko-python/actions/workflows/test-package.yml/badge.svg)](https://github.com/rocktimsaikia/zoko-python/actions/workflows/test-package.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/zoko.svg)](https://pypi.org/project/zoko)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zoko.svg)](https://pypi.org/project/zoko)

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

## Resources

The client exposes one attribute per resource:

```python
zoko.account   # get_all_templates, get_template_by_id, get_templates_by_type
zoko.message   # send_message, get_message, delete_message, get_message_history, delete_messages
zoko.customer  # get_customers, get_customer, delete_messages, properties (list/create/get/update/delete),
               # tags (list_tags/update_tags/add_tag/delete_tag), assign_customer
zoko.agent     # get_agent, update_agent, get_agents, get_teams
zoko.webhook   # get_webhooks, create_webhook, get_webhook, update_webhook, delete_webhook
zoko.group     # create_group, get_groups, get_group, update_settings, delete_group, invite_members,
               # remove_participants, invite links, join requests, auto-approval, invitation template
```

Any non-2xx response raises `zoko.ZokoError`, which carries `status_code` and the parsed `response` body:

```python
from zoko import ZokoClient, ZokoError

zoko = ZokoClient(api_key="YOUR_API_KEY")
try:
    zoko.customer.get_customer("bad-id")
except ZokoError as err:
    print(err.status_code, err.response)
```

## Documentation
You can find the documentation for the all the available resource and method examples [here](./examples).

## License

`zoko` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
