from exceptions import ComparisonError
from version import Version
import unittest


class TestVersion(unittest.TestCase):

    def test_case_1(self):
        version_1 = Version(version="1.0.0")
        version_2 = Version(version="2.0.0")
        expected_result = True
        received_result = version_1 < version_2
        self.assertEqual(expected_result, received_result)

    def test_case_2(self):
        version_1 = Version(version="1.0.0")
        version_2 = Version(version="1.42.0")
        expected_result = True
        received_result = version_1 < version_2
        self.assertEqual(expected_result, received_result)

    def test_case_3(self):
        version_1 = Version(version="1.2.0")
        version_2 = Version(version="1.2.42")
        expected_result = True
        received_result = version_1 < version_2
        self.assertEqual(expected_result, received_result)

    def test_case_4(self):
        version_1 = Version(version="1.1.0-alpha")
        version_2 = Version(version="1.2.0-alpha.1")
        expected_result = True
        received_result = version_1 < version_2
        self.assertEqual(expected_result, received_result)

    def test_case_5(self):
        version_1 = Version(version="1.0.1b")
        version_2 = Version(version="1.0.10-alpha.beta")
        expected_result = True
        received_result = version_1 < version_2
        self.assertEqual(expected_result, received_result)

    def test_case_6(self):
        version_1 = Version(version="1.0.0-rc.1")
        version_2 = Version(version="1.0.0")
        expected_result = False
        received_result = version_1 < version_2
        self.assertEqual(expected_result, received_result)

    def test_case_lt_exception(self):
        version_1 = Version(version="1.0.0")
        version_2 = "2.0.0"
        with self.assertRaises(expected_exception=ComparisonError):
            version_1 < version_2

    def test_case_eq_exception(self):
        version_1 = Version(version="1.0.0")
        version_2 = "1.0.0"
        with self.assertRaises(expected_exception=ComparisonError):
            version_1 == version_2

    def test_eq_comparison(self):
        version_1 = Version(version="1.0.0-rc.1")
        version_2 = Version(version="1.0.0")
        expected_result = False
        received_result = version_1 == version_2
        self.assertEqual(expected_result, received_result)

    def test_key_error_exception(self):
        version_1 = Version(version="1.0.0-trash.1")
        version_2 = Version(version="1.0.0")
        expected_result = False
        received_result = version_1 < version_2
        self.assertEqual(expected_result, received_result)
