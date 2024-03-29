from typing import List, TypedDict

import requests

from zoko.constants import endpoint
from zoko.types.common import TemplateType


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

    def get_templates_by_type(self, template_type: TemplateType) -> List[Template]:
        """
        Get the templates by type.

        Parameters
        ----------
        template_type
            The type of the template to be fetched. Must be one of the following:
                - text
                - image
                - document
                - audio
                - video
                - location
                - sticker
                - contacts
                - template
                - richTemplate
                - buttonTemplate

        Returns
        -------
        List[Template]
            List of templates with the given type.

        Raises
        ------
        ValueError:
            Raised when the template type is not provided.
        ValueError:
            Raised when the template type is invalid or not found.
        """
        if template_type is None:
            raise ValueError("Template type is required")

        all_templates = self.get_all_templates()
        templates_filtered = [
            template
            for template in all_templates
            if template["templateType"] == template_type
        ]
        if templates_filtered is None:
            raise ValueError("Template type is invalid")
        return templates_filtered
