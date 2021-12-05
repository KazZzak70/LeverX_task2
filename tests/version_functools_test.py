from exceptions import VersionError
from unittest.mock import patch
import unittest
import version_functools


class TestVersionFunc(unittest.TestCase):

    @patch("version_functools.reformat")
    def test_to_list(self, mock_reformat):
        mock_reformat.return_value = "4.3.2.rc.1"
        expected_result = ["4", "3", "2", "rc", "1"]
        received_result = version_functools.to_list("4.3.2.rc.1")
        self.assertEqual(expected_result, received_result)

    def test_to_list_exception(self):
        with self.assertRaises(expected_exception=VersionError):
            version_functools.to_list(version=None)

    def test_equalize_lengths(self):
        input_data = [["a", "b", "c"], ["1"]]
        expected_result = [["a", "b", "c"], ["1", "_", "_"]]
        received_result = list(version_functools.equalize_lengths(*input_data))
        self.assertEqual(expected_result, received_result)

    def test_reformat(self):
        input_str = "4.3.2rc1"
        expected_result = "4.3.2.rc.1"
        received_result = version_functools.reformat(version=input_str)
        self.assertEqual(expected_result, received_result)
