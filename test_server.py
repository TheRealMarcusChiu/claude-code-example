import threading
import unittest
from http.server import HTTPServer
from urllib.request import urlopen
from urllib.error import URLError

from server import PlainTextHandler


class TestPlainTextHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Bind to port 0 so the OS assigns an ephemeral port.
        cls.server = HTTPServer(("localhost", 0), PlainTextHandler)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever)
        cls.thread.daemon = True
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.thread.join()

    def _get(self):
        url = f"http://localhost:{self.port}/"
        with urlopen(url) as response:
            return response

    def test_status_200(self):
        url = f"http://localhost:{self.port}/"
        with urlopen(url) as response:
            self.assertEqual(response.status, 200)

    def test_body_is_hello_world(self):
        url = f"http://localhost:{self.port}/"
        with urlopen(url) as response:
            body = response.read()
        self.assertEqual(body, b"Hello, world!")

    def test_content_type_is_text_plain(self):
        url = f"http://localhost:{self.port}/"
        with urlopen(url) as response:
            content_type = response.headers.get("Content-Type")
        self.assertEqual(content_type, "text/plain")

    def test_content_length_matches_body(self):
        url = f"http://localhost:{self.port}/"
        with urlopen(url) as response:
            content_length = int(response.headers.get("Content-Length"))
            body = response.read()
        self.assertEqual(content_length, len(body))


if __name__ == "__main__":
    unittest.main()
