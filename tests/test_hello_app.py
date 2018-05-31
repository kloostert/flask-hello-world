import unittest

from app import app


class HelloTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        assert b'Hello' in rv.data

    def test_delayed_hello(self):
        rv = self.app.get('/test')
        assert b'Delay' in rv.data

    def test_both(self):
        rv = self.app.get('/')
        assert b'Hello' in rv.data
        rv = self.app.get('/test')
        assert b'Delay' in rv.data
        rv = self.app.get('/')
        assert b'Hello' in rv.data


if __name__ == '__main__':
    unittest.main()
