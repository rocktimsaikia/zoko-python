from zoko.exceptions import ZokoError


class Resource:
    """Base class for API resources. Holds auth headers and sends requests."""

    def __init__(self, session, headers):
        self._session = session
        self._headers = headers

    @staticmethod
    def _clean(payload):
        # Drop keys whose value is None so optional fields aren't sent as null.
        return {k: v for k, v in payload.items() if v is not None}

    def _request(self, method, url, *, params=None, json=None):
        response = self._session.request(
            method,
            url,
            headers=self._headers,
            params=params,
            json=json,
        )
        if not response.ok:
            try:
                body = response.json()
                message = body.get("message") or body.get("statusText") or response.text
            except ValueError:
                body = None
                message = response.text
            raise ZokoError(response.status_code, message, body)

        # 204 No Content (and empty bodies) have nothing to parse.
        if response.status_code == 204 or not response.content:
            return None
        return response.json()
