import json
import unittest

import httpretty

from zoko import ZokoClient, ZokoError
from zoko.constants.endpoint import MessageEndpoint


def _send(zoko):
    return zoko.message.send_message(
        recipient="919998880000", template_type="text", message="hi"
    )


class TestZokoClientRetry(unittest.TestCase):
    def setUp(self):
        httpretty.enable(verbose=True, allow_net_connect=False)

    def tearDown(self):
        httpretty.disable()
        httpretty.reset()

    def _register(self, statuses):
        """Register SEND to return the given status sequence, counting calls.

        The last status repeats once the sequence is exhausted.
        """
        calls = []

        def callback(request, uri, response_headers):
            idx = min(len(calls), len(statuses) - 1)
            calls.append(request)
            status = statuses[idx]
            body = json.dumps({"status": str(status)})
            return [status, response_headers, body]

        httpretty.register_uri(
            httpretty.POST,
            MessageEndpoint.SEND,
            body=callback,
            content_type="application/json",
        )
        return calls

    def test_retries_on_5xx_then_succeeds(self):
        # backoff_factor=0 so the test doesn't actually sleep.
        zoko = ZokoClient(api_key="k", max_retries=2, backoff_factor=0)
        calls = self._register([503, 200])
        result = _send(zoko)
        self.assertEqual(result, {"status": "200"})
        self.assertEqual(len(calls), 2)  # 1 failed + 1 successful

    def test_raises_after_exhausting_retries(self):
        zoko = ZokoClient(api_key="k", max_retries=1, backoff_factor=0)
        calls = self._register([500])
        with self.assertRaises(ZokoError) as ctx:
            _send(zoko)
        self.assertEqual(ctx.exception.status_code, 500)
        self.assertEqual(len(calls), 2)  # initial attempt + 1 retry

    def test_no_retry_by_default(self):
        zoko = ZokoClient(api_key="k")
        calls = self._register([503])
        with self.assertRaises(ZokoError):
            _send(zoko)
        self.assertEqual(len(calls), 1)


if __name__ == "__main__":
    unittest.main()
