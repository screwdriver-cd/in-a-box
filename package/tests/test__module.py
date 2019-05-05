import os
import unittest
from vcr_unittest import VCRTestCase


class TestInABoxModule(VCRTestCase):
    def setUp(self):
        self._docker_host = os.environ.get('DOCKER_HOST', None)
        if self._docker_host:
            del os.environ['DOCKER_HOST']

    def tearDown(self):
        if os.environ.get('DOCKER_HOST', None):
            del os.environ['DOCKER_HOST']
        if self._docker_host:
            os.environ['DOCKER_HOST'] = self._docker_host

    def test_import(self):
        import screwdriver_cd_setup

    def test__get_ip_address__docker_host(self):
        import screwdriver_cd_setup
        os.environ['DOCKER_HOST'] = 'tcp://foo.bar.com:2375'
        self.assertEqual(screwdriver_cd_setup.get_ip_address(), 'foo.bar.com')

    def test__get_ip_address__no_docker_host(self):
        import screwdriver_cd_setup
        result = screwdriver_cd_setup.get_ip_address()
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
