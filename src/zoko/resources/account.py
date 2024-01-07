import requests
from zoko.constants import endpoint
from typing import TypedDict, List


class Template(TypedDict):
    active: bool
    channel: str
    isRichTemplate: bool
    templateDesc: str
    templateId: str
    templateLanguage: str
    templateType: str
    templateVariableCount: int


class Account:
    def __init__(self, __headers):
        self.__headers = __headers
        pass

    def get_all_templates(self) -> List[Template]:
        """
        Returns all the templates for the account.

        Returns
        -------
        list[Template]
            List of all the available templates for the account.
        """
        response = requests.request(
            "GET",
            endpoint.AccountEndpoint.TEMPLATES,
            headers=self.__headers,
        )
        response_json = response.json()
        return response_json

    def get_template_by_id(self, template_id: str) -> Template:
        """
        Get the template by ID.

        Parameters
        ----------
        template_id
            The ID of the template to be fetched.

        Returns
        -------
        Template
            The template object with the given ID.

        Raises
        ------
        ValueError:
            Raised when the template ID is not provided.
        ValueError:
            Raised when the template ID is invalid or not found.
        """
        if template_id is None:
            raise ValueError("Template ID is required")

        all_templates = self.get_all_templates()
        current_template = [
            template
            for template in all_templates
            if template["templateId"] == template_id
        ]
        current_template = current_template[0]
        if current_template is None:
            raise ValueError("Template ID is invalid")
        return current_template
