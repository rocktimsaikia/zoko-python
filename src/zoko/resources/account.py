import requests
from zoko.constants import endpoint


class Account:
    def __init__(self, __headers):
        self.__headers = __headers
        pass

    def get_all_templates(self):
        response = requests.request(
            "GET",
            endpoint.AccountEndpoint.TEMPLATES,
            headers=self.__headers,
        )
        response_json = response.json()
        return response_json

    def get_template_by_id(self, template_id: str):
        if template_id is None:
            raise ValueError("Template ID is required")

        all_templates = self.get_all_templates()
        current_template = [
            template
            for template in all_templates
            if template["templateId"] == template_id
        ]
        current_template = current_template[0]
        return current_template or None
