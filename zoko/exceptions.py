class ZokoError(Exception):
    """Raised when the Zoko API returns a non-2xx response."""

    def __init__(self, status_code, message, response=None):
        self.status_code = status_code
        self.response = response
        super().__init__(f"Zoko API error {status_code}: {message}")
